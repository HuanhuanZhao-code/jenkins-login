def read_txt(filepath):
    with open(filepath, mode="r", encoding="utf-8") as f:
        return f.readlines()
