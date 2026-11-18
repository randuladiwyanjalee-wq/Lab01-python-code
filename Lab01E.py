print("Two's complement (8-bit)")
print("------------------------")
num = int(input("Enter a decimal number (-128 to 127): "))

print(f"8-bit pattern: {num & 0xFF:08b}")
