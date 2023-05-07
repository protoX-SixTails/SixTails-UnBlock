### Arat: ###

def StartGame(self):

### Altına Ekle: ###

		if app.UNBLOCK_SYSTEM_ENABLED:
			self.interface.BloktanKurtarOpen()

### En Alta Ekle: ###

	if app.UNBLOCK_SYSTEM_ENABLED:
		def BloktanKurtarici(self,gDurum):
			if self.interface:
				self.interface.BloktanKurtariciGui(True)