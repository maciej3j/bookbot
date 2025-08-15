def count_words(text: str) -> int:
    return len(text.split())


def count_each_character(text: str) -> dict:
    cnt = {}
    for ch in text:
        ch = ch.lower()
        if ch.isalpha():
            if ch not in cnt:
                cnt[ch] = 1
            else:
                cnt[ch] += 1
    return cnt


def sort_dict(dict_to_sort: dict) -> list:
    new_list = []
    for key, value in dict_to_sort.items():
        new_list.append({"name": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def sort_on(items):
    return items["num"]
