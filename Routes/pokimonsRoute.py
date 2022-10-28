

from fastapi import APIRouter
import requests;
from Database import pokimon_queiries as pq;
from Database import pokimon_create_data as pc
from consts import url_api_request
from Routes import ErrorHandling


router = APIRouter()

#pokimon
@router.get('/pokimons/', status_code=200)
async def get_pokemons_by_trainer(trainer_name):
    try:
        if(trainer_name.isnumeric()):
            return ErrorHandling.the_param_incorrect("trainer_name");

        return pq.find_pokimons_of_trainer(trainer_name);
    except TypeError as e:
        return e;


@router.get('/pokimons/type/', status_code=200)
async def get_pokemons_by_type(type):
    try:
        if(type.isnumeric()):
            return ErrorHandling.the_param_incorrect("type");

        return pq.find_by_type(type);
    except TypeError as e:
        return e;




def request_from_pokeApi_for_pokimon_detailes(pokimon_name,url,callback):
    pokimon_details = requests.get(callback(pokimon_name,url))   
    if(pokimon_details.status_code!=200):
        return {}
    pokimon_details_json =pokimon_details.json()   
    return pokimon_details_json

def request_from_pokeApi_for_evolotion(url,callback):
    pokimon_details = requests.get(callback(url))
    pokimon_details_json =pokimon_details.json()
    return pokimon_details_json



def create_types_for_pokimon(pokimon_type,pokimon_id):
    for type in pokimon_type:
          pc.create_type_pokimon_to_pokimon(type["type"]["name"],pokimon_id)  

    return{"type_name":pokimon_type,"pokimon_id":pokimon_id}        



@router.get('/pokimons/{pokimon_name}', status_code=200)
async def get_pokimon(pokimon_name):
    try:
       if(pokimon_name.isnumeric()):
           return ErrorHandling.the_param_incorrect("pokimon_name");

       pokimon_details_json = request_pokimon_detailes(pokimon_name)

       pokimon_type = pokimon_details_json["types"];
       
       pokimon_id = pq.find_id_pokimon_by_name(pokimon_name);       
       create_types_for_pokimon(pokimon_type,pokimon_id)         
       pokimon_details = pq.find_pokimon_by_id(pokimon_id);
       return pokimon_details;          
    
    except TypeError as e:
        return e;





def request_pokimon_evolotion_url(pokimon_detailes):
     pokimon_spiecies = request_from_pokeApi_for_evolotion(pokimon_detailes["species"]["url"],
     url_api_request.get_detailes_acording_to_url_from_pockimon)
     pokimon_evolution_chain_url = pokimon_spiecies["evolution_chain"]["url"];
     return pokimon_evolution_chain_url


def request_pokimon_detailes(pokimon_name):
     pokimon_detailes = request_from_pokeApi_for_pokimon_detailes(pokimon_name,url_api_request.pokimon_details_url,url_api_request.get_detailes_acording_to_url); 
     return pokimon_detailes;

def request_evolotion_detailes(pokimon_evolution_chain_url):
    pokimon_evoulotion = request_from_pokeApi_for_evolotion(pokimon_evolution_chain_url,
        url_api_request.get_detailes_acording_to_url_from_pockimon);    
    return pokimon_evoulotion;     



def evolve_the_pokimon(pokimon_chain_evolotion,pokimon_name):
    chain = pokimon_chain_evolotion["chain"]
    evolotion_of_pokimon =chain
    the_evolve_name=0;
    for _ in range(2):            
        if(evolotion_of_pokimon["species"]["name"]==pokimon_name):
            if(evolotion_of_pokimon["evolves_to"]==[]):
                return the_evolve_name;
            
            the_evolve_species =evolotion_of_pokimon["evolves_to"][0]["species"]     
            the_evolve_name=the_evolve_species["name"]
        else:
            evolotion_of_pokimon=chain["evolves_to"][0]

    return the_evolve_name;


def delete_old_pokimon_after_evolve(pokimon_name,trainer_name):
    old_pokimon_id= pq.find_id_pokimon_by_name(pokimon_name);
    the_delete_row=pq.delete_pokimon_from_trainer(trainer_name,old_pokimon_id)
    return the_delete_row;


def add_new_pokimon_after_evolve(pokimon_name,trainer_name):    
    pokimon_evolve_id = pq.find_id_pokimon_by_name(pokimon_name);
    pc.create_trainer_pokimon(trainer_name,pokimon_evolve_id);
    return pokimon_evolve_id;



@router.post("/pokimons/")
def add_pokimon(pokimon_name):
    pokimon_detailes = request_pokimon_detailes(pokimon_name)        
    if pokimon_detailes=={}:
        return ErrorHandling.the_param_incorrect("pokimon_name")
        
    new_pokimon =pc.create_pokimon(pokimon_detailes["id"],pokimon_detailes["name"],pokimon_detailes["height"],pokimon_detailes["weight"])
    return new_pokimon     
        
        


@router.post('/evolve/', status_code=200)
async def evolve_pokimon(pokimon_name,trainer_name):
    try:

        pokimon_detailes = request_pokimon_detailes(pokimon_name)        
        if pokimon_detailes=={}:
            return ErrorHandling.the_param_incorrect("pokimon_name") 
        if(pq.find_if_trainer_has_pokimon_with_same_type(trainer_name,pokimon_name)):
            return ErrorHandling.the_same_type()
        pokimon_evolution_chain_url = request_pokimon_evolotion_url(pokimon_detailes)
                        
        pokimon_evoulotion = request_evolotion_detailes(pokimon_evolution_chain_url)
        the_evolve_name_of_pokimon = evolve_the_pokimon(pokimon_evoulotion,pokimon_name)

        if(the_evolve_name_of_pokimon!=0):          
            delete_row = delete_old_pokimon_after_evolve(pokimon_name,trainer_name)        
            if(delete_row!={}):
                pokimon_evolve_id=add_new_pokimon_after_evolve(the_evolve_name_of_pokimon,trainer_name)
            else:
                return ErrorHandling.the_row_dosent_excit();
        else:
             return ErrorHandling.the_evolve_finished();        

        return {"trainer_name":trainer_name,"pokimon_id":pokimon_evolve_id}
 
    except TypeError as e:
        return e;




