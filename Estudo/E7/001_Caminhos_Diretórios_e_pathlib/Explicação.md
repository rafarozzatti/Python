# **Caminhos, diretórios e&#x20;**`pathlib`

Neste assunto, vamos aprender como o Python identifica a localização de arquivos e pastas, como navegar entre diretórios e como trabalhar com caminhos de maneira organizada.

## **1. O que são arquivos e diretórios?**

Antes de começar, precisamos entender dois conceitos:

- **Arquivo:** contém informações, como um documento `.txt`, uma planilha `.csv` ou um arquivo `.json`.
- **Diretório:** é uma pasta utilizada para organizar arquivos e outras pastas.

Imagine esta estrutura:

**projeto_python**

dados.txt

vendas.csv

clientes.json

**relatorios**

resumo.txt

O Python consegue acessar esses arquivos desde que saibamos informar seus caminhos.

## **2. O que são caminhos (paths)?**

Um caminho é o endereço que indica onde um arquivo ou diretório está localizado no computador.

Existem dois tipos principais.

### **Caminho absoluto**

É o endereço completo de um arquivo ou pasta, começando pela localização principal do sistema.

Exemplo no Windows:

```
C:\Users\Rafael\Documents\projeto_python\dados.txt
```

Exemplo no Linux:

```
/home/rafael/projeto_python/dados.txt
```

O caminho absoluto informa exatamente onde o arquivo está.

### **Caminho relativo**

É um endereço definido a partir do diretório de referência do programa, normalmente o diretório de trabalho atual.

Imagine esta estrutura:

```
projeto_python/
│
├── main.py
├── dados.txt
│
└── arquivos/
    └── vendas.csv
```

Se o diretório de trabalho atual for `projeto_python`, podemos acessar os arquivos utilizando:

```
'dados.txt'
```

Ou:

```
'arquivos/vendas.csv'
```

Não precisamos informar o endereço completo do computador.

### **Diferença entre eles**

| Absoluto                               | Relativo                                  |
| -------------------------------------- | ----------------------------------------- |
| Endereço completo                      | Endereço a partir de uma referência       |
| Independente do diretório de trabalho  | Depende do diretório de trabalho          |
| Pode ser específico de cada computador | Geralmente facilita compartilhar projetos |

## **3. O que é o diretório de trabalho atual?**

O diretório de trabalho atual (*current working directory*) é a pasta que o Python utiliza como referência para interpretar caminhos relativos.

Podemos descobrir qual é utilizando o módulo `os`:

```
import os

print(os.getcwd())
```

O método `getcwd()` retorna o caminho absoluto do diretório de trabalho atual.

Por exemplo:

```
C:\Users\Rafael\Documents\projeto_python
```

Também podemos alterar o diretório de trabalho com:

```
os.chdir('C:/Users/Rafael/Documents')
```

O método `chdir()` muda o diretório de trabalho do programa.

**Importante:** alterar o diretório de trabalho pode mudar a interpretação dos caminhos relativos. Por isso, precisamos saber qual é a referência utilizada pelo programa.

## **4. O que é o pathlib?**

O `pathlib` é um módulo nativo do Python que permite trabalhar com caminhos de arquivos e diretórios de maneira mais simples e organizada.

Ele oferece recursos para criar, consultar e manipular caminhos.

Primeiro, precisamos importar `Path`:

```
from pathlib import Path
```

`Path` é a classe utilizada para representar caminhos.

Podemos criar um caminho assim:

```
from pathlib import Path

arquivo = Path('dados.txt')

print(arquivo)
```

Resultado:

```
dados.txt
```

Nesse exemplo, criamos um objeto que representa o caminho do arquivo. Isso não significa que o arquivo já existe.

## **5. Caminhos absolutos com pathlib**

Podemos criar caminhos absolutos:

```
from pathlib import Path

arquivo = Path('C:/Users/Rafael/Documents/dados.txt')

print(arquivo)
```

Também podemos descobrir o caminho absoluto de um caminho relativo utilizando `resolve()`:

```
from pathlib import Path

arquivo = Path('dados.txt')

print(arquivo.resolve())
```

O método `resolve()` retorna o caminho absoluto correspondente.

## **6. Consultando informações de arquivos e diretórios**

O `pathlib` possui métodos que permitem verificar informações sobre um caminho.

Vamos conhecer os principais.

`exists()`**&#x20;— verifica se o caminho existe.**

```
from pathlib import Path

arquivo = Path('dados.txt')

print(arquivo.exists())
```

Retorna `True` se o caminho existir e `False` caso contrário.

`is_file()`**&#x20;— verifica se é um arquivo.**

```
print(arquivo.is_file())
```

`is_dir()`**&#x20;— verifica se é um diretório.**

```
pasta = Path('relatorios')

print(pasta.is_dir())
```

Esses métodos retornam valores booleanos.

## **7. Obtendo informações do caminho**

Também podemos extrair partes de um caminho utilizando propriedades do `Path`.

```
from pathlib import Path

arquivo = Path('projeto_python/relatorios/vendas.csv')

print(arquivo.name)
print(arquivo.stem)
print(arquivo.suffix)
print(arquivo.parent)
```

Resultado:

```
vendas.csv
vendas
.csv
projeto_python/relatorios
```

Entenda cada propriedade:

| Propriedade | Retorno                                             |
| ----------- | --------------------------------------------------- |
| `.name`     | Nome completo do arquivo                            |
| `.stem`     | Nome sem a extensão                                 |
| `.suffix`   | Extensão do arquivo                                 |
| `.parent`   | Diretório pai, ou seja, a pasta imediatamente acima |

## **8. Juntando caminhos com pathlib**

Uma das funcionalidades mais úteis do `pathlib` é construir caminhos sem precisar concatenar textos manualmente.

Observe:

```
from pathlib import Path

pasta = Path('projeto_python')
arquivo = pasta / 'dados.txt'

print(arquivo)
```

Resultado:

```
projeto_python/dados.txt
```

O operador `/` permite juntar partes do caminho.

Podemos fazer isso com vários níveis:

```
from pathlib import Path

pasta = Path('projeto_python')

arquivo = pasta / 'dados' / 'vendas.csv'

print(arquivo)
```

Resultado:

```
projeto_python/dados/vendas.csv
```

O próprio `pathlib` adapta os separadores de caminho ao sistema operacional.

## **9. Criando diretórios**

Também podemos criar pastas com o `pathlib`.

Utilizamos o método `mkdir()`:

```
from pathlib import Path

pasta = Path('relatorios')

pasta.mkdir()
```

Esse comando cria uma pasta chamada `relatorios` no diretório de trabalho atual.

Podemos utilizar `parents=True` para criar também os diretórios intermediários:

```
from pathlib import Path

pasta = Path('projeto/arquivos/relatorios')

pasta.mkdir(parents=True)
```

Assim, se as pastas `projeto` e `arquivos` ainda não existirem, elas também serão criadas.

Existe ainda a opção `exist_ok=True`:

```
pasta.mkdir(parents=True, exist_ok=True)
```

Ela evita um erro caso o diretório já exista.

## **Resumo do assunto**

| Recurso          | Finalidade                             |
| ---------------- | -------------------------------------- |
| Caminho absoluto | Endereço completo                      |
| Caminho relativo | Endereço a partir de uma referência    |
| `os.getcwd()`    | Consulta o diretório de trabalho atual |
| `os.chdir()`     | Altera o diretório de trabalho         |
| `Path()`         | Cria um objeto de caminho              |
| `resolve()`      | Obtém o caminho absoluto               |
| `exists()`       | Verifica se o caminho existe           |
| `is_file()`      | Verifica se é arquivo                  |
| `is_dir()`       | Verifica se é diretório                |
| `.name`          | Obtém o nome completo                  |
| `.stem`          | Obtém o nome sem extensão              |
| `.suffix`        | Obtém a extensão                       |
| `.parent`        | Obtém o diretório pai                  |
| `mkdir()`        | Cria diretórios                        |
