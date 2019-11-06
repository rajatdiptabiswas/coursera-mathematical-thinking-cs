def transpositions(p):
  l = p.copy()
  transposes = 0
  left_correct_pos_elements = -1
  length = len(l)

  while left_correct_pos_elements < length-1:
    current_pos = left_correct_pos_elements + 1
    right_min_pos = current_pos

    while current_pos < length-1:
      current_pos += 1
      
      if l[current_pos] < l[right_min_pos]:
        right_min_pos = current_pos

    if left_correct_pos_elements+1 != right_min_pos:
      # print(f'Before swap\t-> { l }')
      l[left_correct_pos_elements+1], l[right_min_pos] = l[right_min_pos], l[left_correct_pos_elements+1]
      # print(f'After swap\t-> { l }')
      transposes += 1

    left_correct_pos_elements += 1

  return transposes


def is_even(p):
  if transpositions(p) % 2 == 0:
    return True
  else:
    return False


# # case 1
# p1 = [0,3,2,4,5,6,7,1,9,8]

# # case 2
# p2 = [8, 9, 0, 6, 7, 3, 5, 1, 2, 4]

# # case 3
# p3 = [1, 0, 3, 5, 10, 2, 6, 8, 9, 4, 7]

# print(is_even(p1)) # T
# print(is_even(p2)) # F
# print(is_even(p3)) # F