import pygame as pg
import threading
import pynput
import os

pg.mixer.init()



def loadSoundFile(path:str, vol:float=0.3) -> pg.mixer.Sound:
	sound = pg.mixer.Sound(path)
	sound.set_volume(vol)
	return sound


class Sound :
	def __init__(self, name:str):
		self.loadSound(name)

		self.stream = threading.Thread(target=self.streamThread)


	def loadSound(self, name:str):
		self.keys = {}

		for soundFile in os.listdir('sounds/') :
			self.keys[soundFile[:-4:]] = loadSoundFile(f'sounds/{soundFile}')


	def streamThread(self):
		with pynput.keyboard.Listener(on_press=self.play) as listener:
			listener.join()


	def startStream(self):
		self.stream.start()


	def stopStream(self):
		self.stream.stop()


	def setVolume(self, volume:int) -> None:
		self.press.set_volume(volume)


	def play(self, key) -> None:
		keyName = str(key)[4::]
		if keyName in tuple(self.keys.keys()):
			self.keys[keyName].play()
		else:
			self.keys['other'].play()