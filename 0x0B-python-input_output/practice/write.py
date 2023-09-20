#!/usr/bin/python3

def write_file(filename="", tt=""):
    try:
        with open(filename, "a", encoding="utf-8") as my_file:
            char_num = my_file.write(tt)
        return char_num
    except Exception:
        return 0

nb = write_file("my_file_.t", "here is the end")
print(nb)
