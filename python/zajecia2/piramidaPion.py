def generate_piramid(wysokosc = 7) :
    y = wysokosc - 1
    while y >= 0:
        x = 1
        while x < (wysokosc * 2):
            if x > y and x < (wysokosc*2 -y):
                print("#", end = "")
            else:
                print(" ", end = "")
            x+=1
        print()
        y-=1
generate_piramid()