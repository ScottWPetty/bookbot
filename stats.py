
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_count = dict()
    string = text.lower()
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        elif char in char_count:
            char_count[char] += 1
    return char_count

def get_count_list(char_count):
    counts = []
    for char in char_count:
        temp = {"character" : char, "count" : char_count[char]}
        counts.append(temp)
    def sort_on(dict):
        return dict["count"]
    counts.sort(reverse=True, key=sort_on)
    return counts
