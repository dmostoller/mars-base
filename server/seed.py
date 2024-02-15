from config import app
import random
from models import *

if __name__ == "__main__":
    with app.app_context():
        
        print("Clearing tables....")

        Resource.query.delete()
        Task.query.delete()

        print("Loading available resources......")


        air = Resource(name = "Air", quantity = 50)
        food = Resource(name = "Food", quantity = 50)
        fuel = Resource(name = "Fuel", quantity = 50)        
        water = Resource(name = "Water", quantity = 50)

        db.session.add(air)
        db.session.add(food)
        db.session.add(fuel)
        db.session.add(water)
        db.session.commit()      

        print("Loading active tasks.......")
 
        tasks = []

        tasks.append(Task(
            name = "Change Air Filters", 
            description = "clean and replace the life support system air filters", 
            reward = random.randint(10,40),
            resource_id = air.id 
        ))
        tasks.append(Task(
            name = "Plant Seeds", 
            description = "plant new seeds in the soil of the hydroponic farm", 
            reward = random.randint(10,40),
            resource_id = food.id 
        ))
        tasks.append(Task(
            name = "Mine Ore", 
            description = "mine for ore that you can refined into fuel", 
            reward = random.randint(10,40),
            resource_id = fuel.id 
        ))
        tasks.append(Task(
            name = "Repair Valve", 
            description = "repair leaky valve on the main water pipe", 
            reward = random.randint(10,40),
            resource_id = water.id 
        ))
        tasks.append(Task(
            name = "Repair Air Conditioning", 
            description = "repair the main condensor on the air conditioning unit", 
            reward = random.randint(10,40),
            resource_id = air.id 
        ))
        tasks.append(Task(
            name = "Fertilize Soil", 
            description = "add fertilizer to the soil in the hydroponic farm", 
            reward = random.randint(10,40),
            resource_id = food.id 
        ))
        tasks.append(Task(
            name = "Refine Ore", 
            description = "refine the mined ore into its component elements", 
            reward = random.randint(10,40),
            resource_id = fuel.id 
        ))
        tasks.append(Task(
            name = "Clean Algae Vats", 
            description = "clean the algae vats that filter the water supply", 
            reward = random.randint(10,40),
            resource_id = water.id 
        ))
        
        db.session.add_all(tasks)
        db.session.commit()