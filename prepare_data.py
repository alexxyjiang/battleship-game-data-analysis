#!/usr/bin/python
import sys

# load ship conf, assign index
def load_ship_conf(file_ship_conf):
    handle  = open(file_ship_conf)
    count   = 0
    for line in handle:
        dict_ship[line.strip('\n')] = count
        count                       += 1
    handle.close()

def main():
    pass

if __name__ == '__main__':
    main()

