import yaml


def yaml_handle(fpath):
    with open(fpath, encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        return data
