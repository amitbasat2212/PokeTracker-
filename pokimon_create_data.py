import json
import pymysql 
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

pokimon_data_json = open('PokeTracker-\pokimon.json')
pokimon_data_fetures = json.load(pokimon_data_json);


# sql_pokimon = "DELETE FROM pokemon"
# mycursor = connection.cursor()
# mycursor.execute(sql_pokimon)
# connection.commit()

# sql_trainer = "DELETE FROM trainer"
# mycursor.execute(sql_trainer)
# connection.commit()

def create_pokimon(id,name,type,height,weight):
    try:
        with connection.cursor() as cursor:
            insert_pokimon = f"INSERT INTO pokemon values({id},'{name}','{type}',{height},{weight})"
            cursor.execute(insert_pokimon)
            connection.commit()
    except TypeError as e:
        print(e)





def create_trainer(name,town):
    try:
        with connection.cursor() as cursor:
            insert_trainer = f"INSERT IGNORE INTO trainer(name_trainer,town) values('{name}','{town}')"            
            cursor.execute(insert_trainer)
            connection.commit()
    except TypeError as e:
        print(e)

def create_trainer_pokimon(name_trainer,id_pokimon):
    try:
        with connection.cursor() as cursor:
            insert_trainer = f"INSERT IGNORE INTO trainer_pokemon values('{name_trainer}',{id_pokimon})"            
            cursor.execute(insert_trainer)
            connection.commit()
    except TypeError as e:
        print(e)


def create_all_the_data_about_pokimons():
    for pokimon in pokimon_data_fetures:
                create_pokimon(pokimon["id"],
                pokimon["name"],
                pokimon["type"],
                pokimon["height"],
                pokimon["weight"])
                for trainer in pokimon["ownedBy"]:                    
                    create_trainer(trainer["name"],trainer["town"])
                    create_trainer_pokimon(trainer["name"],pokimon["id"])


   
   
    

create_all_the_data_about_pokimons()

    
