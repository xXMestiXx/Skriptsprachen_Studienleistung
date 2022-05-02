from re import I

string = "This is a test"
print(string)

string_list = string.split()
print('_'.join(string_list))


s1 = "Hello, World"
s1_l = s1.split()
s1_1= str(s1_l[0])

def string_backwards(x):
    return x[::-1]

output_string = string_backwards(s1_1)
print(output_string)
