"""Peça ao usuário para digitar uma cor do semáforo (vermelho, amarelo, verde) e exiba a ação correspondente:

- "vermelho" → "Pare!"
- "amarelo" → "Atenção!"
- "verde" → "Siga!"
- Se a cor não for reconhecida, exiba "Cor inválida!"."""

cor = input('Digite a cor do semáforo: ').lower()
if cor == 'vermelho':
    print('Pare!')
elif cor == 'amarelo':
    print('Atenção!')
elif cor == 'verde':
    print('Siga!')
else:
    print('Cor inválida')
