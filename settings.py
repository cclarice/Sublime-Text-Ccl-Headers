from sublime import load_settings

import os

class Settings:

    SETTINGS_FILE = 'ccl-headers.sublime-settings'

    LOGIN_KEY = 'login'

    DATE_TIME_FORMAT = '%Y/%m/%d %H:%M:%S'

    def __init__(self):
        self.all = load_settings(Settings.SETTINGS_FILE)

        self.update_login()
        self.all.add_on_change(Settings.LOGIN_KEY, self.update_login)

    def update_login(self):
        self.login = self.all.get(
            Settings.LOGIN_KEY,
            os.getenv('', '')
        )

    def timestamp(self, stamp):
        formatted = stamp.strftime(Settings.DATE_TIME_FORMAT)

        return '%s' % (formatted)

    def by(self):
        mail = 'cclarice@student.21-school.ru'

        return 'cclarice@student.21-school.ru'

