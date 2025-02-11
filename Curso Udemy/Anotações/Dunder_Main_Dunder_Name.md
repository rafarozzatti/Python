# `__name__` e `__main__` em Python

Em Python, os identificadores `__name__` e `__main__` são usados para definir o comportamento de um script quando ele é executado diretamente ou importado como um módulo.

---

## **1. O que é `__name__`?**
`__name__` é uma variável especial que Python define automaticamente em cada módulo. Seu valor depende de como o script está sendo executado:
- Se o script é executado diretamente, `__name__` é atribuído como `"__main__"`.
- Se o script é importado como um módulo, `__name__` recebe o nome do arquivo do módulo sem a extensão `.py`.

---

## **2. Exemplo básico de `__name__`**
```python
# arquivo: modulo.py
print(f"O valor de __name__ neste arquivo é: {__name__}")
```
### **Saída ao rodar diretamente:**
```
O valor de __name__ neste arquivo é: __main__
```
### **Saída ao importar em outro script:**
```python
import modulo
```
```
O valor de __name__ neste arquivo é: modulo
```

---

## **3. Usando `if __name__ == "__main__"`**
A condição `if __name__ == "__main__"` é usada para garantir que determinado bloco de código só seja executado quando o script for executado diretamente, e não quando for importado.

```python
# arquivo: exemplo.py
def saudacao():
    print("Olá, bem-vindo ao programa!")

if __name__ == "__main__":
    saudacao()
```
### **Saída ao rodar `python exemplo.py`:**
```
Olá, bem-vindo ao programa!
```
### **Saída ao importar `exemplo.py` em outro script:**
```python
import exemplo
```
**Nenhuma saída ocorre**, pois `if __name__ == "__main__"` impede a execução da função `saudacao()`.

---

## **4. Benefícios de `__name__ == "__main__"`** ✅
- Evita a execução de código indesejado ao importar um módulo.
- Permite que um script seja usado tanto como um programa independente quanto como um módulo reutilizável.
- Facilita a organização de testes dentro do próprio arquivo.

---

## **5. Conclusão**
A verificação `if __name__ == "__main__"` é uma prática fundamental em Python para garantir um comportamento adequado de scripts e módulos. Isso permite reutilizar códigos sem que blocos indesejados sejam executados ao importar arquivos.
