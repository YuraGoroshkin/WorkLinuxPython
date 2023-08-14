import subprocess


def create_data():
    out = start_ps_aux().stdout
    all_list = str(out).split(sep='\\n')
    result_count_process = len(all_list) - 1
    user = []
    count_user = {}
    cpu = float(0)
    mem = float(0)
    all_list.pop(0)
    all_list.pop()
    # go to list all objects user/pid/cpu and etc
    for object_list in all_list:
        list_this_obj = object_list.split()
        cpu += float(list_this_obj[2])
        mem += float(list_this_obj[4])
        if list_this_obj[0] not in user:
            user.append(list_this_obj[0])
        elif list_this_obj[0] in user:
            i = user.index(list_this_obj[0])
            key = str(i)
            if key not in count_user:
                count_user.update({str(i): 0})
            if key in count_user:
                count_user[str(i)] = count_user.get(str(i)) + 1
    mem = float("{0:.1f}".format(mem / 1000000))
    cpu = round(cpu)
    data = (f'Отчёт о состоянии системы:\n  Пользователи системы:{user}\n  Процессов запущено:{result_count_process}\n  '
            f'Пользовательских процессов:{user} {count_user}\n  Всего памяти используется:{mem} mb\n  Всего CPU используется:{cpu} %')
    return data


def out_file():
    file = open("otus7.txt", "w")
    form = create_data()
    file.write(form)
    file.close()
    pass


def start_ps_aux():
    result = subprocess.run(["ps", "aux"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return result


a = create_data()
print(a)
