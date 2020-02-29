import csbettingsite
import subprocess
import sys
#call "python3 start end instances"
input = " "
input = str(input)
for i in range(int(sys.argv[3])):
    input = input + "python3 csbettingsite.py " + str(int(sys.argv[1])+i) + " " +  str(sys.argv[2]) + " " + str(sys.argv[3])
    if(i != int(sys.argv[3]) - 1):
        input = input + " & "

print(input)
subprocess.run(input, shell=True)