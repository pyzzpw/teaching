import qrcode 
img = qrcode.make('山上还有山-打一字')
# 保存二维码
img.save('hello.png')
# 展示二维码
img.show()