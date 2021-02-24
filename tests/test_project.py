from middleware.handle import Handle
import pytest
import json
import requests
from jsonpath import jsonpath

data = Handle.excel.read("project")
print(data)


@pytest.mark.parametrize("test_info", data)
def test_register(test_info):
    print("test_info ", test_info)
    test_info = json.dumps(test_info)
    test_info = Handle.repalce_data(test_info)
    test_info = json.loads(test_info)
    print(test_info)

    url = Handle.host_data["host"] + test_info["url"]
    method = test_info["method"]
    json_data = json.loads(test_info["json"])
    print(url)
    print(method)
    print(json_data)
    headers = json.loads(test_info["headers"])

    resp = requests.request(method=method,
                            url=url,
                            json=json_data,
                            headers = headers
                            )
    print(resp.json())
    code = resp.status_code
    print("code", code)
    expected = test_info["expected"]
    print("expected", expected)
    r = resp.json()
    print(r)
    try:
        assert code == expected
    except AssertionError as e:
        Handle.logger.error("用例失败了：{}".format(e))
        raise e
    finally:
        Handle.excel.write(sheet="project",
                           data=str(r),
                           row=int(test_info["case_id"]) + 1,
                           column=9)
    if test_info["extractor"]:
        print("token")
        extractors = json.loads(test_info["extractor"])
        print(extractors)
        for prop, exp in extractors.items():
            value = jsonpath(r, exp)[0]
            setattr(Handle, prop, value)


