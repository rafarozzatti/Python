contatos = {
    'rafael@gmail.com': {'nome': 'Rafael', 'idade': 26, 'telefone': '3333-2221'}
    }

# O valor não é encontrado, então retorna KeyError
contatos['chave']

# # O valor não é encontrado, então retorna None
contatos.get('chave')
# # O valor não é encontrado, então retorna o valor informado({})
contatos.get('chave', {})
# # O valor é encontrado, caso não fosse encontrado retornaria o valor informado({})
contatos.get('rafael@gmail.com', {})
