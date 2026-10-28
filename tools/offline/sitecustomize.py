"""Offline verification: local transports only; provider CLIs remain disabled."""
import socket,ipaddress,subprocess
connect=socket.socket.connect;connect_ex=socket.socket.connect_ex;dns=socket.getaddrinfo;popen=subprocess.Popen
def local(address):
 if isinstance(address,str):return True
 if address[0] in ['localhost','']:return True
 try:return ipaddress.ip_address(address[0]).is_loopback
 except ValueError:return False
def check_connect(self,address):
 if not local(address):raise RuntimeError('External networking is disabled for source verification.')
 return connect(self,address)
def check_connect_ex(self,address):
 if not local(address):raise RuntimeError('External networking is disabled for source verification.')
 return connect_ex(self,address)
def check_dns(host,*a,**kw):
 if host is not None and not local((host,0)):raise RuntimeError('External DNS is disabled for source verification.')
 return dns(host,*a,**kw)
class OfflinePopen(popen):
 def __init__(self,args,*a,**kw):
  command=args[0] if isinstance(args,(tuple,list)) else str(args).split()[0]
  if str(command).rsplit("/",1)[-1] in {"modal","vast","vastai","aws","ssh","curl","docker"}:raise RuntimeError("Provider/service CLIs are disabled for source verification.")
  super().__init__(args,*a,**kw)
socket.socket.connect=check_connect;socket.socket.connect_ex=check_connect_ex;socket.getaddrinfo=check_dns;subprocess.Popen=OfflinePopen
