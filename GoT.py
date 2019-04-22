from characters import characters
from houses import houses
from pprint import pprint

# How many characters names start with "A"?
def A_chars():
    name_count = 0
    for c in characters:
        if c["name"][0] == "A":
            name_count += 1
    print("There are %d characters whose name starts with A in GoT" % name_count)
# A_chars()

# How many characters names start with "Z"?
def Z_chars():
    name_count = 0
    for c in characters:
        if c["name"][0] == "Z":
            name_count += 1
    print("There are %d characters whose name starts with Z in GoT" % name_count)
# Z_chars()

# How many characters are dead?
def dead_chars():
    dead_count = 0
    for c in characters:
        if c["died"]:
            dead_count += 1
    print("There are %d dead characters in GoT" % dead_count)
# dead_chars()

# Who has the most titles?
def most_titles():
    most_titled_char = characters[0]
    for c in characters:
        if len(c["titles"]) > len(most_titled_char["titles"]):
            most_titled_char = c
    print("The character in GoT with the most titles is %s:" % most_titled_char["name"])
    for t in most_titled_char["titles"]:
        print(t)
# most_titles()

# How many are Valyrian?
def valyrian():
    val_count = 0
    for c in characters:
        if c["culture"] == "Valyrian":
            val_count += 1
    print("There are %d Valyrian characters in GoT" % val_count)
# valyrian()

# What actor plays "Hot Pie" (and don't use IMDB)?
def hot_pie():
    for c in characters:
        if c["name"] == "Hot Pie":
            print("Hot Pie is played by %s" % c["playedBy"][0])
# hot_pie()

# How many characters are *not* in the tv show?
def not_in_show():
    no_show = 0
    for c in characters:
        print(c["tvSeries"])
        if c["tvSeries"][0] == '':
            no_show += 1
    print("There are %d characters not in the GoT TV show" % no_show)
# not_in_show()

# Produce a list characters with the last name "Targaryen"
def targs():
    targ_list = []
    for c in characters:
        if len(c["name"]) < 11:
            continue
        if c["name"][-9:] == "Targaryen":
            targ_list.append(c["name"])
    print(targ_list)
# targs()

# Create a histogram of the houses (it's the "allegiances" key)
def allegiances():
    house_dict = {}
    for c in characters:
        if c["allegiances"]:
            for a in c["allegiances"]:
                house_name = houses[a]
                if house_name not in house_dict.keys():
                    house_dict[house_name] = 1
                if house_name in house_dict.keys():
                    house_dict[house_name] += 1
    for h in house_dict.keys():
        pprint(str(h) + ": " + str(house_dict[h]))
# allegiances()