# 1. O comando `break`

O `break` interrompe completamente o laço de repetição, mesmo que a condição ainda permita continuar.

Por exemplo:

```
for numero in range(1, 11):    
    if numero == 5:        
        break    
    print(numero)
    
print('Fim do programa')
```

Saída:

```
1
2
3
4
Fim do programa
```

## Entendendo o código

1. O `for` começa a percorrer os números de 1 até 10.
2. Quando `numero` vale 5, a condição `numero == 5` se torna verdadeira.
3. O `break` interrompe o laço imediatamente.
4. O número 5 não é impresso, porque o `break` acontece antes do `print()`.
5. O programa continua executando o código que está depois do laço.

Atenção: `break` não encerra o programa inteiro. Ele encerra apenas o laço em que está.

## 2. O comando `continue`

O `continue` funciona de maneira diferente: ele pula o restante da execução daquela repetição e passa para a próxima, sem encerrar o laço.

Veja o exemplo:

```
for numero in range(1, 6):    
    if numero == 3:        
        continue    
    print(numero)
    
print('Fim do programa')
```

Saída:

```
1
2
4
5
Fim do programa
```

## Entendendo o código

1. O laço começa com o número 1.
2. Quando chega ao número 3, a condição `numero == 3` é verdadeira.
3. O `continue` pula o `print(numero)` daquela repetição.
4. O laço continua com o número 4 e depois com o 5.
5. Como não existe `break`, o laço termina normalmente quando os valores acabam.

Perceba que o número 3 foi ignorado, mas o laço não foi encerrado.

## 3. Diferença entre `break` e `continue`

`break` — parar

Interrompe o laço imediatamente. Nenhuma outra repetição daquele laço será executada.

`continue` — pular

Ignora o restante da repetição atual e passa para a próxima.

Compare os resultados usando os números de 1 a 5:

| Comando    | Quando o número é 3  | Resultado       |
| ---------- | -------------------- | --------------- |
| `break`    | Encerra o laço       | `1, 2`          |
| `continue` | Pula apenas o 3      | `1, 2, 4, 5`    |
| Nenhum     | Continua normalmente | `1, 2, 3, 4, 5` |

## 4. Usando `break` e `continue` com `while`

Os dois comandos também funcionam com `while`.

### Exemplo com `break`

```
numero = 1

while numero <= 5:    
    if numero == 4:        
        break    
    print(numero)    
    numero += 1
```

Saída:

```
1
2
3
```

Quando `numero` chega a 4, o `break` encerra o laço.

### Exemplo com `continue`

```
numero = 0

while numero < 5:    
    numero += 1    
    
    if numero == 3:        
        continue    
        
    print(numero)
```

Saída:

```
1
2
4
5
```

Aqui, o contador é atualizado antes do `continue`. Isso é importante: se a atualização estivesse depois dele, o programa poderia ficar preso em um loop infinito quando `numero` chegasse a 3.

## 5. Quando usar cada um?

- Use `break` quando quiser parar a repetição antes de ela terminar naturalmente, como quando encontrar um registro ou receber um comando de encerramento.
- Use `continue` quando quiser ignorar determinados valores e continuar processando os demais, como pular números negativos ou registros que não atendem a uma condição.

O ponto principal é lembrar: `break` encerra o laço; `continue` pula apenas a repetição atual.
