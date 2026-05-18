import random

remis = 0
wygrane = 0
przegrane = 0


while True:
    computer_move_num = random.randrange(1, 4)

    #user_move = input("Wpisz jedna z liter k p n")
    user_move = input("Wpisz jedna z liter k p n lub koniec")
    if (user_move =="koniec"):
        break

    #print(computer_move_num)

    if(computer_move_num ==1):
        computer_move = "k"
    elif computer_move_num == 2:
        computer_move = "p"
    elif computer_move_num == 3:
        computer_move = "n" 

    print(f"Ruch komputera: {computer_move}")

    print(f"Ruch gracza: {user_move}")

    if (computer_move == "k"):
        if(user_move == "p"):
            print("Wygrałeś")
            wygrane = wygrane +1
        elif(user_move == "n"):
            print("Przegrałeś")
            przegrane = przegrane+1
        elif(user_move == "k"):
            print("remis")
            remis = remis + 1
    elif (computer_move == "p"):
        if(user_move == "n"):
            print("Wygrałeś")
            wygrane = wygrane +1
        elif(user_move == "k"):
            print("Przegrałeś")
            przegrane = przegrane+1
        elif(user_move == "p"):
            print("remis")
            remis = remis + 1
    elif (computer_move == "n"):
        if(user_move == "k"):
            print("Wygrałeś")
            wygrane = wygrane +1
        elif(user_move == "p"):
            print("Przegrałeś")
            przegrane = przegrane+1
        elif(user_move == "n"):
            print("remis")
            remis = remis + 1


print("Wygranych:")
print(wygrane)
print("przegrane:")
print(przegrane)
print("remisów:")
print(remis)
