class ContextManager:
    def __init__(self):
        # Constructor will always be called first
        print("Init method")

    def __enter__(self):
        # This method will be called when the with statement is used and before called the statements in the with block
        print("Enter method")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This method will be called when the with statement is used and after called the statements in the with block
        print("Exit method")


with ContextManager() as cm:
    print("Inside with block")
