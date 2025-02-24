import numpy as np
import pandas as pd
import gradio as gr
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 🎯 Generate Sample Dataset
data_size = 500

df = pd.DataFrame({
    "paper": np.random.uniform(0, 100, data_size),
    "metal": np.random.uniform(0, 100, data_size),
    "organic": np.random.uniform(0, 100, data_size),
    "glass": np.random.uniform(0, 100, data_size),
    "cardboard": np.random.uniform(0, 100, data_size),
    "plastic": np.random.uniform(0, 100, data_size),
})

# 🌱 Define Environmental Benefits
df["water_saved"] = df["paper"] * 5 + df["glass"] * 2 + df["cardboard"] * 3 + np.random.uniform(0, 50, data_size)
df["co2_saved"] = df["metal"] * 8 + df["plastic"] * 6 + df["paper"] * 4 + np.random.uniform(0, 30, data_size)
df["trees_saved"] = (df["paper"] * 0.1 + df["cardboard"] * 0.05 + np.random.uniform(0, 5, data_size)).round().astype(int)

# 🏋️ Split Data for Training
X = df[["paper", "metal", "organic", "glass", "cardboard", "plastic"]]
y = df[["water_saved", "co2_saved", "trees_saved"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🎯 Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Evaluate Model Performance
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")

# 🔮 Prediction Function
def predict_savings(paper, metal, organic, glass, cardboard, plastic):
    input_data = np.array([[paper, metal, organic, glass, cardboard, plastic]])
    prediction = model.predict(input_data)[0]
    
    return {
        "Water Saved (Liters)": round(prediction[0], 2),
        "CO2 Saved (kg)": round(prediction[1], 2),
        "Trees Saved": int(round(prediction[2]))
    }

# 🎨 Gradio Interface
interface = gr.Interface(
    fn=predict_savings,
    inputs=[
        gr.Number(label="Paper (kg)"),
        gr.Number(label="Metal (kg)"),
        gr.Number(label="Organic (kg)"),
        gr.Number(label="Glass (kg)"),
        gr.Number(label="Cardboard (kg)"),
        gr.Number(label="Plastic (kg)")
    ],
    outputs="json",
    title="♻️ Environmental Impact Estimator",
    description="Enter the weight (kg) of different waste materials to estimate environmental savings! 🌱"
)

# 🚀 Launch the App
if __name__ == "__main__":
    interface.launch()
