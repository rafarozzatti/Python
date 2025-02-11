# Módulos Customizados em Python

Os módulos customizados são arquivos Python criados pelo próprio usuário para reutilizar funções, classes e variáveis. Eles ajudam a organizar melhor o código e evitam repetições desnecessárias.

---

## **1. Criando um Módulo Customizado**
Podemos criar um módulo simplesmente salvando um arquivo com a extensão `.py`.

### **Exemplo: Criando um módulo chamado `meu_modulo.py`**
```python
# Arquivo: meu_modulo.py

# Função que retorna a soma de dois números
def somar(a, b):
    return a + b

# Função que retorna a diferença entre dois números
def subtrair(a, b):
    return a - b
```

---

## **2. Importando um Módulo Customizado**
Para utilizar um módulo customizado, basta importá-lo no arquivo principal.

### **Exemplo: Importando e utilizando `meu_modulo.py`**
```python
# Importando o módulo
import meu_modulo

# Usando as funções do módulo
resultado_soma = meu_modulo.somar(5, 3)
resultado_subtracao = meu_modulo.subtrair(10, 4)

print(f"Soma: {resultado_soma}")  # Saída: Soma: 8
print(f"Subtração: {resultado_subtracao}")  # Saída: Subtração: 6
```

---

## **3. Importando Apenas Algumas Funções**
Podemos importar apenas funções específicas de um módulo para evitar importar conteúdo desnecessário.

```python
# Importando apenas a função somar do módulo
from meu_modulo import somar

print(somar(7, 2))  # Saída: 9
```

---

## **4. Definindo um Alias (Apelido) para um Módulo**
Podemos dar um nome alternativo ao módulo para simplificar sua utilização.

```python
import meu_modulo as mm

print(mm.somar(4, 6))  # Saída: 10
```

---

## **5. O Bloco `if __name__ == "__main__"`**
Esse bloco permite que um módulo seja tanto importado quanto executado diretamente.

```python
# Arquivo: meu_modulo.py

def saudacao():
    print("Olá, bem-vindo ao módulo!")

if __name__ == "__main__":
    saudacao()
```

Se o arquivo `meu_modulo.py` for executado diretamente, ele imprimirá "Olá, bem-vindo ao módulo!". Se for importado, essa linha não será executada.

---

## **6. Onde Colocar o Módulo?**
O módulo deve estar no mesmo diretório do arquivo que o importa ou em um diretório incluído no `sys.path`.

Podemos verificar os caminhos onde o Python busca os módulos:

```python
import sys
print(sys.path)
```

---

## **Quando Usar Módulos Customizados?** ✅
- Para organizar o código em partes reutilizáveis.
- Para facilitar a manutenção e o entendimento do projeto.
- Para evitar repetição de código.

## **Quando Evitar Módulos Customizados?** ❌
- Quando o código é muito pequeno e não justifica a separação.
- Quando já existem bibliotecas prontas que fazem a mesma coisa de forma eficiente.

---

## **Conclusão**
Os módulos customizados são uma ferramenta poderosa para organizar código em Python, tornando os projetos mais modulares e fáceis de manter.
