# Testes em Python

A testagem de código é essencial para garantir que nossos programas funcionem corretamente e para facilitar a manutenção. Em Python, há diversas formas de escrever e executar testes, como **Assertions**, **Doctests** e **Hooks**.

---

## **1. Assertions (`assert` em Python)**

O `assert` é uma forma simples de verificar se uma condição é verdadeira. Caso contrário, ele levanta um erro do tipo `AssertionError`.

```python
# Usando assert para testar condições

def dividir(a, b):
    assert b != 0, "Erro: Divisão por zero não permitida"
    return a / b

# Teste 1: Divisão normal
print(dividir(10, 2))  # Saída: 5.0

# Teste 2: Tentativa de divisão por zero (gera erro)
print(dividir(10, 0))  # Saída: AssertionError: Erro: Divisão por zero não permitida
```

### **Vantagens e desvantagens do `assert`**
✅ Simples e rápido para testes básicos.  
❌ Pode ser desativado em produção se o Python for executado com a flag `-O` (optimize).  

---

## **2. Doctests (`doctest` em Python)**

O `doctest` permite escrever testes diretamente na docstring da função.

```python
import doctest

def somar(a, b):
    """
    Retorna a soma de dois números.
    
    >>> somar(2, 3)
    5
    >>> somar(-1, 1)
    0
    """
    return a + b

# Executando os testes do doctest
if __name__ == "__main__":
    doctest.testmod()
```

### **Como executar o Doctest?**
Basta rodar o script normalmente. Se os testes passarem, nada será exibido. Se falharem, o erro será mostrado.

---

## **3. Hooks em Testes**

Hooks são funções que podem ser executadas antes ou depois dos testes para configurar o ambiente.

### **Exemplo usando `pytest`**

```python
import pytest

@pytest.fixture
def setup():
    print("Preparando o teste...")
    return {"nome": "Teste", "valor": 100}

def test_exemplo(setup):
    assert setup["valor"] == 100  # Verifica se o valor está correto

# Executando com pytest no terminal: pytest nome_do_arquivo.py
```

### **Saída esperada:**
```
Preparando o teste...
.
1 passed in 0.12s
```

### **Benefícios dos Hooks**
✅ Configurações antes e depois dos testes.  
✅ Evita repetição de código em múltiplos testes.  

---

## **Conclusão**

- **Assertions** são úteis para verificações rápidas.
- **Doctests** documentam e testam o código ao mesmo tempo.
- **Hooks** facilitam a configuração de testes automatizados.
