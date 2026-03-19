import time

tennis_points = 0
basketball_points = 0
soccer_points = 0

while True:
    name = input("Please identify yourself---")
    input()
    answer1 = input("Which ball do you like the best? A) tennis ball B) basketball or C) soccer ball?")
    input()
    if answer1 == "A" or answer1 == "a":
        tennis_points += 1
        time.sleep(0.5)
        print("Cool")
    elif answer1 == "B" or answer1 == "b":
        basketball_points += 1
    elif answer1 == "C" or answer1 == "c":
        soccer_points += 1
    else:
        print("Sorry, I don't quite understand")
        time.sleep(0.5)
        print("Please type in A, a, B, b, C, or c...")
        continue
    while True:
        answer2 = input("Which person do prefer to meet in real life? A) Rafael Nadal B) Lebron James or C) Lionel Messi?")
        input()
        if answer2 == "A" or answer2 == "a":
            tennis_points += 1
            time.sleep(0.5)
            print("Cool")
        elif answer2 == "B" or answer2 == "b":
            basketball_points += 1
        elif answer2 == "C" or answer2 == "c":
            soccer_points += 1
        else:
            print("Sorry, I don't quite understand")
            time.sleep(0.5)
            print("Please type in A, a, B, b, C, or c...")
            continue
        while True:
            answer3 = input("Which sport would you want to play in the future the most? A) Tennis B) Basketball C) Soccer or D) None?")
            if answer3 == "A" or answer3 == "a":
                tennis_points += 2
                time.sleep(0.5)
                print("Cool")
            elif answer3 == "B" or answer3 == "b":
                basketball_points += 2
            elif answer3 == "C" or answer3 == "c":
                soccer_points += 2
            elif answer3 == "D" or answer3 == "d":
                tennis_points += 0
                basketball_points += 0
                soccer_points += 0
            else:
                print("Sorry I do not understand. Please pick A, a, B, b, C, c, D, or d")
                continue
            while True:
                answer4 = input("How many points do you have to play to for a set in a tennis game? A) 6 B) 7 or C) Depends")
                if answer4 == "A" or answer4 == "a":
                    soccer_points += 2
                elif answer4 == "B" or answer4 == "b":
                    basketball_points += 1
                elif answer4 == "C" or answer4 == "c":
                    tennis_points += 1
                else:
                    print("Sorry I do not understand. Please pick A, a, B, b, C, c, D, or d")
                    continue   
                while True:
                    answer5 = input("Which sport do you play and watch often? A) Tennis B) Basketball or C) Soccer?")
                    input()
                    if answer5 == "A" or answer5 == "a":
                        tennis_points += 1
                        time.sleep(0.5)
                        print("Cool")
                        time.sleep(0.5)
                        print(f"Thank you for answering my questions {name}")
                        if tennis_points > basketball_points and tennis_points > soccer_points:
                            print("I'm guessing that you like tennis")
                            input()
                            input()
                            input()
                            input()
                            input()
                        elif basketball_points > tennis_points and basketball_points > soccer_points:
                            print("I'm guessing that you like basketball")
                            input()
                            input()
                            input()
                            input()
                            input()
                        elif soccer_points > basketball_points and soccer_points > tennis_points:
                            print("I'm guessing that you like soccer")
                            input()
                            input()
                            input()
                            input()
                            input()
                    elif answer5 == "B" or answer5 == "b":
                        basketball_points += 1
                        time.sleep(0.5)
                        print("Cool")
                        time.sleep(0.5)
                        print(f"Thank you for answering my questions {name}")
                        if tennis_points > basketball_points and tennis_points > soccer_points:
                            print("I'm guessing that you like tennis")
                            input()
                            input()
                            input()
                            input()
                            input()
                        elif basketball_points > tennis_points and basketball_points > soccer_points:
                            print("I'm guessing that you like basketball")
                            input()
                            input()
                            input()
                            input()
                            input()
                        elif soccer_points > basketball_points and soccer_points > tennis_points:
                            print("I'm guessing that you like soccer")
                            input()
                            input()
                            input()
                            input()
                            input()
                    elif answer5 == "C" or answer5 == "c":
                        soccer_points += 1
                        time.sleep(0.5)
                        print("Cool")
                        time.sleep(0.5)
                        print(f"Thank you for answering my questions {name}")
                        if tennis_points > basketball_points and tennis_points > soccer_points:
                            print("I'm guessing that you like tennis")
                            input()
                            input()
                            input()
                            input()
                        elif basketball_points > tennis_points and basketball_points > soccer_points:
                            print("I'm guessing that you like basketball")
                            input()
                            input()
                            input()
                            input()
                        elif soccer_points > basketball_points and soccer_points > tennis_points:
                            print("I'm guessing that you like soccer")
                            input()
                            input()
                            input()
                            input()
                    else:
                        print("Sorry, I don't quite understand")
                        time.sleep(0.5)
                        print("Please type in A, a, B, b, C, or c...")
                        continue