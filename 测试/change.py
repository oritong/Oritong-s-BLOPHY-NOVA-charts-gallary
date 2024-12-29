import json
import os

# 获取当前文件夹中的第一个 .mc 文件
def find_mc_file():
    # 强制设置当前工作目录为脚本所在目录
    current_folder = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_folder)
    print(f"当前工作目录：{current_folder}")  # 打印当前目录

    for file_name in os.listdir(current_folder):
        if file_name.endswith(".mc"):
            print(f"找到文件: {file_name}")
            return os.path.join(current_folder, file_name)
    print("未找到 .mc 文件！")
    return None

# 读取 .mc 文件
def read_mc_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("成功加载 .mc 文件")
            return data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到！")
        return None
    except json.JSONDecodeError:
        print(f"文件 {filename} 不是有效的 JSON 格式！")
        return None

# 从 note 中获取最后一项的 offset 值并除以 1000，如果没有找到则返回 0
def extract_and_process_last_offset(data):
    if 'note' in data and len(data['note']) > 0:
        last_note = data['note'][-1]
        if 'offset' in last_note:
            offset_value = last_note['offset']
            a = offset_value / 1000  # 将 offset 除以 1000
            print(f"获取到的 offset 值为: {offset_value}, 转换后的值为: {a}")
            return a
    print("未找到有效的 offset 值，默认返回 0")
    return 0  # 如果没有找到有效的 offset，返回 0

# 获取 time 数组中的 beat 和 bpm 并转换为 bpmList
def create_bpm_list(data):
    bpm_list = []
    if 'time' in data:
        for entry in data['time']:
            if 'beat' in entry and 'bpm' in entry:
                beat = entry['beat']
                bpm = entry['bpm']
                
                a = beat[0]
                b = beat[1]
                c = beat[2]
                d = bpm
                e = a + b / c if c != 0 else a
                e = round(e, 8)  # 保证最大保留到小数点后8位
                
                bpm_list.append({
                    "integer": a,
                    "molecule": b,
                    "denominator": c,
                    "currentBPM": d,
                    "ThisStartBPM": e
                })
    print(f"生成的 bpmList: {bpm_list}")  # 打印生成的 bpmList
    return bpm_list

# 创建 Chart.json 文件
def create_chart_json(offset, bpm_list):
    chart_data = {
        "yScale": 6.0,
        "beatSubdivision": 4,
        "verticalSubdivision": 16,
        "eventVerticalSubdivision": 10,
        "playSpeed": 1.0,
        "offset": offset,
        "musicLength": -1.0,
        "loopPlayBack": True,
        "bpmList": bpm_list,
        "boxes": [{
                "boxEvents": {
                    "speed": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                               "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                               "startValue": 3.0, "endValue": 3.0, "curveIndex": 0, "IsSelected": False}],
                    "moveX": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                               "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                               "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
                    "moveY": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                               "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                               "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
                    "rotate": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                               "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                               "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
                    "alpha": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                               "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                               "startValue": 1.0, "endValue": 1.0, "curveIndex": 0, "IsSelected": False}],
                    "scaleX": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                                "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                                "startValue": 2.7, "endValue": 2.7, "curveIndex": 0, "IsSelected": False}],
                    "scaleY": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                                "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                                "startValue": 2.7, "endValue": 2.7, "curveIndex": 0, "IsSelected": False}],
                    "centerX": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                                 "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                                 "startValue": 0.5, "endValue": 0.5, "curveIndex": 0, "IsSelected": False}],
                    "centerY": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                                 "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                                 "startValue": 0.5, "endValue": 0.5, "curveIndex": 0, "IsSelected": False}],
                    "lineAlpha": [{"startBeats": {"integer": 0, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 0.0},
                                   "endBeats": {"integer": 1, "molecule": 0, "denominator": 1, "currentBPM": 0.0, "ThisStartBPM": 1.0},
                                   "startValue": 0.0, "endValue": 0.0, "curveIndex": 0, "IsSelected": False}],
                    "LengthSpeed": 1, "LengthMoveX": 1, "LengthMoveY": 1, "LengthRotate": 1,
                    "LengthAlpha": 1, "LengthScaleX": 1, "LengthScaleY": 1, "LengthCenterX": 1,
                    "LengthCenterY": 1, "LengthLineAlpha": 1
                },
                "lines": [{"onlineNotes": [], "onlineNotesLength": 0, "offlineNotes": [], "offlineNotesLength": 0,
                           "OnlineNotesLength": 0, "OfflineNotesLength": 0}] * 5
    }]}

    try:
        chart_file_path = "Chart.json"
        print(f"准备创建 Chart.json 文件：{chart_file_path}")
        with open(chart_file_path, "w", encoding="utf-8") as file:
            json.dump(chart_data, file, ensure_ascii=False, indent=4)
        print(f"成功创建 Chart.json 文件: {chart_file_path}")
    except Exception as e:
        print(f"创建 Chart.json 文件失败: {e}")

# 自动查找当前文件夹中的 .mc 文件并处理
mc_file = find_mc_file()

if mc_file:
    mc_data = read_mc_file(mc_file)
    if mc_data:
        offset = extract_and_process_last_offset(mc_data)
        bpm_list = create_bpm_list(mc_data)
        if offset is not None:
            create_chart_json(offset, bpm_list)
else:
    print("未找到任何 .mc 文件！")
