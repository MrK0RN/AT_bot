from selenium import webdriver
from selenium_stealth import stealth


class Driver:

    def __init__(self):
        self.driver = None

        self.user_agent = self.set_user_agent()
        self.languages = self.set_languages()
        self.vendor = self.set_vendor()
        self.platform = self.set_platform()
        self.webgl_vendor = self.set_webgl_vendor()
        self.renderer = self.set_renderer()
        self.fix_hairline = self.set_fixhairline()
        self.run_on_insecure_origins = self.set_run_on_insecure_origins()
        self.driver_status = "off"

    def set_user_agent(self):
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'
    def set_languages(self):
        return ["en-US", "en"]
    def set_vendor(self):
        return "Google Inc."
    def set_platform(self):
        return "Win32"
    def set_webgl_vendor(self):
        return "Intel Inc."
    def set_renderer(self):
        return "Intel Iris OpenGL Engine"
    def set_fixhairline(self):
        return True
    def set_run_on_insecure_origins(self):
        return False


    def driver_start(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        # options.add_argument("--headless") Today

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--load-extension=0.1.0_0')



        self.driver = webdriver.Chrome(options=options)

        stealth(self.driver,
                user_agent=self.user_agent,
                languages=self.languages,
                vendor=self.vendor,
                platform=self.platform,
                webgl_vendor=self.webgl_vendor,
                renderer=self.renderer,
                fix_hairline=self.fix_hairline,
                run_on_insecure_origins=self.run_on_insecure_origins,
                )


    def new_driver_status(self, f):
        self.driver_status = f

    def driver_quit(self):
        self.driver.quit()

