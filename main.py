import tkinter.ttk as ttk
import tkinter as tk
import core
import os




class MechKeys :
	def __init__ (self) :
		# initialize window
		self.window = tk.Tk()

		self.window.title('Mech keys / v1.0')

		self.window.geometry('500x500')
		self.window.resizable(False, False)

		icon = tk.PhotoImage(file='theme/icon.png')

		self.window.iconphoto(False, icon)

		# theme handler
		core.theme.initTheme(self.window)
		core.theme.setTheme(self.window, 'dark')

		# sound
		self.soundPacks = ['Select sound'] + os.listdir('sounds')

		self.soundHandler = core.sound.Sound()


	def loadSound(self, soundPack) :
		self.soundHandler.loadSound(soundPack)


	def run(self) :
		# start sound
		ttk.Button(self.window,
			text='Start sound',
			command=self.soundHandler.startStream).grid(row=0, column=0, padx=10, pady=10)

		self.soundPackVar = tk.StringVar(self.window)
		self.soundPackOption = ttk.OptionMenu(self.window,
			self.soundPackVar,
			*self.soundPacks,
			command=self.loadSound)

		self.soundPackOption.grid(row=0, column=1, padx=10, pady=10)

		self.window.mainloop()


if __name__ == '__main__':
	MechKeys().run()