TEGIN AI - Radar Target Classifier
TEGIN AI is a radar target classification system developed using Convolutional Neural Networks (CNNs) and the publicly available MSTAR dataset.
The project includes a web-based demonstration built with Streamlit, allowing users to classify randomly selected radar images in real-time.

Project Overview
This project aims to demonstrate the application of deep learning techniques, particularly CNNs, in radar image target classification.
The system processes radar imagery, predicts the target class, and provides immediate feedback on the model's performance through a user-friendly web interface.

Features
Radar target classification using a ResNet-18 based CNN model

Adaptation of the ResNet-18 architecture for single-channel (grayscale) radar images

Training performed on the MSTAR dataset

Real-time inference and interactive user interface powered by Streamlit

Display of true class, model prediction, and prediction correctness

Technologies Used
Python 3

PyTorch

Torchvision

Streamlit

PIL (Python Imaging Library)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/tegin-ai.git
cd tegin-ai
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Ensure that the trained model file radar_resnet18_model.pth is placed in the correct directory (/path/to/model).

Usage
Navigate to the application directory:

bash
Copy
Edit
cd app
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Once running, the web application will open in your default browser.
Press the "Get New Radar Image" button to generate a random radar image and view the classification results.

Results
The model has been trained on the MSTAR dataset and achieves a high classification accuracy on the validation set.
Real-time predictions provide immediate insight into the model’s performance, showcasing the potential of CNN-based solutions for radar target classification tasks.

License
This project is released for educational and research purposes.
