import numpy as np
import pandas as pd
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
import matplotlib.pyplot as plt
from settings import images_sum



def load_training_data(image_directory, num_classes=images_sum):
    data = []
    labels = []
    for i in range(num_classes):
        path = os.path.join(image_directory, str(i))
        images = os.listdir(path)
        for img in images:
            try:
                img_path = os.path.join(path, img)
                image = Image.open(img_path)
                image = image.resize((30,30))
                image = np.array(image)
                data.append(image)
                labels.append(i)
            except:
                print(f"Error loading image: {img_path}")
    data = np.array(data)
    labels = np.array(labels)
    return data, labels

def load_test_data(csv_path):
    test_df = pd.read_csv(csv_path)
    data = []
    labels = test_df["ClassId"].values
    for img_path in test_df["Path"].values:
        image = Image.open(img_path)
        image = image.resize((30,30))
        data.append(np.array(image))
    data = np.array(data)
    return data, labels

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
    # Load training data
    image_directory = 'Train'
    data, labels = load_training_data(image_directory)
    
    # Splitting the dataset
    X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
    y_train = to_categorical(y_train, images_sum)
    y_val = to_categorical(y_val, images_sum)

    # Building and training the model
    model = build_model(X_train.shape[1:], images_sum)
    history = model.fit(X_train, y_train, batch_size=32, epochs=15, validation_data=(X_val, y_val))

    # Save the model
    model.save("traffic_signs_v7.h5")

    # Load test data
    csv_path = 'Train.csv'
    X_test, y_test_labels = load_test_data(csv_path)
    y_test = to_categorical(y_test_labels, images_sum)

    # Evaluate on test data
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
    print(f"Test accuracy: {test_acc}, Test loss: {test_loss}")

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
