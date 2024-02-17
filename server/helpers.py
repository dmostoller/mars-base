import time
from rich import print
import random
from rich.console import Console
from models import *
from playsound import playsound
from lorem_text import lorem

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


def decrease_resource(difficulty):
    if difficulty == "hard":
        range_low = 25
        range_high = 50
    else:
        range_low = 10
        range_high = 25

    r = [1, 2, 3, 4]
    resource = db.session.get(Resource, random.choice(r))
    rand_num = random.randint(range_low,range_high)
    resource.quantity -= rand_num
    db.session.commit()
    # print(range_low, range_high)
    console.print(f"[red]Your {resource.name} reserves decreased by {rand_num}% due to normal usage.[/red]")

def resource_depleted():
    resources = Resource.query.all()
    for resource in resources:
        if resource.quantity <= 0:
            return True

def resources_filled():
    resources_full = False
    resources = Resource.query.all()
    for resource in resources:
        if resource.quantity >= 100:
            resources_full = True
        else:
            resources_full = False
    return resources_full


def add_task(new_name, resource):
    new_description = lorem.words(6) 
    if resource.lower() == "air":
        res_id = 1
    elif resource.lower() == "food":
        res_id = 2
    elif resource.lower() == "fuel":
        res_id = 3
    elif resource.lower() == "water":
        res_id = 4
    new_task = Task(
        name = new_name,
        description = new_description,
        reward = 50,
        resource_id = res_id 
    )
    db.session.add(new_task)
    db.session.commit()

def powerup():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smb_coin.wav')

def powerdown():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smb_pipe.wav') 

def goodnews():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smb_powerup.wav') 

def badnews():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smb_warning.wav') 

def win_sound():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smb_stage_clear.wav')

def lose_sound():    
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smb_mariodie.wav')

def intro_sound():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/sm64_exit_course_pause_menu.wav')

def goodbye_sound():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smas-smb3_peach-letter.wav')

def add_task_sound():
    playsound('/Users/Kabayun/Development/code/phase-3/mars-base/sounds/smw_kick.wav')

def goodbye(username):
    print_quickly("-----------------------------------------------------------------------------------------------------")
    console.print(f"Goodbye Commander [bold]{username}[/bold], have a safe return journey to Earth.",style="magenta", justify="center")
    print("""\
                    o                .        ___---___                    .                   
                            .              .--\        --.     .     .         .
                                         ./.;_.\     __/~ \.     
                                        /;  / `-'  __\    . \                            
                    .         .       / ,--'     / .   .;   \        |
                                     | .|       /       __   |      -O-       .
                                    |__/    __ |  . ;   \ | . |      |
                                    |      /  \\_    . ;| \___|    
                        .    o      |      \  .~\\___,--'     |           .
                                     |     | . ; ~~~~\_    __|1
                         |             \    \   .  .  ; \  /_/   .
                        -O-        .    \   /         . |  ~/                  .
                         |    .          ~\ \   .      /  /~          o
                        .                   ~--___ ; ___--~       
                                    .           ---         .              
            """)
    goodbye_sound()
def you_died(username):
    print_quickly("-----------------------------------------------------------------------------------------------------")
    print("""\
          
                                  ██████╗  █████╗ ███╗   ███╗███████╗       
                                 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝       
                                 ██║  ███╗███████║██╔████╔██║█████╗         
                                 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝         
                                 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗       
                                  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝       
                                                                         
                                  ██████╗ ██╗   ██╗███████╗██████╗          
                                 ██╔═══██╗██║   ██║██╔════╝██╔══██╗         
                                 ██║   ██║██║   ██║█████╗  ██████╔╝         
                                 ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗         
                                 ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║         
                                  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                  
            
         """)
    console.print(f"One or more of the base's resources were depleted. Better luck next time, Commander [bold]{username}[/bold].", style="magenta", justify="center")
    lose_sound()

def you_win(username):
    print_quickly("-----------------------------------------------------------------------------------------------------")
    print("""\
                                    
                          ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
                          ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
                           ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
                            ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
                             ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
                             ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝            
                                        
         """)
    console.print(f"All base resources levels are over 100%. Congratulations, Commander [bold]{username}[/bold]!", style="magenta", justify="center")
    win_sound()

def seed_tasks():
    Task.query.delete()

    print_slowly("Contacting Mission Control..........................................................................")

    air = db.session.get(Resource, 1)
    food = db.session.get(Resource, 2)
    fuel = db.session.get(Resource, 3)
    water = db.session.get(Resource, 4)
    
    tasks = []

    tasks.append(Task(
        name = "Change Air Filters", 
        description = "clean and replace the HVAC system air filters", 
        reward = random.randint(10,35),
        resource_id = air.id 
    ))
    tasks.append(Task(
        name = "Plant Seeds", 
        description = "plant new seeds in the soil of the hydroponic farm", 
        reward = random.randint(10,35),
        resource_id = food.id 
        ))
    tasks.append(Task(
        name = "Mine Ore", 
        description = "mine for ore that you can refined into fuel", 
        reward = random.randint(10,35),
        resource_id = fuel.id 
    ))
    tasks.append(Task(
        name = "Repair Valve", 
        description = "repair leaky valve on the main water pipe", 
        reward = random.randint(10,35),
        resource_id = water.id 
    ))
    tasks.append(Task(
        name = "Repair Air Conditioning", 
        description = "repair the main condensor on the A/C unit", 
        reward = random.randint(10,35),
        resource_id = air.id 
    ))
    tasks.append(Task(
        name = "Fertilize Soil", 
        description = "add fertilizer to the soil in the hydroponic farm", 
        reward = random.randint(10,35),
        resource_id = food.id 
    ))
    tasks.append(Task(
        name = "Refine Ore", 
        description = "refine the mined ore into its component elements", 
        reward = random.randint(10,35),
        resource_id = fuel.id 
    ))
    tasks.append(Task(
        name = "Clean Algae Vats", 
        description = "clean the algae vats that filter the water supply", 
        reward = random.randint(10,35),
        resource_id = water.id 
    ))
    tasks.append(Task(
        name = "Repair Fan Motor", 
        description = "repair or replace the motor for the air system fan", 
        reward = random.randint(10,35),
        resource_id = air.id 
    ))
    tasks.append(Task(
        name = "Till Soil", 
        description = "turn and till the soil of the hydroponic farm", 
        reward = random.randint(10,35),
        resource_id = food.id 
    ))
    tasks.append(Task(
        name = "Refill Fuel Cells", 
        description = "refill the base's fuel cells with refined ore", 
        reward = random.randint(10,35),
        resource_id = fuel.id 
    ))
    tasks.append(Task(
        name = "Test Bacterial Levels", 
        description = "test the water supply for bacteria and organisms", 
        reward = random.randint(10,35),
        resource_id = water.id 
    ))              
        
    db.session.add_all(tasks)
    db.session.commit()
    console.print("We have just recieved a comminication from mission control.", style="magenta", justify="center")
    console.print("They have provided additional tasks for you to complete.", style="magenta", justify="center")


def random_event():
    if random.random() < 0.5:
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print("EMERGENCY ALERT", style="bold magenta", justify="center")
        x = [1, 2, 3, 4, 5, 6, 7, 8]
        rand_ev = random.choice(x)
        # print(rand_ev)
        if rand_ev == 1:
            # print("ONE")
            fuel = db.session.get(Resource, 3)
            fuel.quantity -= 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("Aliens have attacked the base, resulting in the loss of 20% of your fuel reserves.", style="magenta", justify="center")
            console.print("""
                                    
                                            o
                                            \_/\o
                                            ( Oo)                    \|/
                                            (_=-)  .===O-  ~~Z~A~P~~ -O-
                                            /   \_/U'                /|
                                            ||  |_/
                                            ||  |
                                            {K ||
                                            | PP
                                            | ||
                                            (__||

                """)
            badnews()
        elif rand_ev == 2:
            # print("TWO")
            food = db.session.get(Resource, 2)
            food.quantity -= 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("The base was impacted by a powerful solar flare, resulting in the loss of 20% of your food reserves.", style="magenta", justify="center")
            console.print("""                            

                                            .       . 
                                          +  :      .
                                                    :       _
                                                .   !   '  (_)
                                                   ,|.' 
                                         -  -- ---(-O-`--- --  -
                                                  ,`|'`.
                                                ,   !    .
                                                    :       :  " 
                                                    .     --+--
                                          .:        .       !                              

                """)
            badnews()
        elif rand_ev == 3:
            # print("THREE")
            air = db.session.get(Resource, 1)
            air.quantity -= 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("A meteorite has hit the base, the resulting leak has resulted in the loss of 20% of your air reserves.", style="magenta", justify="center")
            console.print("""    
                                                        
                                                            .:'
                                                        _.::'
                                            .-;;-.   (_.'
                                           / ;;;'  \
                                          |.  `:   | 
                                           \:   `; /
                                            '-..-'
                                
                """)
            badnews()
        elif rand_ev == 4:
            # print("FOUR")
            water = db.session.get(Resource, 4)
            water.quantity -= 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")            
            console.print("There was an explosion in the hydrogen processing plant, resulting in the loss of 20% of your water reserves.", style="magenta", justify="center")
            console.print("""    

                            
                                              _ ._  _ , _ ._
                                            (_ ' ( `  )_  .__)
                                         ( (  (    )   `)  ) _)
                                        (__ (_   (_ . _) _) ,__)
                                            `~~`\ ' . /`~~`
                                                  ;   ;
                                                  /   /
                                    _____________/_ __ \_____________                                                        

                            
                """)
            badnews()   
        elif rand_ev == 5:
            # print("FOUR")
            water = db.session.get(Resource, 1)
            water.quantity += 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("An experimental drug has reduced your oxygen intake, your air reserves have increased by 20%", style="magenta", justify="center")
            console.print("""    

                                              _________
                                             {_________}
                                              )=======(
                                             /         \
                                            | _________ |
                                            ||   _     ||
                                            ||  |_)    ||
                                            ||  | \/   ||
                                      __    ||    /\   ||
                                 __  (_|)   |'---------'|
                                (_|)        `-.........-'                                                  

                            
                """)
            goodnews()
        elif rand_ev == 6:
            # print("FOUR")
            water = db.session.get(Resource, 3)
            water.quantity += 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("The yield from ore harvesting was larger than expected, your power reserves have increased by 20%.", style="magenta", justify="center")
            console.print("""    

                                ) ) )                     ) ) )
                              ( ( (                      ( ( (
                              ) ) )                       ) ) )
                           (~~~~~~~~~)                 (~~~~~~~~~)
                            | POWER |                   | POWER |
                            |       |                   |       |
                            I      _._                  I       _._
                            I    /'   `\                I     /'   `\
                            I   |   N   |               I    |   N   |
                            f   |   |~~~~~~~~~~~~~~|    f    |    |~~~~~~~~~~~~~~|
                        .'    |   ||~~~~~~~~|    |  .'     |    | |~~~~~~~~|   |
                        /'______|___||__###___|____|/'_______|____|_|__###___|___|                                                     

                            
                """)
            goodnews()
        elif rand_ev == 7:
            # print("FOUR")
            water = db.session.get(Resource, 2)
            water.quantity += 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("The farm had a surplus harvest, your food stores have increased by 20%.", style="magenta", justify="center")
            console.print("""    

                                ,,,                      ,,,
                               {{{}}    ,,,             {{{}}    ,,,
                            ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,, 
                           {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
                            ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
                            \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
                            \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
                            \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
                            \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                    
                            
                """)
            goodnews()
        elif rand_ev == 8:
            # print("FOUR")
            water = db.session.get(Resource, 4)
            water.quantity += 20
            db.session.commit()
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("A supply ship has arrived. Your water supplies have increased by 20%", style="magenta", justify="center")
            console.print("""    

                                            `. ___
                                            __,' __`.                _..----....____
                                __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
                          _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
                        ,'________________                          \`-._`-','
                        `._              ```````````------...___   '-.._'-:
                            ```--.._      ,.                     ````--...__\-.
                                    `.--. `-`                       ____    |  |`
                                    `. `.                       ,'`````.  ;  ;`
                                        `._`.        __________   `.      \'__/`
                                        `-:._____/______/___/____`.     \  `
                                                    |       `._    `.    \
                                                    `._________`-.   `.   `.___
                                                                        `------'`                                                    

                            
                """)
            goodnews() 
   
                