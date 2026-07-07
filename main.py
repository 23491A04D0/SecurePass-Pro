"""
====================================================
 SecurePass Pro

 Application Launcher

====================================================
"""


from src.splash import SplashScreen
from src.ui import SecurePassUI



splash=SplashScreen()

splash.show()



app=SecurePassUI()

app.run()