m = float(input('Uma distância em metros: '))
print(f'''A medida de {m}m corresponde a
{m / 1000}km
{m / 100}hm
{m / 10}dam
{m * 10:.0f}dm
{m * 100:.0f}cm
{m * 1000:.0f}mm''')