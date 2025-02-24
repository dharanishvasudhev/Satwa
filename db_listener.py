import mysql.connector
import time

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'WillofD@30',
    'database': 'satwa'
}

# Class to angle mapping (12 classes, 30-degree step)
angle_mapping = {
    "biological": 0, "brown glass": 30, "white glass": 60, "trash": 90,
    "shoes": 120, "plastic": 150, "paper": 180, "clothes": 210,
    "metal": 240, "cardboard": 270, "green glass": 300, "Unknown": 330
}

def get_latest_prediction():
    """ Fetch the latest entry from garbage_classification """
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        query = "SELECT predicted_class FROM garbage_classification ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            predicted_class = result[0]
            angle = angle_mapping.get(predicted_class, angle_mapping["Unknown"])
            print(f"The servo motor rotated {angle}° for class: {predicted_class}")

        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def monitor_database():
    """ Continuously checks for new insertions """
    last_timestamp = None

    while True:
        try:
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            cursor.execute("SELECT timestamp FROM trigger_log ORDER BY id DESC LIMIT 1")
            latest = cursor.fetchone()

            if latest and latest[0] != last_timestamp:
                print("New entry detected! Processing latest data...")
                last_timestamp = latest[0]
                get_latest_prediction()

            cursor.close()
            db.close()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")

        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    print("Listening for new database entries...")
    monitor_database()
