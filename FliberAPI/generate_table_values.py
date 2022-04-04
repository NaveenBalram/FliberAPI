#
import os
# scripts = ""
# tables = ""
# schemas = ""
#
# with open("c_data.py", "r") as re:
#     for line in re.readlines():
#         script_values = line.split("=")[0].split(",")
#
#         scripts += f'[uuid.uuid4(), {script_values[0].strip()}, {script_values[1].strip()}, {script_values[2].strip()}, {script_values[3].strip()}, {script_values[4].strip()}, datetime.now(), datetime.now()],\n'
#
#         # try:
#         #     value = int(script_values[1].strip())
#         # except ValueError:
#         #     pass
#         #
#         # try:
#         #     value = float(script_values[1].strip())
#         # except ValueError:
#         #     pass
#         #
#         # try:
#         #     value = bool(script_values[1].strip())
#         # except ValueError:
#         #     pass
#         #
#         # if isinstance(value, int):
#         #     tables += f"{script_values[0]} = Column(Integer, nullable=False)\n"
#         # elif isinstance(value, bool):
#         #     tables += f"{script_values[0]} = Column(String, nullable=False, default=False)\n"
#         # elif isinstance(value, float):
#         #     tables += f"{script_values[0]} = Column(String, nullable=False, default=False)\n"
#         # elif isinstance(script_values[1].strip(), str):
#         #     tables += f"{script_values[0]} = Column(String, nullable=False)\n"
#         #
#         # if isinstance(value, int):
#         #     schemas += f"{script_values[0]} : int\n"
#         # elif isinstance(value, bool):
#         #     schemas += f"{script_values[0]} = bool\n"
#         # elif isinstance(value, float):
#         #     schemas += f"{script_values[0]} = float\n"
#         # elif isinstance(script_values[1], str):
#         #     schemas += f"{script_values[0]} = str\n"
#
#
# with open("db_values.txt","w") as dbw:
#     dbw.write(scripts)
#
# # with open("table_values.txt", "w") as dbw:
# #     dbw.write(tables)
# #
# # with open("schema_values.txt", "w") as dbw:
# #     dbw.write(schemas)


import os

# dir_list = os.listdir(
#     r"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPI\app\api\routes"
# )

# for ldir in dir_list:
#     if ldir not in ["__pycache__", "api.py"]:
#         pass
# dir_list = os.listdir(r"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPILatest\app\service")
# actions = ["create", "update", "get", "delete"]
# dir_list.pop(dir_list.index('__init__.py'))
# dir_list.pop(dir_list.index('__pycache__'))
# dir_list.pop(dir_list.index('rebalance_logic'))
# dir_list.pop(dir_list.index('post_retirement_logic'))
#
# dir_list = dir_list[8:]
# # print(dir_list)

for file_name in ["banks.py", "asset_type.py"]:

    name = file_name.split(".")[0]
    f_name = name.split("_")
    rep_name = ""
    for x in f_name:
        rep_name += x.capitalize()
        # print(rep_name)

    with open(fr"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPILatest\app\service\{file_name}", "r") as r:
        text = ""
        for line in r:
            # print(f"-> Out{rep_name}Schema")

            if line.__contains__(f"-> Out{rep_name}Schema"):
                text += line.replace(f'-> {rep_name}Schema', "")
                continue

            if line.__contains__(f"Out{rep_name}Schema(**"):
                text += line.replace(f'Out{rep_name}Schema(**',"").replace(".dict())", "")
                continue

            if line.__contains__(f"{name} = []"):
                continue

            if line.strip().__contains__(f'{name}_repository = {rep_name}Repository(self._db_session)'):
                continue

            if line.__contains__(f'await {name}_repository'):
                text += line.replace(f'{name}_repository', f'self._{name}_repository')
                continue

            text += line
            if line.__contains__("self._db_session: AsyncSession = db_session"):
                text += f"        self._{name}_repository = {rep_name}Repository(self._db_session)\n"

        with open(fr"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPILatest\app\service\{file_name}", "w") as f:
            f.write(text)

