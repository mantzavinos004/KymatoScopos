import subprocess
import os
import time

class MonitorManager:
    def __init__(self):
        self.is_monitor_mode = False

    def start_monitor(self, interface):
        """Start monitor mode on a specified interface"""
        try:
            print(f"[*] Starting monitor mode on {interface}...")
            subprocess.run(['sudo','airmon-ng','check','kill'],capture_output=True, text=True)
            time.sleep(2)
            print(f"[*] Trying airmon-ng start {interface}...\n")
            result=subprocess.run(['sudo','airmon-ng','start', interface], capture_output=True, text=True)
            print(result.stdout.lower())
            
            if self.check_monitor_status(interface):
                self.is_monitor_mode = True
                print(f"[+] Monitor mode enabled on {interface}")
                return True
            else:
                print("[-] Failed to enable monitor mode")
                return False
        except Exception as e:
            print(f"[-] Error starting monitor mode: {e}")
            return False

    def stop_monitor(self, interface):
        """Stop monitor mode and restore managed mode"""
        try:
            print(f"[*] Stopping monitor mode on {interface}...")
            result= subprocess.run(['sudo','airmon-ng','stop',interface], capture_output=True,text=True)
            time.sleep(2)
            subprocess.run(['sudo','airmon-ng','check','kill'], capture_output= False)
            time.sleep(2)
            subprocess.run(['sudo','ip','link','set',interface,'down'], capture_output=False)
            subprocess.run(['sudo','iw',interface,'set','type','managed'], capture_output=False)
            subprocess.run(['sudo','ip','link','set',interface,'up'], capture_output=False)
            time.sleep(2)
            subprocess.run(['sudo','systemctl','restart','NetworkManager'], capture_output=True)
            time.sleep(5)

            if not self.check_monitor_status(interface):
                self.is_monitor_mode= False
                print(f"[+] Successfully returned {interface} to managed mode")
                return True
            else:
                print(f"[-] Could not verify return to managed mode")
                return False
        except Exception as e:
            print(f"[-] Error stopping monitor mode: {e}")
            return False        
    
    def check_monitor_status(self, interface):
        """ Check if the interface is in monitor mode or no """
        try:
            result = subprocess.run(['iwconfig',interface],capture_output= True, text= True)
            return "Mode:Monitor" in result.stdout
        except:
            return False

