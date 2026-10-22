# 3. Operadores lógicos em condições

Os operadores lógicos permitem combinar ou inverter condições. Eles são úteis quando precisamos verificar mais de uma regra em um mesmo `if`.

Os três operadores são:

| Operador | Significado | Quando retorna verdadeiro?                   |
| -------- | ----------- | -------------------------------------------- |
| `and`    | E           | Quando todas as condições são verdadeiras.   |
| `or`     | Ou          | Quando pelo menos uma condição é verdadeira. |
| `not`    | Não         | Quando inverte o resultado lógico.           |

## 1.1. Operador `and`

O `and` exige que todas as condições sejam verdadeiras.

Exemplo:

```
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:    
    print('Pode dirigir')
```

Saída:

```
Pode dirigir
```

O Python verifica duas condições:

- `idade >= 18` → `True`
- `tem_carteira` → `True`

Como ambas são verdadeiras, o programa exibe a mensagem.

Se `tem_carteira` fosse `False`, a mensagem não seria exibida.

## 1.2. Operador `or`

O `or` exige que pelo menos uma condição seja verdadeira.

Exemplo:

```
dia = 'sábado'

if dia == 'sábado' or dia == 'domingo':    
    print('Fim de semana')
```

Saída:

```
Fim de semana
```

A primeira condição é verdadeira porque o dia é sábado. Portanto, o `if` é executado.

## 1.3. Operador `not`

O `not` inverte o resultado lógico de uma condição.

Exemplo:

```
tem_divida = False

if not tem_divida:    
    print('Pode solicitar crédito')
```

Saída:

```
Pode solicitar crédito
```

Como `tem_divida` é `False`, `not tem_divida` resulta em `True`.

## 1.4. Combinando operadores

Também podemos combinar operadores lógicos na mesma condição.

```
idade = 25
renda = 3000
tem_emprego = True

if idade >= 18 and renda >= 2500 and tem_emprego:    
    print('Requisitos atendidos')
else:    
    print('Requisitos não atendidos')
```

Saída:

```
Requisitos atendidos
```

Nesse caso, as três condições precisam ser verdadeiras para que o programa exiba `Requisitos atendidos`.

Atenção: quando combinamos `and` e `or` na mesma expressão, a ordem de avaliação pode importar. Podemos usar parênteses para deixar a intenção explícita. Vamos praticar isso mais adiante, depois de dominar os casos básicos.
