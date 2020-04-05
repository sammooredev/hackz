import os
import re
    
#remove masscan text from output
os.system("tail -n +3 masscan_greppable_output.txt | head -n -1 > work_file.txt")

with open("work_file.txt") as f:
    #for line of masscan output
    for line in f:
        #strip line of not needed text
        line2 = line.strip().replace('Host: ', '').replace('()','').replace('Ports:','').replace('/open/tcp////','')
        #grab ip, port from line in masscan output 
        ip = line2[0:15].strip()
        port = line2[16:20].strip()

        with open('final_output.txt', 'r+') as read_obj:
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
                        the_line = open('final_output.txt').readlines()
                        print('         line with pair -> ' + the_line[line_number - 1])
                        the_line[line_number - 1] = line.strip() + ',' + port + '\n'
                        open('final_output.txt','w+').write(''.join(the_line))
                    
                    not_in = False

            if not_in == True:
                read_obj.write(ipandport_home + '\n')
            else:
                print('ip was in file')

                    
