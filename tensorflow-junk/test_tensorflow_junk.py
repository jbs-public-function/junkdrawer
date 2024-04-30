import tensorflow as tf

print("Physical Devices")
print(tf.config.list_physical_devices())
print("\nGpu Available")
print(tf.test.is_gpu_available())
print("\nBuilt WIth Cuda")
print(tf.test.is_built_with_cuda())


import tensorflow as tf

# Check if GPU is available
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Define some sample data
data = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, activation='relu', input_shape=(2,))
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Print model summary
model.summary()

# Train the model
model.fit(data, data, epochs=10)
