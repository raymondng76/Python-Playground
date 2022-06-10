class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print("Init method")

    def __enter__(self):
        print("Enter method")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit method")
        self.file.close()


with FileManager("test.txt", "w") as f:
    f.write("Hello World")
