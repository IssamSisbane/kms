from KMS import KMS
from IoTDevice import IotDevice
from CloudServer import CloudServer
from ExternalDevice import ExternalDevice

# Different actors
iot_device_1 = IotDevice("00:11:22:33:44:55")
iot_device_2 = IotDevice("00:11:22:33:44:56")
kms = KMS()
cloud_server = CloudServer()
external_device = ExternalDevice()


# Key distribution by the KMS
iot_device_1.set_public_key(kms.get_key(iot_device_1.mac_adress))
iot_device_2.set_public_key(kms.get_key(iot_device_2.mac_adress))


# Data encryption by IoT Devices. We supposed that encryption is done internally, in order to simplify the code, we just pass the plain data in parameters
encypted_data_1 = iot_device_1.encrypt_data(10)
# second value on device 1 to test homomorphic property
encypted_data_1_bis = iot_device_1.encrypt_data(15) 
encypted_data_2 = iot_device_2.encrypt_data(20)


# Data save in the cloud server
cloud_server.store_data(iot_device_1.mac_adress, encypted_data_1)
cloud_server.store_data(iot_device_1.mac_adress, encypted_data_1_bis)
cloud_server.store_data(iot_device_2.mac_adress, encypted_data_2)


# An external device link with the 2 IoT Devices (with a supposed App)
external_device.generate_keys()
external_device.link_iot_device(iot_device_1.mac_adress)
external_device.link_iot_device(iot_device_2.mac_adress)



# The external device ask the cloud server to send the data
data_1_encrypted = cloud_server.get_data(iot_device_1.mac_adress)
data_2_encrypted = cloud_server.get_data(iot_device_2.mac_adress)
sum_data_encrypted = cloud_server.get_sum_of_data(iot_device_1.mac_adress)

# The external device ask to the KMS for re-encrypted data
data_1_reencrypted = kms.reencrypt(iot_device_1.mac_adress, data_1_encrypted, external_device.public_key)
data_2_reencrypted = kms.reencrypt(iot_device_2.mac_adress, data_2_encrypted, external_device.public_key)
sum_data_reencrypted = kms.reencrypt(iot_device_1.mac_adress, sum_data_encrypted, external_device.public_key)

# Let’s check the results when the external device decrypt
print("First value of device 1 :", external_device.private_key.decrypt(data_1_reencrypted))
print("First value of device 2 :", external_device.private_key.decrypt(data_2_reencrypted))
print("Sum of all values of device 1 :", external_device.private_key.decrypt(sum_data_reencrypted))