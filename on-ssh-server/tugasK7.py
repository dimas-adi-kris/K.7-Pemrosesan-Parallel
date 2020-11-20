import psutil as psu
import time

sent_total_after = psu.net_io_counters(pernic=True)['Wi-Fi'].bytes_sent
sent_total_before = sent_total_after

rec_total_after = psu.net_io_counters(pernic=True)['Wi-Fi'].bytes_recv
rec_total_before = rec_total_after

time.sleep(1)

sent_total_before = sent_total_after
rec_total_before = rec_total_after

sent_total_after = psu.net_io_counters(pernic=True)['Wi-Fi'].bytes_sent
sent_interval = sent_total_after - sent_total_before
rec_total_after = psu.net_io_counters(pernic=True)['Wi-Fi'].bytes_recv
rec_interval = rec_total_after - rec_total_before
print('''
_______________________________________
Node 1					|''')
print(psu.net_connections('inet4')[1].laddr.ip,'	        |')
print("CPU Usage : {}%			|".format(psu.cpu_percent()))
print("Memory usage : {}%			|".format(psu.virtual_memory()[2]))
print("Internet tranffic :			|")
print("TX : {0:0.2f} KB RX : {1:0.2f} KB		|".format(sent_interval/1024,rec_interval/1024),end='\r')
#time.sleep(1)

