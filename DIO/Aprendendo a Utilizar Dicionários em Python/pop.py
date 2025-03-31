contatos = {
    'rafael@gmail.com': {'nome': 'Rafael', 'idade': 26, 'telefone': '3333-2221'}
    }

# Exclui o valor informado
print(contatos.pop('rafael@gmail.com'))
# Exclui o valor informado, caso não encontre, imprime o valor sugerido({})
print(contatos.pop('rafael@gmail.com'), {})
