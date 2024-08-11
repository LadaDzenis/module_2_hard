list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dict_ = {}
for element in list1:
    if element <= 2:
        continue
    for sum1 in range(1, element):
        for sum2 in range(sum1 + 1, element):
            if element % (sum1 + sum2) == 0:
                if element in dict_:
                    dict_[element].append((sum1, sum2))
                else:
                    dict_[element] = [(sum1, sum2)]
            continue

for key, values in dict_.items():
    string_values = [f'{a}{b}' for a, b in values]
    joined = "".join(string_values)
    print(f"{key}: {joined}")

