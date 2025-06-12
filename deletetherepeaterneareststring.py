def super_reduced_string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack) if stack else "Empty String"

input_str = input("Enter the string: ")
print(super_reduced_string(input_str))
# result = super_reduced_string(input_str)
# print(result)

# str= input("Enter the string: ").split()
# print(str)
# listofstr = []
# for i in str:
#     listofstr.append(i)
# a = len(listofstr)
# i = 0
# for string in listofstr:
#     if listofstr[i] == listofstr[i+1]:
#         listofstr.remove(string)
#         i += 1
# print(listofstr)
# print(" ".join(listofstr))

