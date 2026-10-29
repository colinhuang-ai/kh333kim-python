# define a function to simulate cooking rice
def mo_phong_nau_com():
    # declare the variables
    so_bat_gao = 2 # integer
    ti_le_nuoc = 1.5 # floats
    muc_nuoc = 1.2 # float

    print("MO PHONG NAU COM") # in ra màn hình
    print(f"1. Do {so_bat_gao} bat gao.")
    print("2. Vo gao sach.")
    print("3. Cho gao vao noi com dien.")
    print("4. Kiem tra luong nuoc...")

    while muc_nuoc < ti_le_nuoc:
        print("   Nuoc chua du, them nuoc.")
        muc_nuoc = ti_le_nuoc
    print("   Nuoc da vua du.")

    print("5. Dong nap va bat noi com.")
    print("6. Cho den khi com chin.")
    print("7. De com nghi 10 phut, sau do xoi com.")
    print("Nau com xong!")


# run the simulation
if __name__ == "__main__":
    # call function to simulate cooking rice
    mo_phong_nau_com()