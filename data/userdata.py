import base64
import getpass

pb64b = base64.b64encode(getpass.getpass().encode("ascii"))
passwordb64 = pb64b.decode("ascii")

username = "root"
password = base64.b64decode(passwordb64).decode("ascii")

print(f"{username} | {password}")