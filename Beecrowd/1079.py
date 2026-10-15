n = int(input())
for i in range(3):
    t1, t2, t3 = input().split()
    t1 = float(t1)
    t2 = float(t2)
    t3 = float(t3)
    media = (t1 * 2 + t2 * 3 + t3 * 5) / 10
    print(f'{media:.1f}')
