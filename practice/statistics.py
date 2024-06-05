def stats(nums:list):
    print('the minimum value is ' + str(min(nums)))
    print('the maximum value is ' + str(max(nums)))
    print('the sum of the values is ' + str(sum(nums)))
    print('the average of the values is ' + str(sum(nums)/len(nums)))

stats([1,2,3,4,5,6,7,8,9,10])