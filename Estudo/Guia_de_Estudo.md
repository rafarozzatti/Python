# Roadmap completo de Python para análise de dados

## Etapa 1 — Fundamentos de Python

Aprender a escrever os primeiros programas.

- `print()` e comentários
- Variáveis e atribuição de valores
- Tipos de dados: `int`, `float`, `str`, `bool`
- `type()` e conversão de tipos: `int()`, `float()`, `str()`, `bool()`
- Entrada de dados com `input()`
- Operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operadores de comparação: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Operadores lógicos: `and`, `or`, `not`
- Formatação de textos com f-strings
- Precedência de operadores

## Etapa 2 — Condições e lógica de programação

Ensinar o programa a tomar decisões.

- `if`, `elif` e `else`
- Condições simples e compostas
- Condições aninhadas
- Operadores lógicos em condições
- Validação de entradas
- Tratamento de diferentes cenários
- Exercícios de classificação, cálculos e regras de negócio

## Etapa 3 — Estruturas de repetição

Automatizar tarefas repetitivas.

- Laço `while`
- Laço `for`
- Função `range()`
- Contadores e acumuladores
- Condições de parada
- `break` e `continue`
- Laços aninhados
- Soma, média, contagem, mínimo e máximo
- Padrões de saída e sequências numéricas

## Etapa 4 — Estruturas de dados

Armazenar e organizar informações.

- Strings: índices, fatiamento e métodos
- Listas: criação, acesso, alteração e remoção
- Métodos de listas: `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `sort()`
- Tuplas
- Conjuntos (`set`)
- Dicionários (`dict`)
- Métodos de dicionários: `keys()`, `values()`, `items()`, `get()`
- Iteração por estruturas de dados
- Listas e dicionários aninhados
- Compreensão de listas (list comprehensions)
- Mutabilidade, cópias e referências

## Etapa 5 — Funções

Criar códigos reutilizáveis e organizados.

- Funções com `def`
- Parâmetros e argumentos
- `return` versus `print()`
- Argumentos padrão
- Escopo de variáveis
- Retorno de múltiplos valores
- Funções com listas e dicionários
- Funções lambda
- Funções integradas úteis: `len()`, `sum()`, `min()`, `max()`, `sorted()`, `round()`, `enumerate()` e `zip()`

## Etapa 6 — Organização e qualidade do código

Escrever programas mais confiáveis.

- Módulos e importações (`import`)
- Bibliotecas padrão, como `math`, `random` e `datetime`
- Tratamento de erros com `try`, `except`, `else` e `finally`
- Exceções comuns
- Leitura de mensagens de erro (tracebacks)
- Depuração (debugging)
- Organização em arquivos e pastas
- Ambientes virtuais e instalação de pacotes com `pip`
- Noções de testes com `assert` e `pytest`

## Etapa 7 — Arquivos e dados externos

Trabalhar com dados salvos fora do programa.

- Caminhos e diretórios
- Leitura e escrita de arquivos `.txt`
- Arquivos CSV com o módulo `csv`
- Arquivos JSON com o módulo `json`
- Codificação de texto, como UTF-8
- Cabeçalhos, delimitadores e valores ausentes
- Introdução ao `pathlib`
- Leitura de múltiplos arquivos e automação de tarefas

## Etapa 8 — Programação orientada a objetos (POO)

- Classes e objetos
- Atributos e métodos
- Construtor `__init__`
- `self`
- Encapsulamento
- Herança e polimorfismo
- Métodos especiais básicos

Importante para entender projetos maiores e bibliotecas Python; não precisa ser dominada antes de começar a analisar dados.

## Etapa 9 — NumPy

- Arrays e diferenças entre listas e arrays
- Criação e tipos de arrays
- Indexação e fatiamento
- Operações vetorizadas
- Agregações, médias e estatísticas básicas
- Valores ausentes e operações matemáticas
- Noções de dimensões e matrizes

## Etapa 10 — Pandas (uma das etapas mais importantes)

- `Series` e `DataFrame`
- Importação de CSV, Excel e JSON
- Inspeção: `head()`, `tail()`, `shape`, `info()` e `describe()`
- Seleção de colunas e linhas com `loc` e `iloc`
- Filtros e condições
- Ordenação de dados
- Valores nulos: `isna()`, `fillna()` e `dropna()`
- Remoção de duplicatas
- Conversão de tipos e tratamento de datas
- Criação e alteração de colunas
- `groupby()` e agregações
- `value_counts()`
- `merge()`, `join()` e `concat()`
- Tabelas dinâmicas com `pivot_table()`
- Aplicação de funções e expressões vetorizadas
- Exportação para CSV e Excel
- Boas práticas de limpeza e validação de dados

## Etapa 11 — Visualização de dados

- Matplotlib: gráficos de barras, linhas, dispersão e histogramas
- Seaborn: distribuições e relações entre variáveis
- Títulos, eixos, legendas e escalas
- Escolha do gráfico adequado
- Identificação de tendências, padrões e valores atípicos
- Comunicação dos resultados com gráficos

## Etapa 12 — APIs e coleta de dados

- Conceitos de API e HTTP
- Requisições com `requests`
- Métodos GET e noções de POST
- Códigos de status HTTP
- Respostas em JSON
- Paginação e parâmetros de consulta
- Tratamento de falhas e limites de requisições
- Consumo de APIs públicas
- Cuidados com chaves de acesso e credenciais

## Etapa 13 — Python com SQL e bancos de dados

- Conexão com MySQL
- Bibliotecas de conexão e SQLAlchemy
- Execução de consultas SQL pelo Python
- Leitura de resultados para DataFrames
- Parâmetros em consultas e segurança contra SQL injection
- Inserção e atualização controladas de dados
- Integração entre Python, SQL e Pandas
- Exportação dos resultados para arquivos e ferramentas de BI

## Etapa 14 — ETL e automação de dados

- Conceitos de ETL: extrair, transformar e carregar
- Coleta de dados de CSV, Excel, APIs e bancos SQL
- Padronização e limpeza
- Validação da qualidade dos dados
- Junção de fontes diferentes
- Organização de scripts de processamento
- Logs e tratamento de falhas
- Exportação automatizada
- Noções de execução agendada e pipelines

## Etapa 15 — Git, GitHub e portfólio

- Repositórios e controle de versão
- `git init`, `add`, `commit`, `status` e `push`
- Organização de arquivos
- Arquivo `README.md`
- Documentação de objetivo, ferramentas e resultados
- Requisitos e dependências do projeto
- Boas práticas para não publicar senhas ou credenciais
- Histórico de alterações e apresentação do projeto

## Etapa 16 — Projetos práticos para o portfólio

Você não precisa esperar terminar todo o conteúdo para começar a criar projetos. Vamos construir projetos pequenos ao longo do aprendizado e aumentar a complexidade conforme você evoluir.

### Projeto 1 — Análise de vendas básica

Fundamentos

Receber valores, calcular faturamento, médias, totais e classificar resultados. Tudo inicialmente sem bibliotecas externas.

### Projeto 2 — Análise de arquivo CSV

Arquivos

Ler uma base de vendas, contar registros, calcular indicadores e gerar um relatório.

### Projeto 3 — Análise exploratória com Pandas

Análise de dados

Limpar dados, tratar ausências, remover duplicatas, agrupar informações e identificar oportunidades de negócio.

### Projeto 4 — Indicadores e visualizações

Visualização

Criar gráficos com Python, explicar os resultados e, posteriormente, levar os dados tratados para o Power BI.

### Projeto 5 — Pipeline de dados

Integração

Obter dados de uma API ou arquivo, tratar com Python, armazenar em CSV ou MySQL e gerar uma saída pronta para análise.

## Etapa 17 — Conteúdos complementares para evoluir

Depois de dominar os conteúdos anteriores, você pode estudar:

- Estatística com Python: média, mediana, moda, variância, desvio padrão, correlação, distribuições e testes de hipóteses.
- Análise de dados avançada: detecção de valores atípicos, análise temporal, segmentação e indicadores de negócio.
- Testes e qualidade: testes automatizados, validação de dados e organização de código.
- Performance: operações vetorizadas, uso eficiente de memória e processamento de bases maiores.
- Engenharia de dados: conceitos de data warehouse, orquestração de pipelines e introdução a ferramentas como Airflow e dbt.
- Machine Learning: introdução ao Scikit-learn, preparação de dados, treinamento e avaliação de modelos. É opcional para começar na área de análise de dados.
