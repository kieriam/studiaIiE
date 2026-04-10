slownik =input()

print(len(slownik))

i = 0
stack = []

for x in slownik:
    if x != " ":
        i = i + 1
    
    if x not in stack:
        stack.append(x)

print("liczba liter : ")
print(i)

spacje = slownik.count(" ")
print("liczba spacji : ")
print(spacje)

wyrazy = len(slownik.split())
print("liczba wyrazów : ")
print(wyrazy)

print("czestotliwosc zanków: ")
for x in stack:
    print(str(slownik.count(x)) + x, end = " ")