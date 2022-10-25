from Database.DataBaseManager import connection

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


def find_pokimon_to_trainer_by_id_and_name(trainer_name,id_pokimon):
    try:
        with connection.cursor() as cursor:            
            query_excist_pokimon_from_trainer = f"SELECT * from trainer_pokemon where trainer_name='{trainer_name}' AND pokemon_id={id_pokimon} ;"
            cursor.execute(query_excist_pokimon_from_trainer)            
            result_pokimon = cursor.fetchall()                                 
            if(len(result_pokimon)==0):
                return False;
            return True;
            
   
    except TypeError as e:
        return e;



def delete_pokimon_from_trainer(trainer_name,pokimon_id):
    try:
        with connection.cursor() as cursor: 
            if_row_excist = find_pokimon_to_trainer_by_id_and_name(trainer_name,pokimon_id)           
            if(if_row_excist):
                delete_pokimon_from_trainer = f"Delete from trainer_pokemon where trainer_name='{trainer_name}' AND pokemon_id={pokimon_id} ;"
                cursor.execute(delete_pokimon_from_trainer)
                connection.commit()
                return {"trainer_name":trainer_name,"pokimon_id":pokimon_id}
            
            return {}

   
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





def find_pokimon_types_by_id(pokimons):
    try:
            with connection.cursor() as cursor: 
                pokimons_type=[]
                for pokimon in pokimons:
                    pokimon_id = find_id_pokimon_by_name(pokimon)
                    pokimon_type_query = f"SELECT type_name FROM typepokemon_pokemon WHERE pokemon_id='{pokimon_id}'"
                    cursor.execute(pokimon_type_query)        
                    pokimon_types = cursor.fetchall()
                    for type in pokimon_types:
                        pokimons_type.append(type["type_name"])
                   
                return pokimons_type    
    except TypeError as e:
            return e;

def find_if_trainer_has_pokimon_with_same_type(trainer_name,pokimon_name):
    try:
            with connection.cursor() as cursor: 
                pokimon_id = find_id_pokimon_by_name(pokimon_name);
                pokimon_type_query = f"SELECT type_name FROM typepokemon_pokemon WHERE pokemon_id='{pokimon_id}'"
                cursor.execute(pokimon_type_query)        
                pokimon_type = cursor.fetchall()
                pokimons_of_trainer = find_pokimons_of_trainer(trainer_name);  
                pokimons_of_trainer_types = find_pokimon_types_by_id(pokimons_of_trainer);              

                for pokimon in pokimon_type:
                    if pokimon["type_name"] in pokimons_of_trainer_types:
                        return True;

                return False;    

                 
    except TypeError as e:
            return e;


