nums = [2,2,2,1,2,2,1,2,2,2]
l, r = 0, 0 
window = []
result = []
result_sum = []  
result_avg = []
no_of_odd = [] # This is a list for sub array of len k 
odd_counter = 0 
main_counter = 0
k = 1
while k >= 1 and k < len(nums):
    # Initialize the first window
    while r < k:
        window.append(nums[r])
        if nums[r]%2 != 0:
            odd_counter+=1
        r += 1
    # Append the initial window to the result
    result_sum.append(sum(window[:]))
    result_avg.append(sum(window[:])/len(window[:]))
    result.append(window[:])
    no_of_odd.append(odd_counter)

    # Continue with the sliding window
    while r < len(nums):
        # Slide the window to the right 
        
        if nums[r]%2 != 0:
            odd_counter+=1
        
        if nums[l]%2 == 0:
            odd_counter-=1
            
        window.append(nums[r]) # we maintain window length
        window.remove(nums[l]) # we maintain window length
    
        result.append(window[:])
        result_sum.append(sum(window[:]))
        result_avg.append(sum(window[:])/len(window[:]))
        no_of_odd.append(odd_counter)
        
        l += 1
        r += 1
    
    print(result)
    print(result_sum)
    print(result_avg)
    print(no_of_odd)
    
    for x in no_of_odd:
        if x == 2:
            main_counter+=1
    
    # Resetting to original state
    l, r = 0, 0 
    window = []
    result = []
    result_sum = []  
    result_avg = []
    no_of_odd = []
    odd_counter = 0 
    k+=1
print("main_counter",main_counter)