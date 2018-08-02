def compare_ref(parameter):
    return type(parameter)
VARA = "hello"
VARB = 12
STRING_TYPE = "string"
if compare_ref(VARA) == compare_ref(STRING_TYPE) or compare_ref(VARB) == compare_ref(STRING_TYPE):
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
    
