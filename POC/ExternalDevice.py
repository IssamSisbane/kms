from phe import paillier

class ExternalDevice:
    iot_devices_mac_associated = []
    public_key = None
    private_key = None

    def generate_keys(self):
        self.public_key, self.private_key = paillier.generate_paillier_keypair(n_length=512)

    def link_iot_device(self, iot_device_mac):
        self.iot_devices_mac_associated.append(iot_device_mac)