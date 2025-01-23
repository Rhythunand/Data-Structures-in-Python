def test(lst) :
  result = {}
  for item in lst :
    result[item[0]] = item[1:]
  return result

students = [[1, 'Jean Castro', 'V',], [2, 'Lucan Powell', 'V'], [3, 'Brain Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOriginal list of lists :")
print(students)
print("\n Converted list to dictionary :")
print(test(students))