def levenshtein_distance(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Создаем матрицу размером (len_str1 x len_str2) и заполняем ее значениями
    matrix = [[0 for n in range(len_str2)] for m in range(len_str1)]

    for i in range(len_str1):
        matrix[i][0] = i

    for j in range(len_str2):
        matrix[0][j] = j

    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min([
                matrix[i-1][j] + 1,      # удаление
                matrix[i][j-1] + 1,      # вставка
                matrix[i-1][j-1] + cost  # замена
            ])

    return matrix[len_str1-1][len_str2-1]


word1 = "собака"
word2 = "скат"
distance = levenshtein_distance(word1, word2)
print(f"Расстояние Левенштейна между '{word1}' и '{word2}': {distance}")
