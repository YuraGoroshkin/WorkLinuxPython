import subprocess
import datetime


def create_data():
    out = start_ps_aux().stdout
    all_list = str(out).split(sep='\\n')
    result_count_process = len(all_list) - 1
    users = []
    count_user = {}
    # dic with name_coman / cpu / mem
    comands = {}
    cpu = float(0)
    mem = float(0)
    all_list.pop(0)
    all_list.pop()
    # go to list all objects user/pid/cpu and etc
    for object_list in all_list:
        list_this_obj = object_list.split()
        cpu += float(list_this_obj[2])
        mem += float(list_this_obj[4])
        if list_this_obj[0] not in users:
            users.append(list_this_obj[0])
        elif list_this_obj[0] in users:
            i = users.index(list_this_obj[0])
            key = str(i)
            if key not in count_user:
                count_user.update({str(i): [0, i]})
            if key in count_user:
                count_user[str(i)][0] = count_user.get(str(i))[0] + 1
        if len(list_this_obj) == 12:
            name_comand = list_this_obj[10] + " " + list_this_obj[11]
            if len(name_comand) > 20:
                name_comand = name_comand[0:20] + '...'
            if name_comand not in comands.keys():
                # write name_comand:[name_comand, cpu, mem]
                comands.update({name_comand: [name_comand, list_this_obj[2], list_this_obj[3]]})
        if len(list_this_obj) == 11:
            name_comand = list_this_obj[10]
            if len(name_comand) > 20:
                name_comand = name_comand[0:20] + '...'
            if name_comand not in comands.keys():
                # write name_comand:[name_comand, cpu, mem]
                comands.update({name_comand: [name_comand, list_this_obj[2], list_this_obj[3]]})
    mem = float("{0:.1f}".format(mem / 1000000))
    cpu = round(cpu)
    string_for_user_process = ''
    # create string from a dic with index and a list
    for index, user in enumerate(users):
        dict_key = str(index)
        if dict_key in count_user:
            user_processes = count_user[dict_key][0] + 1
            string_for_user_process += f"  {user}: {user_processes}\n"
        else:
            string_for_user_process += f"  {user}: 1\n"
    # search max cpu comand
    max_cpu_comand = max(list(comands.items()), key=lambda i: i[1][1])
    # search max mem comand
    max_mem_comand = max(list(comands.items()), key=lambda i: i[1][2])
    data = (
        f'Отчёт о состоянии системы:\n  Пользователи системы:{users}\n  Процессов запущено:{result_count_process}\n  '
        f'Пользовательских процессов:\n{string_for_user_process}  Всего памяти используется:{mem} mb\n  Всего CPU используется:{cpu} %\n  '
        f'Больше всего памяти использует: {max_mem_comand[1][2]}% {max_mem_comand[1][0]}\n  Больше всего CPU использует: {max_cpu_comand[1][1]}% {max_cpu_comand[1][0]}')
    return data


def out_file():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    file = open(f"{date.day}-{date.month}-{date.year}-{time.hour}:{time.minute}-scan-ps.txt", "w")
    form = create_data()
    file.write(form)
    file.close()
    pass


def start_ps_aux():
    result = subprocess.run(["ps", "aux"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return result


out_file()
print(create_data())
