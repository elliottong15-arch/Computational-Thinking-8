print("")
print("")
print("")
name = input(-Please Identify yourself---\n")
input()
print(f"Hello {name}. I am Bob, a program interested in your likings.")
input()
food = input("\n---What is your favorite food---\n")
input()
print(f"Cool!!! I love to eat {food}")
input()
favorite_subject = input("\n---Well, what is your favorite subject?---\n")
if favorite_subject == "Math" or "math" or "English" or "english" or "Science" or "science" or "History" or "history":
    print("Ew those are bad subjects")
    input()
    feelings = input("\nHow are you feeling today?\n")
    if feelings == "Good" or "good" or "Great" or "great":
        print("That's good to hear.")
    else:
        print("Ok, well I don't care")
else:
    print(f"Oh cool! I like {favorite_subject}")
    input()
    feelings = input("\nHow are you feeling today?\n")
    if feelings == "Good" or "good" or "Great" or "great":
        print("That's good to hear.")
    else:
        print("Ok, well I don't care")

