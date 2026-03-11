print("Welcome to CT8!")
print("Great job correctly setting up this codespace")
print("We will be using this site for the majority of the projects for this class")
print("Make sure you bookmark this page using the STAR icon in the top right corner of your browser")
input("\n---Press Enter when you have bookmarked the page---\n")


print("\n\n")
print("This area is called the TERMINAL.")
print("It shows messages and errors.")
print("You also can type in the terminal.")
name = input("\n---Type your first name here, then press Enter---\n")
name_second = input("\n---Type your last name here, then press Enter---\n")

print("\n\n")
print(r"  _____ ____  __  __ _____    _______ _    _ _____ _   _ _  _______ _   _  _____    ___  ")
print(r" / ____/ __ \|  \/  |  __ \  |__   __| |  | |_   _| \ | | |/ /_   _| \ | |/ ____|  / _ \ ")
print(r"| |   | |  | | \  / | |__) |    | |  | |__| | | | |  \| | ' /  | | |  \| | |  __  | (_) |")
print(r"| |   | |  | | |\/| |  ___/     | |  |  __  | | | | . ` |  <   | | | . ` | | |_ |  > _ < ")
print(r"| |___| |__| | |  | | |         | |  | |  | |_| |_| |\  | . \ _| |_| |\  | |__| | | (_) |")
print(r" \_____\____/|_|  |_|_|         |_|  |_|  |_|_____|_| \_|_|\_\_____|_| \_|\_____|  \___/ ")
# text art from https://patorjk.com/software/taag/


print(f"This codespace belongs to {name} {name_second}")
print("\n\n")
two_truths_and_one_lie = ["I play tennis", "I don't like sandwiches", "I broke 6 bones"]
for two_truths_and_one_lie in two_truths_and_one_lie:
    print(two_truths_and_one_lie)
    lie = input("\n---Type the lie here---\n")
    if lie == "I play tennis":
        print("Sorry, that's wrong!")
    elif lie == "I don't like sandwiches":
        print("Sorry, that's wrong!")
    elif lie == "I broke 6 bones":
        print("Correct!! You Win!!!")
    else:
        print("I don't quite understand.")

                                                                                          
                                  
print("Now it's your turn:")
print("I play tennis often.")                                  