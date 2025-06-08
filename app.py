import streamlit as st
import pandas as pd
import pickle

# Load model and imputer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("imputer.pkl", "rb") as f:
    imputer = pickle.load(f)

st.title("🏡 House Price Predictor")

uploaded_file = st.file_uploader("Upload a CSV with columns: GrLivArea, BedroomAbvGr, FullBath", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Validate required columns
    required_cols = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
    if all(col in data.columns for col in required_cols):
        X = data[required_cols]
        X_imputed = imputer.transform(X)
        predictions = model.predict(X_imputed)
        data['PredictedPrice'] = predictions

        st.write("### 📊 Predictions:")
        st.dataframe(data)

        # Download button
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV with Predictions", csv, "predictions.csv", "text/csv")
    else:
        st.error(f"❌ Your CSV must contain these columns: {required_cols}")
