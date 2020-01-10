# --- Part Two ---
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.
#
# Given this additional criterion, but still ignoring the range rule, the following are now true:
#
# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?
#
# Your puzzle input is still 152085-670283.

# def isvalid(num):
#     double = False
#     increase = True
#     for i in range(1,6):
#         if int(str(num)[i]) - int(str(num)[i-1]) == 0:
#             double = True
#         if int(str(num)[i]) - int(str(num)[i-1]) < 0:
#             increase = False
#     return double and increase
#
# total = 0
#
# for num in range(152085,670283+1):
#     if isvalid(num):
#         total +=1

#from reddit
print(len({i for i in range(152085, 670283+1)
              if sorted(str(i)) == list(str(i))
              and 2 in {str(i).count(x) for x in str(i)}}))
