import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Load and preprocess data
# X_train, X_test, y_train, y_test = load_your_data()

# Build a CNN model
model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(number_of_sign_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, 
                    validation_data=(X_test, y_test))

# Save the model
model.save('traffic_sign_model.h5')

# Predict with the model
predictions = model.predict(X_test)
predicted_signs = np.argmax(predictions, axis=1)

# Infer meaning (this is a simple mapping, in practice you'd have a lookup)
sign_meanings = {0: 'Stop', 1: 'Yield', ...} # Replace with actual mappings
predicted_meanings = [sign_meanings[pred] for pred in predicted_signs]