#The player is trapped in the “magic maze”.
#If still in the “magical maze”, ask the player which way to go. Announce it like:“You are in the magic maze. Which way to go? (N,S,E,W)”
#Accepted directions are N[orth], S[outh], E[ast] and W[est].
#The secret escape combination is: SSNWES
#Keep track of the number of “moves”
#If the escape sequence is correct, announce that the player has won:“You have escaped the maze in X moves”
#If the escape chain is broken, start from the beginning. Suppose the player has the sequence SSN and then tries E. This breaks the chain an we must start again from the first valid move: S.
#After 10 moves the player loses one life
#The player starts with 3 lives and “dies” when the life counter reaches 0
#Inform the player when he loses one life and how many he has left


print ("You are in the magic maze. With the correct combination you can scape.")

solution = ["S","S","N","W","E","S"]

sol = 0
movimientos = 0
vidas = 3

temp = True
while temp:

    direc = input ("Which way to go? (N,S,E,W): ")
    if direc == solution [sol]:
        print("CONGRATULATION YOU ACCERTED")
        print ("you have: ", vidas, "lives")
        print ("Moves done: ", movimientos + 1)
        sol += 1
        movimientos +=1

    else:
        print ("SORRY, NOT THE RIGHT DIRECTION, INCORRECT!!")
        movimientos += 1
        vidas -= 1
        print("you have: ", vidas, "lives")
        print("Moves done: ", movimientos)

        if direc== len(solution):
            print("you WON you made", movimientos, "moves to win!")

        if movimientos % 10 == 0:
            vidas = vidas - 1
            print (" you lost a life! You have ", vidas, "lifes left")

        if vidas == 0:
            print("You lost ")
            temp = False

