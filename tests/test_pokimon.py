import requests;


API_ENDPOINT_POKIMONS = "http://localhost:8080/pokimons/"

API_ENDPOINT_POKIMONS_TYPE = "http://localhost:8080/pokimons/type/"



data_to_test = ["wartortle", "caterpie", "beedrill", "arbok",
 "clefairy", "wigglytuff", "persian", 
 "growlithe", "machamp", "golem", "dodrio", 
 "hypno", "cubone", "eevee", "kabutops"]


data_by_type = "eevee"

data_type = "normal"
data_to_add_pok_name = "yanma"

data_name_to_test ="Drasna" 

session = requests.Session()

def test_get_pokimons_by_trainer():
    
    payload = {'trainer_name': data_name_to_test}
    response_json = session.get(API_ENDPOINT_POKIMONS, params=payload)
    pokimons_of_trainer = response_json.json();
    assert response_json.status_code==200;
    assert pokimons_of_trainer==data_to_test   

def test_get_pokimons_by_trainer_wrong_name():
   
    payload = {'trainer_name': 1}
    response_json = session.get(API_ENDPOINT_POKIMONS, params=payload)   
    pokimons_of_trainer = response_json.json();     
    assert response_json.status_code==400;
    assert pokimons_of_trainer=={
    "message": "the trainer_name incorrect"
}



def get_pokimon_by_type(data):
    
    payload = {'type': data}
    response_json = session.get(API_ENDPOINT_POKIMONS_TYPE, params=payload)
    pokimons_by_type = response_json 
    return pokimons_by_type

def test_get_pokimon_by_type():   
    pokimons_by_type = get_pokimon_by_type(data_type)
    assert pokimons_by_type.status_code==200;  
    assert data_by_type in pokimons_by_type.json() ;


def test_get_pokimon_by_wrong_type():
    pokimons_by_type = get_pokimon_by_type(1)   
    assert pokimons_by_type.status_code==400;
    assert pokimons_by_type.json()=={
        "message":f"the type incorrect"
    }



def get_pokimons_by_type_test(data,data_to_check):
    pokimons_by_type = get_pokimon_by_type(data)
    assert pokimons_by_type.status_code==200;  
    assert data_to_check in pokimons_by_type.json() ;    

def test_add_pokimon():   
    payload = {'pokimon_name': data_to_add_pok_name}
    response_json = session.post(API_ENDPOINT_POKIMONS, params=payload)   
    assert response_json.status_code==200;
    get_pokimons_by_type_test("bug",data_to_add_pok_name)
    get_pokimons_by_type_test("flying",data_to_add_pok_name)
   
    