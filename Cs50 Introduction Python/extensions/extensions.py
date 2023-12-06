
# this is my input
file_w =input ("File name: ")

# I'm try to find lower case
file = file_w.lower()

if ".gif" in file:
    print("image/gif")
elif ".jpg" in file:
    print("image/jpg")
elif ".jpeg" in file:
    print("image/jpeg")
elif ".pdf" in file:
    print("application/pdf")
elif ".png" in file:
    print("image/png")
elif ".text" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream ")



