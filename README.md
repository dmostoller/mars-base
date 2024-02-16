# Mars Base

This app is an interactive CLI game created with SQLAlchemy and Python. 

## How to Play the Game:

To run the program, please run the following commands in the *mars-base* directory:

pipenv install
pipenv shell

then cd into the server folder and run:

python seed.py
python app.py

Then enter your name to begin the game.

You are the Commander of the UN Mars Base. The base relies on four resources, Air, Food, Fuel, and Water.  
Mission control has sent you a list of tasks to do that each increase *one* of the four resources by a random amount.
Each task has a 50% chance of success, and each time you attempt a task a randomly selected resource will be depleted by a randomly selected amount.
You resource levels start at 50% capactity.
If any of the resources reaches 0%, you lose the game.
If you can replenish all four resources to at least 100%, you win the game.
If you neglect any of your resources you will quickly run out, so you should try to perform tasks with the highest rewards.
You can filter current tasks so you can more easily compare the rewards to select the highest yielding tasks. 
If you run out of tasks, more will be sent from mission control automatically.
Additionally, if you're not satifsified with the rewards for the available tasks, you can re-roll a new set of tasks with a new set of randomly generated reward values.
You can type *add* on the task menu to manually create your own task for whichever resource you need, with a 50% potential reward.

There are also random events that either deplete or replenish a given resource by 20%, so be careful not to let your resources levels get too low! You never know when disaster can strike!
Finally, if you want an even bigger challenge, you can begin the game in hard mode, which effectively doubles the rate of resource depletion. Make sure your choices count!


## Database Structures:

The app uses SQLAlchemy to create a database with two tables in a one-to-many relationship.

### Tasks table 

| Column|Type|
|-----|-------|       
|id|primary integer|
|name|string|
|description|string|
|resource_id|foreign integer|
|reward|integer|

### Resources table 

| Column|Type|
|-----|-------|       
|id|primary integer|
|name|string|
|quantity|integer|


Utilizing sessionmaker within SQLAlchemy, the code is able to constantly obtain information from these tables, as well as update the database as the game progresses. 

## Additional resources:

The Rich library was used to style the text and make tables in the CLI.
The Playsound library was used to play sound effects in the game.
Varous random python methods like randint were used to generate random values in a range and to set probablities. 