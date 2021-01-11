def anagram(word_a, word_b):
    w1 = word_a.lower()
    w2 = word_b.lower()
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "Cinema"))