import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView 

class WebsiteApp(QMainWindow):
    def __init__(self):
        super(WebsiteApp, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.fiverr.com/zafranhaider?up_rollout=true#!"))  # Replace with your website's URL

        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Create navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Stop button
        stop_btn = QAction('Stop', self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Address bar
       #self.url_bar = QLineEdit()
        #self.url_bar.returnPressed.connect(self.navigate_to_url)
        #navbar.addWidget(self.url_bar)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.fiverr.com/zafranhaider?up_rollout=true#!"))  # Replace with your website's URL

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

app = QApplication(sys.argv)
QApplication.setApplicationName("App")
window = WebsiteApp()
app.exec_()
