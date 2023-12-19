



def open_file(file: str):
    with open(file=file, mode='r') as f:
        return f.readlines()
    
def aoc_day_1_ans_1(input_data: list):
    temp = []
    data = [ [ l for l in line if l.isdigit()] for line in input_data ]
    for d in data:
        temp.append(int(d[0] + d[-1]))
        
    # print(temp)
    
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
    temp: list = ['_' for i in range(len(data))]
    
    for n, dig in enumerate(data):
        if dig.isdigit():
            temp[n] = dig

    for let_dig in letters_to_digits_dictionary.keys():
        if let_dig in data:
            for n, s in enumerate(data):
                if data.find(let_dig, n, len(data)) > -1:
                    temp[data.find(let_dig, n, len(data))] = str(letters_to_digits_dictionary[let_dig])
                    # data = data.replace(let_dig, ''.join([ '_' for i in range(len(let_dig)) ]), 1)
                    # print(temp)

    return [i  for i in temp if i != '_']

def aoc_day_1_ans_2_change_data_to_digit_numbers(data):
    temp: list = []
    for d in data:
        new_data = ''.join(letters_to_digit(d))
        temp.append(new_data)

    return temp


            
    
### test part 1 ###
data = open_file(r'advent_of_code_2023\day_1\test_input.txt')
print(aoc_day_1_ans_1(data))

### ans part 1 ###
print("=" * 50)
print('ANS PART 1')
data_ans_1 = open_file(r'advent_of_code_2023\day_1\input.txt')
print(aoc_day_1_ans_1(data_ans_1))

### test part 2 ###
print("=" * 50)
print('ENTRY TEST PART 2')
print(('fiveeight792eightqskstrftdpccsrgskrhc'))
temp = letters_to_digit('fiveeight792eightqskstrftdpccsrgskrhc')
print(temp)

print("=" * 50)
print('INPUT TEST PART 2')

data_test = open_file(r'advent_of_code_2023\day_1\test_input_part_2.txt')
temp = aoc_day_1_ans_2_change_data_to_digit_numbers(data_test)
ans_test_2 = aoc_day_1_ans_1(temp)
print(ans_test_2)

print("=" * 50)
print('ANS PART 2')
data = open_file(r'advent_of_code_2023\day_1\input_part_2.txt')
temp = aoc_day_1_ans_2_change_data_to_digit_numbers(data)
ans2 = aoc_day_1_ans_1(temp)
print(ans2)
    