print("Welcome to Granny Hounted House!")
name = input("What is your name?: ")
age = int(input("What is your age?: "))

health = 10

print(f"Hello {name}, welcome to your worse dream!")

if age >= 18:
    print("You are eligible to enter this house compound.")

    want_to_play = input("Do you want to play? (yes/no): ").lower()
    if want_to_play == "yes":
        print("Prepare for the worse day in your life!!!")
        print(f"You are starting with {health} health.")

        left_or_right = input("First...Left or Right? (left/right): ").lower()
        if left_or_right == "left":
            ans = input("Nice one...you follow the path and reach a lake, do you swim across or go around? (across/around): ").lower()
            if ans == "around":
                print("You went around and reach the other side of the lake.")
            elif ans == "across":
                print("You were bitten by a Tiger fish and lost 5 health.")
                health -= 5
                print(f"You are now left with {health} health.")

            ans = input("You notice a house and a bush, which one do you choose, house or bush? (house/bush): ").lower()
            if ans == "house":
                print("You found granny and immediately she kill you.")
                print("YOU LOSE!!!")
            elif ans == "bush":
                print("You manage to run away from Granny.")

            ans = input("You found 2 coloured boxes, Red and White, choose one. (red/white): ").lower()
            if ans == "red":
                print("You found a hand grenade and immediately you throw the hand grenade to Granny's house...BOOM!!! YOU WIN!!!")
            elif ans == "white":
                print("You found a Cobra in the box and immediately it bite you! You you manage to kill it and lost 5 health.")
                health -= 5
                
                if health <= 0:
                    print("YOU LOSE!!!")
                else:
                    print("You have survive...YOU WIN!!!")

        else:
            print("You fell down and lost...YOU LOSE!!!")

    else:
        print("So sad to see you go, 'till we meet next time.")

else:
    print("Sorry, you are not eligible to play this game.")