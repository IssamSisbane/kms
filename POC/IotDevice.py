class IotDevice:
    mac_address = None
    public_key = None
    
    def __init__(self, mac_address):
        self.mac_address = mac_address
    
    def set_public_key(self, public_key):
        self.public_key = public_key
    
    def encrypt_data(self, data):
        return self.public_key.encrypt(data)