arquivo = open(r'C:\Users\Rafael\OneDrive\Área de Trabalho\Documentos\estudos\Python\Curso Udemy\Aulas\14 - Leitura e Escrita de Arquivos\texto.txt')
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())
arquivo.seek(19)
print(arquivo.read())

arquivo.seek(0)
print(arquivo.readline())

print(arquivo.readline())

print(arquivo.readline())

print(arquivo.readline())

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
