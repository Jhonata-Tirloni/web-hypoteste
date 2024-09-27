![](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![](	https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white) ![](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)

<img src="https://github.com/Jhonata-Tirloni/web-hypoteste/blob/dev/static/logo_hypoteste.png">

# Sobre
O aplicativo Hypoteste foi criado para facilitar o acesso a realização de testes de hipótese em qualquer local e momento, com uma interface amigável e de fácil uso. 
O app utiliza testes T, para realizar suas conclusões. Antes de usar admite-se que o usuário tenha os valores solicidados calculados de forma prévia.

# Como usar
O Hypoteste foi desenvolvido para ser utilizado tanto localmente, caso queira clonar e fazer suas modificações, quanto online através de um deploy do streamlit.

## 🛜 Usando online
Para usar a versão online hospedada via streamlit é muito simples, basta acessar este link, selecionar o tipo de teste no lado esquerdo, preencher os campos e clicar em "realizar teste". 

## 👨🏻‍💻 Usando localmente
Caso queira utilizar o aplicativo de forma local, basta seguir os paços abaixo:

1. Clone este repositório abrindo um terminal e digitando o comando abaixo:
```
git clone https://gitlab.com/data-science-apps/hypoteste.git
```
2. Abra a pasta onde os dados foram clonados e abra um terminal
3. Instale as dependências do projeto com o comando abaixo
```
pip install -r requirements.txt
```
5. Feito isso, digite o comando abaixo no terminal
```
streamlit run Amostra_Unica.py
```
Ao fazer isso, o streamlit irá abrir um navegador com o aplicativo sendo executado em localhost. Ao mesmo tempo, é possível realizar o deploy do app localmente para toda a rede.
