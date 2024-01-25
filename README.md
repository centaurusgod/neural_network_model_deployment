# Bird Classification Model

Welcome to the Bird Classification Model project! This project leverages a Convolutional Neural Network (CNN) to accurately classify bird images. Below are the details on setting up the project and utilizing the model.

## Requirements

- Python 3.8.18
- Pip 23.3.1
- Django 4.2.9
- Django Rest Framework 3.14.0
- MySQL Connector Python 8.3.0
- Numpy 1.20.3
- Matplotlib 3.7.0
- Scikit-learn 1.3.2
- Scipy 1.10.1
- TensorFlow 2.10.0

## Setting up the Environment

1. Create a virtual environment with Python 3.8.0:
   ```bash
   python3.8 -m venv env
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Linux:
     ```bash
     source env/bin/activate
     ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Download the Model

Download the bird classification model `bird_classification_model.h5` from [Google Drive](https://drive.google.com/file/d/1iH9_p35WGNQXdwYQnyMpMQ60cwYJUWS8/view?usp=sharing). Place the model file inside `birdwatch/imageclassification/`.

## Model Capabilities

The model can predict the following bird classes:

- Malacocincla abbotti
- Dupetor flavicollis
- Alcedo meninting
- ...

**Note:** For optimal results, it's suggested to use somewhat cropped images when providing input to the model.

## Running the Application

1. Run the Django server locally:
   ```bash
   python manage.py runserver
   ```

2. To access the application in your local network, find your IPv4 address using `ipconfig` (Windows) or `ifconfig` (Linux).

3. Run the server on your local network:
   - Windows:
     ```bash
     python manage.py runserver your_ip_address:8000
     ```
   - Linux:
     ```bash
     python manage.py runserver your_ip_address:8000
     ```

4. Access the application from any device on the local network using the provided IP address. Remember to update the API requests in HTML files and JavaScript to use the relevant IP address instead of localhost.

Happy bird watching! 🐦🔍
