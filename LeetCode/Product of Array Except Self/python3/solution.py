def productExceptSelf(self, nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

#     nums = [ 1 , 2 , 3 , 4 ]
#     For i = 2 (the 3):

#     [ 1   2 ]  3  [ 4 ]
#      \_____/   ^   \_/
#       left     |  right
#       = 2    skip  = 4

#     answer[2] = 2 × 4 = 8

# Pass 1: left → right (prefix)

# prefix holds the product of everything seen so far. At each step it stores first, then multiplies, so nums[i] itself is never included in res[i].

#  i  | prefix (before) | res[i] = prefix | prefix *= nums[i]
# ----+-----------------+-----------------+-------------------
#  0  |       1         |       1         |   1 × 1 = 1
#  1  |       1         |       1         |   1 × 2 = 2
#  2  |       2         |       2         |   2 × 3 = 6
#  3  |       6         |       6         |   6 × 4 = 24

# res = [ 1,  1,  2,  6 ]
#         │   │   │   └── 1×2×3   (everything left of index 3)
#         │   │   └────── 1×2     (everything left of index 2)
#         │   └────────── 1       (everything left of index 1)
#         └────────────── nothing on the left → 1
# Pass 2: right → left (postfix)

# range(len(nums)-1, -1, -1) means start at the last index, go down to 0, and step by -1.

# postfix holds the product of everything to the right. The code multiplies it into what’s already in res[i], again before including nums[i].

#  i  | postfix (before) | res[i] *= postfix | postfix *= nums[i]
# ----+------------------+-------------------+--------------------
#  3  |        1         |   6 × 1  = 6      |   1 × 4  = 4
#  2  |        4         |   2 × 4  = 8      |   4 × 3  = 12
#  1  |       12         |   1 × 12 = 12     |  12 × 2  = 24
#  0  |       24         |   1 × 24 = 24     |  24 × 1  = 24

# res = [ 24, 12, 8, 6 ]
# Both passes combined
#         left (pass 1)    right (pass 2)    result
# i=0:    (none) = 1   ×   2×3×4 = 24    =   24
# i=1:    1            ×   3×4   = 12    =   12
# i=2:    1×2    = 2   ×   4             =    8
# i=3:    1×2×3  = 6   ×   (none) = 1    =    6

# You can check it: 24 = 2×3×4, 12 = 1×3×4, 8 = 1×2×4, 6 = 1×2×3. ✓
