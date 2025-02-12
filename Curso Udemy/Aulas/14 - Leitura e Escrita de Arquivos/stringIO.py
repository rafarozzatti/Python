from io import StringIO
mensagem = 'Este é apenas uma string normal'
arquivo = StringIO(mensagem)
print(arquivo.read())
arquivo.write(' Outro texto')
arquivo.seek(0)
print(arquivo.read())