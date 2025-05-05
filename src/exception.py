import sys


# The funciton is about error message details:


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # this exc_tb will all the info on which line error has occured, what is the cause of error:
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message= "Error occured inpython script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
        
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): # constractor
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    
    

