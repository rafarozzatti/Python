# 10. Formatação de textos com f-strings

As f-strings permitem inserir variáveis e expressões dentro de um texto, facilitando a criação de mensagens e a apresentação de resultados.

Imagine que você tenha estas variáveis:

```
nome = "Rafael"
idade = 27
```

Uma maneira de exibir os valores seria:

```
print("Nome:", nome)
print("Idade:", idade)
```

Saída:

```
Nome: Rafael
Idade: 27
```

Mas podemos fazer isso de uma forma mais prática usando f-strings.

## 2. Como utilizar uma f-string

Para criar uma f-string, coloque a letra `f` antes das aspas e escreva o nome da variável entre chaves `{}`.

```
nome = "Rafael"
idade = 27

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Saída:

```
Meu nome é Rafael e tenho 27 anos.
```

Observe três detalhes:

- A letra `f` aparece antes das aspas.
- As variáveis ficam dentro de `{}`.
- O restante do texto permanece normal.

Sem o `f`, as chaves não são substituídas pelos valores das variáveis.

```
nome = "Rafael"
print("Meu nome é {nome}")
```

Saída:

```
Meu nome é {nome}
```

## 3. Inserindo cálculos em f-strings

Você também pode colocar expressões matemáticas entre chaves, sem precisar criar outra variável.

```
preco = 50
quantidade = 3

print(f"Total da compra: R$ {preco * quantidade}")
```

Saída:

```
Total da compra: R$ 150
```

Nesse caso, o Python calcula `preco * quantidade` e insere o resultado no texto.

Você pode utilizar operações que já estudou, como soma, subtração, multiplicação e divisão.

Outro exemplo:

```
a = 10
b = 5

print(f"A soma é {a + b}")
print(f"A diferença é {a - b}")
```

Saída:

```
A soma é 15
A diferença é 5
```

## 4. Formatando números decimais

As f-strings também permitem controlar a quantidade de casas decimais exibidas.

Para isso, utilizamos `:.2f` dentro das chaves.

```
preco = 19.999
print(f"Preço: R$ {preco:.2f}")
```

Saída:

```
Preço: R$ 20.00
```

Entenda a estrutura:

- `:` inicia a especificação de formatação.
- `.2` indica duas casas decimais.
- `f` indica a formatação numérica de ponto flutuante.

Mais um exemplo:

```
media = 7.4568

print(f"Média: {media:.2f}")
print(f"Média: {media:.1f}")
```

Saída:

```
Média: 7.46
Média: 7.5
```

O Python arredonda o número exibido para a quantidade de casas decimais solicitada. Isso não altera o valor original da variável.

## 5. Organizando valores em textos

Podemos misturar texto, variáveis e cálculos em uma única mensagem.

```
produto = "Teclado"
preco = 120
quantidade = 2

total = preco * quantidade

print(f"Produto: {produto}")print(f"Preço unitário: R$ {preco:.2f}")print(f"Quantidade: {quantidade}")print(f"Total: R$ {total:.2f}")
```

Saída:

```
Produto: Teclado
Preço unitário: R$ 120.00
Quantidade: 2
Total: R$ 240.00
```

Esse recurso é bastante útil para exibir resultados de cálculos, relatórios e análises de dados.
