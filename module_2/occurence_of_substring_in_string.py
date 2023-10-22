string1 = "ababababa"
sub1 = 'aba'

str1 = len(string1)
res = sum(1 for i in range(str1)
          if string1.startswith("aba", i))
print("Number of substrings", res)