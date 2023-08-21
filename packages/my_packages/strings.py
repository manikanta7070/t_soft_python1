#Write a program to determine the given number is palindrome number or not using Functions
N=eval(input("Enter a number N: ")) 
temp0=N
def palindrome(N):
      s=0
      while N>0:
            r=N%10
            s=s*10+r
            N=N//10
      return s

#Write a program to determine the given number is perfect number or not using Functions
N1=eval(input("Enter a number N1: "))
temp1=N1
def perfect_number(N1):
      s=0
      while N1>0:
            r=N1%10
            s=s+(r*r*r)
            N1=N1//10
      return s

#Write a program to determine the given number is Armstrong number or not using Functions
N2=eval(input("Enter a number N2: "))
def armstrong(N2):
      s=0
      i=1
      while i<=N2:
            r=N2%i
            if r==0:
                  s=s+i
            i+=1
      return s
