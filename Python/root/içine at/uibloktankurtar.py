import wndMgr
import ui
import app
import player

BUTTON_IMAGE_PATHS = {
	"up": "d:/ymir work/ui/buton/bkurtar_1.tga",
	"over": "d:/ymir work/ui/buton/bkurtar_2.tga",
	"down": "d:/ymir work/ui/buton/bkurtar_3.tga"
}

class BloktanKurtar(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Initialize()
		self.questionDialog = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Initialize(self):
		self.SixTails = None
		self.board = None

	def Destroy(self):
		self.ClearDictionary()
		self.SixTails = None
		self.board = None
		self.questionDialog = None

	def Open(self):

		self.SetPosition(110, wndMgr.GetScreenHeight() - 110)
		self.SetTop()
		self.SetSize(32, 50)
		self.AddFlag('movable')
		self.SixTails = ui.Button()
		self.SixTails.SetParent(self)
		self.SixTails.SetUpVisual(BUTTON_IMAGE_PATHS["up"])
		self.SixTails.SetOverVisual(BUTTON_IMAGE_PATHS["over"])
		self.SixTails.SetDownVisual(BUTTON_IMAGE_PATHS["down"])
		self.SixTails.SetEvent(ui.__mem_func__(self.show_board))
		self.SixTails.SetPosition(0, 0)
		self.SixTails.SetTop()
		self.SixTails.Show()
		self.Hide()

	def GosterGizle(self, i):
		if i:
			self.Show()
		else:
			self.Hide()

	def show_board(self):
		if self.questionDialog and self.questionDialog.IsShow():
			self.questionDialog.Close()
			return
		else:
			if self.questionDialog is not None:
				self.questionDialog.Close()

		import uiCommon
		questionDialog = uiCommon.SixTailsBugDialog()
		questionDialog.SetText("Bloktan kurtulmak mý istiyorsunuz?")
		questionDialog.SetAcceptEvent(lambda arg = True: self.yes_button_event(arg))
		questionDialog.SetCancelEvent(lambda arg = False: self.yes_button_event(arg))
		questionDialog.Open()
		self.questionDialog = questionDialog

	def button_event(self, accept):
		if accept:
			player.BloktanKurtar()
		self.board.Hide()

	def yes_button_event(self, answer):
		if not self.questionDialog:
			return

		self.questionDialog.Close()

		if not answer:
			return

		player.BloktanKurtar()
		self.GosterGizle(False)
		return True

	def BloktanKurtar(self):
		player.BloktanKurtar()
		self.GosterGizle(False)
