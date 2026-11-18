q=float(input("Enter a appllied load per unit area:"))
r=float(input("Enter a radius of the circular loaded area:"))
z=float(input("Enter a depth below the center of the loaded area :"))

s=q*(1-(1/(((r*r)/(z*z)+1))**(1.5)))
print(f"The vertical stress  is {s:.3f}")

