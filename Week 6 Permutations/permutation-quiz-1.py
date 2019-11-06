#!/usr/bin/env python3


def swap_string(string, x, y):
  str_list = list(string)
  str_list[x], str_list[y] = str_list[y], str_list[x]
  return ''.join(str_list)


def seq_util(start, final):
  ans = []
  length = len(start)

  for i in range(length-1):
    find = final[i]
    loc = start.index(find)
    if i == loc:
      continue
    ans.append((i,loc))
    print(f'Before swapping\t-> { start }')
    start = swap_string(start, i, loc)
    print(f'After swapping\t-> { start }')
    print()
    
  return ans


def sequence():
  # return [( , ), ( , ),...,( , )]
  # return [(0, 1), (1, 3), (4, 5)]
  return seq_util('MARINE', 'AIRMEN')


print(sequence())