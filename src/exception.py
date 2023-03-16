import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    fname = exc_tb.tb_frame.f_code.co_filename
    error_message = f"error occured at python script name [{fname}] at line {exc_tb.tb_lineno} with error message {str(error)}"

    return error_message


class CustomeException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
