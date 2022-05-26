from pydocsis.MtaConfig import MtaConfig
from pydocsis.cmConfig import CmConfig
from pydocsis.docsisTlvs import DocsisTlvs
import binascii


class ConfigFile(object):
    def __init__(self):
        self.tlvs = []
        self.configFilePath = ""
        self.tlv_string = ""
        self.tags = DocsisTlvs
        self.hashme = []

    def generate_string_from_file(self, file=""):
        if file != "":
            self.configFilePath = file
        if self.configFilePath != "":
            f = open(self.configFilePath, "rb")
            content = f.read()
            self.tlv_string = binascii.hexlify(content).decode('UTF-8')[:]
        else:
            raise ValueError("Cannot turn a file into a string if there is no file.")

    def get_config(self):
        if self.tlv_string.startswith("fe0101"):
            bob = MtaConfig()
            bob.configFilePath = self.configFilePath
            bob.tlv_string = self.tlv_string
            return bob
        else:
            bob = CmConfig()
            bob.configFilePath = self.configFilePath
            bob.tlv_string = self.tlv_string
            return bob