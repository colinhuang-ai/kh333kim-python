# Define function
# y = f(x)
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# test with 3 test case
mark1 = 7
xl1 = xep_loai(mark1)
print(xl1)

# tuong minh
mark2 = 9.5
xl2 = xep_loai(mark2)
print(xl2)

# test case with mark 6
mark3 = 6
print(xep_loai(mark3))

# ko tuong minh, chaining
print(xep_loai(4.9))