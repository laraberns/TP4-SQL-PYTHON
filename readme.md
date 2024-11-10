# Projeto de Bloco de Fundamento de Dados - TP4

Este projeto foi desenvolvido como parte do Teste de Performance 4 (TP4) do curso de Fundamentos de Dados, com o objetivo de criar um sistema em Python para manipulação e análise de dados usando SQLite, arquivos CSV e JSON. A partir das consultas SQL realizadas, os resultados são exportados para JSON e visualizados no Looker Studio, fornecendo insights através de tabelas e gráficos interativos.

## Estrutura do Projeto

O projeto consiste na criação e manipulação de tabelas SQLite baseadas em dados importados de arquivos CSV, realizando consultas SQL avançadas em Python e exportando os resultados em formato JSON para visualização no Looker Studio.

### Tabelas Utilizadas

1. **Funcionários** - Armazena informações sobre os funcionários, como nome, cargo, departamento, salário e data de admissão.
2. **Cargos** - Contém os cargos dos funcionários, incluindo salário base, nível e carga horária.
3. **Departamentos** - Guarda informações sobre os departamentos, como nome, andar e sigla.
4. **Histórico de Salários** - Registra o histórico de salários dos funcionários, mês a mês.
5. **Dependentes** - Armazena dados dos dependentes dos funcionários.
6. **Projetos Desenvolvidos** - Guarda informações sobre projetos, incluindo descrição, data de início, data de conclusão, custo e status.
7. **Recursos do Projeto** - Registra os recursos utilizados em cada projeto, com detalhes sobre tipo e quantidade.

### Consultas SQL

As consultas realizadas no Python são:

1. **Média de Salários de Funcionários em Projetos Concluídos por Departamento**
2. **Três Recursos Materiais mais Usados nos Projetos**
3. **Custo Total dos Projetos Concluídos por Departamento**
4. **Lista de Projetos em Execução com Responsáveis**
5. **Projeto com o Maior Número de Dependentes Envolvidos**

### Visualização no Looker Studio

Três das consultas acima foram exportadas para JSON e visualizadas no Looker Studio:

1. **Média de Salários de Funcionários em Projetos Concluídos por Departamento**
2. **Custo Total dos Projetos Concluídos por Departamento**
3. **Três Recursos Materiais mais Usados nos Projetos**

Cada visualização inclui tabelas e gráficos, com filtros interativos que permitem aos usuários explorar os dados de forma dinâmica.

## Como Rodar o Projeto

1. Clone o repositório e acesse a pasta do projeto.
2. Execute o script Python para gerar o banco de dados SQLite e carregar os dados dos arquivos CSV.
3. Execute as consultas SQL diretamente no script Python.
4. Exporte os resultados das consultas para JSON.
5. Importe os arquivos JSON para o Looker Studio para visualização.
