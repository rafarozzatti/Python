## **Estruturas condicionais**

### **1.&#x20;**`if`

O `if` é utilizado para executar um bloco de código somente quando uma condição for verdadeira (`True`).

Se a condição for falsa (`False`), o código dentro do `if` será ignorado.

**Exemplo:**

```
idade = 20

if idade >= 18:    
    print('Maior de idade')
```

Resultado:

```
Maior de idade
```

Como a idade é maior ou igual a 18, a condição é verdadeira e o `print()` é executado.

Se alterarmos a idade:

```
idade = 15

if idade >= 18:    
    print('Maior de idade')
```

Não haverá saída, pois a condição é falsa.

### **2.&#x20;**`else`

O `else` permite executar um bloco de código quando a condição do `if` for falsa.

Ele não possui uma condição própria: representa o caminho alternativo.

**Exemplo:**

```
idade = 15

if idade >= 18:    
    print('Maior de idade')
else:    
    print('Menor de idade')
```

Resultado:

```
Menor de idade
```

Nesse caso:

- Se `idade >= 18` for verdadeiro, executa o `if`.
- Caso contrário, executa o `else`.

### **3.&#x20;**`elif`

O `elif` significa *else if* e permite verificar uma nova condição caso a condição anterior seja falsa.

Podemos utilizar vários `elif` em uma mesma estrutura.

**Exemplo:**

```
nota = 7

if nota >= 9:    
    print('Excelente')
elif nota >= 7:    
    print('Aprovado')
else:    
    print('Reprovado')
```

Resultado:

```
Aprovado
```

Python verifica as condições de cima para baixo:

1. `nota >= 9` → `False`.
2. `nota >= 7` → `True`.
3. Executa o bloco do `elif` e ignora o restante da estrutura.

**Importante:** quando uma condição é verdadeira, somente o bloco correspondente é executado. As condições seguintes são ignoradas.

### **4. Comparação entre&#x20;**`if`**,&#x20;**`elif`**&#x20;e&#x20;**`else`

| Estrutura | Função                                                   |
| --------- | -------------------------------------------------------- |
| `if`      | Verifica a primeira condição.                            |
| `elif`    | Verifica outra condição se as anteriores forem falsas.   |
| `else`    | Executa quando nenhuma condição anterior foi verdadeira. |

Uma estrutura pode ter apenas `if`, pode ter `if` e `else`, ou pode combinar `if`, vários `elif` e `else`.

**Resumo:** estruturas condicionais permitem que um programa tome decisões de acordo com determinadas condições.
