from sys import getsizeof
list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
gen_comp = getsizeof(x * 10 for x in range(1000))
print(f'''Para fazer a mesma tarefa gastamos em memória:
List Comprehension: {list_comp} bytes
Set Comprehension: {set_comp} bytes
Dictionary Comprehension: {dic_comp} bytes
Generato Expression: {gen_comp} bytes''')
print()


gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)
    