def first(number):
    number_str = str(number)
    number_str = number_str.replace("0", "")
    number_str = number_str.replace(".", "")
    result_sum = 0
    for digit in number_str:
        result_sum += int(digit)
    exponent = len(number_str)
    res_sum = result_sum / 10
    return res_sum, exponent

def second(s2, decimal_number):
    result_s2 = ""
    if "." in decimal_number:
        for i in range(len(s2)):
            if i % 2 == 0:
                result_s2 += s2[i]
    else:
        for i in range(len(s2)):
            if i % 2 != 0:
                result_s2 += s2[i]
    return result_s2


input_num = input("Enter the numerical value: ")
input_name = input("Enter the character value: ")

res_sum, exponent = first(input_num)
result_s2 = second(input_name, str(input_num))
if "." in input_num:
    password = str(res_sum) + "e-" +str(exponent) +"@"+result_s2
else:
    password = str(res_sum) + "e+" +str(exponent) +"@"+result_s2

password = password.replace("0", "zero")
password = password.replace("1", "one")
password = password.replace("2", "two")
password = password.replace("3", "three")
password = password.replace("4", "four")
password = password.replace("5", "five")
password = password.replace("6", "six")
password = password.replace("7", "seven")
password = password.replace("8", "eight")
password = password.replace("9", "nine")

print(password)
