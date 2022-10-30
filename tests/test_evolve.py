
import requests;
session = requests.Session()
API_EVOLVE = "http://localhost:8080/evolve/"
API_ENDPOINT_POKIMON = "http://localhost:8080/pokimons/"

data_pokimon_evolev = "pinsir"
data_trainer_evolve = "Archie"




def evole(data_pokimon,data_trainer):
    payload = {'pokimon_name': data_pokimon,"trainer_name":data_trainer}
    response_json = session.post(API_EVOLVE,params=payload)
    return response_json;
       
    

def test_evole_pokimon_wrong_pok():  
    pokimon_wrong_evolve = evole(data_pokimon_evolev,data_trainer_evolve)    
    assert pokimon_wrong_evolve.status_code==400;
    assert pokimon_wrong_evolve.json()=={
        "message":f"there is no more evolotion"
    }

def test_evolve_not_excit_pokimon():
     data_pokimon_evolev="spearow"
     data_trainer_evolve="Archie"
     pokimon_wrong_evolve = evole(data_pokimon_evolev,data_trainer_evolve)     
     assert pokimon_wrong_evolve.status_code==400;
     assert pokimon_wrong_evolve.json()=={
        "message":f"the trainer does not have this pokimon"
    }   


def test_evolve_pokimon():
     data_pokimon_evolev="oddish"
     data_trainer_evolve="Whitney"
     pokimon_wrong_evolve = evole(data_pokimon_evolev,data_trainer_evolve)     
     assert pokimon_wrong_evolve.status_code==200;
     assert pokimon_wrong_evolve.json()["trainer_name"]==data_trainer_evolve;
     assert pokimon_wrong_evolve.json()["pokimon_name"]=="gloom";
        
def test_evolve_wrong():
     data_pokimon_evolev="oddish"
     data_trainer_evolve="Whitney"
     pokimon_wrong_evolve = evole(data_pokimon_evolev,data_trainer_evolve)     
     assert pokimon_wrong_evolve.status_code==400;
     assert pokimon_wrong_evolve.json()=={
        "message":f"the trainer does not have this pokimon"
     }   


def get_all_pokimons():
    data_trainer_evolve="Whitney"
    payload = {'trainer_name': data_trainer_evolve}
    response_json = session.get(API_ENDPOINT_POKIMON, params=payload)
    pokimons_of_trainer = response_json.json();
    assert response_json.status_code==200
    assert "gloom" in pokimons_of_trainer