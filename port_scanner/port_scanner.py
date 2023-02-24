import socket
import sys

s=socket.socket()
def static_scan():
    target = "www.google.com"
    ip =  socket.gethostbyname(target)
    print("Starting the scan on the target: ", ip)

    port= 80
    print("")

    def scan(port):
        try:
            s.connect((ip, port))
            s.settimeout(0.1)
            return True
        except:
            return False

    if scan(port):
        print("Port", port, "is open.")
    else:
        print("Port",port, "is  closed.")

def user_input_scan():
    target = input("Enter an url which you want to scan: ")
    ip =  socket.gethostbyname(target)
    print("Starting the scan on the target: ", ip)

    port= int(input("Which port do you want to scan: "))
    print("")

    def port_scan(port):
        try:
            s.connect((ip, port))
            s.settimeout(0.1)
            return True
        except:
            return False

    if port_scan(port):
        print("Port", port, "is open.")
    else:
        print("Port",port, "is  closed.")

def specific_port():
    target = input("Enter the url what you want to scan: ")
    ip =  socket.gethostbyname(target)
    print("Starting the scan on the target: ", ip)
    port_list = list(map(int, input("Enter the list of ports (comma_separated): ").split(",")))
    
    for i in port_list:
        def scan():
            try:
                s.connect((ip, i))
                s.settimeout(0.1)
                return True
            except:
                return False

        if scan() == True:
            print("Port", i, "is open.")
        else:
            print("Port",i, "is  closed.")

def p_range():
    opened_number = 0
    closed_number = 0

    name = input("Enter the url what you want to scan: ")
    ip =  socket.gethostbyname(name)
    print("Starting the scan on the target: ", ip)
    ports_range = input("Enter the range of the ports using ('-' separated): ")
    port_list = ports_range.split('-')
    for i in range(int(port_list[0]), int(port_list[1])+1):
        def port_scan():
            try:
                s.connect((ip, i))
                s.settimeout(0.1)
                return True
            except:
                return False

        if port_scan() == True:
            print("Port", i, "is open.")
            opened_number += 1
        else:
            print("Port",i, "is  closed.")
            closed_number +=1 

    print("The open ports are {opened_number} and closed ports are {closed_number}")


def all():
    opened_number = 0
    closed_number = 0
    name = input("Enter the url what you want to scan: ")
    ip =  socket.gethostbyname(name)
    print("Starrting the scan on the target: ", ip)
    
    for i in range(0, 65536):
        def scan():
            try:
                s.connect((ip, i))
                s.settimeout(0.1)
                return True
            except:
                return False

        if scan() == True:
            print("Port", i, "is open.")
            opened_number += 1
        else:
            print("Port",i, "is  closed.")
            closed_number +=1 

    print("The open ports are ", opened_number, "and closed ports are ", closed_number)

def main():
    
    print("\nEnter '1' to scan the static url and port.")
    print("Enter '2' to scan url and port from user input.")
    print("Enter '3' to scan specific ports of an ip.")
    print("Enter '4' to scan ports in soecific range of an ip.")
    print("Enter '5' to scan all the ports of the ip.")
    print("Enter '6' to quit the program.")
    choice = input("Please enter your choice: ")
    if choice == "1":
        static_scan()
        main()
    elif choice == "2":
        user_input_scan()
        main()
    elif choice == "3":
        specific_port()
        main()
    elif choice == "4":
        p_range()
        main()
    elif choice == "5":
        all()
        main()
    elif choice == "6":
        print("Quitting")
        exit
    else:
        print("Invalid input!!")
        main()
main()
