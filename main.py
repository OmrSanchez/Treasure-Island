print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

decision_one = input(
    "You come across a dark and gloomy hallway intersection with only a small torch providing the tiniest of light.\nYour only options are to turn left or right.\nTo the left, you hear screams of horror and terror.\nTo the right you can feel this extreme heat radiating down the corridor.\nWhich direction do you go in? (Left or Right) "
)
decision_one = decision_one.lower()
if decision_one == "left":
    decision_two = input(
        "You decided to go left.\nThe screams grow louder and louder.\nFrom a distance you can see a light source.\nUpon reaching the end of the hallway you come accross this giant lake that is infested with crocodiles.\nA man hangs from above the lake screaming to not be lowered.\nYou can see no other way to advance but to SWIM in the croc infested lake or turn around.\nFrom behind, you can feel the heat radiating hotter and hotter and the ground below you feet start to vibrate and grow into a loud shake.\nYou can not be certain, but it feels like the heat and ground shake are related.\nYou think to yourself that you have survived this long, maybe the best course to is to WAIT a second for a solution to hit you.\nAs the heat grows, you must decide what to do? (SWIM or WAIT) "
    )
    decision_two = decision_two.lower()
    if decision_two == "swim":
        decision_three = input(
            "In a moment, you see the crocodiles have their attention on the hanging man.\nYou dive into the lake!\nAs you splash in, you can hear an even louder scream 'NO!!!!PLEASE!!!' followed by a large splash.\nThe crocodiles pounce and tear the meat and bones off of the man.\nYou try swimming faster. Kicking and pullig yourself through the thick lake.\nThen suddenly, you kick something that feels like a tree truck.\nThis wasn't hear a second ago.\nYou want to look back but fear overtakes you.\nThere is no time.\nYou are almost to the other side.\nYou reach out with your had and touch land.\nOut of breath, you look down to find you dropped most of your gear.\nAll that is left is your compass and your sword.\nStaring across the lake, you almost through up as you see crocs fighting over an arm. You look away from the lake and press on.\nYou enter a dimly light room with three doors.\nA RED door, a BLUE door, and a YELLOW door.\nThey are not locked.\nWhich door do you take? "
        )
        decision_three = decision_three.lower()
        if decision_three == "red":
            print(
                f"You go through the {decision_three} door.\nIt is another long dark hallway.\nYou walk for what seems like hours.\nEventually, you decide to stop, rest, and gather you strength.\nAs you sit there, alone, in the dark.\nYou hear the faintest of footsteps.\nFirst to the left. Then to the right. Behind?\nThe footsteps are everywhere.\nSomething runs over and past your foot.\nThen you feel it again.\nThen two at a time.\nYou hear squeaks.\nRats!\nThey're surrounding you.\nYou have been spinning this whole time you don't know which way to go.\nThen at you try to go a direction, any direction to run into a wall.\nYou follow the wall with your hands and to your horror! You're trapped by walls in every direction.\nSuddenly, a rat just land on your shoulder, then another, then hundreds!\nHundreds of rats are now all over your body.\nYou squirm and squirm but there are too many.\nSoon you feel them biting.\nThey start devouring you, hundreds of chuncks at a time.\nIn the darkness, somewhere in the depths of the dungeon.\nYou get eaten alive by rats\nGAME OVER!"
            )
        elif decision_three == "blue":
            print(
                f"You go through the {decision_three} door.\nInside you find yourself in a treasure room.\nIt's like a city of gold in there.\nEvery nook and cranny contains treasure beyond your wildest beliefs.\nYou rush to the first pile of gold you find.\n'I knew it! It is real! I'm rich' you yell.\nYou fill your pockets and hands with as much gold as you can carry.\nAs you enjoy the fruits of your labor, you cannot help but lay down for a rest.\nYou lay down on a pile of gold coins and before you know it you fall asleep.\nYour body lays there in the stack of gold coins, however unbeknownst to you, magic fills this room.\nThis magic puts a person into an eternal sleep.\nOnce asleep they can never awaken. The person becomes comatosed.\nIn you glory, your overconfidence, you let your gaurd down and now this treasure room becomes your tomb.\nGAMEOVER!"
            )
        elif decision_three == "yellow":
            print(
                f"You go through the {decision_three} door.\nOnce inside you find that this a small room. No larger than a shed.\nTo your amazement you find a small chest.\nYou open the chest a find it is filled with gold trinkets and coins.\nA special item peaks your interest. A crown.\nIt has writing on it 'Whomever wears this crown gains dominion over GOD and his land.'\nUnsure what to make of it you put it on.\nSuddenly, power surges through your body. MAGIC! You gain infinite knowledge and learn the secrets of the land, the world, the universe.\nEmpowered, you feel unstopable. Suddendly, the room is engolfed in flames! A trap.\nThe flames burn everything in the room, however you do not feel any pain at all.\nInvulerability. Another ability gained by the power of the crown.\nWith this you can overcome anything in the world.\nYou snap your fingers and vanish into the void!\nThat night giant sparks were seen in the night sky and the stars were rearranged!\nFilled with the power of the 'ONE ABOVE ALL' you kill both god and the devil and become HIM!\nYOU WIN!"
            )
        else:
            print(
                f"{decision_three}.\nThis decision.\nBaffling!\nIt was completely wrong.\nStupid even.\n'The narrator confused by your decision decides to leave the game.'\nYou stand there in silence.\nThe decisions have ended.\nThe story over.\nWhy did you do that?\n{decision_three}.\nRemember your decision.\nGAME OVER!"
            )
    elif decision_two == "wait":
        print(
            "You stop and look around, but the path ends hear.\nYou wish you had more time.\n'It isn't fair. How did it come to this.' you think to yourself.\nThen you hear the man yell 'NOO!!!!PLEASE!!!' as he gets dropped into the crocadile infested lake.\nYou think that maybe he can be used as a distraction while you swim accross.\nIt's too late however, some crocodiles have spotted you and now wait for you to jump.\nSo much is happening. The ground shakes vigorously.\nYou turn around and what you see breaks your spirit.\nA demonic human-like figure, eyes red, emanating more heat than you have ever felt, approaches you.\n'HAHAHA'. The demon laughs at you.\nHis presence is overwhelming. You can't move, can't breathe, can't even think.\n'I may not have your treasure demon. But I still have my soul.' Your last words as you gather your strength and attempt to stab the demon.\nBefore you can stab anything, the demon strikes you through the head with its tail.\nYour lifeless body taken away.\nGAME OVER!"
        )
    else:
        print(
            f"{decision_two}.\nThis decision.\nBaffling!\nIt was completely wrong.\nStupid even.\n'The narrator confused by your decision decides to leave the game.'\nYou stand there in silence.\nThe decisions have ended.\nThe story over.\nWhy did you do that?\n{decision_two}.\nRemember your decision.\nGAME OVER!"
        )
elif decision_one == "right":
    print(
        "You turn right.\nThe heat is overbearing.\nYou start coughing and sweating.\nYou push on, hoping to find the source and end your suffering.\nThen you feel like each step you take is slower than the last.\nYou feel as if though you are walking on a sticky floor.\nYou reach down with your hand to touch the ground.\nIt burns your hand, yet feels just as dry as ever.\nAfter one more step you figure it out.\nYour boots are melting from the heat.\nYou feel a pain like no other.\nYou drop to your knees. You regret coming this direction.\nYour clothes starts to turn brown, then black.\nThen, they quickly fall off.\nYour mind gets lost in the pain.\nWater.\nThe last word that comes to mind and the next moment.\nDarkness.\nGAME OVER! "
    )
else:
    print(
        f"{decision_one}.\nThis decision.\nBaffling!\nIt was completely wrong.\nStupid even.\n'The narrator confused by your decision decides to leave the game.'\nYou stand there in silence.\nThe decisions have ended.\nThe story over.\nWhy did you do that?\n{decision_one}.\nRemember your decision.\nGAME OVER!"
    )

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
