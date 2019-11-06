def is_even(p):
  length = len(p)
  start = p
  final = [x for x in range(length)]
  ans = []
  
  if set(p) == set(range(length)):
    for i in range(length-1):
      find = final[i]
      loc = start.index(find)
      if i == loc:
        continue
      ans.append((i,loc))
      # print(f'Before swapping\t-> { start }')
      start[i], start[loc] = start[loc], start[i]
      # print(f'After swapping\t-> { start }')
      # print()
    
    # print(ans)
    
    if len(ans) % 2 == 0:
      return True
    else:
      return False
  
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