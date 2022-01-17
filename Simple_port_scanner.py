import socket


                
def conn(host):
        
        for i in range(1,10000):
                port = i
                
                with socket.socket() as s:
                        s.settimeout(1)
                        if  s.connect_ex((host,port)):
                                print(f"Port {port} is closed .")
                        else:
                                print(f"Port {port} is open ")
                
def main():
        host = input("Enter the ip addr to scan : ")

        if len(host) != 0: 
                if type(host) == 'int':
                        print(int(host))
                        conn(host)
                else:
                        print(socket.gethostbyname(host))
                        conn(host)
        else:
                print("No input given syntx{123.123.12.0 or somthing.com }")
                
        
        

if __name__ == '__main__':
        main()
                