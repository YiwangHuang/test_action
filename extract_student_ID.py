import random

# 生成两个随机数
random_number1 = random.randint(1, 43)
random_number2 = random.randint(1, 43)

# 写入文档
with open('random_numbers.txt', 'w') as file:
    file.write(f'Random Number 1: {random_number1}\nRandom Number 2: {random_number2}')
