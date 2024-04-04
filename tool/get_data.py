from tool.read_txt import read_txt


def get_data(filepath):
    arras = []
    for data in read_txt(filepath):
        arras.append(tuple(data.strip().split(",")))
    return arras[1:]


if__name__ = "__main__"

get_data("../data/login.txt")