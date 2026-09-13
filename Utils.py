def customize_drone() -> None:
    change_hat(Hats.Wizard_Hat)
 
def no_op():
    pass   
 
def error_NYI(feature: str = "") -> None:
    print(feature)
    raise(500, "Not Yet Implemented")  

def raise(code: int, msg: str):
    print("::Exception Raised::")
    quick_print("ErrorCode: " + str(code))
    quick_print("Message: " + msg)
    while True:
        pass
