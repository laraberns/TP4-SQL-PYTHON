-- Criar Tabela Departamentos
CREATE TABLE departamentos(
  id_departamento SERIAL PRIMARY KEY,
  nome VARCHAR(256) NOT NULL,
  andar INTEGER NOT NULL,
  sigla VARCHAR(5) NOT NULL
);

-- Criar Tabela Cargos com id_departamento
CREATE TABLE cargos(
  id_cargo SERIAL PRIMARY KEY,
  descricao VARCHAR(256) NOT NULL,
  salario_base FLOAT NOT NULL,
  nivel VARCHAR(10) CHECK (nivel IN ('estagiário', 'técnico', 'analista', 'gerente', 'diretor')) NOT NULL,
  carga_horaria_semanal INT NOT NULL,
  id_departamento INTEGER REFERENCES departamentos(id_departamento) NOT NULL
);

-- Criar Tabela Funcionários
CREATE TABLE funcionarios(
  id_funcionario SERIAL PRIMARY KEY,
  nome VARCHAR(256) NOT NULL,
  id_cargo INTEGER REFERENCES cargos(id_cargo) NOT NULL,
  id_departamento INTEGER REFERENCES departamentos(id_departamento) NOT NULL,
  salario_real FLOAT NOT NULL,
  data_admissao DATE NOT NULL
);	

-- Criar Tabela Histórico de Salários
CREATE TABLE historico_salarios(
  id_salario SERIAL PRIMARY KEY,
  id_funcionario INTEGER REFERENCES funcionarios(id_funcionario) NOT NULL,
  mes_ano DATE NOT NULL, 
  salario_recebido FLOAT NOT NULL
);

-- Criar Tabela Dependentes
CREATE TABLE dependentes(
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
  status VARCHAR(20) CHECK (status IN ('Em Planejamento', 'Em Execução', 'Concluído', 'Cancelado')) NOT NULL, 
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

-- Inserir dados na Tabela Departamentos
INSERT INTO departamentos (nome, andar, sigla) VALUES
('Produção', 1, 'PRO'),
('Compras',5, 'COM'),
('Desenvolvimento',2, 'DEV'),
('Recursos Humanos', 1, 'RH'),
('Marketing', 3, 'MKT'),
('Financeiro', 4, 'FIN'),
('Suporte Técnico', 2, 'SUP');

-- Inserir dados na Tabela Cargos
INSERT INTO cargos (descricao, salario_base, nivel, carga_horaria_semanal, id_departamento) VALUES
('Analista de Sistemas', 5000.00, 'analista', 40, 1),
('Desenvolvedor Backend', 6000.00, 'analista', 40, 1),
(' de Projeto', 8000.00, 'gerente', 45, 1),
('Diretor de Tecnologia', 12000.00, 'diretor', 50, 1),
('Estagiário de TI', 2000.00, 'estagiário', 30, 7),
('Analista de Recursos Humanos', 4500.00, 'analista', 40, 2);

-- Inserir dados na Tabela Funcionários
INSERT INTO funcionarios (nome, id_cargo, id_departamento, salario_real, data_admissao) VALUES
('Paulo Nobre', 2, 3, 2500.00, '2024-07-10'),
('Keiran Bosh', 5, 1, 2000.00, '2023-05-30'),
('Laura Amado', 5, 4, 2000.00, '2023-05-30'),
('Ana Silva', 1, 1, 5000.00, '2023-01-10'),
('Bruno Oliveira', 2, 1, 6000.00, '2023-02-15'),
('Carlos Souza', 3, 1, 8000.00, '2023-03-20'),
('Daniela Santos', 4, 1, 12000.00, '2023-04-25'),
('Eduardo Costa', 5, 5, 2000.00, '2023-05-30'),
('Fernanda Lima', 6, 2, 4500.00, '2023-06-05'),
('Gabriel Almeida', 6, 3, 6500.00, '2023-07-10');

-- Inserir dados na Tabela Dependentes
INSERT INTO dependentes (id_funcionario, relacao, sexo, nome, data_nascimento) VALUES
(1, 'filho(a)', 'feminino', 'Maria Bosh', '2015-06-20'),
(1, 'cônjuge', 'feminino', 'Laura Bosh', '1988-08-15'),
(2, 'companheiro(a)', 'masculino', 'Pedro Amado', '1990-09-12'),
(2, 'filho(a)', 'masculino', 'Lucas Amado', '2016-12-05'),
(3, 'filho(a)', 'masculino', 'Felipe Silva', '2012-10-30'),
(3, 'cônjuge', 'feminino', 'Carla Silva', '1991-02-14'),
(4, 'filho(a)', 'feminino', 'Isabela Oliveira', '2018-03-22'),
(4, 'companheiro(a)', 'feminino', 'Camila Oliveira', '1989-01-09'),
(5, 'filho(a)', 'feminino', 'Sofia Souza', '2014-11-10'),
(5, 'cônjuge', 'feminino', 'Juliana Souza', '1990-07-17'),
(6, 'enteado(a)', 'masculino', 'Rafael Santos', '2011-05-02'),
(6, 'companheiro(a)', 'masculino', 'Marcelo Santos', '1987-12-11'),
(7, 'filho(a)', 'masculino', 'André Almeida', '2017-02-20'),
(7, 'filho(a)', 'feminino', 'Paula Almeida', '2019-06-25'),
(8, 'filho(a)', 'masculino', 'Roberto Costa', '2015-05-16'),
(8, 'cônjuge', 'feminino', 'Juliana Costa', '1988-09-30'),
(9, 'filho(a)', 'masculino', 'Felipe Lima', '2015-08-05'),
(9, 'filho(a)', 'feminino', 'Juliana Lima', '2018-01-30'),
(10, 'filho(a)', 'masculino', 'Rafael Almeida', '2016-10-10'),
(10, 'cônjuge', 'feminino', 'Sofia Almeida', '1989-02-20');

-- Inserir dados na Tabela Histórico de Salários
INSERT INTO historico_salarios (id_funcionario, mes_ano, salario_recebido) VALUES
(1, '2023-05-31', 2000.00),
(1, '2023-06-30', 2000.00),
(1, '2023-07-31', 2000.00),
(1, '2023-08-31', 2000.00),
(1, '2023-09-30', 2000.00),
(1, '2023-10-31', 2000.00),
(2, '2023-05-31', 2000.00),
(2, '2023-06-30', 2000.00),
(2, '2023-07-31', 2000.00),
(2, '2023-08-31', 2000.00),
(2, '2023-09-30', 3200.00),
(2, '2023-10-31', 3700.00),
(3, '2023-01-31', 5000.00),
(3, '2023-02-28', 7000.00),
(3, '2023-03-31', 7000.00),
(3, '2023-04-30', 7000.00),
(3, '2023-05-31', 7000.00),
(3, '2023-06-30', 7000.00),
(4, '2023-02-28', 6000.00),
(4, '2023-03-31', 6000.00),
(4, '2023-04-30', 6000.00),
(4, '2023-05-31', 6000.00),
(4, '2023-06-30', 10000.00),
(4, '2023-07-31', 10000.00),
(5, '2023-03-31', 8000.00),
(5, '2023-04-30', 8000.00),
(5, '2023-05-31', 8000.00),
(5, '2023-06-30', 8000.00),
(5, '2023-07-31', 9000.00),
(5, '2023-08-31', 9000.00),
(6, '2023-04-30', 12000.00),
(6, '2023-05-31', 12000.00),
(6, '2023-06-30', 12000.00),
(6, '2023-07-31', 12000.00),
(6, '2023-08-31', 12000.00),
(6, '2023-09-30', 18000.00),
(7, '2023-05-31', 12000.00),
(7, '2023-06-30', 12000.00),
(7, '2023-07-31', 12000.00),
(7, '2023-08-31', 12000.00),
(7, '2023-09-30', 12000.00),
(7, '2023-10-31', 12000.00),
(8, '2023-05-31', 2000.00),
(8, '2023-06-30', 2000.00),
(8, '2023-07-31', 2000.00),
(8, '2023-08-31', 2000.00),
(8, '2023-09-30', 2000.00),
(8, '2023-10-31', 2000.00),
(9, '2023-05-31', 4500.00),
(9, '2023-06-30', 4500.00),
(9, '2023-07-31', 4500.00),
(9, '2023-08-31', 4500.00),
(9, '2023-09-30', 4500.00),
(9, '2023-10-31', 4500.00),
(10, '2023-06-30', 6500.00),
(10, '2023-07-31', 6500.00),
(10, '2023-08-31', 6500.00),
(10, '2023-09-30', 6500.00),
(10, '2023-10-31', 6500.00),
(10, '2023-11-30', 6500.00);

-- Rodar no Terminal do PSQL para criar arquivos CSV
-- \copy public.cargos TO 'C:\Users\Lara\Documents\TP-3-Bloco\csv\cargos.csv' DELIMITER ',' CSV HEADER;
-- \copy public.departamentos TO 'C:\Users\Lara\Documents\TP-3-Bloco\csv\departamentos.csv' DELIMITER ',' CSV HEADER;
-- \copy public.dependentes TO 'C:\Users\Lara\Documents\TP-3-Bloco\csv\dependentes.csv' DELIMITER ',' CSV HEADER;
-- \copy public.funcionarios TO 'C:\Users\Lara\Documents\TP-3-Bloco\csv\funcionarios.csv' DELIMITER ',' CSV HEADER;
-- \copy public.historico_salarios TO 'C:\Users\Lara\Documents\TP-3-Bloco\csv\historico_salarios.csv' DELIMITER ',' CSV HEADER;