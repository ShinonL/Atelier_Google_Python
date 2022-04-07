import datetime

def compute_c(cnp):
    number = "279146358279"
    product_list = [int(x) * int(y) for x, y in zip(number, cnp)]
    rest = sum(product_list) % 11
    return 1 if rest == 10 else rest

def is_cnp_valid(cnp):
    if len(cnp) != 13:
        return False

    if cnp[0] == 0:
        return False

    date = cnp[1:3] + '/' + cnp[3:5] + '/' + cnp[5:7]
    try: 
        datetime.datetime.strptime(date, "%y/%m/%d")
    except ValueError:
        return False

    if not "01" <= cnp[7:9] <= "52":
        return False

    if not "001" <= cnp[9:12] <= "999":
        return False

    if int(cnp[12]) != compute_c(cnp[:-1]):
        return False

    return True

cnp = input("Enter a CNP: ")
if is_cnp_valid(cnp):
    print("The CNP is valid")
else:
    print("The CNP is NOT valid")