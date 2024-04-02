def is_stop_sign(file_path):
    # Dummy function to represent the concept of checking for STOP signs
    # Implement image preprocessing and pattern recognition here
    # Return True if a STOP sign is detected, False otherwise
    return False  # Placeholder implementation

def classify(file_path):
    global label_packed
    if is_stop_sign(file_path):
        sign = "Állj, minden járműnek meg kell állnia"  # Assuming this is the STOP sign in your classes dictionary
    else:
        image = Image.open(file_path)
        image = image.resize((30,30))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        prediction = model.predict([image])
        pred = np.argmax(prediction, axis=1)[0]  # Get the index of the max value
        sign = classes[pred+1]
    label.configure(foreground='#011638', text=sign)
