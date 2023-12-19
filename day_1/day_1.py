



def open_file(file: str):
    with open(file=file, mode='r') as f:
        return f.readlines()
    
def aoc_day_1_ans_1(input_data: list):
    temp = []
    data = [ [ l for l in line if l.isdigit()] for line in input_data ]
    for d in data:
        temp.append(int(d[0] + d[-1]))
        
    print(temp)
    
    return sum(temp)

def letters_to_digit(data: str):
    letters_to_digits_dictionary = {
        'one' : 1, 
        'two' : 2, 
        'three' : 3, 
        'four' : 4, 
        'five' : 5, 
        'six' : 6, 
        'seven' : 7, 
        'eight' : 8, 
        'nine' : 9,
    }
    temp: list = []
    
    for dig in data:
        if dig.isdigit():
            temp.insert(data.index(dig), dig)
            continue
        for let_dig in letters_to_digits_dictionary.keys():
            if let_dig in data:
                temp.insert(data.index(let_dig), str(letters_to_digits_dictionary[let_dig]))
                continue
            
    return temp


            
    
### test part 1 ###
data = open_file(r'D:\Python\#14_advent_of_code_2023\day_1\test_input.txt')
print(aoc_day_1_ans_1(data))

### ans part 1 ###
data_ans_1 = open_file(r'D:\Python\#14_advent_of_code_2023\day_1\input.txt')
print(aoc_day_1_ans_1(data_ans_1))

### test part 2 ###
temp = letters_to_digit('26fmrrhhpthree6b')
print(temp)

# data = open_file(r'D:\Python\#14_advent_of_code_2023\day_1\test_input_part_2.txt')

# temp: list = []
# for d in data:
#     new_data = letters_to_digit(d)
#     temp.append(new_data)
# print(temp)
    