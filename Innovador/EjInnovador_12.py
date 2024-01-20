# Patron Singleton

class ChatSettings:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ChatSettings, cls).__new__(cls)
            cls._instance.user_name = "DefaultUser"
            cls._instance.interface_theme = "Light"
            cls._instance.notifications_enabled = True
        return cls._instance

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_interface_theme(self, theme):
        self.interface_theme = theme

    def enable_notifications(self, enabled):
        self.notifications_enabled = enabled
