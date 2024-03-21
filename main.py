import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img

import os
import json

# Define the directory where your images are stored
image_directory = 'path_to_your_utjelzotablak_folder'

# Load the JSON file with your descriptions
with open('path_to_your_json_file', 'r') as json_file:
    image_labels = json.load(json_file)

# Preprocess images
def preprocess_images(image_directory, image_labels):
    image_data = []
    labels = []
    
    for file_name, label in image_labels.items():
        image_path = os.path.join(image_directory, file_name)
        image = load_img(image_path)
        image = img_to_array(image.resize((32, 32)))  # Resize to the input shape expected by the CNN
        image /= 255.0  # Normalize pixel values
        
        image_data.append(image)
        labels.append(label)  # You might want to convert these labels to a numerical format
    
    return np.array(image_data), np.array(labels)

# Run the preprocessing function
X, y = preprocess_images(image_directory, image_labels)

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