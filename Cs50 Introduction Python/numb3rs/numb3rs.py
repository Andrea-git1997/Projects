import re
import sys


def main():
    ip = validate(input("IPv4 Address: "))
    print(ip)


def validate(ip):
    ip.replace("IPv4 Address:","")
    #print(f"ip is = {ip}" )
    # (25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d|\d)
    # 25[0-5] 250-255 o 2[0-4]\d 240-249 o |1\d{2}|[1-9]?\d 100-199 o 0-99 |\d 0-9
    match = re.match(r"^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d|\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d|\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d|\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d|\d))$", ip)

    if match:
        return "True"
    else:
        return "False"



...


if __name__ == "__main__":
    main()

# python numb3rs.py
