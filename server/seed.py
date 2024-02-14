from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
      
      print("Clearing tables....")

      Resource.query.delete()
      Task.query.delete()

      print("Loading available resources......")


      air = Resource(name = "Air", quantity = 90)
      food = Resource(name = "Food", quantity = 90)
      fuel = Resource(name = "Fuel", quantity = 90)        
      water = Resource(name = "Water", quantity = 90)

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
          reward = 10,
          resource_id = air.id 
          ))
      tasks.append(Task(
          name = "Plant Seeds", 
          description = "plant new seeds in the soil of the hydroponic farm", 
          reward = 10,
          resource_id = food.id 
          ))
      tasks.append(Task(
          name = "Mine Ore", 
          description = "mine for ore that you can refined into fuel", 
          reward = 10,
          resource_id = fuel.id 
          ))
      tasks.append(Task(
          name = "Repair Valve", 
          description = "repair leaky valve on the main water pipe", 
          reward = 10,
          resource_id = water.id 
          ))
      tasks.append(Task(
          name = "Change Air Filters", 
          description = "clean and replace the life support system air filters", 
          reward = 20,
          resource_id = air.id 
          ))
      tasks.append(Task(
          name = "Plant Seeds", 
          description = "plant new seeds in the soil of the hydroponic farm", 
          reward = 20,
          resource_id = food.id 
          ))
      tasks.append(Task(
          name = "Mine Ore", 
          description = "mine for ore that you can refined into fuel", 
          reward = 20,
          resource_id = fuel.id 
          ))
      tasks.append(Task(
          name = "Repair Valve", 
          description = "repair leaky valve on the main water pipe", 
          reward = 20,
          resource_id = water.id 
          ))
      
      db.session.add_all(tasks)
      db.session.commit()