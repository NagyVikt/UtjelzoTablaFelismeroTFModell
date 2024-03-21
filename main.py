import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import json
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Define the directory where your images are stored
image_directory = 'utjelzotablak'
# Load the JSON file with your descriptions
with open('descritptions.json', 'r') as json_file:
    image_labels = json.load(json_file)

# Assuming the labels are categorical, create a mapping to numerical values
unique_labels = sorted(set(image_labels.values()))
label_to_number = {label: i for i, label in enumerate(unique_labels)}
number_of_classes = len(unique_labels)

def preprocess_images(image_directory, image_labels):
    image_data = []
    labels = []
    
    for file_name, label in image_labels.items():
        image_path = os.path.join(image_directory, file_name)
        image = load_img(image_path, target_size=(32, 32))  # Direct resize
        image = img_to_array(image) / 255.0  # Normalize pixel values
        
        image_data.append(image)
        labels.append(label_to_number[label])  # Convert label to numerical format
    
    return np.array(image_data), np.array(labels)

# Preprocess images
X, y = preprocess_images(image_directory, image_labels)
# Convert labels to one-hot encoding
y = to_categorical(y, num_classes=number_of_classes)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define your CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(number_of_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save the model
model.save('traffic_sign_model.h5')

# Predict with the model (adapted for softmax/categorical)
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)

# Reverse mapping for interpretation
number_to_label = {i: label for label, i in label_to_number.items()}
predicted_labels = [number_to_label[pred] for pred in predicted_classes]
