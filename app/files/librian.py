import json


def txt_to_str(file, direction=False):
    if direction:
        with open(f"app/files/directions/{file}", 'r', encoding='utf-8') as f:
            string = f.read()
            f.close()
        return string
    else:
        with open(f"app/files/{file}", 'r', encoding='utf-8') as f:
            string = f.read()
            f.close()
        return string


def get_directions(group):
    with open('app/files/all_directions.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    result = list()
    for item in directions[group]:
        result.append(((txt_to_str(item, True)), item))
    return result


def get_cods():
    with open('app/files/all_directions.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    result = list()
    for key in directions.keys():
        for item in directions[key]:
            result.append(item)
    return result


def get_b():
    with open('app/files/calc/b.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    return directions


def get_m():
    with open('app/files/calc/m.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    return directions


def get_a():
    with open('app/files/calc/a.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    return directions


def new_member(name):
    with open('app/json_files/stat.json', 'r', encoding='utf-8') as f:
        stat = json.load(f)
        f.close()
    stat["cnt"] += 1
    if name not in stat["members"]:
        stat["members"].append(name)
    with open('app/json_files/stat.json', 'w', encoding='utf-8') as f:
        json.dump(stat, f)
        f.close()


def get_stat():
    with open('app/json_files/stat.json', 'r', encoding='utf-8') as f:
        stat = json.load(f)
        f.close()
    return stat


def ban(name):
    with open('app/json_files/blacklist.json', 'r', encoding='utf-8') as f:
        blacklist = json.load(f)
        f.close()
    blacklist["members"].append(name)
    with open('app/json_files/blacklist.json', 'w', encoding='utf-8') as f:
        json.dump(blacklist, f)
        f.close()


def ban_check(name):
    with open('app/json_files/blacklist.json', 'r', encoding='utf-8') as f:
        blacklist = json.load(f)
        f.close()
    if name not in blacklist["members"]:
        return True
    return False


def admin_check(name):
    with open('app/json_files/admins.json', 'r', encoding='utf-8') as f:
        admins = json.load(f)
        f.close()
    if name in admins["members"]:
        return True
    return False


def new_task_num():
    with open('app/json_files/n_task.json', 'r', encoding='utf-8') as f:
        n_task = json.load(f)
        f.close()
    n_task["num"] += 1
    num = n_task["num"]
    with open('app/json_files/n_task.json', 'w', encoding='utf-8') as f:
        json.dump(n_task, f)
        f.close()
    return num


def new_task(chat_id, number, text):
    with open('app/json_files/tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        f.close()
    tasks[number] = (chat_id, text)
    with open('app/json_files/tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f)
        f.close()


def delete_task(number):
    with open('app/json_files/tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        f.close()
    del tasks[str(number)]
    with open('app/json_files/tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f)
        f.close()


def search_task(num):
    with open('app/json_files/tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        f.close()
    return tasks[str(num)]


def all_task():
    with open('app/json_files/tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        f.close()
    return tasks


def get_files():
    with open('app/json_files/all_files.json', 'r', encoding='utf-8') as f:
        all_files = json.load(f)
        f.close()
    result = dict()
    for item in all_files["files"]:
        if '0' in item:
            result[item] = f"app/files/directions/{item}"
        else:
            result[item] = f"app/files/{item}"
    return result


def open_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        f.close()
    return s


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()


def get_full_stat():
    with open('app/json_files/full_stat.json', 'r', encoding='utf-8') as f:
        full_stat = json.load(f)
        f.close()
    return full_stat


def add_to_full_stat(path):
    with open('app/json_files/full_stat.json', 'r', encoding='utf-8') as f:
        full_stat = json.load(f)
        f.close()
    full_stat[path] += 1
    with open('app/json_files/full_stat.json', 'w', encoding='utf-8') as f:
        json.dump(full_stat, f)
        f.close()
