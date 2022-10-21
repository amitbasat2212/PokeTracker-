
from fastapi import APIRouter
from Database import pokimon_queiries as pq;
from Database import pokimon_create_data as pc
from Routes import ErrorHandling


router = APIRouter()

#trainers
@router.get('/trainers/', status_code=200)
async def get_trainers_of_pokimon(pokimon_name):
    try:
        return pq.find_trainers_of_pokimon(pokimon_name);
    except TypeError as e:
        return e;

@router.post('/trainers/', status_code=201)
async def add_trainer(name,town):
    try:
        if(name.isnumeric() and town.isnumeric()):
            return ErrorHandling.params_incorrect("name","town");

        pc.create_trainer(name,town);
        new_trainer = {"name":name,"town":town}
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



