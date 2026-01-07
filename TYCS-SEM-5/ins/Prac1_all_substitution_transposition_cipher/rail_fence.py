##Rail Fence with 2 layrers

# string=input("Enter a string : ")
# def RailFence(txt):
#     result=""
#     for i in range (len(string)):
#         if (i%2==0):
#             result+=string[i]
#     for i in range (len(string)):
#         if (i%2!=0):
#             result+=string[i]
#     return result
# print("Rail Fence Output : ",RailFence(string))




#Rail Fence with multiple layers
def RailFence(txt, layers):
    result = [''] * layers
    direction = 1 
    layer = 0

    for char in txt:
        result[layer] += char
        layer += direction

        if layer == 0 or layer == layers - 1:
            direction *= -1 

    return ''.join(result)

layers = int(input("Enter number of layers: "))
string = input("Enter a string: ")
if layers < 1:
    print("Number of layers must be at least 1.")
else:
    if layers == 1:
        print("Rail Fence Output: ", string)
    else:
        print("Rail Fence Multi Layer Output: ", RailFence(string, layers))   
