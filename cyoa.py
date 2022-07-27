location = input
name = input
items = input
self = input
class Player:
     def __init__(self, name, items):
         self.name = name
         self.items = items

class Room:
    def __init__(self, name, objects, floor, description):
        self.name = name
        self.objects = objects
        self.floor = floor
        self.description = description

person = Player(name, [])
art_room = Room("Art Room", ["Box Cutter"], "Fourth Floor", "The art room was painted with stains upon stains of dry paint and broken sculptures. Around you was useless paint brushes, and box cutters. Maybe you can pick the box cutters up for protection 😲") 
hallway1 = Room("Hallway", [], "Fourth Floor", "You're now in the hallway! Its completely deserted, aside from the broken windows. Most of the classroom doors were borded up by the teachers so students in the classrooms couldn't escape, but you were lucky to have woken up before the teachers came back to barricade the door you were at. There's a staircase, the art room, and the math room. Where would you like to go? 🤔\n")
math_room = Room("Math Room", [], "Fourth Floor", "As you stepped in the classroom, you were face to face, with your math teacher, holding a bat. Your attempts to scurry out failed, as a teacher had held the door closed, leaving you to await your death. Shouldn't have trusted going into the math room 😬")
closet = Room("Closet", [], "Fourth Floor", "You stay in the closet, hoping that you could simply wait it out. Unfortunately, your heavy breathing caused a teacher, the science teacher, to hear your. Maybe the closet wasn't the best option. 🤭")
windows = Room("Windows", [], "Fourth Floor", "You're literally on the fourth floor. Why on earth would you think that you would survive that fall 🤨? Its too late now, since you're already dead 😂.")
suicide = Room("Art Room", [], "Fourth Floor", "Seems like staying in here for too long wasn't the best option, as you began to go deep in thought about the situation, becoming more and more depressed that you might not be able to live the way you used to. Falling into despair, you had no choice, but to use the box cutter on yourself. How unfortunate 😢")
roof = Room ("Roof", [], "Roof", "Yikes. Seems like the roof wasn't the best choice to pick, as most teachers suspected that students would go there for sos. You were swarmed by teachers, getting pushed off the roof. Yikers.")
person.name = input("Hello. Welcome to my game. Please type in what you'd like to be addressed as 😊:")
hallway2 = Room ("Hallway", [], "Third Floor", "You made it to the 3rd floor. The rooms and hall were deserted, a scary sight to see. There was the music room, as well as the girl's bathroom. The boy's was borded up for whatever reason. You can also travel down to the 2nd floor through the staircase. Going back up to the 4th floor may get you in trouble, considering that the teachers are hunting for you. Where would you like to go? 🤔\n")
music_room = Room ("Music Room", [], "Third Floor", "Immediately, your ears explode from walking in, some teachers blasting music right in your ear. Before you could even react to it, your ears were blasted with music again, and you were stuck in a loop of having your ears explode 😵.")
bathroom = Room ("Bathroom", [], "Third Floor", "Seems like the teachers hadn't thought to check the bathrooms, considering that you were completely safe stepping in the bathroom. After 5 minutes, you stepped out the bathroom, finding yourself in a completely different setting than where you were before. The walls were covered in a nostolgic yellow pattern, the floor was a moist carpet, and the halls were practically identical. I don't think you're supposed to be here 😕.")
hallway3 = Room ("Hallway", [], "Second Floor", "You go down to the 2nd floor, where there are many abandonded classrooms, borded up, as well as the science lab and the computer lab. You may travel down to the 1st floor, as the 3rd floor in unavailable due to the rabid teachers that came down to the 3rd floor. Where to next? 🤔\n")
science_lab = Room ("Science Lab", [], "Second Floor", "You stepped into the science lab, where the entire classroom engulfed in flames, the  science teacher leaking gases inside and creating a spark with the door. To be honest, you should never trust the science teacher in these situations 😞.")
computer_lab = Room ("Computer Lab", [], "Second Floor", f"Walking in, it seemed pretty normal. You decided to try and kill time by playing something on the computers, booting it up and turning on the only game on the computer, Roblox. You thought that if you voice chatted and told someone that you were in trouble, you could alert the cops, as you didn't have your phone on you.\n 'Hello? Is anyone in this game?' You ask, hoping that someone had voice chat, and indeed someone did! \n 'Hi. I'm here.' \n 'Oh good. Please call the cops, the teachers in my school have gone insane! 😥'\n 'No thanks. I wouldn't wanna snitch on myself. Sorry for this, {person.name} 😇'\n Immediately, you were knocked out, waking up back where you started, but this time, the teachers were there, not very happy. Yikes.")
hallway4 = Room ("Hallway", [], "First Floor", "Finally, you made it to the first floor. In order to escape, you must break the exit to the school. You can also go to the gymnasium to see if any students are there. Don't try to go back up though.")
gymnasium = Room ("Gymnasium", [], "First Floor", "As you stepped in, you walked into what looked like teachers having a ceremony, perhaps of having taught the students a lesson. They all turned to you, huge grins on their face. Despite how open it was, the teachers formed a giant circle around you, as they surrounded you, singing a song you absolutely HATE. That's a fate worse than death 🤢.")
print(f"Okay! Hello {person.name}.")
location = input("You woke up in the middle of your homeroom, confused. Why were you here? And why were you at school so late?. After thinking about it, you remember. You remember how you got there. The teachers had gone crazy, and locked you and your classmates in the school! Should've done your homework 😔. Anyways, around you is the closet, the windows, and the classroom exit. Where would you like to go? 🤔\n")

if location == "closet": 
    print(closet.description)
    print("GAME OVER. Ending 1 out of 12, FOUND 🤫")
elif location == "windows":
    print(windows.description)
    print("GAME OVER. Ending 2 out of 12, FALLEN ⏬")
elif location == "classroom exit":
    location = input (hallway1.description)
    if location == "art room":
        print(art_room.description)
        user_input = input("Do you plan to take one? 🤔\n")
        if user_input == "yes":
            unwanted=art_room.objects.pop(0)
            person.items.append(unwanted)
            print("Okay! The box cutter has been added to your inventory!")
            user_input = input("Would you like to return to the hallway? 🤔\n")
            if user_input == "yes":
                location = input (hallway1.description)
                if location == "math room":
                    print(math_room.description)
                    print("GAME OVER. Ending 4 out of 12, CAUGHT 🫣")
                elif location == "borded room":
                    print("You step into the boarded room, where you find the students, partying in the room. What's going on? You ask.\n 'ITS JUST A PRANK BRO.'")
                    print("SECRET ENDING, PRANK 🤣")
                elif location == "staircase":
                    location = input("Okay! Would you like to go to the Roof or the 3rd floor? 🤔 \n")
                    if location == "roof":
                        print(roof.description)
                        print("GAME OVER. Ending 5 out of 12, PUSHED 🥲")
                    elif location == "3rd floor":
                        location = input(hallway2.description)
                        if location == "music room":
                            print(music_room.description)
                            print("GAME OVER. Ending 6 out of 12, MUSIC 🎶")
                        elif location == "girl's bathroom":
                            print(bathroom.description)
                            print("GAME OVER. Ending 7 out of 12, BACKROOMS 😵")
                        elif location == "staircase":
                            location = input(hallway3.description)
                            if location == "science lab":
                                print(science_lab.description)
                                print("GAME OVER. Ending 8 out of 12, EXPLOTION 💥")
                            elif location == "computer lab":
                                print(computer_lab.description)
                                print("GAME OVER. Ending 9 out of 12, ROBLOX 🎮")
                            elif location == "staircase":
                                location = input(hallway4.description)
                                if location == "exit":
                                    user_input = input("You must break the door with your feet! Break door? 🤔\n")
                                    if user_input == "yes":
                                        print("You kicked the door with all your might, and although you might've broken your foot from how hard you kicked it, you were able to escape, limping off to safety. Congrats! You've escaped!")
                                        print("CONGRATS! Ending 12 out of 12, FREEDOM 🥳🥳🥳")
                                    else:
                                        print("Your descision ended up causing the police to burst open the doors, all trampling over you. They came at the worse time.")    
                                        print("GAME OVER. Ending 11 out of 12, POLICE 🚓")
                                elif location == "gymnasium":
                                    print(gymnasium.description)
                                    print("GAME OVER. Ending 10 out of 12, TORTURE 😩")
            else:
                print(suicide.description)
                ("GAME OVER. Ending 3 out of 12, SUICIDE 🔪")
        else:
            ("Okay. Would you like to return to the hallway?")
            if user_input == "yes":
                location = input (hallway1.description)
                if location == "math room":
                    print(math_room.description)
                    print("GAME OVER.  Ending 4 out of 12, CAUGHT 🫣")
                elif location == "borded room":
                    print("You step into the boarded room, where you find the students, partying in the room. What's going on? You ask.\n 'ITS JUST A PRANK BRO.'")
                    print("SECRET ENDING, PRANK 🤣")
                elif location == "staircase":
                    location = input ("Okay! Would you like to go to the Roof or the 3rd floor? 🤔\n")
                    if location == "roof":
                        print(roof.description)
                        print("GAME OVER. Ending 5 out of 12, PUSHED 🥲")
                    elif location == "3rd floor":
                        location = input(hallway2.description)
                        if location == "music room":
                            print(music_room.description)
                            print("GAME OVER. Ending 6 out of 12, MUSIC 🎶")
                        elif location == "girl's bathroom":
                            print(bathroom.description)
                            print("GAME OVER. Ending 7 out of 12, BACKROOMS 😵")
                        elif location == "staircase":
                            location = input(hallway3.description)
                            if location == "science lab":
                                print(science_lab.description)
                                print("GAME OVER. Ending 8 out of 12, EXPLOTION 💥")
                            elif location == "computer lab":
                                print(computer_lab.description)
                                print("GAME OVER. Ending 9 out of 12, ROBLOX 🎮")
                            elif location == "staircase":
                                location = input(hallway4.description)
                                if location == "exit":
                                    user_input = input("You must break the door with your feet! Break door? 🤔")
                                    if user_input == "yes":
                                        print("You kicked the door with all your might, and although you might've broken your foot from how hard you kicked it, you were able to escape, limping off to safety. Congrats! You've escaped!")
                                        print("CONGRATS! Ending 12 out of 12, FREEDOM 🥳🥳🥳")
                        else:
                            print("Your descision ended up causing the police to burst open the doors, all trampling over you. They came at the worse time.")    
                            print("GAME OVER. Ending 11 out of 12, POLICE 🚓")
                    elif location == "gymnasium":
                        print(gymnasium.description)
                        print("GAME OVER. Ending 10 out of 12, TORTURE 😩")
            else:
                (suicide.description)
                ("GAME OVER. Ending 3 out of 12, SUICIDE 🔪")
    elif location == "math room":
        print(math_room.description)
        print("GAME OVER.  Ending 4 out of 12, CAUGHT 🫣")
    elif location == "borded room":
        print("You step into the boarded room, where you find the students, partying in the room. What's going on? You ask.\n 'ITS JUST A PRANK BRO.'")
        print("SECRET ENDING, PRANK 🤣")
    elif location == "staircase":
        location = input("Okay! Would you like to go to the Roof or the 3rd floor? 🤔 \n")
        if location == "roof":
            print(roof.description)
            print("GAME OVER. Ending 5 out of 12, PUSHED 🥲")
        elif location == "3rd floor":
            location = input(hallway2.description)
            if location == "music room":
                print(music_room.description)
                print("GAME OVER. Ending 6 out of 12, MUSIC 🎶")
            elif location == "girl's bathroom":
                print(bathroom.description)
                print("GAME OVER. Ending 7 out of 12, BACKROOMS 😵")
            elif location == "staircase":
                location = input(hallway3.description)
                if location == "science lab":
                    print(science_lab.description)
                    print("GAME OVER. Ending 8 out of 12, EXPLOTION 💥")
                elif location == "computer lab":
                    print(computer_lab.description)
                    print("GAME OVER. Ending 9 out of 12, ROBLOX 🎮")
                elif location == "staircase":
                    location = input(hallway4.description)
                    if location == "exit":
                        user_input = input("You must break the door with your feet! Break door? 🤔")
                        if user_input == "yes":
                            print("You kicked the door with all your might, and although you might've broken your foot from how hard you kicked it, you were able to escape, limping off to safety. Congrats! You've escaped!")
                            print("CONGRATS! Ending 12 out of 12, FREEDOM 🥳🥳🥳")
                        else:
                            print("Your descision ended up causing the police to burst open the doors, all trampling over you. They came at the worse time.")    
                            print("GAME OVER. Ending 11 out of 12, POLICE 🚓")
                    elif location == "gymnasium":
                        print(gymnasium.description)
                        print("GAME OVER. Ending 10 out of 12, TORTURE 😩")