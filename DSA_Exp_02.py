#To create ADT that implements the “set” concept,
#A)Add(New element)-Place a value into the set,
#B)Remove(element)-Remove the value.
#C)Contains(element) Return true if element is in collection,
#D) Size ()-Return number of values in collection Iterator () Return an iterator used to loop over collection ,
#E)Intersection of two sets, F).Union of two sets. G) Difference between two sets, H) Subset.
def create_set():
    return set()

def add_to_set(s, element):
    s.add(element)

def remove_from_set(s, element):
    if element in s:
        s.remove(element)
    else:
        print(f"{element} not found in the set.")

def contains_in_set(s, element):
    return element in s

def size_of_set(s):
    return len(s)

def iterator_of_set(s):
    return iter(s)

def intersection_of_sets(set1, set2):
    return set1.intersection(set2)

def union_of_sets(set1, set2):
    return set1.union(set2)

def difference_of_sets(set1, set2):
    return set1.difference(set2)

def is_subset(set1, set2):
    return set1.issubset(set2)


# Function to get user input for set elements
def get_user_input_for_set():
    input_set = create_set()
    num_elements = int(input("Enter the number of elements in the set: "))
    
    for i in range(num_elements):
        element = int(input(f"Enter element {i + 1}: "))
        add_to_set(input_set, element)

    return input_set


# Example usage:
print("Enter elements for Set 1:")
set1 = get_user_input_for_set()

print("\nEnter elements for Set 2:")
set2 = get_user_input_for_set()

print("\nSet 1:", set1)
print("Set 2:", set2)

set3 = intersection_of_sets(set1, set2)
print("\nIntersection of Set 1 and Set 2:", set3)

set4 = union_of_sets(set1, set2)
print("Union of Set 1 and Set 2:", set4)


set5 = difference_of_sets(set1, set2)
print("Difference of Set 1 and Set 2:", set5)

print("Is Set 1 a subset of Set 2?", is_subset(set1, set2))

element_to_add = int(input("\nEnter element to add to Set 1: "))
add_to_set(set1, element_to_add)

element_to_remove = int(input("Enter element to remove from Set 2: "))
remove_from_set(set2, element_to_remove)

element_to_check = int(input("Enter element to check in Set 1: "))
print(f"Set 1 contains {element_to_check}: {contains_in_set(set1, element_to_check)}")

print(f"Size of Set 1: {size_of_set(set1)}")
print(f"Size of Set 2: {size_of_set(set2)}")

