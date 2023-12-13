



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
    
### test ###
data = open_file(r'D:\Python\#14_advent_of_code_2023\day_1\test_input.txt')
print(aoc_day_1_ans_1(data))

data_ans_1 = open_file(r'D:\Python\#14_advent_of_code_2023\day_1\input.txt')
print(aoc_day_1_ans_1(data_ans_1))
    