num=[78,120,25,44,20,27,222,201]
print("Original list",num)
num=[x for x in num if x%2!=0]
print("List after removing Even numbers",num)