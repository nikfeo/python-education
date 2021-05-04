# 1. Hello, World.
print("Hello, World!")

# =================================================================================================

# 2. Variables and Types
mystring = "hello"
myfloat = 10.0
myint = 20
print(mystring)
print(myfloat)
print(myint)

# =================================================================================================

# 3. Lists
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append('world')

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# =================================================================================================

# 4. Basic Operators
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# =================================================================================================

# 5. String Formatting
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# =================================================================================================

# 6. Basic String Operations
s = "Strings are awesome!"

print("Length of s = %d" % len(s))
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
print("Split the words of the string: %s" % s.split(" "))

# =================================================================================================

# 7. Conditions
number = 20
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
if not second_number:
    print("6")

# =================================================================================================

# 8. Loops
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if not number % 2:
        print(number)
    elif number == 237:
        break


# =================================================================================================

# 9.1. Functions
def list_benefits():
    benefits_list = ["More organized code",
                     "More readable code",
                     "Easier code reuse",
                     "Allowing programmers to share and connect code together"]
    return benefits_list


def build_sentence(benefit):
    string_with_benefit = "%s is a benefit of functions!" % benefit
    return string_with_benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()


# =================================================================================================

# 9.2. Multiple_Function_Arguments
def foo(a, b, c, *some_args):
    return len(some_args)


def bar(a, b, c, **spec_args):
    return spec_args["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")

# =================================================================================================

# 11. Dictionaries
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
phonebook.pop("Jill")
phonebook["Jake"] = 938273443

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# =================================================================================================

# 12. Sets
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

a_set = set(a)
b_set = set(b)

print(a_set.difference(b_set))

# =================================================================================================

# 14. Modules and Packages
import re

members_list_with_word_find = []
for member in dir(re):
    if 'find' in member:
        members_list_with_word_find.append(member)

print(members_list_with_word_find)

# =================================================================================================
