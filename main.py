from FindMissingNumber import FindMissingNumber
from FindMissMatchCount import FindMissMatchCount
  
if __name__ == '__main__':
  # arr = [1,2,4,5,7,10]
  # k   = 2
  # fmn = FindMissingNumber(arr, k)
  # missing_value = fmn.get_missing_number()
  # print(missing_value)

  # str="xzxzx"
  str="abcdefg"
  fmm=FindMissMatchCount(str)
  print(f"Count of mismatch = {fmm.getCountOfMismatch()}")