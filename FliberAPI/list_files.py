import os

dir_list = os.listdir(
    r"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPI\app\service"
)

new_list = []
for name in dir_list:

    name = name.rsplit(".", maxsplit=1)[0]
    name = name.split("_")
    new_name = ""
    for value in name:
        new_name += value.capitalize()
    new_list.append(new_list)

    with open("file_list_names.txt", "a") as wr:
        wr.write(f"{new_name}\n")

print(new_list)
