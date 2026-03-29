#NiU 103106
cyfry = [1,0,3,6]

print("podaj Liczbę całkowitą")

x = (input())

try:
    x = int(x)
except ValueError:
    print("Nieprawidłowy typ!")


for i in range(len(cyfry)):
    for j in range(i+1,len(cyfry)):
        if(x==cyfry[i]+cyfry[j]):
            print("suma tak dla: " + str(cyfry[i]) +" "+ str(cyfry[j]))
        if(x==cyfry[i]*cyfry[j]):
            print("iloczyn tak dla: " + str(cyfry[i]) +" "+ str(cyfry[j]))



