import sys
from pathlib import Path
# Add the parent directory to the Python module search path
sys.path.append(str(Path(__file__).parent.parent))

# Import necessary libraries
import get_info
import json
import socket

def main():
    
    # Receive arguments from the command line
    if len(sys.argv) != 4:
        print(f"[ERROR] In valid number of arguments provided.")
        print(f"Usage: python client.py <server-ip> <server-port> <your-id>")
        return
    
    server_host, server_port, ID = sys.argv[1:]
    server_port = int(server_port)
    
    # message
    # {
    #     "ID": <id>
    #     "Hostname": <hostname>,
    #     "User": <current_user>,
    #     "OS": <os_system>,
    #     "OS version": <os_version>,
    #     "Mac": <mac>,
    #     "Local IP": <local_ip>,
    #     "Public IP": <public_ip>,
    # }
    message = get_info.extract()
    message["ID"] = ID

    try:
        
        # TODO
        # Create a socket object
        # =============================================


        # =============================================

        # TODO
        # Connect to the server
        # =============================================
        
        
        # =============================================
        print(f"[INFO] Connected to server at {server_host}:{server_port}")

        # TODO
        # After the connection has been established, send the information in json format to the server
        # =============================================


        # =============================================
        print(f"[INFO] Sent message: {message}")

        # TODO
        # Receive response from the server in json format {"TOKEN": <token>}
        # Use 1024 bytes as the buffer size
        # =============================================
        
        
        # =============================================
        print(f"[INFO] Received response: {response.decode('utf-8')}")


    except ConnectionRefusedError:
        print("[ERROR] Could not connect to the server. Make sure it is running.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        print("[INFO] Connection closed.")
        
if __name__ == '__main__':
    main()