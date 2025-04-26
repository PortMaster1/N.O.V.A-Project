import threading
import time
import sqlite3
import paho.mqtt.client as mqtt
from flask import Flask, jsonify

# --- MQTT Setup ---
BROKER = 'your.mqtt.broker.ip'
TOPIC = 'notify/her'

mqtt_client = mqtt.Client()

# --- Flask Setup ---
app = Flask(__name__)

def get_messages_for(recipient):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('SELECT id, message FROM messages WHERE recipient=? AND delivered=0', (recipient,))
    messages = c.fetchall()
    conn.close()
    return messages

def mark_messages_delivered(message_ids):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.executemany('UPDATE messages SET delivered=1 WHERE id=?', [(mid,) for mid in message_ids])
    conn.commit()
    conn.close()

@app.route('/get_messages/<recipient>', methods=['GET'])
def get_messages(recipient):
    messages = get_messages_for(recipient)
    message_list = [{'id': mid, 'message': msg} for (mid, msg) in messages]

    if message_list:
        mark_messages_delivered([m['id'] for m in message_list])

    return jsonify(message_list)

# --- Thread targets ---

def run_flask():
    app.run(host='0.0.0.0', port=5000)

def run_mqtt():
    mqtt_client.connect(BROKER)
    mqtt_client.loop_forever()

# --- Main ---

if __name__ == "__main__":
    # Start Flask server thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start MQTT client thread
    mqtt_thread = threading.Thread(target=run_mqtt)
    mqtt_thread.start()

    # (optional) Keep main thread alive
    while True:
        time.sleep(1)