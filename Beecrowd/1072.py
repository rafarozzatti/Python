contin = contout = 0
n = int(input())
for i in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        contin += 1
    else:
        contout += 1
print(f'''{contin} in
{contout} out''')
