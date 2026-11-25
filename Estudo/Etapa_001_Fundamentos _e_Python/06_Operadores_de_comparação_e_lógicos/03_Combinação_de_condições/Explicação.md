## **Combinação de condições**

A combinação de condições consiste em utilizar operadores de comparação e operadores lógicos na mesma expressão para verificar regras mais específicas.

Podemos combinar `==`, `!=`, `>`, `<`, `>=` e `<=` com `and`, `or` e `not`.

### **1. Combinação com&#x20;**`and`

Imagine que uma empresa exige que o candidato tenha pelo menos 18 anos e possua experiência.

```
idade = 25
experiencia = True

aprovado = idade >= 18 and experiencia == True

print(aprovado)
```

Resultado:

```
True
```

As duas condições precisam ser verdadeiras para que o resultado seja `True`.

### **2. Combinação com&#x20;**`or`

Imagine que uma loja oferece frete grátis para compras acima de R$ 200 ou para clientes VIP.

```
valor_compra = 150
cliente_vip = True

frete_gratis = valor_compra >= 200 or cliente_vip == True

print(frete_gratis)
```

Resultado:

```
True
```

O cliente não atingiu o valor mínimo da compra, mas possui cadastro VIP. Portanto, uma das condições é verdadeira.

### **3. Combinação com&#x20;**`and`**&#x20;e&#x20;**`or`

Também podemos utilizar os dois operadores na mesma expressão.

Imagine uma promoção válida para clientes VIP ou para compras acima de R$ 200 realizadas por clientes cadastrados.

```
valor_compra = 250
cliente_vip = False
cliente_cadastrado = True

promocao = cliente_vip or (valor_compra >= 200 and cliente_cadastrado)

print(promocao)
```

Resultado:

```
True
```

Nesse caso:

1. `valor_compra >= 200` → `True`
2. `cliente_cadastrado` → `True`
3. `True and True` → `True`
4. `False or True` → `True`

Os parênteses deixam explícito qual parte da expressão deve ser avaliada primeiro.

### **4. Combinação com&#x20;**`not`

Podemos utilizar `not` junto com outros operadores para inverter uma condição.

Imagine verificar se um produto não está disponível:

```
disponivel = False
estoque_bloqueado = False

pode_vender = not disponivel == True and not estoque_bloqueado

print(pode_vender)
```

Resultado:

```
False
```

A primeira condição resulta em `True`, mas a segunda também precisa ser verdadeira. Como `estoque_bloqueado` é `False`, `not estoque_bloqueado` resulta em `True`.

**Atenção:** uma forma mais simples de escrever a primeira condição seria `not disponivel`.

### **Resumo**

- Podemos combinar várias condições em uma única expressão.
- `and` exige que todas as condições sejam verdadeiras.
- `or` exige que pelo menos uma seja verdadeira.
- `not` inverte uma condição.
- Parênteses ajudam a controlar e deixar clara a ordem de avaliação.
