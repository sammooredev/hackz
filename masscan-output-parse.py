import os
import re
    
#remove masscan text from output
os.system("tail -n +3 testjson | head -n -1 > testjson2")

with open("testjson2") as f:
    #for line of masscan output
    for line in f:
        #strip line of not needed text
        line2 = line.strip().replace('Host: ', '').replace('()','').replace('Ports:','').replace('/open/tcp////','')
        #grab ip, port from line in masscan output 
        ip = line2[0:15].strip()
        port = line2[16:20].strip()

        with open('all_servers_scanned.txt', 'r+') as read_obj:
            # Read all lines in the file one by one
            ipandport_home = str(ip + ' ' + port)
            not_in = True
            print("Testing: " + ip + ' ' + port)
            line_number = 0
            for line in read_obj:
                line_number += 1
                print(line_number)
                if ip in line:
                    if port not in line:
                        the_line = open('all_servers_scanned.txt').readlines()
                        print('         line with pair -> ' + the_line[line_number - 1])
                        the_line[line_number - 1] = line.strip() + ',' + port + '\n'
                        open('all_servers_scanned.txt','w+').write(''.join(the_line))
                    
                    not_in = False

            if not_in == True:
                read_obj.write(ipandport_home + '\n')
            else:
                print('ip was in file')

                    