#made by Timo654
import sys
input_files = sys.argv[1:]

#amd files seem to be little endian
ENDIANNESS = 'little'

#checks if there are any files
if input_files == []:
    input("No files detected. You need to drag and drop the file(s).\nPress any key to continue.")
    sys.exit()

#saves new file
def save_files(input_files, binary_data):
    with open(input_files[:-4] + '.amd', 'wb') as f:
        f.write(binary_data)
        print(input_files[:-4] + ".amd saved.")
#verifies if the file is actually gmo
def file_check(input_files):
    if not binary_data[0x00:0x04].decode().strip('\x00') == 'OMG.':
        input("Not a valid gmo file.\nPress any key to continue.")
        sys.exit()
#loads the file
def load_file(input_files):
    global binary_data
    with open(input_files, 'rb') as binary_file:
        binary_data = bytearray(binary_file.read())
        num_bytes = binary_file.tell()
    file_check(input_files)
    add_header(binary_data, input_files, num_bytes)

#adds the amd header
def add_header(binary_data, input_files, num_bytes):
    binary_data[0x0:0x0] = bytearray([0]*31)
    binary_data[0x0:0x1B] = bytearray(b'CHNK\x01\x00\x00\x00MODEL_DATA\x00\x00\x00\x00\x00\x00\x01\x01\x00')
    binary_data[0x1C:0x1F] = num_bytes.to_bytes(4, byteorder=ENDIANNESS)
    save_files(input_files, binary_data)

#loads each file
for file in input_files:
    load_file(file)

input("Files successfully converted.\nPress enter to continue...")