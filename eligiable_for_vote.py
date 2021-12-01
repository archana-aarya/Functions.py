def voter(age):
    if age > 18:
        print("eligible")
    else:
        print("not eligible")
num=int(input('Enter the number'))
voter(num)