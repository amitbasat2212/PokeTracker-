from DataBaseManager import connection

def find_the_haviest_pokimon():
    try:
        with connection.cursor() as cursor:
            query_haviest_pokimon = f"SELECT * FROM pokemon WHERE weight = ( SELECT MAX(weight) FROM pokemon );"
            cursor.execute(query_haviest_pokimon)        
            result = cursor.fetchall()
            return result;
    except TypeError as e:
        return e;


def find_pokimon_by_id(pokimon_id):
    try:
        with connection.cursor() as cursor:
            query_haviest_pokimon = f"SELECT * FROM pokemon WHERE id={pokimon_id} ;"
            cursor.execute(query_haviest_pokimon)        
            result = cursor.fetchall()
            return result;
    except TypeError as e:
        return e;




def find_by_type(types_pokimon):
    try:
        with connection.cursor() as cursor:            
            query_pokimon_by_types = f"SELECT po.name_pokemon FROM pokemon as po,typepokemon_pokemon as ty WHERE ty.pokemon_id=po.id AND ty.type_name='{types_pokimon}';"
            cursor.execute(query_pokimon_by_types)        
            result_pokimon_by_type = cursor.fetchall()                                  
            list_of_pokimon_types=adding_items_to_list_by_param(result_pokimon_by_type,"name_pokemon");            
            return list_of_pokimon_types;
   
    except TypeError as e:
        return e;
        

def adding_items_to_list_by_param(result,param):
    list_of_item_to_return=[];          
    for item in result:
        list_of_item_to_return.append(item[param])               
    return list_of_item_to_return;       


def find_trainers_of_pokimon(pokimon_name):
    try:
        with connection.cursor() as cursor:            
            query_trainer_names = f"SELECT tp.trainer_name FROM pokemon as po,trainer_pokemon as tp WHERE po.id=tp.pokemon_id AND po.name_pokemon='{pokimon_name}' ;"
            cursor.execute(query_trainer_names)        
            result_trainer_names = cursor.fetchall()                                  
            list_of_trainer_names=adding_items_to_list_by_param(result_trainer_names,"trainer_name");         
            return list_of_trainer_names;
   
    except TypeError as e:
        return e;




def find_pokimons_of_trainer(name_trainer):
    try:
        with connection.cursor() as cursor:            
            query_pokimon_names = f"SELECT po.name_pokemon FROM pokemon as po,trainer_pokemon as tp WHERE po.id=tp.pokemon_id AND tp.trainer_name='{name_trainer}' ;"
            cursor.execute(query_pokimon_names)        
            result_pokimon_names = cursor.fetchall()                          
            list_of_pokimon_names=adding_items_to_list_by_param(result_pokimon_names,"name_pokemon");            
            return list_of_pokimon_names;
   
    except TypeError as e:
        return e;




def delete_pokimon_from_trainer(trainer_name,pokimon_id):
    try:
        with connection.cursor() as cursor:            
            delete_pokimon_from_trainer = f"Delete from trainer_pokemon where trainer_name='{trainer_name}' AND pokemon_id={pokimon_id} ;"
            cursor.execute(delete_pokimon_from_trainer)
            connection.commit()
   
    except TypeError as e:
        return e;

def find_id_pokimon_by_name(pokimon_name):
        try:
            with connection.cursor() as cursor:            
                query_pokimon_names = f"SELECT id FROM pokemon WHERE name_pokemon='{pokimon_name}';"
                cursor.execute(query_pokimon_names)        
                result_pokimon_id = cursor.fetchall() 
                return result_pokimon_id[0]["id"];         
        except TypeError as e:
            return e;

                       
