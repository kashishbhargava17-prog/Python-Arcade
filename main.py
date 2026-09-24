import tkinter as tk
import random

# ============================================================
# PYTHON ARCADE
# ============================================================

window = tk.Tk()
window.title("PYTHON ARCADE  •  Level Up Your Python")
window.geometry("1100x700")
window.resizable(False, False)
window.configure(bg="#03040B")
window.option_add("*Font", ("Segoe UI", 10))

# ============================================================
# COLORS
# ============================================================

BG = "#060712"
NAVY = "#090C1B"
PURPLE = "#8B5CF6"
PURPLE_LIGHT = "#B49CFF"
PINK = "#EC4899"
CYAN = "#22D3EE"
BLUE = "#3B82F6"
GREEN = "#34D399"
ORANGE = "#F59E0B"
WHITE = "#FFFFFF"
LIGHT = "#DDE3F5"
GREY = "#8993B2"
CARD = "#11162D"
CARD_BORDER = "#252B4A"

# ============================================================
# MAIN CANVAS
# ============================================================

canvas = tk.Canvas(
    window,
    width=1100,
    height=700,
    bg=BG,
    highlightthickness=0,
    bd=0
)

canvas.pack()

page_items = []
page_widgets = []

# ============================================================
# PLAYER ACCOUNTS
# ============================================================

ACCOUNT_FILE = "player_accounts.txt"

current_username = ""
player_xp = 0


def load_accounts():

    accounts = []

    try:

        file = open(ACCOUNT_FILE, "r")

        for line in file:

            line = line.strip()

            if line != "":

                parts = line.split("|")

                if len(parts) == 3:

                    username = parts[0]
                    password = parts[1]
                    xp = int(parts[2])

                    accounts.append(
                        [username, password, xp]
                    )

        file.close()

    except:

        accounts = []

    return accounts


def save_accounts(accounts):

    file = open(ACCOUNT_FILE, "w")

    for account in accounts:

        username = account[0]
        password = account[1]
        xp = account[2]

        file.write(
            username + "|" +
            password + "|" +
            str(xp) + "\n"
        )

    file.close()


accounts = load_accounts()


def save_current_account():

    global accounts

    if current_username == "":
        return

    for account in accounts:

        if account[0] == current_username:

            account[2] = player_xp

    save_accounts(accounts)


def close_arcade():

    save_current_account()
    window.destroy()


window.protocol(
    "WM_DELETE_WINDOW",
    close_arcade
)

# ============================================================
# GAME STATISTICS
# ============================================================

GAME_STATS_FILE = "game_statistics.txt"

game_statistics = {}


def load_game_statistics():

    statistics = {}

    try:

        file = open(GAME_STATS_FILE, "r")

        for line in file:

            line = line.strip()

            if line != "":

                parts = line.split("|")

                if len(parts) == 6:

                    username = parts[0]
                    games_played = int(parts[1])
                    games_won = int(parts[2])
                    games_lost = int(parts[3])
                    xp_earned = int(parts[4])
                    most_played = parts[5]

                    statistics[username] = [
                        games_played,
                        games_won,
                        games_lost,
                        xp_earned,
                        most_played
                    ]

        file.close()

    except:

        statistics = {}

    return statistics


def save_game_statistics():

    file = open(GAME_STATS_FILE, "w")

    for username in game_statistics:

        stats = game_statistics[username]

        file.write(
            username + "|" +
            str(stats[0]) + "|" +
            str(stats[1]) + "|" +
            str(stats[2]) + "|" +
            str(stats[3]) + "|" +
            stats[4] + "\n"
        )

    file.close()


game_statistics = load_game_statistics()


# ============================================================
# GAME STAT FUNCTIONS
# ============================================================

def create_player_statistics(username):

    if username not in game_statistics:

        game_statistics[username] = [
            0,
            0,
            0,
            0,
            "None"
        ]

        save_game_statistics()


def record_game(game_name, won, xp):

    global game_statistics

    if current_username == "":
        return

    create_player_statistics(current_username)

    stats = game_statistics[current_username]

    # Games played

    stats[0] += 1

    # Games won / lost

    if won:

        stats[1] += 1

    else:

        stats[2] += 1

    # XP earned

    stats[3] += xp

    # Most played game

    stats[4] = game_name

    save_game_statistics()

# ============================================================
# PAGE MANAGEMENT
# ============================================================

def clear_page():

    global page_items, page_widgets

    for item in page_items:

        try:
            canvas.delete(item)
        except:
            pass

    page_items = []

    for widget in page_widgets:

        try:
            widget.destroy()
        except:
            pass

    page_widgets = []


def add_item(item):

    page_items.append(item)
    return item


def add_widget(widget):

    page_widgets.append(widget)
    return widget

# ============================================================
# BACKGROUND
# ============================================================

def draw_background():

    canvas.delete("background")

    canvas.create_rectangle(
        0,
        0,
        1100,
        700,
        fill=BG,
        outline="",
        tags="background"
    )

    # Decorative rings

    canvas.create_oval(
        -180,
        -180,
        350,
        350,
        outline="#17133A",
        width=3,
        tags="background"
    )

    canvas.create_oval(
        -130,
        -130,
        300,
        300,
        outline="#10102B",
        width=1,
        tags="background"
    )

    canvas.create_oval(
        820,
        470,
        1240,
        890,
        outline="#161438",
        width=3,
        tags="background"
    )

    canvas.create_oval(
        760,
        -170,
        1150,
        220,
        outline="#101D38",
        width=2,
        tags="background"
    )

    # Grid

    for x in range(0, 1100, 55):

        canvas.create_line(
            x,
            100,
            x,
            700,
            fill="#0B1020",
            tags="background"
        )

    for y in range(100, 700, 55):

        canvas.create_line(
            0,
            y,
            1100,
            y,
            fill="#0B1020",
            tags="background"
        )

    # Particles

    particles = [
        (80, 170, PURPLE),
        (160, 550, CYAN),
        (270, 125, PINK),
        (450, 175, PURPLE),
        (610, 110, CYAN),
        (740, 610, PINK),
        (930, 310, PURPLE),
        (1020, 460, CYAN),
        (60, 630, PINK),
        (520, 640, PURPLE),
        (1000, 150, PINK),
        (350, 620, CYAN)
    ]

    for x, y, color in particles:

        canvas.create_oval(
            x - 2,
            y - 2,
            x + 2,
            y + 2,
            fill=color,
            outline="",
            tags="background"
        )

    # Small stars

    stars = [
        (120, 110),
        (210, 610),
        (400, 105),
        (680, 145),
        (840, 410),
        (970, 590),
        (1050, 280)
    ]

    for x, y in stars:

        canvas.create_text(
            x,
            y,
            text="✦",
            fill="#25204C",
            font=("Segoe UI", 8),
            tags="background"
        )

# ============================================================
# NAVBAR
# ============================================================

def create_navbar():

    # Main navbar

    canvas.create_rectangle(
        0,
        0,
        1100,
        92,
        fill=NAVY,
        outline="",
        tags="nav"
    )

    # Subtle glow strips

    canvas.create_rectangle(
        0,
        89,
        1100,
        92,
        fill="#17133A",
        outline="",
        tags="nav"
    )

    canvas.create_line(
        0,
        91,
        1100,
        91,
        fill="#332A62",
        width=1,
        tags="nav"
    )

    # ========================================================
    # LOGO GLOW
    # ========================================================

    canvas.create_oval(
        22,
        13,
        72,
        73,
        outline="#211B48",
        width=2,
        tags="nav"
    )

    canvas.create_oval(
        28,
        19,
        66,
        67,
        outline="#15132F",
        width=1,
        tags="nav"
    )

    # Diamond

    canvas.create_text(
        47,
        43,
        text="◆",
        fill="#4A2C8E",
        font=("Segoe UI", 31, "bold"),
        tags="nav"
    )

    canvas.create_text(
        47,
        41,
        text="◆",
        fill=PURPLE,
        font=("Segoe UI", 24, "bold"),
        tags="nav"
    )

    # PYTHON

    canvas.create_text(
        78,
        29,
        text="PYTHON",
        fill=WHITE,
        font=("Segoe UI", 18, "bold"),
        anchor="w",
        tags="nav"
    )

    # ARCADE

    canvas.create_text(
        78,
        55,
        text="ARCADE",
        fill=CYAN,
        font=("Segoe UI", 15, "bold"),
        anchor="w",
        tags="nav"
    )

    # Accent line

    canvas.create_rectangle(
        78,
        71,
        168,
        74,
        fill=PURPLE,
        outline="",
        tags="nav"
    )

    canvas.create_rectangle(
        168,
        71,
        200,
        74,
        fill=CYAN,
        outline="",
        tags="nav"
    )

    # Tiny subtitle

    canvas.create_text(
        78,
        82,
        text="LEVEL UP YOUR PYTHON",
        fill="#59627F",
        font=("Segoe UI", 6, "bold"),
        anchor="w",
        tags="nav"
    )

    # ========================================================
    # NAVIGATION BACKGROUND SEPARATOR
    # ========================================================

    canvas.create_line(
        275,
        20,
        275,
        72,
        fill="#242544",
        width=1,
        tags="nav"
    )

    # ========================================================
    # NAVIGATION BUTTONS
    # ========================================================

    nav_items = [
        ("HOME", show_home, 310, 60),
        ("GAMES", show_games, 405, 65),
        ("SCORES", show_scores, 505, 75),
        ("ABOUT", show_about, 615, 65)
    ]

    for text, command, x, width in nav_items:

        button = tk.Button(
            window,
            text=text,
            command=command,
            bg=NAVY,
            fg=LIGHT,
            activebackground="#11162D",
            activeforeground=PURPLE_LIGHT,
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold")
        )

        button.place(
            x=x,
            y=25,
            width=width,
            height=40
        )

        add_widget(button)

    # ========================================================
    # ACHIEVEMENTS BUTTON
    # ========================================================

    achievement_button = tk.Button(
        window,
        text="🏆",
        command=show_achievements,
        bg=NAVY,
        fg=ORANGE,
        activebackground="#11162D",
        activeforeground="#FFD166",
        relief="flat",
        bd=0,
        highlightthickness=0,
        cursor="hand2",
        font=("Segoe UI", 18, "bold")
    )

    achievement_button.place(
        x=690,
        y=25,
        width=55,
        height=40
    )

    add_widget(achievement_button)

    # ========================================================
    # RIGHT SIDE SEPARATOR
    # ========================================================

    canvas.create_line(
        760,
        20,
        760,
        72,
        fill="#242544",
        width=1,
        tags="nav"
    )

    # ========================================================
    # PLAYER PROFILE BUTTON
    # ========================================================

    profile_button = tk.Button(
        window,
        text="PLAYER\nLEVEL 01",
        command=show_profile,
        bg=NAVY,
        fg=WHITE,
        activebackground="#11162D",
        activeforeground=PURPLE_LIGHT,
        relief="flat",
        bd=0,
        highlightthickness=0,
        cursor="hand2",
        font=("Segoe UI", 8, "bold"),
        justify="left"
    )

    profile_button.place(
        x=785,
        y=22,
        width=85,
        height=45
    )

    add_widget(profile_button)

    # ========================================================
    # XP BADGE
    # ========================================================

    canvas.create_rectangle(
        885,
        24,
        1025,
        66,
        fill="#11162D",
        outline="#292452",
        width=1,
        tags="nav"
    )

    canvas.create_text(
        905,
        35,
        text="✦",
        fill=PURPLE,
        font=("Segoe UI", 12, "bold"),
        tags="nav"
    )

    canvas.create_text(
        925,
        35,
        text="XP",
        fill=GREY,
        font=("Segoe UI", 7, "bold"),
        anchor="w",
        tags="nav"
    )

    canvas.create_text(
        925,
        52,
        text=str(player_xp),
        fill=CYAN,
        font=("Segoe UI", 12, "bold"),
        anchor="w",
        tags="nav"
    )

    # Tiny end accent

    canvas.create_rectangle(
        1038,
        31,
        1042,
        59,
        fill=PURPLE,
        outline="",
        tags="nav"
    )

    canvas.create_rectangle(
        1045,
        36,
        1049,
        54,
        fill=CYAN,
        outline="",
        tags="nav"
    )


# ============================================================
# ACHIEVEMENTS
# ============================================================

def show_achievements():

    clear_page()
    draw_background()
    create_navbar()

    add_item(canvas.create_text(
        550,
        125,
        text="ACHIEVEMENTS",
        fill=ORANGE,
        font=("Segoe UI", 28, "bold")
    ))

    add_item(canvas.create_text(
        550,
        165,
        text="Collect XP and unlock your arcade milestones.",
        fill=GREY,
        font=("Segoe UI", 11)
    ))

    achievements = [
        ("🌱", "GETTING STARTED", "Reach 100 XP", 100),
        ("⚡", "XP HUNTER", "Reach 250 XP", 250),
        ("🔥", "XP MASTER", "Reach 500 XP", 500),
        ("💎", "ARCADE ELITE", "Reach 1,000 XP", 1000),
        ("👑", "ARCADE LEGEND", "Reach 2,000 XP", 2000)
    ]

    positions = [
        (315, 250),
        (785, 250),
        (315, 355),
        (785, 355),
        (550, 460)
    ]

    for achievement, position in zip(achievements, positions):

        icon, title, description, required_xp = achievement

        x, y = position

        unlocked = player_xp >= required_xp

        if unlocked:
            border = ORANGE
            status = "✓ UNLOCKED"
            status_color = GREEN
        else:
            border = CARD_BORDER
            status = "🔒 LOCKED"
            status_color = GREY

        canvas.create_rectangle(
            x - 200,
            y - 45,
            x + 200,
            y + 45,
            fill=CARD,
            outline=border,
            width=2,
            tags="page"
        )

        canvas.create_text(
            x - 160,
            y,
            text=icon,
            fill=ORANGE if unlocked else GREY,
            font=("Segoe UI", 22, "bold"),
            tags="page"
        )

        canvas.create_text(
            x - 120,
            y - 15,
            text=title,
            fill=WHITE if unlocked else GREY,
            font=("Segoe UI", 11, "bold"),
            anchor="w",
            tags="page"
        )

        canvas.create_text(
            x - 120,
            y + 12,
            text=description,
            fill=GREY,
            font=("Segoe UI", 9),
            anchor="w",
            tags="page"
        )

        canvas.create_text(
            x + 150,
            y,
            text=status,
            fill=status_color,
            font=("Segoe UI", 8, "bold"),
            anchor="e",
            tags="page"
        )

    canvas.create_text(
        550,
        570,
        text=f"CURRENT XP  •  {player_xp}",
        fill=CYAN,
        font=("Segoe UI", 12, "bold"),
        tags="page"
    )

    create_button(
        470,
        615,
        160,
        40,
        "← BACK",
        show_home,
        CARD_BORDER
    )

# ============================================================
# PLAYER STATISTICS
# ============================================================

def show_profile():

    clear_page()
    draw_background()
    create_navbar()

    # ========================================================
    # GET PLAYER GAME STATISTICS
    # ========================================================

    create_player_statistics(current_username)

    stats = game_statistics[current_username]

    games_played = stats[0]
    games_won = stats[1]
    games_lost = stats[2]
    xp_earned = stats[3]
    most_played = stats[4]

    # ========================================================
    # TITLE
    # ========================================================

    add_item(canvas.create_text(
        550,
        115,
        text="PLAYER STATISTICS",
        fill=CYAN,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text="Your Python Arcade progress at a glance.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    # ========================================================
    # LEADERBOARD DATA
    # ========================================================

    leaderboard = []

    for account in accounts:

        username = account[0]
        xp = account[2]

        leaderboard.append(
            [username, xp]
        )

    # Sort highest XP first

    for i in range(len(leaderboard)):

        for j in range(i + 1, len(leaderboard)):

            if leaderboard[j][1] > leaderboard[i][1]:

                temporary = leaderboard[i]

                leaderboard[i] = leaderboard[j]

                leaderboard[j] = temporary

    # ========================================================
    # PLAYER RANK
    # ========================================================

    player_rank = 0

    for i in range(len(leaderboard)):

        if leaderboard[i][0] == current_username:

            player_rank = i + 1

            break

    # ========================================================
    # LEVEL
    # ========================================================

    level = (player_xp // 100) + 1

    current_level_xp = player_xp % 100

    xp_to_next = 100 - current_level_xp

    if current_level_xp == 0:

        xp_to_next = 100

    progress_width = 320 * current_level_xp / 100

    # ========================================================
    # ACHIEVEMENTS
    # ========================================================

    achievement_count = 0

    achievement_requirements = [
        100,
        250,
        500,
        1000,
        2000
    ]

    for required_xp in achievement_requirements:

        if player_xp >= required_xp:

            achievement_count += 1

    # ========================================================
    # MAIN CARD
    # ========================================================

    add_item(canvas.create_rectangle(
        70,
        180,
        1030,
        625,
        fill=CARD,
        outline="#292452",
        width=2
    ))

    # ========================================================
    # PLAYER ICON
    # ========================================================

    add_item(canvas.create_oval(
        115,
        210,
        195,
        290,
        fill="#17133A",
        outline=PURPLE,
        width=2
    ))

    add_item(canvas.create_text(
        155,
        250,
        text="◆",
        fill=PURPLE,
        font=("Segoe UI", 27, "bold")
    ))

    # ========================================================
    # PLAYER NAME
    # ========================================================

    add_item(canvas.create_text(
        220,
        215,
        text=current_username.upper(),
        fill=WHITE,
        font=("Segoe UI", 17, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        220,
        242,
        text="PYTHON ARCADE PLAYER",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    # ========================================================
    # LEVEL + XP
    # ========================================================

    add_item(canvas.create_text(
        220,
        275,
        text=f"LEVEL {level:02d}",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        220,
        302,
        text=f"{player_xp} XP",
        fill=CYAN,
        font=("Segoe UI", 16, "bold"),
        anchor="w"
    ))

    # ========================================================
    # XP PROGRESS
    # ========================================================

    add_item(canvas.create_text(
        440,
        270,
        text=f"{current_level_xp} / 100 XP TO NEXT LEVEL",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_rectangle(
        440,
        287,
        760,
        300,
        fill="#080B18",
        outline=""
    ))

    add_item(canvas.create_rectangle(
        440,
        287,
        440 + progress_width,
        300,
        fill=PURPLE,
        outline=""
    ))

    add_item(canvas.create_text(
        780,
        293,
        text=f"{xp_to_next} XP",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    # ========================================================
    # GAME STATISTICS TITLE
    # ========================================================

    add_item(canvas.create_text(
        115,
        340,
        text="GAME STATISTICS",
        fill=ORANGE,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    # ========================================================
    # GAMES PLAYED
    # ========================================================

    add_item(canvas.create_rectangle(
        115,
        365,
        325,
        435,
        fill="#0C1022",
        outline="#252B4A",
        width=1
    ))

    add_item(canvas.create_text(
        220,
        385,
        text="GAMES PLAYED",
        fill=GREY,
        font=("Segoe UI", 8, "bold")
    ))

    add_item(canvas.create_text(
        220,
        413,
        text=str(games_played),
        fill=CYAN,
        font=("Segoe UI", 17, "bold")
    ))

    # ========================================================
    # GAMES WON
    # ========================================================

    add_item(canvas.create_rectangle(
        345,
        365,
        555,
        435,
        fill="#0C1022",
        outline="#252B4A",
        width=1
    ))

    add_item(canvas.create_text(
        450,
        385,
        text="GAMES WON",
        fill=GREY,
        font=("Segoe UI", 8, "bold")
    ))

    add_item(canvas.create_text(
        450,
        413,
        text=str(games_won),
        fill=GREEN,
        font=("Segoe UI", 17, "bold")
    ))

    # ========================================================
    # GAMES LOST
    # ========================================================

    add_item(canvas.create_rectangle(
        575,
        365,
        785,
        435,
        fill="#0C1022",
        outline="#252B4A",
        width=1
    ))

    add_item(canvas.create_text(
        680,
        385,
        text="GAMES LOST",
        fill=GREY,
        font=("Segoe UI", 8, "bold")
    ))

    add_item(canvas.create_text(
        680,
        413,
        text=str(games_lost),
        fill=PINK,
        font=("Segoe UI", 17, "bold")
    ))

    # ========================================================
    # XP EARNED
    # ========================================================

    add_item(canvas.create_rectangle(
        805,
        365,
        985,
        435,
        fill="#0C1022",
        outline="#252B4A",
        width=1
    ))

    add_item(canvas.create_text(
        895,
        385,
        text="XP EARNED",
        fill=GREY,
        font=("Segoe UI", 8, "bold")
    ))

    add_item(canvas.create_text(
        895,
        413,
        text=str(xp_earned),
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 17, "bold")
    ))

    # ========================================================
    # MOST PLAYED GAME
    # ========================================================

    add_item(canvas.create_text(
        115,
        465,
        text="RECENTLY PLAYED",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    if most_played == "None":

        most_played_text = "NO GAMES YET"

    else:

        most_played_text = most_played.upper()

    add_item(canvas.create_text(
        115,
        492,
        text=most_played_text,
        fill=WHITE,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    # ========================================================
    # LEADERBOARD RANK
    # ========================================================

    add_item(canvas.create_text(
        430,
        465,
        text="LEADERBOARD RANK",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    if player_rank > 0:

        rank_text = "#" + str(player_rank)

    else:

        rank_text = "--"

    add_item(canvas.create_text(
        430,
        492,
        text=rank_text,
        fill=PINK,
        font=("Segoe UI", 14, "bold"),
        anchor="w"
    ))

    # ========================================================
    # BADGES
    # ========================================================

    add_item(canvas.create_text(
        650,
        465,
        text="BADGES UNLOCKED",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        650,
        492,
        text=f"{achievement_count} / 5",
        fill=ORANGE,
        font=("Segoe UI", 14, "bold"),
        anchor="w"
    ))

    # ========================================================
    # BACK BUTTON
    # ========================================================

    create_button(
        470,
        555,
        160,
        40,
        "← BACK",
        show_home,
        CARD_BORDER
    )

    # ============================================================
# LOGIN / SIGN UP
# ============================================================

def show_login():

    clear_page()
    draw_background()

    add_item(canvas.create_text(
        550,
        125,
        text="PYTHON ARCADE",
        fill=CYAN,
        font=("Segoe UI", 30, "bold")
    ))

    add_item(canvas.create_text(
        550,
        165,
        text="LOG IN TO CONTINUE",
        fill=GREY,
        font=("Segoe UI", 10, "bold")
    ))

    # ========================================================
    # LOGIN CARD
    # ========================================================

    add_item(canvas.create_rectangle(
        350,
        205,
        750,
        555,
        fill=CARD,
        outline=CARD_BORDER,
        width=2
    ))

    add_item(canvas.create_text(
        550,
        245,
        text="WELCOME BACK",
        fill=WHITE,
        font=("Segoe UI", 18, "bold")
    ))

    add_item(canvas.create_text(
        550,
        275,
        text="Enter your arcade account details.",
        fill=GREY,
        font=("Segoe UI", 9)
    ))

    # ========================================================
    # USERNAME
    # ========================================================

    add_item(canvas.create_text(
        420,
        320,
        text="USERNAME",
        fill=LIGHT,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    username_entry = tk.Entry(
        window,
        bg="#0C1022",
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        font=("Segoe UI", 11)
    )

    username_entry.place(
        x=420,
        y=340,
        width=260,
        height=38
    )

    add_widget(username_entry)

    # ========================================================
    # PASSWORD
    # ========================================================

    add_item(canvas.create_text(
        420,
        395,
        text="PASSWORD",
        fill=LIGHT,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    password_entry = tk.Entry(
        window,
        bg="#0C1022",
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        show="*",
        font=("Segoe UI", 11)
    )

    password_entry.place(
        x=420,
        y=415,
        width=260,
        height=38
    )

    add_widget(password_entry)

    feedback = add_item(canvas.create_text(
        550,
        475,
        text="",
        fill=PINK,
        font=("Segoe UI", 9, "bold")
    ))

    def login():

        global current_username
        global player_xp

        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":

            canvas.itemconfig(
                feedback,
                text="Please enter username and password.",
                fill=PINK
            )

            return

        for account in accounts:

            if account[0] == username:

                if account[1] == password:

                    current_username = username
                    player_xp = account[2]

                    show_home()

                    return

                else:

                    canvas.itemconfig(
                        feedback,
                        text="Incorrect password.",
                        fill=PINK
                    )

                    return

        canvas.itemconfig(
            feedback,
            text="Account not found. Please sign up.",
            fill=PINK
        )

    create_button(
        420,
        505,
        120,
        40,
        "LOG IN",
        login,
        PURPLE
    )

    create_button(
        560,
        505,
        120,
        40,
        "SIGN UP",
        show_signup,
        CARD_BORDER
    )

    # ============================================================
# SIGN UP
# ============================================================

def show_signup():

    clear_page()
    draw_background()

    add_item(canvas.create_text(
        550,
        115,
        text="CREATE ACCOUNT",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 28, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text="Create your own Python Arcade profile.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    # ========================================================
    # SIGN UP CARD
    # ========================================================

    add_item(canvas.create_rectangle(
        350,
        180,
        750,
        590,
        fill=CARD,
        outline=CARD_BORDER,
        width=2
    ))

    # ========================================================
    # USERNAME
    # ========================================================

    add_item(canvas.create_text(
        420,
        220,
        text="CHOOSE USERNAME",
        fill=LIGHT,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    username_entry = tk.Entry(
        window,
        bg="#0C1022",
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        font=("Segoe UI", 11)
    )

    username_entry.place(
        x=420,
        y=240,
        width=260,
        height=38
    )

    add_widget(username_entry)

    # ========================================================
    # PASSWORD
    # ========================================================

    add_item(canvas.create_text(
        420,
        295,
        text="PASSWORD",
        fill=LIGHT,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    password_entry = tk.Entry(
        window,
        bg="#0C1022",
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        show="*",
        font=("Segoe UI", 11)
    )

    password_entry.place(
        x=420,
        y=315,
        width=260,
        height=38
    )

    add_widget(password_entry)

    # ========================================================
    # CONFIRM PASSWORD
    # ========================================================

    add_item(canvas.create_text(
        420,
        370,
        text="CONFIRM PASSWORD",
        fill=LIGHT,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    confirm_entry = tk.Entry(
        window,
        bg="#0C1022",
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        show="*",
        font=("Segoe UI", 11)
    )

    confirm_entry.place(
        x=420,
        y=390,
        width=260,
        height=38
    )

    add_widget(confirm_entry)

    feedback = add_item(canvas.create_text(
        550,
        455,
        text="",
        fill=PINK,
        font=("Segoe UI", 9, "bold")
    ))

    def create_account():

        global accounts
        global current_username
        global player_xp

        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_entry.get()

        if username == "" or password == "":

            canvas.itemconfig(
                feedback,
                text="Please fill in all fields.",
                fill=PINK
            )

            return

        if password != confirm_password:

            canvas.itemconfig(
                feedback,
                text="Passwords do not match.",
                fill=PINK
            )

            return

        for account in accounts:

            if account[0] == username:

                canvas.itemconfig(
                    feedback,
                    text="Username already exists.",
                    fill=PINK
                )

                return

        accounts.append(
            [username, password, 0]
        )

        save_accounts(accounts)

        current_username = username
        player_xp = 0

        create_player_statistics(username)

        show_home()

    create_button(
        420,
        485,
        120,
        40,
        "CREATE",
        create_account,
        PURPLE
    )

    create_button(
        560,
        485,
        120,
        40,
        "← LOGIN",
        show_login,
        CARD_BORDER
    )

# ============================================================
# BUTTON HELPER
# ============================================================

def create_button(
    x,
    y,
    width,
    height,
    text,
    command,
    bg_color=PURPLE,
    fg=WHITE,
    font_size=11
):

    button = tk.Button(
        window,
        text=text,
        command=command,
        bg=bg_color,
        fg=fg,
        activebackground=bg_color,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        highlightthickness=0,
        cursor="hand2",
        font=("Segoe UI", font_size, "bold")
    )

    button.place(
        x=x,
        y=y,
        width=width,
        height=height
    )

    return add_widget(button)

# ============================================================
# XP
# ============================================================

def add_xp(amount):

    global player_xp

    player_xp += amount

# ============================================================
# HOME
# ============================================================

def show_home():

    clear_page()
    draw_background()
    create_navbar()

    add_item(canvas.create_text(
        70,
        145,
        text="✦ WELCOME TO THE ARCADE ✦",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        70,
        190,
        text="LEVEL UP YOUR",
        fill=WHITE,
        font=("Segoe UI", 34, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        70,
        235,
        text="PYTHON EXPERIENCE.",
        fill=CYAN,
        font=("Segoe UI", 34, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        72,
        290,
        text="Learn Python. Play games. Earn XP.",
        fill=GREY,
        font=("Segoe UI", 14),
        anchor="w"
    ))

    create_button(
        70,
        330,
        150,
        48,
        "PLAY NOW  →",
        show_games,
        PURPLE
    )

    stats = [
        ("8", "GAMES"),
        ("∞", "CHALLENGES"),
        (str(player_xp), "XP"),
        ("01", "LEVEL")
    ]

    x_positions = [
        80,
        220,
        390,
        520
    ]

    for i, (value, label) in enumerate(stats):

        add_item(canvas.create_text(
            x_positions[i],
            470,
            text=value,
            fill=WHITE,
            font=("Segoe UI", 25, "bold")
        ))

        add_item(canvas.create_text(
            x_positions[i],
            500,
            text=label,
            fill=GREY,
            font=("Segoe UI", 9, "bold")
        ))

    add_item(canvas.create_rectangle(
        700,
        145,
        1030,
        250,
        fill=CARD,
        outline=CARD_BORDER,
        width=1
    ))

    add_item(canvas.create_text(
        725,
        175,
        text="◉",
        fill=PURPLE,
        font=("Segoe UI", 24, "bold")
    ))

    add_item(canvas.create_text(
        770,
        170,
        text="NUMBER GUESS",
        fill=WHITE,
        font=("Segoe UI", 13, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        770,
        200,
        text="Can you find the hidden number?",
        fill=GREY,
        font=("Segoe UI", 9),
        anchor="w"
    ))

    add_item(canvas.create_rectangle(
        700,
        270,
        1030,
        375,
        fill=CARD,
        outline=CARD_BORDER,
        width=1
    ))

    add_item(canvas.create_text(
        725,
        300,
        text="?",
        fill=CYAN,
        font=("Segoe UI", 24, "bold")
    ))

    add_item(canvas.create_text(
        770,
        295,
        text="PYTHON QUIZ",
        fill=WHITE,
        font=("Segoe UI", 13, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        770,
        325,
        text="Test your Python knowledge.",
        fill=GREY,
        font=("Segoe UI", 9),
        anchor="w"
    ))

# ============================================================
# GAMES
# ============================================================

games = [
    ("◉", "NUMBER GUESS", "Guess the hidden number", "LOGIC", PURPLE),
    ("✊", "ROCK PAPER SCISSORS", "Battle against the computer", "ARCADE", PINK),
    ("?", "PYTHON QUIZ", "Test your Python knowledge", "KNOWLEDGE", CYAN),
    ("+", "MATH CHALLENGE", "Solve problems and earn points", "CHALLENGE", BLUE),
    ("A", "WORD GUESS", "Find the hidden word", "WORDS", GREEN),
    ("◆", "MEMORY CHALLENGE", "Test your memory", "MEMORY", ORANGE),
    ("#", "NUMBER SEQUENCE", "Find what comes next", "LOGIC", PURPLE_LIGHT),
    ("↑", "HIGHER OR LOWER", "Predict the next number", "LUCK", PINK)
]


def create_game_card(
    x,
    y,
    icon,
    title,
    description,
    tag,
    color
):

    width = 400
    height = 90

    add_item(canvas.create_rectangle(
        x - width / 2,
        y - height / 2,
        x + width / 2,
        y + height / 2,
        fill=CARD,
        outline=CARD_BORDER,
        width=1
    ))

    add_item(canvas.create_rectangle(
        x - width / 2,
        y - height / 2,
        x - width / 2 + 5,
        y + height / 2,
        fill=color,
        outline=""
    ))

    add_item(canvas.create_text(
        x - 165,
        y,
        text=icon,
        fill=color,
        font=("Segoe UI", 22, "bold")
    ))

    add_item(canvas.create_text(
        x - 125,
        y - 15,
        text=title,
        fill=WHITE,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        x - 125,
        y + 13,
        text=description,
        fill=GREY,
        font=("Segoe UI", 8),
        anchor="w"
    ))

    add_item(canvas.create_text(
        x + 115,
        y - 15,
        text=tag,
        fill=color,
        font=("Segoe UI", 7, "bold")
    ))

    button = tk.Button(
        window,
        text="PLAY  →",
        command=lambda n=title: start_selected_game(n),
        bg=color,
        fg=WHITE,
        activebackground=color,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        highlightthickness=0,
        cursor="hand2",
        font=("Segoe UI", 8, "bold")
    )

    button.place(
        x=x + 105,
        y=y + 5,
        width=70,
        height=26
    )

    add_widget(button)


def show_games():

    clear_page()
    draw_background()
    create_navbar()

    add_item(canvas.create_text(
        70,
        125,
        text="GAME LIBRARY",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        70,
        155,
        text="Choose your challenge.",
        fill=WHITE,
        font=("Segoe UI", 25, "bold"),
        anchor="w"
    ))

    positions = [
        (315, 225),
        (785, 225),
        (315, 335),
        (785, 335),
        (315, 445),
        (785, 445),
        (315, 555),
        (785, 555)
    ]

    for game, position in zip(
        games,
        positions
    ):

        create_game_card(
            position[0],
            position[1],
            game[0],
            game[1],
            game[2],
            game[3],
            game[4]
        )


def start_selected_game(game_name):

    if game_name == "NUMBER GUESS":
        show_number_guess()

    elif game_name == "ROCK PAPER SCISSORS":
        show_rock_paper_scissors()

    elif game_name == "PYTHON QUIZ":
        show_python_quiz()

    elif game_name == "MATH CHALLENGE":
        show_math_challenge()

    elif game_name == "WORD GUESS":
        show_word_guess()

    elif game_name == "MEMORY CHALLENGE":
        show_memory_challenge()

    elif game_name == "NUMBER SEQUENCE":
        show_number_sequence()

    elif game_name == "HIGHER OR LOWER":
        show_higher_lower()

# ============================================================
# SCORES
# ============================================================

def show_scores():

    clear_page()
    draw_background()
    create_navbar()

    add_item(canvas.create_text(
        70,
        125,
        text="SCORE CENTER",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        70,
        160,
        text="Your Python Arcade progress.",
        fill=WHITE,
        font=("Segoe UI", 25, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_rectangle(
        70,
        220,
        500,
        370,
        fill=CARD,
        outline=CARD_BORDER,
        width=1
    ))

    add_item(canvas.create_text(
        105,
        255,
        text="TOTAL XP",
        fill=GREY,
        font=("Segoe UI", 10, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        105,
        305,
        text=str(player_xp),
        fill=CYAN,
        font=("Segoe UI", 40, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        105,
        345,
        text="Keep playing to level up!",
        fill=GREY,
        font=("Segoe UI", 10),
        anchor="w"
    ))

    add_item(canvas.create_rectangle(
        550,
        220,
        1030,
        370,
        fill=CARD,
        outline=CARD_BORDER,
        width=1
    ))

    add_item(canvas.create_text(
        585,
        255,
        text="CURRENT LEVEL",
        fill=GREY,
        font=("Segoe UI", 10, "bold"),
        anchor="w"
    ))

    level = (player_xp // 100) + 1

    add_item(canvas.create_text(
        585,
        305,
        text=f"LEVEL {level:02d}",
        fill=PURPLE,
        font=("Segoe UI", 30, "bold"),
        anchor="w"
    ))

    remaining = 100 - (player_xp % 100)

    add_item(canvas.create_text(
        585,
        345,
        text=f"{remaining} XP until next level",
        fill=GREY,
        font=("Segoe UI", 10),
        anchor="w"
    ))

    # ========================================================
    # LEADERBOARD
    # ========================================================

    add_item(canvas.create_text(
        70,
        430,
        text="🏆 ARCADE LEADERBOARD",
        fill=ORANGE,
        font=("Segoe UI", 12, "bold"),
        anchor="w"
    ))

    # Sort players by XP

    leaderboard = []

    for account in accounts:

        username = account[0]
        xp = account[2]

        leaderboard.append(
            [username, xp]
        )

    # Highest XP first

    for i in range(len(leaderboard)):

        for j in range(i + 1, len(leaderboard)):

            if leaderboard[j][1] > leaderboard[i][1]:

                temporary = leaderboard[i]

                leaderboard[i] = leaderboard[j]

                leaderboard[j] = temporary

    # ========================================================
    # PLAYERS TO DISPLAY
    # TOP 3 + CURRENT PLAYER
    # ========================================================

    players_to_show = []

    # Add top 3 players

    for i in range(len(leaderboard)):

        if i < 3:

            players_to_show.append(
                leaderboard[i]
            )

    # Make sure current player is visible

    for account in leaderboard:

        if account[0] == current_username:

            already_added = False

            for player in players_to_show:

                if player[0] == current_username:

                    already_added = True

            if already_added == False:

                players_to_show.append(account)

    # ========================================================
    # LEADERBOARD CARD
    # ========================================================

    add_item(canvas.create_rectangle(
        70,
        455,
        1030,
        585,
        fill=CARD,
        outline=CARD_BORDER,
        width=1
    ))

    # Headers

    add_item(canvas.create_text(
        100,
        475,
        text="RANK",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        230,
        475,
        text="PLAYER",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="w"
    ))

    add_item(canvas.create_text(
        980,
        475,
        text="XP",
        fill=GREY,
        font=("Segoe UI", 8, "bold"),
        anchor="e"
    ))

    # ========================================================
    # PLAYER ROWS
    # ========================================================

    if len(leaderboard) == 0:

        add_item(canvas.create_text(
            550,
            530,
            text="NO PLAYERS YET",
            fill=GREY,
            font=("Segoe UI", 10, "bold")
        ))

    else:

        for i in range(len(players_to_show)):

            username = players_to_show[i][0]
            xp = players_to_show[i][1]

            # Find actual rank

            rank = 1

            for account in leaderboard:

                if account[1] > xp:

                    rank += 1

                elif account[0] == username:

                    break

            y = 510 + (i * 25)

            # Highlight current player

            if username == current_username:

                player_color = WHITE
                xp_color = CYAN

            else:

                player_color = LIGHT
                xp_color = PURPLE_LIGHT

            # Rank symbol

            if rank == 1:

                rank_text = "🥇"

            elif rank == 2:

                rank_text = "🥈"

            elif rank == 3:

                rank_text = "🥉"

            else:

                rank_text = "#" + str(rank)

            add_item(canvas.create_text(
                100,
                y,
                text=rank_text,
                fill=ORANGE if rank <= 3 else GREY,
                font=("Segoe UI", 9, "bold"),
                anchor="w"
            ))

            add_item(canvas.create_text(
                230,
                y,
                text=username.upper(),
                fill=player_color,
                font=("Segoe UI", 9, "bold"),
                anchor="w"
            ))

            add_item(canvas.create_text(
                980,
                y,
                text=str(xp) + " XP",
                fill=xp_color,
                font=("Segoe UI", 9, "bold"),
                anchor="e"
            ))

    # Total players

    add_item(canvas.create_text(
        550,
        595,
        text=f"TOTAL PLAYERS  •  {len(leaderboard)}",
        fill=GREY,
        font=("Segoe UI", 8, "bold")
    ))

    # Back button

    create_button(
        450,
        625,
        200,
        42,
        "← BACK TO HOME",
        show_home,
        PURPLE
    )

# ============================================================
# NUMBER GUESS
# ============================================================

number_answer = 0
number_attempts = 0
number_won = False


def show_number_guess():

    global number_answer
    global number_attempts
    global number_won

    clear_page()
    draw_background()
    create_navbar()

    number_answer = random.randint(1, 100)
    number_attempts = 0
    number_won = False

    add_item(canvas.create_text(
        550,
        125,
        text="NUMBER GUESS",
        fill=PURPLE,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        165,
        text="Guess the hidden number between 1 and 100.",
        fill=GREY,
        font=("Segoe UI", 11)
    ))

    add_item(canvas.create_text(
        550,
        215,
        text="YOUR GUESS",
        fill=LIGHT,
        font=("Segoe UI", 9, "bold")
    ))

    guess_entry = tk.Entry(
        window,
        bg=CARD,
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        justify="center",
        font=("Segoe UI", 16, "bold")
    )

    guess_entry.place(
        x=450,
        y=235,
        width=200,
        height=45
    )

    add_widget(guess_entry)

    feedback = add_item(canvas.create_text(
        550,
        355,
        text="ENTER A NUMBER",
        fill=GREY,
        font=("Segoe UI", 13, "bold")
    ))

    attempts_text = add_item(canvas.create_text(
        550,
        385,
        text="ATTEMPTS: 0",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 9, "bold")
    ))

    def check_guess():

        global number_attempts
        global number_won

        if number_won:
            return

        try:

            guess = int(guess_entry.get())

        except ValueError:

            canvas.itemconfig(
                feedback,
                text="⚠ ENTER A VALID NUMBER",
                fill=PINK,
                font=("Segoe UI", 13, "bold")
            )

            return

        if guess < 1 or guess > 100:

            canvas.itemconfig(
                feedback,
                text="⚠ ENTER A NUMBER FROM 1 TO 100",
                fill=PINK,
                font=("Segoe UI", 11, "bold")
            )

            return

        number_attempts += 1

        canvas.itemconfig(
            attempts_text,
            text=f"ATTEMPTS: {number_attempts}"
        )

        if guess < number_answer:

            canvas.itemconfig(
                feedback,
                text="🔽 TOO LOW!",
                fill=CYAN,
                font=("Segoe UI", 17, "bold")
            )

        elif guess > number_answer:

            canvas.itemconfig(
                feedback,
                text="🔼 TOO HIGH!",
                fill=ORANGE,
                font=("Segoe UI", 17, "bold")
            )

        else:

            number_won = True

            # Add XP
            add_xp(50)

            # Record completed game
            record_game(
                "Number Guess",
                True,
                50
            )

            canvas.itemconfig(
                feedback,
                text=f"🎉 CORRECT! THE NUMBER WAS {number_answer}  +50 XP",
                fill=GREEN,
                font=("Segoe UI", 12, "bold")
            )

            new_button.config(
                state="normal"
            )

    # CHECK BUTTON
    create_button(
        470,
        290,
        160,
        42,
        "CHECK",
        check_guess,
        PURPLE
    )

    # NEW GAME
    new_button = create_button(
        405,
        425,
        130,
        40,
        "NEW GAME",
        show_number_guess,
        CARD_BORDER
    )

    new_button.config(
        state="disabled"
    )

    # BACK
    create_button(
        565,
        425,
        130,
        40,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# ROCK PAPER SCISSORS
# ============================================================

rps_player_score = 0
rps_computer_score = 0


def show_rock_paper_scissors():

    global rps_player_score
    global rps_computer_score

    clear_page()
    draw_background()
    create_navbar()

    rps_player_score = 0
    rps_computer_score = 0

    add_item(canvas.create_text(
        550,
        120,
        text="ROCK PAPER SCISSORS",
        fill=PINK,
        font=("Segoe UI", 25, "bold")
    ))

    add_item(canvas.create_text(
        550,
        155,
        text="Choose your move.",
        fill=GREY,
        font=("Segoe UI", 11)
    ))

    score_text = add_item(canvas.create_text(
        550,
        205,
        text="YOU  0     —     0  COMPUTER",
        fill=WHITE,
        font=("Segoe UI", 15, "bold")
    ))

    result_text = add_item(canvas.create_text(
        550,
        290,
        text="MAKE YOUR MOVE",
        fill=LIGHT,
        font=("Segoe UI", 15, "bold")
    ))

    moves = [
        "ROCK",
        "PAPER",
        "SCISSORS"
    ]

    def play(move):

        global rps_player_score
        global rps_computer_score

        computer = random.choice(moves)

        if move == computer:

            result = f"DRAW! Both chose {move}."

        elif (
            (move == "ROCK" and computer == "SCISSORS")
            or
            (move == "PAPER" and computer == "ROCK")
            or
            (move == "SCISSORS" and computer == "PAPER")
        ):

            rps_player_score += 1

            add_xp(10)

            record_game(
                "Rock Paper Scissors",
                True,
                10
            )

            result = "YOU WIN! +10 XP"

        else:

            rps_computer_score += 1

            record_game(
                "Rock Paper Scissors",
                False,
                0
            )

            result = "COMPUTER WINS!"

        canvas.itemconfig(
            score_text,
            text=f"YOU  {rps_player_score}     —     {rps_computer_score}  COMPUTER"
        )

        canvas.itemconfig(
            result_text,
            text=f"{result}\nYou: {move}   Computer: {computer}",
            fill=GREEN if "WIN" in result
            else PINK if "COMPUTER" in result
            else CYAN
        )

    # ========================================================
    # MOVE BUTTONS
    # ========================================================

    create_button(
        350,
        365,
        120,
        48,
        "✊ ROCK",
        lambda: play("ROCK"),
        PURPLE
    )

    create_button(
        490,
        365,
        120,
        48,
        "✋ PAPER",
        lambda: play("PAPER"),
        CYAN
    )

    create_button(
        630,
        365,
        120,
        48,
        "✌ SCISSORS",
        lambda: play("SCISSORS"),
        PINK
    )

    # ========================================================
    # NEW GAME
    # ========================================================

    create_button(
        420,
        470,
        120,
        40,
        "NEW GAME",
        show_rock_paper_scissors,
        CARD_BORDER
    )

    # ========================================================
    # BACK
    # ========================================================

    create_button(
        560,
        470,
        120,
        40,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# PYTHON QUIZ
# ============================================================

quiz_questions = [
    (
        "Which keyword is used to create a function in Python?",
        ["function", "def", "fun", "create"],
        "def"
    ),
    (
        "Which data type is used for whole numbers?",
        ["float", "string", "int", "bool"],
        "int"
    ),
    (
        "Which symbol is used for a comment in Python?",
        ["//", "#", "/*", "--"],
        "#"
    ),
    (
        "Which loop is commonly used when you know how many times to repeat?",
        ["if", "while", "for", "switch"],
        "for"
    ),
    (
        "Which collection stores data as key-value pairs?",
        ["List", "Tuple", "Dictionary", "Set"],
        "Dictionary"
    ),
    (
        "What does len() return?",
        ["The data type", "The length", "The first item", "The last item"],
        "The length"
    ),
    (
        "Which of these is a Boolean value?",
        ["10", "'Hello'", "True", "3.14"],
        "True"
    ),
    (
        "Which brackets are used to create a list?",
        ["()", "{}", "[]", "<>"],
        "[]"
    ),
    (
        "Which keyword is used to stop a loop immediately?",
        ["stop", "exit", "break", "end"],
        "break"
    ),
    (
        "What is the result of int('10')?",
        ["'10'", "10", "10.0", "True"],
        "10"
    )
]

quiz_question_number = 0
quiz_score = 0
quiz_answered = False


def show_python_quiz():

    global quiz_question_number
    global quiz_score
    global quiz_answered

    clear_page()
    draw_background()
    create_navbar()

    quiz_question_number = 0
    quiz_score = 0
    quiz_answered = False

    display_quiz_question()


def display_quiz_question():

    global quiz_answered

    clear_page()
    draw_background()
    create_navbar()

    quiz_answered = False

    if quiz_question_number >= len(
        quiz_questions
    ):

        show_quiz_result()
        return

    question, options, correct = quiz_questions[
        quiz_question_number
    ]

    add_item(canvas.create_text(
        550,
        115,
        text="PYTHON QUIZ",
        fill=CYAN,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text=f"QUESTION {quiz_question_number + 1} / {len(quiz_questions)}",
        fill=GREY,
        font=("Segoe UI", 9, "bold")
    ))

    add_item(canvas.create_text(
        550,
        210,
        text=question,
        fill=WHITE,
        font=("Segoe UI", 14, "bold"),
        width=750
    ))

    feedback = add_item(canvas.create_text(
        550,
        480,
        text="Choose an answer.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    option_buttons = []

    def answer(choice, button):

        global quiz_answered
        global quiz_score

        if quiz_answered:
            return

        quiz_answered = True

        if choice == correct:

            quiz_score += 1
            add_xp(20)

            button.config(
                bg=GREEN,
                activebackground=GREEN
            )

            canvas.itemconfig(
                feedback,
                text="✓ CORRECT! +20 XP",
                fill=GREEN
            )

        else:

            button.config(
                bg=PINK,
                activebackground=PINK
            )

            canvas.itemconfig(
                feedback,
                text=f"✗ WRONG! Correct answer: {correct}",
                fill=PINK
            )

            for option_button, option_text in option_buttons:

                if option_text == correct:

                    option_button.config(
                        bg=GREEN,
                        activebackground=GREEN
                    )

        next_button.config(
            state="normal"
        )

    y_positions = [
        270,
        325,
        380,
        435
    ]

    for option, y in zip(
        options,
        y_positions
    ):

        button = tk.Button(
            window,
            text=option,
            bg=CARD,
            fg=WHITE,
            activebackground=PURPLE,
             activeforeground=WHITE,
            relief="flat",
            bd=1,
            highlightthickness=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold")
        )

        button.config(
            command=lambda choice=option, b=button:
            answer(choice, b)
        )

        button.place(
            x=350,
            y=y,
            width=400,
            height=40
        )

        add_widget(button)

        option_buttons.append(
            (button, option)
        )

    def next_question():

        global quiz_question_number

        quiz_question_number += 1

        if quiz_question_number >= len(
            quiz_questions
        ):

            show_quiz_result()

        else:

            display_quiz_question()

    next_button = create_button(
        450,
        525,
        200,
        42,
        "NEXT QUESTION →",
        next_question,
        PURPLE
    )

    next_button.config(
        state="disabled"
    )

    create_button(
        450,
        580,
        200,
        38,
        "← BACK TO GAMES",
        show_games,
        CARD_BORDER,
        WHITE,
        9
    )


def show_quiz_result():

    clear_page()
    draw_background()
    create_navbar()

    # ========================================================
    # CALCULATE QUIZ XP
    # ========================================================

    quiz_xp = quiz_score * 20

    # ========================================================
    # RECORD QUIZ IN PLAYER STATISTICS
    # ========================================================

    if quiz_score > 0:

        record_game(
            "Python Quiz",
            True,
            quiz_xp
        )

    else:

        record_game(
            "Python Quiz",
            False,
            0
        )

    # ========================================================
    # RESULT SCREEN
    # ========================================================

    add_item(canvas.create_text(
        550,
        190,
        text="QUIZ COMPLETE!",
        fill=CYAN,
        font=("Segoe UI", 30, "bold")
    ))

    add_item(canvas.create_text(
        550,
        245,
        text=f"{quiz_score} / {len(quiz_questions)}",
        fill=WHITE,
        font=("Segoe UI", 35, "bold")
    ))

    add_item(canvas.create_text(
        550,
        295,
        text=f"Great work!  +{quiz_xp} XP",
        fill=GREY,
        font=("Segoe UI", 12)
    ))

    create_button(
        400,
        380,
        130,
        42,
        "PLAY AGAIN",
        show_python_quiz,
        CYAN
    )

    create_button(
        570,
        380,
        130,
        42,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# MATH CHALLENGE
# ============================================================

math_question_number = 0
math_score = 0
math_answered = False
math_correct_answer = 0


def show_math_challenge():

    global math_question_number
    global math_score

    clear_page()
    draw_background()
    create_navbar()

    math_question_number = 0
    math_score = 0

    display_math_question()


def generate_math_question():

    operation = random.choice([
        "+",
        "-",
        "*",
        "/"
    ])

    if operation == "+":

        a = random.randint(5, 50)
        b = random.randint(5, 50)
        answer = a + b

    elif operation == "-":

        a = random.randint(20, 80)
        b = random.randint(5, a)
        answer = a - b

    elif operation == "*":

        a = random.randint(2, 12)
        b = random.randint(2, 12)
        answer = a * b

    else:

        b = random.randint(2, 12)
        answer = random.randint(2, 12)
        a = b * answer

    return f"{a} {operation} {b}", answer


def display_math_question():

    global math_answered
    global math_correct_answer

    clear_page()
    draw_background()
    create_navbar()

    math_answered = False

    question, answer = generate_math_question()

    math_correct_answer = answer

    add_item(canvas.create_text(
        550,
        115,
        text="MATH CHALLENGE",
        fill=BLUE,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text=f"QUESTION {math_question_number + 1} / 10",
        fill=GREY,
        font=("Segoe UI", 9, "bold")
    ))

    progress_width = 400

    progress = (
        math_question_number / 10
    ) * progress_width

    add_item(canvas.create_rectangle(
        350,
        180,
        750,
        188,
        fill="#1C2340",
        outline=""
    ))

    add_item(canvas.create_rectangle(
        350,
        180,
        350 + progress,
        188,
        fill=BLUE,
        outline=""
    ))

    add_item(canvas.create_text(
        550,
        235,
        text=question,
        fill=WHITE,
        font=("Segoe UI", 30, "bold")
    ))

    add_item(canvas.create_text(
        550,
        275,
        text=f"SCORE: {math_score}",
        fill=LIGHT,
        font=("Segoe UI", 10, "bold")
    ))

    feedback = add_item(canvas.create_text(
        550,
        500,
        text="Choose an answer.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    choices = [
        math_correct_answer
    ]

    while len(choices) < 4:

        wrong = math_correct_answer + random.randint(
            -10,
            10
        )

        if wrong >= 0 and wrong not in choices:

            choices.append(wrong)

    random.shuffle(choices)

    option_buttons = []

    def answer(choice, button):

        global math_answered
        global math_score

        if math_answered:
            return

        math_answered = True

        if choice == math_correct_answer:

            button.config(
                bg=GREEN,
                activebackground=GREEN
            )

            math_score += 1
            add_xp(20)

            canvas.itemconfig(
                feedback,
                text="✓ CORRECT! +20 XP",
                fill=GREEN
            )

        else:

            button.config(
                bg=PINK,
                activebackground=PINK
            )

            canvas.itemconfig(
                feedback,
                text=f"✗ WRONG! Answer: {math_correct_answer}",
                fill=PINK
            )

            for option_button, option_value in option_buttons:

                if option_value == math_correct_answer:

                    option_button.config(
                        bg=GREEN,
                        activebackground=GREEN
                    )

        next_button.config(
            state="normal"
        )

    y_positions = [
        325,
        380,
        435,
        490
    ]

    for choice, y in zip(
        choices,
        y_positions
    ):

        button = tk.Button(
            window,
            text=str(choice),
            bg=CARD,
            fg=WHITE,
            activebackground=BLUE,
            activeforeground=WHITE,
            relief="flat",
            bd=1,
            highlightthickness=0,
            cursor="hand2",
            font=("Segoe UI", 11, "bold")
        )

        button.config(
            command=lambda value=choice, b=button:
            answer(value, b)
        )

        button.place(
             x=400,
            y=y,
            width=300,
            height=40
        )

        add_widget(button)

        option_buttons.append(
            (button, choice)
        )

    def next_question():

        global math_question_number

        math_question_number += 1

        if math_question_number >= 10:

            show_math_result()

        else:

            display_math_question()

    next_button = create_button(
        450,
        545,
        200,
        40,
        "NEXT →",
        next_question,
        BLUE
    )

    next_button.config(
        state="disabled"
    )

    create_button(
        450,
        595,
        200,
        35,
        "← BACK TO GAMES",
        show_games,
        CARD_BORDER,
        WHITE,
        9
    )


def show_math_result():

    clear_page()
    draw_background()
    create_navbar()

    # ========================================================
    # CALCULATE XP
    # ========================================================

    math_xp = math_score * 20

    # ========================================================
    # RECORD GAME STATISTICS
    # ========================================================

    if math_score > 0:

        record_game(
            "Math Challenge",
            True,
            math_xp
        )

    else:

        record_game(
            "Math Challenge",
            False,
            0
        )

    # ========================================================
    # RESULT SCREEN
    # ========================================================

    add_item(canvas.create_text(
        550,
        190,
        text="CHALLENGE COMPLETE!",
        fill=BLUE,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        245,
        text=f"{math_score} / 10",
        fill=WHITE,
        font=("Segoe UI", 35, "bold")
    ))

    add_item(canvas.create_text(
        550,
        295,
        text=f"Keep practicing!  +{math_xp} XP",
        fill=GREY,
        font=("Segoe UI", 12)
    ))

    create_button(
        400,
        380,
        130,
        42,
        "PLAY AGAIN",
        show_math_challenge,
        BLUE
    )

    create_button(
        570,
        380,
        130,
        42,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# WORD GUESS
# ============================================================

word_bank = [
    ("PYTHON", "A popular programming language"),
    ("VARIABLE", "It stores a value in a program"),
    ("FUNCTION", "A reusable block of code"),
    ("LOOP", "It repeats a block of code"),
    ("COMPUTER", "An electronic machine that processes data"),
    ("KEYBOARD", "You use it to type"),
    ("ALGORITHM", "A step-by-step method for solving a problem"),
    ("PROGRAM", "A set of instructions for a computer"),
    ("DATABASE", "A structured collection of information"),
    ("INTERNET", "A worldwide network of computers"),
    ("SOFTWARE", "Programs that run on a computer"),
    ("HARDWARE", "The physical parts of a computer"),
    ("INTEGER", "A whole number data type"),
    ("STRING", "A sequence of characters"),
    ("BOOLEAN", "A data type with True or False"),
    ("TUPLE", "An ordered Python collection"),
    ("DICTIONARY", "A Python collection of key-value pairs"),
    ("ARCADE", "A place full of games"),
    ("PUZZLE", "A game that tests your thinking"),
    ("TKINTER", "A Python library used to create GUIs")
]

word_answer = ""
word_hint = ""
word_guessed_letters = []
word_wrong_attempts = 0
word_max_attempts = 6
word_game_over = False
word_xp_earned = 0


def show_word_guess():

    global word_answer
    global word_hint
    global word_guessed_letters
    global word_wrong_attempts
    global word_game_over
    global word_xp_earned

    clear_page()
    draw_background()
    create_navbar()

    word_answer, word_hint = random.choice(
        word_bank
    )

    word_guessed_letters = []
    word_wrong_attempts = 0
    word_game_over = False
    word_xp_earned = 0

    add_item(canvas.create_text(
        550,
        110,
        text="WORD GUESS",
        fill=GREEN,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text=f"HINT: {word_hint}",
        fill=GREY,
        font=("Segoe UI", 10),
        width=800
    ))

    word_display = add_item(canvas.create_text(
        550,
        225,
        text="_ " * len(word_answer),
        fill=WHITE,
        font=("Segoe UI", 25, "bold")
    ))

    attempts_text = add_item(canvas.create_text(
        400,
        280,
        text="ATTEMPTS LEFT: 6",
        fill=ORANGE,
        font=("Segoe UI", 10, "bold")
    ))

    xp_text = add_item(canvas.create_text(
        700,
        280,
        text="XP: +0",
        fill=CYAN,
        font=("Segoe UI", 10, "bold")
    ))

    feedback = add_item(canvas.create_text(
        550,
        320,
        text="Choose a letter.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    keyboard_buttons = []

    def update_word_display():

        display = ""

        for letter in word_answer:

            if letter in word_guessed_letters:

                display += letter + " "

            else:

                display += "_ "

        canvas.itemconfig(
            word_display,
            text=display
        )

    def guess_letter(letter):

        global word_wrong_attempts
        global word_game_over
        global word_xp_earned

        if word_game_over:
            return

        if letter in word_guessed_letters:
            return

        word_guessed_letters.append(letter)

        for button, button_letter in keyboard_buttons:

            if button_letter == letter:

                button.config(
                    state="disabled",
                    bg="#242A46"
                )

        if letter in word_answer:

            occurrences = word_answer.count(
                letter
            )

            gained = occurrences * 10

            word_xp_earned += gained

            add_xp(gained)

            canvas.itemconfig(
                feedback,
                text=f"✓ Correct! +{gained} XP",
                fill=GREEN
            )

            canvas.itemconfig(
                xp_text,
                text=f"XP: +{word_xp_earned}"
            )

        else:

            word_wrong_attempts += 1

            canvas.itemconfig(
                feedback,
                text="Not in the word.",
                fill=PINK
            )

        attempts_left = (
            word_max_attempts -
            word_wrong_attempts
        )

        canvas.itemconfig(
            attempts_text,
            text=f"ATTEMPTS LEFT: {attempts_left}"
        )

        update_word_display()

        won = all(
            letter in word_guessed_letters
            for letter in word_answer
        )

        # ====================================================
        # WIN
        # ====================================================

        if won:

            word_game_over = True

            add_xp(50)
            word_xp_earned += 50

            # Record completed game
            record_game(
                "Word Guess",
                True,
                word_xp_earned
            )

            canvas.itemconfig(
                feedback,
                text=f"🎉 YOU WON! +50 BONUS XP   WORD: {word_answer}",
                fill=GREEN
            )

            canvas.itemconfig(
                xp_text,
                text=f"XP: +{word_xp_earned}"
            )

            new_button.config(
                state="normal"
            )

            for button, _ in keyboard_buttons:

                button.config(
                    state="disabled"
                )

        # ====================================================
        # LOSS
        # ====================================================

        elif attempts_left <= 0:

            word_game_over = True

            # Record completed game
            record_game(
                "Word Guess",
                False,
                word_xp_earned
            )

            canvas.itemconfig(
                feedback,
                text=f"GAME OVER! The word was {word_answer}",
                fill=PINK
            )

            new_button.config(
                state="normal"
            )

            for button, _ in keyboard_buttons:

                button.config(
                    state="disabled"
                )

    # ========================================================
    # KEYBOARD
    # ========================================================

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    start_x = 280
    start_y = 370

    button_width = 48
    button_height = 32
    gap = 8

    for index, letter in enumerate(letters):

        row = index // 9
        col = index % 9

        x = start_x + col * (
            button_width + gap
        )

        y = start_y + row * (
            button_height + gap
        )

        button = tk.Button(
            window,
            text=letter,
            command=lambda l=letter:
            guess_letter(l),
            bg=CARD,
            fg=WHITE,
            activebackground=GREEN,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            font=("Segoe UI", 9, "bold")
        )

        button.place(
            x=x,
            y=y,
            width=button_width,
            height=button_height
        )

        add_widget(button)

        keyboard_buttons.append(
            (button, letter)
        )

    # ========================================================
    # NEW GAME
    # ========================================================

    new_button = create_button(
        410,
        555,
        130,
        40,
        "NEW GAME",
        show_word_guess,
        CARD_BORDER
    )

    new_button.config(
        state="disabled"
    )

    # ========================================================
    # BACK
    # ========================================================

    create_button(
        560,
        555,
        130,
        40,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# MEMORY CHALLENGE
# ============================================================

memory_cards = []
memory_buttons = []
memory_first_card = None
memory_second_card = None
memory_locked = False
memory_matches = 0
memory_xp_earned = 0


def show_memory_challenge():

    global memory_cards
    global memory_buttons
    global memory_first_card
    global memory_second_card
    global memory_locked
    global memory_matches
    global memory_xp_earned

    clear_page()
    draw_background()
    create_navbar()

    memory_cards = [
        "★", "◆", "●", "▲",
        "♥", "☀", "♣", "✦"
    ] * 2

    random.shuffle(memory_cards)

    memory_buttons = []
    memory_first_card = None
    memory_second_card = None
    memory_locked = False
    memory_matches = 0
    memory_xp_earned = 0

    add_item(canvas.create_text(
        550,
        105,
        text="MEMORY CHALLENGE",
        fill=ORANGE,
        font=("Segoe UI", 25, "bold")
    ))

    add_item(canvas.create_text(
        550,
        138,
        text="Find all 8 matching pairs.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    pairs_text = add_item(canvas.create_text(
        430,
        175,
        text="PAIRS: 0 / 8",
        fill=LIGHT,
        font=("Segoe UI", 10, "bold")
    ))

    xp_text = add_item(canvas.create_text(
        670,
        175,
        text="XP: +0",
        fill=CYAN,
        font=("Segoe UI", 10, "bold")
    ))

    board = tk.Frame(
        window,
        bg=BG,
        bd=0,
        highlightthickness=0
    )

    board.place(
        x=350,
        y=205,
        width=400,
        height=300
    )

    add_widget(board)

    for row in range(4):

        board.grid_rowconfigure(
            row,
            weight=1
        )

    for col in range(4):

        board.grid_columnconfigure(
            col,
            weight=1
        )

    def hide_memory_cards(
        first,
        second
    ):

        global memory_first_card
        global memory_second_card
        global memory_locked

        try:

            memory_buttons[first].config(
                text="?",
                fg=WHITE,
                bg=CARD
            )

            memory_buttons[second].config(
                text="?",
                fg=WHITE,
                bg=CARD
            )

        except:
            pass

        memory_first_card = None
        memory_second_card = None
        memory_locked = False

    def memory_complete():

        # ====================================================
        # RECORD COMPLETED GAME
        # ====================================================

        record_game(
            "Memory Challenge",
            True,
            memory_xp_earned
        )

        clear_page()
        draw_background()
        create_navbar()

        add_item(canvas.create_text(
            550,
            205,
            text="MEMORY MASTER!",
            fill=ORANGE,
            font=("Segoe UI", 30, "bold")
                    ))

        add_item(canvas.create_text(
            550,
            255,
            text="You found all 8 pairs!",
            fill=WHITE,
            font=("Segoe UI", 15, "bold")
        ))

        add_item(canvas.create_text(
            550,
            295,
            text=f"Keep training your memory.  +{memory_xp_earned} XP",
            fill=GREY,
            font=("Segoe UI", 11)
        ))

        create_button(
            400,
            380,
            130,
            42,
            "NEW GAME",
            show_memory_challenge,
            ORANGE
        )

        create_button(
            570,
            380,
            130,
            42,
            "BACK",
            show_games,
            CARD_BORDER
        )

    def flip_memory_card(index):

        global memory_first_card
        global memory_second_card
        global memory_locked
        global memory_matches
        global memory_xp_earned

        if memory_locked:
            return

        if memory_buttons[index]["state"] == "disabled":
            return

        if memory_first_card == index:
            return

        memory_buttons[index].config(
            text=memory_cards[index],
            fg=ORANGE,
            bg="#1B2140"
        )

        if memory_first_card is None:

            memory_first_card = index
            return

        memory_second_card = index
        memory_locked = True

        first = memory_first_card
        second = memory_second_card

        if memory_cards[first] == memory_cards[second]:

            memory_buttons[first].config(
                state="disabled",
                disabledforeground=GREEN,
                bg="#122A28"
            )

            memory_buttons[second].config(
                state="disabled",
                disabledforeground=GREEN,
                bg="#122A28"
            )

            memory_matches += 1
            memory_xp_earned += 20

            add_xp(20)

            canvas.itemconfig(
                pairs_text,
                text=f"PAIRS: {memory_matches} / 8"
            )

            canvas.itemconfig(
                xp_text,
                text=f"XP: +{memory_xp_earned}"
            )

            memory_first_card = None
            memory_second_card = None
            memory_locked = False

            if memory_matches == 8:

                memory_complete()

        else:

            window.after(
                800,
                lambda:
                hide_memory_cards(
                    first,
                    second
                )
            )

    # ========================================================
    # MEMORY BOARD
    # ========================================================

    for index in range(16):

        row = index // 4
        col = index % 4

        button = tk.Button(
            board,
            text="?",
            command=lambda i=index:
            flip_memory_card(i),
            bg=CARD,
            fg=WHITE,
            activebackground="#252B4A",
            activeforeground=ORANGE,
            relief="flat",
            bd=1,
            highlightthickness=0,
            cursor="hand2",
            font=("Segoe UI", 18, "bold")
        )

        button.grid(
            row=row,
            column=col,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        memory_buttons.append(
            button
        )

    # ========================================================
    # NEW GAME
    # ========================================================

    create_button(
        410,
        535,
        130,
        40,
        "NEW GAME",
        show_memory_challenge,
        CARD_BORDER
    )

    # ========================================================
    # BACK
    # ========================================================

    create_button(
        560,
        535,
        130,
        40,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# NUMBER SEQUENCE
# ============================================================

sequence_question_number = 0
sequence_score = 0
sequence_answered = False
sequence_correct_answer = 0


def generate_sequence():

    sequence_type = random.choice([
        "addition",
        "subtraction",
        "multiplication",
        "squares",
        "alternating"
    ])

    if sequence_type == "addition":

        start = random.randint(2, 20)
        difference = random.randint(2, 12)

        numbers = [
            start + difference * i
            for i in range(5)
        ]

        answer = numbers[-1] + difference

    elif sequence_type == "subtraction":

        start = random.randint(50, 100)
        difference = random.randint(2, 10)

        numbers = [
            start - difference * i
            for i in range(5)
        ]

        answer = numbers[-1] - difference

    elif sequence_type == "multiplication":

        start = random.randint(2, 5)
        multiplier = random.randint(2, 4)

        numbers = [
            start * (multiplier ** i)
            for i in range(5)
        ]

        answer = numbers[-1] * multiplier

    elif sequence_type == "squares":

        start = random.randint(1, 5)

        numbers = [
            (start + i) ** 2
            for i in range(5)
        ]

        answer = (start + 5) ** 2

    else:

        start = random.randint(2, 10)
        first_difference = random.randint(2, 6)
        second_difference = random.randint(7, 12)

        numbers = [start]

        for i in range(1, 5):

            if i % 2 == 1:

                numbers.append(
                    numbers[-1] + first_difference
                )

            else:

                numbers.append(
                    numbers[-1] + second_difference
                )

        answer = (
            numbers[-1] + first_difference
        )

    return numbers, answer


def show_number_sequence():

    global sequence_question_number
    global sequence_score

    clear_page()
    draw_background()
    create_navbar()

    sequence_question_number = 0
    sequence_score = 0

    display_sequence_question()


def display_sequence_question():

    global sequence_answered
    global sequence_correct_answer

    clear_page()
    draw_background()
    create_navbar()

    sequence_answered = False

    numbers, answer = generate_sequence()

    sequence_correct_answer = answer

    add_item(canvas.create_text(
        550,
        115,
        text="NUMBER SEQUENCE",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text=f"ROUND {sequence_question_number + 1} / 10",
        fill=GREY,
        font=("Segoe UI", 9, "bold")
    ))

    add_item(canvas.create_rectangle(
        350,
        180,
        750,
        188,
        fill="#1C2340",
        outline=""
    ))

    progress = (
        sequence_question_number / 10
    ) * 400

    add_item(canvas.create_rectangle(
        350,
        180,
        350 + progress,
        188,
        fill=PURPLE_LIGHT,
        outline=""
    ))

    add_item(canvas.create_text(
        550,
        235,
        text="WHAT COMES NEXT?",
        fill=LIGHT,
        font=("Segoe UI", 11, "bold")
    ))

    sequence_text = "   ".join(
        str(number)
        for number in numbers
    )

    add_item(canvas.create_text(
        550,
        285,
        text=sequence_text + "   ?",
        fill=WHITE,
        font=("Segoe UI", 23, "bold")
    ))

    add_item(canvas.create_text(
        550,
        330,
        text=f"SCORE: {sequence_score}",
        fill=CYAN,
        font=("Segoe UI", 10, "bold")
    ))

    feedback = add_item(canvas.create_text(
        550,
        535,
        text="Choose the number that comes next.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    options = [
        sequence_correct_answer
    ]

    offsets = [
        random.choice([-12, -10, -8, -6]),
        random.choice([4, 6, 8, 10]),
        random.choice([12, 14, 16, 18])
    ]

    for offset in offsets:

        wrong_answer = (
            sequence_correct_answer +
            offset
        )

        if (
            wrong_answer >= 0
            and wrong_answer not in options
        ):

            options.append(
                wrong_answer
            )

    while len(options) < 4:

        wrong_answer = (
            sequence_correct_answer +
            random.randint(-20, 20)
        )

        if (
            wrong_answer >= 0
            and wrong_answer not in options
        ):

            options.append(
                wrong_answer
            )

    random.shuffle(options)

    option_buttons = []

    def choose_answer(
        choice,
        button
    ):

        global sequence_answered
        global sequence_score

        if sequence_answered:
            return

        sequence_answered = True

        if choice == sequence_correct_answer:

            sequence_score += 1

            add_xp(20)

            button.config(
                bg=GREEN,
                activebackground=GREEN
            )

            canvas.itemconfig(
                feedback,
                text="✓ CORRECT! +20 XP",
                fill=GREEN
            )

        else:

            button.config(
                bg=PINK,
                activebackground=PINK
            )

            canvas.itemconfig(
                feedback,
                text=f"✗ WRONG! The answer was {sequence_correct_answer}",
                fill=PINK
            )

            for option_button, option_value in option_buttons:

                if option_value == sequence_correct_answer:

                    option_button.config(
                        bg=GREEN,
                        activebackground=GREEN
                    )

        next_button.config(
            state="normal"
        )

    positions = [
        (360, 375),
        (590, 375),
        (360, 440),
        (590, 440)
    ]

    for choice, (x, y) in zip(
        options,
        positions
    ):

        button = tk.Button(
            window,
            text=str(choice),
            bg=CARD,
            fg=WHITE,
            activebackground=PURPLE,
            activeforeground=WHITE,
            relief="flat",
            bd=1,
            highlightthickness=0,
            cursor="hand2",
            font=("Segoe UI", 12, "bold")
        )

        button.config(
            command=lambda value=choice, b=button:
            choose_answer(value, b)
        )

        button.place(
            x=x,
            y=y,
            width=150,
            height=42
        )

        add_widget(button)

        option_buttons.append(
            (button, choice)
        )

    def next_round():

        global sequence_question_number

        sequence_question_number += 1

        if sequence_question_number >= 10:

            show_sequence_result()

        else:

            display_sequence_question()

    next_button = create_button(
        450,
        585,
        200,
        40,
        "NEXT ROUND →",
        next_round,
        PURPLE_LIGHT,
        NAVY
    )

    next_button.config(
        state="disabled"
    )

    create_button(
        450,
        635,
        200,
        32,
        "← BACK TO GAMES",
        show_games,
        CARD_BORDER,
        WHITE,
        8
    )


def show_sequence_result():

    # ========================================================
    # CALCULATE XP
    # ========================================================

    sequence_xp = sequence_score * 20

    # ========================================================
    # DETERMINE WIN / LOSS
    # ========================================================

    if sequence_score >= 5:

        sequence_won = True

    else:

        sequence_won = False

    # ========================================================
    # RECORD GAME STATISTICS
    # ========================================================

    record_game(
        "Number Sequence",
        sequence_won,
        sequence_xp
    )

    # ========================================================
    # RESULT SCREEN
    # ========================================================

    clear_page()
    draw_background()
    create_navbar()

    add_item(canvas.create_text(
        550,
        190,
        text="SEQUENCE COMPLETE!",
        fill=PURPLE_LIGHT,
        font=("Segoe UI", 28, "bold")
    ))

    add_item(canvas.create_text(
        550,
        245,
        text=f"{sequence_score} / 10",
        fill=WHITE,
        font=("Segoe UI", 38, "bold")
    ))

    if sequence_score >= 8:

        message = (
            "Your pattern recognition is impressive!"
        )

    elif sequence_score >= 5:

        message = (
            "Nice work! Keep sharpening your logic."
        )

    else:

        message = (
            "Keep practicing those patterns!"
        )

    add_item(canvas.create_text(
        550,
        300,
        text=f"{message}  +{sequence_xp} XP",
        fill=GREY,
        font=("Segoe UI", 11)
    ))

    create_button(
        400,
        380,
        130,
        42,
        "PLAY AGAIN",
        show_number_sequence,
        PURPLE_LIGHT,
        NAVY
    )

    create_button(
        570,
        380,
        130,
        42,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# HIGHER OR LOWER — FINAL GAME
# ============================================================

higher_lower_round = 0
higher_lower_score = 0
higher_lower_current = 0
higher_lower_answered = False


def show_higher_lower():

    global higher_lower_round
    global higher_lower_score
    global higher_lower_current
    global higher_lower_answered

    clear_page()
    draw_background()
    create_navbar()

    higher_lower_round = 0
    higher_lower_score = 0
    higher_lower_current = random.randint(
        1,
        50
    )
    higher_lower_answered = False

    display_higher_lower()


def display_higher_lower():

    global higher_lower_answered

    clear_page()
    draw_background()
    create_navbar()

    higher_lower_answered = False

    add_item(canvas.create_text(
        550,
        115,
        text="HIGHER OR LOWER",
        fill=PINK,
        font=("Segoe UI", 27, "bold")
    ))

    add_item(canvas.create_text(
        550,
        150,
        text=f"ROUND {higher_lower_round + 1} / 10",
        fill=GREY,
        font=("Segoe UI", 9, "bold")
    ))

    # --------------------------------------------------------
    # Progress bar
    # --------------------------------------------------------

    add_item(canvas.create_rectangle(
        350,
        180,
        750,
        188,
        fill="#1C2340",
        outline=""
    ))

    progress = (
        higher_lower_round / 10
    ) * 400

    add_item(canvas.create_rectangle(
        350,
        180,
        350 + progress,
        188,
        fill=PINK,
        outline=""
    ))

    add_item(canvas.create_text(
        550,
        225,
        text="CURRENT NUMBER",
        fill=GREY,
        font=("Segoe UI", 9, "bold")
    ))

    # --------------------------------------------------------
    # Current number
    # --------------------------------------------------------

    add_item(canvas.create_text(
        550,
        285,
        text=str(higher_lower_current),
        fill=WHITE,
        font=("Segoe UI", 48, "bold")
    ))

    add_item(canvas.create_text(
        550,
        335,
        text="Will the next number be...",
        fill=LIGHT,
        font=("Segoe UI", 12)
    ))

    score_text = add_item(canvas.create_text(
        550,
        535,
        text=f"SCORE: {higher_lower_score}",
        fill=CYAN,
        font=("Segoe UI", 10, "bold")
    ))

    feedback = add_item(canvas.create_text(
        550,
        565,
        text="Make your prediction!",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    # --------------------------------------------------------
    # Generate next number in advance
    # --------------------------------------------------------

    next_number = random.randint(
        1,
        50
    )

    while next_number == higher_lower_current:

        next_number = random.randint(
            1,
            50
        )

    if next_number > higher_lower_current:

        correct_choice = "HIGHER"

    else:

        correct_choice = "LOWER"

    # --------------------------------------------------------
    # Answer buttons
    # --------------------------------------------------------

    higher_button = tk.Button(
        window,
        text="⬆  HIGHER",
        bg=CARD,
        fg=WHITE,
        activebackground=GREEN,
        activeforeground=WHITE,
        relief="flat",
        bd=1,
        highlightthickness=0,
        cursor="hand2",
        font=("Segoe UI", 12, "bold")
    )

    higher_button.place(
        x=330,
        y=400,
        width=200,
        height=55
    )

    add_widget(higher_button)

    lower_button = tk.Button(
        window,
        text="⬇  LOWER",
        bg=CARD,
        fg=WHITE,
        activebackground=PINK,
        activeforeground=WHITE,
        relief="flat",
        bd=1,
        highlightthickness=0,
        cursor="hand2",
        font=("Segoe UI", 12, "bold")
        )

    lower_button.place(
        x=570,
        y=400,
        width=200,
        height=55
    )

    add_widget(lower_button)

    def choose_prediction(choice):

        global higher_lower_answered
        global higher_lower_score
        global higher_lower_current

        if higher_lower_answered:
            return

        higher_lower_answered = True

        if choice == correct_choice:

            higher_lower_score += 1

            add_xp(20)

            if choice == "HIGHER":

                higher_button.config(
                    bg=GREEN,
                    activebackground=GREEN
                )

            else:

                lower_button.config(
                    bg=GREEN,
                    activebackground=GREEN
                )

            canvas.itemconfig(
                feedback,
                text=f"✓ CORRECT! Next number was {next_number}. +20 XP",
                fill=GREEN
            )

        else:

            if choice == "HIGHER":

                higher_button.config(
                    bg=PINK,
                    activebackground=PINK
                )

                lower_button.config(
                    bg=GREEN,
                    activebackground=GREEN
                )

            else:

                lower_button.config(
                    bg=PINK,
                    activebackground=PINK
                )

                higher_button.config(
                    bg=GREEN,
                    activebackground=GREEN
                )

            canvas.itemconfig(
                feedback,
                text=f"✗ WRONG! Next number was {next_number}.",
                fill=PINK
            )

        canvas.itemconfig(
            score_text,
            text=f"SCORE: {higher_lower_score}"
        )

        next_button.config(
            state="normal"
        )

    higher_button.config(
        command=lambda:
        choose_prediction("HIGHER")
    )

    lower_button.config(
        command=lambda:
        choose_prediction("LOWER")
    )

    # --------------------------------------------------------
    # Next round
    # --------------------------------------------------------

    def next_round():

        global higher_lower_round
        global higher_lower_current

        higher_lower_round += 1

        if higher_lower_round >= 10:

            show_higher_lower_result()

        else:

            higher_lower_current = next_number

            display_higher_lower()

    next_button = create_button(
        450,
        600,
        200,
        38,
        "NEXT ROUND →",
        next_round,
        PINK
    )

    next_button.config(
        state="disabled"
    )

    create_button(
        450,
        645,
        200,
        28,
        "← BACK TO GAMES",
        show_games,
        CARD_BORDER,
        WHITE,
        8
    )


def show_higher_lower_result():

    clear_page()
    draw_background()
    create_navbar()

    # --------------------------------------------------------
    # Calculate XP
    # --------------------------------------------------------

    xp_earned = higher_lower_score * 20

    # --------------------------------------------------------
    # Determine win / loss
    # 5 or more = WIN
    # --------------------------------------------------------

    if higher_lower_score >= 5:

        higher_lower_won = True

    else:

        higher_lower_won = False

    # --------------------------------------------------------
    # Record statistics
    # --------------------------------------------------------

    record_game(
        "Higher or Lower",
        higher_lower_won,
        xp_earned
    )

    # --------------------------------------------------------
    # Result screen
    # --------------------------------------------------------

    add_item(canvas.create_text(
        550,
        185,
        text="HIGHER OR LOWER COMPLETE!",
        fill=PINK,
        font=("Segoe UI", 25, "bold")
    ))

    add_item(canvas.create_text(
        550,
        245,
        text=f"{higher_lower_score} / 10",
        fill=WHITE,
        font=("Segoe UI", 40, "bold")
    ))

    add_item(canvas.create_text(
        550,
        300,
        text=f"+{xp_earned} XP EARNED",
        fill=CYAN,
        font=("Segoe UI", 12, "bold")
    ))

    if higher_lower_score >= 8:

        message = (
            "Your prediction skills are on fire! 🔥"
        )

    elif higher_lower_score >= 5:

        message = (
            "Nice predictions! Keep playing."
        )

    else:

        message = (
            "The numbers fooled you this time!"
        )

    add_item(canvas.create_text(
        550,
        340,
        text=message,
        fill=GREY,
        font=("Segoe UI", 11)
    ))

    create_button(
        400,
        405,
        130,
        42,
        "PLAY AGAIN",
        show_higher_lower,
        PINK
    )

    create_button(
        570,
        405,
        130,
        42,
        "BACK",
        show_games,
        CARD_BORDER
    )

# ============================================================
# ABOUT
# ============================================================

def show_about():

    clear_page()
    draw_background()
    create_navbar()

    add_item(canvas.create_text(
        550,
        170,
        text="ABOUT PYTHON ARCADE",
        fill=PURPLE,
        font=("Segoe UI", 28, "bold")
    ))

    add_item(canvas.create_text(
        550,
        230,
        text="A fun gaming project built using Python and Tkinter.",
        fill=LIGHT,
        font=("Segoe UI", 12)
    ))

    add_item(canvas.create_text(
        550,
        270,
        text="Learn programming concepts while playing simple games.",
        fill=GREY,
        font=("Segoe UI", 10)
    ))

    add_item(canvas.create_text(
        550,
        330,
        text="PYTHON  •  TKINTER  •  GUI  •  GAMES",
        fill=CYAN,
        font=("Segoe UI", 11, "bold")
    ))

    create_button(
        450,
        400,
        200,
        42,
        "BACK TO HOME",
        show_home,
        PURPLE
    )

# ============================================================
# START APPLICATION
# ============================================================

show_login()

window.mainloop()
