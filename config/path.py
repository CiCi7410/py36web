import os

path_path = os.path.abspath(__file__)
path_dir_path = os.path.dirname(path_path)
root_path = os.path.dirname(path_dir_path)

excel_path = os.path.join(root_path, "data", "cases.xlsx")

logs_path = os.path.join(root_path, "logs")
if not os.path.exists(logs_path):
    os.mkdir(logs_path)

reports_path = os.path.join(root_path, "reports")
if not os.path.exists(reports_path):
    os.mkdir(reports_path)

host_path = os.path.join(path_dir_path, "host.yaml")
security_path = os.path.join(path_dir_path, "security.yaml")
