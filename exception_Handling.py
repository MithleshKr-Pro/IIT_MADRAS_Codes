try:
    f = open('M:\Mith_Programs\IITM_Python\gr5.py','r')
    a = int(input())
    b = int (input())
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Invalid statement")
except Exception as e:
    print(e,"Something went wrong")
finally:
    if 'f' in locals() and f:
        f.close()
        print("executed")
