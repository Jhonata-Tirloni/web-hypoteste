from scipy import stats
from numpy import sqrt
from streamlit import error

def teste_duas_amostras_independentes(variancia_amostra_um:float, variancia_amostra_dois:float,
                                      tamanho_amostra_um:int, tamanho_amostra_dois:int,
                                      estat_amostra_um:float, estat_amostra_dois:float,
                                      teste_bilateral:bool, teste_esquerda:bool, teste_direita:bool) -> float:
    """
    Para este teste considera-se que as variâncias das duas amostras são diferentes.
    Um teste de amostras duplas e independentes é um tipo de teste estatístico usado para 
    comparar as médias de duas amostras independentes provenientes de duas populações diferentes. 
    Isso é feito para determinar se as médias das duas populações são estatisticamente 
    diferentes uma da outra.

    Alpha = 0.05
    Graus de liberdade: Fórmula de Welch
    T crítico: stats.t.ppf
    """

    graus_de_liberdade = ((variancia_amostra_um**2 / tamanho_amostra_um)
                        + (variancia_amostra_dois**2 / tamanho_amostra_dois))**2 \
                        / (((variancia_amostra_um**2 / tamanho_amostra_um)**2 \
                            / (tamanho_amostra_um - 1))
                           + ((variancia_amostra_dois**2 / tamanho_amostra_dois)**2\
                              / (tamanho_amostra_dois - 1)))
    alpha = 0.05

    # Valor T
    alpha_bicaudal = stats.t.ppf(1 - alpha/2, df=graus_de_liberdade)
    alpha_unicaudal = stats.t.ppf(1 - alpha, df=graus_de_liberdade)

    try:
        if (teste_bilateral is True or teste_esquerda is True or teste_direita is True )\
            and (tamanho_amostra_um != '' and tamanho_amostra_dois != '' and\
                  variancia_amostra_um != '' and variancia_amostra_dois != '' and\
                      estat_amostra_um != '' and estat_amostra_dois != ''):

            t = (estat_amostra_um-estat_amostra_dois)/sqrt((variancia_amostra_um/tamanho_amostra_um)
                                                           +(variancia_amostra_dois/tamanho_amostra_dois))

            p_valor_bicaudal = 2 * (1 - stats.t.cdf(abs(t), df=graus_de_liberdade))

            p_valor_unicaudal = (1 - stats.t.cdf(abs(t), df=graus_de_liberdade))

        return t, p_valor_bicaudal, p_valor_unicaudal, alpha_unicaudal, alpha_bicaudal, graus_de_liberdade

    except Exception as e:
        return error(str(e)+". Porfavor, tente novamente!", icon="🚨")
