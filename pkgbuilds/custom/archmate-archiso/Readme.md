# Custom ArchISO

This section contains scripts and files to build a custom ArchISO images

## Project Repository

You can find all required files in project repository here: [ArchMate ArchISO](https://github.com/mekatronik-achmadi/archmate/tree/main/archiso).


## Requirements

Minimal requirements:

- Archiso packages, either using:
	- [archiso](https://archlinux.org/packages/extra/any/archiso/)
	- the PKGBUILD for this package (recommended)
- A working directory contains at least:
	- a build script either:
		- **archiso_mate.sh** (for MATE Desktop)
		- **archiso_cli.sh** (for CLI only)
	- a package list:
		- **pkg-mate-x86_64.txt** (for MATE Desktop)
		- **pkg-cli-x86_64.txt** (for CLI only)
	- a package collection folders:
		- folder/databases (contain database files)
		- folder/packages/official (contain packages from repository)
		- folder/packages/custom (contain your custom packages)

Please read the script for more details.
You can use **newpkgs.md** as guideline to build package folders.

## Build

to build, run commands:

```sh
sudo ./archiso_mate.sh
```

## Test the ISO

You can test the ISO using Qemu X86_64 with **qemutest.sh** script

```sh
./qemutest.sh archlinux-desktop_customdate-x86_64.iso
```

