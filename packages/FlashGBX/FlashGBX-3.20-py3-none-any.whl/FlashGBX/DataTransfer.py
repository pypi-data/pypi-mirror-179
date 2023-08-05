# -*- coding: utf-8 -*-
# FlashGBX
# Author: Lesserkuma (github.com/lesserkuma)

import traceback
from . import pyside as PySide2

class DataTransfer(PySide2.QtCore.QThread):
	CONFIG = None
	FINISHED = False
	
	updateProgress = PySide2.QtCore.Signal(object)

	def __init__(self, config=None):
		PySide2.QtCore.QThread.__init__(self)
		if config is not None:
			self.CONFIG = config
		self.FINISHED = False
	
	def setConfig(self, config):
		self.CONFIG = config
		self.FINISHED = False
	
	def isRunning(self):
		return not self.FINISHED
	
	def run(self):
		try:
			if self.CONFIG == None:
				pass
			
			else:
				self.FINISHED = False
				self.CONFIG['port'].TransferData(self.CONFIG, self.updateProgress)
				self.FINISHED = True
		
		except Exception as e:
			traceback.print_exc()
			self.updateProgress.emit({"action":"ABORT", "info_type":"msgbox_critical", "info_msg":"An unresolvable error has occured. See console output for more information. Reconnect the device, restart the software and try again.\n\n{:s}: {:s}".format(type(e).__name__, str(e)), "abortable":False})
			self.FINISHED = True
