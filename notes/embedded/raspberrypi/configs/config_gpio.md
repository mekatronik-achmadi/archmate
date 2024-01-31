# GPIO Configurations

## Reading GPIO

```sh
# config gpio-12 (pin 32) as pulled-down input
# its recomended to use high output gpio as input
echo 12 | sudo tee /sys/class/gpio/export
echo in | sudo tee /sys/class/gpio/gpio12/direction

# check gpio value
cat /sys/class/gpio/gpio12/value
```

## writing GPIO

```sh
# config gpio-16 (pin 36) as output
# must use current limiting resistor to avoid damage
echo 16 | sudo tee /sys/class/gpio/export
echo out | sudo tee /sys/class/gpio/gpio16/direction

# set gpio as high
echo 1 | sudo tee /sys/class/gpio/gpio16/value

# set gpio as low
echo 0 | sudo tee /sys/class/gpio/gpio16/value
```
