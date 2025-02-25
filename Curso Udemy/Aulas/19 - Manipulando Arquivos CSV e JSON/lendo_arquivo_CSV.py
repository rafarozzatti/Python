from csv import reader, DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no/na {linha[1]} e mede {linha[2]} centimetro')

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f'{linha['Nome']} nasceu no/na {linha['Pais']} e mede {linha['Altura (em cm)']} centimetro')
