try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    result=num1/num2
    print("result is ",result)
except ValueError:
   print("enter a interger value")
except ZeroDivisionError:
   print("number two expect is zero")
except:
   print("wrong input")
else:
   print("no except")
finally:
   print("this block will execute no matter what")



