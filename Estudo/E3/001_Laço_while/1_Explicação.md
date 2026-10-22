# 1. Laço `while`?

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

## 3. Cuidado com o loop infinito

Observe este código:

```
contador = 1

while contador <= 5:    
    print(contador)
```

O problema é que o contador nunca muda. Como continua valendo `1`, a condição `contador <= 5` permanece verdadeira e o programa não para sozinho.

Por isso, em muitos laços `while`, precisamos atualizar alguma variável ou alterar a condição para que a repetição termine.
