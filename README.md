# arpspoofingdetect
This script analyzes ARP tables to see if there are 2 or more same MAC Addresses, if there are it's usually a sign of an ARP Spoofing attack going on with one host impersonating gateway if ff:ff:ff:ff:ff:ff (which is the broadcast address) is the only same MAC Address there is not attack taking place.

## Usage
Install the script and run it with 
<pre> python3 arp_spoof_detect.py </pre>
Input your IP Address and the script will do the ARP tables scanning. 

### Note that tests are still ongoing.
