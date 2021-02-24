import pytest
from datetime import datetime
from config.path import reports_path
import os

cs = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_path = "report" + cs + ".html"
report = os.path.join(reports_path, file_path)
pytest.main(["--html={}".format(report), "-s"])
