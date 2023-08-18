#1

def indent(n):
    s = ""
    s += " " * n
    return s

#2
def is_true(s):
    return s.strip().lower() == "true"

#3
def contains_rep(s, t):
    if t == "" and s == "":
        return True
    elif t == " " and s == " ":
        return True
    elif t in s:
        return True
    else:
        return False

#4
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_char(ch, n):

    alphabet_size = len(alphabet)
    index = alphabet.index(ch)
    shifted_index = (index + n) % alphabet_size
    shifted_char = alphabet[shifted_index]
    return shifted_char

#5

def average_ch(s):
    total = 0
    len_s = len(s)
    for i in range(len_s):
        total += int(ord(s[i]))
    avg = total/len_s

    return (chr(int(avg)))

#6

def mixed_case(s):
    len_s = len(s)
    new_s = ""
    for i in range(len_s):
        c = s[i]
        if i % 2 == 0:
            new_s += c.lower()
        else:
            new_s += c.upper()
    return new_s
           
#7a

def occurences(s, t):
    count = 0
    index = 0

    while True:
        index = s.find(t, index)
        if index == -1:
            break
        count += 1
        index += 1

    return count


#7b
" 1 2  3 15 "
"1 2  3 15"
"1" "2  3 15"

def sum_numbers(s):
    list = s.split()
    new_list = []

    for chr in list:
        if chr.isnumeric():
            new_list.append(int(chr))
    return sum(new_list)

            

            

        


    return sum

#8 TRUE truE true

def intersperse(s, t):
    new_s = ""
    len_s = len(s)
    for i in range(len_s):
        c = s[i]
        if i == len_s - 1:
            new_s += c
        else:
            new_s += c + t 
    return new_s


#9

def swap_at(s, n):
    str1 = s[0:n]
    str2 = s[n:len(s)]
    return str2 + str1

#10

def evaluate(s):
    result = 0
    current_number = 0
    operator = "+"
    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in ["+", "-"]:
            if operator == "+":
                result += current_number
            else:
                result -= current_number
            operator = char
            current_number = 0

    if operator == "+":
        result += current_number
    else:
        result -= current_number

    return result


#test

def main():

    print("INDENT")
    print("3")
    print(indent(3))
    print("-1")
    print(indent(-1))

    print()

    print("IS_TRUE")
    print(is_true("True"))
    print(is_true("Sarp"))
    print(is_true("TrUE"))

    print()

    print("CONTAINS_REP")
    print(contains_rep("techttech", "t"))
    print(contains_rep("sarp", "t"))

    print()

    print("SHIFT_CHAR")
    print(shift_char('y', 3))
    print(shift_char('c', -1))

    print()

    print("AVERAGE_CH")
    print(average_ch("hello world"))
    print(average_ch("1234"))

    print()

    print("MIXED_CASE")
    print(mixed_case("hello world!"))
    print(mixed_case("s3arp5"))

    print()

    print("OCCURENCES")
    print(occurences('mississippi', 'ss'))
    print(occurences("aaaaa", "aa"))

    print()

    print("SUM_NUMBERS")
    print(sum_numbers(" 1 2  3 15 "))
    print(sum_numbers("5 6 4 23 2 a"))

    print()

    print("INTERSPERSE")
    print(intersperse('hello world', '-'))
    print(intersperse('sarp    keskin', '!'))

    print()

    print("SWAP_AT")
    print(swap_at("hello world", 5))
    print(swap_at("sarpsarp", 3))

    print()

    print("EVALUATE")
    print(evaluate("5+5"))



main()










