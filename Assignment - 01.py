#Question - 01

answer = (60+(10**2)/4*7)-134.25
print("Question 1 :")
print(answer)

#Question - 02

str_1 = "Hello"
print(str_1[1:-1])

str_1 = "java"
print(str_1[1:-1])

str_1 = "coding"
print("Question 2 :")
print(str_1[1:-1])

#Question - 03
print("Question 3 :")

a = [1,2,3]
b = [4,5,6]
print(a[-2],b[-2])
a = [7,7]
b = [3,8,0]
print(a[-2],b[-2])
a = [5,2,9,0,2,4]
b = [1,4,5,1]
print(a[-2],b[-2])

#Question - 04

nested_list = [1, 2, [3, 4, 'hello']]
nested_list[2][2] = "goodbye"
print("Question 4 :")
print(nested_list)

#Question - 05

my_list = [1, 2, 2, 33, 4, 411, 22, 3, 3, 2]
my_sorted_list=set(my_list)
print("Question 5 :")
print(my_sorted_list)

#Question - 06

my_file = open("test.txt")
text = my_file.read()
my_file.close()

print("Question 6 :")
print(len(text))

#Question - 07

l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
l_one[2][0] >= l_two[2]['k1']
answer=bool(l_one[2][0] >= l_two[2]['k1'])
print("Question 7 :")
print(answer)

#Question - 08

d = {"k1": {'nest_key': ['this is deep', ['hello']]}}
the_key = d["k1"]
my_key = the_key['nest_key']
print("Question 8 :")
print(my_key[1][0])
