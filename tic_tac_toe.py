import numpy as np
import streamlit as st

# ----------------------------
# Page configuration
# ----------------------------
st.set_page_config(
    page_title="Tic-Tac-Toe",
    page_icon="🎮",
    layout="centered"
)

# ----------------------------
# Initialize session state
# ----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.result = None


symbols = {
    0: " ",
    1: "X",
    -1: "O"
}


# ----------------------------
# Winner checking
# ----------------------------
def check_winner(board):

    # Rows
    for row in board:
        if np.sum(row) == 3:
            return "X"

        if np.sum(row) == -3:
            return "O"

    # Columns
    for col in board.T:
        if np.sum(col) == 3:
            return "X"

        if np.sum(col) == -3:
            return "O"

    # Main diagonal
    if np.trace(board) == 3:
        return "X"

    if np.trace(board) == -3:
        return "O"

    # Other diagonal
    other_diagonal = np.fliplr(board)

    if np.trace(other_diagonal) == 3:
        return "X"

    if np.trace(other_diagonal) == -3:
        return "O"

    # Draw
    if not np.any(board == 0):
        return "DRAW"

    return None


# ----------------------------
# Make a move
# ----------------------------
def make_move(row, col):

    if (
        int(st.session_state.board[row, col]) == 0
        and st.session_state.result is None
    ):

        st.session_state.board[row, col] = st.session_state.current

        result = check_winner(st.session_state.board)

        if result is not None:
            st.session_state.result = result
        else:
            st.session_state.current *= -1

        st.rerun()


# ----------------------------
# Title
# ----------------------------
st.title("🎮 Tic-Tac-Toe")
st.caption("Built with NumPy + Streamlit")


# ----------------------------
# Game status
# ----------------------------
if st.session_state.result == "DRAW":

    st.success("😎 Ohoo, it's a draw!")

elif st.session_state.result is not None:

    st.success(
        f"🏆 {st.session_state.result} wins!"
    )

else:

    turn = "X" if st.session_state.current == 1 else "O"

    st.info(
        f"It's **{turn}**'s turn"
    )


# ----------------------------
# 3 × 3 Board
# ----------------------------
for i in range(3):

    cols = st.columns(3)

    for j in range(3):

        # Convert NumPy value to normal Python integer
        value = int(st.session_state.board[i, j])

        cell_value = symbols[value]

        # IMPORTANT:
        # Convert NumPy bool to normal Python bool
        is_disabled = bool(
            value != 0
            or st.session_state.result is not None
        )

        with cols[j]:

            if st.button(
                cell_value,
                key=f"cell_{i}_{j}",
                disabled=is_disabled,
                use_container_width=True
            ):

                make_move(i, j)


# ----------------------------
# Restart
# ----------------------------
st.divider()

if st.button(
    "🔄 Restart Game",
    use_container_width=True
):

    st.session_state.board = np.zeros(
        (3, 3),
        dtype=int
    )

    st.session_state.current = 1
    st.session_state.result = None

    st.rerun()