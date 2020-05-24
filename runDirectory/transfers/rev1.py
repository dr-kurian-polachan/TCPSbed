import socket
import numpy as np

def init_tx(address_tx,mode_tx): 
    if(mode_tx == "udp"):
        obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
        ret = (obj,address_tx,mode_tx)
    return(ret)
    
def init_rx(address_rx,mode_rx):
    if(mode_rx == "udp"):
        obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   
        obj.bind(address_rx)
        ret = (obj,address_rx,mode_rx)

    if(mode_rx == "udp-timeout"):
	obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   
	obj.settimeout(10e-3)
        obj.bind(address_rx)
        ret = (obj,address_rx,mode_rx)

    if(mode_rx == "udp-timeout-2"):
	obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   
	obj.setblocking(0)
        obj.bind(address_rx)
        ret = (obj,address_rx,mode_rx)

    return(ret)


    
def send(obj_tx,msg):
    obj = obj_tx[0];
    address_tx = obj_tx[1]
    mode_tx = obj_tx[2]
    
    if((msg == "NULL") or (msg=="NaN")):
        return

    if(mode_tx == "udp"):
        obj.sendto(msg, (address_tx))
    
    return
    
def receive(obj_rx):
    obj = obj_rx[0]
    address_rx = obj_rx[1]
    mode_rx = obj_rx[2]

    if((mode_rx == "udp") or (mode_rx == "udp-non-blocking")):
	data, addr = obj.recvfrom(60000) 
        
    if((mode_rx == "udp-timeout") or (mode_rx == "udp-timeout-2")):
	try:
		data, addr = obj.recvfrom(60000) 
	except:
		data = "NULL"
	
    return(data)

def close(object):  
    obj = object[0]
    obj.close()

    return
    
