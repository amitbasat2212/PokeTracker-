
from fastapi import FastAPI,APIRouter
import pokimon_queiries as pq;
import pokimon_create_data as pc
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
        #return json.dumps(pq.find_pokimons_of_trainer(trainer_name));
        pass
    except TypeError as e:
        return e;
 