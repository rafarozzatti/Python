s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if s1 == s2 == s3:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif s1 != s2 != s3 != s1:
     print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')