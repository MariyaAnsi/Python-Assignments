# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Do not name your variable sum or use the sum() function.
h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
def computepay(h,r) :
    if h > 40 :
        return 40 * r + (h-40)*1.5*r
    elif h < 0 :
        print("Entered hours is wrong")
    else :
        return h * r
p = computepay(h, r)
print("Pay",p)