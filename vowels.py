word=str(input("Enter the string:"))
print("The original string is:" +word)
print("The vowles are:",end=" ")
for i in word:
    if i in 'aeiouAEIOU':
        print([i],end=" ")