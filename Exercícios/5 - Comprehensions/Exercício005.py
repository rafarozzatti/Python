"""Crie uma lista de listas, onde cada lista interna contém os números de 1 até 5. Em seguida, use list comprehension para criar uma lista única contendo todos os números, ou seja, "achatar" a lista de listas em uma lista simples."""

listas = [[1, 2, 3, 4, 5], 
         [1, 2, 3, 4, 5], 
         [1, 2, 3, 4, 5], 
         [1, 2, 3, 4, 5], 
         [1, 2, 3, 4, 5]]

nova_lista = [numero for lista in listas for numero in lista]
print(nova_lista)
