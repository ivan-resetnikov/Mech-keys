import ctypes as ct



def setTitlebarTheme(window, theme):
	values = {'light': 0, 'dark': 2}

	window.update()
	DWMWA_USE_IMMERSIVE_DARK_MODE = 20
	set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
	get_parent = ct.windll.user32.GetParent
	hwnd = get_parent(window.winfo_id())
	rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
	value = values[theme]
	value = ct.c_int(value)
	set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))


def initTheme(window):
	window.tk.call('source', 'theme.tcl')


def setTheme(window, theme):
	window.tk.call('set_theme', theme)
	setTitlebarTheme(window, theme)