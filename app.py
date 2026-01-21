import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path

# ============================================================
# WINE CULTIVAR ORIGIN PREDICTION SYSTEM
# Student: Ogah Victor (Matric: 22CG031902)
# ============================================================

# Page configuration
st.set_page_config(
    page_title="Wine Cultivar Prediction",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .header-title {
        color: #8B4513;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subheader {
        color: #A0522D;
        font-size: 1.2rem;
    }
    .prediction-box {
        background-color: #F5DEB3;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #8B4513;
    }
    .info-box {
        background-color: #FFF8DC;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_model_and_artifacts():
    """Load the trained model and preprocessing artifacts"""
    try:
        # Define paths
        model_dir = Path(__file__).parent / "model"
        model_path = model_dir / "wine_cultivar_model.pkl"
        scaler_path = model_dir / "scaler.pkl"
        features_path = model_dir / "features.pkl"
        
        # Load artifacts
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        features = joblib.load(features_path)
        
        return model, scaler, features
    except FileNotFoundError as e:
        st.error(f"❌ Error: Could not load model files. {str(e)}")
        st.info("Make sure the following files exist in the 'model' directory:")
        st.write("- wine_cultivar_model.pkl")
        st.write("- scaler.pkl")
        st.write("- features.pkl")
        return None, None, None

def predict_cultivar(model, scaler, features, input_values):
    """Make prediction using the trained model"""
    try:
        # Create DataFrame with input values
        input_df = pd.DataFrame([input_values], columns=features)
        
        # Scale the input
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        return prediction, prediction_proba
    except Exception as e:
        st.error(f"❌ Error during prediction: {str(e)}")
        return None, None

def cultivar_name(prediction):
    """Convert numeric prediction to cultivar name"""
    cultivar_map = {
        0: "Cultivar 1",
        1: "Cultivar 2",
        2: "Cultivar 3"
    }
    return cultivar_map.get(prediction, "Unknown")

# ============================================================
# MAIN APP
# ============================================================

# Header
st.markdown('<div class="header-title">🍷 Wine Cultivar Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">AI-Powered Wine Origin Classification</div>', unsafe_allow_html=True)
st.divider()

# Load model and artifacts
model, scaler, features = load_model_and_artifacts()

if model is not None:
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📊 About Model", "ℹ️ Instructions"])
    
    # ============================================================
    # TAB 1: PREDICTION
    # ============================================================
    with tab1:
        st.markdown("### Enter Wine Chemical Properties")
        st.info("📝 Input the chemical properties of your wine sample to predict its cultivar (origin).")
        
        # Create two columns for input
        col1, col2 = st.columns(2)
        
        with col1:
            alcohol = st.number_input(
                "Alcohol (%)",
                min_value=10.0,
                max_value=15.0,
                value=12.5,
                step=0.1,
                help="Alcohol content percentage"
            )
            
            total_phenols = st.number_input(
                "Total Phenols (g/dm³)",
                min_value=0.5,
                max_value=4.0,
                value=2.3,
                step=0.1,
                help="Total phenols in wine"
            )
            
            flavanoids = st.number_input(
                "Flavanoids (g/dm³)",
                min_value=0.0,
                max_value=5.0,
                value=2.2,
                step=0.1,
                help="Flavanoids content"
            )
        
        with col2:
            color_intensity = st.number_input(
                "Color Intensity",
                min_value=0.0,
                max_value=13.0,
                value=4.5,
                step=0.1,
                help="Wine color intensity"
            )
            
            hue = st.number_input(
                "Hue",
                min_value=0.0,
                max_value=2.0,
                value=1.0,
                step=0.1,
                help="Wine hue value"
            )
            
            proline = st.number_input(
                "Proline (mg/dm³)",
                min_value=300.0,
                max_value=1700.0,
                value=600.0,
                step=50.0,
                help="Proline concentration"
            )
        
        # Prediction button
        st.divider()
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col2:
            predict_button = st.button("🔍 Predict Cultivar", use_container_width=True)
        
        # Make prediction
        if predict_button:
            input_values = {
                'alcohol': alcohol,
                'total phenols': total_phenols,
                'flavanoids': flavanoids,
                'color intensity': color_intensity,
                'hue': hue,
                'proline': proline
            }
            
            prediction, probabilities = predict_cultivar(model, scaler, features, input_values)
            
            if prediction is not None:
                # Display prediction result
                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
                st.markdown(f"### 🎯 Prediction Result")
                st.markdown(f"## **{cultivar_name(prediction)}**")
                
                # Display probabilities
                st.markdown("### Prediction Confidence")
                confidence_df = pd.DataFrame({
                    'Cultivar': ['Cultivar 1', 'Cultivar 2', 'Cultivar 3'],
                    'Confidence (%)': [f"{prob*100:.2f}%" for prob in probabilities]
                })
                st.table(confidence_df)
                
                # Confidence bar chart
                fig_data = pd.DataFrame({
                    'Cultivar': ['Cultivar 1', 'Cultivar 2', 'Cultivar 3'],
                    'Confidence': probabilities
                })
                st.bar_chart(fig_data.set_index('Cultivar'))
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    # ============================================================
    # TAB 2: ABOUT MODEL
    # ============================================================
    with tab2:
        st.markdown("### 📊 Model Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Algorithm Details")
            st.info("""
            - **Algorithm**: Random Forest Classifier
            - **Number of Trees**: 100
            - **Max Depth**: 10
            - **Model Persistence**: Joblib (.pkl)
            """)
        
        with col2:
            st.markdown("#### Dataset Information")
            st.info("""
            - **Dataset**: Wine Dataset (UCI)
            - **Total Samples**: 178
            - **Training Samples**: ~142
            - **Testing Samples**: ~36
            - **Number of Classes**: 3
            """)
        
        st.divider()
        st.markdown("#### 📋 Selected Features")
        features_list = ['alcohol', 'total phenols', 'flavanoids', 'color intensity', 'hue', 'proline']
        for i, feature in enumerate(features_list, 1):
            st.write(f"{i}. {feature.title()}")
        
        st.divider()
        st.markdown("#### 📈 Model Performance")
        performance_data = {
            'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
            'Training': ['~0.9944', '~0.9944', '~0.9944', '~0.9944'],
            'Testing': ['~0.9722', '~0.9722', '~0.9722', '~0.9722']
        }
        st.table(performance_data)
        
        st.info("""
        ✅ The model demonstrates excellent performance with high accuracy and robust metrics across all evaluation measures.
        """)
    
    # ============================================================
    # TAB 3: INSTRUCTIONS
    # ============================================================
    with tab3:
        st.markdown("### 📖 How to Use This System")
        
        with st.expander("1️⃣ Prepare Your Wine Sample", expanded=True):
            st.write("""
            Obtain chemical analysis results for your wine sample. You'll need measurements for:
            - Alcohol content
            - Total phenols
            - Flavanoids
            - Color intensity
            - Hue
            - Proline
            """)
        
        with st.expander("2️⃣ Input the Values", expanded=True):
            st.write("""
            Enter each chemical property value in the prediction tab. 
            The system will automatically validate the input ranges.
            """)
        
        with st.expander("3️⃣ Get Prediction", expanded=True):
            st.write("""
            Click the "Predict Cultivar" button to get:
            - The predicted wine cultivar (1, 2, or 3)
            - Confidence scores for each cultivar
            - A visualization of prediction probabilities
            """)
        
        with st.expander("4️⃣ Interpret Results", expanded=True):
            st.write("""
            - The highest confidence percentage indicates the most likely cultivar
            - The bar chart shows how confident the model is in each prediction
            - High confidence (>80%) indicates a reliable prediction
            - Lower confidence suggests the wine may be a blend or atypical
            """)
        
        st.divider()
        st.markdown("### ❓ About the Wine Cultivars")
        st.write("""
        This system classifies wines into one of 3 cultivars based on their chemical composition:
        
        - **Cultivar 1**: Wines with distinct chemical characteristics
        - **Cultivar 2**: Wines with unique property combinations
        - **Cultivar 3**: Wines with specific chemical profiles
        
        The Random Forest model was trained to recognize these distinct chemical patterns.
        """)
    
    # Footer
    st.divider()
    st.markdown("""
    <div class="info-box">
    <small>
    <b>Wine Cultivar Origin Prediction System</b><br>
    Student: Ogah Victor | Matric: 22CG031902<br>
    Machine Learning Algorithm: Random Forest Classifier<br>
    Model Persistence: Joblib<br>
    </small>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("❌ Application Error")
    st.write("Unable to load the trained model. Please check the model files in the 'model' directory.")
