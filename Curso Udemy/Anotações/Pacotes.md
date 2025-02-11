# Pacotes em Python

## O que são pacotes?
Pacotes em Python são coleções de módulos organizados em diretórios, permitindo uma estrutura hierárquica para organizar o código.

---

## Criando um pacote
Para criar um pacote, siga estas etapas:

1. Crie uma pasta com o nome do pacote.
2. Dentro dessa pasta, crie um arquivo `__init__.py` (pode estar vazio ou conter inicialização do pacote).
3. Adicione módulos (arquivos `.py`) dentro da pasta do pacote.

### Estrutura do pacote:
```
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
```

### Criando os arquivos:

#### **`modulo1.py`**
```python
# Função dentro do modulo1

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao pacote."
```

#### **`modulo2.py`**
```python
# Função dentro do modulo2

def soma(a, b):
    return a + b
```

---

## Importando e utilizando um pacote

Para usar o pacote em outro script, importe os módulos conforme necessário.

### **Forma 1: Importando o módulo inteiro**
```python
# Importando um módulo do pacote
import meu_pacote.modulo1

# Usando a função do modulo1
print(meu_pacote.modulo1.saudacao("Carlos"))
```
**Saída:**
```
Olá, Carlos! Bem-vindo ao pacote.
```

### **Forma 2: Importando funções específicas**
```python
# Importando apenas a função desejada
from meu_pacote.modulo2 import soma

# Usando a função soma
print(soma(3, 5))
```
**Saída:**
```
8
```

---

## Pacotes aninhados
Pacotes podem conter subpacotes, organizando ainda mais o código.

### Estrutura de pacotes aninhados:
```
meu_pacote/
    __init__.py
    modulo1.py
    subpacote/
        __init__.py
        modulo3.py
```

#### **`subpacote/modulo3.py`**
```python
# Função dentro de um subpacote

def multiplicacao(a, b):
    return a * b
```

### **Importando de um subpacote**
```python
from meu_pacote.subpacote.modulo3 import multiplicacao
print(multiplicacao(4, 2))
```
**Saída:**
```
8
```

---

## Quando usar pacotes?
✅ Quando o projeto tem muitos módulos e precisa de organização.
✅ Para reutilizar códigos de maneira mais estruturada.
✅ Quando deseja separar funcionalidades distintas.

## Quando evitar pacotes?
❌ Para pequenos scripts ou projetos simples.
❌ Quando a separação de arquivos prejudica a compreensão do código.

---

## Conclusão
Pacotes ajudam a organizar grandes projetos, facilitando a reutilização e manutenção do código. Ao usar pacotes corretamente, você melhora a estrutura do seu software!
