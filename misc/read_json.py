import yaml


def read_yaml(file):
    with open(file, "r") as stream:
        try:
            file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return file