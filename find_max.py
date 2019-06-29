def find_max(a_list):
    if a_list == False:
        return 0
    count = 0
    max_number = 0    
    for number in a_list:
        if number > max_number:
            max_number = number
        
    return max_number


print(find_max([1, 2, 3]), '為最大值')                
print(find_max([1, -1, -5]), '為最大值')
print(find_max([]), '為最大值') 
 