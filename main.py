def sort_on(dict):
    return dict["repeats"]

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(f"There are {len(words)} words in this file")
    lower_contents = file_contents.lower()

    occurrence = {}
    for l in lower_contents:
        if l not in occurrence:
            occurrence[l] = 1
        else:
            occurrence[l] += 1
    # print(occurrence)
    
    sorted_list = []
    for char in occurrence:
        sorted_list.append({"character": char, "repeats": occurrence[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    # print(sorted_list)

    for pair in sorted_list:
        if not pair["character"].isalpha():
            continue
        print(f"The alphabet {pair['character']} was found {pair['repeats']} times")