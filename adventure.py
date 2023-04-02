import sys
import json

file = open(f'{sys.argv[-1]}')
data = json.load(file)
curr_room = 0
inventory = []

def computeabb(direction):
    if direction == "n" or direction == "north":
        return "north"
    if direction == "s" or direction == "south":
        return "south"
    if direction == "e" or direction == "east":
        return "east"
    if direction == "w" or direction == "west":
        return "west"
    if direction == "nw" or direction == "northwest":
        return "northwest"
    if direction == "ne" or direction == "northeast":
        return "northeast"
    if direction == "sw" or direction == "southwest":
        return "southwest"
    if direction == "se" or direction == "southeast":
        return "southeast"

def get(item):
    global inventory, curr_room, data, file
    if str(item) in data[curr_room]['items']:
        inventory.append(item)
        data[curr_room]['items'].remove(str(item))
        print(f"You pick up the {item}.")
    else:
        print(f"There's no {item} anywhere.")

def drop(item):
    global inventory, curr_room, data, file
    print(f"You drop the {item}.")
    if 'items' in data[curr_room]:
        data[curr_room]['items'].append(str(item))
    else:
        data[curr_room]['items'] = [f"{item}"]
    inventory.remove(item)

def look():
    global curr_room, data, file
    print(f"> {data[curr_room]['name']}\n")
    print(f"{data[curr_room]['desc']}\n")
    if 'items' in data[curr_room]:
        item = ""
        count = 1
        for i in data[curr_room]['items']:
            if count <= len(data[curr_room]['items']) and count!=1:
                item += ", " + i
            else:
                item += " " + i
            count += 1
        print(f"Items:{item}\n")
    exit = ""
    for i in data[curr_room]['exits']:
        exit += " " + i
    print(f"Exits:{exit}\n")    

def go(direction):
    global file, data, curr_room
    return data[curr_room]['exits'][f'{direction}']

nextmove = ""
look()
directionlist = ["north", "south", "east", "west", "northeast", "northwest", "southeast", "southwest"]
points = 1
while("quit" not in nextmove):
    nextmove = input("What would you like to do? ")
    nextmove = nextmove.lower()
    nextmove = nextmove.split(" ")
    if len(nextmove) == 1 and computeabb(nextmove[0]) in directionlist:
        direction = computeabb(nextmove[0])
        if direction in data[curr_room]['exits']:
            if "pointstoenter" in data[0]:
                nextroom = go(direction)
                if int(data[nextroom]['pointstoenter']) <= points:
                    print(f"You go {direction}.\n")
                    points += 1
                    curr_room = nextroom
                    look()
                else:
                    print(f"You are not authorized to go {direction} as you have insufficient points.")
            else:
                nextroom = go(direction)
                print(f"You go {direction}.\n")
                curr_room = nextroom
                look()
        else:
            print(f"There's no way to go {direction}.")
    elif "go" in nextmove and len(nextmove) > 1:
        direction = nextmove[-1]
        if direction in data[curr_room]['exits']:
            if 'pointstoenter' in data[0]:
                nextroom = go(direction)
                if int(data[nextroom]['pointstoenter']) <= points:
                    print(f"You go {direction}.\n")
                    points += 1
                    curr_room = nextroom
                    look()
                else:
                    print(f"You are not authorized to go {direction} as you have insufficient points.")
            else:
                nextroom = go(direction)
                print(f"You go {direction}.\n")
                curr_room = nextroom
                look()
        else:
            print(f"There's no way to go {direction}.")
    elif "go" in nextmove and len (nextmove)<=1:
        print("Sorry, you need to 'go' somewhere.")

    elif "look" in nextmove:
        look()

    elif "quit" in nextmove:
        print("Goodbye!")
        break
    
    elif "inventory" in nextmove:
        if len(inventory) == 0:
            print("You're not carring anything.")
        else:
            print("Inventory:")
            for i in inventory:
                print(f" {i}")
    elif "get" in nextmove:
        item = ""
        for i in range(1,len(nextmove)):
            item += nextmove[i] + " "
        item = item.rstrip()
        if len(nextmove) <= 1:
            print("Sorry, you need to 'get' something.")
        elif 'items' not in data[curr_room]:
            print(f"There's no {item} anywhere.")
        else:
            get(item)
    
    elif "drop" in nextmove:
        item = ""
        for i in range(1,len(nextmove)):
            item += nextmove[i] + " "
        item = item.rstrip()
        if item not in inventory:
            print("No such item in the inventory")
        else:
            drop(item)

    else:
        print("Use 'quit' to exit.")
    
