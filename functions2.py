# nums = [2,3,11,15,7]

# target = 9


# def two_sum(arr,t):
#     r = []
#     for i in nums:
#         for j in range(len(nums)):
#             if i + nums[j] == target:
#                 r.append(nums.index(i))
#     return r
# print(two_sum(nums,target))


# def mean(lst):
#     nums = []
#     string = []

#     for i in lst:
#         if i.isdigit():  
#             nums.append(int(i))
#         else:
#             string.append(i) 

#     average = sum(nums) / len(nums)

#     joined_string = "".join(string)

#     return [average, joined_string]


# lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
# print(mean(lst))
# lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']


# def leaderboard_sort(leaderboard, changes):
#     nwe_chenges = {}

#     for i in changes:
#         if i[-2] == "+":
#             nwe_chenges[i[:-3]] = int(i[-1])
#         elif i[-2] == "-":
#             nwe_chenges[i[:-3]] = -int(i[-1])
#     return nwe_chenges

# leaderboard =[
#     'John',
#     'Brian',
#     'Jim',
#     'Dave',
#     'Fred'
#     ]

# changes = ['Dave +1', 'Fred +4', 'Brian -1']

# print(leaderboard_sort(leaderboard,changes))

# student_ages = [12,13,18,19,18,17,20,45]

# numbers = [1,2,3,4,5,]

# nwe_arr = list(filter(lambda x: x >= 18,student_ages))

# map_arr = list(map(lambda x: x * 2 ,numbers))

# print(nwe_arr)
# print(map_arr)


dictionary = {"k":3,"s":5,"a":1}

res = sorted(dictionary.items(),key=lambda k: k[1])
print(res)

employse = [
    {"name":"BCB","sal":40},
    {"name":"ABB","sal":50},
]

res = sorted(employse,key=lambda i: i["name"])
print(res)

