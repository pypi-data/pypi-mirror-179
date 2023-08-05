import configparser

class Config:
    def __init__(self, config_file_path):
        """Create config object with config file
        """
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)