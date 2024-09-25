"""import dos módulos para calculo do valro T, graus de liberdade e raiz quadrada"""
from scipy import stats
from numpy import sqrt

def teste_duas_amostras_independentes(variancia_amostra_um, variancia_amostra_dois, 
                                      tamanho_amostra_um, tamanho_amostra_dois,
                                      estat_amostra_um, estat_amostra_dois) -> float:
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

    s1_value = float(txt_variancia_amostra_pop.value)
    s2_value = float(txt_variancia_amostra_pop_dois.value)
    n1 = int(txt_tamanho_amostra.value)
    n2 = int(txt_tamanho_amostra_dois.value)
    xis_barra1 = float(txt_estat_amostra.value)
    xis_barra2 = float(txt_parametro_pop.value)
    graus_de_liberdade = ((s1_value**2 / n1) \
                        + (s2_value**2 / n2))**2 / (((s1_value**2 / n1)**2 / (n1 - 1)) \
                        + ((s2_value**2 / n2)**2 / (n2 - 1)))
    alpha = 0.05

    # Valor T
    alpha_bicaudal = stats.t.ppf(1 - alpha/2, df=graus_de_liberdade)
    alpha_unicaudal = stats.t.ppf(1 - alpha, df=graus_de_liberdade)

    try:
        if (btn_teste_bilateral.value == True or btn_teste_esquerda == True or btn_teste_direita == True )\
            and (n1 != '' and n2 != '' and s1_value != '' and s1_value != '' and xis_barra1 != '' and xis_barra2 != ''):
            
            t = (xis_barra1-xis_barra2)/sqrt((s1_value/n1)+(s2_value/n1))
            p_valor = 2 * (1 - stats.t.cdf(abs(t), df=graus_de_liberdade))
            p_valor_unicaudal = (1 - stats.t.cdf(abs(t), df=graus_de_liberdade))

            output.clear_output()

            with output:
                # Testes bilaterais
                df = 20
                x = linspace(-4, 4, 1000)
                pdf = dist_t.pdf(x, df)
                plot = plt.plot(x, pdf)

                print('Realizando teste..')
                if btn_teste_bilateral.value == True and t > 0 and t <= alpha_bicaudal:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {(alpha_bicaudal)*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor}")
                    print("Valor T menor do que o valor alpha tabelado.")
                    print("Recomendação: Não rejeitar a hipótese nula, e desfavorecer a hipótese alternativa. ")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x1_fill = linspace(-4, alpha_bicaudal*-1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(x1_fill, 0, dist_t.pdf(x1_fill, df), color='red', alpha=0.3)
                    plt.fill_between(x2_fill, 0, dist_t.pdf(x2_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--', label='Resultado do teste')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    plt.show(plot)
                    
                elif btn_teste_bilateral.value == True and t > 0 and t > alpha_bicaudal:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {(alpha_bicaudal)*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor}")
                    print("Valor T maior do que o valor alpha tabelado.")
                    print("Recomendação: Rejeitar a hipótese nula, e favorecer a hipótese alternativa.")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x1_fill = linspace(-4, alpha_bicaudal*-1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(x1_fill, 0, dist_t.pdf(x1_fill, df), color='red', alpha=0.3)
                    plt.fill_between(x2_fill, 0, dist_t.pdf(x2_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--', label='Resultado do teste')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    plt.show(plot)

                elif btn_teste_bilateral.value == True and t < 0 and t <= (alpha_bicaudal)*-1:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {(alpha_bicaudal)*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor}")
                    print("Valor T menor do que o valor alpha tabelado.")
                    print("Recomendação: Não rejeitar a hipótese nula, e desfavorecer a hipótese alternativa. ")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x1_fill = linspace(-4, alpha_bicaudal*-1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(x1_fill, 0, dist_t.pdf(x1_fill, df), color='red', alpha=0.3)
                    plt.fill_between(x2_fill, 0, dist_t.pdf(x2_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.show(plot)
                    
                elif btn_teste_bilateral.value == True and t < 0 and t > (alpha_bicaudal)*-1:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {(alpha_bicaudal)*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor}")
                    print("Valor T maior do que o valor alpha tabelado.")
                    print("Recomendação: Rejeitar a hipótese nula, e favorecer a hipótese alternativa.")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x1_fill = linspace(-4, alpha_bicaudal*-1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(x1_fill, 0, dist_t.pdf(x1_fill, df), color='red', alpha=0.3)
                    plt.fill_between(x2_fill, 0, dist_t.pdf(x2_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.show(plot)
                
                # Testes unilaterais a esquerda
                elif btn_teste_esquerda.value == True and t < 0 and t <= (alpha_unicaudal)*-1:
                    print(f"Valor T tabelado: Para resultado negativo temos {(alpha_unicaudal)*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor_unicaudal}")
                    print("Valor T menor do que o valor alpha tabelado.")
                    print("Recomendação: Não rejeitar a hipótese nula, e desfavorecer a hipótese alternativa. ")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x1_fill = linspace(-4, alpha_unicaudal*-1, 1000)
                    plt.fill_between(x1_fill, 0, dist_t.pdf(x1_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.show(plot)
                    
                elif btn_teste_esquerda.value == True and t < 0 and t > (alpha_unicaudal)*-1:
                    print(f"Valor T tabelado: Para resultado negativo temos {(alpha_unicaudal)*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor_unicaudal}")
                    print("Valor T maior do que o valor alpha tabelado.")
                    print("Recomendação: Rejeitar a hipótese nula, e favorecer a hipótese alternativa.")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x1_fill = linspace(-4, alpha_unicaudal*-1, 1000)
                    plt.fill_between(x1_fill, 0, dist_t.pdf(x1_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.show(plot)

                # Testes unilaterais a direita
                elif btn_teste_direita.value == True and t > 0 and t <= alpha_unicaudal:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_unicaudal}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor_unicaudal}")
                    print("Valor T menor do que o valor alpha tabelado.")
                    print("Recomendação: Não rejeitar a hipótese nula, e desfavorecer a hipótese alternativa. ")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x2_fill = linspace(4, alpha_unicaudal, 1000)
                    plt.fill_between(x2_fill, 0, dist_t.pdf(x2_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--', label='Resultado do teste')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    plt.show(plot)
                    
                elif btn_teste_direita.value == True and t > 0 and t > alpha_unicaudal:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_unicaudal}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor p do teste: {p_valor_unicaudal}")
                    print("Valor T maior do que o valor alpha tabelado.")
                    print("Recomendação: Rejeitar a hipótese nula, e favorecer a hipótese alternativa.")
                    print("O gráfico abaixo demonstra a distribuição T, os valores críticos em vermelho e o resultado do teste na linha preta.")
                    x2_fill = linspace(4, alpha_unicaudal, 1000)
                    plt.fill_between(x2_fill, 0, dist_t.pdf(x2_fill, df), color='red', alpha=0.3)
                    plt.axvline(x=(lambda t:-4 if t < -4 else(4 if t > 4 else t))(t), color='black', linestyle='--', label='Resultado do teste')
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    plt.show(plot)

            btn_realizar_teste.value=None
        else:
            output.clear_output()
            with output:
                print('Erro: Por favor, verifique se não esqueceu de preencher alguma etapa e tente novamente!')
            btn_realizar_teste.value=None
    except Exception as e:
        output.clear_output()
        with output:
            print(e)
        btn_realizar_teste.value=None

    return