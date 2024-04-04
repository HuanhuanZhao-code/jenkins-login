def read_txt(filepath):
    with open(filepath, mode="r", encoding="utf-8") as f:
        return f.readlines()

if__name__ = "__main__"
read_txt("../data/login.txt")