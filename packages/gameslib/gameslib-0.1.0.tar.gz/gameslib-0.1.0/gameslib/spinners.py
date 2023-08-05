def __prr__(text):
	print(text, end="\r")

class line1:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("|")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("/")
					self.currentp += 1
				case 2:
					__prr__("-")
					self.currentp += 1
				case 3:
					__prr__("\\")
					self.currentp += 1
				case 4:
					__prr__("|")
					self.currentp = 0
	def end(self, text):
		__prr__(text)


class line2:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("-  ")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__(" - ")
					self.currentp += 1
				case 2:
					__prr__("  -")
					self.currentp += 1
				case 3:
					__prr__(" - ")
					self.currentp += 1
				case 4:
					__prr__("-  ")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class line3:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[-  ]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[ - ]")
					self.currentp += 1
				case 2:
					__prr__("[  -]")
					self.currentp += 1
				case 3:
					__prr__("[ - ]")
					self.currentp += 1
				case 4:
					__prr__("[-  ]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class dot1:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("•  ")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__(" • ")
					self.currentp += 1
				case 2:
					__prr__("  •")
					self.currentp += 1
				case 3:
					__prr__(" • ")
					self.currentp += 1
				case 4:
					__prr__("•  ")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class dot2:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[•  ]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[ • ]")
					self.currentp += 1
				case 2:
					__prr__("[  •]")
					self.currentp += 1
				case 3:
					__prr__("[ • ]")
					self.currentp += 1
				case 4:
					__prr__("[•  ]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo1:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("►  ")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__(" ► ")
					self.currentp += 1
				case 2:
					__prr__("  ◄")
					self.currentp += 1
				case 3:
					__prr__(" ◄ ")
					self.currentp += 1
				case 4:
					__prr__("►  ")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo2:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[►  ]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[ ► ]")
					self.currentp += 1
				case 2:
					__prr__("[  ◄]")
					self.currentp += 1
				case 3:
					__prr__("[ ◄ ]")
					self.currentp += 1
				case 4:
					__prr__("[►  ]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo3:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("►  ")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("►► ")
					self.currentp += 1
				case 2:
					__prr__("►►►")
					self.currentp += 1
				case 3:
					__prr__(" ►►")
					self.currentp += 1
				case 4:
					__prr__("  ►")
					self.currentp += 1
				case 5:
					__prr__("   ")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo4:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[►  ]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[►► ]")
					self.currentp += 1
				case 2:
					__prr__("[►►►]")
					self.currentp += 1
				case 3:
					__prr__("[ ►►]")
					self.currentp += 1
				case 4:
					__prr__("[  ►]")
					self.currentp += 1
				case 5:
					__prr__("[   ]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo5:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("  ◄")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__(" ◄◄")
					self.currentp += 1
				case 2:
					__prr__("◄◄◄")
					self.currentp += 1
				case 3:
					__prr__("◄◄ ")
					self.currentp += 1
				case 4:
					__prr__("◄  ")
					self.currentp += 1
				case 5:
					__prr__("   ")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo6:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[  ◄]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[ ◄◄]")
					self.currentp += 1
				case 2:
					__prr__("[◄◄◄]")
					self.currentp += 1
				case 3:
					__prr__("[◄◄ ]")
					self.currentp += 1
				case 4:
					__prr__("[◄  ]")
					self.currentp += 1
				case 5:
					__prr__("[   ]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)


class geo7:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("➼  ")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("➼➼ ")
					self.currentp += 1
				case 2:
					__prr__("➼➼➼")
					self.currentp += 1
				case 3:
					__prr__(" ➼➼")
					self.currentp += 1
				case 4:
					__prr__("  ➼")
					self.currentp += 1
				case 5:
					__prr__("   ")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class geo8:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[➼  ]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[➼➼ ]")
					self.currentp += 1
				case 2:
					__prr__("[➼➼➼]")
					self.currentp += 1
				case 3:
					__prr__("[ ➼➼]")
					self.currentp += 1
				case 4:
					__prr__("[  ➼]")
					self.currentp += 1
				case 5:
					__prr__("[   ]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)


class emoji1:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("☻")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("☺")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class emoji2:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[☻]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[☺]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class emoji3:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("★")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("☆")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class emoji4:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[★]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[☆]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class emoji5:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("♥")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("♡")
					self.currentp = 0
	def end(self, text):
		__prr__(text)

class emoji6:
	currentp = 0
	
	def spin(self):
		if self.currentp == 0:
			__prr__("[♥]")
			self.currentp += 1
		else:
			match self.currentp:
				case 0:
					pass
					self.currentp += 1
				case 1:
					__prr__("[♡]")
					self.currentp = 0
	def end(self, text):
		__prr__(text)