# i=0
# sum=0
# while i<=10:
#     print(f"{i}.Hello World")
#     i=i+1

# for i in range(11):
#     sum = sum + i
# print(f"Hello sum: {sum}")

#DRY Principle = Do not repeat yourself(code)
import random
winning_number = random.randint(1,100)
guess =1 
number = int(input("guess a number between 1 to 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you win the game and your attempt is {guess}")
        game_over = True
    else:
        if number > winning_number:
            print("Too High...")
        else:
            print("Too Low...")

        guess += 1
        number=int(input("guess again : "))

