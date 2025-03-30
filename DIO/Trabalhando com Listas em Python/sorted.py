linguagens = ['python', 'js', 'c', 'java', 'csharp']

# Organiza os termos da lista de acordo com a quantidade de letras de forma crescente
sorted(linguagens, key=lambda x: len(x)) #['c', 'js', 'java', 'python', 'csharp']

# Organiza os termos da lista de acordo com a quantidade de letras de forma decrescente
sorted(linguagens, key=lambda x: len(x), reverse=True) #['python', 'csharp', 'java', 'js', 'c']
