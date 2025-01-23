first = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Lenght of list", len(first))
print("First Element", first[0])
print("Last Element", first[-1])

first.append('Pappaya')
print("Updated list", first)

first.remove('Guava')
print("Updated list", first)

first.sort()
print("Sorted List", first)

first.pop(1)
print("Updated list", first)

first.reverse()
print("Reversed list", first)

print("Multiplication on list", first*2)

first = first[:4]
print("Sliced list", first)

first.clear()
print("Updated list", first)