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





def findByType(types_pokimon):
    try:
        with connection.cursor() as cursor:            
            query_types_of_pokimon = f"SELECT po.name_pokemon FROM pokemon as po,typepokemon_pokemon as ty WHERE ty.pokemon_id=po.id AND ty.type_name='{types_pokimon}';"
            cursor.execute(query_types_of_pokimon)        
            result_types_of_pokimon = cursor.fetchall()                                  
            list_of_pokimon_types=[];            
            
            for trainer in result_types_of_pokimon:
                 list_of_pokimon_types.append(trainer["trainer_name"])               
           
            return list_of_pokimon_types;
   
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




def findRoster(name_trainer):
    try:
        with connection.cursor() as cursor:            
            query_pokimon_names = f"SELECT po.name_pokemon FROM pokemon as po,trainer_pokemon as tp WHERE po.id=tp.pokemon_id AND tp.trainer_name='{name_trainer}' ;"
            cursor.execute(query_pokimon_names)        
            result_pokimon_names = cursor.fetchall()          
                       
            list_of_pokimon_names=[];            
            
            for trainer in result_pokimon_names:
                 list_of_pokimon_names.append(trainer["name_pokemon"])               
           
            return list_of_pokimon_names;
   
    except TypeError as e:
        print(e)

   

print(findByType("grass"))