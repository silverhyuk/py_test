from ctypes import *
import sys
import win32gui
import win32api
import win32con
import time
from datetime import datetime

class window:
    def sendMessage(self, windowName, message):
        try:
            '''메인창 이름을 가지고 창을 추적'''
            hwndMain = win32gui.FindWindow(None, windowName)
            hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

            '''하위 창 확인 / Kakao Editor'''
            hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RichEdit20W", None)

            '''메시지를 에디터에 등록'''
            win32gui.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, message)

            '''메시지 전송 요청 / Enter 입력'''
            win32api.PostMessage(hwndEdit, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        except win32gui.error:
            print('요청한 창이 존재하지 않습니다.')


# windowName = input("카카오톡 대화창 이름을 입력하세요...(예. HYUK) : ")
# message    = input("전송할 메시지를 입력하세요... : ")

"""
콘솔 입력 키를 기준으로 메시지 전송
> python window.py "창이름" "메시지 전송 내용"
"""
windowName = sys.argv[1]
message = sys.argv[2]

'''입력 값이 먼지 확인하기 위해 한번 찍어봄'''
print(windowName)

kakao = window()

for i in range(500):
    now = datetime.now()
    kakao.sendMessage(windowName, ('%s-%s-%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)))
    time.sleep(1)
