spisol = [5, 2, 3, 1, 10]
maxspisol = max(spisol)
minspisol = min(spisol)
indexmaxspisol = spisol.index(maxspisol)
indexminspisol = spisol.index(minspisol)

spisol.pop(indexmaxspisol)
spisol.pop(indexminspisol)

spisol.insert(indexminspisol, maxspisol)
spisol.insert(indexmaxspisol, minspisol)
print(spisol)
