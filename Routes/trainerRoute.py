
from fastapi import APIRouter
from requests import request
from Database import pokimon_queiries as pq;
from Database import pokimon_create_data as pc
from Routes import ErrorHandling
from fastapi import Request

router = APIRouter()

#trainers
@router.get('/trainers/', status_code=200)
async def get_trainers_of_pokimon(pokimon_name):
    try:
        return pq.find_trainers_of_pokimon(pokimon_name);
    except TypeError as e:
        return e;

@router.post('/trainers/', status_code=201)
async def add_trainer(request: Request):
    try:
        trainer =await request.json()
        if(trainer["name"].isnumeric() and trainer["town"].isnumeric()):
            return ErrorHandling.params_incorrect("name","town");

        pc.create_trainer(trainer["name"],trainer["town"]);
        new_trainer = {"name":trainer["name"],"town":trainer[""]}
        return new_trainer
    except TypeError as e:
        return e;


@router.delete('/trainers/{trainer_name}/pokimons/{pokimon_id}', status_code=200)
async def delete_pokimon_from_trainer(trainer_name,pokimon_id):
    try:
        if(trainer_name.isnumeric() and not pokimon_id.isnumeric()):
            return ErrorHandling.params_incorrect("trainer_name","pokimon_id");

        pq.delete_pokimon_from_trainer(trainer_name,pokimon_id)
        delete_trainer = {"trainer_name":trainer_name,"pokimon_id":pokimon_id}
        return delete_trainer;
    except TypeError as e:
        return e;   



