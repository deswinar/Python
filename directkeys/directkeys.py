# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes, win32gui, win32api, win32con
import time

SendInput = ctypes.windll.user32.SendInput

KEY_ESCAPE = 0x01
KEY_1 = 0x02
KEY_2 = 0x03
KEY_3 = 0x04
KEY_4 = 0x05
KEY_5 = 0x06
KEY_6 = 0x07
KEY_7 = 0x08
KEY_8 = 0x09
KEY_9 = 0x0A
KEY_0 = 0x0B
KEY_MINUS = 0x0C
KEY_EQUALS = 0x0D
KEY_BACK = 0x0E
KEY_TAB = 0x0F
KEY_Q = 0x10
KEY_W = 0x11
KEY_E = 0x12
KEY_R = 0x13
KEY_T = 0x14
KEY_Y = 0x15
KEY_U = 0x16
KEY_I = 0x17
KEY_O = 0x18
KEY_P = 0x19
KEY_LBRACKET = 0x1A
KEY_RBRACKET = 0x1B
KEY_RETURN = 0x1C
KEY_LCONTROL = 0x1D
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20
KEY_F = 0x21
KEY_G = 0x22
KEY_H = 0x23
KEY_J = 0x24
KEY_K = 0x25
KEY_L = 0x26
KEY_SEMICOLON = 0x27
KEY_APOSTROPHE = 0x28
KEY_GRAVE = 0x29
KEY_LSHIFT = 0x2A
KEY_BACKSLASH = 0x2B
KEY_Z = 0x2C
KEY_X = 0x2D
KEY_C = 0x2E
KEY_V = 0x2F
KEY_B = 0x30
KEY_N = 0x31
KEY_M = 0x32
KEY_COMMA = 0x33
KEY_PERIOD = 0x34
KEY_SLASH = 0x35
KEY_RSHIFT = 0x36
KEY_MULTIPLY = 0x37
KEY_LALT = 0x38
KEY_SPACE = 0x39
KEY_CAPSLOCK = 0x3A
KEY_F1 = 0x3B
KEY_F2 = 0x3C
KEY_F3 = 0x3D
KEY_F4 = 0x3E
KEY_F5 = 0x3F
KEY_F6 = 0x40
KEY_F7 = 0x41
KEY_F8 = 0x42
KEY_F9 = 0x43
KEY_F10 = 0x44
KEY_NUMLOCK = 0x45
KEY_SCROLL = 0x46
KEY_NUMPAD7 = 0x47
KEY_NUMPAD8 = 0x48
KEY_NUMPAD9 = 0x49
KEY_SUBTRACT = 0x4A
KEY_NUMPAD4 = 0x4B
KEY_NUMPAD5 = 0x4C
KEY_NUMPAD6 = 0x4D
KEY_ADD = 0x4E
KEY_NUMPAD1 = 0x4F
KEY_NUMPAD2 = 0x50
KEY_NUMPAD3 = 0x51
KEY_NUMPAD0 = 0x52
KEY_DECIMAL = 0x53
KEY_F11 = 0x57
KEY_F12 = 0x58
KEY_F13 = 0x64
KEY_F14 = 0x65
KEY_F15 = 0x66
KEY_KANA = 0x70
KEY_CONVERT = 0x79
KEY_NOCONVERT = 0x7B
KEY_YEN = 0x7D
KEY_NUMPADEQUALS = 0x8D
KEY_CIRCUMFLEX = 0x90
KEY_AT = 0x91
KEY_COLON = 0x92
KEY_UNDERLINE = 0x93
KEY_KANJI = 0x94
KEY_STOP = 0x95
KEY_AX = 0x96
KEY_UNLABELED = 0x97
KEY_NUMPADENTER = 0x9C
KEY_RCONTROL = 0x9D
KEY_NUMPADCOMMA = 0xB3
KEY_DIVIDE = 0xB5
KEY_SYSRQ = 0xB7
KEY_RMENU = 0xB8
KEY_HOME = 0xC7
KEY_UP = 0xC8
KEY_PGUP = 0xC9
KEY_LEFT = 0xCB
KEY_RIGHT = 0xCD
KEY_END = 0xCF
KEY_DOWN = 0xD0
KEY_PGDN = 0xD1
KEY_INSERT = 0xD2
KEY_DELETE = 0xD3
KEY_LWIN = 0xDB
KEY_RWIN = 0xDC
KEY_APPS = 0xDD

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
        _fields_ = [("wVk", ctypes.c_ushort),
                    ("wScan", ctypes.c_ushort),
                    ("dwFlags", ctypes.c_ulong),
                    ("time", ctypes.c_ulong),
                    ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
        _fields_ = [("uMsg", ctypes.c_ulong),
                    ("wParamL", ctypes.c_short),
                    ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
        _fields_ = [("dx", ctypes.c_long),
                    ("dy", ctypes.c_long),
                    ("mouseData", ctypes.c_ulong),
                    ("dwFlags", ctypes.c_ulong),
                    ("time",ctypes.c_ulong),
                    ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
        _fields_ = [("ki", KeyBdInput),
                    ("mi", MouseInput),
                    ("hi", HardwareInput)]

class Input(ctypes.Structure):
        _fields_ = [("type", ctypes.c_ulong),
                    ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

class Mouse:
    """It simulates the mouse"""
    MOUSEEVENTF_MOVE = 0x0001 # mouse move 
    MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down 
    MOUSEEVENTF_LEFTUP = 0x0004 # left button up 
    MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down 
    MOUSEEVENTF_RIGHTUP = 0x0010 # right button up 
    MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down 
    MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up 
    MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled 
    MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move 
    SM_CXSCREEN = 0
    SM_CYSCREEN = 1

    def _do_event(self, flags, x_pos, y_pos, data, extra_info):
        """generate a mouse event"""
        x_calc = 65536L * x_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CXSCREEN) + 1
        y_calc = 65536L * y_pos / ctypes.windll.user32.GetSystemMetrics(self.SM_CYSCREEN) + 1
        return ctypes.windll.user32.mouse_event(flags, x_calc, y_calc, data, extra_info)

    def _get_button_value(self, button_name, button_up=False):
        """convert the name of the button into the corresponding value"""
        buttons = 0
        if button_name.find("right") >= 0:
            buttons = self.MOUSEEVENTF_RIGHTDOWN
        if button_name.find("left") >= 0:
            buttons = buttons + self.MOUSEEVENTF_LEFTDOWN
        if button_name.find("middle") >= 0:
            buttons = buttons + self.MOUSEEVENTF_MIDDLEDOWN
        if button_up:
            buttons = buttons << 1
        return buttons

    def move_mouse(self, pos):
        """move the mouse to the specified coordinates"""
        (x, y) = pos
        old_pos = self.get_position()
        x =  x if (x != -1) else old_pos[0]
        y =  y if (y != -1) else old_pos[1]    
        self._do_event(self.MOUSEEVENTF_MOVE + self.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

    def press_button(self, pos=(-1, -1), button_name="left", button_up=False):
        """push a button of the mouse"""
        self.move_mouse(pos)
        self._do_event(self._get_button_value(button_name, button_up), 0, 0, 0, 0)

    def click(self, pos=(-1, -1), button_name= "left"):
        """Click at the specified placed"""
        self.move_mouse(pos)
        self._do_event(self._get_button_value(button_name, False)+self._get_button_value(button_name, True), 0, 0, 0, 0)

    def double_click (self, pos=(-1, -1), button_name="left"):
        """Double click at the specifed placed"""
        for i in xrange(2): 
            self.click(pos, button_name)

    def get_position(self):
        """get mouse position"""
        return win32api.GetCursorPos()

mouse = Mouse()
#while True:
        #mouse.move_mouse((500, 500))
