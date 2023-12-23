

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

#         one game:
# [
#  [['3', 'blue'], ['4', 'red']], -> set
#  [['1', 'red'], ['2', 'green'], ['6', 'blue']], 
#  [['2', 'green']]
# ]
def power_of_set(data: list):
    power_of_set: int = 0
    num_of_cubes_of_each_color_dict: dict = {
            'red': [],
            'green': [],
            'blue': [],
        }  # key='blue' : value [3, 6, ...]
    for set in data:
        for cube in set:
            num_of_cubes_of_each_color_dict[ cube[1] ].append( int(cube[0]) ) 

    red_min = max(num_of_cubes_of_each_color_dict['red'])
    green_min = max(num_of_cubes_of_each_color_dict['green'])
    blue_min = max(num_of_cubes_of_each_color_dict['blue'])
    
    power_of_set = red_min * green_min * blue_min
    
    return power_of_set

def ans_part_2(list_of_game: list):
    sum_of_all_games: int = 0
    for game in list_of_game:
        sum_of_all_games += power_of_set(data= game)
        
    return sum_of_all_games
    
    
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
print('\n' + '='* 50)
print('### TEST PART 2 ###')
test_def_power_of_set = power_of_set(data= [[['3', 'blue'], ['4', 'red']], [['1', 'red'], ['2', 'green'], ['6', 'blue']], [['2', 'green']]] )
print(test_def_power_of_set)
print('### TEST PART 2 VOL 1.2 ###')

sum_of_all_games = ans_part_2(list_of_game_test_1)
print(sum_of_all_games)
    
### ANS PART 2 ###
print('='* 50)
print('### ANS PART 2 ###')
sum_of_all_games_part_2 = ans_part_2(list_of_game= list_of_games_part_1)
print(sum_of_all_games_part_2)
