import os
import tempfile

print(tempfile.gettempdir())
print(tempfile.gettempprefix())

with tempfile.TemporaryFile("w+") as tfp:
    tfp.write("Some temp data")
    tfp.seek(0)
    print(tfp.read())


with tempfile.TemporaryDirectory() as tdp:
    filepath = os.path.join(tdp, "tempfile.txt")
    print(filepath)

    with open(filepath, "w+") as tfp:
        tfp.write("Temp file in temp directory")
        tfp.seek(0)
        print(tfp.read())
