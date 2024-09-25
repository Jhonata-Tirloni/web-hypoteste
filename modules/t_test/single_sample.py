"""import dos módulos para calculo do valro T, graus de liberdade e raiz quadrada"""
from scipy import stats
from numpy import sqrt

def teste_amostra_unica(variancia_amostral:float, tamanho_amostra:int, estat_amostra:float,
                        parametro_pop:float, teste_bilateral:bool,
                        teste_esquerda:bool, teste_direita:bool) -> float:
    """
    Um teste de amostra única é um tipo de teste estatístico usado para verificar uma 
    afirmação sobre a média de uma população, quando apenas uma amostra dessa 
    população está disponível.
    O cálculo de graus de liberdade necessários é realizado dentro desta
    função.
    
    Alpha = 0.05
    Graus de liberdade: n-1
    T crítico: stats.t.ppf
    """
    graus_de_liberdade = tamanho_amostra-1
    alpha = 0.05
    alpha_unicaudal = stats.t.ppf(1-alpha, df=graus_de_liberdade)
    alpha_bicaudal = stats.t.ppf(1-alpha/2, df=graus_de_liberdade)

    try:
        if (teste_bilateral is True or teste_esquerda is True or teste_direita is True )\
            and (tamanho_amostra != '' and estat_amostra != '' and parametro_pop != '' and variancia_amostral != ''):

            t = (float(estat_amostra) - float(parametro_pop))/(float(variancia_amostral)/sqrt(float(tamanho_amostra)))
            p_valor_bicaudal = 2*(1-stats.t.cdf(abs(t), df=graus_de_liberdade))
            p_valor_unicaudal = 1-stats.t.cdf(abs(t), df=graus_de_liberdade)

        return t, p_valor_bicaudal, p_valor_unicaudal, alpha_unicaudal, alpha_bicaudal

    except Exception as e:
        return e
