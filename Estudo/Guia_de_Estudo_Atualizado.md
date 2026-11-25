# **Roteiro completo — Python do zero à Análise de Dados**

## **Etapa 1 — Fundamentos de Python**

**Objetivo:** aprender a sintaxe e os conceitos básicos da linguagem.

1\. **Introdução ao Python**

- O que é Python e para que serve.
- Como executar programas.
- Estrutura básica de um programa.
- `print()`.
- Comentários.

2\. **Variáveis e tipos de dados**

- Criação e atribuição de variáveis.
- Regras para nomes de variáveis.
- Tipos `int`, `float`, `str` e `bool`.
- Função `type()`.

3\. **Conversão de tipos**

- `int()`, `float()`, `str()` e `bool()`.
- Conversões entre tipos.
- Conversões válidas e inválidas.

4\. **Entrada e saída de dados**

- `input()`.
- `print()`.
- Concatenação.
- F-strings.

5\. **Operadores aritméticos**

- Adição, subtração, multiplicação e divisão.
- Divisão inteira (`//`).
- Resto da divisão (`%`).
- Potenciação (`**`).
- Precedência dos operadores.

6\. **Operadores de comparação e lógicos**

- `==`, `!=`, `>`, `<`, `>=` e `<=`.
- `and`, `or` e `not`.
- Combinação de condições.

7\. **Operadores de atribuição**

- `=`, `+=`, `-=`, `*=`, `/=`.
- `//=`, `%=` e `**=`.

## **Etapa 2 — Condições e lógica**

**Objetivo:** fazer o programa tomar decisões com base em condições.

1\. **Estruturas condicionais**

- `if`, `elif` e `else`.
- Condições simples e compostas.
- Identação e blocos condicionais.

2\. **Condições aninhadas e operadores**

- Condições dentro de outras condições.
- Utilização de `and`, `or` e `not`.
- Operador `in`.
- Combinação de diferentes condições.

3\. **Validação de entradas**

- Verificação de valores informados.
- Tratamento de entradas inválidas.
- Validação de números e textos.
- Diferentes cenários de execução.

4\. **Aplicações práticas**

- Classificação de dados.
- Cálculos condicionais.
- Regras de negócio.
- Situações práticas envolvendo decisões.

## **Etapa 3 — Estruturas de repetição**

**Objetivo:** automatizar tarefas e executar operações repetidamente.

1\. **Laços de repetição**

- `while`.
- `for`.
- Função `range()`.
- Diferenças entre `while` e `for`.

2\. **Controle de repetições**

- Contadores.
- Acumuladores.
- Condições de parada.
- Repetições controladas por entradas.

3\. **Controle de fluxo**

- `break`.
- `continue`.
- Laços aninhados.

4\. **Aplicações práticas**

- Soma e média de valores.
- Contagem de ocorrências.
- Identificação de maior e menor valor.
- Tabuadas e sequências numéricas.
- Processamento repetitivo de informações.

## **Etapa 4 — Estruturas de dados**

**Objetivo:** aprender a armazenar, organizar, acessar e manipular conjuntos de informações.

1\. **Strings**

- Criação e manipulação.
- Índices positivos e negativos.
- Fatiamento (*slicing*).
- Imutabilidade.
- Métodos:
  - `upper()`, `lower()`, `capitalize()` e `title()`.
  - `strip()`, `replace()` e `split()`.
  - `join()`, `find()` e `count()`.
  - `startswith()` e `endswith()`.

2\. **Listas**

- Criação e acesso aos elementos.
- Índices e *slicing*.
- Alteração de elementos.
- Adição e remoção de elementos.
- Métodos:
  - `append()`, `extend()` e `insert()`.
  - `pop()` e `remove()`.
  - `sort()` e `reverse()`.
  - `index()`, `count()` e `clear()`.
- Ordenação crescente e decrescente.

3\. **Tuplas**

- Criação e acesso.
- Índices e *slicing*.
- Imutabilidade.
- Métodos `count()` e `index()`.
- Diferenças entre listas e tuplas.

4\. **Sets (conjuntos)**

- Criação de conjuntos.
- Elementos únicos.
- Adição e remoção.
- União, interseção e diferença.
- Métodos de manipulação.

5\. **Dicionários**

- Criação de dicionários.
- Chaves e valores.
- Acesso e alteração de informações.
- Adição e remoção de elementos.
- Iteração sobre dicionários.
- Métodos:
  - `keys()`, `values()` e `items()`.
  - `get()`, `update()` e `pop()`.
  - `clear()`.
- Verificação da existência de chaves.

6\. **Estruturas de dados aninhadas**

- Listas dentro de listas.
- Dicionários dentro de dicionários.
- Listas dentro de dicionários.
- Dicionários dentro de listas.
- Acesso e manipulação de estruturas aninhadas.

7\. **Iteráveis e iteradores**

- O que são objetos iteráveis.
- Diferença entre iteráveis e iteradores.
- Função `iter()`.
- Função `next()`.
- Relação com o `for`.

8\. **Comprehensions**

- List comprehensions.
- Dictionary comprehensions.
- Set comprehensions.
- Condições dentro de comprehensions.

9\. **Mutabilidade e cópias**

- Tipos mutáveis e imutáveis.
- Referências de objetos.
- Diferença entre atribuição e cópia.
- Cópia rasa (*shallow copy*).
- Cópia profunda (*deep copy*).
- Módulo `copy`.

## **Etapa 5 — Funções**

**Objetivo:** organizar o código, evitar repetições e criar funcionalidades reutilizáveis.

1\. **Fundamentos de funções**

- Definição com `def`.
- Chamada de funções.
- Parâmetros e argumentos.
- Funções com e sem parâmetros.

2\. **Tipos de argumentos**

- Argumentos posicionais.
- Argumentos nomeados.
- Valores padrão.
- `*args`.
- `**kwargs`.

3\. **Retorno de valores**

- Diferença entre `return` e `print()`.
- Retorno de valores.
- Retorno de múltiplos valores.
- Retorno de listas e dicionários.

4\. **Escopo de variáveis**

- Variáveis locais e globais.
- Palavra-chave `global`.
- Noções de `nonlocal`.

5\. **Funções lambda**

- O que são funções anônimas.
- Sintaxe `lambda`.
- Quando utilizar.

6\. **Funções e recursos nativos**

- `len()`, `sum()`, `min()` e `max()`.
- `sorted()` e `round()`.
- `enumerate()` e `zip()`.

7\. **Funções aplicadas às estruturas de dados**

- Funções que recebem listas e dicionários.
- Funções que retornam estruturas de dados.
- Funções que recebem outras funções.
- Composição de funções.

8\. **Boas práticas**

- Nomes de funções.
- Responsabilidade de cada função.
- Reutilização e organização.
- Legibilidade do código.

## **Etapa 6 — Organização e qualidade do código**

**Objetivo:** desenvolver programas mais organizados, confiáveis e fáceis de manter.

1\. **Módulos e importações**

- `import`.
- `from ... import`.
- `as`.
- Criação e utilização de módulos próprios.
- Bibliotecas padrão:
  - `math`.
  - `random`.
  - `datetime`.
  - `os`.
  - `sys`.

2\. **Organização de arquivos e módulos**

- Arquivos Python separados.
- Importação entre arquivos.
- Organização de pastas e pacotes.
- Docstrings.

3\. **Tratamento de erros e exceções**

- `try`, `except`, `else` e `finally`.
- Exceções comuns:
  - `ValueError`.
  - `TypeError`.
  - `IndexError`.
  - `KeyError`.
  - `ZeroDivisionError`.
  - `FileNotFoundError`.
- Utilização de `raise`.

4\. **Depuração (*debugging*)**

- Leitura de mensagens de erro.
- Interpretação de *tracebacks*.
- Identificação de erros.
- Breakpoints e execução passo a passo.

5\. **Ambientes virtuais e dependências**

- O que são ambientes virtuais.
- Criação de ambientes com `venv`.
- Instalação de bibliotecas com `pip`.
- Arquivo `requirements.txt`.

6\. **Testes e boas práticas**

- Testes com `assert`.
- Introdução ao `pytest`.
- Testes simples.
- Nomenclatura e legibilidade.
- Manutenção do código.

7\. **Git básico**

- O que é controle de versão.
- `git init`.
- `git status`.
- `git add`.
- `git commit`.

## **Etapa 7 — Arquivos e dados externos**

**Objetivo:** aprender a ler, escrever e manipular informações armazenadas em arquivos.

1\. **Caminhos e diretórios — introdução**

- O que são caminhos de arquivos.
- Caminhos absolutos e relativos.
- Diretório de trabalho.
- Localização de arquivos.

2\. **Arquivos TXT**

- Abertura com `open()`.
- Modos:
  - `r`: leitura.
  - `w`: escrita e sobrescrita.
  - `a`: acréscimo.
  - `x`: criação exclusiva.
- Fechamento com `close()`.
- Gerenciamento com `with`.
- Leitura:
  - `read()`.
  - `readline()`.
  - `readlines()`.
- Escrita:
  - `write()`.
  - `writelines()`.
- Leitura, sobrescrita e acréscimo de informações.

3\. **Codificação de arquivos**

- O que é codificação de caracteres.
- UTF-8.
- Outras codificações.
- Problemas com acentuação.
- Parâmetro `encoding`.

4\. **Arquivos CSV**

- O que é CSV.
- Biblioteca `csv`.
- `csv.reader()`.
- `csv.writer()`.
- `csv.DictReader()`.
- `csv.DictWriter()`.
- Cabeçalhos e delimitadores.
- Leitura e escrita de linhas e colunas.
- Tratamento de valores ausentes.

5\. **Arquivos JSON**

- O que é JSON.
- Relação entre JSON e estruturas de dados Python.
- `json.load()`.
- `json.dump()`.
- `json.loads()`.
- `json.dumps()`.
- Parâmetro `indent`.
- Leitura, alteração e gravação de dados JSON.

6\. **Biblioteca pathlib**

- Classe `Path`.
- Caminhos absolutos e relativos.
- `exists()`.
- `mkdir()`.
- `glob()` e `rglob()`.
- Verificação e manipulação de arquivos e pastas.

7\. **Manipulação de múltiplos arquivos**

- Leitura de vários CSVs e JSONs.
- Escrita de múltiplos arquivos.
- Organização de arquivos.
- Tratamento de erros.
- Automatização de tarefas com arquivos.

## **Etapa 8 — Programação Orientada a Objetos (POO)**

**Objetivo:** compreender como estruturar programas utilizando classes e objetos.

1\. **Fundamentos de POO**

- O que é programação orientada a objetos.
- Classes e objetos.
- Atributos e métodos.
- Método construtor `__init__`.
- Parâmetro `self`.
- Atributos de instância e de classe.

2\. **Encapsulamento**

- Conceito de encapsulamento.
- Atributos públicos e privados como convenções.
- Métodos de acesso.
- `@property`.

3\. **Herança e polimorfismo**

- Herança entre classes.
- Reutilização de código.
- Sobrescrita de métodos.
- Polimorfismo.

4\. **Métodos especiais e decoradores**

- `__str__`.
- `__repr__`.
- `__len__`.
- `__eq__`.
- `@classmethod`.
- `@staticmethod`.

5\. **Composição e organização**

- Composição entre classes.
- Relação entre objetos.
- Organização de classes em módulos.

## **Etapa 9 — NumPy**

**Objetivo:** aprender a trabalhar com cálculos numéricos e arrays de maneira eficiente.

1\. **Introdução ao NumPy**

- O que é NumPy.
- Instalação e importação.
- Diferenças entre listas e arrays.
- Criação com `np.array()`.
- Tipos de dados com `dtype`.
- `zeros()`, `ones()`, `arange()` e `linspace()`.

2\. **Dimensões e matrizes**

- Arrays unidimensionais e multidimensionais.
- `shape`, `ndim` e `size`.
- Indexação.
- Slicing.
- Alteração de elementos.

3\. **Operações com arrays**

- Vetorização.
- Operações aritméticas entre arrays.
- Broadcasting.
- Comparações entre elementos.

4\. **Agregações e estatística**

- `sum()`, `mean()`, `min()` e `max()`.
- `std()`.
- Parâmetro `axis`.
- Estatísticas básicas.

5\. **Filtros e operações adicionais**

- Máscaras booleanas.
- Filtragem de valores.
- Valores ausentes com `NaN`.
- `isnan()` e `nanmean()`.
- Ordenação.
- Noções de álgebra matricial.

## **Etapa 10 — Pandas**

**Objetivo:** aprender a importar, explorar, limpar, transformar e analisar dados.

1\. **Introdução ao Pandas**

- O que é Pandas.
- Instalação e importação.
- Series.
- DataFrames.
- Criação de estruturas.
- Diferenças entre Series e DataFrames.

2\. **Importação e exportação**

- `read_csv()`.
- `read_excel()`.
- `read_json()`.
- Exportação com `to_csv()`, `to_excel()` e `to_json()`.
- Importação de diferentes fontes.

3\. **Inspeção e exploração de dados**

- `head()` e `tail()`.
- `shape`.
- `info()`.
- `describe()`.
- `columns`, `dtypes` e `index`.
- `unique()` e `nunique()`.
- Exploração inicial de bases.

4\. **Seleção, filtros e ordenação**

- Seleção de colunas e linhas.
- `loc[]` e `iloc[]`.
- Filtros simples e compostos.
- `isin()` e `between()`.
- `sort_values()` e `sort_index()`.

5\. **Limpeza e tratamento de dados**

- `isna()` e `isnull()`.
- `fillna()` e `dropna()`.
- `drop_duplicates()`.
- `astype()`.
- `to_datetime()`.
- Manipulação de textos com `.str`.
- `rename()` e `drop()`.
- Tratamento de dados inconsistentes.
- Verificação da qualidade dos dados.

6\. **Criação e transformação de dados**

- Criação de colunas.
- Alteração de valores.
- `apply()` e `map()`.
- Operações vetorizadas.
- Transformações condicionais.
- Criação de indicadores.

7\. **Agrupamento e agregação**

- `groupby()`.
- `agg()`.
- `value_counts()`.
- Agrupamento por uma ou várias colunas.
- Cálculo de indicadores e estatísticas.

8\. **Junção de dados**

- `merge()`.
- `join()`.
- `concat()`.
- Tipos de junção.
- Integração de diferentes fontes.

9\. **Reorganização de dados**

- `pivot_table()`.
- `melt()`.
- Transformação do formato dos dados.
- Reorganização de tabelas.

10\. **Boas práticas e validação**

- Organização do fluxo de análise.
- Verificação dos resultados.
- Consistência dos dados.
- Legibilidade e eficiência.

## **Etapa 11 — Visualização de dados**

**Objetivo:** aprender a construir gráficos e comunicar resultados.

1\. **Matplotlib**

- O que é Matplotlib.
- Instalação e importação.
- Figuras e eixos.
- Criação de gráficos.
- Personalização.

2\. **Tipos de gráficos**

- Gráficos de barras.
- Gráficos de linhas.
- Gráficos de dispersão.
- Histogramas.
- Gráficos de setores.

3\. **Personalização de gráficos**

- Títulos.
- Eixos.
- Legendas.
- Escalas.
- Rótulos.
- Anotações.
- Salvamento de gráficos.

4\. **Seaborn**

- Introdução à biblioteca.
- Distribuições.
- Histogramas e KDE.
- Gráficos de barras.
- Boxplots.
- Gráficos de dispersão.
- Heatmaps.
- Análise de relações entre variáveis.

5\. **Interpretação e comunicação**

- Escolha do gráfico adequado.
- Identificação de tendências e padrões.
- Identificação de outliers.
- Análise de distribuições.
- Comparação de resultados.
- Comunicação de informações por meio de gráficos.

## **Etapa 12 — APIs e coleta de dados**

**Objetivo:** aprender a obter informações de fontes externas utilizando Python.

1\. **Fundamentos de APIs e HTTP**

- O que é uma API.
- Comunicação cliente-servidor.
- Requisições e respostas.
- Métodos GET e POST.
- Códigos de status HTTP.

2\. **Biblioteca requests**

- Instalação e importação.
- Requisições GET e POST.
- Parâmetros.
- Headers.
- Conteúdo das respostas.
- Obtenção de dados JSON.

3\. **Recursos e tratamento de requisições**

- Paginação.
- Autenticação.
- Chaves e credenciais.
- Timeout.
- Falhas de requisição.
- Rate limits.
- Respostas inválidas.
- Consumo de APIs públicas.

4\. **Integração com análise de dados**

- Transformação de respostas em listas e dicionários.
- Conversão para DataFrames.
- Tratamento com Pandas.
- Exportação para CSV e JSON.

## **Etapa 13 — Python com SQL e bancos de dados**

**Objetivo:** conectar Python a bancos de dados e integrar consultas SQL aos processos de análise.

1\. **Revisão de bancos relacionais e SQL**

- Conceitos de bancos relacionais.
- Tabelas, registros e colunas.
- `SELECT`.
- `WHERE`.
- `ORDER BY`.
- `GROUP BY`.
- Funções de agregação.
- `JOIN`.
- Subqueries quando necessárias.
- `INSERT`, `UPDATE` e `DELETE`.
- Conexão com MySQL e bibliotecas necessárias.

2\. **Consultas e manipulação com Python**

- Conexão Python e MySQL.
- Execução de consultas `SELECT`.
- Aplicação de filtros e ordenações.
- Inserção, atualização e exclusão de registros.
- Leitura de resultados em listas e dicionários.

3\. **Parâmetros, transações e segurança**

- Consultas parametrizadas.
- Prevenção contra SQL Injection.
- `commit()` e `rollback()`.
- Transações.
- Tratamento de erros.
- Fechamento de conexões.

4\. **SQLAlchemy e integração com Pandas**

- Introdução ao SQLAlchemy.
- Conexões com bancos de dados.
- Consultas.
- Leitura de dados em DataFrames.
- Integração Python, SQL e Pandas.
- Exportação para CSV e Excel.

## **Etapa 14 — ETL e automação de processos**

**Objetivo:** utilizar Python para integrar, transformar e disponibilizar dados automaticamente.

1\. **Fundamentos de ETL**

- O que é ETL.
- Extração, transformação e carregamento.
- Diferença entre ETL e ELT.
- Conceito de pipelines de dados.

2\. **Extração de dados**

- Extração de CSV.
- Extração de Excel.
- Extração de APIs.
- Extração de bancos SQL.
- Integração de diferentes fontes.

3\. **Transformação de dados**

- Padronização de informações.
- Limpeza de dados.
- Tratamento de valores ausentes.
- Remoção de duplicatas.
- Conversão de tipos.
- Junção de bases.
- Aplicação de regras de negócio.
- Validação dos dados com Pandas.

4\. **Carregamento de dados**

- Exportação de arquivos.
- Carregamento em bancos de dados.
- Preparação de dados para ferramentas de BI.
- Organização dos resultados.

5\. **Automação de processos**

- Criação de scripts automatizados.
- Separação das etapas do pipeline.
- Tratamento de falhas.
- Logs.
- Processamento incremental.
- Idempotência.
- Agendamento de tarefas.
- Monitoramento e documentação.

## **Etapa 15 — Git, GitHub e portfólio**

**Objetivo:** organizar, versionar e apresentar projetos de Python e Análise de Dados.

1\. **Git e GitHub**

- Diferença entre Git e GitHub.
- Repositórios.
- Versionamento.
- `git init`, `status`, `add`, `commit`, `push`.

2\. **Histórico e gerenciamento**

- `git log`.
- `git clone`.
- `git pull`.
- Branches.
- `git branch`.
- `git switch` e `git checkout`.
- Resolução de conflitos.
- Arquivo `.gitignore`.

3\. **Organização e documentação**

- Estrutura de pastas.
- Criação de README.
- Descrição dos objetivos.
- Ferramentas utilizadas.
- Resultados obtidos.
- Dependências e `requirements.txt`.
- Proteção de credenciais.
- Organização do histórico de alterações.

4\. **Construção de portfólio**

- Projetos de fundamentos de Python.
- Limpeza e tratamento de dados.
- Análise exploratória (EDA).
- Projetos com NumPy e Pandas.
- Visualização de dados.
- Integração com SQL.
- Consumo de APIs.
- Pipelines ETL.
- Integração com Power BI.
- Publicação e apresentação dos projetos.
