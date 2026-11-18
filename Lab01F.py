import math 
print("Floating point comparison")
print("------------------------------")
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

sum=a+b
diff=abs(sum-c)

print(f"a+b = {sum:.20f}")
print(f"|a+b-c| = {diff:.3e}")
print(f"a+b == c : {sum == c}")
print(f"math.isclose(a + b, c) : {math.isclose(sum, c)}")

      

      

      
