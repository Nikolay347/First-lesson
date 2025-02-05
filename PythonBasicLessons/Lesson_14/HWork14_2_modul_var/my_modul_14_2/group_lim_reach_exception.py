#my_modul_14_1/group_lim_reach_exception.py
#function with forming log file

class GroupLimitReachedException(Exception):    #Added for this HWork new class of exception from BaseException
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name
        self.log_error_data()

    def log_error_data(self):
        with open("log_exceptions.txt", "a") as file:
            file.write(f"\n".join(self.args)+ "\n")