# **1. O que é um arquivo CSV?**

CSV significa *Comma-Separated Values* (valores separados por delimitadores).

É um formato utilizado para armazenar dados em formato de tabela, organizados em linhas e colunas.

Imagine uma tabela de funcionários:

| Nome    | Idade | Salário |
| ------- | ----- | ------- |
| Carlos  | 30    | 3500    |
| Mariana | 25    | 4200    |
| João    | 28    | 3900    |

Essas informações poderiam ser armazenadas em um arquivo chamado `funcionarios.csv`:

```
Nome,Idade,Salario
Carlos,30,3500
Mariana,25,4200
João,28,3900
```

Observe que:

- Cada linha representa um registro.
- A primeira linha contém os nomes das colunas.
- As vírgulas separam os valores.

**Importante:** apesar do nome CSV mencionar vírgulas, o arquivo também pode utilizar outros delimitadores, como ponto e vírgula (`;`).

Isso é bastante comum em arquivos exportados do Excel no Brasil.

# **2. O módulo csv**

O Python possui um módulo nativo chamado `csv`, que permite ler e escrever arquivos CSV.

Não precisamos instalar nada.

Para utilizá-lo:

```
import csv
```

O módulo possui diversas funcionalidades. Vamos estudar as principais: `reader()`, `DictReader()`, `writer()` e `DictWriter()`.

# **3. Lendo arquivos CSV com reader()**

Imagine que temos o arquivo `funcionarios.csv`:

```
Nome,Idade,Salario
Carlos,30,3500
Mariana,25,4200
João,28,3900
```

Podemos ler os dados utilizando `csv.reader()`:

```
import csv

with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:    
    leitor = csv.reader(arquivo)    
    
    for linha in leitor:        
        print(linha)
```

Resultado:

```
['Nome', 'Idade', 'Salario']
['Carlos', '30', '3500']
['Mariana', '25', '4200']
['João', '28', '3900']
```

Vamos entender:

- `csv.reader(arquivo)`: cria um leitor para percorrer o CSV.
- `for linha in leitor`: percorre cada linha do arquivo.
- `print(linha)`: exibe os valores daquela linha.

Observe que cada linha é retornada como uma lista.

Por exemplo:

```
['Carlos', '30', '3500']
```

Podemos acessar os valores utilizando índices:

```
print(linha[0])  # Nome
print(linha[1])  # Idade
print(linha[2])  # Salário
```

**Atenção:** os valores lidos pelo `csv.reader()` são strings, mesmo quando representam números.

Por exemplo, `'30'` é uma string, não um inteiro.

# **4. Ignorando o cabeçalho**

Em muitos arquivos CSV, a primeira linha contém os nomes das colunas.

Se quisermos percorrer somente os registros, podemos utilizar `next()`:

```
import csv

with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:    
    leitor = csv.reader(arquivo)    
    
    next(leitor)    
    
    for linha in leitor:        
        print(linha)
```

Resultado:

```
['Carlos', '30', '3500']
['Mariana', '25', '4200']
['João', '28', '3900']
```

O `next()` avança o leitor para a próxima linha. Nesse caso, ele consome o cabeçalho, deixando os registros para o `for`.

# **5. Utilizando DictReader()**

Existe outra maneira de ler arquivos CSV: utilizando `csv.DictReader()`.

A principal diferença é que ele transforma cada registro em um dicionário, utilizando os nomes das colunas como chaves.

Exemplo:

```
import csv

with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:    
    leitor = csv.DictReader(arquivo)    
    
    for linha in leitor:        
        print(linha)
```

Resultado:

```
{'Nome': 'Carlos', 'Idade': '30', 'Salario': '3500'}
{'Nome': 'Mariana', 'Idade': '25', 'Salario': '4200'}
{'Nome': 'João', 'Idade': '28', 'Salario': '3900'}
```

Agora podemos acessar os valores utilizando os nomes das colunas:

```
print(linha['Nome'])
print(linha['Idade'])
print(linha['Salario'])
```

Isso facilita bastante quando estamos trabalhando com tabelas que possuem muitas colunas.

### **Diferença entre reader() e DictReader()**

| `csv.reader()`                             | `csv.DictReader()`                              |
| ------------------------------------------ | ----------------------------------------------- |
| Retorna listas                             | Retorna dicionários                             |
| Acessa valores por índices                 | Acessa valores por nomes de colunas             |
| O cabeçalho é tratado como uma linha comum | Utiliza o cabeçalho como chaves automaticamente |

# **6. Escrevendo arquivos CSV com writer()**

Agora vamos aprender a criar arquivos CSV.

Imagine que queremos gerar um arquivo chamado `produtos.csv`.

Utilizamos `csv.writer()`:

```
import csv

with open('produtos.csv', 'w', encoding='utf-8', newline='') as arquivo:    
    escritor = csv.writer(arquivo)    
    
    escritor.writerow(['Produto', 'Preco', 'Estoque'])    
    escritor.writerow(['Notebook', 3500, 10])    
    escritor.writerow(['Mouse', 80, 50])    
    escritor.writerow(['Teclado', 150, 25])
```

O arquivo gerado terá este conteúdo:

```
Produto,Preco,Estoque
Notebook,3500,10
Mouse,80,50
Teclado,150,25
```

Vamos entender os métodos:

- `csv.writer(arquivo)`: cria um escritor CSV.
- `writerow()`: escreve uma linha no arquivo.
- `newline=''`: evita problemas de linhas em branco extras, especialmente no Windows.

Também podemos escrever várias linhas de uma só vez utilizando `writerows()`:

```
import csv

with open('produtos.csv', 'w', encoding='utf-8', newline='') as arquivo:    
    escritor = csv.writer(arquivo)    
    
    dados = [        
        ['Produto', 'Preco', 'Estoque'],        
        ['Notebook', 3500, 10],        
        ['Mouse', 80, 50],        
        ['Teclado', 150, 25]    
    ]    
    
    escritor.writerows(dados)
```

A diferença:

| Método        | Função                |
| ------------- | --------------------- |
| `writerow()`  | Escreve uma linha     |
| `writerows()` | Escreve várias linhas |

# **7. Escrevendo CSV com DictWriter()**

Assim como temos o `DictReader()`, também temos o `DictWriter()`.

Ele permite escrever arquivos CSV utilizando dicionários.

Exemplo:

```
import csv

with open('funcionarios.csv', 'w', encoding='utf-8', newline='') as arquivo:    
    campos = ['Nome', 'Idade', 'Salario']    
    
    escritor = csv.DictWriter(arquivo, fieldnames=campos)    
    
    escritor.writeheader()    
    
    escritor.writerow({        
        'Nome': 'Carlos',        
        'Idade': 30,        
        'Salario': 3500    
    })    
    
    escritor.writerow({        
        'Nome': 'Mariana',        
        'Idade': 25,        
        'Salario': 4200    
    })
```

Resultado:

```
Nome,Idade,Salario
Carlos,30,3500
Mariana,25,4200
```

Entenda os métodos:

- `fieldnames`: define os nomes e a ordem das colunas.
- `writeheader()`: escreve o cabeçalho.
- `writerow()`: escreve um registro utilizando um dicionário.

# **8. Trabalhando com delimitadores**

Até agora, utilizamos vírgulas para separar os valores.

Mas imagine que recebemos um arquivo assim:

```
Nome;Idade;Salario
Carlos;30;3500
Mariana;25;4200
João;28;3900
```

Nesse caso, o delimitador é o ponto e vírgula (`;`).

Precisamos informar isso ao leitor:

```
import csv

with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:    
    leitor = csv.reader(arquivo, delimiter=';')    
    
    for linha in leitor:        
        print(linha)
```

Também podemos utilizar `delimiter=';'` com `DictReader()`, `writer()` e `DictWriter()`.

**Importante:** o delimitador precisa corresponder ao utilizado no arquivo. Caso contrário, o Python pode interpretar uma linha inteira como uma única coluna.

# **9. Valores ausentes em arquivos CSV**

Imagine que recebemos o seguinte arquivo:

```
Nome,Idade,Salario
Carlos,30,3500
Mariana,,4200
João,28,
```

Observe que existem valores ausentes:

- Mariana não possui idade informada.
- João não possui salário informado.

Quando utilizamos `csv.reader()` ou `csv.DictReader()`, esses campos normalmente são retornados como strings vazias (`''`).

Exemplo:

```
import csv

with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:    
    leitor = csv.DictReader(arquivo)    
    
    for linha in leitor:        
        if linha['Idade'] == '':            
            print(f"{linha['Nome']} está sem idade.")
```

Resultado:

```
Mariana está sem idade.
```

Nesse exemplo, utilizamos uma condição para identificar os campos vazios.

Lembre-se: o módulo `csv` não realiza automaticamente o tratamento dos dados. Ele apenas lê e escreve as informações. A análise e o tratamento ficam por nossa conta.

# **Resumo geral**

| Recurso            | Finalidade                               |
| ------------------ | ---------------------------------------- |
| `import csv`       | Importa o módulo                         |
| `csv.reader()`     | Lê CSV como listas                       |
| `csv.DictReader()` | Lê CSV como dicionários                  |
| `next()`           | Avança para a próxima linha              |
| `csv.writer()`     | Escreve CSV com listas                   |
| `writerow()`       | Escreve uma linha                        |
| `writerows()`      | Escreve várias linhas                    |
| `csv.DictWriter()` | Escreve CSV com dicionários              |
| `writeheader()`    | Escreve o cabeçalho                      |
| `fieldnames`       | Define as colunas                        |
| `delimiter`        | Define o separador                       |
| `newline=''`       | Evita linhas em branco extras na escrita |
