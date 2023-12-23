import sys

# Input values from console
val1 = str(sys.argv[1])
val2 = int(sys.argv[2])
val3 = str(sys.argv[3])

def logicalOpr():
   # print("Greather than:", val1 > val2)
   # print("Less than:", val1 <= val3)
    print("logical opr:", (val1 == val3) or (val1 == val2))

logicalOpr()