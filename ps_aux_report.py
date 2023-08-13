import subprocess


def create_data():
    out = start_ps_aux().stdout
    all_list = str(out).split(sep='\\n')
    result_count_process = len(all_list) - 1
    user = []
    count_user = {}
    file = open("otus7.txt", "w")
    file.write(str(all_list))
    file.close()
    for object_list in all_list:
        list_this_obj = object_list.split()
        if list_this_obj[0] not in user:
            user.append(list_this_obj[0])
        elif list_this_obj[0] in user:
            i = user.index(list_this_obj[0])
            key = str(i - 1)
            if key not in count_user:
                count_user.update({str(i - 1) : 0})
            if key in count_user:
                count_user[str(i - 1)] = count_user.get(str(i - 1)) + 1
    user.pop()
    user.pop(0)
    result_count_root = all_list.count('root')
    return user, result_count_process, result_count_root


def out_file():
    pass


def start_ps_aux():
    result = subprocess.run(["ps", "aux"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return result

a = create_data()
print(a[0])
print(a[2])

# for i in c:
#     a = i.split()
#     c = a[0]
#     print(a[0])
# # writing
# file = open("otus7.txt", "w")
# file.write(str(c))
# file.close()

