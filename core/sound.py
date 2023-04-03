import pygame as pg
import threading
import logging
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
		packs = os.listdir(f'sounds/{name}/')

		logging.info(f'Availible packs: {packs}')
		
		logging.debug(f'Loading pack: {name}')

		for soundFile in packs :
			self.keys[soundFile[:-4:]] = loadSoundFile(f'sounds/{name}/{soundFile}')

		logging.info(f'Loaded keys: {self.keys}')


	def streamThread(self) -> None:
		self.pressed = []

		with pynput.keyboard.Listener(on_press=self.press, on_release=self.release) as listener:
			listener.join()


	def startStream(self) -> None:
		self.stream.start()


	def setVolume(self, volume:int) -> None:
		self.press.set_volume(volume)


	def press(self, key) -> None:
		keyName = str(key)[4::]

		try:
			if not str(key) in self.pressed :
				if keyName in tuple(self.keys.keys()):
					self.keys[keyName].play()
				else:
					self.keys['other'].play()

				self.pressed.append(str(key))

		except AttributeError:
			print('[x] No sound pack loaded')


	def release(self, key) :
		try:
			self.pressed.remove(str(key))
		except ValueError:
			self.pressed = []