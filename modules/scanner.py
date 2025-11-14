import subprocess
import time
import csv
import os

class NetworkScanner:
    def scan(self, interface, duration=10):
        """ Scan for nearby wireless networks """
        try:
            print(f"[*] Scanning for {duration} seconds...")
            cmd = ['sudo','airodump-ng','--write','/tmp/kymatoscopos_scans','--output-format','csv',interface]
            process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(duration)
            process.terminate()
            process.wait()
            return self._parse_scan_results('/tmp/kymatoscopos_scans-01.csv')
        except Exception as e:
            print(f"[-] Scan error: {e}")
            return []

    def _parse_scan_results(self, filename):
        """ Parse the airodump-ng CSV results """
        networks=[]
        try:
            if not os.path.exists(filename):
                return networks
            with open(filename, 'r') as f:
                lines =f.readlines()
            # Find where networks start in file
            start_index = 0
            for i, line in enumerate(lines):
                if line.startswith('BSSID,'):
                    start_index = i +1
                    break
            # Parse the networks
            for line in lines[start_index:]:
                if line.strip() =='':
                    break
                parts = line.split(',')
                if len(parts) >= 14:
                    network = {
                        'bssid': parts[0].strip(),
                        'essid': parts[13].strip(),
                        'channel': parts[3].strip(),
                        'power': part[8].strip(),
                        'encryption': parts[5].strip()
                    }
                    # only then append this network
                    networks.append(nework)
            
            # Cleanup the scan file
            if os.path.exists(filename):
                os.remove(filename)
            return networks
        except Exception as e:
            print(f"[-] Parse error: {e}")
            return []
            


