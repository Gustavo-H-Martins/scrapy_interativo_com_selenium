# web-scraping_api-restful-python :computer: :electric_plug: :battery:

# Em contrução :right_anger_bubble: :thought_balloon: :octocat: :mortar_board

## Introdução

- Trabalhar em um FORK deste repositório em seu usuário;
- O projeto back-end deverá ser desenvolvido usando a Linguagem de preferência da Vaga;
- O projeto front-end deverá ser desenvolvido usando em ReactJs ou Framework de preferência;
- Documentação para configuração do projeto em ambientes de produção (como instalar, rodar e referências a libs usadas);



- Criar um banco de dados MongoDB usando Atlas: https://www.mongodb.com/cloud/atlas ou algum Banco de Dados SQL se não sentir confortável com NoSQL;
- Criar uma REST API com as melhores práticas de desenvolvimento.
- Criar uma versão Web para listar os produtos
- Recomendável usar Drivers oficiais para integração com o DB

### Modelo de Dados:
- `GET /products/:code`: Obter a informação somente de um produto;
- `GET /products`: Listar todos os produtos da base de dados, utilizar o sistema de paginação para não sobrecarregar a `REQUEST`.

### Front End

Desenvolver um projeto em ReactJs ou técnologia de preferência para listar os produtos com a seguinte informação:

- Imagem
- Nome

Ao clicar nos produtos, expandiremos a informação utilizando um modal com os dados:

- Barcode
- Status
- Packaging
- Brands
- Store


## Extras

- **Diferencial 1** Adicionar um sistema de comparação entre os produtos;
- **Diferencial 2** Configurar Docker no Projeto para facilitar o Deploy da equipe de DevOps;
- **Diferencial 3** Configurar um sistema de alerta se tem algum falho durante o Sync dos produtos;
- **Diferencial 4** Descrever a documentação da API utilizando o conceito de Open API 3.0;
- **Diferencial 5** Escrever Unit Tests para os endpoints da API;
- **Diferencial 1** Configurar Docker no Projeto para facilitar o Deploy da equipe de DevOps;
- **Diferencial 2** Configurar um sistema de alerta se tem algum falho durante o Sync dos produtos;
- **Diferencial 3** Descrever a documentação da API utilizando o conceito de Open API 3.0;
- **Diferencial 4** Escrever Unit Tests para os endpoints da API;


## Readme do Repositório
- Como instalar e usar o projeto (instruções)
- Não esqueça o [.gitignore](https://www.toptal.com/developers/gitignore)
