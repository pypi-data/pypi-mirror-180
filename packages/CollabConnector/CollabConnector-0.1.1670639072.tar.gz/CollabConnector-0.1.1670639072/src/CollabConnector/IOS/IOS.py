import sys
import threading
import time
import getpass
import re

try:
	import netmiko
except:
	print("To Interact with devices via SSH install netmiko.", file=sys.stderr)
	print(f"<< pip3 install netmiko >>", file=sys.stderr)

try:
	import netconf
except:
	print("For some of the config parsing we use NETCONF which isn't installed.", file=sys.stderr)
	print(f"<< pip3 install netconf >>", file=sys.stderr)


class Connect():
	keep_system_alive = True
	config = []
	interface_status = []
	speed = { 'half': [], 'ten': [] }
	hostname = None
	domain = None
	ip = {}
	inventory = []
	version = None
	cdp = {}

	def __init__(self, *args, **kwargs):
		if args or kwargs:
			if args and isinstance(args[0], dict):
				self.deviceLogin = args[0]
			elif kwargs:
				self.deviceLogin = kwargs
		if len(args) == 3:
			ipaddress, username, password = args
		else:
			self.deviceLogin = {'ip': input("IP Address: "), 'username': input("Username: "), 'password': getpass.getpass()}

		self.deviceLogin['device_type'] = 'cisco_ios'
		self.deviceLogin['keepalive'] = 10

		# setup ssh connection to the switch
		try:
			self.netmiko = netmiko.ConnectHandler(**self.deviceLogin)
			self.netmiko.enable()
			self.netmiko.disable_paging(command='terminal length 0', delay_factor=1, cmd_verify=True, pattern=None)

		except Exception as err:
			print(f"Cannot connect to this device: {err}", file=sys.stderr)
			self = False

		else:
			self.status = True
			print(f"Connected to device: {self.deviceLogin['ip']}", file=sys.stderr)

			# send find_prompt() in background every 30sec to keep session alive
			keepalive = threading.Thread(target=self.session_keepalive,args=()) # create thread process
			keepalive.daemon = True  # enable run in background
			keepalive.start() 		 # start keepalives

		self.config = self.fix_file_format(self.parse_config(self.show_run()))

	def exec(self, *commands, auto_confirm=False):
		send_commands = []
		for arg in commands:
			if isinstance(arg,list):
				for each in arg:
					send_commands.append(each)

			else:
				send_commands.append(arg)

		if not self.status:
			try:
				self.netmiko.establish_connection()
				self.netmiko.enable()
				self.netmiko.disable_paging(command='terminal length 0', delay_factor=1, cmd_verify=True, pattern=None)
			except Exception as err:
				print(f"Cannot reestablish SSH connection to: {self.deviceLogin['ip']}", file=sys.stderr)
			else:
				self.status = True

		if self.status:
			output = []
			for command in send_commands:
				# if show command use send_command using auto find promptr return
				if re.search("^sh",command):
					try:
						command_out = self.netmiko.send_command(command,cmd_verify=True,strip_prompt=False).splitlines() #.splitlines() to plit lines into list

					except Exception as err:
						print(f"Error sending commands: {err}", file=sys.stderr)
						command_out = False

					if command_out and not re.search("\% Invalid input detected at ",str(command_out)):
						command_out.pop()
						output.append('\n'.join(command_out))
					else:
						print(f"Syntax Error: {command} - {command_out}", file=sys.stderr)
						output.append(False)

				else:
					# else send via command timing to catch confirmations
					try:
						command_out = self.netmiko.send_command_timing(command,cmd_verify=True,strip_prompt=False) #.splitlines() to plit lines into list
						if auto_confirm:
							while re.search("\]$",command_out) or re.search("\?$",command_out.strip()):
								print(f"{command} - {command_out} - Auto Confirming")
								try:
									command_out = self.netmiko.send_command_timing("")
								except:
									print(f"Error sending commands: {err}", file=sys.stderr)
									break

						output.append(command_out)

					except Exception as err:
						print(f"Error sending commands: {err}", file=sys.stderr)
						output.append(False)					

			return output

		else:
			return False

	def show_run(self):
		return self.exec("show running-config")

	def show_tech(self):
		return self.exec("show tech-support")

	def save(self):
		current_time = int(time.time())
		if self.exec(f'copy start {current_time}_Running-Config.txt'):
			if self.exec('copy run start'):
				return True 
	
		print("Error saving IOS config.", file=sys.stderr)
		return False

	def wr(self):
		return self.save()

	def config_t(self, *commands):
		send_commands = []
		for arg in commands:
			if isinstance(arg,list):
				for each in arg:
					send_commands.append(each)
			else:
				send_commands.append(arg)
		if not self.status:
			try:
				self.netmiko.establish_connection()
				self.netmiko.enable()
				self.netmiko.disable_paging(command='terminal length 0', delay_factor=1, cmd_verify=True, pattern=None)

			except Exception as err:
				print(f"Cannot reestablish SSH connection to: {self.deviceLogin['ip']}", file=sys.stderr)

			else:
				self.status = True

		if self.status:
			try:
				output = self.netmiko.send_config_set(send_commands)

			except Exception as err:
				print(f"Error sending commands: {err}", file=sys.stderr)
				return False

			else:
				return output
		else:
			return False

	def exit(self):
		self.keep_system_alive = False 
		self.netmiko.cleanup(command='exit')
		return True

	# Keepalive for o365 token in backgroung.  Renew every 10min before expures timer
	def session_keepalive(self):
		while True and self.keep_system_alive:
			time.sleep(30)

			# get prompt place to keep session alive
			try:
				self.netmiko.find_prompt()

			except Exception as err:
				print(f"Lost connection to IOS device: {self.deviceLogin['ip']}", file=sys.stderr)
				break

		self.status = False

	def parse_config(self, config=None):
		if config:
			config_list = config.splitlines()
		else:
			config_list = self.config
		x = -1
		while x < len(self.config_list) - 1:
			x += 1

			# parse running config output
			if x < len(self.config_list) and re.match(".*#sh* run*", self.config_list[x]):
				while True:
					x += 1
					if "#" in self.config_list[x]:
						break
					if "ip domain-name" in self.config_list[x]:
						self.domain = self.config_list[x].split(" ")[-1].strip()

					if "hostname" in self.config_list[x]:
						self.hostname = self.config_list[x].split(" ")[-1].strip()
					elif "#" in self.config_list[x]:
						self.hostname = self.config_list[x].split("#")[0].strip()

					if self.config_list[x].find("interface") == 0:
						this_interface = "".join(self.config_list[x].split(' ')[1:]).replace('\n', '')
						while x < len(self.config_list) and "!" not in self.config_list[x]:
							if "ip address" in self.config_list[x]:
								self.ip[this_interface] = [self.config_list[x].split(" ")[-2],
														   self.config_list[x].split(" ")[-1].strip()]
								break
							x += 1

			# Parse show inventory output
			if x < len(self.config_list) and re.match(".*#sh* inv*", self.config_list[x]):
				while x < len(self.config_list):
					x += 1
					if "#" in self.config_list[x]:
						break

					if 'NAME' in self.config_list[x]:
						that_pid = {}
						pid = f"{self.config_list[x]}, {self.config_list[x + 1]}".replace('\n', '')
						i = 1
						this_pid = pid.split('"')
						while i < len(this_pid):
							this_pid[i] = this_pid[i].replace(",", "")
							i += 2

						this_pid = '"'.join(this_pid).replace('"', '').split(',')
						for pid_line in this_pid:

							try:
								that_pid[pid_line.split(':')[0].strip()] = pid_line.split(':')[1].replace('"',
																										  '').replace(
									"\'", '').strip()
							except Exception as err:
								print(f"Error: {self.config_list[x]} - {pid_line} - {err}")
								that_pid = None

						self.inventory.append(that_pid)
						x += 1

			# Find version for show version
			if x < len(self.config_list) and self.config_list[x].find("System image file is ") == 0:
				self.version = self.config_list[x].split(":")[-1].replace('"', '').split('/')[-1].replace('\n', '')

			# Parse show cdp neightbor detail
			if x < len(self.config_list) and re.match(".*#sh* cdp* nei* d*", self.config_list[x]):
				x += 1
				cdp_neighbor = {}
				while self.config_list[x].find("#") < 0:
					if self.config_list[x].find("---") == 0:
						if "Interface" in cdp_neighbor.keys():
							if "Capabilities" in cdp_neighbor.keys():
								cdp_neighbor['Capabilities'] = cdp_neighbor['Capabilities'].split(' ')
							self.cdp[cdp_neighbor['Interface']] = cdp_neighbor
						cdp_neighbor = {}

						x += 1

					else:
						if self.config_list[x].find("Entry address") == 0:
							cdp_neighbor['Entry address'] = []
							x += 1
							while x < len(self.config_list) and re.match(".*IP* address*", self.config_list[x]):
								cdp_neighbor['Entry address'].append(
									":".join(self.config_list[x].split(':')[1:]).strip().replace('\n', ''))
								x += 1

						if self.config_list[x].find("Management address") == 0:
							cdp_neighbor['Management address'] = []
							x += 1
							while x < len(self.config_list) and re.match(".*IP* address*", self.config_list[x]):
								cdp_neighbor['Management address'].append(
									self.config_list[x].split(':')[1].strip().replace('\n', ''))
								x += 1

						if self.config_list[x].find("Version") == 0:
							x += 1
							cdp_neighbor['Version'] = self.config_list[x].replace('\n', '')
							while x < len(self.config_list) and not self.config_list[x].strip() == "":
								x += 1

						for line in self.config_list[x].split(','):
							if not self.config_list[x].strip() == "":
								cdp_neighbor[line.split(":")[0].strip()] = line.split(":")[1].strip().replace('\n', '')

						x += 1

	# parse show interface status to get half and 10MB links
	def parse_interface_status(self, show=['ten', 'half']):
		start = None
		i = 0
		while i < len(self.config_list):
			if "show int status" in self.config_list[i] or "sh int status" in self.config_list[
				i] or "show interface status" in self.config_list[i]:
				start = i + 1

			elif start is not None and "#" not in self.config_list[i] and '/' in self.config_list[i]:
				line = re.sub(" +", " ", self.config_list[i]).split(' ')
				self.interface_status.append([line[0], line[-3], line[-2]])

				if "half" in line[-3]:
					issues = True
					self.speed['half'].append(line[0])

				if line[-2].split('-')[-1] == '10':
					issues = True
					interface = line[0].replace("Fa", "FastEthernet").replace("Gi", "GigabitEthernet")
					if len(self.cdp) > 0 and interface in self.cdp.keys():
						self.speed['ten'].append(
							f"{line[0]} - {self.cdp[interface]['Platform']} {self.cdp[interface]['Device ID']}")
					else:
						self.speed['ten'].append(line[0])

			elif start is not None and "#" in self.config_list[i]:
				break

			i += 1

		print("Parse Complete!")

		if issues is False:
			print(f"{self.hostname} - No 10/half issues")

		else:
			if 'ten' in show:
				print(f"{self.hostname} - Half Duplex Interfaces {self.speed['half']}")
			if 'half' in show:
				print(f"{self.hostname} - 10MB Interfaces {self.speed['ten']}")

	def fix_file_format(self, file):
		if file is None:
			return self.config
		elif type(file) == str:
			return file.split("\n")
		elif type(file) == io.TextIOWrapper:
			return file.readlines()
		elif type(file) == list:
			return file
		else:
			print("Error: IOS.section must be given a text file via string, file or list", file=sys.stderr)
			return []

	def section(self, search, file=None):
		file_lines = self.fix_file_format(file)
		i = 0
		while i < len(file_lines):
			if file_lines[i].lower().find(search.lower()) > -1:
				print(file_lines[i])
				while file_lines[i].find("!") != 0:
					i += 1
					print(file_lines[i])
			i += 1

	def include(self, search, file=None):
		for line in self.fix_file_format(file):
			if line.lower().find(search.lower()) > -1:
				print(line)
