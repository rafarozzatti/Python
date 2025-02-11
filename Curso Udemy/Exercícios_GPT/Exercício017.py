""" Exercício: Crie uma tupla com nomes de cinco cidades e:
- Verifique se "São Paulo" está na tupla.
- Conte quantas vezes "Rio de Janeiro" aparece."""

count = 0
cidades = ("Rio de Janeiro", "São Paulo", "Belo Horizonte", "Curitiba", "Fortaleza")
print("São Paulo está na tupla" if "São Paulo" in cidades else "São Paulo não está na tupla")
print(f'Rio de Janeiro aparece {cidades.count("Rio de Janeiro")} vez(es) na tupla')
