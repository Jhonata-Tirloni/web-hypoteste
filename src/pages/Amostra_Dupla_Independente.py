import matplotlib.pyplot as plt
import streamlit as st
from numpy import linspace
from scipy.stats import t as dist_t
from modules.t_test.double_sample_independent import teste_duas_amostras_independentes

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
    page_icon="../static/favicon.png",
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
st.sidebar.button("O que é teste de hipótese?", use_container_width=True)
st.sidebar.button("Sobre o aplicativo", use_container_width=True)
st.sidebar.button("Contato", use_container_width=True, on_click=modal_contato)
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.image(r"../static/1710959268147.png", width=70)

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
        st.image(r"../static/logo_hypoteste.png", use_column_width=True)
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
            st.image(r"../static/primeiro_passo.png", use_column_width=True)
        with direction_center_column:
            st.subheader("Selecione a direção do teste")
        st.write(
            "Selecione apenas um. Caso tenha selecionado outros,\
                     desmarque-os e selecione o correto."
        )
        left_center_column, center_center_column, right_center_column = st.columns(3)
        with left_center_column:
            teste_esquerda = st.checkbox(" ", key="bt_esquerda")
            st.image(r"../static/bt_esquerda.png")
        with center_center_column:
            teste_bilateral = st.checkbox(" ", key="bt_bilateral")
            st.image(r"../static/bt_bilateral.png")
        with right_center_column:
            teste_direita = st.checkbox(" ", key="bt_direita")
            st.image(r"../static/bt_direita.png")
        st.write("")

        text_info_left_column, text_info_center_column = st.columns([0.03, 0.60])
        with text_info_left_column:
            st.image(r"../static/segundo_passo.png", use_column_width=True)
        with text_info_center_column:
            st.subheader("Preencha os campos do teste")

        estat_amostra_um = st.number_input(label="Estatística da amostra um")
        estat_amostra_dois = st.number_input(label="Estatística da amostra dois")
        variancia_amostra_um = st.number_input(label="Variância da amostra um")
        variancia_amostra_dois = st.number_input(label="Variância da amostra dois")
        tamanho_amostra_um = st.number_input(label="Tamanho da amostra um")
        tamanho_amostra_dois = st.number_input(label="Tamanho da amostra dois")

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
                ) = teste_duas_amostras_independentes(
                    variancia_amostra_um=variancia_amostra_um,
                    variancia_amostra_dois=variancia_amostra_dois,
                    tamanho_amostra_um=tamanho_amostra_um,
                    tamanho_amostra_dois=tamanho_amostra_dois,
                    estat_amostra_um=estat_amostra_um,
                    estat_amostra_dois=estat_amostra_dois,
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
