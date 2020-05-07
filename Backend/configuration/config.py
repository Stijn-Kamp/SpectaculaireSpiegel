import codecs
import configparser
from os import path

from basicfuctions import get_package_root


class ConfigReader:
    """
    This class is used to get variables from the config file.
    """

    def __init__(self, configFile, configType=''):
        self.configType = configType
        self.config = configFile

    def _get_from_config(self, varName):
        """
        @param varName:
        @return:
        """
        raise NotImplementedError

    def get_var(self, varName):
        """
        This function is used to get a variable from the config file.
        @param varName: The name of the variable.
        @return: Value of the variable.
        """
        var = self._get_from_config(varName)
        return var

    def get_int(self, varName):
        """
        This function is used to get a int from the config file.
        @param varName: The name of the variable.
        @return: int if successful, None if unsuccessful.
        """
        i = self.get_var(varName)
        if i is None:
            return None
        try:
            return int(i)
        except (TypeError, ValueError):
            return None

    def get_float(self, varName):
        """
        This function is used to get a float from the config file.
        @param varName: The name of the variable.
        @return: int if successful, None if unsuccessful.
        """
        f = self.get_var(varName)
        if f is None:
            return None
        try:
            return float(f)
        except (TypeError, ValueError):
            return None

    def get_list(self, varName):
        """
        This function is used to get a list of variables from the config file.
        @param varName: The name of the list.
        @return: list.
        """
        array = []
        i = 1
        while True:
            var = self._get_from_config(varName.format(i))
            if var is None:
                break
            array.append(var)
            i += 1
        return array

    def get_bool(self, varName):
        """
        This function is used to get a bool from the config file, is false by default.
        @param varName: The name of the variable.
        @return: True if true, else False
        """
        b = self.get_var(varName)
        b = b if b is None else str(b).lower()
        return b == 'true'


class IniConfigReader(ConfigReader):
    """
    This class is used to initialize the config reader.
    """

    def __init__(self, configFile):
        ConfigReader.__init__(self, configFile)
        self.config = {}
        self.type = type
        try:
            config = configparser.ConfigParser(allow_no_value=True, strict=False)
            configText = codecs.open(path.join(get_package_root(), configFile), "r", "utf-8-sig").read()
            config.read_string("[config]\n" + configText)
            self.config = config["config"]
        except SyntaxError:
            pass

    def _get_from_config(self, varName):
        """
        This function is used to get a variable from the config file.
        @param varName: The name of the variable.
        @return: If successful str(var).replace('\'', ''), if unsuccessful return None.
        """
        var = self.config.get(varName, None)
        return var
