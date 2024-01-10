"""
ID: raytang1
LANG: PYTHON3
TASK: test
"""

with open('test.in', 'r') as infile:
    nums = infile.readline()
    nums = nums.split(" ")
    nums = [int(x) for x in nums]

with open('test.out', 'w') as outfile:
    outfile.writelines(str(nums[0] + nums[1]))
    outfile.writelines("\n")