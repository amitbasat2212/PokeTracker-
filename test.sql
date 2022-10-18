use poketracker;

SELECT po.name_pokemon
FROM pokemon as po,typepokemon_pokemon as ty
WHERE ty.pokemon_id=po.id AND ty.type_name="grass";

