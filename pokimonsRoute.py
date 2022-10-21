
from fastapi import FastAPI,APIRouter
import requests;
import pokimon_queiries as pq;
import pokimon_create_data as pc
import url_api_request

app = FastAPI()
router = APIRouter()

#pokimon
@router.get('/pokimons/', status_code=200)
async def get_pokemons_by_trainer(trainer_name):
    try:
        return pq.find_pokimons_of_trainer(trainer_name);
    except TypeError as e:
        return e;


@router.get('/pokimons/type/', status_code=200)
async def get_pokemons_by_type(type):
    try:
        return pq.find_by_type(type);
    except TypeError as e:
        return e;


def request_from_pokeApi_for_pokimon_detailes(pokimon_name,url,callback):
    pokimon_details = requests.get(callback(pokimon_name,url))
    pokimon_details_json =pokimon_details.json()
    return pokimon_details_json

def request_from_pokeApi_for_evolotion(url,callback):
    pokimon_details = requests.get(callback(url))
    pokimon_details_json =pokimon_details.json()
    return pokimon_details_json



def create_types_for_pokimon(pokimon_type,pokimon_id):
    for type in pokimon_type:
          pc.create_type_pokimon_to_pokimon(type["type"]["name"],pokimon_id)  
       



@router.get('/pokimons/{pokimon_name}', status_code=200)
async def get_pokimon(pokimon_name):
    try:
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

@router.get('/evolve', status_code=200)
async def evolve_pokimon(pokimon_name):
    try:
        pokimon_detailes = request_pokimon_detailes(pokimon_name)   
        
        pokimon_evolution_chain_url = request_pokimon_evolotion_url(pokimon_detailes)
                        
        pokimon_evoulotion = request_evolotion_detailes(pokimon_evolution_chain_url)
         
        return pokimon_evoulotion["chain"]["evolves_to"]

    except TypeError as e:
        return e;




