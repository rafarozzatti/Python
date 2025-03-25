"""Crie uma função chamada criar_usuario que receba nome, idade e cidade como parâmetros obrigatórios, mas aceite informações adicionais ilimitadas usando **kwargs."""

def criar_usuario(nome, idade, cidade, **kwargs):
    usuario = {"nome": nome, "idade": idade, "cidade": cidade}
    usuario.update(kwargs)
    return usuario

usuario = criar_usuario("Rafael", 26, "São Caetano do Sul", profissão="Engenheiro", hobbie="Programação")
print(usuario)
