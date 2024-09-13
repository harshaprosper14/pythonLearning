original_list=[1,2,2,4]
unique_list=[]
duplicate_counter=2
for a in original_list:
    freq=original_list.count(a)
    if freq==1 and a not in unique_list:
        unique_list.append(a)
#print(unique_list)
print(len(unique_list))
for b in unique_list:
    print(b,',')