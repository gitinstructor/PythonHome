def myfunction(msg):
    """
    This function is 
    a pylint testing function.
    """
    msg_local = msg
    def myfunction_inner():
        return msg_local
    return myfunction_inner
MSG = "Hello, World"
aaa = myfunction(MSG)
print(aaa())
