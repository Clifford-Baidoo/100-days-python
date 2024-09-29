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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print('''You are an adventurer named Elias, renowned for your bravery and wits. 
      After hearing legends of an ancient treasure hidden deep within Skull Island, 
      you set sail alone. Armed with a map, a sword, and your instincts, you finally 
      arrive at the island. The air is thick with danger, and every decision could be 
      your last.''')

print("Chapter 1: The Landing")
print('''You step off your boat and onto the shore of Skull Island. The beach is eerily quiet,
       with only the waves gently crashing in the background. To your left is a dense jungle 
      with trees so thick they block out the sun. To your right is a rocky path leading up
       to a cliff.''')

choice = input("Which direction do you want to go? (left/right) ")

if choice.lower() == "left":
    print("Chapter 2: The Jungle")
    print('''You step cautiously into the jungle, the humidity thick and oppressive. 
          You hear strange noises all around — the chittering of unseen animals, the rustling of leaves. 
          As you press forward, you come across two paths: one leads to a dark cave, the other to a riverbank.''')
    choice = input("Which path do you want to take? (cave/river) ")
    if choice.lower() == "cave":
        print("Chapter 3: The Cave")
        print('''You light a torch and venture into the cave. The air is cold, and the walls are damp.
               As you walk deeper, you notice the faint glint of gold in the distance. Could it be the treasure? 
              Suddenly, a massive snake lunges from the shadows!''')
        choice = input("What do you do? (fight/run) ")
        if choice.lower() == "fight":
            print('''You draw your sword and slash at the snake. 
                  The creature is fast, but with a few well-aimed strikes, you manage to wound it. 
                  The snake slithers away into the darkness, leaving behind a treasure chest. 
                  You open it to find gold and jewels — you’ve found the treasure! 
                  Congratulations, you survive and become rich beyond your wildest dream''')
        else:
            print('''You turn and run, but the cave is narrow, and the snake is faster. 
                  It strikes, sinking its fangs into your leg. 
                  The venom courses through your body, and you collapse, unable to move. Sadly, you die.''')
    if choice.lower() == "river":
        print("Chapter 3: The River")
        print('''You follow the river, its waters crystal clear.
               Suddenly, you see something sparkling beneath the surface. 
              Is it the treasure? You lean in to get a closer look when you hear a loud roar. 
              A crocodile leaps out of the water, jaws wide open!
              Do you dive into the river or climb the trees''')
        choice = input("What do you do? (dive/climb) ")
        if choice.lower == "dive":
            print('''You dive into the river, narrowly avoiding the crocodile’s snap.
                   As you swim downstream, you notice something glimmering on the riverbed. 
                  You dive down and retrieve a chest filled with treasure!
                   You quickly return to the shore with the treasure in hand.
                   You survive and claim the riches!''')
        if choice.lower == "climb":
            print('''You scramble up the tree, just as the crocodile snaps at your heels. 
                  Unfortunately, the tree is covered in slick moss. You lose your grip and fall.
                   The crocodile is waiting. You die.''')
if choice.lower() == "right":
    print("Chapter 2: The Rocky Path")
    print('''You decide to take the rocky path up to the cliff.
           As you climb, you spot an old wooden bridge leading to a mysterious temple across the ravine.
           The bridge looks old and unstable. Below, jagged rocks wait for anyone who falls.''')
    choice = input("Do you want to cross the bridge or find another way? (bridge/another")
    if choice.lower() == "bridge":
        print('''You step onto the creaky bridge, testing its strength. 
              With every step, the planks groan under your weight. 
              Halfway across, the bridge snaps, sending you plunging into the ravine. 
              You die on the jagged rocks below.''')
    if choice.lower() == "another":
        print('''You decide to avoid the bridge and search for a safer route. 
              After some time, you find a hidden stone path leading down the cliff to a small cave.
               Inside, you discover the treasure chest resting atop a pedestal. 
              Carefully, you open it, and gold spills out. You survive, claiming the treasure for yourself!''')
        
print('''No matter the path you choose, Skull Island is full of dangers, but for the brave and the wise, 
      it also holds untold riches. Every decision you make leads to new perils or great rewards. 
      How many treasures can you find, and how many ways can you avoid your doom?''')