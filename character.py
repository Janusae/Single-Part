def analyse_string():
    import re
    info = {}
    inputs = input("\..")
    special_character = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    letter = inputs.split(" ")
    special_count = 0
    for i in inputs:
        if i in special_character:
            special_count += 1
    info["special_character"] = special_count
    total_count = 0
    for a in inputs:
        if a != " ":
            total_count += 1
    info["total"] = total_count
    split = re.split(r"[% = $ ( ) * - + < > ? ! \ | /{ } _ - @ # , . ]" , inputs)
    counter = 0
    for i in split:
        if i.isalpha() == True and len(i) > 1:
            counter += 1
    info["words"] = counter
    print(info)
analyse_string()