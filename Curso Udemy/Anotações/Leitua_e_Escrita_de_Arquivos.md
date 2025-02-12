# Leitura de Arquivos em Python

A leitura de arquivos em Python é feita utilizando a função `open()`, que permite abrir arquivos em diferentes modos, como leitura (`'r'`), escrita (`'w'`), adição (`'a'`) e modos binários (`'rb'`, `'wb'`).

---

## **1. Abrindo e lendo um arquivo**
A maneira mais simples de ler um arquivo é usando o modo de leitura `'r'`.

```python
# Abre o arquivo 'exemplo.txt' no modo de leitura ('r')
arquivo = open('exemplo.txt', 'r')

# Lê todo o conteúdo do arquivo e armazena na variável conteudo
conteudo = arquivo.read()

# Exibe o conteúdo do arquivo
print(conteudo)

# Fecha o arquivo para liberar recursos
arquivo.close()

# Verifica se o arquivo foi fechado
print(arquivo.closed)  # True se estiver fechado
```

### **Saída (supondo que o arquivo contém o texto "Olá, Mundo!")**
```
Olá, Mundo!
True
```

---

## **2. Usando `seek()` para mover o cursor do arquivo**
O método `seek()` permite mover o cursor para uma posição específica dentro do arquivo.

```python
# Abre o arquivo no modo leitura
with open('exemplo.txt', 'r') as arquivo:
    print(arquivo.read(5))  # Lê os primeiros 5 caracteres
    arquivo.seek(0)  # Retorna ao início do arquivo
    print(arquivo.read(5))  # Lê novamente os primeiros 5 caracteres
```

### **Saída**
```
Olá, 
Olá, 
```

---

## **3. Trabalhando com `StringIO` (arquivos em memória)**
O `StringIO` permite manipular strings como se fossem arquivos.

```python
from io import StringIO

# Criando um "arquivo" na memória
arquivo = StringIO("Linha 1\nLinha 2\nLinha 3")

# Lendo o conteúdo
print(arquivo.read())

# Movendo o cursor para o início e lendo linha por linha
arquivo.seek(0)
for linha in arquivo:
    print(linha.strip())
```

### **Saída**
```
Linha 1
Linha 2
Linha 3
Linha 1
Linha 2
Linha 3
```

---

## **4. Escrevendo em um arquivo (`'w'`)**
O modo `'w'` cria um novo arquivo ou sobrescreve um arquivo existente.

```python
# Abre o arquivo no modo escrita ('w')
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# Verifica se o arquivo foi fechado automaticamente
print(arquivo.closed)  # True
```

---

## **5. Adicionando conteúdo a um arquivo (`'a'`)**
O modo `'a'` (append) permite adicionar texto a um arquivo existente sem sobrescrever o conteúdo anterior.

```python
# Abre o arquivo no modo de adição ('a')
with open('exemplo.txt', 'a') as arquivo:
    arquivo.write("Terceira linha\n")
```

---

## **6. Quando usar cada método de leitura?** ✅❌

| Método          | Quando usar | Quando evitar |
|----------------|------------|---------------|
| `read()`       | Para ler arquivos pequenos de uma só vez. | Arquivos grandes podem consumir muita memória. |
| `readline()`   | Quando precisamos ler apenas uma linha. | Não é eficiente para arquivos grandes. |
| `readlines()`  | Quando queremos todas as linhas como uma lista. | Pode consumir muita memória em arquivos grandes. |
| Iteração com `for` | Para processar arquivos grandes de maneira eficiente, linha por linha. | Não há desvantagens significativas. |
| `seek()` / `tell()` | Quando precisamos reposicionar ou obter a posição do cursor. | Pode ser confuso se não souber a posição exata. |
| `truncate()`   | Para reduzir o tamanho do arquivo. | Se não quiser perder dados acidentalmente. |

---

