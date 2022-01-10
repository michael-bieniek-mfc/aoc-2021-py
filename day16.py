f = open("day16.dat", "r")

contents = list(f.read())
num_of_bits = 4

def to_binary(in_hex):
  return list(map(lambda item: bin(int(item, 16))[2:].zfill(num_of_bits),in_hex))


def get_packet_type(packet):
  pver = int(packet[0:3],2)
  ptype = int(packet[3:6],2)
  packet_len = None
  len_bit = None

  if ptype != 4:
    len_bit = packet[6:7]
    if len_bit == "0":
      packet_len = int(packet[7:7+15],2)
    elif len_bit == "1":
      packet_len = int(packet[7:7+11],2)
      print(packet_len)
  return (pver, ptype, len_bit, packet_len)

type_map = {
  0: "Sum",
  1: "Mult",
  2: "Min",
  3: "Max",
  4: "Val",
  5: ">",
  6: "<",
  7: "Eq",
}

def read_packet(packet):
  if packet is None:
    return ([], [])
  header = get_packet_type(packet)
  ( pver, ptype, plenbit, plenbitvalue ) = header
  print("Ver", pver, "Type", ptype)
  vers = []
  if ptype != 4:
    print("Op", type_map[ptype])
    # operation    
    if plenbit == "0":
      # the plenbitvalue is the integer representing total length in bits of sub-packets
      # VVVTTTILLLLLLLLLLLLLLL
      subpacket = packet[22:22+plenbitvalue]
      while len(subpacket) > 0:
        subpacket, out_vers = read_packet(subpacket)
        vers.append(out_vers)
      #return (packet[22+plenbitvalue:], vers)
    elif plenbit == "1":
      # the plenbitvalue is the integer representing total num of subpackets
      # VVVTTTILLLLLLLLLLLLLLL
      subpacket = packet[18:]
      for subpackind in range(int(plenbitvalue)):
        subpacket, out_vers = read_packet(subpacket)
        vers.append(out_vers)
      #return  (subpacket, vers)
    # now, let's apply the appropriate operation
    print("Vers", vers)
    """
    if ptype == 0:
      vers.append('*')
    if ptype == 1:
      vers.append('*')
    if ptype == 2:
      vers.append('m')
    if ptype == 3:
      vers.append('M')
    if ptype == 5:
      vers.append('>')
    if ptype == 6:
      vers.append('<')
    if ptype == 7:
      vers.append('e')
    """
    return (None, sum(vers))
  else:
    bit_pointer = 6
    bit_rep = ""

    while True:
      # get next 5
      if bit_pointer+5 > len(packet):
        break
      bits = packet[bit_pointer:bit_pointer+5]
      bit_rep = bit_rep + f"{packet[bit_pointer+1:bit_pointer+5]}"
      bit_pointer += 5
      if bits[0] == "0":
        # last part
        break
    #print(int(bit_rep,2))
    
    
    return ( [], int(bit_rep,2) )
    #if len(packet[bit_pointer:]) == 0:      
    #  return ([], [int(bit_rep,2)])
    #else:
    #  return (packet[bit_pointer:], [int(bit_rep,2)])


packet = "".join(to_binary(contents))

sample1 = "".join(to_binary('38006F45291200'))
sample2 = "".join(to_binary('C0015000016115A2E0802F182340'))

#print(read_packet(sample1))

vers = []

print(read_packet(packet)[-1])