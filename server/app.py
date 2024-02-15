from config import app, migrate
from models import db, Task, Resource
from helpers import *
from rich import print
from rich.console import Console 
from rich.align import Align
from rich.table import Table 
import random 
# from playsound import playsound



if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    console = Console() 

    def powerup():
        # playsound('./sounds/smw_message_block.wav')
        pass

    def powerdown():
        # playsound('./sounds/smw_spring_jump.wav')
        pass

    def decrease_resource():
        r = [1, 2, 3, 4]
        resource = db.session.get(Resource, random.choice(r))
        rand_num = random.randint(5,10)
        resource.quantity -= rand_num
        db.session.commit()
        console.print(f"[red]Your {resource.name} reserves decreased by {rand_num}% due to normal usage.[/red]")

    def random_event():
        if random.random() < 0.25:
            print_quickly("-----------------------------------------------------------------------------------------------------")
            console.print("EMERGENCY ALERT", style="bold magenta", justify="center")
            x = [1, 2, 3, 4]
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
   
                
        
    def task_menu(username):      
        print_quickly("-----------------------------------------------------------------------------------------------------")

        console.print("CURRENT RESOURCE LEVELS", style="bold magenta", justify="center")
        table = Table(show_header=True, header_style="bold", border_style="none")
        table.add_column("Air", justify="center")
        table.add_column("Food", justify="center")
        table.add_column("Fuel", justify="center")
        table.add_column("Water", justify="center")
          
        air = db.session.get(Resource, 1)
        food = db.session.get(Resource, 2)
        fuel = db.session.get(Resource, 3)
        water = db.session.get(Resource, 4)
          
        table.add_row(
            f"[yellow]{air.quantity}%[/yellow]",
            f"[green]{food.quantity}%[/green]",
            f"[red]{fuel.quantity}%[/red]",
            f"[blue]{water.quantity}%[/blue]"
        )
        console.print(Align.center(table))

        def load_tasks(username, resource):
            tasks_remaining = Task.query.first()
            if not tasks_remaining:
                console.print("We have just recieved a comminication from mission control.", style="magenta", justify="center")
                console.print("They have provided additional tasks for you to complete.", style="magenta", justify="center")
                seed_tasks()  

            print_quickly("-----------------------------------------------------------------------------------------------------")

            console.print("TASKS", style="bold magenta", justify="center")
            table2 = Table(show_header=False, header_style="bold", border_style="none")
            table2.add_column("", justify="center")
            table2.add_column("Name", justify="left")
            table2.add_column("Description", justify="left")
            table2.add_column("Reward", justify="center")
            table2.add_column("Resource",  justify="left")


            if resource == None:
                tasks = Task.query.all()
            elif resource.lower() == "air" or resource.lower() == "food" or resource.lower() == "fuel" or resource.lower() == "water":
                if resource.lower() == "air":
                    res_id = 1
                elif resource.lower() == "food":
                    res_id = 2
                elif resource.lower() == "fuel":
                    res_id = 3
                elif resource.lower() == "water":
                    res_id = 4
              
                tasks = Task.query.filter_by(resource_id = res_id).all()

            for task in tasks:
                if task.resource.name == "Air":
                    text_color = "yellow"
                elif task.resource.name == "Food":
                    text_color = "green"
                elif task.resource.name == "Fuel":
                    text_color = "red"
                elif task.resource.name == "Water":
                    text_color = "blue"
                              
                table2.add_row(
                    f"{task.id}",
                    f"{task.name}",
                    f"{task.description}",
                    f"+{task.reward}%",
                    f"{task.resource.name}",
                    style=f"{text_color}"
            )

            console.print(Align.center(table2))
            console.print("Please enter a number to select a task, type a resource name to view tasks for that resource, or type exit to leave the game.")

        load_tasks(username, None)

        task_response = input()
        if task_response.lower() == "exit":
            goodbye(username)
        elif task_response.lower() == "air":
            load_tasks(username, "air")
        elif task_response.lower() == "food":
            load_tasks(username, "food")
        elif task_response.lower() == "fuel":
            load_tasks(username, "fuel")
        elif task_response.lower() == "water":
            load_tasks(username, "water")
        elif isinstance(task_response, int):                
            task_to_do = db.session.get(Task, {task_response})
            console.print(f"Would you like to [green italic]{task_to_do.name}[/green italic] and replenish your {task_to_do.resource.name} supply by {task_to_do.reward}%?")
            console.print("Input [green]yes[/green] to attempt task or [red]exit[/red] to select another task.")
            attempt_task = input()
            if attempt_task.lower() == "yes":  
                resource_to_update = db.session.get(Resource, {task_to_do.resource.id})            
                if descision():
                    #update resource table to increment resource quantity
                    resource_to_update.quantity += task_to_do.reward
                    if resource_to_update.quantity >= 100:
                        resource_to_update.quantity = 100
                    else:
                        pass
                    db.session.commit()
                    #print text saying task completed
                    console.print(f"Your attempt to {task_to_do.name} was successful. You have replenished your {task_to_do.resource.name} supply by {task_to_do.reward}%", style="green")
                    #delete task row
                    db.session.delete(task)
                    db.session.commit()                 
                    #return to main menu
                    decrease_resource()
                    powerup()
                    random_event()
                    task_menu(username)
                else:
                    console.print(f"Your attempt to {task_to_do.name} has failed, please try again.", style="red")
                    decrease_resource()
                    powerdown()
                    random_event()
                    task_menu(username)
            elif attempt_task.lower() == "exit":
                decrease_resource()
                random_event()
                task_menu(username)
            else:
                goodbye(username)

    
    def main_menu(username):
        print("""\
                  
                      .    _     *       \|/   .       .      -*-              +
                        .' \\`.     +    -*-     *   .         '       .   *
                    .  |__''_|  .       /|\ +         .    +       .           |
                        |     | .                                        .     -*-
                        |     |           `  .    '             . *   .    +    '
                      _.'-----'-._     *                  .
                    /             \__.__.--._______________
                """)
        task_menu(username)  
    
    


    
    def welcome():
        print("""\
              

          .         _  .          .          .    +     .          .          .      .
                  .(_)          .            .            .            .       :
                  .   .      .    .     .     .    .      .   .      . .  .  -+-        .
                    .           .   .        .           .          /         :  .
              . .        .  .      /.   .      .    .     .     .  / .      . ' .
                  .  +       .    /     .          .          .   /      .
                .            .  /         .            .        *   .         .     .
                .   .      .    *     .     .    .      .   .       .  .
                    .           .           .           .           .         +  .
            . .        .  .       .   .      .    .     .     .    .      .   .

          .   +      .          ___/\_._/~~\_...__/\__.._._/~\        .         .   .
                .          _.--'                              `--./\          .   .
                    /~~\/~\                                         `-/~\_            .
          .      .-'                                                      `-/\_
            _/\.-'                                                          __/~\/\-.__
          .'                                                                           `                     
        
              ███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗  █████╗ ███████╗███████╗
              ████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝
              ██╔████╔██║███████║██████╔╝███████╗    ██████╔╝███████║███████╗█████╗  
              ██║╚██╔╝██║██╔══██║██╔══██╗╚════██║    ██╔══██╗██╔══██║╚════██║██╔══╝  
              ██║ ╚═╝ ██║██║  ██║██║  ██║███████║    ██████╔╝██║  ██║███████║███████╗
              ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝          
              """)
        console.print("Please enter your name to begin......", style="bold magenta", justify="center")
        username = input()
        console.print(f"Welcome to the UN Mars Base, Ensign [bold magenta]{username}[/bold magenta]!")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print("Your job is to ensure the continued operational status of the base's life support systems.")
        console.print("The base relies on four resources: [yellow]Air[/yellow], [green]Food[/green], [red]Fuel[/red] and [blue]Water[/blue].")
        console.print("These resources are consumed at a steady rate and will become depleted over time.")
        console.print("You must perform tasks to maintain and replenish these resources before they run out.")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print(f"Would you like to begin the game, Ensign [bold magenta]{username}[/bold magenta]?")
        console.print("Please enter [green]start[/green] to begin, or [red]exit[/red] to quit.", style="bold")
        def start():
            begin_res = input()
            if begin_res.lower() == "start":
                main_menu(username)
            elif begin_res.lower() == "exit":
                goodbye(username) 
            else:
                console.print("Invalid input, please try again.", style="red")
                start()
        start()
      
    welcome()

    

    



    # remove pass and write your cli logic


