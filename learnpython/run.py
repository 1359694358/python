import os


pipeline = os.popen("python37 ./pyunittest/PyUnit.py")
print(pipeline.read())