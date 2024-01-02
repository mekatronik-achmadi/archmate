### Help/Guides

#### Usages

Name entries:

- **Hostname**: The host name of computer. Please keep it short and no spaces.
- **Username**: The user name of yours. Please keep it short and no spaces.

Partition entries:

- **Root**: Root partition in *ext4* format (ex: */dev/sda2*).
  Size at least 15GB. Must be formatted first. Mandatory.
- **Home**: Home partition in *ext4* format (ex: */dev/sda3*). Optional
- **EFI** : EFI partition in *fat32* format (ex: */dev/sda1*).
  Must be in GPT a disk. Size about 500MB. Mandatory if in EFI mode.
- **GRUB**: Installation disk (not partition) name (ex: */dev/sda*).
  Must be in same disk with Root, Home, Swap, and EFI partition. Mandatory.

Extract Method:

- **Rsync**: Much slower but more guarantee success on old computers.
- **Unsquashfs**: Much faster and great on modern computers. Default.

#### Troubleshoots:

Here some error messages:

- *X not in same GRUB disk*: Partition entries must be in same disk with GRUB disk.
- *X entry is same with something else*: Partition entry is same with another entry.
- *X is empty*: A mandatory or checked entry is empty.
- *X address is empty*: A mandatory or checked entry is empty.
- *X is not in Y format*: Partition not in intended format.
- *X size less than Y*: Partition is less than minimum size.
