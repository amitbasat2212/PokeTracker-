import pymysql 
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poketracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def find_the_haviest_pokimon():
    try:
        with connection.cursor() as cursor:
            query_haviest_pokimon = f"SELECT * FROM pokemon WHERE weight = ( SELECT MAX(weight) FROM pokemon );"
            cursor.execute(query_haviest_pokimon)        
            result = cursor.fetchall()
            return result;
    except TypeError as e:
        print(e)

def findByType(type):
    try:
        with connection.cursor() as cursor:
            # query_haviest_pokimon = f"SELECT * FROM pokemon WHERE "
            # cursor.execute(query_haviest_pokimon)        
            # result = cursor.fetchall()
            # return result;
            pass
    except TypeError as e:
        print(e)


# print(find_the_haviest_pokimon());  

def find_trainers_of_pokimon(pokimon_name):
    try:
        with connection.cursor() as cursor:            
            query_trainer_names = f"SELECT tp.trainer_name FROM pokemon as po,trainer_pokemon as tp WHERE po.id=tp.pokemon_id AND po.name_pokemon='{pokimon_name}' ;"
            cursor.execute(query_trainer_names)        
            result_trainer_names = cursor.fetchall()                                  
            list_of_trainer_names=[];            
            
            for trainer in result_trainer_names:
                 list_of_trainer_names.append(trainer["trainer_name"])               
           
            return list_of_trainer_names;
   
    except TypeError as e:
        print(e)


# print(find_trainers_of_pokimon("gengar"));


# def findRoster(name_trainer):
#     try:
#         with connection.cursor() as cursor:            
#             query_trainer_names = f"SELECT tp.trainer_name FROM pokemon as po,trainer_pokemon as tp WHERE po.id=tp.pokemon_id AND po.name_pokemon='{pokimon_name}' ;"
#             cursor.execute(query_trainer_names)        
#             result_trainer_names = cursor.fetchall()                                  
#             list_of_trainer_names=[];            
            
#             for trainer in result_trainer_names:
#                  list_of_trainer_names.append(trainer["trainer_name"])               
           
#             return list_of_trainer_names;
   
#     except TypeError as e:
#         print(e)

   
#     except TypeError as e:
#         print(e)