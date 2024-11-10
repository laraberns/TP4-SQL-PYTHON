import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter os valores das variáveis de ambiente
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Configuração da conexão com o banco de dados PostgreSQL
engine = create_engine(
    f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Função para criar as tabelas
def criar_tabelas():
    criar_tabelas_sql = """
    -- Criar Tabela Departamentos
    CREATE TABLE IF NOT EXISTS departamentos(
      id_departamento SERIAL PRIMARY KEY,
      nome VARCHAR(256) NOT NULL,
      andar INTEGER NOT NULL,
      sigla VARCHAR(5) NOT NULL
    );

    -- Criar Tabela Cargos com id_departamento
    CREATE TABLE IF NOT EXISTS cargos(
      id_cargo SERIAL PRIMARY KEY,
      descricao VARCHAR(256) NOT NULL,
      salario_base FLOAT NOT NULL,
      nivel VARCHAR(10) CHECK (nivel IN ('estagiário', 'técnico', 'analista', 'gerente', 'diretor')) NOT NULL,
      carga_horaria_semanal INT NOT NULL,
      id_departamento INTEGER REFERENCES departamentos(id_departamento) NOT NULL
    );

    -- Criar Tabela Funcionários
    CREATE TABLE IF NOT EXISTS funcionarios(
      id_funcionario SERIAL PRIMARY KEY,
      nome VARCHAR(256) NOT NULL,
      id_cargo INTEGER REFERENCES cargos(id_cargo) NOT NULL,
      id_departamento INTEGER REFERENCES departamentos(id_departamento) NOT NULL,
      salario_real FLOAT NOT NULL,
      data_admissao DATE NOT NULL
    );    

    -- Criar Tabela Histórico de Salários
    CREATE TABLE IF NOT EXISTS historico_salarios(
      id_salario SERIAL PRIMARY KEY,
      id_funcionario INTEGER REFERENCES funcionarios(id_funcionario) NOT NULL,
      mes_ano DATE NOT NULL, -- Mês e ano do salário recebido
      salario_recebido FLOAT NOT NULL
    );

    -- Criar Tabela Dependentes
    CREATE TABLE IF NOT EXISTS dependentes(
      id_dependente SERIAL PRIMARY KEY,
      id_funcionario INTEGER REFERENCES funcionarios(id_funcionario) NOT NULL,
      relacao VARCHAR(20) CHECK (relacao IN ('cônjuge', 'companheiro(a)', 'filho(a)', 'enteado(a)', 'outro')) NOT NULL,
      sexo VARCHAR(10) CHECK (sexo IN ('feminino', 'masculino')) NOT NULL,
      nome VARCHAR(256) NOT NULL,
      data_nascimento DATE NOT NULL
    );

    -- Criar Tabela Projetos Desenvolvidos
    CREATE TABLE projetos(
      id_projeto SERIAL PRIMARY KEY,
      id_funcionario INTEGER REFERENCES funcionarios(id_funcionario) NOT NULL,
      nome VARCHAR(256) NOT NULL,
      descricao TEXT NOT NULL,
      data_inicio DATE NOT NULL,
      data_conclusao DATE,
      custo_projeto FLOAT NOT NULL,
      status VARCHAR(20) CHECK (status IN ('Em Planejamento', 'Em Execução', 'Concluído', 'Cancelado')) NOT NULL
    );

    -- Criar Tabela Recursos do Projeto
    CREATE TABLE recursos_projeto (
      id_recurso SERIAL PRIMARY KEY,
      id_projeto INTEGER REFERENCES projetos(id_projeto) NOT NULL,
      descricao TEXT NOT NULL,
      tipo_recurso VARCHAR(20) CHECK (tipo_recurso IN ('financeiro', 'material', 'humano')) NOT NULL, 
      quantidade_utilizada FLOAT NOT NULL,
      data_utilizacao DATE NOT NULL
    );
    """

    with engine.connect() as connection:
        connection.execute(text(criar_tabelas_sql))
    print("Tabelas criadas com sucesso!")

# Função para inserir os dados a partir dos arquivos CSV
def inserir_dados():
    # Importando os CSVs
    data_frame_cargos = pd.read_csv(r'C:\Users\Lara\Documents\TP4-BLOCO\csv\cargos.csv', encoding='latin1')
    data_frame_departamentos = pd.read_csv(
        r'C:\Users\Lara\Documents\TP4-BLOCO\csv\departamentos.csv', encoding='latin1')
    data_frame_funcionarios = pd.read_csv(
        r'C:\Users\Lara\Documents\TP4-BLOCO\csv\funcionarios.csv', encoding='latin1')
    data_frame_dependentes = pd.read_csv(
        r'C:\Users\Lara\Documents\TP4-BLOCO\csv\dependentes.csv', encoding='latin1')
    data_frame_historico_salarios = pd.read_csv(
        r'C:\Users\Lara\Documents\TP4-BLOCO\csv\historico_salarios.csv', encoding='latin1')
    data_frame_projetos = pd.read_csv(
        r'C:\Users\Lara\Documents\TP4-BLOCO\csv\projetos.csv', encoding='latin1')
    data_frame_recursos_projeto = pd.read_csv(
        r'C:\Users\Lara\Documents\TP4-BLOCO\csv\recursos_projetos.csv', encoding='latin1')

    # Inserindo os dados nas tabelas SQL
    data_frame_funcionarios.to_sql(
        'funcionarios', engine, if_exists='append', index=False)
    data_frame_departamentos.to_sql(
        'departamentos', engine, if_exists='append', index=False)
    data_frame_cargos.to_sql('cargos', engine, if_exists='append', index=False)
    data_frame_dependentes.to_sql(
        'dependentes', engine, if_exists='append', index=False)
    data_frame_historico_salarios.to_sql(
        'historico_salarios', engine, if_exists='append', index=False)
    data_frame_projetos.to_sql(
        'projetos', engine, if_exists='append', index=False)
    data_frame_recursos_projeto.to_sql(
        'recursos_projeto', engine, if_exists='append', index=False)

    print("Dados inseridos com sucesso!")

# Criar as tabelas e inserir os dados
criar_tabelas()
inserir_dados()
