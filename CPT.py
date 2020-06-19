import random
global monster_storylines
monster_storylines = ["|You enter a cave and find a ", "|You walk by a lake and find a ", "|You walk by a pond and find a ",
 "|You hear a noise and head towards it only to find a ", "|An arrow is shot at you and barely misses you, you see a "]
global buff_storylines
buff_storylines = ["|You find a potion by a tree, do you drink it?|", "|You find a wizard and he offers you a drink|",
 "|You find an elixir leaking from a tree, do you drink it?|", "|You find a lake filled with a strange liquid do you drink it?|"]
global monster_goblin
monster_goblin = {"name": "Goblin", "hp": 10, "atk": 15}
global monster_rascal
monster_rascal = {"name": "Rascal", "hp": 15, "atk":10}
global monster_dreadgolem
monster_dreadgolem = {"name": "Dread Golem", "hp": 150, "atk":20}
global monster_dragon
monster_dragon = {"name": "Dragon", "hp": 100, "atk":25}
global simple_monsters
simple_monsters = [monster_goblin, monster_rascal]
global difficult_monsters
difficult_monsters = [monster_dreadgolem, monster_dragon]
global simple_monster_names
simple_monster_names = ["Goblin|", "Rascal|"]
global difficult_monster_names
difficult_monster_names = ["Dread Golem|", "Dragon|"]
global player
player = {"max hp": 100, "hp": 100, "atk": 20, "heal": 35}

# ---------------------------------------------------------------------------------------------------------------------

def greetings():
    player_name = str(input("Enter your name here: "))

    print("|Hello " + player_name + "|")
    print(" ")
    print("|Welcome to the Ravaged Forest!|")
    print(" ")
    print("|In order to get out of the forest you must fight your way through several monsters and make it out alive.|")
    print(" ")
    print("|There will be 8 rounds to get past.|")
    print(" ")
    print("|You will start with: |")
    print(" ")
    print("|100 hp|")
    print(" ")
    print("|20 attack damage|")
    print(" ")
    print("|15 healing ability|")
    print(" ")
    print("|You will only get 3 heal uses every fight.|")
    print(" ")
    print("|You now enter the forest...|")
    print(" ")
    print("|You first find an elder wizard who offers you a drink.|")
    print(" ")
    print("|Do you accept?|")

# ---------------------------------------------------------------------------------------------------------------------

def monster_determine_simple(easy_monster):
    if easy_monster == "Goblin|":
        easy_monster = simple_monsters[0]
        return easy_monster
    elif easy_monster == "Rascal|":
        easy_monster = simple_monsters[1]
        return easy_monster

# ---------------------------------------------------------------------------------------------------------------------
    
def monster_determine_difficult(difficult_monster):
    if difficult_monster == "Dread Golem|":
        difficult_monster = difficult_monsters[0]
        return difficult_monster
    elif difficult_monster == "Dragon|":
        difficult_monster = difficult_monsters[1]
        return difficult_monster

# ---------------------------------------------------------------------------------------------------------------------

def random_story_easy():
    easy_story = random.choice(monster_storylines)
    easy_monster = random.choice(simple_monster_names)
    print(easy_story + easy_monster)
    return easy_monster

# ---------------------------------------------------------------------------------------------------------------------

def random_story_difficult():
    difficult_story = random.choice(monster_storylines)
    difficult_monster = random.choice(difficult_monster_names)
    print(difficult_story + difficult_monster)
    return difficult_monster

# ---------------------------------------------------------------------------------------------------------------------

def random_element_story():
    element = random.choice(buff_storylines)
    print(element)

# ---------------------------------------------------------------------------------------------------------------------

def random_buff_nerf():
    health_buff = player["hp"] + 10
    attack_buff = player["atk"] + 10
    heal_buff = player["heal"] + 10
    max_hp_buff = player["max hp"] + 10
    attack_buff_strong = player["atk"] + 12.5
    max_hp_nerf = player["max hp"] - 10
    health_nerf = player["hp"] - 10
    attack_nerf = player["atk"] - 5
    heal_nerf = player["heal"] - 5
    buffs = [health_buff, attack_buff, heal_buff, health_nerf, attack_nerf, 
    heal_nerf, attack_buff_strong, max_hp_buff, max_hp_nerf]
    buff_nerf_choice = random.choice(buffs)
    if buff_nerf_choice == health_buff:
        player["hp"] = health_buff
        if player["hp"] > player["max hp"]:
            player["hp"] = player["max hp"]
            print("|Health cannot go above max health.|")
        else:
            print("|+10 You got a health buff!|")
    elif buff_nerf_choice == attack_buff:
        player["atk"] = attack_buff
        print("|+10 You got an attack buff!|")
    elif buff_nerf_choice == max_hp_buff:
        if player["hp"] == player["max hp"]:
            player["max hp"] = max_hp_buff
            player["hp"] = player["max hp"]
            print("|+10 You got a max health buff!|")
        else:
            player["max hp"] = max_hp_buff
            print("|+10 You got a max health buff!|")
    elif buff_nerf_choice == max_hp_nerf:
        if player["hp"] == player["max hp"]:
            player["max hp"] = max_hp_nerf
            player["hp"] = player["max hp"]
            print("|-10 You lost max health!|")
        else:
            player["max hp"] = max_hp_nerf
            print("|-10 You lost max health!|")
    elif buff_nerf_choice == attack_buff_strong:
        player["atk"] = attack_buff_strong
        print("|+12.5 You got an attack buff!|")
    elif buff_nerf_choice == heal_buff:
        player["heal"] = heal_buff
        print("|+10 You got a heal buff!|")
    elif buff_nerf_choice == health_nerf:
        player["hp"] = health_nerf
        print("|-10 You lost health!|")
        if player["hp"] <= 0:
            print(" ")
            print("|Game Over|")
            exit()
    elif buff_nerf_choice == attack_nerf:
        player["atk"] = attack_nerf
        print("|-5 You lost attack!|")
    else:
        player["heal"] = heal_nerf
        print("|-5 You lost heal!|")

# ---------------------------------------------------------------------------------------------------------------------

def acceptOrdeclineDrink():
    print("|yes/no ?|")
    choice1 = 0
    while choice1 != "yes" or "no":
        choice1 = input()
        if choice1 == "yes":
            random_buff_nerf()
            print(player)
            print("|You leave the wizard and venture out further into the forest.|")
            return
        elif choice1 == "no":
            print("|You leave the wizard and venture out further into the forest.|")
            return
        else:
            print("|Choose one of the options.|")

# ---------------------------------------------------------------------------------------------------------------------

def acceptOrdecline():
    print("|yes/no ?|")
    choice1 = 0
    while choice1 != "yes" or "no":
        choice1 = input()
        if choice1 == "yes":
            random_buff_nerf()
            print(player)
            return
        elif choice1 == "no":
            return
        else:
            print("|Choose one of the options.|")

# ---------------------------------------------------------------------------------------------------------------------

def monster_action_choice(monster, player):
    print(monster)
    damage_done = 0
    count = 0
    while monster["hp"] != 0:
        print("|Please select action:|")
        print("|1) attack|")
        print("|2) heal|")
        action_choice = input()
        if action_choice == "heal":
            if player["hp"] < player["max hp"]:
                player["hp"] <= player["max hp"]
                player["hp"] = player["hp"] + player["heal"]
                print(player)
                print("|The monster attacks you|")
                player["hp"] = player["hp"] - monster["atk"]
                print(player)
                count += 1
            if count == 3:
                print("|Heal uses used up for this round.|")
                action_choice != "heal"

            if player["hp"] >= player["max hp"]:
                print("|Cannot heal anymore.|")

            if player["hp"] <= 0:
                print(" ")
                print("|Game Over|")
        elif action_choice == "attack":
            damage_done += player["atk"]
            monster["hp"] = monster["hp"] - player["atk"]
            print(monster)
            if monster["hp"] > 0:
                print("|The monster attacks you|")
                player["hp"] = player["hp"] - monster["atk"]
                print(player)
                if player["hp"] <= 0:
                    print(" ")
                    print("|Game Over|")
                    exit()
            else:
                print("|You have slain the monster.|")
                monster["hp"] = monster["hp"] + damage_done
                break
        else:
            print("|Choose one of the options|")

# ---------------------------------------------------------------------------------------------------------------------
# Main Code execution

greetings()
print(" ")
acceptOrdeclineDrink()
print(" ")
monster_action_choice(monster_determine_simple(random_story_easy()), player)
for i in range(1, 5):
    round_count = str(i)
    print(" ")
    print("|You have made it to " + "Round: " + round_count + "|")
    random_element_story()
    acceptOrdecline()
    monster_action_choice(monster_determine_simple(random_story_easy()), player)
for i in range(5, 9):
    round_count = str(i)
    print(" ")
    print("|You have made it to " + "Round: " + round_count + "|")
    random_element_story()
    acceptOrdecline()
    monster_action_choice(monster_determine_difficult(random_story_difficult()), player)
    if int(i) == 8:
        print("|Congratulations! You have made it through the Ravaged Forest!|")