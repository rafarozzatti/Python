n = int(input())
hrs = n // 3600
min = (n % 3600) // 60
seg = (n % 3600) % 60
print(f'{hrs}:{min}:{seg}')
