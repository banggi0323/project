def calculate_tax(income):
    if (income >= 0 and income <= 12000000):
        return income * 0.06
    elif (income > 12000000 and income <= 46000000 ):
        return income * 0.15
    elif (income > 46000000 and income <= 88000000 ):
        return income * 0.24
    elif (income > 88000000 and income <= 150000000 ):
        return income * 0.35
    elif (income > 150000000 and income <= 300000000 ):
        return income * 0.38
    elif (income > 300000000 and income <= 500000000 ):
        return income * 0.40
    elif (income > 500000000 ):
        return income * 0.42

while (True):  
    income = int(input("수입입력: "))
    tax = calculate_tax(income)
    if (tax > 0) :
        print("세금 : ", tax)
    if (income == 0):
        print("종료")
        break
