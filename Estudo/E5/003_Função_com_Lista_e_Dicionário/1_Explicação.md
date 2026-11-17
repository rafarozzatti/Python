# ** Funções com listas e dicionários**

Neste assunto, vamos aprender a utilizar funções para trabalhar diretamente com listas e dicionários.

Isso é bastante útil em análise de dados, pois frequentemente precisamos receber conjuntos de informações, processá-los e devolver resultados.

## **1. Funções que recebem listas**

Uma função pode receber uma lista como parâmetro, assim como recebia números e textos.

Exemplo:

```
def mostrar_numeros(numeros):    for numero in numeros:        print(numero)valores = [10, 20, 30, 40]mostrar_numeros(valores)
```

Saída:

```
10
20
30
40
```

Observe que:

- `numeros` é o parâmetro da função.
- `valores` é a lista enviada como argumento.
- O `for` percorre os elementos da lista.

## **2. Calculando informações de uma lista**

Podemos criar funções para analisar os dados de uma lista.

Exemplo:

```
def analisar_vendas(vendas):    total = sum(vendas)    media = total / len(vendas)    maior_venda = max(vendas)    return total, media, maior_vendavalores = [100, 200, 300, 400]total, media, maior = analisar_vendas(valores)print(total)print(media)print(maior)
```

Saída:

```
1000
250.0
400
```

Aqui combinamos:

- Listas como parâmetros.
- Funções integradas.
- Cálculos.
- Retorno de múltiplos valores.

## **3. Alterando uma lista dentro de uma função**

Também podemos modificar uma lista recebida como parâmetro.

Exemplo:

```
def adicionar_produto(produtos, produto):    produtos.append(produto)lista = ['Notebook', 'Mouse']adicionar_produto(lista, 'Teclado')print(lista)
```

Saída:

```
['Notebook', 'Mouse', 'Teclado']
```

**Por que a lista original foi alterada?**

Porque listas são estruturas mutáveis. Quando passamos uma lista para uma função, ela pode modificar a própria lista recebida.

Isso significa que a alteração permanece mesmo depois que a função termina.

## **4. Funções que recebem dicionários**

O mesmo princípio funciona com dicionários.

Exemplo:

```
def mostrar_funcionario(funcionario):    print(f"Nome: {funcionario['nome']}")    print(f"Cargo: {funcionario['cargo']}")    print(f"Salário: R$ {funcionario['salario']}")dados = {    'nome': 'Rafael',    'cargo': 'Analista de Dados',    'salario': 3500}mostrar_funcionario(dados)
```

Saída:

```
Nome: Rafael
Cargo: Analista de Dados
Salário: R$ 3500
```

Observe que acessamos os valores pelas chaves do dicionário.

## **5. Alterando um dicionário dentro de uma função**

Podemos adicionar ou modificar informações de um dicionário dentro de uma função.

Exemplo:

```
def atualizar_salario(funcionario, novo_salario):    funcionario['salario'] = novo_salariodados = {    'nome': 'Carlos',    'salario': 3000}atualizar_salario(dados, 4000)print(dados)
```

Saída:

```
{'nome': 'Carlos', 'salario': 4000}
```

Assim como acontece com listas, a alteração permanece no dicionário original.

## **6. Retornando um novo dicionário**

Uma função também pode receber informações e devolver um dicionário.

Exemplo:

```
def criar_produto(nome, preco, estoque):    produto = {        'nome': nome,        'preco': preco,        'estoque': estoque    }    return produtoresultado = criar_produto('Monitor', 1200, 15)print(resultado)
```

Saída:

```
{'nome': 'Monitor', 'preco': 1200, 'estoque': 15}
```

Nesse caso, a função cria um novo dicionário e o devolve com `return`.

## **Resumo do conteúdo**

| Conceito              | Aplicação                                  |
| --------------------- | ------------------------------------------ |
| Receber listas        | Percorrer e analisar elementos             |
| Modificar listas      | Utilizar `append()`, alterar posições etc. |
| Receber dicionários   | Acessar informações pelas chaves           |
| Modificar dicionários | Adicionar ou atualizar informações         |
| Retornar dicionários  | Criar e devolver estruturas de dados       |
