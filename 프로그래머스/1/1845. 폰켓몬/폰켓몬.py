def solution(pokemons):
    
    pokemons_list=list(set(pokemons))
    if len(pokemons_list)>len(pokemons)/2:
        return len(pokemons)/2
    return len(pokemons_list)