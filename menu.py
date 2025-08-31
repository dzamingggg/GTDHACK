import os
import time
import requests
from Crypto.Cipher import AES
import base64

RESET = "\033[0m"
RED = "\033[91m"
ORANGE = "\033[38;5;208m"
YELLOW = "\033[93m"
LIME = "\033[92m"
GREEN = "\033[32m"
SPRINGGREEN = "\033[38;5;48m"
CYAN = "\033[96m"
SKYBLUE = "\033[94m"
ROYALBLUE = "\033[38;5;63m"
INDIGO = "\033[38;5;54m"
VIOLET = "\033[95m"
MAGENTA = "\033[35m"
DEEPPINK = "\033[38;5;198m"
CRIMSON = "\033[38;5;161m"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def aes_encrypt(message, key, iv):
    key_bytes = key.encode("utf-8")
    iv_bytes = iv.encode("utf-8")

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    pad = AES.block_size - len(message.encode("utf-8")) % AES.block_size
    data = message.encode("utf-8") + bytes([pad] * pad)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted).decode("utf-8")

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(RED + r"""
  _______ ____   ____  _         _____ _______ _____   
 |__   __/ __ \ / __ \| |       / ____|__   __|  __ \  
    | | | |  | | |  | | |      | |  __   | |  | |  | | 
    | | | |  | | |  | | |      | | |_ |  | |  | |  | | 
    | | | |__| | |__| | |____  | |__| |  | |  | |__| | 
    |_|  \____/ \____/|______|  \_____|  |_|  |_____/  
                                                       
                                                       
""" + RED + "                 TOOL By Doan Gia Minh" + RESET)
    print()

def menu():
    print(YELLOW     + "[1]"  + RED        + "  Hack Anti Ban")
    print(YELLOW     + "[2]"  + ORANGE     + "  Hack Tài Nguyên")
    print(YELLOW     + "[3]"  + YELLOW     + "  Hack Stage")
    print(YELLOW     + "[4]"  + LIME       + "  Hack Hero")
    print(YELLOW     + "[5]"  + GREEN      + "  Hack Tháp")
    print(YELLOW     + "[6]"  + SPRINGGREEN+ "  Change IP")
    print(YELLOW     + "[7]"  + CYAN       + "  Block Account")
    print(YELLOW     + "[8]"  + SKYBLUE    + "  Put Blacklist User")
    print(YELLOW     + "[9]"  + ROYALBLUE  + "  Put PvP Point")
    print(YELLOW     + "[10]" + INDIGO     + "  Put Guild War Point")
    print(YELLOW     + "[11]" + VIOLET     + "  Change Name Normal")
    print(YELLOW     + "[12]" + MAGENTA    + "  Change Name Color")
    print(YELLOW     + "[13]" + DEEPPINK   + "  Change Android ID")
    print(YELLOW     + "[14]" + CRIMSON    + "  Hack X3 Speed PvP")
    print(YELLOW     + "[15]" + RED        + "  Hack Level")
    print(YELLOW     + "[16]" + RESET      + "  Exit")
    print()

def main():
    while True:
        banner()
        menu()
        choice = input(CYAN + "Enter choice: " + RESET)

        if choice == "1":
            valid_platforms = ["AMO", "ATV", "SS", "LG"]
            while True:
                platform = input(GREEN + "Nhập Nền Tảng người dùng (AMO/ATV/SS/LG): " + RESET)
                if platform in valid_platforms:
                    break
                else:
                    print(SKYBLUE + "❌ Chỉ chấp nhận AMO, ATV, SS, LG." + RESET)
            user_id = input(GREEN + "Nhập ID người dùng: " + RESET)
            payload_raw = f'{{"UNIQ_ID":"{user_id}"}}'

            encrypted = aes_encrypt(payload_raw, "aksekf2djrqjfwk!", "towerdefence_gtd")
            url = f"http://211.253.26.47:8093/TOWERDEFENCE_{platform}/Counter/unblock_user.php"

            try:
                print(SKYBLUE + "⏳ Đang gửi request Anti Ban..." + RESET)
                res = requests.post(url, data={"encryt": encrypted}, timeout=10)
                time.sleep(3)
                print(RED + f"Đã thực hiện chức năng Anti Ban cho tài khoản {user_id}" + RESET)
            except Exception as e:
                print(RED + f"❌ Lỗi: {e}" + RESET)

            input("Nhấn Enter để quay lại menu...")

        elif choice == "2":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "3":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "4":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "5":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "6":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "7":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")
            
        elif choice == "8":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "9":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "10":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "11":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")
  
        elif choice == "12":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "13":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "14":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "15":
            input( RED + "Mua Tool Vip dùng full chức năng liên hệ FB : Doan Gia Minh.")

        elif choice == "16":
            print(RED + "Thoát TOOL GTD..." + RESET)
            time.sleep(1)
            break

        else:
            print(GREEN + "👉 Lựa chọn {choice} không hợp lệ!" + RESET)
            input("Nhấn Enter để quay lại menu...")

if __name__ == "__main__":
    main()
