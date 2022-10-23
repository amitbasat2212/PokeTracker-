

import requests;


API_ENDPOINT_POKIMONS = "http://localhost:8080/pokimons/"

API_ENDPOINT_POKIMONS_TYPE = "http://localhost:8080/pokimons/type/"



data_to_test = ["wartortle", "caterpie", "beedrill", "arbok",
 "clefairy", "wigglytuff", "persian", 
 "growlithe", "machamp", "golem", "dodrio", 
 "hypno", "cubone", "eevee", "kabutops"]


data_by_type = "eevee"

data_type = "normal"

data_name_to_test ="Drasna" 


def test_get_pokimons_by_trainer():
    session = requests.Session()
    payload = {'trainer_name': data_name_to_test}
    response_json = session.get(API_ENDPOINT_POKIMONS, params=payload)
    pokimons_of_trainer = response_json.json();
    assert response_json.status_code==200;
    assert pokimons_of_trainer==data_to_test   

def test_get_pokimons_by_trainer_wrong_name():
    session = requests.Session()
    payload = {'trainer_name': 1}
    response_json = session.get(API_ENDPOINT_POKIMONS, params=payload)   
    pokimons_of_trainer = response_json.json();     
    assert response_json.status_code==400;
    assert pokimons_of_trainer=={
    "message": "the trainer_name incorrect"
}


def test_get_pokimon_by_type():
    session = requests.Session()
    payload = {'type': data_type}
    response_json = session.get(API_ENDPOINT_POKIMONS_TYPE, params=payload)
    pokimons_by_type = response_json.json();  
    assert response_json.status_code==200;  
    assert data_by_type in pokimons_by_type ;


def test_get_pokimon_by_wrong_type():
    session = requests.Session()
    payload = {'type': 1}
    response_json = session.get(API_ENDPOINT_POKIMONS_TYPE, params=payload)
    pokimons_by_type = response_json.json();   
    assert response_json.status_code==400;
    assert pokimons_by_type=={
        "message":f"the type incorrect"
    }





