def increment(alist):
    incremented = []
    for a in alist:
        incremented.append(a * 2)

    return incremented
print(increment([0, 1, 2]))

base = [0, 1, 2]

print("0 1 2 3")
for i in base:
    print(i+1, end=" ")
    for j in base:
        print((i+1) * (j+1), end=" ")
    print("")

