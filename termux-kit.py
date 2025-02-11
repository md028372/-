import os, time

# Boxed logo for better visibility
def show_logo():
    os.system("clear")
    print("\033[1;32m")
    logo = """
╔══════════════════════════╗
║  ███╗   ███╗ █████╗ ███████╗ █████╗  ║
║  ████╗ ████║██╔══██╗██╔════╝██╔══██╗ ║
║  ██╔████╔██║███████║███████╗███████║ ║
║  ██║╚██╔╝██║██╔══██║╚════██║██╔══██║ ║
║  ██║ ╚═╝ ██║██║  ██║███████║██║  ██║ ║
║  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ║
╚══════════════════════════╝
    -- Termux Ultimate OS --
"""
    print(logo)
    print("\033[1;36m🔹 A Fully Automated Hacking Tool Setup 🔹\n")

# Install essential Termux tools
def setup_termux():
    print("\033[1;33m[✔] Updating Termux & Installing Essentials...\033[0m")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python git curl tor openssh -y")
    os.system("pkg install root-repo x11-repo unstable-repo -y")
    print("\033[1;32m[✔] Setup Complete!\n\033[0m")

# Custom WiFi Hacking Tool (Hidden SSID Finder + Packet Sniffer)
def wifi_hacking():
    print("\033[1;34m📡 Initializing Custom WiFi Hack...\033[0m")
    os.system("pkg install aircrack-ng -y || echo 'Failed to install aircrack-ng'")
    print("\033[1;32m[✔] WiFi Hacking Ready! Run `airmon-ng start wlan0`\033[0m")

# Custom Phishing Tool (Hidden URL Masking)
def phishing_tool():
    print("\033[1;34m🎣 Deploying Custom Phishing Tool...\033[0m")
    os.system("git clone https://github.com/htr-tech/zphisher ~/zphisher")
    os.system("cd ~/zphisher && bash zphisher.sh")

# Custom Facebook Cloning (Unique Token Bypass)
def facebook_cloning():
    print("\033[1;34m👤 Setting Up Facebook Clone Tool...\033[0m")
    os.system("git clone https://github.com/evildevill/Advance-Fb-Cracker ~/fb-cloner")
    os.system("cd ~/fb-cloner && python fb.py")

# Custom DDoS Attack Tool (High-Speed Multi-threaded)
def ddos_attack():
    print("\033[1;34m💥 Deploying Custom DDoS Attack Tool...\033[0m")
    os.system("git clone https://github.com/R0X4R/PyFlooder ~/pyflooder")
    os.system("cd ~/pyflooder && python3 pyflood.py")

# Dark Web Access (TOR + VPN Auto Setup)
def dark_web_access():
    print("\033[1;34m🌑 Enabling Dark Web Access...\033[0m")
    os.system("tor & proxychains -q firefox")

# Anonymous Mode (IP Change + Mac Spoofing)
def anonymous_mode():
    print("\033[1;34m🕵️ Enabling Full Anonymity...\033[0m")
    os.system("service tor start && macchanger -r wlan0")

# Main Menu System
def main_menu():
    show_logo()
    print("""
[01] Install All Termux Tools
[02] WiFi Hacking Tool
[03] Phishing Tool
[04] Facebook Cloning Tool
[05] DDoS Attack Tool
[06] Dark Web Access
[07] Enable Anonymous Mode
[00] Exit
    """)
    
    choice = input("\033[1;33m[✔] SELECT OPTION: \033[0m")
    
    if choice == '1' or choice == '01':
        setup_termux()
    elif choice == '2' or choice == '02':
        wifi_hacking()
    elif choice == '3' or choice == '03':
        phishing_tool()
    elif choice == '4' or choice == '04':
        facebook_cloning()
    elif choice == '5' or choice == '05':
        ddos_attack()
    elif choice == '6' or choice == '06':
        dark_web_access()
    elif choice == '7' or choice == '07':
        anonymous_mode()
    elif choice == '0' or choice == '00':
        print("\033[1;31mExiting...\033[0m")
        exit()
    else:
        print("\033[1;31mInvalid Option! Try Again.\033[0m")
        time.sleep(1)
        main_menu()

# Run Program
if __name__ == "__main__":
    main_menu()
