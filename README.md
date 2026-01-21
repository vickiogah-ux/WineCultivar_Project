# Wine Cultivar Origin Prediction System

A machine learning-powered web application for predicting wine cultivar (origin) based on chemical properties.

## Project Details

- **Student**: Ogah Victor
- **Matric Number**: 22CG031902
- **Institution**: Covenant University
- **Course**: CSC 415 - Artificial Intelligence
- **Semester**: Alpha, 400 Level

## Overview

This project implements a complete machine learning pipeline to predict the cultivar (origin) of wine based on chemical properties using a Random Forest Classifier. The system includes:

1. **Model Development**: Trained on the UCI Wine Dataset
2. **Web Interface**: Interactive Streamlit application
3. **Deployment**: Cloud-hosted on Render.com
4. **API Integration**: Ready for integration with other systems

## Features

- 🎯 **Accurate Predictions**: 97% accuracy on test dataset
- 🔄 **Easy Integration**: RESTful API endpoints
- 📊 **Visual Feedback**: Confidence scores and probability charts
- 🚀 **Cloud-Deployed**: Accessible from anywhere
- 📱 **Responsive UI**: Works on desktop and mobile devices

## Technical Stack

- **Backend**: Python, Streamlit
- **Machine Learning**: scikit-learn, Random Forest
- **Data Processing**: pandas, NumPy
- **Model Persistence**: Joblib
- **Deployment**: Render.com

## Dataset

**Wine Dataset** (UCI Machine Learning Repository)
- **Samples**: 178 wine samples
- **Classes**: 3 wine cultivars
- **Features Used**: 6 out of 11 available features

### Selected Features

1. Alcohol (%)
2. Total Phenols (g/dm³)
3. Flavanoids (g/dm³)
4. Color Intensity
5. Hue
6. Proline (mg/dm³)

## Model Architecture

**Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Max Depth**: 10
- **Model Persistence**: Joblib (.pkl format)

### Performance Metrics

| Metric | Training | Testing |
|--------|----------|---------|
| Accuracy | 99.44% | 97.22% |
| Precision | 99.44% | 97.22% |
| Recall | 99.44% | 97.22% |
| F1-Score | 99.44% | 97.22% |

## Project Structure

```
WineCultivar_Project_OgahVictor_22CG031902/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── WineCultivar_hosted_webGUI_link.txt  # Submission details
├── model/
│   ├── model_building.ipynb       # Model training notebook
│   ├── wine_cultivar_model.pkl    # Trained model
│   ├── scaler.pkl                 # Feature scaler
│   └── features.pkl               # Feature names list
├── static/                         # CSS and static files
└── templates/                      # HTML templates (if applicable)
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/WineCultivar_Project_OgahVictor_22CG031902.git
cd WineCultivar_Project_OgahVictor_22CG031902
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model (Optional)

To retrain the model from scratch:

1. Open `model/model_building.ipynb` in Jupyter Notebook or Google Colab
2. Run all cells to train the model and generate `.pkl` files
3. Place generated files in the `model/` directory

### 5. Run the Application Locally

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Usage

1. **Navigate to the Web Application**: Visit the deployed URL
2. **Enter Wine Properties**: Input the 6 chemical measurements
3. **Get Prediction**: Click the prediction button
4. **View Results**: See cultivar prediction with confidence scores

## Deployment

### Deploy to Render

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect GitHub repository
5. Set Build Command: `pip install -r requirements.txt`
6. Set Start Command: `streamlit run app.py --server.port=10000`
7. Deploy

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create new app
4. Connect GitHub repository and select `app.py`
5. Deploy

## Model Development Process

### Step 1: Data Preprocessing
- Loaded Wine dataset from scikit-learn
- Selected 6 most predictive features
- Checked for missing values
- Applied StandardScaler for feature normalization

### Step 2: Feature Selection
- Analyzed feature importance
- Selected features with highest correlation to target
- Reduced dimensionality from 11 to 6 features

### Step 3: Train-Test Split
- 80% training data (142 samples)
- 20% testing data (36 samples)
- Stratified split to maintain class balance

### Step 4: Model Training
- Implemented Random Forest with optimized hyperparameters
- Trained on 100 decision trees
- Applied max depth constraint to prevent overfitting

### Step 5: Model Evaluation
- Calculated accuracy, precision, recall, and F1-score
- Generated confusion matrix
- Created classification report for all 3 classes

### Step 6: Model Persistence
- Saved model using Joblib
- Also saved scaler and feature names for consistent preprocessing

## Key Learning Points

1. **Data Preprocessing**: Importance of feature scaling and handling missing values
2. **Model Selection**: Why Random Forest works well for multiclass classification
3. **Evaluation Metrics**: Understanding accuracy, precision, recall, and F1-score
4. **Hyperparameter Tuning**: Impact of model parameters on performance
5. **Model Persistence**: Saving and loading trained models
6. **Web Deployment**: Making ML models accessible through web interfaces

## Future Improvements

- Add more advanced algorithms (XGBoost, Neural Networks)
- Implement cross-validation for better evaluation
- Add data visualization features
- Create API endpoints for programmatic access
- Add batch prediction capability
- Implement user authentication

## Exam Preparation Notes

**Key Concepts to Study**:
- Random Forest algorithm and how it works
- Feature scaling and its importance
- Multiclass classification metrics
- Train-test split and stratification
- Model persistence with Joblib
- Streamlit for web app development

**Practice Questions**:
1. Why is feature scaling mandatory for this project?
2. How does Random Forest prevent overfitting?
3. What is the difference between weighted and macro averages?
4. Why use Joblib instead of Pickle?
5. How to optimize hyperparameters of Random Forest?

## Troubleshooting

### Model files not found
- Ensure `model/` directory contains `.pkl` files
- Retrain the model using the notebook

### Streamlit connection error
- Check internet connection
- Verify Render deployment status
- Check if port 10000 is accessible

### Prediction errors
- Verify input values are within valid ranges
- Check if all feature names match exactly
- Ensure scaler.pkl is loaded correctly

## References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [UCI Wine Dataset](https://archive.ics.uci.edu/ml/datasets/wine)
- [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## License

This project is submitted for academic evaluation at Covenant University.

## Contact

**Student**: Ogah Victor  
**Matric**: 22CG031902  
**Course**: CSC 415 - Artificial Intelligence  

---

*Last Updated: January 21, 2026*
