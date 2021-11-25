def check_string(string):
    def string_info(string):
        nums = []
        letters = []    
        for symbol in string:
            try:
                nums.append(int(symbol))
            except:
                letters.append(symbol)
        return (nums, letters)

    str_info = string_info(string)
    if len(string) >= 30 and len(string)<=50:
        print("Len string is ", len(string))
        print("Number of nums: ", len(str_info[0]))
        print("Number of letters: ", len(str_info[1]))
    elif len(string) < 30:
        print("Sum of nums: ", sum(str_info[0]))
        print("String of letters: ", "".join(str_info[1]))
    else:
        print("String fail")

check_string(input("Enter the string"))
