from PIL import ImageGrab
import time
import keyboard
import win32api, win32con

game_coords = [1000, 26, 1694, 260]

def check(x,y,rval,gval,bval,key,rval1,gval1,bval1):
    arrow = screen.getpixel((x, y))
    r, g, b = arrow
    if (r == rval and g == gval and b == bval):
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        time.sleep(0.005)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.02)
    if (r == rval1 and g == gval1 and b == bval1):
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        while (r == rval1 and g == gval1 and b == bval1):
            screen1 = ImageGrab.grab(bbox=game_coords)
            arrow = screen1.getpixel((x, y))
            rval1, gval1, bval1 = arrow
        #time.sleep(0.02)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)




while keyboard.is_pressed('p') == False:
    #mouse_pos = pyautogui.position()
    #mouse_x_pos = mouse_pos[0]
    #mouse_y_pos = mouse_pos[1]

    #if ((mouse_x_pos in range (game_coords[0],game_coords[2])) and (mouse_y_pos in range(game_coords[1],game_coords[3]))):
    screen = ImageGrab.grab(bbox=game_coords)
    check(104, 154, 194, 75, 153, win32con.VK_LEFT, 170, 110, 161)
    check(263, 154, 0, 255, 255, win32con.VK_DOWN, 54, 218, 222)
    check(426, 154, 18, 250, 5, win32con.VK_UP, 65, 215, 72)
    check(588, 154, 249, 57, 63, win32con.VK_RIGHT, 203, 99, 107)




