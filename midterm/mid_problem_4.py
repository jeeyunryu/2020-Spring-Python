f=['apple', 'avocado', 'BANANA', 'blueberry', 'coconut', 'lemon', 'LIME', 'mango', 'papaya', 'PEACH','strawberry']

for j in range(len(f)):
    k=f[j][1]
    if k=='a' or k=='A'or k=='e' or k=='E' or k=='i' or k=='I' or k=='o' or k=='O' or k=='u' or k=='U':
        f.pop(j)
print(f)


