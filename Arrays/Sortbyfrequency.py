def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    return frequency

def sort_arr_by_frequency(arr):
    frequency = count_frequency(arr)
    freq_list  = []
    for key, value in frequency.items():
        freq_list.append((key, value))
    for i in range(0, len(freq_list)):
        swapped = False
        for j in range(0, len(freq_list)-i-1):
            if freq_list[j][1] < freq_list[j+1][1]:
                freq_list[j], freq_list[j+1] = freq_list[j+1], freq_list[j]
                swapped = True
            if freq_list[j][1] == freq_list[j+1][1]:
                if freq_list[j][0] > freq_list[j+1][0]:
                    freq_list[j], freq_list[j+1] = freq_list[j+1], freq_list[j]
                    swapped = True
        if not swapped:
            break
    sorted_arr = []
    for element, count in freq_list:
        sorted_arr.extend([element]*count)
    return sorted_arr
arr = [10,20,30,20,30,10,20,30,10, 10,20,30,30,30]
print(sort_arr_by_frequency(arr))


#Method 2
from collections import Counter
def sort_by_freq(arr):
    freq = Counter(arr)
    sorted_arr = sorted(arr, key = lambda x: (-freq[x], x))
    return sorted_arr
arr1 = [10,20,30,20,30,10,20,30,10,20,30,10]
print(sort_by_freq(arr1))