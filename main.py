import tkinter.ttk as ttk
import tkinter as tk
import core



class MechKeys :
	def __init__ (self) :
		# initialize window
		self.window = tk.Tk()

		self.window.title('Mech keys / v1.0')

		self.window.geometry('500x500')
		self.window.resizable(False, False)

		# theme handler
		core.theme.initTheme(self.window)
		core.theme.setTheme(self.window, 'dark')

		# sound
		self.sound = core.sound.Sound('sound0')


	def run(self) :
		ttk.Button(self.window,
			text='Start sound',
			command=self.sound.startStream).grid(row=0, column=0, padx=10, pady=10)

		self.window.mainloop()


if __name__ == '__main__':
	MechKeys().run()