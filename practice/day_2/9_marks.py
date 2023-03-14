# marks grade show

marks=int(input("Enter the marks obtained: "))

if marks>=90:
    print('Grade = A')
elif marks>=70 and marks<=89:
    print('Grade = B')
elif marks>=50 and marks<=69:
    print('Grade = C')
elif marks>=40 and marks<=49:
    print('Grade = D')
else:
    print('Grade = F')