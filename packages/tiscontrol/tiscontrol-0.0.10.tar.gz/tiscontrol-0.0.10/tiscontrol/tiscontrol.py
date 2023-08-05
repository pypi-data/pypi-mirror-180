import sys
import socket
import time
import logging
import asyncio

_LOGGER = logging.getLogger(__name__)

TRV = {}

DEFAULT_PROXY_PORT = 6000


light=[]


class UDPCollector:
    """UDP proxy to collect Lightwave traffic."""

    def __init__(self):
        """Initialise Collector entity."""
        self.transport = None

    def _send_message(self, msg):
        """Add message to queue and start processing the queue."""
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSock.sendto(bytes.fromhex(msg), ("192.168.29.180", 6000))

    # pylint: disable=W0613, R0201
    def datagram_received(self, data):
        """Manage receipt of a UDP packet from Lightwave."""

        _LOGGER.warning(self.add_space(self.convert_hex(data)))
        #self.store_data(self.convert_hex(data))


    def add_space(self,a):
        # split address to 6 character
        pac=' '.join([a[i:i+2] for i in range(0, len(a), 2)])
        # format to 00:00:00:00:00:00
        return pac

    def convert_hex(self, data):
        res = ""
        for b in data:
            res += "%02x" % b
        return res
    def enquiry(self,list1): 

        return not list1

    def turn_on_light(self, device_id, name):
        """Create the message to turn light on."""
        msg = "C0A8018B534D415254434C4F5544AAAA0F01FEFFFE0031012C01640000BFB3"
        self._send_message(msg)
       

    def turn_off_light(self, device_id, name):
        """Create the message to turn light on."""
        msg = "C0A8018B534D415254434C4F5544AAAA0F01FEFFFE0031012C01000000F818"
        self._send_message(msg)
    

    def get_light_status(self, device_id):
        """Create the message to turn light on."""
        msg = "C0A8018B534D415254434C4F5544AAAA0B01FEFFFE0033012CB013"
        self._send_message(msg)
       

    def store_data(self, data):
        _LOGGER.warning("received message from TIS server : %s"  % data)
        if(str(data[42:46])=="0034"):
            print("your packet is right 0034",self.add_space(data))
        elif(str(data[42:46])=="0032"):
            print("your packet is right 0032 ",self.add_space(data))
            status_data=data[34:-1]
            print(status_data)
            subnet_id=status_data[0:2]
            device_id=status_data[2:4]
            channel_id=status_data[16:18]
            concat=status_data[0:2]+status_data[2:4]+status_data[16:18]
            level=status_data[20:22]

            if self.enquiry(light): 
                print("The list is Empty") 
                light.append({"level":level,"device_id":concat})
                print(light)
            else: 
                 print("The list isn't empty")
                 for value in light:
                    if(concat==value["device_id"]):
                        value["level"]=level
                        print(light)
                        return 

    def read_trv_status(self):
            """Read Lightwave TRV status from the proxy."""

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    sock.bind(("", DEFAULT_PROXY_PORT))
                    sock.settimeout(2.0)
                    msg="C0A8018B534D415254434C4F5544AAAA0B01FEFFFE0033012CB013"
                    sock.sendto(bytes.fromhex(msg), ("192.168.29.180", 6000))
                    data, addr = sock.recvfrom(65565) # buffer size is 65565 bytes

                    return self.datagram_received(data)
                

            except socket.timeout:
                _LOGGER.warning("TIS proxy not responing")

            except socket.error as ex:
                _LOGGER.warning("TIS proxy error %s", ex)

            return "Success"









