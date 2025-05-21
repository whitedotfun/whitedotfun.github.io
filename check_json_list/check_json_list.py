import json
import os
import sys

CONFIG_FILE = "json_list.txt"

def check_json_format(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, "✅ 格式正确"
    except json.JSONDecodeError as e:
        return False, f"❌ 格式错误: {e}"
    except Exception as e:
        return False, f"❌ 文件读取失败: {e}"

def get_exe_dir():
    if getattr(sys, 'frozen', False):  # 打包为 exe 后为 True
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def main():
    exe_dir = get_exe_dir()
    list_path = os.path.join(exe_dir, CONFIG_FILE)

    if not os.path.isfile(list_path):
        print(f"❌ 缺少配置文件: {CONFIG_FILE}")
        input("按任意键退出...")
        return

    with open(list_path, 'r', encoding='utf-8') as f:
        paths = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    for relative_path in paths:
        abs_path = os.path.normpath(os.path.join(exe_dir, relative_path))
        if not os.path.isfile(abs_path):
            print(f"[{relative_path}] ❌ 文件不存在")
            continue

        ok, msg = check_json_format(abs_path)
        print(f"[{relative_path}] {msg}")

    input("检查完成，按任意键退出...")

if __name__ == "__main__":
    main()
