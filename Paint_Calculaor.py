import math
print("Welcome To Paint Calculator(- -)")
height = int(input("Enter the height of the wall"))
width = int(input("Enter the width of the wall"))
coverage = int(input("Enter the Can Coverage"))
def Paint_Calculator(h,w,cov):
    Paint = (height*width)/coverage
    print(f"You need {math.ceil(Paint)} Cans to Paint your Wall.! Thanks!")

Paint_Calculator(h = height, w= width, cov = coverage)