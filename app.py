from flask import Flask, render_template, request

app = Flask(__name__)

# Game variables
player = {
    "name": "",
    "weapon": "",
    "resources": []
}

current_chapter = 1

# Game content
chapters = [
    {
        "title": "The Mysterious Forest",
        "text": "As you step into the dense, ancient forest, the foliage closes behind you, leaving only a faint trail. The air is thick with enchantment, and the path ahead seems both inviting and ominous.",
        "options": ["LOOK", "INVENTORY", "MOVE FORWARD"]
    },
    {
        "title": "The Whispering Grove",
        "text": "You find yourself in a clearing surrounded by ancient trees. The wind carries whispers, and a shimmering light dances in the distance.",
        "options": ["LISTEN", "APPROACH", "REST"]
    },
    {
        "title": "The Crossroads",
        "text": "The path forks, and you're unsure which way to go. Mysterious sounds echo from both directions.",
        "options": ["EXAMINE", "CHOOSE LEFT", "CHOOSE RIGHT"]
    },
    {
        "title": "The Mystic Guardian",
        "text": "A mystical creature blocks your path, guarding a mysterious portal. It seems friendly but cautious.",
        "options": ["COMMUNICATE", "SHOW [Resource]", "ATTACK"]
    },
    {
        "title": "The Conclusion",
        "text": "Your decisions have led you to a clearing where the enchantment feels even stronger. The path ahead splits into two, leading to unknown destinations.",
        "options": ["DECIDE [Path]", "WAIT", "REFLECT"]
    }
]

# Game routes
@app.route("/", methods=["GET", "POST"])
def index():
    global current_chapter

    if request.method == "POST":
        action = request.form["action"]

        # Process player's action
        process_action(action)

    # Render the current chapter
    return render_template("index.html", chapter=chapters[current_chapter - 1], player=player)

def process_action(action):
    global current_chapter

    current_chapter_data = chapters[current_chapter - 1]

    # Check the player's action and update the game state accordingly
    if action == "LOOK":
        player_message = "You carefully observe your surroundings."
    elif action == "INVENTORY":
        player_message = f"Your inventory: {' , '.join(player['resources'])}"
    elif action == "MOVE FORWARD":
        player_message = "You decide to move forward."
        current_chapter += 1
    else: 
        # Handle unknown action
        player_message = "Invalid action. Try again."

    # Update the player's message in the game state
    player['message'] = player_message

    #Ensure the chapter index is within bounds
    if current_chapter > len(chapters):
        current_chapter = 1

if __name__ == "__main__":
    app.run(debug=True)


