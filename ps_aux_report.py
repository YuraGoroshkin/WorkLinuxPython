import subprocess


def create_data():
    out = start_ps_aux().stdout
    all_list = str(out).split(sep='\\n')
    result_count_process = len(all_list) - 1
    user = []
    for object_list in all_list:
        list_this_obj = object_list.split()
        if list_this_obj[0] not in user:
            user.append(list_this_obj[0])
    user.pop()
    user.pop(0)
    return user, result_count_process


def out_file():
    pass


def start_ps_aux():
    result = subprocess.run(["ps", "aux"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return result

a = create_data()
print(a[0])
# a = start_ps_aux().stdout
# # create List in string
# c = str(a).split(sep='\\n')
# # create element in string
# for i in c:
#     a = i.split()
#     c = a[0]
#     print(a[0])
# # writing
# file = open("otus7.txt", "w")
# file.write(str(c))
# file.close()

# print(a)
# print("HELLO IT IS ERROR \n" + start_ps_aux().stderr.decode())
# print("HELLO IT IS OUT \n" + start_ps_aux().stdout.decode())
