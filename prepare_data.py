#/usr/bin/python
#-*- encoding: utf-8 -*-
import ConfigParser

dict_index  = {}
dict_res    = {}
dict_ships  = {}
dict_name   = {}
count       = 0

# load all support resource
def load_resource_types(list_resource):
    global count 
    for item in list_resource:
        dict_index[count]   = item[1]
        dict_res[item[1]]   = count
        count               += 1

# load all ship types 
def load_ship_types(list_ship):
    global count
    for item in list_ship:
        dict_index[count]   = item[1]
        dict_ships[item[1]] = count
        dict_name[item[0]]  = item[1]
        count               += 1

# process build file
# Fuel Ammo Fe Al Name Type
def process_build_file(handle_in, handle_out):
    for line in handle_in:
        items   = line.strip('\n').split('\t')
        if len(items) != 6:
            continue
        list_out    = items[0:len(dict_res)]
        ship_out    = items[-1]
        ship_index  = dict_ships[dict_name[ship_out]]
        for i in range(len(dict_res), len(dict_index)):
            if i != ship_index:
                list_out.append('0')
            else:
                list_out.append('1')
        handle_out.write('\t'.join(list_out))
        handle_out.write('\n')

# process build file
# Fuel Ammo Fe Al Type Count
def process_stat_file(handle_in, handle_out):
    for line in handle_in:
        items   = line.strip('\n').split('\t')
        if len(items) != 6:
            continue
        list_out    = items[0:len(dict_res)]
        ship_out    = items[-2]
        ship_count  = int(items[-1])
        ship_index  = dict_ships[dict_name[ship_out]]
        for i in range(len(dict_res), len(dict_index)):
            if i != ship_index:
                list_out.append('0')
            else:
                list_out.append('1')
        for j in range(ship_count):
            handle_out.write('\t'.join(list_out))
            handle_out.write('\n')

# do all
def do_work(file_config):
    confp   = ConfigParser.ConfigParser()
    confp.read(file_config)
    if confp.has_section('resource_types'):
        load_resource_types(confp.items('resource_types'))
    if confp.has_section('ship_types'):
        load_ship_types(confp.items('ship_types'))
    if confp.has_option('output', 'output_file'):
        handle_out  = open(confp.get('output', 'output_file'), 'w')
        list_title  = []
        for index in range(len(dict_index)):
            list_title.append(dict_index[index])
        handle_out.write('\t'.join(list_title))
        handle_out.write('\n')
        if confp.has_section('input'):
            for item in confp.items('input'):
                if item[0].find('build_data') != -1:
                    handle_in   = open(item[1])
                    process_build_file(handle_in, handle_out)
                    handle_in.close()
                if item[0].find('stat_data') != -1:
                    handle_in   = open(item[1])
                    process_stat_file(handle_in, handle_out)
                    handle_in.close()
        handle_out.close()

def main():
    do_work('./conf/convert.conf')

if __name__ == '__main__':
    main()

