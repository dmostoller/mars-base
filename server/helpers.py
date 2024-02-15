import time
from rich import print
import random
from rich.console import Console
from models import *

console = Console()

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.01)
        # time.sleep(0)
    print()

def print_quickly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.005)
        # time.sleep(0)
    print()

def descision():
    return random.random() < 0.50


def goodbye(username):
    print_quickly("-----------------------------------------------------------------------------------------------------")
    console.print(f"Goodbye Ensign [bold magenta]{username}[/bold magenta], have a safe return journey to Earth.", justify="center")
    print("""\
                    o               .        ___---___                    .                   
                            .              .--\        --.     .     .         .
                                        ./.;_.\     __/~ \.     
                                        /;  / `-'  __\    . \                            
                    .        .       / ,--'     / .   .;   \        |
                                    | .|       /       __   |      -O-       .
                                    |__/    __ |  . ;   \ | . |      |
                                    |      /  \\_    . ;| \___|    
                        .    o       |      \  .~\\___,--'     |           .
                                    |     | . ; ~~~~\_    __|1
                        |             \    \   .  .  ; \  /_/   .
                        -O-        .    \   /         . |  ~/                  .
                        |    .          ~\ \   .      /  /~          o
                        .                   ~--___ ; ___--~       
                                    .          ---         .              
            """)

    return

def seed_tasks():
    air = db.session.get(Resource, 1)
    food = db.session.get(Resource, 2)
    fuel = db.session.get(Resource, 3)
    water = db.session.get(Resource, 4)
    
    tasks = []

    tasks.append(Task(
        name = "Change Air Filters", 
        description = "clean and replace the life support system air filters", 
        reward = random.randint(5,20),
        resource_id = air.id 
    ))
    tasks.append(Task(
        name = "Plant Seeds", 
        description = "plant new seeds in the soil of the hydroponic farm", 
        reward = random.randint(5,20),
        resource_id = food.id 
        ))
    tasks.append(Task(
        name = "Mine Ore", 
        description = "mine for ore that you can refined into fuel", 
        reward = random.randint(5,20),
        resource_id = fuel.id 
    ))
    tasks.append(Task(
        name = "Repair Valve", 
        description = "repair leaky valve on the main water pipe", 
        reward = random.randint(5,20),
        resource_id = water.id 
    ))
    tasks.append(Task(
        name = "Repair Air Conditioning", 
        description = "repair the main condensor on the air conditioning unit", 
        reward = random.randint(5,20),
        resource_id = air.id 
    ))
    tasks.append(Task(
        name = "Fertilize Soil", 
        description = "add fertilizer to the soil in the hydroponic farm", 
        reward = random.randint(5,20),
        resource_id = food.id 
    ))
    tasks.append(Task(
        name = "Refine Ore", 
        description = "refine the mined ore into its component elements", 
        reward = random.randint(5,20),
        resource_id = fuel.id 
    ))
    tasks.append(Task(
        name = "Clean Algae Vats", 
        description = "clean the algae vats that filter the water supply", 
        reward = random.randint(5,20),
        resource_id = water.id 
    ))
    tasks.append(Task(
        name = "Repair Fan Motor", 
        description = "repair or replace the motor for the air system fan", 
        reward = random.randint(5,20),
        resource_id = air.id 
    ))
    tasks.append(Task(
        name = "Till Soil", 
        description = "turn and till the soil of the hydroponic farm", 
        reward = random.randint(5,20),
        resource_id = food.id 
    ))
    tasks.append(Task(
        name = "Refill Fuel Cells", 
        description = "refill the base's fuel cells with the refined elements", 
        reward = random.randint(5,20),
        resource_id = fuel.id 
    ))
    tasks.append(Task(
        name = "Test Bacterial Levels", 
        description = "test the water supply for bacteria and other organisms", 
        reward = random.randint(5,20),
        resource_id = water.id 
    ))              
        
    db.session.add_all(tasks)
    db.session.commit()


