from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Przechowywanie stanów przełączników na serwerze
light_states = {
    'salon': False,
    'kitchen': False,
    'bathroom': False,
    'wardrobe': False,
    'bedroom': False,
    'hall': False,
    'bathroom_led': False,
    'bathroom_mirror': False
}

# Przechowywanie temperatur w pokojach
temperature_states = {
    'salon': 22,  # Domyślna temperatura
    'bedroom': 22,
    'bathroom': 22
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lights')
def lights():
    return render_template('lights.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/security')
def security():
    return render_template('security.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

# Obsługa WebSocket - synchronizacja stanów przełączników
@socketio.on('toggle_light')
def handle_toggle_light(data):
    room = data.get('room')
    state = data.get('state')

    if room in light_states and isinstance(state, bool):
        # Aktualizacja stanu przełącznika
        light_states[room] = state
        # Emituj zmiany do wszystkich podłączonych klientów
        socketio.emit('update_light', {'room': room, 'state': state})
    else:
        print(f"Invalid data received: {data}")

@socketio.on('get_states')
def handle_get_states():
    # Wyślij aktualne stany przełączników do klienta
    socketio.emit('sync_states', light_states)

# Obsługa WebSocket - synchronizacja temperatur
@socketio.on('set_temperature')
def handle_set_temperature(data):
    room = data.get('room')
    temperature = data.get('temperature')

    if room in temperature_states and isinstance(temperature, int) and 16 <= temperature <= 30:
        # Aktualizacja temperatury w pokoju
        temperature_states[room] = temperature
        # Emituj zmiany temperatury do wszystkich podłączonych klientów
        socketio.emit('sync_temperature', {'room': room, 'temperature': temperature})
    else:
        print(f"Invalid data received for temperature: {data}")

@socketio.on('get_temperatures')
def handle_get_temperatures():
    # Wyślij aktualne temperatury do klienta
    socketio.emit('sync_temperature', temperature_states)

if __name__ == '__main__':
    # Uruchom aplikację Flask z WebSocket
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)