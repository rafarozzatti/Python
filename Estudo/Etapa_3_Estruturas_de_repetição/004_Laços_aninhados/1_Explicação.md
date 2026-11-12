# 1. Laços aninhados

Laços aninhados são estruturas de repetição colocadas uma dentro da outra.

Podemos usar um `for` dentro de outro `for`, um `while` dentro de outro `while` ou combinar `for` e `while`.

Imagine que você queira imprimir os números de 1 a 3 três vezes. Poderia fazer assim:

```
for i in range(1, 4):    
    for j in range(1, 4):        
        print(j)
```

Saída:

```
1
2
3
1
2
3
1
2
3
```

## 2. Como o código funciona?

Vamos entender cada laço:

```
for i in range(1, 4):    
    for j in range(1, 4):        
        print(j)
```

Laço externo:

```
for i in range(1, 4):
```

Controla quantas vezes o bloco interno será repetido. Nesse exemplo, ele executa 3 vezes, com `i` valendo 1, 2 e 3.

Laço interno:

```
for j in range(1, 4):    
    print(j)
```

A cada repetição do laço externo, o laço interno executa todas as suas 3 repetições.

### Visualizando as repetições

Cada linha representa uma repetição do laço externo.

Quando i = 1

## 1

## 2

## 3

Quando i = 2

## 1

## 2

## 3

Quando i = 3

## 1

## 2

## 3

O laço externo executa 3 vezes e o interno executa 3 vezes para cada uma delas: 3 × 3 = 9 execuções do `print()`.

## 3. Laços aninhados com variáveis diferentes

É comum utilizar uma variável para o laço externo e outra para o interno, como `i` e `j`.

Veja este exemplo:

```
for i in range(1, 4):    
    for j in range(1, 3):        
        print(f'i = {i}, j = {j}')
```

Saída:

```
i = 1, j = 1
i = 1, j = 2
i = 2, j = 1
i = 2, j = 2
i = 3, j = 1
i = 3, j = 2
```

Observe que `j` volta a começar em 1 sempre que uma nova repetição de `i` começa.

O laço externo tem 3 repetições, e o interno tem 2 para cada repetição externa. Portanto, o `print()` é executado \\(3 \times 2 = 6\\) vezes.

## 4. Laços aninhados com `while`

Também podemos colocar um `while` dentro de outro `while`.

```
i = 1

while i <= 3:    
    j = 1    
    
    while j <= 2:        
        print(f'i = {i}, j = {j}')        
        j += 1    
        
    i += 1
```

A saída é a mesma do exemplo anterior.

Atenção a dois detalhes importantes:

- `j = 1` fica dentro do laço externo para reiniciar o contador interno a cada nova repetição de `i`.
- `j += 1` precisa estar dentro do laço interno para que ele termine. Da mesma forma, `i += 1` atualiza o contador externo.

Se esquecer de atualizar um contador, pode ocorrer um loop infinito.

## 5. Quando usar laços aninhados?

Eles são úteis quando precisamos repetir uma operação dentro de outra repetição, por exemplo:

- Exibir tabuada de vários números.
- Montar padrões com linhas e colunas.
- Percorrer tabelas de dados.
- Comparar elementos de duas listas.

Uma regra para guardar: o laço interno termina todas as suas repetições antes de o laço externo avançar para a próxima repetição.
