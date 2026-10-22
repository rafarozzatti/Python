# Exercícios de Condições Aninhadas

## Exercício 1

Crie um programa que:

1. Crie a variável `idade` com o valor `25`.
2. Crie a variável `tem_carteira` com o valor `True`.
3. Verifique primeiro se a idade é maior ou igual a `18`.
4. Dentro desse `if`, verifique se `tem_carteira` é verdadeiro.
5. Se as duas condições forem verdadeiras, exiba `Pode dirigir`.

Saída esperada:

```
Pode dirigir
```

## Exercício 2

Agora, use a mesma estrutura, mas altere a variável `idade` para `16`. Mantenha `tem_carteira = True`.

O programa deve verificar a idade e, dentro do primeiro `if`, verificar se a pessoa tem carteira. Se ambas as condições forem verdadeiras, deve exibir `Pode dirigir`.

Saída esperada: nenhuma mensagem será exibida, pois a primeira condição será falsa.

## Exercício 3

Agora, crie um programa com:

- `idade = 25`
- `tem_carteira = False`

Verifique primeiro se a idade é maior ou igual a `18`. Dentro desse `if`, verifique se a pessoa tem carteira. Se as duas condições forem verdadeiras, exiba `Pode dirigir`.

Saída esperada: nenhuma mensagem será exibida, porque a segunda condição será falsa.

## Exercício 4

Crie um programa que:

1. Crie a variável `idade` com o valor `20`.
2. Crie a variável `tem_carteira` com o valor `False`.
3. Verifique se a idade é maior ou igual a `18`.
4. Dentro desse `if`, verifique se a pessoa tem carteira:
   - Se tiver, exiba `Pode dirigir`.
   - Caso contrário, exiba `Precisa tirar a carteira`.

Saída esperada:

```
Precisa tirar a carteira
```

## Exercício 5

Crie um programa que:

1. Crie a variável `idade` com o valor `16`.
2. Crie a variável `tem_autorizacao` com o valor `True`.
3. Verifique primeiro se a idade é maior ou igual a `18`.
   - Se for, verifique se `tem_autorizacao` é verdadeiro:
     - Se for, exiba `Acesso permitido`.
     - Caso contrário, exiba `Autorização necessária`.
   - Se a idade for menor que `18`, exiba `Acesso negado por idade`.

Saída esperada:

```
Acesso negado por idade
```

## Exercício 6

Crie um programa que:

1. Crie a variável `usuario` com o texto `'Rafael'`.
2. Crie a variável `senha` com o valor `1234`.
3. Verifique se `usuario == 'Rafael'`.
   - Se for verdadeiro, verifique dentro desse `if` se `senha == 1234`.
   - Se as duas condições forem verdadeiras, exiba `Login realizado`.
   - Se o usuário estiver correto, mas a senha estiver errada, exiba `Senha incorreta`.
4. Se o usuário estiver incorreto, exiba `Usuário não encontrado`.

Saída esperada:

```
Login realizado
```

## Exercício 7

Crie um programa que:

1. Crie a variável `saldo` com o valor `500`.
2. Crie a variável `saque` com o valor `200`.
3. Verifique se `saldo` é maior ou igual a `saque`.
   - Se for verdadeiro, verifique dentro desse `if` se `saque > 0`.
   - Se as duas condições forem verdadeiras, exiba `Saque realizado`.
   - Se o saldo for suficiente, mas o saque não for maior que zero, exiba `Valor de saque inválido`.
4. Se o saldo for menor que o valor do saque, exiba `Saldo insuficiente`.

Saída esperada:

```
Saque realizado
```

## Exercício 8

Crie um programa que:

1. Crie a variável `nota` com o valor `8`.
2. Crie a variável `frequencia` com o valor `80`.
3. Verifique se `nota >= 7`.
   - Se for verdadeiro, verifique dentro desse `if` se `frequencia >= 75`.
   - Se as duas condições forem verdadeiras, exiba `Aprovado`.
   - Se a nota for suficiente, mas a frequência for inferior a `75`, exiba `Reprovado por frequência`.
4. Se a nota for inferior a `7`, exiba `Reprovado por nota`.

Saída esperada:

```
Aprovado
```

## Exercício 9

Crie um programa que:

1. Crie a variável `valor_compra` com o valor `250`.
2. Crie a variável `cliente_vip` com o valor `True`.
3. Verifique se `valor_compra >= 200`.
   - Se for verdadeiro, verifique dentro desse `if` se `cliente_vip` é verdadeiro.
   - Se as duas condições forem verdadeiras, exiba `Desconto VIP aplicado`.
   - Se o valor da compra for suficiente, mas o cliente não for VIP, exiba `Desconto comum aplicado`.
4. Se o valor da compra for inferior a `200`, exiba `Compra sem desconto`.

Saída esperada:

```
Desconto VIP aplicado
```

## Exercício 10

Crie um programa que:

1. Crie a variável `idade` com o valor `22`.
2. Crie a variável `renda_mensal` com o valor `3000`.
3. Crie a variável `possui_emprego` com o valor `True`.
4. Verifique se `idade >= 18`.
   - Se for verdadeiro, verifique se `possui_emprego` é verdadeiro.
     - Se for verdadeiro, verifique se `renda_mensal >= 2500`.
       - Se as três condições forem satisfeitas, exiba `Crédito aprovado`.
       - Se a pessoa tiver emprego, mas a renda for inferior a `2500`, exiba `Renda insuficiente`.
     - Se não possuir emprego, exiba `É necessário possuir emprego`.
5. Se a idade for inferior a `18`, exiba `Idade insuficiente`.

Saída esperada:

```
Crédito aprovado
```
