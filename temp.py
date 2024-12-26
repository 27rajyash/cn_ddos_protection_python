def bubble_sort():
    temp_list = [i for i in range(1000, -1, -1)]
    print(temp_list)
    n = len(temp_list)

    for i in range(n):
        for j in range(n-i-1):
            if temp_list[j] > temp_list[j+1]:
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                swapped = True

        if (swapped == False):
            break
    
    return temp_list

temp_list = bubble_sort()
print(temp_list)