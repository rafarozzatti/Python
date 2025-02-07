import math
def area(r):
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))
print()


raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []
for r in raios:
    areas.append(area(r))
print(areas)
print()


areas = map(area, raios)
print(list(areas))
print()


print(list(map(lambda r: math.pi * (r ** 2), raios)))
print()


cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
