
import time, random
print("When I say DRAW , hit ENTER on your keyboard")
time.sleep(1)
print("Ready?")
time.sleep(random.randint(1, 5))
play_again = "y"

while play_again = y:
    print("DRAW")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    react_time = end_time - start_time
    print("Your score was " + str(react_time) + " seconds")
    play_again = input("Would you like to play again? (y/n): ")

