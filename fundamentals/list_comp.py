my_list = [0, 1, 2, 3, 4]

using_comp = [x for x in range(5)]

print(my_list == using_comp)
print(using_comp)

mulp_list = [x * 3 for x in range(5)]
print(mulp_list)

print([n for n in range(10) if n % 2 == 0])

people_you_know = ["Greg", "max", " JOHN", "Rolf"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)
