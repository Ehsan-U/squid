import subprocess
import re


def install():
    subprocess.call("apt update",shell=True)
    subprocess.call("apt install squid -y",shell=True)
    print("\n Installtion Completed!")
def check_status():
    try:
        squid_status = subprocess.check_output("service squid status",shell=True)

        result = re.search(r": active",str(squid_status))
        if result:
            print("Squid is running now..")
        else:
            print("error")
    except subprocess.CalledProcessError:

        print('Squid has been stopped running')

def start():

    subprocess.call("service squid start",shell=True)
    print(check_status())

def stop():

    subprocess.call("service squid stop",shell=True)
    print(check_status())

def find_file():

    print("\nPath > /etc/squid/squid.conf\nYou can change it according to your requirements.\n\ne.g\nnano <path>      (for opening file)\n")


print("\n1 > for installing squid\n2 > for checking status \n3 > for starting squid service\n4 > for stop squid service\n5 > find squid config file\n")
inp1 = int(input("Enter your choice:"))
if inp1 == 1:
    install()
elif inp1 == 2:
    check_status()
elif inp1 == 3:
    start()
elif inp1 == 4:
    stop()
elif inp1 == 5:
    find_file()
