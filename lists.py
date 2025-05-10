def remove_elements(list_to_remove_elements):

    if len(list_to_remove_elements)>5:
        del list_to_remove_elements[5]
       
    if len(list_to_remove_elements)>4:
        del list_to_remove_elements[4]

    if len (list_to_remove_elements)>0:
        del list_to_remove_elements [0]
    return list_to_remove_elements

sample= ["Yellow", "Green", "Purple", "Red", "White", "Blue", "Magenta"]
output= remove_elements(sample)
print(output)

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements
sample = ['Red', 'Green', 'White', 'Black']
output = add_elements(sample)
print(output)

def is_empty(list_to_check):
    if len(list_to_check)==0:
        return True
    if len(list_to_check)>0:
        return False
sample = []
output = is_empty(sample)
print(output)
   
def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
       return False
List1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
List2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
output = check_lists(List1,List2)
print(output)


def list_of_lists(list_of_lists_to_modify):
  if len(list_of_lists_to_modify) == 3:
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
  return list_of_lists_to_modify

List= [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
output = list_of_lists(List)
print(output)
