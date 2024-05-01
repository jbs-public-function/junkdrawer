import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # or any {'0', '1', '2'}
import tensorflow as tf

gpu_devices = tf.config.list_physical_devices('GPU')

print(f"tensorflow built with cuda - {tf.test.is_built_with_cuda()}")
print(f"list physical devices - {gpu_devices[0]}")

details = tf.config.experimental.get_device_details(gpu_devices[0])

print(f"device name - {details.get('device_name', 'Unknown GPU')}")
