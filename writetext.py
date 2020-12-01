file1 = open("test.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.close()

file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.readlines())
print
file1.close()
