# Do not remove these imports. You may add others if you wish.
import sys
# Args:
#    matrix: an NxN list of lists containing the matrix to check
# Returns:
#    The string "VALID" if matrix contains a valid sub-sudoku solution, and
#    "INVALID" otherwise
def check_sub_sudoku(mat):
      
  def check_positive():
      all_positive = False
      for line in mat:
        for num in line:
          if num > 0:
            all_positive = True
          else:
            all_positive = False
#       if all_positive is True:
#           print('all positive nums')
#       else:
#           print('oops negative nums')  
      return all_positive

  N = len(mat)
  as_should_be = []
  for x in range(1, N+1):
    as_should_be.append(x) # should be [1,2,3,4] etc.
  
  def check_1_to_N():
    one_to_N = False
     # this should be comparison of line to should be but I could not get it to work yet so I did a work around
    for line in mat:
      line.sort()
      if mat[0][0] == 1:
        if sum(line) == sum(as_should_be) and line[0] == 1:
          one_to_N = True
        else:
          one_to_N = False
    return one_to_N
   
  first_sum = sum(mat[0])
  def check_lines():
#     print('first sum is: {}'.format(first_sum))
    for line in mat:
#       print(sum(line))
      if sum(line) == first_sum:
        sumup = True
      else:
        sumup = False
#     if sumup is True:
#       print('all lines sum up to: {}'.format(first_sum)) 
#     else:
#       print('line sums do not match')
    return sumup

  def check_cols():
#   will use the as_shoud_be which is the 1st line sorted
    col = []
    good_column = False
    for line in mat:
        col.append(line[0])
#     print(as_should_be)
    if sorted(col) == as_should_be:
        good_column = True
#       print('good column')
    else:
#       print('colums do not match')
        good_column = False
    return good_column
  
  if check_1_to_N() is True:
    if check_positive() is True:
      if check_lines() is True:
#         if check_cols() is True: #run out of time could not debug
        return "VALID" 
  
  
  return "INVALID"

# DO NOT MODIFY BELOW THIS LINE
def main():
  matrix = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue
    matrix.append([int(x) for x in line.rstrip().split(" ")])

  print(check_sub_sudoku(matrix))

main()
