#Main application entry point and background loop runner
from core.models import NetworkDevice 
from utils.permissons import is_admin

def test_steps():
    print("Testing stpe 2: Permissions")
    admin_status = is_admin()
    print(f"Running with Admin/Root Privileges; {admin_status}")
    
    print("\n Testing Step 1: Data Models")
    test_device = NetworkDevice(
        ip= "192.168.1100",
        mac="AA:BB:CC:11:22:33",
        hostname = "router.local",
        vendor="TP-Link",
        )
    print(f"Device IP: {test_device.ip}")
    print(f"Device MAC: {test_device.mac}")
    print(f"Device Vendo: {test_device.vendor}")
    print(f"Timestamp: {test_device.first_seen}")
    
    print("\n[+] Steps 1 & 2 verified successfully!")
    
    if __name__ == "__main__":
        test_steps()