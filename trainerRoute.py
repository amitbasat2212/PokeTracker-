
from fastapi import FastAPI,APIRouter
import pokimon_queiries as pq;
import pokimon_create_data as pc
import json;

router = APIRouter()

#trainers
@router.get('/trainers/', status_code=200)
async def get_trainers_of_pokimon(pokimon_name):
    try:
        return json.dumps(pq.find_trainers_of_pokimon(pokimon_name));
    except TypeError as e:
        return e;

@router.post('/trainers/', status_code=201)
async def add_trainer(name,town):
    try:
        pc.create_trainer(name,town);
        new_trainer = json.dumps({"name":name,"town":town})
        return new_trainer
    except TypeError as e:
        return e;


@router.delete('/trainers/{trainer_name}/pokimons/{pokimon_id}', status_code=200)
async def get_pokimon_from_trainer(trainer_name,pokimon_id):
    try:
        pq.delete_pokimon_from_trainer(trainer_name,pokimon_id)
        delete_trainer = json.dumps({"trainer_name":trainer_name,"pokimon_id":pokimon_id})
        return json.dumps(delete_trainer);
    except TypeError as e:
        return e;   



