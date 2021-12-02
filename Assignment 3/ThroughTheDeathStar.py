#CPCS230-03
#Homework Assignment 3

#Choose Your Own Adventure

import random

# variable creation & setting loop control variable
room = 1
# generating a random number
death_die = random.randint(1,100)

while room != 0:
    #Docking Bay
    if room == 1:
        print('You are a Jedi and have landed on the Death star do you "fight"')
        print('through the stormtroopers to the armory or run away to the "flight control" room?')
        print()
        choice = input('What is your choice youngling? "fight" or "flight control"? :')
        if choice == 'fight':
            if death_die > 80:
                print("You got blasted to death by stormtroopers")
                room = 0
            else:
                room = 2
            death_die = random.randint(1,100)
        elif choice == 'flight control':
            room = 3
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
    # Armory Room
    elif room == 2:
        print()
        print('You do crazy Jedi lightsaber moves and kill all the stormtroopers and you made it to the armory')
        print('Do you keep going to the "gravity" control room, ')
        print('"blow up" the armory or go back to the "flight control" room?')
        print()
        choice = input('What will it be young padawon? "gravity" "blow up" or "flight control" :')
        if choice == 'blow up':
            print("You blew up the armory and yourself. You are now a force ghost (>'.')>")
            room = 0
        elif choice == 'gravity':
            room = 4
        elif choice == 'flight control':
            room = 3
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
    #Flight Control Room
    elif room == 3:
        print()
        print('You seal the door behind you and find your self in front of Emperor Palpatine')
        print('Fight Emperor "Palpatine", turn to the dark side and "join" Palpatine, run back to "fight" the stormtroopers near the armory,')
        print('or flee to the "engine" room?')
        print()
        choice = input('Execute order 66 young Jedi! "Palpatine" "join" "fight" "engine" :')
        if choice == 'Palpatine':
            if death_die > 20:
                print("You got electrocuted to death by Emporor Palpatine")
                room = 0
            else:
                room = 6
            death_die = random.randint(1,100)
        elif choice == 'join':
            print("You joined Emporor Palpatine and rule the empire for all eternity with an iron fist")
            room = 0
        elif choice == 'fight':
            if death_die > 80:
                print("You got blasted to death by stormtroopers")
                room = 0
            else:
                room = 2
            death_die = random.randint(1,100)
        elif choice == 'engine':
            room = 5
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
    #Gravity Room
    elif room == 4:
        print()
        print('In the gravity room you can either pull the "lever", go "fight" your way back to the armory, or')
        print('go through to the "engine" room.')
        print()
        choice = input('May the force be with you and choose. "lever" "fight" "engine" :')
        if choice == 'fight':
            if death_die > 80:
                print("You got blasted to death by stormtroopers")
                room = 0
            else:
                room = 2
            death_die = random.randint(1,100)
        elif choice == 'lever':
            if death_die > 50:
                print("You float around and you couldn't get back to the lever. You float into the intake and are chopped up")
                room = 0
            else:
                print()
                print("You float around but you use your force powers back to the lever and switch it back")
                room = 4
            death_die = random.randint(1,100)
        elif choice == 'engine':
            room = 5
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
    #Engine Room
    elif room == 5:
        print()
        print('You are now in the engine room. You can "destroy" the engine, go to the "gravity" control room,')
        print('or go to the "flight control" room')
        print()
        choice = input('Trust your instincts! "destroy" "gravity" "flight control" :')
        if choice == 'destroy':
            if death_die > 95:
                print("You hit a gas tank with your lightsaber and the explosion destroys the death star and you.")
                print("The galaxy is now safe but you are dead.")
                room = 0
            else:
                room = 6
            death_die = random.randint(1,100)
        elif choice == 'flight control':
            room = 3
        elif choice == 'gravity':
            room = 4
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
    #Reactor Room
    elif room == 6:
        print()
        print('You have won but you were then force teleported to the reactor room and Darth Vader is infront of you with lightsaber in hand.')
        print('Do you "fight" Darth Vader, "join" Darth Vader, or "flee" in fear?')
        print()
        choice = input('There Is No Escape! Don\'t make me destroy you! "fight" "join" "flee" :')
        if choice == 'fight':
            if death_die > 65:
                print('Darth Vader overcomes you with spectacular lightsaber abilities and cuts you into two.')
                room = 0
            else:
                room = 7
            death_die = random.randint(1,100)
        elif choice == 'join':
            print("You start to kneel and embrace the darkside. Darth Vader and you rule the Galaxy with an iron fist")
            room = 0
        elif choice == 'flee':
            print("You try to flee but Darth Vader uses the force to bring your neck to his palm.")
            print("He then stabs you in the gut and you are dead.")
            room = 0
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
    #The Final Choice
    else:
        print()
        print('With astounding abilities you disarm Darth Vader of his lightsaber and he pleads for his life')
        print()
        Ultimate_Choice = input('Do you kill him or spare him? "kill" "spare" :')
        if Ultimate_Choice == 'kill':
            print()
            print("You take both lightsabers and strike him down. The galaxy is now rid of the evil forces of the Sith and the Empire.")
            print("The Galaxy is at peace. But you might slip into the darkside like Anakin did when he killed Count Duku.")
            room = 0
        elif Ultimate_Choice == 'spare':
            print()
            print("You put away both lightsabers and give out a hand to Darth Vader")
            print("He clasp your hand and you both embrace")
            print("Darth Vader changes his ways and the galaxy has true peace and posperity.")
            room = 0
        else:
            print(choice, " wasn't one of the options Jedi Scum. Try again." )
