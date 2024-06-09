# encoding=utf-8
import json
import random
import pandas as pd

def shffle_data(input_file):
    # 读取JSON文件，指定编码为UTF-8
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 检查数据是否为列表
    if isinstance(data, list):
        # 随机打乱列表元素顺序
        random.shuffle(data)

        # 将打乱顺序后的列表写入新的JSON文件，保留原始格式
        with open(input_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        print("JSON数据不是一个数组。")

def read_excel(input_file):
    # 读取Excel文件
    df = pd.read_excel(input_file)  # 替换为你的Excel文件名

    # 将数据转换为两个列表
    text_list = df['text'].tolist()
    sql_list = df['sql'].tolist()

    # 打印列表以验证
    return text_list, sql_list

def generate_json(db_id, input_list, output_list, history, instruction):
    # 创建一个包含固定值的字典
    data = {
        'db_id': db_id,
        'input': input_list,
        'output': output_list,
        'history': history,
        'instruction': instruction
    }
    return data

def add_to_json_file(filename, new_data):
    # 读取现有的JSON文件
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []  # 如果文件不存在或JSON解析失败，则创建一个空列表

    # 将新的数据添加到现有数据中
    existing_data.append(new_data)

    # 将更新后的数据写回JSON文件
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)

excel_file = "sql_excel.xlsx"
db_id_value = "zhly_nhjk"
history_value = []
instruction_value = """我想让你充当一个示例数据库前面的SQL终端, 你只需要把sql命令发给我。下面是一个描述任务的指令, 写一个适当的回复来完成请求。
\"\n##指示:\nzhly_nhjk 包含以下表 stats_meter_data_collect, tb_smart_manager_device, tb_building, tb_cabinet, tb_terminal, tb_room, tb_park, tb_month_eus, tb_meter_data, tb_loop, tb_floor, stats_day_meter, stats_month_meter, stats_month_collect, stats_day_collect. 表 stats_meter_data_collect 具有以下列 id, terminal_id, start_value, end_value, loop_level, create_time, update_time, terminal_type, cabinet_id, floor_id. 表 tb_smart_manager_device 具有以下列 id, name, identification, model, number, floor_id, install_time, create_user, create_time, update_user, update_time, del_flag. 表 tb_building 具有以下列 id, number, floor_count, park_id, area, user_id, create_user, create_time, update_user, update_time, del_flag. 表 tb_cabinet 具有以下列 id, number, floor_id, create_user, create_time, update_user, update_time, del_flag. 表 tb_terminal 具有以下列 id, identification, name, alias, model, smart_manager_device_id, loop_id, address, status, report_time_update, create_user, create_time, update_user, update_time, del_flag. 表 tb_room 具有以下列 id, floor_id, dal_flag, room_name, create_time, update_time, update_user, create_user. 表 tb_park 具有以下列 id, name, company, city, area, longitude, latitude, address, create_user, create_time, update_user, update_time, del_flag. 表 tb_month_eus 具有以下列 id, building_id, total_electric_energy, total_power, insert_time, year, month. 表 tb_meter_data 具有以下列 id, gateid, cabinet_id, loop_id, terminal_id, address, status, report_data, report_time, create_time. 表 tb_loop 具有以下列 id, name, current_specification, level, cabinet_id, load, create_user, create_time, update_user, update_time, del_flag. 表 tb_floor 具有以下列 id, floor_number, building_id, create_user, area, sort, create_time, update_user, update_time, del_flag. 表 stats_day_meter 具有以下列 id, terminal_id, kwh, floor_id, month, loop_level, day, terminal_type, create_time, cabinet_id, stats_time, update_time. 表 stats_month_meter 具有以下列 id, terminal_id, kwh, floor_id, month, year, loop_level, terminal_type, cabinet_id, create_time, update_time. 表 stats_month_collect 具有以下列 id, terminal_id, data, terminal_type, cabinet_id, loop_level, floor_id, month, year, create_time, stats_time, update_time. 表 stats_day_collect 具有以下列 id, terminal_id, data, terminal_type, create_time, cabinet_id, loop_level, stats_time, month, day, floor_id, update_time. \n\n"""

text_values, sql_values = read_excel(excel_file)


for text, sql in zip(text_values, sql_values):

    modified_text = "###输入:\n" + text + "\n\n###回答:"
    # 生成新的JSON数据
    new_json_data = generate_json(db_id_value, modified_text, sql, history_value, instruction_value)

    # 将新的JSON数据添加到现有的JSON文件中
    json_filename = "text.json"
    add_to_json_file(json_filename, new_json_data)

shffle_data("text.json")
