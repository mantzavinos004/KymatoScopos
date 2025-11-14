#!/usr/bin/env python3
import os 
import sys 
import time 
from modules.monitor import MonitorManager
#from modules.scanner import NetworkScanner
#from modules.handshake import HandshakeCapture
#from modules.cracker import HandshakeCracker

class Kymatoscopos:
    def __init__(self):
        self.monitor = MonitorManager()
#        self.scanner = NetworkScanner()
#        self.handshake = HandshakeCapture()
#        self.cracker = HandshakeCracker()
        self.current_interface = "wlan0"
    
    
    def print_banner(self):
        banner=r"""
         _  __ _   _ __  __ ___   ___  ___ ___  ___  ____ ____  
 | |/ /| | | |  \/  |_ _| / __|/ __/ _ \/ __|/ ___/ ___| 
 | ' / | |_| | |\/| || |  \__ \ (_| (_) \__ \___ \___ \ 
 |_|\_\  \___/|_|  |_|___| |___/\___\___/|___/____/____/ 
                         |_|                             
        Wi-Fi Penetration Testing Framework v1.0
                Academic Use Only
        """
        print(banner)
    
    def clear_sceen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def main_menu(self):
        while True:
            self.clear_sceen()
            self.print_banner()
            print("\n" + "="*50)
            print("              MAIN MENU")
            print("="*50)
            print("1.  Start Monitor Mode")
            print("2.  Stop Monitor Mode")
            print("3.  Scan Networks Nearby")
            print("4.  Capture Handshake from Network")
            print("5.  Install Wireless Tools")
            print("6.  Show Captured Handshakes")
            print("7.  Crack Handshake (with .cap file)")
            print("8.  Crack Handshake (manual input)")
            print("9.  Create Custom Wordlist")
            print("10. Scan for WPS Networks")
            print("11. Attack WPS Network")
            print("12. Atomic Bomb (Advanced)")
            print("13. Change your MAC Address")
            print("0.  Exit")
            print("="*50)
            
            choice = input("\n[?] Select option: ").strip()
            
            if choice == "1":
                self.start_monitor_mode()
            elif choice == "2":
                self.stop_monitor_mode()
            elif choice == "3":
                self.scan_networks()
            elif choice == "4":
                self.capture_handshake()
            elif choice == "5":
                self.install_tools()
            elif choice == "6":
                self.show_handshakes()
            elif choice == "7":
                self.crack_handshake_file()
            elif choice == "8":
                self.crack_handshake_manual()
            elif choice == "9":
                self.create_wordlist()
            elif choice == "10":
                self.scan_wps_networks()
            elif choice == "11":
                self.attack_wps()
            elif choice == "12":
                self.atomic_bomb()
            elif choice == "13":
                self.change_mac()
            elif choice == "0":
                print("\n[+] Exiting Kymatoscpos. Goodbye!")
                break
            else:
                print("[-] Invalid option! Press Enter to continue.")
                input()
            
    def start_monitor_mode(self):
        print("\n[+] Starting Monitor Mode...")
        interface = input("[?] Enter your interface (default: wlan0): ").strip() or "wlan0"
        
        if self.monitor.start_monitor(interface):
            self.current_interface = f"{interface}mon"
            print(f"[+] Monitor Mode started on {self.current_interface}")
        else:
            print(f"[-] Failed to start monitor mode. Make sure your equipment has monitor mode capabilities")
        input("\nPress Enter to continue...")
    
            
if __name__ == "__main__":
    try:
        tool = Kymatoscopos()
        tool.main_menu()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
    
