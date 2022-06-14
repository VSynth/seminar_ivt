ipv4 = input("ipv4 - 0.0.0.0/0 : ")
subnet = int(ipv4.split("/")[1])
ipv4_dec = [int(ipv4.split("/")[0].split(".")[x]) for x in range(len(ipv4.split("/")[0].split(".")))]

def dec_to_bin(n):
    bin_n = [0 for x in range(8)]
    for i in range(1,len(bin_n)+1):
        if n == 0:
            break
        if n % 2 == 1:
            bin_n[-i] = 1
            n -= 1
        n /= 2
    return bin_n

def bin_to_dec(n):
    dec_n = 0
    for i in range(len(n)):
        dec_n += n[i]*(2**(len(n)-i-1))
    return dec_n

ipv4_bin = [dec_to_bin(ipv4_dec[x]) for x in range(len(ipv4_dec))]

ipv4_network_bin = [[0 for x in range(8)] for y in range(len(ipv4_bin))]
for i in range(len(ipv4_bin)):
    for j in range(8):
        if i*8+j < subnet:
            ipv4_network_bin[i][j] = ipv4_bin[i][j]
ipv4_network_dec = [bin_to_dec(ipv4_network_bin[x]) for x in range(len(ipv4_network_bin))]
ipv4_network_dec_str = [str(ipv4_network_dec[x]) for x in range(len(ipv4_network_dec))]
print("Network: "+ str(".".join(ipv4_network_dec_str)))

ipv4_broadcast_bin = [[1 for x in range(8)] for y in range(len(ipv4_bin))]
for i in range(len(ipv4_bin)):
    for j in range(8):
        if i*8+j < subnet:
            ipv4_broadcast_bin[i][j] = ipv4_bin[i][j]
ipv4_broadcast_dec = [bin_to_dec(ipv4_broadcast_bin[x]) for x in range(len(ipv4_broadcast_bin))]
ipv4_broadcast_dec_str = [str(ipv4_broadcast_dec[x]) for x in range(len(ipv4_broadcast_dec))]
print("Broadcast: "+ str(".".join(ipv4_broadcast_dec_str)))

if subnet < 31:
    ipv4_host_first_bin = ipv4_network_bin
    ipv4_host_first_bin[-1][-1] = 1
    ipv4_host_first_dec = [bin_to_dec(ipv4_host_first_bin[x]) for x in range(len(ipv4_host_first_bin))]
    ipv4_host_first_dec_str = [str(ipv4_host_first_dec[x]) for x in range(len(ipv4_host_first_dec))]
    
    ipv4_host_last_bin = ipv4_broadcast_bin
    ipv4_host_last_bin[-1][-1] = 0
    ipv4_host_last_dec = [bin_to_dec(ipv4_host_last_bin[x]) for x in range(len(ipv4_host_last_bin))]
    ipv4_host_last_dec_str = [str(ipv4_host_last_dec[x]) for x in range(len(ipv4_host_last_dec))]
    
    print("Host IP range: "+ str(".".join(ipv4_host_first_dec_str)) + " - " + str(".".join(ipv4_host_last_dec_str)))
