from flask import Flask, render_template, request

app = Flask(__name__)

# Gamme variables
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
        "text": "As you step into the dense, ancient forest, the foliage closes behind you, leaving only a faint trail. The air is thick with enchantment, and the path ahead seems both inviting and ominous."
        "options": ["LOOK","INVENTORY","MOVE FORWARD"]
    },
    {
        "title": "The Whispering Grove",
        "text": "You find yourself in a clearing surrounded by  ancient trees. The wind carries whispers, and a shimmering light dances in the distance.",
        "options": ["LISTEN", "APPROACH", "REST"]
    },
    {
        "title": "The Crossroads",
        "text": "The path forks, and you're unsure which way to go. Mysterious sounds echo from both directions.",
        "options": ["EXAMINE", "CHOOSE LEFT", "CHOOSE RIGHT"]
    },
    {
        "title": "The Mystic Guardian",
        "text": "A mystical creature blocks your path, guarding a mysterious portal.It seems friendly but cautious.",
        "options": ["COMMUNICATE", "SHOW [Resource]", "ATTACK"]
    },
    {
        "title": "The Conclusion",
        "text": "Your decisions have led you to a clearing where the enchatment feels even stronger. The path ahead splits into two, leading to unknown destinations."
        "options": ["DECIDE [Path]", "WAIT", "REFLECT"]
    }
]

# Game routes
app.rotute("/", methods=["GET", "POST"])
def index():
    global current_chapter

    if request.method == "POST":
        action = request.form["action"]

        # Process