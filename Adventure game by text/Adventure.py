import random

def create_character(name, health, damage):
    return {
        "name": name,
        "health": health,
        "max_health": health,
        "damage": damage,
    }

def create_wizard():
    return create_character("Wizard", 65, 25)

def create_knight():
    return create_character("Knight", 75, 20)

def create_rogue():
    return create_character("Rogue", 63, 23)

def create_enemy(name, health, damage):
    return create_character(name, health, damage)

def display_with_spacing(text):
    print("\n" + text + "\n")

def display_enemy_health(enemy):
    health_bar = "=" * (enemy["health"] * 20 // enemy["max_health"])
    display_with_spacing(f"{enemy['name']} Health: [{health_bar}] {enemy['health']}/{enemy['max_health']}")

def player_attack(player, enemy):
    damage = random.randint(player["damage"] // 2, player["damage"])
    enemy["health"] -= damage
    return damage

def enemy_attack(enemy, player):
    damage = random.randint(enemy["damage"] // 2, enemy["damage"])
    player["health"] -= damage
    return damage

def level_one(player):
    beast = create_enemy("Wild Beast", 45, 12)
    display_with_spacing("=== Level 1 ===")
    display_with_spacing("You find yourself in a dark forest.")
    display_with_spacing("A wild beast suddenly appears!")

    health_potion_count = 1
    explore_count = 0

    while player["health"] > 0 and beast["health"] > 0:
        display_with_spacing(f"{player['name']} Health: {player['health']}")
        display_enemy_health(beast)
        action = input("Choose your action (1. Attack, 2. Run, 3. Explore): ")

        if action == "1":
            damage = player_attack(player, beast)
            display_with_spacing(f"You attack the wild beast and deal {damage} damage.")
            enemy_damage = enemy_attack(beast, player)
            display_with_spacing(f"The wild beast attacks and deals {enemy_damage} damage.")
        elif action == "2":
            if random.random() < 0.7:  # 70% chance of successfully running
                display_with_spacing("You try to run away and successfully escape from the wild beast.")
                return "level_two"
            else:
                display_with_spacing("You try to run away, but the wild beast catches you.")
                enemy_damage = enemy_attack(beast, player)
                display_with_spacing(f"The wild beast attacks and deals {enemy_damage} damage.")
        elif action == "3" and explore_count < 2:
            display_with_spacing("You explore and find a health potion. You drink it and regain full health.")
            player["health"] = player["max_health"]
            health_potion_count -= 1
            display_with_spacing(f"{player['name']} Health: {player['health']}")
        else:
            display_with_spacing("Invalid choice. Choose 1, 2, or 3.")

        if health_potion_count <= 0:
            display_with_spacing("You've run out of health potions.")
        explore_count += 1

    if player["health"] <= 0:
        display_with_spacing("Game over.")
    else:
        display_with_spacing("You defeated the Wild Beast!")
        return "level_two"

def level_two(player):
    haunted_knight = create_enemy("Haunted Knight", 60, 18)
    display_with_spacing("=== Level 2 ===")
    display_with_spacing("You enter a haunted castle.")
    display_with_spacing("A spooky haunted knight appears!")

    explore_count = 0

    while player["health"] > 0 and haunted_knight["health"] > 0:
        display_with_spacing(f"{player['name']} Health: {player['health']}")
        display_enemy_health(haunted_knight)
        action = input("Choose your action (1. Attack, 2. Sneak past, 3. Search): ")

        if action == "1":
            damage = player_attack(player, haunted_knight)
            display_with_spacing(f"You attack the haunted knight and deal {damage} damage.")
            enemy_damage = enemy_attack(haunted_knight, player)
            display_with_spacing(f"The haunted knight attacks and deals {enemy_damage} damage.")
        elif action == "2":
            if random.random() < 0.5:  # 50% chance of engaging in combat when sneaking
                display_with_spacing("You try to sneak past the haunted knight, but it notices you!")
                enemy_damage = enemy_attack(haunted_knight, player)
                display_with_spacing(f"The haunted knight attacks and deals {enemy_damage} damage.")
            else:
                display_with_spacing("You successfully sneak past the haunted knight.")
                return "level_three"
        elif action == "3" and explore_count < 2:
            display_with_spacing("You search and find a valuable item.")
        else:
            display_with_spacing("Invalid choice. Choose 1, 2, or 3.")

        explore_count += 1

    if player["health"] <= 0:
        display_with_spacing("Game over.")
    else:
        display_with_spacing("You defeated the Haunted Knight!")
        return "level_three"

def level_three(player):
    enchanted_tree = create_enemy("Enchanted Tree", 85, 18)
    display_with_spacing("=== Level 3 ===")
    display_with_spacing("You reach a mystical forest.")

    first_turn_converse = True

    while player["health"] > 0 and enchanted_tree["health"] > 0:
        display_with_spacing(f"{player['name']} Health: {player['health']}")
        display_enemy_health(enchanted_tree)

        if first_turn_converse:
            action = input("Choose your action (1. Attack, 2. Converse with the tree, 3. Climb the tree): ")

            if action == "1":
                damage = player_attack(player, enchanted_tree)
                display_with_spacing(f"You attack the enchanted tree and deal {damage} damage.")
                enemy_damage = enemy_attack(enchanted_tree, player)
                display_with_spacing(f"The enchanted tree attacks and deals {enemy_damage} damage.")
            elif action == "2":
                display_with_spacing("You converse with the enchanted tree. It offers to let you pass and restores your health.")
                player["health"] = player["max_health"]
                first_turn_converse = False
                final_boss(player)
            elif action == "3":
                display_with_spacing("You attempt to climb the tree to bypass the obstacle, but it shakes you off.")
                enemy_damage = enemy_attack(enchanted_tree, player)
                display_with_spacing(f"The enchanted tree attacks and deals {enemy_damage} damage.")
            else:
                display_with_spacing("Invalid choice. Choose 1, 2, or 3.")
        else:
            action = input("Choose your action (1. Attack, 2. Climb the tree): ")

            if action == "1":
                damage = player_attack(player, enchanted_tree)
                display_with_spacing(f"You attack the enchanted tree and deal {damage} damage.")
                enemy_damage = enemy_attack(enchanted_tree, player)
                display_with_spacing(f"The enchanted tree attacks and deals {enemy_damage} damage.")
            elif action == "2":
                display_with_spacing("You attempt to climb the tree to bypass the obstacle, but it shakes you off.")
                enemy_damage = enemy_attack(enchanted_tree, player)
                display_with_spacing(f"The enchanted tree attacks and deals {enemy_damage} damage.")
            else:
                display_with_spacing("Invalid choice. Choose 1 or 2.")

    if player["health"] <= 0:
        display_with_spacing("Game over.")
    else:
        display_with_spacing("You passed the Enchanted Tree!")
        return "final_boss"

def final_boss(player):
    special_attack = False
    dragon = create_enemy("Dragon", 100, 25)
    display_with_spacing("=== Final Boss ===")
    display_with_spacing("You enter a cavern where a fierce dragon awaits!")

    while player["health"] > 0 and dragon["health"] > 0:
        display_with_spacing(f"{player['name']} Health: {player['health']}")
        display_enemy_health(dragon)
        action = input("Choose your action (1. Attack, 2. Special Attack): ")

        if action == "1":
            damage = player_attack(player, dragon)
            display_with_spacing(f"You attack the dragon and deal {damage} damage.")
            enemy_damage = enemy_attack(dragon, player)
            display_with_spacing(f"The dragon attacks and deals {enemy_damage} damage.")
        elif action == "2" and special_attack == False:
            damage = player_attack(player, dragon)
            display_with_spacing(f"You use a special attack on the dragon and deal {damage + 15} damage.")
            special_attack = True
            enemy_damage = enemy_attack(dragon, player)
            display_with_spacing(f"The dragon attacks and deals {enemy_damage} damage.")
        else:
            display_with_spacing("Invalid choice. Choose 1 or 2.")

    if player["health"] <= 0:
        display_with_spacing("Game over. The dragon defeated you!")
    else:
        display_with_spacing("Congratulations! You have defeated the Dragon and completed the game!")

def main():
    display_with_spacing("Welcome to the text-based adventure game!")
    display_with_spacing("Choose your class:")
    display_with_spacing("1. Wizard (Health: 60, Damage: 25)")
    display_with_spacing("2. Knight (Health: 70, Damage: 20)")
    display_with_spacing("3. Rogue (Health: 65, Damage: 23)")

    class_choice = input("Enter the number of your chosen class: ")

    if class_choice == "1":
        player = create_wizard()
    elif class_choice == "2":
        player = create_knight()
    elif class_choice == "3":
        player = create_rogue()
    else:
        display_with_spacing("Invalid choice. Please choose 1, 2, or 3.")
        return

    display_with_spacing(f"You are a {player['name']}. Get ready for the adventure!")

    level = "level_one"

    while level:
        if level == "level_one":
            level = level_one(player)
        elif level == "level_two":
            level = level_two(player)
        elif level == "level_three":
            level = level_three(player)
        elif level == "final_boss":
            final_boss(player)
            break

if __name__ == "__main__":
    main()