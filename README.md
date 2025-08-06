# 🏠 House Price Prediction Web App

A machine learning-powered web app that predicts housing prices in Bengaluru based on location, square footage, number of bathrooms, and bedrooms.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://house-price-predictor-babmyikfyjxf4npuulpuki.streamlit.app/)

---

## 🧠 Features

- Predicts housing prices in Bengaluru
- Uses a trained ML model (Linear Regression)
- Clean, interactive UI using Streamlit
- Input parameters: location, BHK, bathrooms, total sqft

---

## 💡 How It Works

1. The dataset (`Bengaluru_House_Data.csv`) is cleaned and preprocessed.
2. A Linear Regression model is trained and evaluated (R² ≈ 0.51).
3. The model is saved as a `.pkl` file using `joblib`.
4. A Streamlit frontend loads the model and takes user input to predict price.

---

## 🛠️ Built With

- Python
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib

---

## 🧪 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/madhur140305/house-price-predictor.git
cd house-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


## 🧑‍💻 Author

**Madhur Kumar**  
B.Tech CSE | VIT Vellore  
📧 madhur140305@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/madhur140305) | [GitHub](https://github.com/madhur140305)


## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) — for making web app development easy and fast
- [Kaggle: Bengaluru Housing Dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) — used for training the model
- Inspired by the learning journey of Data Science and Machine Learning


