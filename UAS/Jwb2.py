try:
    num1 = 9
    num2 = 3
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred due to zero division")
except:
    print("An error occurred")
finally:
    print("This block is always executed")
