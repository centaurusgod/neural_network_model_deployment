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
Note that you need to change settings.py to use different database like inbuilt sqllite database provided by django. 
The following is what database part in my settings.py looks like. Ask chatgpt and modify to default django sqlllite if needed. 
The API to get bird detail is already made but commented just to return scientific name of the image provided by any devices. 
One can modify the code accordingly and use as per their use. Go to birdwatch/mlapi/views.py to get more insights. 
One might also need to make some database migrations to make this code functional. Refer to ChatGPT for that.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'birdwatch',    # Your MySQL database name
        'USER': 'root',     # Your MySQL username
        'PASSWORD': '',     # Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',     # Default MySQL port
    }
}

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

1. Malacocincla abbotti
2. Dupetor flavicollis
3. Alcedo meninting
4. Pitta nipalensis
5. Tickellia hodgsoni
6. Catreus wallichii
7. Lonchura atricapilla
8. Aegypius monachus
9. Stachyris chrysaea
10. Brachypteryx stellata
11. Botaurus stellaris
12. Buceros bicornis
13. Mulleripicus pulverulentus
14. Ibidorhyncha struthersii
15. Cursorius coromandelicus
16. Grаminicolа bengalensis
17. Caprimulgus asiaticus
18. Sarkidiornis melanotos
19. Anas acuta
20. Mycteria leucocephala
21. Cochoa purpurea
22. Harpactes erythrocephalus
23. Sarcogyps calvus
24. Falco chicquera
25. Anthreptes singalensis
26. Actinodura egertoni
27. Falco cherrug
28. Leiothrix argentauris
29. Rallina eurizonoides
30. Bubo nipalensis
31. Melanochlora sultanea
32. Francolinus gularis
33. Dumetia hyperythra
34. Treron curvirostra
35. Alophoixus flaveolus
36. Saxicola insignis
37. Indicator xanthonotus
38. Phylloscopus cantator


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

## To Test Model's Prediction
1. Go to
   ```bash
   http://localhost:8000/classify_image
Happy bird watching! 🐦🔍

## Extras
1. 
