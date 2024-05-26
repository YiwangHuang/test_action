import random

# 生成两个随机数
random_number1 = random.randint(1, 43)
random_number2 = random.randint(1, 43)

print("开始抽取学号")

# 写入文档
file_path = 'random_numbers.txt'
with open(file_path, 'w') as file:
    file.write(f'Random Number 1: {random_number1}\nRandom Number 2: {random_number2}')

# 输出写入文件的结果
print(f'文件 {file_path} 成功写入！')
