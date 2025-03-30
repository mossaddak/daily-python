'''
- give permission: sudo chmod 666 /dev/hidraw0
- find hidraw0: ls /dev/hidraw*
- find device: lsusb
- find device: lsusb -t
- find device: lsusb -v
- find device: lsusb -v | grep -i fingerprint
- find device: lsusb -v | grep -i 0c45
- find device: lsusb -v | grep -i 0c45:7401
'''

# Device path for the fingerprint scanner
device_path = "/dev/hidraw0"

try:
    # Open the fingerprint scanner device
    with open(device_path, "rb") as device:
        print(f"Listening for fingerprint data from {device_path}...")
        
        # Continuous reading loop
        while True:
            data = device.read(64)  # Read 64 bytes at a time (adjust size if necessary)
            
            # If fingerprint data is received, display it
            if data:
                print(f"Fingerprint Data: {data}")
except PermissionError:
    print(f"Permission denied. Run the script with sudo or change permissions for {device_path}")
except FileNotFoundError:
    print(f"Device {device_path} not found.")
except Exception as e:
    print(f"Error: {e}")
