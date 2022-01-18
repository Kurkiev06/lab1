import json

file = open("pokemon_full.json")
pokemon_desc = file.read()
print("Общее количество символов в файле равно", len(pokemon_desc))
file.close()

counter = 0
for symbol in pokemon_desc:
    if symbol.isalnum():
        counter += 1
print("Количество символов без пробелов и знаков препинания равно", counter)

desc_poke_py = json.loads(pokemon_desc)
longest_desc = 0
pokemon_name = ""
max_words = 0
abilities = ""
for item in desc_poke_py:
    desc = item["description"]
    if len(desc) > longest_desc:
        longest_desc = len(desc)
        poke_name = item["name"]
    for skills in item["abilities"]:
        if len(skills.split()) > max_words:
            max_words = len(skills.split())
            abilities = skills

print("У покемона", poke_name, "наиболее длинное описание")
print("Умение", abilities, "содержит больше всего слов")