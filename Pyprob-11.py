#Problem 11: Integer to Binary
#Write a program that converts an integer number to its binary representation.

def int_to_bin(num):
    if num == 0:
        return '0'
    
    binary_num = ''
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num //= 2 #floor division; which means that it will give you the floor not the nearest value (13//2 = 6 not 7)
    
    return binary_num

int_num = int(input("Enter an integer number: "))
binary_num = int_to_bin(int_num)
print("Binary representation:", binary_num)
