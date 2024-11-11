import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from fastapi import FastAPI
import json

app = FastAPI()
load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

engine = create_engine(
    f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
)

# Função de consulta dinâmica
def consultar(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df)

# Função de gerar JSON
def gerar_json(query, engine, caminho_arquivo):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        df.to_json(caminho_arquivo, force_ascii=False)
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            return json.load(file)


print("1 - Trazer a média dos salários (atual) dos funcionários responsáveis por projetos concluídos, agrupados por departamento:")
query_media_salarios = """
        SELECT departamentos.nome as nome_departamento, AVG(funcionarios.salario_real) as media_salario
        FROM funcionarios
        INNER JOIN projetos ON funcionarios.id_funcionario = projetos.id_funcionario
        INNER JOIN departamentos ON funcionarios.id_departamento = departamentos.id_departamento
        WHERE projetos.status = 'Concluído'
        GROUP BY departamentos.nome
    """
consultar(query_media_salarios)

@app.get("/media-salarios")
async def media_salarios():
    # Gerar JSON e API
    media_salarios_json = gerar_json(
        query_media_salarios, engine, '../json/media_salarios_departamento.json')
    return media_salarios_json

print("2 - Identificar os três recursos materiais mais usados nos projetos, listando a descrição do recurso e a quantidade total usada:")
query_recursos_materiais = """
        SELECT descricao, quantidade_utilizada
        FROM recursos_projeto
        WHERE tipo_recurso = 'material'
        ORDER BY quantidade_utilizada DESC
        LIMIT 3
    """
consultar(query_recursos_materiais)

@app.get("/recursos-materiais")
async def recursos_materiais():
    # Gerar JSON e API
    recursos_materiais_json = gerar_json(
        query_recursos_materiais, engine, '../json/recursos_materiais.json')
    return recursos_materiais_json

print("3 - Calcular o custo total dos projetos por departamento, considerando apenas os projetos 'Concluídos':")
query_custo_projetos_concluidos = """
        SELECT SUM(projetos.custo_projeto) as custo_total_projeto, departamentos.nome as nome_departamento
        FROM funcionarios
        INNER JOIN projetos ON funcionarios.id_funcionario = projetos.id_funcionario
        INNER JOIN departamentos ON funcionarios.id_departamento = departamentos.id_departamento
        WHERE projetos.status = 'Concluído'
        GROUP BY departamentos.nome
    """
consultar(query_custo_projetos_concluidos)

@app.get("/custo-projetos-concluidos")
async def custo_projetos_concluidos():
    # Gerar JSON e API
    custo_projetos_concluidos_json = gerar_json(
        query_custo_projetos_concluidos, engine, '../json/custo_projetos_concluidos.json')
    return custo_projetos_concluidos_json

print("4. Listar todos os projetos com seus respectivos nomes, custo, data de início, data de conclusão e o nome do funcionário responsável, que estejam 'Em Execução':")
consultar("""
    SELECT projetos.nome as nome_projeto, projetos.custo_projeto as custo_projeto, 
           projetos.data_inicio as data_inicio_projeto, projetos.data_conclusao as data_conclusao_projeto, 
           funcionarios.nome as funcionario_nome
    FROM funcionarios
    INNER JOIN projetos ON funcionarios.id_funcionario = projetos.id_funcionario
    WHERE projetos.status = 'Em Execução'
""")

print("5. Identificar o projeto com o maior número de dependentes envolvidos, considerando que os dependentes são associados aos funcionários que estão gerenciando os projetos:")
consultar("""
    SELECT projetos.nome, COUNT(dependentes.id_dependente) AS total_dependentes
    FROM funcionarios
    INNER JOIN projetos ON funcionarios.id_funcionario = projetos.id_funcionario
    INNER JOIN dependentes ON funcionarios.id_funcionario = dependentes.id_funcionario
    GROUP BY projetos.nome
    ORDER BY total_dependentes DESC
    LIMIT 1
""")
