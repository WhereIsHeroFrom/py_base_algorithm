s = input()
i, j = 0, len(s) - 1
while i < j:
    if s[i] != s[j]: break
    i += 1
    j -= 1
print('Y' if i >= j else 'N')