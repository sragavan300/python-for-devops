import sys

# Input values from console
val1 = str(sys.argv[1])
val2 = int(sys.argv[2])
val3 = str(sys.argv[3])

def comparisonOpr(val1, val2):
   # print("Greather than:", val1 > val2)
   # print("Less than:", val1 <= val3)
    print("Greather than or equal to:", val1 == val3)

comparisonOpr(val1, val2)