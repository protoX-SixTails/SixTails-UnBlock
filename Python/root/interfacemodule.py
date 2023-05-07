### importlara Ekle: ###
if app.UNBLOCK_SYSTEM_ENABLED:
	import uibloktankurtar

### Arat: ###
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)
			self.wndDragonSoulRefine.SetInventoryWindows(self.wndInventory, self.wndDragonSoul)
			self.wndInventory.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)

### Altına Ekle: ###
		if app.UNBLOCK_SYSTEM_ENABLED:
			self.wndBloktanKurtar = uibloktankurtar.BloktanKurtar()

### Arat: ###
		# ACCESSORY_REFINE_ADD_METIN_STONE
		if self.wndItemSelect:
			if app.SIXTAILS_PACKFIX002:
				self.wndItemSelect.Hide()
			self.wndItemSelect.Destroy()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

### Altına Ekle: ###
		if app.UNBLOCK_SYSTEM_ENABLED:
			if self.wndBloktanKurtar:
				self.wndBloktanKurtar.Hide()
				self.wndBloktanKurtar.Destroy()

### Arat: ###
		del self.wndItemSelect

### Altına Ekle: ###
		if app.UNBLOCK_SYSTEM_ENABLED:
			del self.wndBloktanKurtar

### Arat: ###
	## PK Mode
	def OnChangePKMode(self):
		self.wndCharacter.RefreshAlignment()
		self.dlgSystem.OnChangePKMode()

### Altına Ekle: ###
	if app.UNBLOCK_SYSTEM_ENABLED:
		def BloktanKurtarOpen(self):
			self.wndBloktanKurtar.Open()

		def BloktanKurtarGuiGG(self, i):
			self.wndBloktanKurtar.GosterGizle(i)

		def BloktanKurtar(self):
			self.wndBloktanKurtar.BloktanKurtar()

### Arat: ###
		if self.wndExpandedTaskBar:
			self.wndExpandedTaskBar.Hide()

### Altına Ekle: ###
		if app.UNBLOCK_SYSTEM_ENABLED:
			if self.wndBloktanKurtar:
				self.wndBloktanKurtar.Hide()

### Arat: ###
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			hideWindows += self.wndDragonSoul,\
						self.wndDragonSoulRefine,

### Altına Ekle: ###
		if app.UNBLOCK_SYSTEM_ENABLED:
			if self.wndBloktanKurtar:
				hideWindows += self.wndBloktanKurtar,