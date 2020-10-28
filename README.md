# ezDistract


A simple redteam tool that will distract the blue teamers from using the terminal properly. (for competition usage)

## Prerequisites

```bash
# Install python3.
sudo apt-get install python3.6
# Install keyboard module.
sudo pip3 install keyboard
# Install argparse module.
sudo pip3 install argparse
```

## Installation
```bash
git clone https://github.com/O72/ezDistract.git
cd ezDistract
python3 ezDistract.py -h
```

## Usage
```bash
$ python3 ezDistract.py -h
usage: ezDistract.py [options]

optional arguments:
  -h, --help   show this help message and exit

Flag options:

  -c, --clear  Clears the terminal as soon as the user click any key in the
               keyboard
  -a, --add    Add the same key multiple times in the terminal
  -w, --write  Write sentences in terminal as soon as the userclick any key in
               the keyboard

```

### To run in the Background for Windows
```bash
C:\O72\RedTeaming>START /B ezDistract.exe -h

```

### To run in the Background for Linux
```bash
λ O72 RedTeaming → python3 ezDistract.py -h &

```

