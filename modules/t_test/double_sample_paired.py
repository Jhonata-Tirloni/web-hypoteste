
def teste_duas_amostras_pareadas() -> float:
    """
    Definição: Um teste de amostras duplas e pareadas é um tipo de teste estatístico usado para comparar as médias de duas amostras pareadas, onde cada observação em uma amostra está relacionada a uma observação na outra . Esse tipo de teste é frequentemente utilizado em estudos onde os mesmos indivíduos são medidos antes e depois de uma intervenção ou tratamento.

    d_barra é a média das diferenças entre as observações pareadas,
    S_d é o desvio padrão das diferenças entre as observações pareadas,
    n é o número de pares de observações.

    Variáveis: Os valores que a função trabalha incluem:
    - S_value: Variância da amostra populacional (para o caso de variância conhecida).
    - n: Tamanho da amostra.
    - xis_barra: Estatística da amostra (média da amostra).
    - mu: Parâmetro populacional (hipótese nula).
    - alpha_unicaudal (1.725) e alpha_bicaudal (2.086): Valores t críticos para um determinado nível de significância e graus de liberdade.
    - S: Indicação de se a variância é conhecida ou não.
    Para o teste de amostras duplas e pareadas, os graus de liberdade são calculados como n - 1, onde n é o número de pares de observações.

    Retorno: Valor calculado t como um número de ponto flutuante (float).
    """

    S_value = float(txt_variancia_amostra_pop.value)
    n = int(txt_tamanho_amostra.value)
    xis_barra = float(txt_estat_amostra.value)
    mu = float(txt_parametro_pop.value)
    graus_de_liberdade = n-1 
    alpha = 0.05
    alpha_unicaudal = stats.t.ppf(1-alpha, df=graus_de_liberdade)
    alpha_bicaudal = stats.t.ppf(1-alpha/2, df=graus_de_liberdade)

    try:
        if (btn_teste_bilateral.value == True or btn_teste_esquerda.value == True or btn_teste_direita.value == True )\
            and (n != '' and xis_barra != '' and mu != '' and S_value != ''):
            
            t = xis_barra/(S_value/sqrt(n))
            p_valor_bicaudal = 2*(1-stats.t.cdf(abs(t), df=graus_de_liberdade))
            p_valor_unicaudal = 1-stats.t.cdf(abs(t), df=graus_de_liberdade)
            output.clear_output()

            with output:
                df = 20
                x = linspace(-4, 4, 1000)
                pdf = dist_t.pdf(x, df)
                plot = plt.plot(x, pdf)

                # Testes bilaterais
                if btn_teste_bilateral.value == True and t > 0 and t <= alpha_bicaudal:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {alpha_bicaudal*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor P do teste: {p_valor_bicaudal}")
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
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {alpha_bicaudal*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor P do teste: {p_valor_bicaudal}")
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

                elif btn_teste_bilateral.value == True and t < 0 and t <= alpha_bicaudal*-1:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {alpha_bicaudal*-1}")
                    print(f"Valor T do teste: {t}")
                    print(f"Valor P do teste: {p_valor_bicaudal}")
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
                    
                elif btn_teste_bilateral.value == True and t < 0 and t > alpha_bicaudal*-1:
                    print(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal} e negativo temos {alpha_bicaudal*-1}")
                    print(f"Valor T do teste:{t}")
                    print(f"Valor P do teste: {p_valor_bicaudal}")
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
                    print(f"Valor P do teste: {p_valor_unicaudal}")
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
                    print(f"Valor P do teste: {p_valor_unicaudal}")
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
                    print(f"Valor P do teste: {p_valor_unicaudal}")
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
                    print(f"Valor P do teste: {p_valor_unicaudal}")
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
                print('Erro: Por favor, verifique se não esqueceu de preencher alguma etapa, e tente novamente!')
            btn_realizar_teste.value=None
    except Exception as e:
        output.clear_output()
        with output:
            print(e)
        btn_realizar_teste.value=None

    return
