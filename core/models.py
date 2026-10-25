#Hold deice information and network scans 
# #Data clases (Device, NetworkState, threat)
from dataclasses import dataclass, field
import time

@dataclass
class NetworkDevice:
    ip: str
    mac: str
    hostname: str= "Unknown"
    vendor: str = "Unknown"
    first_seen: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)
    