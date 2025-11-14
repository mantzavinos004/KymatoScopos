import subprocess
import os

class MonitorManager:
    def __init__(self):
        self.is_monitor_mode = False

    def start_monitor(self, interface):
        """Start monitor mode on a specified interface"""
        try:
            #print(f"Trying sudo airmon-ng check kill\n")
            subprocess.run(['sudo','airmon-ng','check','kill'],capture_output=True, text=True)
            print(f"trying airmon-ng start interface\n")
            result=subprocess.run(['sudo','airmon-ng','start', interface], capture_output=True, text=True)
            print(result.stdout.lower())
            if "monitor mode" in result.stdout.lower():
                self.is_monitor_mode=True
                return True
            return False
        except Exception as e:
            print(f"[-] Error: {e}")
            return False

    def stop_monitor(self, interface):
        """Stop monitor mode and restore managed mode"""
        try:
            result= subprocess.run(['sudo','airmon-ng','stop',interface], capture_output=True,text=True)
            subprocess.run(['sudo','systemctl','start','NetworkManager'], capture_output=True)

            self.is_monitor_mode=False
            return True
        except Exception as e:
            print(f"[-] Error: {e}")
            return False        

