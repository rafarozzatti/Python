# Testes com&#x20;`assert`&#x20;e introdução ao&#x20;`pytest`

O objetivo é aprender como verificar se um código está funcionando corretamente e como automatizar essas verificações.

## **1. O que são testes em Python?**

Testes são verificações realizadas para confirmar se um programa está produzindo os resultados esperados.

Imagine uma função que calcula a soma de dois números:

```
def somar(a, b):    
    return a + b
    
resultado = somar(10, 5)

print(resultado)
```

Resultado:

```
15
```

O código funciona, mas como podemos verificar automaticamente se o resultado está correto?

É aí que entram os testes.

## **2. O que é o assert?**

O `assert` é um comando utilizado para verificar se uma condição é verdadeira.

Sua estrutura é:

```
assert condição
```

Se a condição for verdadeira, o programa continua normalmente.

Se for falsa, Python gera um erro chamado `AssertionError`.

**Exemplo 1 — Condição verdadeira:**

```
idade = 25

assert idade >= 18

print('Verificação concluída!')
```

Resultado:

```
Verificação concluída!
```

A condição `idade >= 18` é verdadeira, então o programa continua.

**Exemplo 2 — Condição falsa:**

```
idade = 15

assert idade >= 18

print('Verificação concluída!')
```

Resultado:

```
AssertionError
```

Como a condição é falsa, o programa interrompe a execução naquele ponto.

## **3. Assert com mensagens personalizadas**

Também podemos adicionar uma mensagem para explicar o motivo da falha:

```
idade = 15

assert idade >= 18, 'A idade precisa ser maior ou igual a 18'

print('Verificação concluída!')
```

Resultado:

```
AssertionError: A idade precisa ser maior ou igual a 18
```

Isso facilita identificar o que não passou na verificação.

## **4. Utilizando assert para testar funções**

Podemos utilizar o `assert` para verificar se uma função retorna o resultado esperado.

Veja:

```
def multiplicar(a, b):    
    return a * b
    
assert multiplicar(5, 3) == 15
assert multiplicar(4, 2) == 8
assert multiplicar(6, 0) == 0

print('Todos os testes passaram!')
```

Resultado:

```
Todos os testes passaram!
```

Nesse exemplo, estamos verificando três situações diferentes da mesma função.

Se algum resultado estiver incorreto, o Python apresentará um `AssertionError`.

**Atenção:** o `assert` é útil para verificações durante o desenvolvimento, mas não deve ser utilizado como mecanismo de validação de dados importantes em sistemas de produção. Ele pode ser desativado quando o Python é executado com determinadas opções.

## **5. O que é o pytest?**

O `pytest` é uma biblioteca externa utilizada para criar e executar testes automatizados em Python.

Enquanto o `assert` é um recurso nativo da linguagem, o `pytest` oferece uma estrutura mais organizada para testar programas.

Ele é bastante utilizado em projetos profissionais.

Para utilizá-lo, primeiro precisamos instalar:

```
pip install pytest
```

## **6. Como funciona um teste com pytest?**

Imagine que temos um arquivo chamado `calculadora.py`:

```
def somar(a, b):    
    return a + b
    
def subtrair(a, b):    
    return a - b
```

Podemos criar outro arquivo chamado `test_calculadora.py`:

```
from calculadora import somar, subtrair

def test_somar():    
    assert somar(10, 5) == 15
    
def test_subtrair():    
    assert subtrair(10, 5) == 5
```

Observe alguns detalhes:

- Os testes ficam em um arquivo separado.
- Os nomes das funções de teste começam com `test_`.
- Cada função verifica um comportamento específico.
- O `assert` verifica se o resultado está correto.

## **7. Como executar os testes?**

No terminal, dentro da pasta do projeto, executamos:

```
pytest
```

O pytest procura os arquivos e funções que seguem os padrões de nomenclatura de testes e executa as verificações.

Uma saída simplificada seria:

```
============================= test session starts =============================

test_calculadora.py ..                                      [100%]

============================== 2 passed ==============================
```

Isso significa que os dois testes passaram.

Se algum teste falhar, o pytest informa qual foi e apresenta detalhes para ajudar a identificar o problema.

## **8. Diferença entre assert e pytest**

| `assert`                                 | `pytest`                              |
| ---------------------------------------- | ------------------------------------- |
| Recurso nativo do Python                 | Biblioteca externa                    |
| Verifica condições                       | Organiza e executa testes             |
| Pode ser utilizado diretamente no código | Geralmente utiliza arquivos separados |
| Não precisa de instalação                | Precisa ser instalado                 |

Uma observação importante: o `pytest` utiliza o próprio `assert` nas funções de teste. Portanto, os dois trabalham juntos.
