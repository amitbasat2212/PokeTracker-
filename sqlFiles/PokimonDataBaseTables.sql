use poketracker;

-- DROP TABLE typepokemon_pokemon,trainer_pokemon,pokemon,trainer,typepokemon


CREATE TABLE Trainer(
    name_trainer VARCHAR(20) NOT NULL PRIMARY KEY,
    town VARCHAR(50)    
);

CREATE TABLE Pokemon(
    id INT NOT NULL PRIMARY KEY,
    name_pokemon VARCHAR(50),    
    height INT,
    weight INT
);


CREATE TABLE TypePokemon( 
    name_type VARCHAR(50) NOT NULL PRIMARY KEY
    
);



CREATE TABLE Trainer_Pokemon(
    trainer_name VARCHAR(20),
    pokemon_id  INT,
    FOREIGN KEY (trainer_name) REFERENCES Trainer(name_trainer),
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
    PRIMARY KEY (trainer_name, pokemon_id)
);

CREATE TABLE TypePokemon_Pokemon(    
    type_name VARCHAR(50),
    pokemon_id  INT,
    FOREIGN KEY (type_name) REFERENCES TypePokemon(name_type),
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(id),
    PRIMARY KEY (type_name, pokemon_id)
    
);


