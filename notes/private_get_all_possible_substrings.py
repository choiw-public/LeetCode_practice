def get_all_substrings(s):
    substrings = ['']
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings


def get_all_substrings_ordered_by_length(s):
    substrings = ['']
    for window_size in range(1, len(s) + 1):
        for start_index in range(0, len(s) - window_size + 1):
            substrings.append(s[start_index:start_index + window_size])
    return substrings


a = get_all_substrings('asdf')
b = get_all_substrings_ordered_by_length('asdf')

ar = [0, 1, 2, 3, 4, 5]

for start_idx in range(0, len(ar) - 3 + 1):
    print(ar[start_idx:start_idx + 3])
