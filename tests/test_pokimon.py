

import requests;


data_to_test = ["wartortle", "caterpie", "beedrill", "arbok",
 "clefairy", "wigglytuff", "persian", 
 "growlithe", "machamp", "golem", "dodrio", 
 "hypno", "cubone", "eevee", "kabutops"]


data_name_to_test ="Drasna" 
def test_get_pokimons_by_trainer():
    response_json= requests.get(f'http://localhost:8080/pokimons/?trainer_name={data_name_to_test}')    
    pokimons_of_trainer = response_json.json();   
    assert pokimons_of_trainer ==data_to_test;

