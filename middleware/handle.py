from config.path import excel_path, host_path, security_path, logs_path
from common.excel_handle import ExcelHandle
import re
from faker import Faker
import requests
from common.yaml_handle import yaml_handle
from common.logger_handle import my_logger
import os


def generate_new_email():
    fk = Faker(locale="zh_CN")
    while True:
        new_email = fk.email()
        url = yaml_handle(host_path)["email_host"].format(new_email)

        resp = requests.request(url=url,
                                method="get"
                                )
        result = resp.json()["count"]
        if result == 0:
            print(new_email)
            return new_email


def create_username():
    fk = Faker(locale="zh_CN")
    while True:
        username = fk.user_name()
        if 6 <= len(username) <= 20:
            url = yaml_handle(host_path)["username_host"].format(username)
            print(url)
            resp = requests.request(url=url,
                                    method="get"
                                    )
            result = resp.json()["count"]
            if result == 0:
                return username


def create_project_name_201():
    project_name_201 = ""
    for i in range(202):
        project_name_201 += "a"
    return project_name_201


def create__name():
    fk = Faker(locale="zh_CN")
    name = fk.user_name()
    return name


class Handle:
    excel = ExcelHandle(excel_path)
    host_data = yaml_handle(host_path)
    security_data = yaml_handle(security_path)

    file_path = os.path.join(logs_path, host_data["logger"]["file_name"])
    logger = my_logger(name=host_data["logger"]["name"],
                       file_name=file_path)

    email_exist = security_data["email_exist"]
    username_exist = security_data["username_exist"]
    password_exist = security_data["password_exist"]
    project_name_exit = security_data["project_name_exit"]

    # project_name_201 = create_project_name_201()
    @classmethod
    def repalce_data(cls, string, pattern="#(.*?)#"):
        results = re.finditer(pattern=pattern, string=string)
        for result in results:
            old = result.group()
            key = result.group(1)
            if key == "email":
                new = generate_new_email()
                string = string.replace(old, new)
            elif key == "username":
                new = create_username()
                string = string.replace(old, new)
            elif key == "leader_51" or key == "name_201" or key =="author_51" or key == "name_51" or key == "tester_51" or key == "programmer_51" or key == "app_101" or key == "desc_201":
                new = create_project_name_201()
                string = string.replace(old, new)
            elif key == "name":
                new = create__name()
                string = string.replace(old, new)
            else:
                new = str(getattr(cls, key, ''))
                string = string.replace(old, new)
        print("string ", string)
        return string


if __name__ == "__main__":
    print(create_project_name_201())
