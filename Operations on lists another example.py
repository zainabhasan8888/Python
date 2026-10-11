class_a = ["Tom", "Jack", "Sarah", "Ben"]
class_b = ["Fred", "Tina", "Micheal"]
# merge two lists in a one list.
total = []
total.extend(class_a)
total.extend(class_b)
print(total)
# another way to merge lists.
total_students = class_a + class_b
print(total_students)
# remove an item from a list.
numbers = [0,1,2,3,4,5]
numbers.remove(1)
print(numbers)
