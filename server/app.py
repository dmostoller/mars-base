from config import app, migrate
from models import db, Task, Resource
from helpers import *
from rich import print
from rich.console import Console 
from rich.align import Align
from rich.table import Table 


if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    console = Console() 

    def task_menu(username, difficulty): 
        if not resource_depleted():
            if not resources_filled():
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

                def load_tasks(username, resource, difficulty):    
                    tasks_remaining = Task.query.first()
                    if not tasks_remaining:
                        seed_tasks()

                    print_quickly("-----------------------------------------------------------------------------------------------------")
                    console.print("TASKS", style="bold magenta", justify="center")
                    table2 = Table(show_header=False, header_style="bold", border_style="none")
                    table2.add_column("", justify="center")
                    table2.add_column("Name", justify="left")
                    table2.add_column("Description", justify="left")
                    table2.add_column("Reward", justify="center")
                    table2.add_column("Resource",  justify="left")

                    current_tasks = []

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
                        current_tasks.append(f"{task.id}")

                    console.print(Align.center(table2))
                    console.print("Please input a [magenta]task number[/magenta] to select a task or a [magenta]resource name[/magenta] to view tasks for that resource.")
                    console.print("Input [magenta]refresh[/magenta] to request new tasks from Mission Control.")
                    if resource != None:
                        console.print("Input [green]all[/green] to show all tasks.")
                    console.print("Input [red]exit[/red] to leave the game.") 
                    def task_select(username, difficulty):
                        task_response = input()
                        if task_response.lower() == "exit":
                            goodbye(username)
                        elif task_response.lower() == "refresh":
                            seed_tasks()
                            load_tasks(username, None, difficulty) 
                        elif task_response.lower() == "all":
                            load_tasks(username, None, difficulty)   
                        elif task_response.lower() == "air":
                            load_tasks(username, "air", difficulty)
                        elif task_response.lower() == "food":
                            load_tasks(username, "food", difficulty)
                        elif task_response.lower() == "fuel":
                            load_tasks(username, "fuel", difficulty)
                        elif task_response.lower() == "water":
                            load_tasks(username, "water", difficulty)
                        elif task_response in current_tasks:                
                            task_to_do = db.session.get(Task, {task_response})
                            print_quickly("-----------------------------------------------------------------------------------------------------")
                            console.print(f"Would you like to [green italic]{task_to_do.name}[/green italic] and replenish your {task_to_do.resource.name} supply by {task_to_do.reward}%?")
                            console.print("Input [green]yes[/green] to attempt task or [red]back[/red] to select another task.")
                            print_quickly("-----------------------------------------------------------------------------------------------------")                        
                            def execute_task(username, difficulty):      
                                attempt_task = input()
                                if attempt_task.lower() == "yes":
                                    resource_to_update = db.session.get(Resource, {task_to_do.resource.id})            
                                    if descision():
                                        #update resource table to increment resource quantity
                                        resource_to_update.quantity += task_to_do.reward
                                        if resource_to_update.quantity >= 150:
                                            resource_to_update.quantity = 150
                                        else:
                                            pass
                                        db.session.commit()
                                        #print text saying task completed
                                        print_quickly("-----------------------------------------------------------------------------------------------------")
                                        console.print(f"Your attempt to {task_to_do.name} was successful. You have replenished your {task_to_do.resource.name} supply by {task_to_do.reward}%", style="green")
                                        #delete task row
                                        db.session.delete(task_to_do)
                                        db.session.commit()                 
                                        #return to main menu
                                        decrease_resource(difficulty)
                                        powerup()
                                        random_event()
                                        task_menu(username, difficulty)
                                    else:
                                        print_quickly("-----------------------------------------------------------------------------------------------------")
                                        console.print(f"Your attempt to {task_to_do.name} has failed, please try again.", style="red")
                                        decrease_resource(difficulty)
                                        powerdown()
                                        random_event()
                                        task_menu(username, difficulty)
                                elif attempt_task.lower() == "back":
                                    random_event()
                                    task_menu(username, difficulty)
                                else:
                                    console.print("Invalid input, please try again.", style="red")
                                    execute_task(username, difficulty)
                            execute_task(username, difficulty)
                        else:
                            console.print("Invalid input, please try again.", style="red")
                            task_select(username, difficulty)
                    task_select(username, difficulty)    
                load_tasks(username, None, difficulty)
            else:
                you_win(username)
        else:
            you_died(username)


    def main_menu(username, difficulty):
        print("""\
                  
                      .    _     *       \|/   .       .      -*-              +
                        .' \\`.     +    -*-     *   .         '       .   *
                     .  |__''_|  .       /|\ +         .    +       .           |
                        |     | .                                        .     -*-
                        |     |           `  .    '             . *   .    +    '
                      _.'-----'-._     *                  .
                    /             \__.__.--._______________
            """)
        task_menu(username, difficulty)  


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
        intro_sound()
        username = input()
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print(f"Welcome to the UN Mars Base, Commander [bold magenta]{username}[/bold magenta]!")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print("This is a game of [bold]chance[/bold].", style="magenta")
        console.print("Your job is to ensure the continued operational status of the base's life support systems.")
        console.print("The base relies on four resources: [yellow bold]Air[/yellow bold], [green bold]Food[/green bold], [red bold]Fuel[/red bold] and [blue bold]Water[/blue bold].")
        console.print("These resources are consumed at a variable rate and will become depleted over time.")
        console.print("You must perform tasks to replenish these resources before they run out.")
        console.print("All tasks have a 50% probablility of success.")
        console.print("If you can fully replenish all of your resources, you win the game.")
        console.print("If any of the four resources are fully depleted, you lose.")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print(f"Good Luck Commander [bold]{username}[/bold]!", style="magenta", justify="center")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print(f"Would you like to begin the game?")
        console.print("Please enter [green]start[/green] to begin, or [red]exit[/red] to quit.", style="bold")
        console.print("For an extra challenge, enter [bold blue]hard[/bold blue] to begin the game in Hard Mode.", style="bold")
        def start():
            begin_res = input()
            if begin_res.lower() == "start":
                difficulty = "easy"
                main_menu(username, difficulty)
            elif begin_res.lower() == "hard":
                difficulty = "hard"
                main_menu(username, difficulty)
            elif begin_res.lower() == "exit":
                goodbye(username) 
            else:
                console.print("Invalid input, please try again.", style="red")
                start()
        start()
      
    welcome()

