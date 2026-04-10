slownik =input()

print(len(slownik))

i = 0

for x in slownik:
    if x == " " :
        i = i + 1

print("liczba spacji: ")
print(i)

i = i + 1
print("liczba wyrazów: ")
print(i)