def generate_piramid(wysokosc = 4) :
    for i in range(wysokosc):
        if(i <= wysokosc):
            for j in range(i):
                print("#", end = "")
            print()

    for i in range(wysokosc - 1, 0, -1):
        for j in range(i):
            print("#", end="")
        print()

        


generate_piramid()