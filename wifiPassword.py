import subprocess,, re

def main():
	command1 = "netsh wlan show profile"
	networks = subprocess.check_output(command1,shell=True)
	network_list = re.findall('(?:profile\s*:\s)(.*)',networks)

	output = ""
	for network in network_list:
		comamnd2 =  "netsh wlan show profile " +network + " key=clear"
		one_network_result = subprocess.check_output(command2, shell=True)
		output += one_network_result
	return output
if __name__ == "__main__":
	print(main())
