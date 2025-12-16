def main():
    a=getnumber()
    sum(a)

def getnumber():
    while True:
     n=int(input("what is n:"))
     if n>0:
        break
    return n
def sum(n):
   b=0
   while n>0:
      b+=n
      n-=1
   print(f"sum={b}") 
main()      