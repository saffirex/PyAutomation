from plyer import notification

for i in range(1,5):
    notification.notify(title = 'testing',
        message = str(i),
        app_name= 'Bomber',
        app_icon = r"E:\Python\scripts\bomb.ico",
        ticker='nonono',
        toast='hihihii',
        timeout = 1)