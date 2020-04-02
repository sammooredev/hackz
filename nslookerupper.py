import datetime
import os
def nslookup_loop(output_path):
		#domain list file for lookup
		with open("domains.txt", "r") as domains_for_ns:
			#iterate through domains
			for domain in domains_for_ns:
				#strip whitespace/newlines
				fixed_domain = domain.strip()
				print("IPs grabbed for: " + fixed_domain)
				#ip regex
				grepip = r"([0-9]{1,3}[\.]){3}[0-9]{1,3}"
				#foobar is part of the awk command
				foobar = '/Name:/{val=$NF;flag=1;next} /Address:/ && flag{print $NF,val;val=""}'
				#lookup domain, grep ip from output, output to temporary work file
				os.system('nslookup ' + fixed_domain + ' |  awk ' + "'" + foobar + "'" + ' | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" | sort -u > temp_ns_outfile.txt')
				#append ip in work file to final ip list
				os.system('cat temp_ns_outfile.txt >> ' + date + '_for_masscan.txt')
#date			
grabdate = datetime.datetime.now().date()
date = str(grabdate)

nslookup_loop(output_path)