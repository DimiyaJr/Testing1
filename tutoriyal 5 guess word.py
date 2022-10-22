print("************************************************")
print("********       GUESS THE WORD    ***************")
print("************************************************")

secret = "Westminster"
guess = "-"*len(secret)
guess_count = 0
max = 10


while guess_count< max:
    for c in guess:
        print(c,end=" ")
    print()
    print("You have",max-guess_count,"times to guess the word")
    char = input("Please guess  a character in the secret word : ")
    if len(char)==1:
        guess_count = guess_count+1
        index = 0
        new_guess=""
        while index<len(secret):
            
            if secret[index]==char and guess[index]=="-":
                new_guess = new_guess+char
            elif guess[index]!="-":
                new_guess = new_guess+guess[index]
            else:
                new_guess = new_guess+"-"
            index = index+1
        guess  = new_guess
        if guess == secret:
            print("Congratulations!!! You have guessed the word ","'"+secret+"'","correctly")
            break
    else:
        print("Please enter a single character")
else:
    print("Sorry!!! You have run out of turns")
