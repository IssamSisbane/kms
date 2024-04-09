class CloudServer:
    data = {}

    def store_data(self, mac_address, data):
        if mac_address not in self.data:
            self.data[mac_address].append(data)
        else:
            self.data[mac_address] = [data]
    
    def get_data(self, mac_address):
        return self.data[mac_address]
    
    def get_sum_of_data(self, mac_address):
        return sum(self.data[mac_address])