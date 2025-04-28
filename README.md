# TEGIN AI - Radar Target Classifier

TEGIN AI is a radar target classification system developed using Convolutional Neural Networks (CNNs) and the MSTAR dataset.  
It includes a web-based demonstration powered by Streamlit, allowing users to classify randomly selected radar images with real-time predictions.

---

## Features

- Radar target classification based on real SAR (Synthetic Aperture Radar) imagery
- Convolutional Neural Network (CNN) architecture (ResNet-18)
- Transfer learning techniques adapted for single-channel (grayscale) radar images
- Interactive web application built with Streamlit
- Real-time random image selection and prediction display
- Lightweight, fast, and easy-to-deploy

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tegin-ai-radar-classifier.git
   cd tegin-ai-radar-classifier
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that the trained model file `radar_resnet18_model.pth` is placed inside the project directory under `models/`.

---

## Usage

Run the Streamlit app:

```bash
streamlit run app/app.py
```

Once the application starts, a new browser window will open automatically.  
Click the "Get New Radar Image" button to display a random radar image and view TEGIN AI's real-time prediction.

---

## Project Structure

```
tegin-ai-radar-classifier/
├── app/
│   ├── app.py            # Streamlit web application
│   └── ...
├── data/
│   └── mstar/            # MSTAR dataset (organized by class folders)
├── models/
│   └── radar_resnet18_model.pth  # Trained model weights
├── README.md
├── requirements.txt
└── ...
```

---

## Model Details

- **Architecture**: ResNet-18 (adapted for grayscale input)
- **Classes**: 8 different radar target classes from the MSTAR dataset
- **Training Notes**:
  - Input images resized to 128x128
  - Single-channel adaptation by modifying the first convolutional layer
  - Normalization applied to radar images for improved model performance
- **Accuracy**: Achieved high classification performance on unseen radar images

---

## Results

The model demonstrates strong prediction accuracy on unseen MSTAR images and performs robust real-time classification within the deployed Streamlit application.

---

## License

This project is intended for educational and research purposes.  
For commercial or production use, please contact the project maintainer.

---

## Acknowledgments

- MSTAR Dataset for providing SAR imagery for radar target classification
- PyTorch and Streamlit open-source communities
