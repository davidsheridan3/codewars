def whatday(num):
  if num >=1 and num <= 7:
      days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
      return days[num - 1] # to allow for 1-7 input, as Sunday = [0]
  else:
        return "Wrong, please enter a number between 1 and 7"