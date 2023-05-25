
def stage2():
    print("Enter Password:")
    op=str(input("=>"))
    
    print("Confirm password")
    cop=str(input("=>"))
    if op==cop:
        print("Login Confirmed")

    else:
        print("Invalid password")
        stage2()

stage2()

