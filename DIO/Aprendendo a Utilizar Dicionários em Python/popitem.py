contatos = {
    'rafael@gmail.com': {'nome': 'Rafael', 'idade': 26, 'telefone': '3333-2221'}
    }

# Exclui sem o valor informado
print(contatos.popitem())
# Caso não encontre, retorna KeyError
print(contatos.popitem())
