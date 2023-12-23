
# test while loop
a = 11111111111111111111111111
b = 111111111111111110 + 1

#while a is b:
if a is b:
    print("output")
#done

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)