# 1. Laço `while`

O `while` é uma estrutura de repetição. Ele executa um bloco de código enquanto uma condição for verdadeira.

Imagine que você queira imprimir os números de 1 até 5. Sem um laço, precisaria escrever vários comandos `print()`. Com `while`, podemos fazer isso de maneira mais simples.

```
contador = 1

while contador <= 5:    
    print(contador)    
    contador = contador + 1
```

Saída:

```
1
2
3
4
5
```

## 2. Entendendo o código

1\. Inicialização

```
contador = 1
```

Define o valor inicial do contador.

2\. Condição

```
while contador <= 5:
```

Enquanto o contador for menor ou igual a 5, o bloco será executado.

3\. Comando repetido

```
print(contador)
```

Mostra o valor atual do contador.

4\. Atualização

```
contador = contador + 1
```

Aumenta o contador em 1 para que a condição eventualmente se torne falsa.

## 3. Entendendo o operador `!=`

O operador `!=` significa diferente de.

Ele compara dois valores e verifica se eles são diferentes. O resultado será `True` (verdadeiro) ou `False` (falso).

| Operador | Significado      | Exemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `==`     | Igual a          | `5 == 5` | `True`    |
| `!=`     | Diferente de     | `5 != 3` | `True`    |
| `!=`     | Diferente de     | `5 != 5` | `False`   |
| `>`      | Maior que        | `5 > 3`  | `True`    |
| `<`      | Menor que        | `5 < 3`  | `False`   |
| `>=`     | Maior ou igual a | `5 >= 5` | `True`    |
| `<=`     | Menor ou igual a | `3 <= 5` | `True`    |

O ponto principal é que `!=` verifica se os valores não são iguais.

## 4. Como usar `while` com `!=`

Veja este exemplo:

```
contador = 5

while contador != 0:    
    print(contador)    
    contador = contador - 1
    
print('Fim')
```

Saída:

```
5
4
3
2
1
Fim
```

Vamos entender o que acontece:

## 1

Primeira verificação

`contador != 0` → `5 != 0` → `True`

Como 5 é diferente de 0, o laço executa.

## 2

O contador diminui

`contador = contador - 1`

O valor passa de 5 para 4. O laço verifica a condição novamente e continua enquanto o contador for diferente de 0.

## 3

Quando chega a zero

`contador != 0` → `0 != 0` → `False`

A condição deixa de ser verdadeira, então o laço termina. O programa continua na linha seguinte e imprime `Fim`.

### Qual é a diferença entre `<=` e `!=` nesse caso?

- `while contador <= 5:` repete enquanto o contador for menor ou igual a 5.
- `while contador != 0:` repete enquanto o contador for diferente de zero.

Ambos podem controlar uma repetição, mas as condições verificam coisas diferentes.

## 5. Usando `while` para receber dados até um valor de parada

O `!=` também é útil quando não sabemos quantas vezes o laço precisará executar.

```
numero = int(input('Digite um número (0 para parar): '))

while numero != 0:    
    print(f'Você digitou: {numero}')    
    numero = int(input('Digite outro número (0 para parar): '))
    
print('Programa encerrado')
```

Nesse exemplo:

1. O programa pede um número.
2. Se ele for diferente de zero, o número é exibido.
3. O programa pede outro número e verifica a condição novamente.
4. Quando você digita `0`, a condição `numero != 0` se torna falsa e o laço termina.

O zero funciona como um valor de parada. Esse tipo de valor também é chamado de sentinela.

## 6. Cuidado com o loop infinito

Observe:

```
contador = 1

while contador <= 5:    
    print(contador)
```

O contador nunca muda. Como continua valendo 1, a condição permanece verdadeira e o programa não para sozinho.

O mesmo problema pode ocorrer com `!=`:

```
contador = 5

while contador != 0:    
    print(contador)
```

Como o contador nunca diminui, ele permanece em 5, que é diferente de 0. Portanto, o laço continua indefinidamente.
