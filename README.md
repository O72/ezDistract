# ezDistract


A simple redteam tool that will distract the blue teamers from using the terminal properly.

## Prerequisites

```bash
# Install python3.
sudo apt-get install python3.6
# Install keyboard module.
sudo pip3 install keyboard
# Install argparse module.
sudo pip3 install argparse
```

## Usage

```bash
$ python3 ezDistract.py -h
usage: ezDistract.py [options]

optional arguments:
  -h, --help   show this help message and exit

Flag options:

  -c, --clear  Clears the terminal as soon as the user clickany key in the
               keyboard
  -a, --add    Add the same key multiple times in the terminal
  -w, --write  Write sentences in terminal as soon as the userclick any key in
               the keyboard

```
