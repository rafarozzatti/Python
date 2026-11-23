# **1. Abrindo arquivos com&#x20;**`open()`

Para trabalhar com arquivos, utilizamos a função nativa `open()`.

Sua estrutura básica é:

```
open('nome_do_arquivo', 'modo')
```

Ela recebe principalmente dois argumentos:

- **Nome do arquivo:** indica qual arquivo queremos acessar.
- **Modo:** define o que queremos fazer com ele, como ler ou escrever.

Os principais modos são:

| Modo  | Função                                                   |
| ----- | -------------------------------------------------------- |
| `'r'` | Ler um arquivo existente                                 |
| `'w'` | Escrever em um arquivo, substituindo o conteúdo anterior |
| `'a'` | Adicionar conteúdo ao final do arquivo                   |
| `'x'` | Criar um arquivo novo, gerando erro se ele já existir    |

Vamos estudar cada um.

# **2. Lendo arquivos com&#x20;**`r`

Imagine que temos um arquivo chamado `dados.txt` com o seguinte conteúdo:

```
Nome: Rafael
Idade: 27
Profissão: Analista de Dados
```

Podemos ler seu conteúdo assim:

```
arquivo = open('dados.txt', 'r')

conteudo = arquivo.read()

print(conteudo)

arquivo.close()
```

Resultado:

```
Nome: Rafael
Idade: 27
Profissão: Analista de Dados
```

Entenda os métodos:

- `open()`: abre o arquivo.
- `read()`: lê todo o conteúdo do arquivo.
- `close()`: fecha o arquivo após a utilização.

**Importante:** se tentarmos abrir um arquivo inexistente utilizando `'r'`, Python apresentará um `FileNotFoundError`.

## **3. Lendo linha por linha com&#x20;**`readline()`

O método `readline()` lê uma linha por vez.

Exemplo:

```
arquivo = open('dados.txt', 'r')

linha1 = arquivo.readline()
linha2 = arquivo.readline()

print(linha1)
print(linha2)

arquivo.close()
```

Resultado:

```
Nome: Rafael

Idade: 27
```

Cada chamada de `readline()` avança para a próxima linha.

## **4. Lendo todas as linhas com&#x20;**`readlines()`

O método `readlines()` lê todas as linhas e retorna uma lista.

```
arquivo = open('dados.txt', 'r')

linhas = arquivo.readlines()

print(linhas)

arquivo.close()
```

Resultado:

```
['Nome: Rafael\n', 'Idade: 27\n', 'Profissão: Analista de Dados']
```

Observe que cada linha pode conter `\n`, que representa uma quebra de linha.

A diferença entre os três métodos:

| Método        | Retorno                        |
| ------------- | ------------------------------ |
| `read()`      | Uma string com todo o conteúdo |
| `readline()`  | Uma string com uma linha       |
| `readlines()` | Uma lista contendo as linhas   |

# **5. Utilizando&#x20;**`with open()`

Existe uma maneira mais recomendada de abrir arquivos: utilizando `with`.

Exemplo:

```
with open('dados.txt', 'r') as arquivo:    
    conteudo = arquivo.read()    
    print(conteudo)
```

Observe que não precisamos utilizar `close()`.

O `with` fecha o arquivo automaticamente quando o bloco de código termina, inclusive se ocorrer algum erro durante a execução.

Essa é a forma que recomendo utilizar no dia a dia.

# **6. Escrevendo arquivos com&#x20;**`w`

Agora imagine que queremos criar um arquivo ou substituir seu conteúdo.

Utilizamos o modo `'w'`:

```
with open('dados.txt', 'w') as arquivo:    
    arquivo.write('Olá, Python!')
```

Se o arquivo não existir, ele será criado.

Se já existir, seu conteúdo anterior será substituído.

O método `write()` escreve o conteúdo informado no arquivo.

Também podemos escrever várias linhas:

```
with open('dados.txt', 'w') as arquivo:    
    arquivo.write('Nome: Rafael\n')    
    arquivo.write('Idade: 27\n')    
    arquivo.write('Profissão: Analista de Dados')
```

O `\n` cria uma quebra de linha.

O conteúdo salvo será:

```
Nome: Rafael
Idade: 27
Profissão: Analista de Dados
```

# **7. Adicionando conteúdo com&#x20;**`a`

Se quisermos adicionar informações sem apagar o conteúdo existente, utilizamos o modo `'a'`.

Exemplo:

```
with open('dados.txt', 'a') as arquivo:    
    arquivo.write('\nCidade: São Paulo')
```

O conteúdo anterior será mantido, e a nova informação será adicionada ao final.

**Diferença importante:**

- `'w'`: substitui o conteúdo.
- `'a'`: mantém o conteúdo e adiciona novas informações.

# **8. Criando arquivos com&#x20;**`x`

O modo `'x'` serve exclusivamente para criar um arquivo novo.

```
with open('novo_arquivo.txt', 'x') as arquivo:    
    arquivo.write('Arquivo criado com sucesso!')
```

Se o arquivo já existir, Python apresentará um `FileExistsError`.

É útil quando queremos evitar substituir acidentalmente um arquivo existente.

# **9. Codificação UTF-8**

Ao trabalhar com arquivos, podemos encontrar problemas com acentos e caracteres especiais.

Por exemplo:

```
Informação
Análise
São Paulo
```

Para evitar problemas de codificação, podemos informar o parâmetro `encoding='utf-8'` ao abrir o arquivo.

**Para leitura:**

```
with open('dados.txt', 'r', encoding='utf-8') as arquivo:    
    conteudo = arquivo.read()
```

**Para escrita:**

```
with open('dados.txt', 'w', encoding='utf-8') as arquivo:    
    arquivo.write('Análise de Dados')
```

O UTF-8 é uma codificação muito utilizada para representar caracteres de diferentes idiomas.

Recomendo utilizar `encoding='utf-8'` sempre que trabalhar com arquivos de texto, especialmente quando houver acentuação.

## **Resumo geral**

| Recurso            | Finalidade                             |
| ------------------ | -------------------------------------- |
| `open()`           | Abrir arquivos                         |
| `read()`           | Ler todo o conteúdo                    |
| `readline()`       | Ler uma linha                          |
| `readlines()`      | Ler todas as linhas em uma lista       |
| `write()`          | Escrever conteúdo                      |
| `close()`          | Fechar o arquivo                       |
| `with open()`      | Abrir e fechar automaticamente         |
| `'r'`              | Modo de leitura                        |
| `'w'`              | Modo de escrita, substituindo conteúdo |
| `'a'`              | Adicionar conteúdo                     |
| `'x'`              | Criar arquivo novo                     |
| `encoding='utf-8'` | Definir a codificação do texto         |
