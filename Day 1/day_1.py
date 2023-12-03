digits = []

def check_for_num(line):
    if line.startswith('zero'):
        return '0'
    elif line.startswith('one'):
        return '1'
    elif line.startswith('two'):
        return '2'
    elif line.startswith('three'):
        return '3'
    elif line.startswith('four'):
        return '4'
    elif line.startswith('five'):
        return '5'
    elif line.startswith('six'):
        return '6'
    elif line.startswith('seven'):
        return '7'
    elif line.startswith('eight'):
        return '8'
    elif line.startswith('nine'):
        return '9'
    else:
        return ''

with open('day_1.txt', 'r') as x:
    nums = x.readlines()

for line in nums:
    for i in range(0,len(line)):
        if line[i].isnumeric():
            first_dig = line[i]
            break
        else:
            res = check_for_num(line[i:])
            if res:
                first_dig = res
                break

    for i in range(0,len(line)):
        if line[i].isnumeric():
            second_dig = line[i]
        else:
            res = check_for_num(line[i:])
            if res:
                second_dig = res

    new_dig = int(first_dig + second_dig)
    digits.append(new_dig)
print(sum(digits))
