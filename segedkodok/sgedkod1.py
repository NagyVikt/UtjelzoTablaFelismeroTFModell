import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import json
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import VGG16, MobileNetV2
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report
import textwrap



def print_error_analysis(y_test, predicted_classes, label_to_number):
    # Convert one-hot encoded y_test to labels
    true_classes = np.argmax(y_test, axis=1)
    
    # Compute confusion matrix
    cm = confusion_matrix(true_classes, predicted_classes)
    print("Confusion Matrix:\n", cm)
    
    # Ensure the number of target names matches the number of classes
    target_names = list(label_to_number.keys())
    unique_classes = np.unique(np.concatenate((true_classes, predicted_classes)))
    if len(unique_classes) != len(target_names):
        print(f"Warning: Number of classes ({len(unique_classes)}) does not match size of target_names ({len(target_names)}). Adjusting.")
        # Optionally adjust target_names here or specify labels explicitly
        target_names = [label_to_number.inverse[c] for c in unique_classes]  # Assuming label_to_number has an inverse mapping
        # If no inverse mapping, you might need to adjust this part
        
    # Compute classification report
    cr = classification_report(true_classes, predicted_classes, target_names=target_names, labels=unique_classes)
    print("Classification Report:\n", cr)
    



def plot_and_save_history(history, save_path='training_history.png'):
    """
    Plots and saves the training history.

    Parameters:
        history: The history object returned by the fit method of a model.
        save_path: Path where the plot image will be saved.
    """
    plt.figure(figsize=(12, 6))

    # Plot training & validation accuracy values
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')

    # Plot training & validation loss values
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')

    plt.savefig(save_path)
    plt.show()

def plot_preprocessed_images(image_data, labels, number_to_label, n=10, cols=5):
    # Determine number of rows needed based on the number of columns specified
    rows = n // cols + (n % cols > 0)
    fig_width = 20  # You can adjust this based on your specific requirements
    fig_height = rows * 4  # Adjust the height based on the number of rows
    plt.figure(figsize=(fig_width, fig_height))

    for i in range(n):
        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(image_data[i])
        # Use textwrap to wrap text
        title = textwrap.fill(number_to_label[np.argmax(labels[i])], width=20)
        plt.title(title, fontsize=10)  # Adjust fontsize to fit the space
        plt.axis('off')  # Turns off the axis

    # Adjust subplot parameters to give more space for titles
    plt.subplots_adjust(top=0.85, hspace=0.3)

    plt.show()
def plot_augmented_images(datagen, original_image, n=10):
    plt.figure(figsize=(20, 2))
    plt.subplot(2, n, 1)
    plt.imshow(original_image)
    plt.title('Original')
    plt.gray()
    plt.axis('off')
    
    # Generate and plot augmented images
    i = 0
    for batch in datagen.flow(np.expand_dims(original_image, 0), batch_size=1):
        plt.subplot(2, n, i + 2)
        plt.imshow(batch[0])
        plt.axis('off')
        i += 1
        if i >= n - 1:
            break
    plt.show()

def load_image_labels(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def create_label_mapping(labels):
    unique_labels = sorted(set(labels.values()))
    label_to_number = {label: i for i, label in enumerate(unique_labels)}
    return label_to_number, len(unique_labels)

def load_and_preprocess_images(image_directory, image_labels, label_to_number):
    def preprocess_image(file_path, label):
        # Load the raw data from the file as a string
        img = tf.io.read_file(file_path)
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, [224, 224])
        img /= 255.0  # Normalize to [0,1] range
        return img, label
    
    paths = [os.path.join(image_directory, fname) for fname in sorted(image_labels, key=lambda x: int(x.split('.')[0]))]
    labels = [label_to_number[image_labels[fname]] for fname in sorted(image_labels, key=lambda x: int(x.split('.')[0]))]

    ds = tf.data.Dataset.from_tensor_slices((paths, labels))
    ds = ds.map(preprocess_image)
    return ds



def preprocess_images(image_directory, image_labels, label_to_number):
    image_data = []
    labels = []
    for file_name in sorted(image_labels, key=lambda x: int(x.split('.')[0])):  # Sort files by number
        label = image_labels[file_name]
        image_path = os.path.join(image_directory, file_name)
        image = load_img(image_path, target_size=(224, 224))
        image = img_to_array(image) / 255.0

        image_data.append(image)
        labels.append(label_to_number[label])

    return np.array(image_data), np.array(labels)

def augment_data(X_train, y_train):
    datagen = ImageDataGenerator(
        rotation_range=30,
        zoom_range=0.25,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.15,
        channel_shift_range=0.2,
        fill_mode="nearest")  # Removed horizontal_flip
    datagen.fit(X_train)
    return datagen

def define_compile_model(number_of_classes):
    # Use MobileNetV2 as the base model
    base_model = MobileNetV2(include_top=False, input_tensor=Input(shape=(224, 224, 3)), weights=None)
    x = base_model.output
    x = tf.keras.layers.GlobalAveragePooling2D()(x)  # Use global average pooling
    x = tf.keras.layers.Dense(256, activation='relu')(x)  # Experiment with the number of units

    x = tf.keras.layers.Dropout(0.5)(x)  # Add dropout
    predictions = tf.keras.layers.Dense(number_of_classes, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def compute_class_weights(y_train):
    from sklearn.utils.class_weight import compute_class_weight
    class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
    return dict(enumerate(class_weights))

def main(image_directory, json_file_path):
    image_labels = load_image_labels(json_file_path)
    label_to_number, number_of_classes = create_label_mapping(image_labels)
    
    X, y = load_and_preprocess_images(image_directory, image_labels, label_to_number)
    print(f"Total images preprocessed: {X.shape[0]}")

    y = to_categorical(y, num_classes=number_of_classes)
    
    # Visualize preprocessed images (optional)
    #plot_preprocessed_images(X, y, {i: label for label, i in label_to_number.items()})


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    class_weights = compute_class_weights(np.argmax(y_train, axis=1))
    
    datagen = augment_data(X_train, y_train)


    # Visualize augmented images (optional)
    plot_augmented_images(datagen, X_train[0])
    
    model = define_compile_model(number_of_classes)
    
    # Learning rate scheduler
    def lr_schedule(epoch):
        lr = 1e-3
        if epoch > 10:
            lr *= 0.5e-3
        elif epoch > 20:
            lr *= 1e-3
        elif epoch > 30:
            lr *= 0.5e-3
        elif epoch > 40:
            lr *= 1e-4
        print('Learning rate: ', lr)
        return lr
    lr_scheduler = tf.keras.callbacks.LearningRateScheduler(lr_schedule)

    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.001)
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
    model_checkpoint = tf.keras.callbacks.ModelCheckpoint('best_model.h5.keras', save_best_only=True, monitor='val_loss')

    

    # Fit the model on the batches generated by datagen.flow().
    history = model.fit(
        datagen.flow(X_train, y_train, batch_size=32),
        epochs=50,  # You may increase the number of epochs
        validation_data=(X_test, y_test),
        class_weight=class_weights,
        callbacks=[reduce_lr, lr_scheduler, early_stopping, model_checkpoint]
    )

    # Save the model in the TensorFlow's default SavedModel format
    model.save('traffic_sign_model.keras')

    plot_and_save_history(history, 'training_history.png')


    predictions = model.predict(X_test)
    predicted_classes = np.argmax(predictions, axis=1)

     # Error Analysis
    print_error_analysis(y_test, predicted_classes, label_to_number)


    number_to_label = {i: label for label, i in label_to_number.items()}
    predicted_labels = [number_to_label[pred] for pred in predicted_classes]

    # Consider printing some results or evaluations here
    unique_labels, counts = np.unique(predicted_labels, return_counts=True)
    for label, count in zip(unique_labels, counts):
        print(f'{label}: {count}')
    print(f'Total predictions: {len(predicted_labels)}')

if __name__ == "__main__":
    image_directory = 'utjelzotablak'
    json_file_path = 'descriptions.json'
    main(image_directory, json_file_path)


