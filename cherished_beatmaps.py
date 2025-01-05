import os
import json

# 获取脚本所在的目录路径
current_folder = os.path.dirname(os.path.realpath(__file__))

# 将工作目录设置为脚本所在的目录
os.chdir(current_folder)

# 读取 index.json 文件
def read_json_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"文件 {file_name} 不存在。")
        return None
    except json.JSONDecodeError:
        print(f"文件 {file_name} 内容格式不正确。")
        return None

# 写入修改后的数据到 index.json 文件
def write_json_file(file_name, data):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"数据已成功写入 {file_name}。")
    except Exception as e:
        print(f"写入文件时发生错误: {e}")

# 将最后一段移到第一段的下面
def move_last_to_first(data):
    if len(data) > 1:
        # 获取最后一段并移除它
        last_item = data.pop()
        # 将最后一段添加到第一段的后面
        data.insert(1, last_item)
    return data

if __name__ == "__main__":
    # 指定文件名
    file_name = "index.json"
    
    # 读取 JSON 文件
    json_data = read_json_file(file_name)
    
    if json_data is not None:
        # 将最后一段移到第一段的后面
        updated_data = move_last_to_first(json_data)
        
        # 写入修改后的数据回文件
        write_json_file(file_name, updated_data)
