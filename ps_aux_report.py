import subprocess


def out_file():
    pass


def start_ps_aux():
    result = subprocess.run(["ps", "aux"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return result



print(start_ps_aux())
print("HELLO IT IS ERROR \n" + start_ps_aux().stderr.decode())
print("HELLO IT IS OUT \n" + start_ps_aux().stdout.decode())
