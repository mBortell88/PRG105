import questions


def main():
    # start scores accumulators
    player_1 = 0
    player_2 = 0

    # create instances for trivia questions
    q1 = questions.Questions("Which animal has the longest lifespan?",
                             ["A. Giant Tortoise", "B. Asian Elephant", "C. Bowhead Whale", "D. Tuatara "], 'C')
    q2 = questions.Questions("Which bird has the fastest airspeed velocity?",
                             ['A. Peregrine Falcon', 'B. Golden Eagle', 'C. Common Swift', 'D. Gyrfalcon'], 'A')
    q3 = questions.Questions("Which cat is the largest 'Big Cat'?",
                             ["A. Tiger", "B. Lion", "C. Panther", "D. Cheetah"], 'A')
    q4 = questions.Questions("What animal is the smallest mammal in the world?",
                             ["A. Pygmy Jerboa", "B. Bumblebee Bat", "C.Least Weasel", "D.American Shrew Mole"], 'B')
    q5 = questions.Questions("What animal is Britain's largest carnivore?",
                             ["A. Badger", "B. Dog", "C. Fox", "D. Wolf"], 'A')
    q6 = questions.Questions("Which animal has the highest blood pressure?",
                             ["A. Kangaroo", "B. Giraffe", "C.Horse", "D. Elephant"], 'B')
    q7 = questions.Questions("In Disney's The Jungle Book, what are the names of the four vultures?",
                             ["A. Leonardo, Michaelangelo, Raphael, Donatello", "B. Harpo, Groucho, Chico, Gummo",
                              "C. John, Paul, George, Ringo", "D. Goodman, Hampton, Wilson, Krupa"], 'C')
    q8 = questions.Questions("The Order of the Elephant is the highest award of honor in what country?",
                             ["A. India", "B. Thailand", "C. France", "D. Denmark"], 'D')
    q9 = questions.Questions("How many times can a Hummingbird flap its wings per second?",
                             ["A. 60", "B. 120", "C. 110", "D. 70"], 'D')
    q10 = questions.Questions("Of all insects, which has the best eyesight?", ["A. Ant", "B. Butterfly", "C. Cockroach", "D. Dragonfly"], 'D')

    # split the questions into sets
    set_1 = {q1, q3, q5, q7, q9}
    set_2 = {q2, q4, q6, q8, q10}

    # Introduction
    print("ANIMAL TRIVIA")
    print("Let's test your knowledge of the Animal Kingdom!")
    print("Two player's will take a turn at answering 5 trivia questions.")
    print("The player who answers the most questions correctly wins.")
    print("Let's Begin!")
    print()

    print("Player 1, You're Up!")
    print("---------------------")

    # use loop to iterate through dictionary of questions (set_1)
    for query in set_1:
        print(query.get_question())
        print(query.get_choices())
        print()
        response = input("Please enter the letter answer:")
        if response.upper() == query.get_answer():
            print("That's right!")
            player_1 += 1
        else:
            print("Incorrect.")
            continue

    print("---------------------")
    print("Player 2's Turn!")
    print("---------------------")

    # use loop to iterate through dictionary of questions (set_1)
    for query2 in set_2:
        print(query2.get_question())
        print(query2.get_choices())
        print()
        response2 = input("Please enter the letter answer:")
        if response2.upper() == query2.get_answer():
            print("That's right!")
            player_2 += 1
        else:
            print("Incorrect.")
            continue

    print()
    print("Now let's tally the scores!")
    print("...And the winner is...")
    print()
    # Now compare scores
    if player_1 == player_2:
        print("It's a tie! Nice Job!")
        print("~*~*~Scores~*~*~")
        print("Player 1:", player_1)
        print("Player 2:", player_2)
    elif player_1 > player_2:
        print("Player 1 Wins! Nice Job!")
        print("~*~*~Scores~*~*~")
        print("Player 1:", player_1)
        print("Player 2:", player_2)
    elif player_2 > player_1:
        print("Player 2 Wins! Nice Job!")
        print("~*~*~Scores~*~*~")
        print("Player 1:", player_1)
        print("Player 2:", player_2)

# call main function
main()
