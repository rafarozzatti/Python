def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vive uma vez'
    return f'Estou comendo {comida} porque {final}'
