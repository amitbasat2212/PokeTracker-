
import requests;
session = requests.Session()
API_EVOLVE = "http://localhost:8080/evolve/"

data_pokimon_evolev = "pinsir"
data_trainer_evolve = "Whitney"


def evole():
    payload = {'pokimon_name': data_pokimon_evolev,"trainer_name":data_trainer_evolve}
    response_json = session.post(API_EVOLVE,params=payload)
    return response_json;
       
    

def test_evole_pokimon_wrong_pok():  
    pokimon_wrong_evolve = evole()
    
    assert pokimon_wrong_evolve.status_code==400;
    assert pokimon_wrong_evolve.json()=={
        "message":f"there is no more evolotion"
    }

def test_evolve_not_excit_pokimon():
    pass;    