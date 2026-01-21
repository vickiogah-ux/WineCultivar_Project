# 🚀 WINE CULTIVAR PROJECT - COMPLETE SETUP GUIDE

## STEP-BY-STEP SUBMISSION GUIDE

### ⏰ TIMELINE
- **TODAY**: Train model + Push to GitHub + Deploy to Render (Deadline: 11:59 PM)

---

## PHASE 1: TRAIN THE MODEL (Google Colab) - 15 mins

### Step 1.1: Upload Notebook to Google Colab
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click "File" → "Upload notebook"
3. Select `model/model_building.ipynb` from your project folder
4. Colab will open the notebook

### Step 1.2: Run All Cells
1. Click "Runtime" → "Run all"
2. Wait for all cells to complete (should take 2-3 minutes)
3. You'll see all output including:
   - Data loaded ✓
   - Model trained ✓
   - Evaluation metrics displayed ✓
   - Model saved ✓

### Step 1.3: Download Generated Files
After training completes, download these 3 files from Colab:
1. `wine_cultivar_model.pkl`
2. `scaler.pkl`
3. `features.pkl`

### Step 1.4: Place Files in Your Project
1. Move the 3 downloaded `.pkl` files to your local `model/` directory
2. Structure should look like:
   ```
   model/
   ├── model_building.ipynb
   ├── wine_cultivar_model.pkl      ← Downloaded
   ├── scaler.pkl                   ← Downloaded
   └── features.pkl                 ← Downloaded
   ```

---

## PHASE 2: SETUP GITHUB REPOSITORY - 10 mins

### Step 2.1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "+" → "New repository"
3. **Repository Name**: `WineCultivar_Project_OgahVictor_22CG031902`
4. **Description**: Wine Cultivar Origin Prediction System
5. Select "Public" (for easy sharing)
6. **Do NOT** initialize with README (we already have one)
7. Click "Create repository"

### Step 2.2: Push Code to GitHub (Using Git)

**Option A: Using Command Line (Recommended)**

Open PowerShell/Terminal in your project directory:

```powershell
# Initialize git repository
git init

# Add your GitHub repository as origin
git remote add origin https://github.com/YourUsername/WineCultivar_Project_OgahVictor_22CG031902.git

# Stage all files
git add .

# Commit changes
git commit -m "Initial commit: Wine Cultivar Prediction System with Random Forest Model"

# Push to GitHub
git branch -M main
git push -u origin main
```

**Option B: Using GitHub Desktop**
1. Download [GitHub Desktop](https://desktop.github.com/)
2. File → Clone repository
3. Paste your repository URL
4. Clone to your project folder
5. Drag project files into the folder
6. Commit and publish

### Step 2.3: Copy Your Repository URL
After pushing, copy the URL from your GitHub repository (format: `https://github.com/YourUsername/WineCultivar_Project_OgahVictor_22CG031902`)

---

## PHASE 3: DEPLOY TO RENDER - 10-15 mins

### Step 3.1: Prepare for Deployment
1. Ensure `requirements.txt` exists in your root directory ✓
2. Ensure `app.py` exists in your root directory ✓
3. Ensure all `.pkl` files are in `model/` directory ✓
4. Everything is pushed to GitHub ✓

### Step 3.2: Create Render Account
1. Go to [Render.com](https://render.com)
2. Click "Sign Up"
3. Select "Sign up with GitHub"
4. Authorize Render to access your GitHub account
5. Complete the signup

### Step 3.3: Create Web Service on Render
1. Go to [Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Select your GitHub repository: `WineCultivar_Project_OgahVictor_22CG031902`
4. Click "Connect"

### Step 3.4: Configure Deployment Settings
Fill in the following:

| Setting | Value |
|---------|-------|
| **Name** | wine-cultivar-predictor |
| **Environment** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run app.py --server.port=10000 --server.enableCORS=false` |
| **Instance Type** | Free (for testing) |

### Step 3.5: Deploy
1. Click "Create Web Service"
2. Wait for deployment (3-5 minutes)
3. You'll see green checkmark when live
4. Copy your live URL (format: `https://wine-cultivar-predictor.onrender.com`)

**Note**: Free tier on Render may take time to boot. If you get 502 error, wait 2-3 minutes and refresh.

---

## PHASE 4: UPDATE SUBMISSION FILE - 2 mins

### Step 4.1: Update WineCultivar_hosted_webGUI_link.txt
Open the file and fill in:

```
Name: Ogah Victor
Matric Number: 22CG031902
Machine Learning Algorithm Used: Random Forest Classifier
Model Persistence Method: Joblib (.pkl)

Live URL of Hosted Application: https://wine-cultivar-predictor.onrender.com

GitHub Repository Link: https://github.com/YourUsername/WineCultivar_Project_OgahVictor_22CG031902
```

### Step 4.2: Push Update to GitHub
```powershell
git add WineCultivar_hosted_webGUI_link.txt
git commit -m "Add deployment URLs"
git push origin main
```

---

## PHASE 5: SUBMIT ON SCORAC - 5 mins

### Step 5.1: Prepare Submission Files
Create this folder structure:

```
WineCultivar_Project_OgahVictor_22CG031902/
├── app.py
├── requirements.txt
├── README.md
├── WineCultivar_hosted_webGUI_link.txt
├── model/
│   ├── model_building.ipynb
│   ├── wine_cultivar_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
├── static/                    (empty folder)
└── templates/                 (empty folder)
```

### Step 5.2: Compress and Upload
1. Right-click the folder → "Send to" → "Compressed (zipped) folder"
2. Rename to: `WineCultivar_Project_OgahVictor_22CG031902.zip`
3. Go to Scorac.com
4. Find CSC 415 assignment
5. Upload the ZIP file
6. **SUBMIT BEFORE 11:59 PM**

---

## ✅ VERIFICATION CHECKLIST

Before submission, verify:

- [ ] Model training notebook runs without errors on Google Colab
- [ ] All 3 `.pkl` files are in the `model/` directory
- [ ] `app.py` file exists in root directory
- [ ] `requirements.txt` file exists with correct dependencies
- [ ] `README.md` is well-formatted and complete
- [ ] `WineCultivar_hosted_webGUI_link.txt` has all URLs filled
- [ ] GitHub repository is public and all files are pushed
- [ ] Render deployment shows green "active" status
- [ ] Web application is accessible at the Render URL
- [ ] Can make predictions on the live web app
- [ ] Zip file is created with correct structure
- [ ] Zip file is uploaded to Scorac

---

## 🧪 TESTING THE APPLICATION

### Test Locally
```powershell
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```
Opens at: `http://localhost:8501`

### Test on Render
1. Visit your Render URL
2. Try sample predictions:
   - **Sample 1**: alcohol=12.5, phenols=2.3, flavanoids=2.2, intensity=4.5, hue=1.0, proline=600
   - **Sample 2**: alcohol=13.0, phenols=1.8, flavanoids=1.5, intensity=5.0, hue=0.8, proline=800

---

## 📚 KEY CONCEPTS FOR EXAM PREP

### Random Forest Classifier
- **Why it works**: Ensemble of decision trees voting on prediction
- **Prevents overfitting**: Random feature and sample selection
- **Fast training**: Parallelizable across CPU cores
- **Feature importance**: Built-in importance ranking

### Feature Scaling (StandardScaler)
- **Why needed**: Features have different ranges
- **Formula**: (x - mean) / std_dev
- **Benefits**: Improves model performance and convergence

### Multiclass Classification Metrics
- **Accuracy**: (TP + TN) / Total - Overall correctness
- **Precision**: TP / (TP + FP) - How many predicted positives were correct
- **Recall**: TP / (TP + FN) - How many actual positives were found
- **F1-Score**: Harmonic mean of precision and recall
- **Weighted average**: Accounts for class imbalance

### Model Persistence
- **Joblib**: Efficient for NumPy-based models
- **Pickle**: General Python object serialization
- **Both save training state** so no retraining needed

---

## 🆘 TROUBLESHOOTING

### Issue: Model files not found error
**Solution**: 
- Check `.pkl` files are in `model/` directory
- Retrain on Google Colab and redownload

### Issue: Streamlit connection timeout
**Solution**:
- Wait 5 minutes (Render container may be sleeping)
- Refresh the page
- Check Render dashboard for errors

### Issue: Git push fails
**Solution**:
```powershell
# Check remote
git remote -v

# If wrong, remove and re-add
git remote remove origin
git remote add origin https://github.com/YourUsername/WineCultivar_Project_OgahVictor_22CG031902.git
```

### Issue: Import errors when running locally
**Solution**:
```powershell
# Create fresh virtual environment
python -m venv venv_new
source venv_new/Scripts/activate
pip install -r requirements.txt
```

---

## 📞 QUICK REFERENCE

| Task | Time | Status |
|------|------|--------|
| Train model (Colab) | 10 min | ⬜ |
| Upload to GitHub | 5 min | ⬜ |
| Deploy to Render | 10 min | ⬜ |
| Update submission file | 2 min | ⬜ |
| Submit on Scorac | 3 min | ⬜ |
| **TOTAL** | **30 min** | ⬜ |

---

## 🎓 FOR EXAM PREPARATION

**Study These Sections of Code**:
1. Data preprocessing in notebook (cells 2-4)
2. Feature scaling implementation (cell 4)
3. Model training and hyperparameters (cell 6)
4. Evaluation metrics calculation (cell 8)
5. Model loading and prediction in app.py (lines 50-75)

**Practice Questions**:
1. Why use stratified train-test split?
2. What does StandardScaler do?
3. How does Random Forest handle feature importance?
4. Why save model as .pkl file?
5. What are the 3 cultivars being predicted?

---

**Good Luck! You've got this! 🚀**

*Submission Deadline: TODAY 11:59 PM*
*Questions? Refer to README.md and code comments*
