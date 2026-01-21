"""
CRUD Tank - A Flask MVC Application for Teaching CRUD Operations

This application demonstrates the Model-View-Controller (MVC) pattern
using a fun fish tank metaphor. Students can:
- CREATE fish (add them to the tank)
- READ fish (view them swimming in the tank)
- UPDATE fish (edit their properties)
- DELETE fish (remove them from the tank)

Run this application with: python app.py
Then visit: http://localhost:5000
"""

from flask import Flask
from controllers.fish_controller import fish_bp

# Create the Flask application instance
app = Flask(__name__)

# Secret key for session management and flash messages
app.secret_key = 'crud-tank-secret-key-for-education'

# Register the fish controller blueprint
app.register_blueprint(fish_bp)

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   🐟 Welcome to CRUD Tank! 🐟                             ║
    ║                                                           ║
    ║   An educational Flask MVC application for learning       ║
    ║   Create, Read, Update, and Delete operations.            ║
    ║                                                           ║
    ║   Visit: http://localhost:5000                            ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    app.run(debug=True, port=5000)
