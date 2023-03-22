# 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

O CEO da empresa precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas 
e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

## Visão Geral

1. Quantos restaurantes estão registrados?
2. Quantos países estão registrados?
3. Quantas cidades estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## Visão Países

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
4. Qual o nome do país que possui a maior quantidade de avaliações feitas?
5. Qual o nome do país que possui, na média, a maior nota média registrada?

## Visão Cidades

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

## Visão Cuisines

1. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
média de avaliação?
2. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
possui a maior média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?
11. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a maior média de avaliação?
12. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a menor média de avaliação?
13. Qual o tipo de culinária que possui a maior nota média?

O CEO também pediu que fosse gerado um dashboard que permitisse que ele
visualizasse as principais informações das perguntas que ele fez. O CEO precisa
dessas informações o mais rápido possível, uma vez que ele também é novo na
empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir
tomar decisões mais assertivas.
Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as
perguntas feitas do CEO e criar o dashboard solicitado.

# 2. Os Dados

O conjunto de dados que representam o contexto está disponível na plataforma do
Kaggle. O link para acesso aos dados:
https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

# 3. Premissas assumidas para a análise

1. A base de dados não contém informações sobre a data dos dados.
2. O modelo de negócio assumido foi o modelo de Marketplace.
3. As principais visões de negócio adotadas foram: Visão Geral, Visão Países, Visão Cidades e Visão Cuisines.
4. O critério de desempate em alguns casos foi o menor id do restaurante.

# 4. Estratégia da solução

1. O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões de negócio.
2. Para a resolução do problema de negócio foram utilizadas as seguintes ferramentas:
  - Como rascunho e análises prévias - Jupyter Notebook
  - Bibliotecas de manipulação de dados - Pandas
  - Bibliotecas de visualização de dados - Plotly, Folium.
  - Script Python Final - Jupyter Lab
  - Visualização do Dashboard - Streamlit e Streamlit Cloud.

# 5. Top 3 Insights de dados

1. Os tipos culinários mais famosos nao se encontram entre os mais bem avaliados.
2. Os países com mais cidades registradas possuem mais restaurantes registrados e mais votos.
3. Os países com mais restaurantes registrados não necessariamente tem a maior nota média.

# 6. O produto final do projeto

Painel online hospedado em Cloud e disponível para acesso em qualquer dispositivo com acesso à internet pelo link:
https://tagarro-projeto-fome-zero.streamlit.app/

# 7. Conclusão

O objetivo deste projeto é criar um conjunto de gráficos e/ou tabelas que exibam estas métricas da melhor maneira possível para o CEO.

# 8. Próximos passos

1. Adicionar novas visões de negócio.
2. Adicionar novas tabelas.
3. Melhorar design da página e apresentação.
