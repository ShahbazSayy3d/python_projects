from plyer import notification
import time
import os

if __name__ == '__main__':
    title = "Please Take REST"
    message = "It is important for health!"
   
    
    icon_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'notify.ico')
    
    notification.notify(
        title=title,
        message=message,
        app_icon=icon_path,  
        timeout=5
    )
    time.sleep(50)

