def increment(num):
    return num+1

def reset_funtion():
    global increment
    addition=50
    increment=lambda num:num+addition

print(increment(5))
reset_funtion()
print(increment(5))