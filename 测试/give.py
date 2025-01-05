import os

# 获取当前脚本所在目录
current_folder = os.path.dirname(os.path.realpath(__file__))

# 强制设置当前工作目录
os.chdir(current_folder)

# 文件路径
chart_file_path = os.path.join(current_folder, 'Chart.json')
need_file_path = os.path.join(current_folder, 'need.txt')

# 读取 need.txt 文件内容
try:
    with open(need_file_path, 'r', encoding='utf-8') as need_file:
        need_content = need_file.read().strip()  # 去除多余的换行符等空白字符
except FileNotFoundError:
    print("need.txt 文件不存在")
    exit(1)

# 读取 Chart.json 文件内容
try:
    with open(chart_file_path, 'r', encoding='utf-8') as chart_file:
        chart_content = chart_file.read().strip()

    # 确保文件以 ']} 结尾'
    if not chart_content.endswith(']}'):
        print("Chart.json 文件格式错误，未以 ']} 结尾'")
        exit(1)

    # 将 need.txt 的内容复制 8 次并加到文件最后的 ']}' 前
    new_content = chart_content[:-2] + (need_content * 8) + ']}'

    # 写回修改后的内容
    with open(chart_file_path, 'w', encoding='utf-8') as chart_file:
        chart_file.write(new_content)

    print("Chart.json 文件已成功更新！")

except FileNotFoundError:
    print("Chart.json 文件不存在")
except Exception as e:
    print(f"出现错误: {e}")
