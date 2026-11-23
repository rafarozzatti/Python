# Tratamento de erros

O tratamento de erros permite que um programa identifique situações inesperadas e execute ações para lidar com elas, em vez de simplesmente interromper a execução.

## **1. try e except**

O `try` contém o código que pode gerar um erro. O `except` define o que será executado caso esse erro aconteça.

**Exemplo:**

```
try:    
    numero = int(input("Digite um número: "))    
    resultado = 100 / numero    
    
    print(resultado)
    
except:    
    print("Ocorreu um erro.")
```

Nesse exemplo:

- Se o usuário digitar `10`, o resultado será `10.0`.
- Se digitar `0`, ocorrerá um erro de divisão por zero.
- Se digitar `"abc"`, ocorrerá um erro de conversão.

Nos dois últimos casos, o `except` será executado.

## **2. Tratamento de exceções específicas**

Em Python, podemos identificar exatamente qual tipo de erro aconteceu.

Isso é melhor do que utilizar um `except` genérico, pois permite apresentar mensagens diferentes para cada situação.

### **ValueError**

Acontece quando um valor possui um formato inadequado para determinada operação.

```
try:    
    idade = int(input("Digite sua idade: "))
    
except ValueError:    
    print("Digite um número válido.")
```

Se o usuário digitar `"abc"`, o Python não conseguirá converter esse texto para inteiro e gerará um `ValueError`.

### **ZeroDivisionError**

Acontece quando tentamos dividir um número por zero.

```
try:    
    resultado = 10 / 0
    
except ZeroDivisionError:    
    print("Não é possível dividir por zero.")
```

### **TypeError**

Acontece quando tentamos realizar uma operação incompatível entre tipos de dados.

```
try:    
    resultado = "Python" + 10
    
except TypeError:    
    print("Não é possível somar texto com número.")
```

### **IndexError**

Acontece quando tentamos acessar uma posição inexistente em uma lista ou sequência.

```
try:    
    numeros = [10, 20, 30]    
    
    print(numeros[5])
    
except IndexError:    
    print("Essa posição não existe na lista.")
```

### **KeyError**

Acontece quando tentamos acessar uma chave que não existe em um dicionário.

```
try:    
    pessoa = {"nome": "Carlos", "idade": 25}    
    
    print(pessoa["cidade"])
    
except KeyError:    
    print("Essa chave não existe no dicionário.")
```

### **FileNotFoundError**

Acontece quando tentamos acessar um arquivo que não foi encontrado.

```
try:    
    arquivo = open("dados.txt", "r")
    
except FileNotFoundError:    
    print("Arquivo não encontrado.")
```

## **3. Múltiplos except**

Podemos utilizar vários blocos `except` para tratar diferentes erros dentro de um mesmo `try`.

**Exemplo:**

```
try:    
    numero1 = int(input("Digite o primeiro número: "))    
    numero2 = int(input("Digite o segundo número: "))    
    
    resultado = numero1 / numero2    
    
    print(resultado)
    
except ValueError:    
    print("Digite apenas números.")
    
except ZeroDivisionError:    
    print("Não é possível dividir por zero.")
    
except TypeError:    
    print("Ocorreu um erro de tipo.")
```

O Python executa o `except` correspondente ao erro que aconteceu.

Atenção: depois que uma exceção acontece dentro do `try`, as instruções restantes daquele bloco não são executadas.

## **4. else**

O `else` é executado somente quando nenhuma exceção acontece dentro do `try`.

**Exemplo:**

```
try:    
    numero = int(input("Digite um número: "))
    
except ValueError:    
    print("Valor inválido.")
    
else:    
    print(f"Número digitado: {numero}")
```

Funcionamento:

- Se o usuário digitar `20`, o `else` será executado.
- Se digitar `"abc"`, o `except` será executado.
- O `else` não será executado quando ocorrer uma exceção no `try`.

## **5. finally**

O `finally` é executado independentemente de ocorrer ou não uma exceção.

É utilizado principalmente para executar ações de encerramento, como fechar arquivos ou liberar recursos.

**Exemplo:**

```
try:    
    numero = int(input("Digite um número: "))
    
except ValueError:    
    print("Valor inválido.")
    
finally:    
    print("Programa finalizado.")
```

Independentemente de o usuário digitar um número ou um texto inválido, a mensagem final será exibida.

## **6. Utilizando try, except, else e finally juntos**

Podemos combinar todos esses recursos em um único programa.

**Exemplo:**

```
try:    
    numero1 = int(input("Digite o primeiro número: "))    
    numero2 = int(input("Digite o segundo número: "))    
    
    resultado = numero1 / numero2
    
except ValueError:    
    print("Digite apenas números.")
    
except ZeroDivisionError:    
    print("Não é possível dividir por zero.")
    
else:    
    print(f"Resultado: {resultado}")
    
finally:    
    print("Operação encerrada.")
```

A ordem é sempre:

1. `try`: tenta executar o código.
2. `except`: trata uma exceção, se acontecer.
3. `else`: executa se não houver exceção.
4. `finally`: executa independentemente do resultado.

## **7. Resumo das principais exceções**

| Exceção               | Quando acontece                    |
| --------------------- | ---------------------------------- |
| `ValueError`          | Valor inadequado para uma operação |
| `TypeError`           | Operação incompatível entre tipos  |
| `ZeroDivisionError`   | Divisão por zero                   |
| `IndexError`          | Índice inexistente                 |
| `KeyError`            | Chave inexistente no dicionário    |
| `FileNotFoundError`   | Arquivo não encontrado             |
| `NameError`           | Variável ou nome não definido      |
| `AttributeError`      | Atributo ou método inexistente     |
| `ImportError`         | Falha ao importar algo             |
| `ModuleNotFoundError` | Módulo não encontrado              |

## **8. Capturando a mensagem do erro com&#x20;**`as`

Também podemos armazenar a mensagem original da exceção em uma variável utilizando `as`.

**Exemplo:**

```
try:    
    numero = int("abc")
    
except ValueError as erro:    
    print(erro)
```

Nesse caso, `erro` recebe a mensagem gerada pelo Python, explicando o motivo da falha.

Isso é útil para entender o que aconteceu durante a execução do programa.

## **Resumo geral**

| Recurso              | Função                                 |
| -------------------- | -------------------------------------- |
| `try`                | Executa código que pode gerar erro     |
| `except`             | Trata uma exceção                      |
| `except TipoErro`    | Trata uma exceção específica           |
| `except ... as erro` | Armazena a mensagem da exceção         |
| `else`               | Executa quando não ocorre exceção      |
| `finally`            | Executa independentemente do resultado |
