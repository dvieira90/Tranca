esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 <.bin>
esptool.py --port /dev/ttyUSB0 erase_flash

ampy -b 115200 -p /dev/ttyUSB0 put main.py

alias node='ampy -b 115200 -p /dev/ttyUSB0 put main.py && ampy -b 115200 -p /dev/ttyUSB0 put funcs.py && minicom -b 115200 -D /dev/ttyUSB0'