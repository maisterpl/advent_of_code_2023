

def open_file(file_path: str):
    with open(file=file_path, mode="r") as f:
        data = f.read().split('\n')
    return data

def return_a_list_of_games(data: list):
    list_of_games = [ [ [ c.split(' ') for c in sset.split(', ') ] for sset in game.split(': ')[1].split('; ')]  for game in data ]
    return list_of_games

def IDs_games(games: list, red_c: int = 0, green_c: int = 0, blue_c: int = 0):
    list_of_the_IDs_games: list = [ id+1 for id, _ in enumerate(games) ]
    for id, game in enumerate(games):
        for sset in game:
            for pos in sset:
                temp_red_c = 0
                temp_green_c = 0
                temp_blue_c = 0
                if pos[1] == 'red' and int(pos[0]) > red_c:
                    if (id + 1) in list_of_the_IDs_games:
                        list_of_the_IDs_games.remove(id + 1)
                    
                elif pos[1] == 'green' and int(pos[0]) > green_c:
                    if (id + 1) in list_of_the_IDs_games:
                        list_of_the_IDs_games.remove(id + 1)
                    
                elif pos[1] == 'blue' and int(pos[0]) > blue_c:
                    if (id + 1) in list_of_the_IDs_games:
                        list_of_the_IDs_games.remove(id + 1)
                    
                
    return list_of_the_IDs_games
                    


### TEST PART 1 ###
print('='* 50)
print('### TEST PART 1 ###')
test_part_1 = open_file(file_path='advent_of_code_2023\day_2\input_test_part_1.txt')
list_of_game_test_1 = return_a_list_of_games(test_part_1)
print(list_of_game_test_1)
list_of_ids_games = IDs_games(list_of_game_test_1, 12, 13, 14)
print(list_of_ids_games)
print(sum(list_of_ids_games))

### ANS PART 1 ###
print('='* 50)
print('### ANS PART 1 ###')
data_part_1 = open_file('advent_of_code_2023\day_2\input_part_1.txt')
list_of_games_part_1= return_a_list_of_games(data_part_1)

list_of_ids_games_part_1 = IDs_games(list_of_games_part_1, 12, 13, 14)
# print(list_of_ids_games_part_1)
print(f'Answer part 1: {sum(list_of_ids_games_part_1)}.')


### TEST PART 2 ###


