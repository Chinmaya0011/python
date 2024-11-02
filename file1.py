# import os
# fileName="chinu.txt"

# if os.path.exists(fileName):
#     os.remove(fileName)
#     print(f"{fileName} has been removed")
# else:
#     print(f"{fileName} does not exist.")

# with open("pratice.txt", "r") as f:
#     word = "Parala"
#     found = False
#     lineNo = 1
#     for line in f:
#         if word in line:
#          found=True
#          print(f"Found line no {lineNo}")
#          break
#         lineNo+=1

# if not found:
#     print("Not FOund")


# with open("pratice.txt","r") as f:
#     count=0
#     for x in f:
#         print(x)
#         count+=1
#     print(count)

# with open("pratice.txt","r") as f:
#  word="Linkedin"
#  count=0
#  for x in f:
#   if word in x:
#    count+=1

# print(count)

# with open("pratice.txt","r") as f:
#     word="Linkedin"
#     for x in f:
#         if word in x:
#             print(x)

with open("pratice.txt","r") as f:
    sum=0
    for x in f:
     numbers=x.split()
     for number in numbers:
        sum+=int(number)
    print(sum)
