# **Tratamento de entradas inválidas**

- **Verificação de valores:** conferir se um valor atende a uma condição.
- **Tratamento de entradas inválidas:** identificar valores inadequados e apresentar uma resposta apropriada.

### **1. Identificando valores inválidos**

Imagine um sistema que solicita a idade de uma pessoa.

Uma idade negativa não faz sentido nesse contexto. Podemos identificar esse caso com uma condição:

```python
idade = int(input('Digite sua idade: '))

if idade < 0:    
    print('Idade inválida')
else:    
    print('Idade registrada')
```

Se o usuário informar `-5`, o programa exibirá `Idade inválida`.

Se informar `25`, exibirá `Idade registrada`.

### **2. Apresentando mensagens para entradas inválidas**

Quando identificamos um valor inadequado, podemos utilizar `print()` para explicar o problema ao usuário.

Exemplo: quantidade de produtos.

```python
quantidade = int(input('Digite a quantidade: '))

if quantidade <= 0:    
    print('Erro: a quantidade deve ser maior que zero')
else:    
    print('Quantidade registrada com sucesso')
```

Observe que não basta identificar o problema. A mensagem também ajuda o usuário a entender o que precisa corrigir.

### **3. Impedindo o processamento de valores inválidos**

Outro cuidado importante é evitar que o programa realize cálculos utilizando valores inadequados.

Imagine um sistema que calcula o preço total de uma compra:

```python
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade: '))

if preco <= 0:    
    print('Preço inválido')
elif quantidade <= 0:    
    print('Quantidade inválida')
else:    
    total = preco * quantidade    
    print(f'Total da compra: R$ {total:.2f}')
```

O cálculo só acontece quando o preço e a quantidade são válidos.

Isso é importante porque evita resultados incorretos.

### **4. Atenção ao tipo de entrada**

Existe uma diferença entre informar um valor inadequado e informar um valor que não pode ser convertido para o tipo esperado.

Por exemplo:

```python
idade = int(input('Digite sua idade: '))
```

Se o usuário digitar `25`, a conversão funciona.

Se digitar `abc`, Python apresentará um erro durante a conversão.
