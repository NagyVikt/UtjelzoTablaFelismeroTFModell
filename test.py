import numpy as np
import os
import json
from PIL import Image
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
import matplotlib.pyplot as plt

def load_image_labels(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:  # Specify encoding here
        return json.load(file)

# Prepare the dataset
def prepare_dataset(image_directory, labels_info):
    data = []
    labels = []
    label_to_number = {}
    number_to_label = {}
    for key, value in labels_info.items():
        if value not in label_to_number:
            number = len(label_to_number)
            label_to_number[value] = number
            number_to_label[number] = value
        
        img_path = os.path.join(image_directory, key)
        image = Image.open(img_path)
        image = image.resize((30, 30))
        data.append(np.array(image))
        labels.append(label_to_number[value])

    data = np.array(data)
    labels = np.array(labels)
    return data, labels, len(label_to_number)

def build_model(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (5, 5), activation='relu', input_shape=input_shape),
        Conv2D(32, (5, 5), activation='relu'),
        MaxPool2D(pool_size=(2, 2)),
        Dropout(0.25),
        Conv2D(64, (3, 3), activation='relu'),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPool2D(pool_size=(2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def main():
    image_directory = 'utjelzotablak'
    json_file_path = 'descriptions.json'
    labels_info = load_image_labels(json_file_path)
    data, labels, num_classes = prepare_dataset(image_directory, labels_info)
    
    # Splitting the dataset
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=200)
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    # Building and training the model
    model = build_model(X_train.shape[1:], num_classes)
    history = model.fit(X_train, y_train, batch_size=64, epochs=300, validation_data=(X_test, y_test))
    model.save("traffic_classifier.keras")

    # Plotting training results
    plt.figure(0)
    plt.plot(history.history['accuracy'], label='training accuracy')
    plt.plot(history.history['val_accuracy'], label='val accuracy')
    plt.title('Accuracy')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.legend()
    plt.show()

    plt.figure(1)
    plt.plot(history.history['loss'], label='training loss')
    plt.plot(history.history['val_loss'], label='val loss')
    plt.title('Loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
