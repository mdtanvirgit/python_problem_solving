

print("python code is running")

fruits = ["Mango","Banana","Orange"];

for x in fruits: 
  print(x);


def my_function(a,b) : 

  if b > a:
    print("b is greater than a")
  else:
    print("a is greater then b")

  
my_function(40,30)

print(type(True));

# find largest number an array 

def find_largest_number(numbers):
  largest = numbers[0];
  for number in numbers : 
    if number>largest: 
        largest = number
  return largest;


print(find_largest_number([10,20,30,40,50]))


# reverse an array 

def reverse_sentence(sentence):
  word = sentence.split();
  word.reverse()
  reverse_sentences = ' '.join(word);
  return reverse_sentences;


print(reverse_sentence('My Name is Tanvir Hossain'));


#  contains only the strings that have a length greater than 5.

def filter_long_string(stringArray): 
  log_string = [];
  for string in stringArray : 
    if len(string) > 5 : 
      log_string.append(string)
  return log_string


print("filter long string greater then 5: ",filter_long_string(["Tanvir","Hossain","jamal","kamal","mokkol"]));


# contain only even integer number 

def filter_even_number(numbers): 
  even_number = []
  for number in numbers:
    if number % 2 == 0:
      even_number.append(number)
  return even_number;



print("even Number:",filter_even_number([10,20,31,45,55]));


# sum array number

def sum_numbers(numbers):
  total = 0
  for number in numbers : 
    total = total + number
  return total


print("sum numbers ",sum_numbers([10,20,30,40,50]));

# vowel number count 

def count_vowel(string):
  vowel = 'aeiou'
  count = 0
  for letter in string : 
    if letter.lower() in vowel:
      count = count + 1
  return count


print("Number of Vowels:",count_vowel("Hello World"));
