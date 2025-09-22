import random
import time

def rock_simulator():
    print("Welcome to pet rock simulator")
    player_name = input("What is your name? ")
    rock_name = input("What would you like to name your pet rock? ")
    
    hunger = 5
    energy = 5
    weight = 5
    
    print(f"\nHello {player_name}, meet your rock {rock_name}! 🪨")
    print("Take good care of it, Or don't. Let’s see what happens.\n")

    while True:
        print(f"\n--- {rock_name}'s Stats ---")
        print(f"Hunger: {hunger}/10")
        print(f"Energy: {energy}/10")
        print(f"Weight: {weight}/10")

        print("\nWhat would you like to do?")
        print("1. Feed your rock")
        print("2. Let your rock rest")
        print("3. Take your rock for a walk")
        print("4. Play with your rock")
        print("5. Do nothing...")
        print("6. Quit game")

        choice = input("Choose an option (1-6): ")

        # Player choices
        if choice == "1":
            hunger -= 2
            weight += 1
            print(f"You fed {rock_name}.")
        elif choice == "2":
            energy += 2
            hunger += 1
            print(f"{rock_name} took a nap.")
        elif choice == "3":
            weight -= 1
            energy -= 2
            print(f"You walked {rock_name}. People stared.")
        elif choice == "4":
            hunger += 1
            energy -= 1
            print(f"You played fetch with {rock_name}. You did all the work.")
        elif choice == "5":
            hunger += 1
            energy -= 1
            print(f"You ignored {rock_name}. It sat there.")
        elif choice == "6":
            print(f"Thanks for playing, {player_name}! {rock_name} will miss you.")
            break
        else:
            print("Invalid choice.")
            
        if random.random() < 0.2:
            event = random.choice([
            "A bird tried to sit on your rock.",
            "Someone mistook your rock for modern art.",
            f"{rock_name} rolled slightly downhill.",
            f"{rock_name} got mossy. It looks fancy now."
            ])
            print(f"Random Event: {event}")
            
        hunger = max(0, min(hunger, 10))
        energy = max(0, min(energy, 10))
        weight = max(1, min(weight, 10))
        
        
        if hunger >= 10:
            print(f"Oh no! {rock_name} crumbled from neglect (too hungry). 💀")
            break
        elif energy <= 0:
            print(f"{rock_name} has no energy left and turned into gravel. 🪨➡️🪨🪨")
            break
        elif weight <= 0:
            print(f"{rock_name} eroded away into sand. 🏖️")
            break
        elif weight >= 10:
            print(f"{rock_name} grew so heavy it sank into the earth forever. 🌍")
            break

        time.sleep(1)
        
rock_simulator()