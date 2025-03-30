# Organiza os termos da lista
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort() #['c', 'csharp', 'java', 'js', 'python']

# Organiza os termos da lista de forma decrecente
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(reverse=True) #['python', 'js', 'java', 'csharp', 'c']

# Organiza os termos da lista de acordo com a quantidade de letras de forma crescente
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x)) #['c', 'js', 'java', 'python', 'csharp']

# Organiza os termos da lista de acordo com a quantidade de letras de forma decrescente
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x), reverse=True) #['csharp', 'python', 'java', 'js', 'c']
