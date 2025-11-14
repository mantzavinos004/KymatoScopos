import json
import os
from datetime import datetime

class StorageManager:
    def __init__(self):
        self.scans_dir = "scans"
        self.handshakes_dir = "handshakes"
        self.wordlists_dir = "wordlists"
        self.setup_directories()

    def setup_directories(self):
        """ Create necessary directories """
        os.makedirs(self.scans_dir, exist_ok=True)
        os.makedirs(self.handshakes_dir, exist_ok=True)
        os.makedirs(self.wordlists_dir, exist_ok=True)

    def save_scan(self, networks):
        """ Save scan results to a JSON file """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.scans_dir}/scan_{timestamp}.json"

        scan_data = {
            'timestamp': timestamp,
            'total_networks': len(networks),
            'networks': networks
        }

        try:
            with open(filename, 'w') as f:
                json.dump(scan_data, f, indent=2)
            print(f"[+] Scan saved to: {filename}")
            return filename
        except Exception as e:
            print(f"[-] Failed to save scan: {e}")
            return None
    
    def load_scan(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"[-] Failed to load scan: {e}")
            return None

    def list_scans(self):
        if not os.path.exists(self.scans_dir):
            return []
        scans = []
        for file in os.listdir(self.scans_dir):
            if file.endswith('.json'):
                scans.append(os.path.json(self.scans_dir,file))
    
        return stored(scans, reverse= True)


