import json
from Database.DataBaseManager import connection

# pokimon_data_json = open('pokimon.json')
# pokimon_data_fetures = json.load(pokimon_data_json);


# mycursor = connection.cursor()

# sql_trainer = "DELETE FROM trainer_pokemon"
# mycursor.execute(sql_trainer)
# connection.commit()

# sql_trainer = "DELETE FROM typepokemon"
# mycursor.execute(sql_trainer)
# connection.commit()

# sql_trainer = "DELETE FROM typepokemon_pokemon"
# mycursor.execute(sql_trainer)
# connection.commit()


# sql_pokimon = "DELETE FROM pokemon"
# mycursor.execute(sql_pokimon)
# connection.commit()

# sql_trainer = "DELETE FROM trainer"
# mycursor.execute(sql_trainer)
# connection.commit()

def create_pokimon(id,name,height,weight):
    try:
        with connection.cursor() as cursor:
            insert_pokimon = f"INSERT IGNORE INTO pokemon values({id},'{name}',{height},{weight})"
            cursor.execute(insert_pokimon)
            connection.commit()
            return {"id":id,"name":name,"height":height,"weight":weight}
    except TypeError as e:
        print(e)


def create_type(types_pokimon):
    try:
        with connection.cursor() as cursor:           
                insert_type_pokimon = f"INSERT IGNORE INTO typepokemon values('{types_pokimon}')"
                cursor.execute(insert_type_pokimon)
                connection.commit()
           
    except TypeError as e:
        print(e)


def create_type_pokimon_to_pokimon(types_pokimon,id_pokimon):
    try:
        with connection.cursor() as cursor:       
           create_type(types_pokimon)     
           insert_type_pokimon = f"INSERT IGNORE INTO typepokemon_pokemon values('{types_pokimon}',{id_pokimon})"
           cursor.execute(insert_type_pokimon)
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


# def create_all_the_data_about_pokimons():
#     for pokimon in pokimon_data_fetures:
#                 create_pokimon(pokimon["id"],
#                 pokimon["name"],                
#                 pokimon["height"],
#                 pokimon["weight"])
                
#                 create_type(pokimon["type"])
#                 create_type_pokimon_to_pokimon(pokimon["type"],pokimon["id"])
#                 for trainer in pokimon["ownedBy"]:                    
#                     create_trainer(trainer["name"],trainer["town"])
#                     create_trainer_pokimon(trainer["name"],pokimon["id"])
                   


# create_all_the_data_about_pokimons()

    
