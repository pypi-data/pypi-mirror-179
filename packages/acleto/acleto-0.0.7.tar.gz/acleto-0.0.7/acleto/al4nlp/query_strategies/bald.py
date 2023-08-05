import logging
from typing import Union

import numpy as np
from datasets.arrow_dataset import Dataset

from .al_strategy_utils import (
    assign_ue_scores_for_unlabeled_data,
    calculate_bald_score_cls,
    calculate_bald_score_ner,
    get_query_idx_for_selecting_by_number_of_tokens,
    get_X_pool_subsample
)
from .strategy_utils.batchbald.consistent_dropout import make_dropouts_consistent
from ..utils.transformers_dataset import TransformersDataset

log = logging.getLogger()


def bald(
    model,
    X_pool: Union[np.ndarray, Dataset, TransformersDataset],
    n_instances: int,
    select_by_number_of_tokens: bool = False,
    **bald_kwargs,
):
    """
    BALD is based on mutual information and scores points based on how well their label
    would inform us about the true model parameter distribution.
    https://arxiv.org/abs/1112.5745
    """
    mc_iterations = bald_kwargs.get("mc_iterations", 10)
    use_stable_dropout = bald_kwargs.get("use_stable_dropout", True)
    use_subsample = bald_kwargs.get("use_subsample", False)

    if use_subsample:
        X_pool_subsample, subsample_indices = get_X_pool_subsample(
            X_pool, mc_iterations, model.seed
        )
    else:
        X_pool_subsample = X_pool

    # Make dropout consistent inside huggingface model
    if use_stable_dropout:
        make_dropouts_consistent(model.model)
    else:
        model.enable_dropout()

    if bald_kwargs.get("only_head_dropout", False):
        raise NotImplementedError
    else:
        # Stable dropout
        probas = []
        for _ in range(mc_iterations):
            if use_stable_dropout:
                # Reset masks
                model.enable_dropout()
                model.disable_dropout()
            probas_iter = model.predict_proba(
                X_pool_subsample, use_predict_loop=True, to_eval_mode=False
            )
            probas.append(probas_iter)

    if model.task == "cls":
        probas_N_K_C = np.stack(probas, -2)
        uncertainty_estimates = calculate_bald_score_cls(probas_N_K_C)
    elif model.task == "ner":
        uncertainty_estimates = calculate_bald_score_ner(probas)
    # The larger the score, the more confident the model is
    argsort = np.argsort(-uncertainty_estimates)

    if select_by_number_of_tokens:
        query_idx = get_query_idx_for_selecting_by_number_of_tokens(
            X_pool_subsample,
            argsort,
            n_instances,
            tokens_column_name=model.data_config["text_name"],
        )
    else:
        query_idx = argsort[:n_instances]

    query = X_pool_subsample.select(query_idx)
    if use_subsample:
        # Update query_idx since now it corresponds to the sampled set
        query_idx = subsample_indices[query_idx]
        uncertainty_estimates = assign_ue_scores_for_unlabeled_data(
            len(X_pool), subsample_indices, uncertainty_estimates
        )

    return query_idx, query, uncertainty_estimates
