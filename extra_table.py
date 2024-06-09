import re
import json

def extract_table_names(sql_statement):
    # 正则表达式匹配SQL语句中的表名
    # 这里假设表名由字母、数字和下划线组成，并且不包含空格
    pattern = r'\b(FROM|JOIN|UPDATE|INSERT INTO)\s+(\w+)'

    # 使用findall方法找到所有匹配的表名
    matches = re.findall(pattern, sql_statement, re.IGNORECASE)

    # 提取表名部分并去除重复
    table_names = set(match[1] for match in matches)

    return table_names

if __name__ == '__main__':

    file_name = './data/test_db_hub_cn_0603.json'
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        sql_statement = item['output']
        table_names = extract_table_names(sql_statement)
        print(table_names)