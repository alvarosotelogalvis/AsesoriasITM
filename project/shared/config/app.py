from project.app import blueprint as blueprints
from project.shared.config.createTables import get_tables
from project.shared.config.jwt import config_jwt
from project.shared.domain.seeders import seeders

from flask import Flask, jsonify
from flask_cors import CORS

# Init app
app = Flask(__name__)

# Register the blueprints
app.register_blueprint(blueprints)

# JWT
jwt = config_jwt(app)

# Add the command to run the seeders
app.cli.add_command(seeders.run_seeders)

# Create tables from models
get_tables()

# Configure CORS
CORS(
    app=app,
    origins="*",
    methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization"]
)

# Endpoint to check API health.
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
