all:
	pio run -v

compiledb:
	pio run -v --target compiledb

upload:
	stm32flash -w .pio/build/bluepill_f103c8/firmware.bin -v /dev/ttyUSB0

clean:
	pio run -v --target clean

monitor:
	pio device monitor -p /dev/ttyUSB0 -b 115200

