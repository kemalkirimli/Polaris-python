def main():
    a=getnumber()
    lunch(a)

def getnumber():
    while True:
     n=int(input("what is n:"))
     if n>0:
        break
    return n
def lunch(n):
   while n>0:
      print(n)
      n=n-1
   print("ATEŞLE",end="!🚀")   
main()   
   
  
     