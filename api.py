from gradio_client import Client
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'satwa'
}

# Create a client to communicate with the deployed Hugging Face Space

client = Client("vasudhevdharanish/cycleworks")

# Call the /predict endpoint with the necessary input data
result = client.predict(
    paper=3,         # weight of paper in kg
    metal=3,         # weight of metal in kg
    organic=3,       # weight of organic material in kg
    glass=3,         # weight of glass in kg
    cardboard=3,     # weight of cardboard in kg
    plastic=3,       # weight of plastic in kg
    api_name="/predict"  # the API endpoint
)

# Print the result received from the API
print(result)
