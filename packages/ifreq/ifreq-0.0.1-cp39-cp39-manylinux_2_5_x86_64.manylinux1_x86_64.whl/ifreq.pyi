
class ifreq:
	''' Control Network Interface In Object Oriented Method. '''

	def ifr_name (ifname:str=None) -> str:
		'''  'ifr_name' variable.\n
			Returns the 'ifr_name' value if ifname is None\n
			else 'ifr_name' is set to 'ifname'. '''
	def ifr_ifindex (ifindex:int=None) -> str:
		'''  'ifr_ifindex' variable.\n
			Returns the 'ifr_ifindex' value if ifindex is None\n
			else 'ifr_ifindex' is set to 'ifindex'.  '''
	def ifr_newname (newname:int) -> str:
		'''  'ifr_newname' variable.\n
			'ifr_newname' is set to 'newname'. '''


	def get_if_index (sock:int) -> int:
		'''  Get interface index from interface mapping according to 'ifr_name' value.
			On success, interface index is stored in 'ifr_ifindex' variable  and 0 is returned.
			On error, -1 is returned. '''
	def get_if_name (sock:int) -> int:
		'''  Get interface name according to 'ifr_ifindex' value.\n
			On success, interface name is stored in 'ifr_name' variable and 0 is returned.\n
			On error, -1 is returned. '''
	def set_if_name (sock:int) -> int:
		'''  Set interface name according to 'ifr_newname' value.
			On success, interface name is changed according to 'ifr_newname' variable  and 0 is returned.
			On error, -1 is returned. '''
