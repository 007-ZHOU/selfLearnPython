
# 读取文件内容并处理每行
with open('selfLearn/ip代理节点.txt', 'r',encoding='utf-8') as input_file:
    lines = [line.strip() for line in input_file]

# 将每行加上引号和逗号
formatted_lines = [f'"{line}",\n' for line in lines]

# 将处理后的内容写入文件
with open('selfLearn/ip代理节点修改.txt', 'w',encoding='utf-8') as output_file:
    output_file.writelines(formatted_lines)
