## **ombinação de diferentes condições**

Neste assunto, vamos aprender a combinar diferentes tipos de condições em uma mesma estrutura condicional.

Podemos utilizar:

- Condições aninhadas.
- Operadores lógicos `and`, `or` e `not`.
- Operadores de comparação.
- Operadores `in` e `not in`.

A ideia é construir verificações mais completas, como as utilizadas em sistemas e regras de negócio.

### **1. Combinação de condições com&#x20;**`and`**&#x20;e&#x20;**`or`

Podemos utilizar `and` e `or` na mesma condição para estabelecer diferentes critérios.

**Exemplo:**

Uma empresa concede um benefício para funcionários que tenham salário acima de R$ 3.000 e pelo menos dois anos de empresa, ou que ocupem o cargo de gerente.

```
salario = 2500
tempo_empresa = 3
cargo = 'Gerente'

if (salario >= 3000 and tempo_empresa >= 2) or cargo == 'Gerente':    
    print('Benefício concedido')
else:    
    print('Benefício não concedido')
```

**Resultado:**

```
Benefício concedido
```

Observe a utilização dos parênteses:

- `salario >= 3000 and tempo_empresa >= 2`: exige que as duas condições sejam verdadeiras.
- `cargo == 'Gerente'`: verifica se o funcionário é gerente.
- `or`: permite que qualquer um dos dois critérios seja suficiente.

Os parênteses deixam explícito qual conjunto de condições deve ser avaliado primeiro.

### **2. Combinação com&#x20;**`not`

Também podemos utilizar `not` junto com outros operadores lógicos.

**Exemplo:**

Um usuário pode acessar um sistema se tiver autorização e não estiver bloqueado.

```
autorizado = True
bloqueado = False

if autorizado and not bloqueado:    
    print('Acesso permitido')
else:    
    print('Acesso negado')
```

**Resultado:**

```
Acesso permitido
```

Nesse caso:

- `autorizado` precisa ser verdadeiro.
- `not bloqueado` verifica se o usuário não está bloqueado.
- As duas condições precisam ser verdadeiras.

### **3. Combinação com&#x20;**`in`**&#x20;e&#x20;**`not in`

Podemos combinar a verificação de presença em listas com outros operadores.

**Exemplo:**

Uma empresa permite acesso aos funcionários ativos que pertencem aos setores autorizados.

```
funcionario_ativo = True
setor = 'TI'

setores_autorizados = ['TI', 'Financeiro', 'RH']

if funcionario_ativo and setor in setores_autorizados:    
    print('Acesso permitido')
else:    
    print('Acesso negado')
```

**Resultado:**

```
Acesso permitido
```

Agora, podemos utilizar `not in` para verificar se um funcionário não está em uma lista de bloqueados.

```
usuario = 'Carlos'
usuarios_bloqueados = ['João', 'Pedro', 'Marcos']

if usuario not in usuarios_bloqueados:    
    print('Usuário autorizado')
else:    
    print('Usuário bloqueado')
```

**Resultado:**

```
Usuário autorizado
```

### **4. Combinação de condições aninhadas e operadores**

Podemos reunir os conceitos estudados em uma estrutura mais completa.

**Exemplo:**

Um sistema de crédito verifica:

1. Se a pessoa tem 18 anos ou mais.
2. Se a renda é suficiente e a pessoa não está bloqueada.
3. Se o cargo pertence à lista de cargos autorizados.

```
idade = 25
renda = 4000
bloqueado = False
cargo = 'Analista'

cargos_autorizados = ['Analista', 'Coordenador', 'Gerente']

if idade >= 18:    
    if renda >= 3000 and not bloqueado:        
        if cargo in cargos_autorizados:            
            print('Crédito aprovado')        
        else:            
            print('Cargo não autorizado')    
    else:        
        print('Renda insuficiente ou usuário bloqueado')
else:    
    print('Idade insuficiente')
```

**Resultado:**

```
Crédito aprovado
```
