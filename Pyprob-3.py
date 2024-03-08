#Problem 3: Palindrome
#Write a program that checks if a given string is a palindrome (reads the same backward as forward).

string = input("Enter your string:\t")

rev_string = string[::-1]
ctr=0
for i in range(len(string)):
    if (rev_string[i]!=string[i]):
        ctr +=1

if ctr!=0: 
    print("String is not Palindrome.")
else:
    print("String is Palindrome.")
