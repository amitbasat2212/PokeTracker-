use poketracker;



--DROP TABLE typePokemon_pokemon,trainer_pokemon,trainer,pokemon,typepokemon;
CREATE TABLE Trainer(
    name_trainer VARCHAR(20) NOT NULL PRIMARY KEY,
    town VARCHAR(50)    
);

CREATE TABLE Pokemon(
    id INT NOT NULL PRIMARY KEY,
    name_pokemon VARCHAR(50),   
    type VARCHAR(20),
    height INT,
    weight INT
);


CREATE TABLE TypePokemon( 
    id_type INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_type VARCHAR(50),
    url VARCHAR(200)
    
);



CREATE TABLE Trainer_Pokemon(
    trainer_name VARCHAR(20),
    pokemon_id  INT,
    FOREIGN KEY (trainer_name) REFERENCES Trainer(name_trainer),
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
    PRIMARY KEY (trainer_name, pokemon_id)
);

CREATE TABLE TypePokemon_Pokemon(    
    type_id INT,
    pokemon_id  INT,
    FOREIGN KEY (type_id) REFERENCES TypePokemon(id_type),
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
    PRIMARY KEY (type_id, pokemon_id)
    
);


