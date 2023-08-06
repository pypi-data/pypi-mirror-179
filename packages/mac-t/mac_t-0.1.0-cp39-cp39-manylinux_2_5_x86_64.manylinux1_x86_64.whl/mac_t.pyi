
class mac_t:
	'''class for MAC(Media Access Control)'''

	def __eq__(self, __o: object) -> bool: ...
	def __ne__(self, __o: object) -> bool: ...
	def __repr__(self) -> str: ...

	def from_string(self, string: str) -> int:
		'''	
		Convert MAC from string to byte.\n
		On success, 17 is returned.\n
		On error, <17, -1 is returned.\n
			<17 : if string length is <17.\n
			-1  : if string is in wrong format.
		'''
		pass

	def to_string(self) -> str:
		'''
		Convert mac to string.
		'''
		pass

