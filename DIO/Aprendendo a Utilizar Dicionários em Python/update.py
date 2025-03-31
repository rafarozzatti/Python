contatos = {
    'rafael@gmail.com': {'nome': 'Rafael', 'idade': 26, 'telefone': '3333-2221'}
    }

# Atualiza o dicionario com os valores fornecidos
contatos.update({'rafael@gmail.com': {'nome': 'Rafa'}})
print(contatos)

# Atualiza o dicionario com os valores fornecidos, caso não tenha, é adicionado
contatos.update({'enzo@gmail.com': {'nome': 'Enzo', 'telefone': '3322-8181'}})
print(contatos)
