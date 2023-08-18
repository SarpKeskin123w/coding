
def product(l):
    product = 1
    for i in l:
        product = product * i
    return product

def maximum(l):
    max_value = l[0]
    max_index = 0
    for i in range(len(l)):
        if l[i] > max_value:
            max_value = l[i]
            max_index = i
    return max_value, max_index #This function doesnt work i couldnt do it


def are_you_sorted(l):
    len_l = len(l)
    for i in range(len_l - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def number_negative(l):
    count = 0
    for num in l:
        if num < 0:
            count += 1
    return count

def ones_digits(l):
    ones = []
    for num in l:
        ones_digit = num % 10
        ones.append(ones_digit)
    return ones

def lengths_of(l):
    lengths = []
    for string in l:
        length = len(string)
        lengths.append(length)
    return lengths

def filter_upper(l):
    filtered_list = []
    for string in l:
        if string.isupper() and string == string.upper():
            filtered_list.append(string)
    return filtered_list

def list_all(l):
    return all(l)


def main():
    
    print("product:", product([2, 3, 4])) 
 

    print("sorted:", are_you_sorted([1, 2, 3, 4, 5])) 
    print("sorted:", are_you_sorted([5, 2, 9, 1, 7]))

 
    print("negative count:", number_negative([-1, 2, -3, 4, -5])) 

    
    print("ones digits:", ones_digits([23, 45, 67]))

 
    print("lengths:", lengths_of(["apple", "banana", "carrot"]))


    print("filtered:", filter_upper(["APPLE", "banana", "CARROT"])) 


    print("all true:", list_all([True, True, True]))  
    print("all true:", list_all([True, False, True])) 

main()