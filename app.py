# largest name find an array

def find_longest_string(strings):
    longest = ""
    for string in strings:
        if(len(string) > len(longest)):
            longest = string
    return longest


print("find largest string an array:",find_longest_string(["Tanvir","Shakib","jamal","Tanvir Hossain","kamal uddin"]))

# array contains check unique number an array 

def unique_number_array(numbers):
    unique_number = []
    for number  in numbers : 
        if number not in unique_number: 
            unique_number.append(number)
    return unique_number


print("unique Number an array",unique_number_array([10,20,30,40,20,40,40,50,60]))

# extract vowels string 

def extract_vowels(strings):
    vowels = "aeiouAEIOU"
    extract = ''
    for string in strings:
        if string in vowels:
            extract = extract + string
    return extract



print("extract vowels of a string",extract_vowels("Tanvir hossainA "));
