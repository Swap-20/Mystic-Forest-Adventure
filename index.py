import pygame

def adventure_game():
    print("Welcome to the Mystic Forest Adventure!")
    print("You are a brave explorer. Your mission is to find the hidden treasure.")
    print("Choose your path wisely...")

    while True:
        choice = input("\nYou see two paths: [1] Dark Cave, [2] Sunny Trail. Where do you go? (1/2): ")
        if choice == "1":
            print("You enter the Dark Cave. It's cold and eerie.")
            cave_choice = input("You see a passageway deep inside the cave. Do you [1] explore deeper or [2] turn back? (1/2): ")
            if cave_choice == "1":
                print("\nYou venture deeper into the cave and find a hidden route!")
                print("Stepping out, you discover a magical paradise with a sparkling lake, colorful flowers, and fluttering butterflies.")
                print("As you admire the beauty, a mischievous fairy named Flick appears!")
                print('"Hello, traveler! If you want to continue, solve this riddle!"')

                # Puzzle time!
                riddle = input('"I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?": ')
                if riddle.lower() == "echo":
                    print("\nFlick claps his tiny hands. \"Well done! Follow me to the palace.\"")
                    print("He guides you to a magnificent palace hidden in the forest!")
                    print("Inside, you find a room filled with glittering treasure. Congratulations, you win!")
                else:
                    print("\nFlick smirks. \"That's not right! Come back when you know the answer.\"")
                    print("You decide to leave for now. Game over.")
            elif cave_choice == "2":
                print("You decide to turn back, missing out on an incredible discovery. Game over.")
            else:
                print("Invalid choice. Try again.")
        elif choice == "2":
            print("You walk along the Sunny Trail. It's beautiful but uneventful.")
            trail_choice = input("You find a fork in the road. Do you [1] take the left path or [2] take the right path? (1/2): ")
            if trail_choice == "1":
                print("You reach a dead end. Game over.")
            elif trail_choice == "2":
                print("You stumble upon an old cabin filled with treasure! You win!")
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid choice. Try again.")

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break
adventure_game()
pygame.quit()