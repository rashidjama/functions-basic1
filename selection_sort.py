def selection_sort(nums_list):
  for i in range(len(nums_list)):
    min = nums_list[i]
    min_location = i
    for j in range(i+1, len(nums_list)):
      if nums_list[j] < min:
        min = nums_list[j]
        min_location = j
    nums_list[min_location] = nums_list[i]
    nums_list[i] = min
  return nums_list
print(selection_sort([50,32,2,-77,-25]))