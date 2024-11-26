from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import json
import os

# Create a blueprint
challenges_bp = Blueprint('challenges', __name__)

# Path to the JSON file
DATA_FILE = os.path.join(os.path.dirname(__file__), '../../data/challenges.json')

# Load challenges from JSON file
def load_challenges():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)
    
# Save challenges to JSON file
def save_challenges(challenges):
    with open(DATA_FILE, 'w') as file:
        json.dump(challenges, file, indent=4)

# Route to display challenges        
@challenges_bp.route('/', methods=['GET'])
def view_challenges():
    challenges = load_challenges()
    return render_template('challenges.html', challenges=challenges), 200, {'Content-Type': 'text/html; charset=utf-8'}

# Route to add a challenge
@challenges_bp.route('/add', methods=['POST'])
def add_challenge():
    challenges = load_challenges()
    new_id = max([challenge['id'] for challenge in challenges] + [0]) + 1 # Generate unique ID
    new_challenge = {
        'id': new_id,
        'title': request.form['title']
    }
    challenges.append(new_challenge)
    save_challenges(challenges)
    return redirect(url_for('challenges.view_challenges'))

# Route to remove a challenge
@challenges_bp.route('/delete/<int:challenge_id>', methods=['POST'])
def remove_challenge(challenge_id):
    challenges = load_challenges()
    challenges = [challenge for challenge in challenges if challenge['id'] != challenge_id]
    save_challenges(challenges)
    return redirect(url_for('challenges.view_challenges'))