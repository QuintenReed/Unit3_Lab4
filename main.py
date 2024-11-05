# Quinten Reed
# U3L4
# Binary Search

def binary_search(target, checklist, pointer=0):
  position = 0
  
  if len(checklist) == 1 and checklist[0] != target:
    return

  elif checklist[int(len(checklist)/2)] < target:
    position = binary_search(target, checklist[int(len(checklist)/2)+1:], pointer + int(len(checklist)/2) + 1)

  elif checklist[int(len(checklist)/2)] > target:
    position = binary_search(target, checklist[:int(len(checklist)/2)+1], pointer)
  
  elif checklist[int(len(checklist)/2)] == target:
    return pointer + int(len(checklist)/2)

  return position

def main():
  nums = [1,2,3,4,5,6,7,8,9]

  test1 = binary_search(2, nums)
  print("\n\nTest 1 - search for 2")
  print(f"Your returned index: {test1}")
  print(f"Test passed? {test1 == 1}\n\n")

  test2 = binary_search(7, nums)
  print("Test 2 - search for 7")
  print(f"Your returned index: {test2}")
  print(f"Test passed? {test2 == 6}\n\n")

  test3 = binary_search(9, nums)
  print("Test 3 - search for 9")
  print(f"Your returned index: {test3}")
  print(f"Test passed? {test3 == 8}\n\n")
  
  test4 = binary_search(99, nums)
  print("Test 4 - number doesn't exist")
  print(f"Your returned index: {test4}")
  print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
  main()