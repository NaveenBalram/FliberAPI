import os

dir_list = os.listdir(
    r"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPI\app\service"
)


def generate(name):

    class_name1 = ""
    name = name.rsplit(".", maxsplit=1)[0]
    function_name1 = name
    names = name.split("_")

    for name in names:
        class_name1 += name.capitalize()

    return function_name1, class_name1


for i in dir_list:
    if i not in ["__init__.py", "__pycache__"]:
        print(i)
        with open(
            rf"C:\Users\Anil HP LGHIVE2104\PycharmProjects\FliberAPI\app\service\{i}",
            "a",
        ) as app:
            function_name, class_name = generate(i)

            app.write(
                """\n
    async def delete_{}_by_user_id(self, user_id: UUID):
        {}_repository = {}Repository(self._db_session)
        await {}_repository.delete_by_user_id(user_id)""".format(
                    function_name, function_name, class_name, function_name
                )
            )
