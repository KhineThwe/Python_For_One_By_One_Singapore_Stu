#Customer exception class
class CustomException(Exception):
    pass

#function
def raise_custom_exception():
    raise CustomException("This is a custom exception")

try:
    raise_custom_exception()
except CustomException as e:
    print("Caught custom exceptin: ",str(e))