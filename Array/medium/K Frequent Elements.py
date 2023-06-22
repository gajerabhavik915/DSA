# this algorithm is same as the leetcode for top K frequent element
# this algorithm runs for printing list that can have k or more than k element in given list(nums)

# time complexity of below algorithm will be o(n) time complexity.


# nums = [1,1,1,2,2,3,1,1,2,2,5,6,3,3]
nums=[1,2]

k = 1
dict1 = {}
# count = 1
pos = 0
l = len(nums)

if k ==1:
    while l > 0:
        if nums[pos] not in dict1.keys():
            dict1[nums[pos]] = 1
            pos += 1

        else:
            nums.pop(pos)
        l = l - 1




while l > 0 :
    if nums[pos] not in dict1.keys():
        dict1[nums[pos]] = 1
        nums.pop(pos)

    else:
        dict1[nums[pos]] = dict1[nums[pos]] + 1
        if dict1[nums[pos]] > k or dict1[nums[pos]] < k:
            nums.pop(pos)
        else:
            pos += 1
    l = l-1

print(nums)
