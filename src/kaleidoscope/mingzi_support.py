from re import findall
import json

# from mingzi import *

ds_path = "C:/Users/17818/Music/mingzi/src/mingzi/data.json"


def conv_to_json():
    with open(ds_path, "r", encoding="UTF-8") as f:
        data = json.load(f)

    data["surname"] = {}
    data["com_surname"] = com_surname
    data["male_single"] = male_single
    data["male_double"] = male_double
    data["female_single"] = female_single
    data["female_double"] = female_double

    total = sum(surname.values())
    for i in surname.keys():
        data["surname"][i] = surname[i] / total

    with open(ds_path, "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def show_ds():
    length = []
    with open(ds_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    for cat in data.keys():
        length.append(len(data[cat]))
        print("{}:\t{}".format(cat, len(data[cat])))
    print("\nnames:     {}\nsurnames:  {}\n\n\n\n\n".format(sum(length[0:4]), sum(length[4:])))


def update_ds(html, cat):
    pat = "[\u4e00-\u9fa5]+"
    result = findall(pat, html)

    with open(ds_path, "r", encoding="UTF-8") as f:
        data = json.load(f)

    selected = []
    for i in result:
        if i not in data[cat]:
            data[cat].append(i)
            selected.append(i)

    cmd = input("{} new names found.\n{}\nUpdate (Y/n)? ".format(len(selected), selected))
    if cmd in ["y", "Y"]:
        with open(ds_path, "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Done. {} {} updated.".format(cat, len(selected)))
    else:
        pass


if __name__ == "__main__":
    html = """
秀娟
    """
    # conv_to_json()
    # show_ds()
    update_ds(html, "female_double")
