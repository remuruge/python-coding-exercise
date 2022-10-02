class FindMissingNumber:

  def __init__(self, arr, k):
    self.position=0
    self.input_arr=arr
    self.n_time=k

  # def __call__(self, arr, k):
  #   self.position=0
  #   self.input_arr=arr
  #   self.n_time=k
  
  def get_missing_number_On(self):
    # print(len(self.input_arr))
    if len(self.input_arr) <= 1:
      print('check len')
      return None
    # #assume it is sorted
    counter = 0
    i = 0
    while i < len(self.input_arr)-1:
      print(f"{self.input_arr[i]} - {counter}")
      if (self.input_arr[i+1]-self.input_arr[i]) > 1:
        counter=counter+1
        if counter == self.n_time:
          return self.input_arr[i] + 1
      i=i+1    
    return None
    # logic becomes o(n^2) is the interval has more than 1 missing value

  # Need to fix this
  def get_missing_number(self):
    i = 0
    counter = 0
    sum_actual_value = 0
    while i < len(self.input_arr)-1:
      sum_actual_value=self.input_arr[i]+sum_actual_value
      i=i+1
      diff=self.input_arr[i+1]-self.input_arr[i]
      if (diff > 1):
        counter=counter+diff
        if counter <= self.n_time:
          break
    sum_expected_value=((i+diff +1) * (i+diff+2))/2
    return int(sum_expected_value - sum_actual_value)