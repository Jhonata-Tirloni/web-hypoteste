"""import dos módulos para calculo do valro T, graus de liberdade e raiz quadrada"""
from scipy import stats
from numpy import sqrt

def teste_duas_amostras_pareadas(variancia_amostra, estat_amostra,
                                 tamanho_amostra, parametro_pop,
                                 teste_bilateral, teste_esquerda, teste_direita) -> float:
    """
    Definição: Um teste de amostras duplas e pareadas é um tipo de teste estatístico 
    usado para comparar as médias de duas amostras pareadas, 
    onde cada observação em uma amostra está relacionada a uma observação na outra . 
    Esse tipo de teste é frequentemente utilizado em estudos onde os mesmos indivíduos 
    são medidos antes e depois de uma intervenção ou tratamento.
    """

    graus_de_liberdade = tamanho_amostra-1
    alpha = 0.05
    alpha_unicaudal = stats.t.ppf(1-alpha, df=graus_de_liberdade)
    alpha_bicaudal = stats.t.ppf(1-alpha/2, df=graus_de_liberdade)

    try:
        if (teste_bilateral is True or teste_esquerda is True or teste_direita is True )\
            and (tamanho_amostra != '' and estat_amostra != '' and parametro_pop != '' and variancia_amostra != ''):

            t = estat_amostra/(variancia_amostra/sqrt(tamanho_amostra))
            p_valor_bicaudal = 2*(1-stats.t.cdf(abs(t), df=graus_de_liberdade))
            p_valor_unicaudal = 1-stats.t.cdf(abs(t), df=graus_de_liberdade)

            return t, p_valor_bicaudal, p_valor_unicaudal, alpha_unicaudal, alpha_bicaudal
    except Exception as e:
        return e
