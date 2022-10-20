
from fastapi import FastAPI,APIRouter
import requests;

import pokimon_queiries as pq;
import pokimon_create_data as pc
import url_api_request
import json;
app = FastAPI()
router = APIRouter()

#pokimon
@router.get('/pokimons/', status_code=200)
async def get_pokemons_by_trainer(trainer_name):
    try:
        return json.dumps(pq.find_pokimons_of_trainer(trainer_name));
    except TypeError as e:
        return e;


@router.get('/pokimons/type/', status_code=200)
async def get_pokemons_by_type(type):
    try:
        return json.dumps(pq.find_by_type(type));
    except TypeError as e:
        return e;


@router.get('/pokimons/{pokimon_name}', status_code=200)
async def get_pokimon(pokimon_name):
    try:
       pokimon_details = requests.get(url_api_request.get_pokimon_details(pokimon_name))
       pokimon_details_json =pokimon_details.json()
       pokimon_type = pokimon_details_json["types"];
       pokimon_id = pq.find_id_pokimon_by_name(pokimon_name);
       
       for type in pokimon_type:
          pc.create_type_pokimon_to_pokimon(type["type"]["name"],pokimon_id)  
       
       pokimon_details = pq.find_pokimon_by_id(pokimon_id);
       return pokimon_details; 
         
    
    except TypeError as e:
        return e;
 