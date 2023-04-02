Shubham Kulkarni skulkarn1@stevens.edu

# URL to GitHub Repo



# Estimate on number of hours spent on the project

I spent approximately 6 hours on the project assignment - 1

# A description on how you tested your code

First started the testing on the maps provided in the description itself, followed by custom 5-6 maps for baseline functions.

Since I used a personalized extension after taking permission to implement, I tested 2 maps, 1 which will have the key required to carryout the extension and 1 of the map for baseline testing so that changes in extension map doesn't affect the baseline functionality.

# Bugs or Issues

Currently there are no bugs or issues in the code.

# Resolved Issues with example

I used a personalized extension of authorization. Entering a room earns you 1 point. In addition to this implementing Authorization for entering a room based on points. Let's assume room2 requires 1 point to enter and room3 requires 2 points to enter. Room 2 and 3 are on north and east respective of room 1. User enter room1 and gain 1 point, now it can go either north or east, but since east requires 2 points, it has to go to to north only.

In order to implement this extension I had to add a key in the map file ie 'pointstoenter' which indicates the points required to enter a room. After adding this field, my code was failing for baseline features as baseline map didnt have 'pointstoenter' key, so had to customize it to make my code work on both maps.

Here is the example of the issue when tested initially on baseline map: "KeyError, pointstoenter not found."

I solved it by checking initially whether the map has 'pointstoenter' key or not, to distinguish between a custom map with baseline map.

# Three Extension implemented

1. Drop: The syntax to drop a object present in the inventory is -> drop <object-name>

If the object is there in the inventory, it will get added to the Items list present in the current room. If it's not there in the inventory then you will get a message -> "No such item in the inventory".

2. Direction: Instead of typing "go <direction>", we can just type <direction> or abbrevation(north -> n or southeast -> se) of it to go to the room located in that direction.

If we can go in the direction based on maps, then you will enter the room in that direction, else you will get a message -> "There's no way to go <direction>."

3. Authorization based on points: Entering a room earns you 1 point. In addition to this implementing Authorization for entering a room based on points. Let's assume room2 requires 1 point to enter and room3 requires 2 points to enter. Room 2 and 3 are on north and east respective of room 1. User enter room1 and gain 1 point, now it can go either north or east, but since east requires 2 points, it has to go to to north only.

No Specific syntax is required for this, just changes in the map required, which has been submitted in the custom map file attached. There will be a "pointstoenter" key for every room in the maps, which indicates the points required to enter the room.


