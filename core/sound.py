import pygame as pg
import threading
import pynput
import os

pg.mixer.init()



def loadSoundFile(path:str, vol:float=0.25) -> pg.mixer.Sound:
	sound = pg.mixer.Sound(path)
	sound.set_volume(vol)
	return sound



class Sound :
	def __init__(self):
		self.stream = threading.Thread(target=self.streamThread)


	def loadSound(self, name:str) -> None:
		self.keys = {}

		for soundFile in os.listdir(f'sounds/{name}/') :
			self.keys[soundFile[:-4:]] = loadSoundFile(f'sounds/{name}/{soundFile}')


	def streamThread(self) -> None:
		with pynput.keyboard.Listener(on_press=self.play) as listener:
			listener.join()


	def startStream(self) -> None:
		self.stream.start()


	def setVolume(self, volume:int) -> None:
		self.press.set_volume(volume)


	def play(self, key) -> None:
		keyName = str(key)[4::]

		try:
			if keyName in tuple(self.keys.keys()):
				self.keys[keyName].play()
			else:
				self.keys['other'].play()

		except AttributeError:
			print('Error: No sound pack loaded')