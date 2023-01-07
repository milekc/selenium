s = '45 45 66 21 94 62 50 13 96'
l = list(map(int, input().split()))
d = dict([(l[-2], l[-1])])
for i in l[-3::-1]:
    d = dict([(i, d)])
print(d)