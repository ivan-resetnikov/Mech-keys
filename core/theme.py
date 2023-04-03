import logging
import ctypes



def setTitlebarTheme(window, theme):
	logging.debug(f'Changing title bar theme to {theme}')

	values = {'light': 0, 'dark': 2}

	window.update()
	ctypes.windll.dwmapi.DwmSetWindowAttribute(
		ctypes.windll.user32.GetParent(window.winfo_id()),
		20, ctypes.byref(ctypes.c_int(values[theme])),
		ctypes.sizeof(ctypes.c_int(values[theme])))


def initTheme(window):
	logging.info('Initializing theme.tcl')

	window.tk.call('source', 'theme.tcl')


def setTheme(window, theme):
	logging.info(f'Setting theme to {theme}')

	window.tk.call('set_theme', theme)
	setTitlebarTheme(window, theme)