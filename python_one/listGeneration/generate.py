L = [n*n for n in range(0,11)]
print(type(L))

LGenerate = (n*n for n in range(0,11))
for s in LGenerate:
    print(s)
