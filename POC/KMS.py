from phe import paillier

class KMS:
    dict_keys = {}

    # Generate a key pair if the device is not already registered otherwise return the public key
    def get_key(self, ior_device_mac):
        if ior_device_mac not in self.dict_keys:
            public_key, private_key = paillier.generate_paillier_keypair(n_length=512)
            self.dict_keys[ior_device_mac] = (public_key, private_key)
        return self.dict_keys[ior_device_mac][0]
    
    # Re-encrypt data with a new public key
    def reencrypt(self, iot_device_mac, encrypted_data, new_public_key):
        private_key = self.dict_keys[iot_device_mac][1]
        return private_key.decrypt(encrypted_data).encrypt(new_public_key)
    

    