from PIL import ImageGrab
import pyautogui 
import time

'''
自动翻页+截图 
@Leon Guo 
'''
#需要一个封面来确定这个PDF在屏幕中的位置以确定截图区域
region = pyautogui.locateOnScreen('cover.png')
left,top,width,height = region 
x_right = left + width 
y_right = top+ height

# parms: left_x,left_y,right_x,right_y
real_region = (left, top, x_right, y_right) 

pyautogui.moveTo(left, top,duration=2) 
# 因为未知原因自动点击无效 所以看到这句提示时需要手动点击一下pdf
print("pls click the pdf")
time.sleep(5)
pyautogui.moveTo(x_right+100, y_right) 


print('we strat ~~~~')
for i in range(1,180):
    im = ImageGrab.grab(real_region)
    pyautogui.press('right')
    print(f'Saving the {i} page') 
    im.save(f'book/{i}.png') 

# 这个输出的图片尺寸将会在pdf合并程序上使用 
# @TODO 未来完成：自动调用合并程序
print('pic size',width,height)
print('done！')