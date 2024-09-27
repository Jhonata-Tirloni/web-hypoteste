import matplotlib.pyplot as plt
import streamlit as st
from numpy import linspace
from scipy.stats import t as dist_t
from modules.t_test.single_sample import teste_amostra_unica

@st.dialog("Sobre testes de hipótese", width='large')
def modal_sobre_teste():
    """
        Renderiza um modal com informações sobre teste
        de hipótese e cases de uso
    """
    st.header("O que é?")
    st.markdown("O teste de hipótese uma maneira de usar dados para decidir se uma afirmação\
             sobre uma população é verdadeira ou falsa. Imagine que\
             você quer saber se uma nova estratégia de marketing\
             realmente aumenta a base de clientes. Você coleta\
             dados antes e depois da implementação da estratégia\
             e usa um teste de hipótese para verificar se\
             o aumento observado é significativo ou apenas por acaso.")
    st.header("E o teste T?")
    st.markdown("O teste T é um tipo específico de teste de hipótese que compara\
                 as médias de dois grupos para ver se são significativamente\
                 diferentes. Por exemplo, você pode usar um teste T\
                 para comparar a média de crescimento de clientes em dois\
                 períodos diferentes, antes e depois de uma campanha de marketing.")
    st.subheader("E qual o motivo de usarmos o teste T neste app?")
    st.markdown("Ele é muito usado porque é simples e eficaz para comparar médias,\
                especialmente quando você tem amostras pequenas e não conhece a variância da população.\
                Além disso, ele também é confiável em casos de não normalidade em\
                 distribuições, devido ao teorema do limite central.")
    st.header("Exemplos de onde usar")
    st.subheader("Crédito")
    st.markdown("Suponha que você quer saber se uma nova política de crédito está\
                 realmente ajudando a aumentar o número de aprovações de crédito.\
                 Você aplica a nova política em um grupo de clientes e compara a\
                 taxa de aprovação desse grupo com a taxa de um grupo que não foi\
                 submetido à nova política. O teste T ajudará a determinar se a\
                 diferença nas taxas de aprovação é significativa.")
    st.subheader("Planejamentos empresariais")
    st.markdown("Imagine que sua empresa financeira está planejando expandir\
                 para uma nova região e quer saber se a demanda por crédito \
                nessa região é suficiente para justificar a expansão. Você \
                pode usar um teste de hipótese para comparar a média de \
                solicitações de crédito na nova região com a média de uma \
                região onde a empresa já opera com sucesso. Se o teste T \
                mostrar que a diferença é significativa, isso pode ajudar a\
                 tomar uma decisão mais informada sobre a expansão.")

@st.dialog("Sobre o aplicativo")
def modal_sobre_app():
    """
        Renderiza um modal com informações rápidas sobre o aplicativo.
    """
    st.markdown("O aplicativo Hypoteste foi criado para facilitar o acesso a\
                realização de testes de hipótese em qualquer local e momento, \
                com uma interface amigável e de fácil uso. O app \
                utiliza testes T, para realizar suas conclusões. Antes de usar\
                 admite-se que o usuário tenha os valores solicidados \
                calculados de forma prévia.")
    st.write("Também existe uma versão portátil para rodar em\
              jupyter notebooks, no repositório deste aplicativo!\
              Sinta-se a vontade para usá-lo conforme necessário.")

@st.dialog("Fale comigo!")
def modal_contato():
    """
        Renderiza um modal com informações de contato ao
        criador do app.
    """
    st.write("Obrigado por se interessar no Hypoteste!")
    st.write("Você pode entrar em contato comigo via e-mail ou LinkedIn:")
    mc_left_column, mc_right_column = st.columns(2)

    with mc_left_column:
        st.image('https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white')
        st.write("https://www.linkedin.com/in/jhonata-tirloni/")
    with mc_right_column:
        st.image('https://img.shields.io/badge/iCloud-3693F3?style=for-the-badge&logo=iCloud&logoColor=white')
        st.write("jhonatatirloni@icloud.com")

# Configurações básicas do app;
st.set_page_config(
    layout="wide",
    page_title="Hypoteste - Testes de hipótese",
    page_icon="favicon.png",
    menu_items={
        "Report a Bug": "mailto:jhonatatirloni@icloud.com",
        "Get help": "https://www.linkedin.com/feed/",
    },
)
i = 0

# Opções da sidebar do app, renderiza primeiro;
while i < 27:
    st.sidebar.write(" ")
    i += 1
st.sidebar.title("Ajuda e informações")
st.sidebar.write("---")
st.sidebar.button("O que é teste de hipótese?", use_container_width=True, on_click=modal_sobre_teste)
st.sidebar.button("Sobre o aplicativo", use_container_width=True, on_click=modal_sobre_app)
st.sidebar.button("Contato", use_container_width=True, on_click=modal_contato)
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.image("/mount/src/web-hypoteste/static/1710959268147.png", width=70)

# Layout baseado em containers, parte superior do app;
container_header = st.container()

with container_header:
    header_left_column, header_center_column, header_right_column = st.columns(
        3, vertical_alignment="top"
    )

    with header_center_column:
        st.html(
            """
            <p style="background-color:#001d11; color:white; text-align:center;">
                << Use o menu lateral esquerdo para mudar o tipo de teste, acessar ajuda e mais!
            </p>
            """
        )
        st.image("logo_hypoteste.png", use_column_width=True)
        st.header("Teste para amostra dupla independente")
        st.write("")
        st.write("")

# Inicio do layout baseado em colunas, parte inferior do app;
left_column, center_column, right_column = st.columns(3)

with center_column:
    container_center_column = st.container()
    with container_center_column:
        direction_left_column, direction_center_column = st.columns([0.03, 0.60])
        with direction_left_column:
            st.image("primeiro_passo.png", use_column_width=True)
        with direction_center_column:
            st.subheader("Selecione a direção do teste")
        st.write(
            "Selecione apenas um. Caso tenha selecionado outros,\
                     desmarque-os e selecione o correto."
        )
        left_center_column, center_center_column, right_center_column = st.columns(3)
        with left_center_column:
            teste_esquerda = st.checkbox(" ", key="bt_esquerda")
            st.image("bt_esquerda.png")
        with center_center_column:
            teste_bilateral = st.checkbox(" ", key="bt_bilateral")
            st.image("bt_bilateral.png")
        with right_center_column:
            teste_direita = st.checkbox(" ", key="bt_direita")
            st.image("bt_direita.png")
        st.write("")

        text_info_left_column, text_info_center_column = st.columns([0.03, 0.60])
        with text_info_left_column:
            st.image("segundo_passo.png", use_column_width=True)
        with text_info_center_column:
            st.subheader("Preencha os campos do teste")

        estat_amostra = st.number_input(label="Estatística da amostra")
        variancia_amostral = st.number_input(label="Variância amostral")
        parametro_pop = st.number_input(label="Parâmetro aproximado da população")
        tamanho_amostra = st.number_input(label="Tamanho da amostra")

        st.write("")
        st.write("")

        btn_left_column, btn_center_column, btn_right_column = st.columns(
            [0.01, 0.6, 0.01]
        )
        with btn_center_column:
            if st.button("Realizar teste", type="primary", use_container_width=True):
                (
                    t,
                    p_valor_bicaudal,
                    p_valor_unicaudal,
                    alpha_unicaudal,
                    alpha_bicaudal,
                    graus_liberdade,
                ) = teste_amostra_unica(
                    variancia_amostral=variancia_amostral,
                    tamanho_amostra=tamanho_amostra,
                    estat_amostra=estat_amostra,
                    parametro_pop=parametro_pop,
                    teste_bilateral=teste_bilateral,
                    teste_esquerda=teste_esquerda,
                    teste_direita=teste_direita,
                )
                df = graus_liberdade
                x = linspace(-4, 4, 1000)
                pdf = dist_t.pdf(x, df)
                plot = plt.plot(x, pdf)

                # Testes bilaterais
                if teste_bilateral is True and t > 0 and t <= alpha_bicaudal:
                    st.write(f"Valor T tabelado: Para resultado positivo temos\
                              {round(alpha_bicaudal, 2)}\
                              e negativo temos {round(alpha_bicaudal*-1, 2)}")
                    st.write(f"Valor T do teste: {round(t, 2)}")
                    st.write(f"Valor P do teste: {round(p_valor_bicaudal, 2)}")
                    st.write("Valor T menor do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Não rejeitar a hipótese nula, \
                             e desfavorecer a hipótese alternativa. "
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T, \
                             os valores críticos em vermelho e o resultado \
                             do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_bicaudal * -1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                        label="Resultado do teste",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    st.pyplot(plt.gcf())

                elif teste_bilateral is True and t > 0 and t > alpha_bicaudal:
                    st.write(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal}\
                              e negativo temos {alpha_bicaudal*-1}")
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_bicaudal}")
                    st.write("Valor T maior do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Rejeitar a hipótese nula,\
                              e favorecer a hipótese alternativa."
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T,\
                              os valores críticos em vermelho e o \
                             resultado do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_bicaudal * -1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                        label="Resultado do teste",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    st.pyplot(plt.gcf())

                elif teste_bilateral is True and t < 0 and t <= alpha_bicaudal * -1:
                    st.write(f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal}\
                              e negativo temos {alpha_bicaudal*-1}")
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_bicaudal}")
                    st.write("Valor T menor do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Não rejeitar a hipótese nula, \
                             e desfavorecer a hipótese alternativa. "
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T,\
                              os valores críticos em vermelho e o resultado\
                              do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_bicaudal * -1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())

                elif teste_bilateral is True and t < 0 and t > alpha_bicaudal * -1:
                    st.write(
                        f"Valor T tabelado: Para resultado positivo temos {alpha_bicaudal}\
                             e negativo temos {alpha_bicaudal*-1}"
                    )
                    st.write(f"Valor T do teste:{t}")
                    st.write(f"Valor P do teste: {p_valor_bicaudal}")
                    st.write("Valor T maior do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Rejeitar a hipótese nula, e \
                             favorecer a hipótese alternativa."
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T, \
                            os valores críticos em vermelho e o resultado do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_bicaudal * -1, 1000)
                    x2_fill = linspace(4, alpha_bicaudal, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())

                # Testes unilaterais a esquerda
                elif teste_esquerda is True and t < 0 and t <= (alpha_unicaudal) * -1:
                    st.write(
                        f"Valor T tabelado: Para resultado negativo temos {(alpha_unicaudal)*-1}"
                    )
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T menor do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Não rejeitar a hipótese nula,\
                            e desfavorecer a hipótese alternativa. "
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T, os\
                            valores críticos em vermelho e o resultado do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_unicaudal * -1, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())

                elif teste_esquerda is True and t < 0 and t > (alpha_unicaudal) * -1:
                    st.write(
                        f"Valor T tabelado: Para resultado negativo temos {(alpha_unicaudal)*-1}"
                    )
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T maior do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Rejeitar a hipótese nula,\
                              e favorecer a hipótese alternativa."
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T,\
                             os valores críticos em vermelho e o resultado do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_unicaudal * -1, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())
                
                elif teste_esquerda is True and t < 0 and t <= alpha_unicaudal * -1:
                    st.write(
                        f"Valor T tabelado: Para resultado negativo temos {(alpha_unicaudal)*-1}"
                    )
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T menor do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Não rejeitar a hipótese nula, \
                             e desfavorecer a hipótese alternativa. "
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T,\
                              os valores críticos em vermelho e o resultado\
                              do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_bicaudal * -1, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())

                elif teste_esquerda is True and t < 0 and t > alpha_unicaudal * -1:
                    st.write(
                        f"Valor T tabelado: Para resultado negativo temos {(alpha_unicaudal)*-1}"
                    )
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T maior do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Rejeitar a hipótese nula, e \
                             favorecer a hipótese alternativa."
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T, \
                            os valores críticos em vermelho e o resultado do teste na linha preta."
                    )
                    x1_fill = linspace(-4, alpha_bicaudal * -1, 1000)
                    plt.fill_between(
                        x1_fill, 0, dist_t.pdf(x1_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())
                
                # Testes unilaterais a direita
                elif teste_direita is True and t > 0 and t <= alpha_unicaudal:
                    st.write(
                        f"Valor T tabelado: Para resultado positivo temos {alpha_unicaudal}"
                    )
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T menor do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Não rejeitar a hipótese nula,\
                             e desfavorecer a hipótese alternativa. "
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T, \
                             os valores críticos em vermelho e o resultado do teste na linha preta."
                    )
                    x2_fill = linspace(4, alpha_unicaudal, 1000)
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                        label="Resultado do teste",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    st.pyplot(plt.gcf())

                elif teste_direita is True and t > 0 and t >= alpha_unicaudal:
                    st.write(
                        f"Valor T tabelado: Para resultado positivo temos {alpha_unicaudal}"
                    )
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T maior do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Rejeitar a hipótese nula,\
                             e favorecer a hipótese alternativa."
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T,\
                             os valores críticos em vermelho e resultado do teste\
                             na linha preta."
                    )
                    x2_fill = linspace(4, alpha_unicaudal, 1000)
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                        label="Resultado do teste",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    plt.legend()
                    st.pyplot(plt.gcf())

                elif teste_direita is True and t < 0 and t <= alpha_unicaudal * -1:
                    st.write(f"Valor T tabelado: Para resultado positivo temos {alpha_unicaudal}")
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T menor do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Não rejeitar a hipótese nula, \
                             e desfavorecer a hipótese alternativa. "
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T,\
                              os valores críticos em vermelho e o resultado\
                              do teste na linha preta."
                    )
                    x2_fill = linspace(4, alpha_unicaudal, 1000)
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())

                elif teste_direita is True and t < 0 and t > alpha_unicaudal * -1:
                    st.write(f"Valor T tabelado: Para resultado positivo temos {alpha_unicaudal}")
                    st.write(f"Valor T do teste: {t}")
                    st.write(f"Valor P do teste: {p_valor_unicaudal}")
                    st.write("Valor T maior do que o valor alpha tabelado.")
                    st.write(
                        "Recomendação: Rejeitar a hipótese nula, e \
                             favorecer a hipótese alternativa."
                    )
                    st.write(
                        "O gráfico abaixo demonstra a distribuição T, \
                            os valores críticos em vermelho e o resultado do teste na linha preta."
                    )
                    x2_fill = linspace(4, alpha_unicaudal, 1000)
                    plt.fill_between(
                        x2_fill, 0, dist_t.pdf(x2_fill, df), color="red", alpha=0.3
                    )
                    plt.axvline(
                        x=(lambda t: -4 if t < -4 else (4 if t > 4 else t))(t),
                        color="black",
                        linestyle="--",
                    )
                    plt.title("Distribuição T, região crítica e posição de T")
                    plt.ylabel("Densidade de probabilidade")
                    plt.xlabel("Valores")
                    st.pyplot(plt.gcf())
