def anagram(word):
    alist1 = list(word)
    alist2 = list(word[::-1])
    if alist1 == alist2:
        return True
    else:
        return False

print(anagram('radar'))
print(anagram('cheat'))
print(anagram('racecar'))
