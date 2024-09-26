import streamlit as st

# Configurações básicas do app;
st.set_page_config(
                    layout="wide",
                    page_title="Hypoteste - Testes de hipótese",
                    page_icon="../static/favicon.png",
                    menu_items={"Report a Bug":"mailto:jhonatatirloni@icloud.com",
                                "Get help":"https://www.linkedin.com/feed/"}
                )
i=0
# Opções da sidebar do app, renderiza primeiro;
st.sidebar.image(r'../static/1710959268147.png') 
st.sidebar.title("Selecionar teste")
st.sidebar.write("Selecione um tipo de teste abaixo")
st.sidebar.write("---")
st.sidebar.button("Amostra única", use_container_width=True)
st.sidebar.button("Duas amostras, pareadas", use_container_width=True)
st.sidebar.button("Duas amostras, independentes", use_container_width=True)
while i < 18: st.sidebar.write(" "); i+=1
st.sidebar.title("Ajuda e informações")
st.sidebar.write("---")
st.sidebar.button("O que é teste de hipótese?", use_container_width=True)
st.sidebar.button("Sobre o aplicativo", use_container_width=True)
st.sidebar.button("Como usar", use_container_width=True)
st.sidebar.button("Contato", use_container_width=True)

# Layout baseado em containers, parte superior do app;
container_header = st.container()

with container_header:
    header_left_column, header_center_column, header_right_column= st.columns(3, vertical_alignment='top')

    with header_center_column:
        st.html(
            '''
            <p style="background-color:#001d11; color:white; text-align:center;">
                << Use o menu lateral esquerdo para mudar o tipo de teste, acessar ajuda e mais!
            </p>
            '''
        )
        st.image(r'../static/logo_hypoteste.png', use_column_width=True)
        st.write("")
        st.write("")

# Inicio do layout baseado em colunas, parte inferior do app;
left_column, center_column, right_column = st.columns(3)

with center_column:
    container_center_column = st.container()
    with container_center_column:

        direction_left_column, direction_center_column = st.columns([0.03, 0.60])
        with direction_left_column:
            st.image(r'../static/primeiro_passo.png', use_column_width=True)
        with direction_center_column:
            st.subheader("Selecione a direção do teste")

        left_center_column, center_center_column, right_center_column = st.columns(3)
        with left_center_column:
            st.checkbox(" ", key="bt_esquerda")
            st.image(r'../static/bt_esquerda.png')
        with center_center_column:
            st.checkbox(" ", key="bt_bilateral")
            st.image(r'../static/bt_bilateral.png')
        with right_center_column:
            st.checkbox(" ", key="bt_direita")
            st.image(r'../static/bt_direita.png')
        st.write("")

        text_info_left_column, text_info_center_column = st.columns([0.03, 0.60])
        with text_info_left_column:
            st.image(r'../static/segundo_passo.png', use_column_width=True)
        with text_info_center_column:
            st.subheader("Preencha os campos do teste")
        st.text_input(label="Estatística da amostra")
        st.text_input(label="Variância amostral")
        st.text_input(label="Parâmetro aproximado da população")
        st.text_input(label="Tamanho da amostra")
        st.write("")
        st.write("")

        btn_left_column, btn_center_column, btn_right_column = st.columns(3)
        with btn_center_column:
            st.button("Realizar teste",
                      type='primary',
                      use_container_width=True)
