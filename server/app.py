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

    def main_menu():
          print("""\
                  .    _     *       \|/   .       .      -*-              +
                    .' \\`.     +    -*-     *   .         '       .   *
                .  |__''_|  .       /|\ +         .    +       .           |
                    |     | .                                        .     -*-
                    |     |           `  .    '             . *   .    +    '
                  _.'-----'-._     *                  .
                /             \__.__.--._______________
                """)
          
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

          print_quickly("-----------------------------------------------------------------------------------------------------")
          console.print("TASKS", style="bold magenta", justify="center")
          table2 = Table(show_header=False, header_style="bold", border_style="none")
          table2.add_column("", justify="center")
          table2.add_column("Name", justify="left")
          table2.add_column("Description", justify="left")
          table2.add_column("Reward", justify="center")
          table2.add_column("Resource",  justify="left")


          tasks = Task.query.all()
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
          console.print("Please enter a number to select a task:")
          task_response = input()

          task = db.session.get(Task, {task_response})
          console.print(f"Would you like to [cyan italic]{task.name}[/cyan italic] and replenish your {task.resource.name} supply by {task.reward}%?")
          console.print("Input [cyan]yes[/cyan] to attempt task or [red]exit[/red] to select another task.")
          attempt_task = input()
          if attempt_task.lower() == "yes":  
              resource_to_update = db.session.get(Resource, {task.resource.id})            
              if descision():
                  #update resource table to increment resource quantity
                  resource_to_update.quantity += task.reward
                  if resource_to_update.quantity >= 100:
                      resource_to_update.quantity = 100
                  else:
                      pass
                  db.session.commit()
                  #print text saying task completed
                  console.print(f"Your attempt to {task.name} was successful. You have replenished your {task.resource.name} supply by {task.reward}%", style="green italic")
                  #delete task row
                  db.session.delete(task)
                  db.session.commit()                 
                  #return to main menu
                  main_menu()
              else:
                  console.print(f"Your attempt to {task.name} has failed, please try again", style="red italic")
                  main_menu()
          elif attempt_task.lower() == "exit":
              main_menu()


    
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
        print_slowly("Please enter your name to begin......")
        username = input()
        console.print(f"Welcome to the UN Mars Base, Ensign [cyan]{username}[/cyan]!")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print("Your job is to ensure the continued operational status of the base's life support systems.")
        console.print("The base relies on four resources: [yellow]Air[/yellow], [green]Food[/green], [red]Fuel[/red] and [blue]Water[/blue].")
        console.print("These resources are consumed at a steady rate and will become depleted over time.")
        console.print("You must perform tasks to maintain and replenish these resources before they run out.")
        print_quickly("-----------------------------------------------------------------------------------------------------")
        console.print(f"Would you like to begin the game, Ensign {username}?")
        console.print("Please enter 1 to begin, or 0 to exit.")
        begin_res = input()
        if begin_res == "1":
            main_menu()
        elif begin_res == "0":
            print(f"Goodbye Ensign {username}, have a safe return journey to Earth.")
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
        else:
           console.print("Invalid input, please try again.")

    
    welcome()

    

    



    # remove pass and write your cli logic


