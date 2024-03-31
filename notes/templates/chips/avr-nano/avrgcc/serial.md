# Virtual Serial

## Setup Virtual ComPort

**NOTE:** make sure the /dev/pts/ number is correct

```sh
socat -d -d pty,raw,echo=0 pty,raw,echo=0
sudo ln -sf /dev/pts/2 /dev/ttyV0
sudo ln -sf /dev/pts/3 /dev/ttyV1
```

## SimulIDE

Serial Port:

- Components: Micro -> Peripherals -> Serial Port
- Properties:
	- Port Name: /dev/ttyV0
	- Baudrate: 9600

Then Click **Open**.

## Serial Term

```sh
picocom -c -b 9600 /dev/ttyV1
```
