import tkinter.ttk as ttk
import tkinter as tk

import logging
import core
import os



class MechKeys :
	def __init__ (self) :
		# initialize window
		self.window = tk.Tk()

		self.window.title('Mech keys / v1.0')

		self.window.geometry('400x500')
		self.window.resizable(False, False)

		icon = tk.PhotoImage(file='theme/icon.png')

		self.window.iconphoto(False, icon)

		# theme handler
		core.theme.initTheme(self.window)
		core.theme.setTheme(self.window, 'dark')

		# sound
		self.soundPacks = ['Select sound pack'] + os.listdir('sounds')

		self.soundHandler = core.sound.Sound()


	def loadSound(self, soundPack) :
		self.soundHandler.loadSound(soundPack)


	def run(self) :
		# select sound
		self.soundPackVar = tk.StringVar(self.window)
		self.soundPackOption = ttk.OptionMenu(self.window,
			self.soundPackVar,
			*self.soundPacks,
			command=self.loadSound)

		self.soundPackOption.config(width=50)
		self.soundPackOption.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

		# start sound
		ttk.Button(self.window,
			text='Start sound',
			command=self.soundHandler.startStream).grid(row=1, column=0, columnspan=3, padx=10, pady=10)

		# contact info
		ttk.Button(self.window,
			text='website',
			command=lambda:os.system('start https://ivan-resetnikov.000webhostapp.com/')).grid(row=2, column=0, padx=10, pady=100)

		ttk.Button(self.window,
			text='patreon',
			command=lambda:os.system('start https://www.patreon.com/join/9723605?u=9723605')).grid(row=2, column=1, padx=10, pady=100)

		ttk.Button(self.window,
			text='email',
			command=lambda:os.system('start mailto:ivan.resetnikov@proton.me')).grid(row=2, column=2, padx=10, pady=100)

		# copyright
		

		self.window.mainloop()
		logging.info('Stopped program')


if __name__ == '__main__':
	MechKeys().run()