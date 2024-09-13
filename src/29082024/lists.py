from operator import truediv

my_list=[1,2,4,6,9,'harsha','krishna','harsha']

print(my_list)
print(len(my_list))

for a in my_list:
    print('value of list in index',a)

# Re assigning list values
my_list=['orange','banana',10]
for a in my_list:
    print('updated list values:',a)

# Appending a new value to end of list
my_list.append('grape')
print(my_list)

# extending a list
my_list.extend(['pine','cashew','cashew'])
print(my_list)

# insert in between of list

my_list.insert(2,'lemon')
print(my_list)

# insert in -index

my_list.insert(-1,'cucumber')
print(my_list)

# remove element
my_list.remove(my_list[1])
print(my_list)
my_list.remove('cashew')

# clearing list
#my_list.clear()
#print(my_list)

# sort list by ascending or descending
list1=[2,1,9,4,0,3]
print(list1)
#list1.sort()
#print(list1)
list1.sort(reverse=False)
print(list1)

# pop removes last item

