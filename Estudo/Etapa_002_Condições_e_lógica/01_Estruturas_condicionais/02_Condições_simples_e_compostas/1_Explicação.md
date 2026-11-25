## **Condições simples e compostas**

As condições utilizadas dentro de estruturas condicionais podem ser classificadas em **simples** ou **compostas**, dependendo da quantidade de verificações realizadas.

### **1. Condições simples**

Uma condição simples verifica apenas uma expressão lógica.

Ela utiliza um operador de comparação para determinar se algo é verdadeiro ou falso.

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

Nesse exemplo, existe apenas uma condição: `idade >= 18`.

Outro exemplo:

```
nota = 5

if nota < 7:    
    print('Nota abaixo da média')
```

Resultado:

```
Nota abaixo da média
```

### **2. Condições compostas**

Uma condição composta verifica duas ou mais condições utilizando operadores lógicos, como `and` e `or`.

**Exemplo com&#x20;**`and`**:**

Imagine que um candidato precisa ter pelo menos 18 anos e possuir habilitação para dirigir.

```
idade = 25
habilitacao = True

if idade >= 18 and habilitacao == True:    
    print('Pode dirigir')
```

Resultado:

```
Pode dirigir
```

As duas condições precisam ser verdadeiras.

**Exemplo com&#x20;**`or`**:**

Imagine que uma loja oferece desconto para clientes VIP ou para compras acima de R$ 500.

```
cliente_vip = False
valor_compra = 600

if cliente_vip == True or valor_compra > 500:    
    print('Desconto disponível')
```

Resultado:

```
Desconto disponível
```

Nesse caso, basta uma das condições ser verdadeira.

### **3. Condições compostas com&#x20;**`and`**&#x20;e&#x20;**`or`

Também podemos combinar os dois operadores na mesma condição.

Imagine que uma empresa oferece um benefício para funcionários com mais de 2 anos de empresa e salário acima de R$ 3.000, ou para funcionários que ocupam cargos de gestão.

```
tempo_empresa = 3
salario = 3500
gestor = False

if (tempo_empresa > 2 and salario > 3000) or gestor:    
    print('Benefício disponível')
```

Resultado:

```
Benefício disponível
```

Vamos analisar:

1. `tempo_empresa > 2` → `True`.
2. `salario > 3000` → `True`.
3. `True and True` → `True`.
4. `True or False` → `True`.

Os parênteses ajudam a agrupar as condições e deixam a lógica mais fácil de entender.

### **4. Diferença entre condições simples e compostas**

| Tipo     | Característica                    | Exemplo                               |
| -------- | --------------------------------- | ------------------------------------- |
| Simples  | Uma condição                      | `idade >= 18`                         |
| Composta | Duas ou mais condições combinadas | `idade >= 18 and habilitacao == True` |

**Resumo:**

- Condições simples verificam uma única expressão.
- Condições compostas combinam duas ou mais expressões.
- `and` exige que todas sejam verdadeiras.
- `or` exige que pelo menos uma seja verdadeira.
- Podemos utilizar parênteses para organizar combinações mais complexas.

Não introduzimos nenhum operador novo; apenas aplicamos os operadores de comparação e lógicos que já estudamos.
