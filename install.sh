#!/bin/bash
 
# Function to install packages based on the package manager
install_package() {
    if command -v apt-get &> /dev/null; then
        sudo apt-get install -y "$1"
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y "$1"
    elif command -v pacman &> /dev/null; then
        sudo pacman -S --noconfirm "$1"
    else
        echo "\n[!] Unsupported package manager. Please install $1 manually."
        exit 1
    fi
}
 
# Check and install macchanger
clear
echo "[+] Installing macchanger..."
install_package macchanger
 
# Check and install tor
clear
echo "[+] Installing tor..."
install_package tor
 
# Change directory and install kali-anonsurf
if [ -d "kali-anonsurf" ]; then
    cd kali-anonsurf
    chmod +x *
    sudo ./installer.sh
else
    echo "[!] Directory kali-anonsurf not found"
    exit 1
fi
 
clear
echo "[*] Installation completed."