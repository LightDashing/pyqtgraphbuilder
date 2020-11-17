import json
import os


class Settings:
    file: str
    setts: dict

    def __init__(self):
        self.file = "settings.conf"
        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                self.setts = {"xMin": 0, "xMax": 10, "step": 1, "yMin": 0, "yMax": 10, "auto": True}
                json.dump(self.setts, f)
        else:
            self.load_settings()

    def load_settings(self):
        with open(self.file, "r", encoding="utf-8") as f:
            self.setts = json.load(f)

    def save_settings(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.setts, f)

    def reset_settings(self):
        self.setts = {"xMin": 0, "xMax": 10, "step": 1, "yMin": 0, "yMax": 10, "auto": True}

    def reload_settings(self):
        self.reset_settings()
        self.save_settings()
