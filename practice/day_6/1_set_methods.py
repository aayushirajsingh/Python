# Write program set all methods.

s1 = {'g', 'e', 'k', 's'}
s2 = {'k', 'u', 'j', 'e'}

union = s1.union(s2)
print('Sets union: ', union)

intersection = s1.intersection(s2)
print('Sets intersection: ', intersection)

difference = s1.difference(s2)
print('Sets difference: ', difference)

symmetric_difference = s1.symmetric_difference(s2)
print("Sets symmetric difference:", symmetric_difference)

s3 = s1.copy()
print('Set copy:', s3)

s1.add('f')
print('Set after adding:', s1)

s1.discard('g')
print('Set after discarding:', s1)

s1.update('o')
print('Set after updating:', s1)

s1.remove('s')
print('Set after removing:', s1)

s1.pop()
print('Set after popping:', s1)

s1.clear()
print('Set after clearing:', s1)