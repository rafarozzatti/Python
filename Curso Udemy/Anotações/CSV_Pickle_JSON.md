# Manipulação de Arquivos CSV, Pickle e JSON em Python

A manipulação de arquivos é essencial para salvar e carregar dados em diferentes formatos. Python oferece suporte nativo para manipular arquivos **CSV**, **Pickle** e **JSON**, cada um com suas vantagens.

---

## **1. Manipulação de Arquivos CSV**

### **Escrevendo em um arquivo CSV**

```python
import csv

# Criando uma lista de dicionários com os dados
dados = [
    {"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"}
]

# Nome do arquivo CSV
arquivo_csv = "dados.csv"

# Escrevendo os dados no arquivo CSV
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    colunas = ["Nome", "Idade", "Cidade"]  # Definindo os cabeçalhos
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    
    escritor.writeheader()  # Escrevendo os cabeçalhos
    escritor.writerows(dados)  # Escrevendo as linhas

print("Arquivo CSV criado com sucesso!")
```

### **Lendo um arquivo CSV**

```python
# Abrindo o arquivo CSV para leitura
with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)  # Cada linha é um dicionário
```

**Saída:**
```
{'Nome': 'Alice', 'Idade': '25', 'Cidade': 'São Paulo'}
{'Nome': 'Bruno', 'Idade': '30', 'Cidade': 'Rio de Janeiro'}
{'Nome': 'Carlos', 'Idade': '22', 'Cidade': 'Belo Horizonte'}
```

---

## **2. Manipulação de Arquivos Pickle**

O **Pickle** é usado para serializar e desserializar objetos Python de forma binária.

### **Escrevendo em um arquivo Pickle**

```python
import pickle

# Dados a serem serializados
dados = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Nome do arquivo pickle
arquivo_pickle = "dados.pkl"

# Salvando o dicionário em um arquivo binário
with open(arquivo_pickle, mode="wb") as arquivo:
    pickle.dump(dados, arquivo)

print("Arquivo Pickle criado com sucesso!")
```

### **Lendo um arquivo Pickle**

```python
# Abrindo o arquivo Pickle para leitura
with open(arquivo_pickle, mode="rb") as arquivo:
    dados_carregados = pickle.load(arquivo)
    print(dados_carregados)  # Exibindo os dados recuperados
```

**Saída:**
```
{'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}
```

**Vantagem do Pickle:** Suporta qualquer tipo de objeto Python, incluindo listas, dicionários, e classes.

---

## **3. Manipulação de Arquivos JSON**

O **JSON (JavaScript Object Notation)** é um formato amplamente utilizado para armazenar e transferir dados de forma estruturada.

### **Escrevendo em um arquivo JSON**

```python
import json

# Criando um dicionário com os dados
dados = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Nome do arquivo JSON
arquivo_json = "dados.json"

# Salvando os dados no formato JSON
with open(arquivo_json, mode="w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Arquivo JSON criado com sucesso!")
```

### **Lendo um arquivo JSON**

```python
# Abrindo o arquivo JSON para leitura
with open(arquivo_json, mode="r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)  # Exibindo os dados recuperados
```

**Saída:**
```
{
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São Paulo'
}
```

**Vantagem do JSON:** Facilidade de compartilhamento entre diferentes linguagens de programação e legibilidade.

---

## **Conclusão**

- **CSV**: Melhor para tabelas e dados tabulares.
- **Pickle**: Melhor para armazenar objetos Python complexos.
- **JSON**: Melhor para compartilhar dados entre diferentes sistemas.
