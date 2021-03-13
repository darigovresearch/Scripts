# raspi_init.py is code to generate initial files for a new raspberry pi SD card

from getpass import getpass

# get wpa ssid
ssid = input("Enter wifi name (aka ssid):")
# get password
pwd = getpass("Password (text will be hidden):")

wpa_string = """country=gb
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid=\"""" + ssid + """\"
 psk=\"""" + pwd + """\"
}"""

# generate wpa file
wpa_file = open('wpa_supplicant.conf', 'w')
wpa_file.write(wpa_string)
wpa_file.close()

# generate ssh file
ssh_file = open('ssh', 'w')
ssh_file.close()
