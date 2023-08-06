import collections

import numpy as np
from numba import njit
from scipy import stats


# convert bnlearn format to my format
def from_bnlearn(dag):
    dag = dag[1: len(dag) - 1]
    output = {}
    for node in dag.split(']['):
        if '|' not in node:
            output[node] = {'par': [], 'nei': []}
        else:
            output[node.split('|')[0]] = {'par': node.split('|')[1].split(':'), 'nei': []}
    return output


def score(dag, data, score_function='bic'):
    if type(dag) is str:
        dag = from_bnlearn(dag)
    elif type(dag) is not dict:
        raise Exception('The format of input true DAG is invalid.')
    varnames = list(data)
    if all(data[var].dtype.name == 'category' for var in data):
        data = data.apply(lambda x: x.cat.codes).to_numpy()
    elif all(data[var].dtype.name != 'category' for var in data):
        data = data.to_numpy()
    else:
        raise Exception('Mixed data is not supported.')

    sco = 0
    for var in varnames:
        cols = [varnames.index(v) for v in [var] + dag[var]['par']]
        sco += local_score(data, cols, score_function)
    return sco


def bic(data, cols, weight=None):
    arities = np.amax(data, axis=0) + 1
    return bic_counter(data, arities, cols, weight)


@njit(fastmath=True)
def bic_counter(data, arities, cols, weight=None):
    if weight is None:
        weight = np.ones(data.shape[0])
    strides = np.empty(len(cols), dtype=np.uint32)
    idx = len(cols) - 1
    stride = 1
    while idx > -1:
        strides[idx] = stride
        stride *= arities[cols[idx]]
        idx -= 1
    N_ijk = np.zeros(stride)
    N_ij = np.zeros(stride)
    for rowidx in range(data.shape[0]):
        idx_ijk = 0
        idx_ij = 0
        for i in range(len(cols)):
            idx_ijk += data[rowidx, cols[i]] * strides[i]
            if i != 0:
                idx_ij += data[rowidx, cols[i]] * strides[i]
        N_ijk[idx_ijk] += weight[rowidx]
        for i in range(arities[cols[0]]):
            N_ij[idx_ij + i * strides[0]] += weight[rowidx]
    bic = 0
    for i in range(stride):
        if N_ijk[i] != 0:
            bic += N_ijk[i] * np.log(N_ijk[i] / N_ij[i])
    bic -= 0.5 * np.log(data.shape[0]) * (arities[cols[0]] - 1) * strides[0]
    return bic


def nal(data, cols, alpha=0.3):
    arities = np.amax(data, axis=0) + 1
    data_local = np.delete(data, data[:, cols].min(axis=1) < 0, axis=0)
    if data_local.shape[0] == 0:
        return -np.inf
    else:
        return nal_counter(data_local, arities, cols,
                           weight=np.ones(data_local.shape[0]) * data.shape[0] / data_local.shape[0], alpha=alpha)


def nal_vn(data, cols, alpha=0.4):
    arities = np.amax(data, axis=0) + 1
    data_local = np.delete(data, data[:, cols].min(axis=1) < 0, axis=0)
    if data_local.shape[0] == 0:
        return -np.inf
    else:
        return nal_counter(data_local, arities, cols, alpha=alpha)


def nal_va(data, cols, alpha=0.3):
    arities = np.amax(data, axis=0) + 1
    data_local = np.delete(data, data[:, cols].min(axis=1) < 0, axis=0)
    alpha = 0.3 + data_local.shape[0] / data.shape[0] / 10
    if data_local.shape[0] == 0:
        return -np.inf
    else:
        return nal_counter(data_local, arities, cols,
                           np.ones(data_local.shape[0]) * data.shape[0] / data_local.shape[0], alpha)


def nal_ipw(data, cols, weight):
    arities = np.amax(data, axis=0) + 1
    alpha = 0.3 + data.shape[0] / sum(weight) / 10
    if data.shape[0] == 0:
        return -np.inf
    else:
        return nal_counter(data, arities, cols, weight, alpha)


def nal_sev(data, cols, cols_rvs):
    arities = np.amax(data, axis=0) + 1
    data = np.delete(data, data[:, cols_rvs].min(axis=1) < 0, axis=0)
    return nal_counter(data, arities, cols, samplesize=data.shape[0])


@njit(fastmath=True)
def nal_counter(data, arities, cols, weight=None, alpha=0.3):
    if weight is None:
        weight = np.ones(data.shape[0])
    strides = np.empty(len(cols), dtype=np.uint32)
    idx = len(cols) - 1
    stride = 1
    while idx > -1:
        strides[idx] = stride
        stride *= arities[cols[idx]]
        idx -= 1
    N_ijk = np.zeros(stride)
    N_ij = np.zeros(stride)
    for rowidx in range(data.shape[0]):
        idx_ijk = 0
        idx_ij = 0
        miss_flag = False
        for i in range(len(cols)):
            if data[rowidx, cols[i]] == -1:
                miss_flag = True
                break
            else:
                idx_ijk += data[rowidx, cols[i]] * strides[i]
                if i != 0:
                    idx_ij += data[rowidx, cols[i]] * strides[i]
        if not miss_flag:
            N_ijk[idx_ijk] += weight[rowidx]
            for i in range(arities[cols[0]]):
                N_ij[idx_ij + i * strides[0]] += weight[rowidx]
    nal = 0
    for i in range(stride):
        if N_ijk[i] != 0:
            nal += N_ijk[i] * np.log(N_ijk[i] / N_ij[i])
    nal /= np.sum(N_ijk)
    if alpha == 1:
        nal -= 0.5 * np.log(np.sum(weight)) / np.sum(weight) * (arities[cols[0]] - 1) * strides[0]
    else:
        nal -= 1 / data.shape[1] * np.power(np.sum(weight), -alpha) * (arities[cols[0]] - 1) * strides[0]
    return nal


def bic_g(data, cols, weights=None):
    X = data[:, cols[1:]]
    y = data[:, cols[0]]
    X = np.hstack((np.ones(len(y)).reshape(len(y), 1), X))
    if len(y) <= X.shape[1]:
        bic = np.nan
    else:
        b = np.linalg.inv(X.T @ X) @ X.T @ y
        ssr = np.sum((y - X @ b) ** 2)
        df = X.shape[0] - X.shape[1]
        bic = - X.shape[0] / 2 * np.log(2 * np.pi * ssr / df) - df / 2 - np.log(X.shape[0]) / 2 * (1 + X.shape[1])
    return bic


# compute weights of data with missing values
def compute_weights(data, varnames, W_ids, cause_list):
    if 'int' in data.dtype.name:
        data_delete = data[(data[:, W_ids].min(axis=1) >= 0) & (data[:, W_ids].max(axis=1) != np.iinfo(data.dtype).max)]
    else:
        data_delete = data[~np.isnan(data[:, W_ids]).any(axis=1)]
    weights = np.ones(len(data_delete))
    for ri in [varnames[i] for i in W_ids]:
        cause = cause_list[ri]
        if len(cause) > 0:
            cause_id = [i for i in range(len(varnames)) if varnames[i] in cause]
            data_beta = data[:, cause_id]
            if 'int' in data.dtype.name:
                numerator = data_beta[
                    (data_beta.min(axis=1) >= 0) & (data_beta.max(axis=1) != np.iinfo(data.dtype).max)]
                denominator = data_beta[
                    (data_beta.min(axis=1) >= 0) & (data_beta.max(axis=1) != np.iinfo(data.dtype).max) & (
                            data[:, varnames.index(ri)] >= 0)]
                arities = np.amax(numerator, axis=0) + 1
                f_w = density_counter(numerator, arities).reshape(arities)
                f_wr = density_counter(denominator, arities).reshape(arities)
                weights *= np.array([f_w[tuple(data_delete[i, cause_id])] for i in range(len(data_delete))]) / np.array(
                    [f_wr[tuple(data_delete[i, cause_id])] for i in range(len(data_delete))])
            else:
                numerator = data_beta[~np.isnan(data_beta).any(axis=1)].T
                denominator = data_beta[(~np.isnan(data_beta).any(axis=1)) & (~np.isnan(data[:, varnames.index(ri)]))].T
                f_w = stats.gaussian_kde(numerator)
                f_wr = stats.gaussian_kde(denominator)
                weights *= f_w(data_delete[:, cause_id].T) / f_wr(data_delete[:, cause_id].T)
    return weights * len(weights) / weights.sum()


@njit(fastmath=True)
def density_counter(data, arities):
    strides = np.empty(data.shape[1], dtype=np.uint32)
    idx = data.shape[1] - 1
    stride = 1
    while idx > -1:
        strides[idx] = stride
        stride *= arities[idx]
        idx -= 1
    CT = np.zeros(stride)
    for rowidx in range(data.shape[0]):
        idx = 0
        for i in range(data.shape[1]):
            idx += data[rowidx, i] * strides[i]
        CT[idx] += 1

    CT /= np.sum(CT)
    return CT


def local_score(data, cols, score_function='default', weights=None, alpha=0.4):
    '''
    :param weights: weight for data
    :param data: numbered version of data set
    :param cols: the index of node and its parents, the first element represents the index of the node and the following elements represent the indices of its parents
    :param score_function: name of score function, currently support bic, nal, bic_g
    :return: local score of node (cols[0]) given its parents (cols[1:])
    '''
    if len(data) == 0:
        return np.nan
    else:
        if score_function == 'default':
            score_function = 'bic' if 'int' in data.dtype.name else 'bic_g'
        try:
            if score_function in ['nal', 'nal_va', 'nal_vn']:
                ls = globals()[score_function](data, np.asarray(cols), alpha=alpha)
            else:
                ls = globals()[score_function](data, np.asarray(cols), weights)
        except Exception as e:
            raise Exception('score function ' + str(
                e) + ' is undefined or does not fit to data type. Available score functions are: bic (BIC for discrete variables) and nal (NAL for discrete variables).')
        return ls
