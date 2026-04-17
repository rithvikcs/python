def reverse_string(s:str):
    return " ".join(s.split(" ")[::-1])

s = "welcome to the jungle"
print(reverse_string(s))
