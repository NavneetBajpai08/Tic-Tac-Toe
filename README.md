# 🎮 Tic-Tac-Toe using Python, NumPy & Streamlit

An interactive **Tic-Tac-Toe game** built using Python, NumPy, and Streamlit. The game supports two-player X vs O gameplay with automatic winner and draw detection.

## ✨ Features

* 🎮 Interactive 3×3 game board
* ❌ X vs O two-player gameplay
* 🔄 Automatic turn switching
* 🏆 Winner detection
* 🤝 Draw detection
* 🔁 Restart game option
* 🔢 NumPy-based board management
* 🌐 Streamlit web interface
* 💻 Simple and beginner-friendly implementation

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Streamlit**

## 📂 Project Structure

```text
tic-tac-toe/
│
├── tic_tac_toe.py
└── README.md
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/tic-tac-toe.git
```

### 2. Navigate to the Project Folder

```bash
cd tic-tac-toe
```

### 3. Install Dependencies

```bash
pip install numpy streamlit
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run tic_tac_toe.py
```

After running the command, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your web browser to play the game.

## 🎯 How to Play

1. Player **X** starts the game.
2. Click any empty cell to place your mark.
3. Player **O** takes the next turn.
4. Players continue taking turns.
5. Get three marks in a row, column, or diagonal to win.
6. If all cells are filled without a winner, the game ends in a draw.
7. Click **🔄 Restart Game** to start a new match.

## 🧠 Game Logic

The board uses a NumPy 3×3 array:

```text
0   0   0
0   0   0
0   0   0
```

The values represent:

| Value | Meaning    |
| ----- | ---------- |
| `0`   | Empty cell |
| `1`   | Player X   |
| `-1`  | Player O   |

NumPy is used to check rows, columns, and diagonals for winning combinations.

Streamlit's **session state** stores the board, current player, and game result so that the game state is maintained between interactions.

## 📸 Screenshot

You can add a screenshot of your game here:

```markdown
![Tic-Tac-Toe](screenshot.png)
```

## 🔮 Future Improvements

Possible future features include:

* 🤖 AI opponent using the Minimax algorithm
* 🎚️ Difficulty levels
* 📊 Score tracking
* 👤 Custom player names
* 🎨 Improved UI and animations
* 📜 Game history
* 🌐 Online multiplayer

## 👨‍💻 Author

**Navneet Bajpai**

B.Tech — Artificial Intelligence & Machine Learning

---

⭐ If you found this project useful, consider giving the repository a star!
