#Problem 30: Pascal's Triangle
#Write a program that generates Pascal's Triangle up to a specified number of rows.

def pascal_traingle(num):
    triangle =[]

    for i in range(num):
        row = [1] * (i+1)

        for j in range(1,i):
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]
            print(row) # to check on each row how it is incremented
        triangle.append(row)

    return triangle

def print_pascalT(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))


def print_pascalStar(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 4))

num_rows = int(input("Enter the number of rows: "))
pascals_triangle = pascal_traingle(num_rows)

print_pascalT(pascals_triangle)
print("*************************************")
print_pascalStar(pascals_triangle)
