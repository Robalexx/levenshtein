import os
import re
import sys
import time


start_time = time.time()

i = 0
listeTerme = []
terme = open("termes.txt", mode="r", encoding="UTF-8")

def LevenshteinD(word1, word2):
    """Dynamic programming solution"""
    m = len(word1)
    n = len(word2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                
    return table[-1][-1]

for item in terme:
    item = item.rstrip("\n")
    if re.search(r"[^ ]", item):
        listeTerme.append(item)

with open("levenshtein4.txt", 'w', encoding="UTF-8") as f:
    for i in range(0,len(listeTerme)):
        for j in range(0, len(listeTerme)):
            if listeTerme[i] != listeTerme [j]:
                #LevenshteinD(listeTerme[i], listeTerme[j])
                if LevenshteinD(listeTerme[i], listeTerme[j]) < 4:
                    print(listeTerme[i], "\t", listeTerme[j], "\t", LevenshteinD(listeTerme[i], listeTerme[j]))
                    f.write(listeTerme[i] + "\t" + listeTerme[j] + "\t" + str(LevenshteinD(listeTerme[i], listeTerme[j])) + "\n")

print("--- %s seconds ---" % (time.time() - start_time))

terme.close()
f.close()

#7514