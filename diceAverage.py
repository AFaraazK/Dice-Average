# dictionary of tuples with each dice pair
# loop through and add each possible dice pair combination
# Choose the lowest value in each pair
# average the result

rollsDict = []

for i in range(20):
  for j in range(20):
    rollsDict.append((i + 1, j + 1))

rollsDictPruned = []

for x in rollsDict:
  rollsDictPruned.append(min(x))

cumul = 0
for x in rollsDictPruned:
  cumul += x

cumul /= len(rollsDictPruned)
print(cumul)
