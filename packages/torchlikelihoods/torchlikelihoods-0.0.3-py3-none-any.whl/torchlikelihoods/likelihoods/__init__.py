from .beta import BetaLikelihood
from .bernoulli import BernoulliLikelihood
from .continous_bernoulli import ContinousBernoulliLikelihood
from .categorical import CategoricalLikelihood
from .normal import NormalLikelihood
from .normal_mean import NormalMeanLikelihood
from .heterogeneous import HeterogeneousLikelihood

likelihood_dict = {
    'beta': BetaLikelihood,
    'ber': BernoulliLikelihood,
    'cb': ContinousBernoulliLikelihood,
    'cat': CategoricalLikelihood,
    'normal': NormalLikelihood,
    'normal1': NormalMeanLikelihood.create(1),
    'normal01': NormalMeanLikelihood.create(0.01),
    'normal001': NormalMeanLikelihood.create(0.001),
    'normal0001': NormalMeanLikelihood.create(0.0001),
    'het': HeterogeneousLikelihood
}


def build_likelihoods_list(lik_info_list):
    likelihoods = []
    for (lik_name_i, domain_size_i) in lik_info_list:
        lik = likelihood_dict[lik_name_i](domain_size_i)
        likelihoods.append(lik)
    return likelihoods
