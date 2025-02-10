# Tratamento de Exceções em Python: `try/except` com `else` e `finally`

O tratamento de exceções em Python é feito com `try/except`, permitindo capturar erros e evitar que o programa seja interrompido. Podemos aprimorar esse tratamento com `else` e `finally`, tornando o código mais organizado e robusto.

---

## **1. Estrutura Básica de `try/except`**

```python
try:
    # Tenta executar este bloco de código
    resultado = 10 / 0  # Isso gera um erro ZeroDivisionError
except ZeroDivisionError:
    # Captura o erro e executa este bloco
    print("Erro: Divisão por zero não é permitida!")
```

**Saída:**
```
Erro: Divisão por zero não é permitida!
```

---

## **2. Usando `try/except` com `else`**

O bloco `else` é executado apenas se nenhuma exceção ocorrer no bloco `try`.

```python
try:
    # Tenta executar este código
    numero = int(input("Digite um número: "))
    print(f"Você digitou: {numero}")
except ValueError:
    # Captura erro caso o usuário não digite um número
    print("Erro: Você deve digitar um número inteiro!")
else:
    # Executado apenas se não houver erro
    print("Conversão realizada com sucesso!")
```

**Exemplo de entrada e saída:**
```
Digite um número: 42
Você digitou: 42
Conversão realizada com sucesso!
```

```
Digite um número: abc
Erro: Você deve digitar um número inteiro!
```

---

## **3. Usando `try/except` com `finally`**

O bloco `finally` sempre é executado, independentemente de ocorrer ou não uma exceção. Isso é útil para limpar recursos como arquivos e conexões.

```python
try:
    arquivo = open("dados.txt", "r")  # Abre um arquivo para leitura
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado!")
finally:
    # Fecha o arquivo, mesmo que tenha ocorrido erro
    print("Finalizando operação.")
    arquivo.close()
```

**Saída caso o arquivo não exista:**
```
Erro: O arquivo não foi encontrado!
Finalizando operação.
```

---

## **4. Usando `try/except` com `else` e `finally` juntos**

Podemos combinar `else` e `finally` para tornar o código mais eficiente.

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro: Você deve digitar um número inteiro!")
else:
    print(f"Você digitou o número {numero}")
finally:
    print("Execução finalizada.")
```

**Exemplo de entrada e saída:**
```
Digite um número: 10
Você digitou o número 10
Execução finalizada.
```

```
Digite um número: abc
Erro: Você deve digitar um número inteiro!
Execução finalizada.
```

---

## **Quando usar `try/except/else/finally`?** ✅
- **`try/except`**: Sempre que houver possibilidade de erro (exemplo: divisão por zero, leitura de arquivos, entrada de usuário).
- **`else`**: Quando deseja executar um código apenas se não houver erro.
- **`finally`**: Para garantir que um recurso seja liberado (exemplo: fechar arquivos, conexões de banco de dados).

## **Quando evitar?** ❌
- **Evitar capturar exceções genéricas** (`except Exception:`) sem necessidade.
- **Não usar `try/except` para fluxos normais de controle** (use validações antes de tentar executar códigos arriscados).

---

## **Conclusão**
O uso de `try/except` com `else` e `finally` torna o tratamento de erros mais seguro e organizado, garantindo que o programa lide bem com falhas sem interromper a execução.
