
import time, random, csv, keyboard


def check_high_scores(react_time: float, high_scores: list):
    if react_time < high_scores[2]:
        if react_time < high_scores[1]:
            if react_time < high_scores[0]:
                high_scores.insert(0, react_time)
            else:
                high_scores.insert(1, react_time)
        else:
            high_scores.insert(2, react_time)
    return high_scores[0:3]

def saved_scores(high_scores: list):
    writer = csv.writer(open("high_scores.csv", "w"))
    writer.writerow(high_scores)

def load_scores(high_scores_file):
    with open(high_scores_file) as f:
        reader = csv.reader(f)
        data = list(reader)
    data = [float(i) for i in data[0]]
    return data


print("When I say DRAW , hit ENTER on your keyboard")
time.sleep(1)
print("Ready?")
play_again = "y"
high_scores = load_scores("high_scores.csv")

while play_again == "y":
    time.sleep(random.randint(1, 3))
    print("DRAW")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    react_time = end_time - start_time
    print("Your score was " + str(react_time) + " seconds")
    high_scores = check_high_scores(react_time, high_scores)
    print(f"Top 3 Best Scores {high_scores}")
    play_again = input("Would you like to play again? (y/n): ")

saved_scores(high_scores)




