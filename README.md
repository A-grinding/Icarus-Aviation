# ✈️ Icarus Aviation — *the world on wings*

A terminal-based flight booking system built with Python and MySQL. Users can sign up or log in, search for flights, book seats, cancel bookings, and manage their account details — all from the command line.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [Setup & Installation](#-setup--installation)
- [Configuration](#-configuration)
- [Running the App](#-running-the-app)
- [Usage Guide](#-usage-guide)
- [Known Issues & Limitations](#-known-issues--limitations)
- [Future Improvements](#-future-improvements)

---

## ✨ Features

- **Sign Up / Log In** — Register a new account or log into an existing one
- **Flight Search** — View available flights between any two cities for upcoming dates
- **Booking** — Choose a flight, pick seats, and pay via Card or UPI
- **Cancellation** — Cancel a booked flight (80% refund policy)
- **Account Management** — Update your username, email, phone number, or password
- **View Bookings** — See all your current booked flights in a formatted table

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Language  | Python 3.x |
| Database  | MySQL |
| DB Driver | `mysql-connector-python` |
| Formatting | `tabulate` |

---

## 🗄 Database Schema

The app automatically creates a database called `icarus_aviation` with three tables:

### `customer`
| Column | Type | Notes |
|--------|------|-------|
| `username` | VARCHAR(30) | Display name |
| `phone_num` | VARCHAR(10) | Primary key |
| `email` | VARCHAR(30) | Primary key |
| `password` | VARCHAR(15) | Stored in plain text (see Known Issues) |

### `flight_status`
| Column | Type | Notes |
|--------|------|-------|
| `flight_no` | VARCHAR(5) | Primary key |
| `from_place` | VARCHAR(20) | Boarding city |
| `to_place` | VARCHAR(20) | Destination city |
| `price` | VARCHAR(9) | Per-seat price |
| `date` | VARCHAR(20) | Date of flight (DD/MM/YYYY) |

### `booked_flight`
| Column | Type | Notes |
|--------|------|-------|
| `boarding` | VARCHAR(30) | Boarding city |
| `destination` | VARCHAR(30) | Destination city |
| `date` | VARCHAR(20) | Flight date |
| `phone_num` | VARCHAR(10) | Customer phone |
| `flight_no` | VARCHAR(5) | Flight number |
| `seats` | VARCHAR(10) | Number of seats booked |

---

## ⚙ Setup & Installation

### 1. Clone or download the project

```bash
git clone https://github.com/your-username/icarus-aviation.git
cd icarus-aviation
```

### 2. Install Python dependencies

```bash
pip install mysql-connector-python tabulate
```

### 3. Make sure MySQL is running

Start your local MySQL server (XAMPP, MySQL Workbench, or system service).

---

## 🔧 Configuration

Open `main.py` and update the database connection details at the top of the file:

```python
mydb = sab.connect(
    host="localhost",      # your MySQL host
    user="root",           # your MySQL username
    password="123456",     # ← replace with your actual password
    port="3306"            # your MySQL port
)
```

> The app will automatically create the `icarus_aviation` database and all required tables on first run — no manual SQL setup needed.

---

## ▶ Running the App

```bash
python main.py
```

You'll see the main menu in your terminal:

```
✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️
✈️             ICARUS AVIATION             ✈️
✈️             ᵗʰᵉ ʷᵒʳˡᵈ ᵒⁿ ʷⁱⁿᵍˢ          ✈️
✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️

╒═══════════════════════╤════════════════════════════════════════════╕
│       CHOICE          │     KEY TO BE PRESSED ON KEYBOARD          │
╞═══════════════════════╪════════════════════════════════════════════╡
│ LOG-in                │ 1                                          │
│ Sign-up               │ 2                                          │
│ To exit               │ 3                                          │
╘═══════════════════════╧════════════════════════════════════════════╛
```

---

## 📖 Usage Guide

### 🆕 Sign Up (Press `2`)
- Enter a password, username, phone number, and email
- Duplicate phone numbers and emails are rejected
- If a duplicate is detected, you're offered the option to log in instead

### 🔑 Log In (Press `1`)
- Enter your username and password
- On success, you're taken to the main dashboard

### Dashboard Options

| Key | Action |
|-----|--------|
| `1` | Book a flight |
| `2` | Cancel a flight |
| `3` | Update account details |
| `4` | View booked flights |
| `5` | Sign out |

### ✈ Booking a Flight
1. Enter your **boarding city** and **destination city** (letters only)
2. A table of 5 available flights is displayed (4 preset + 1 random)
3. Enter the **flight number** you want
4. Enter the **number of seats** (up to 10)
5. Choose payment: **Card** (`c`) or **UPI** (`u`)
6. Confirm payment — booking is saved to the database

### ❌ Cancelling a Flight
- Enter the flight number of the booking you want to cancel
- 80% refund is credited within 2–3 business days
- Only bookings linked to your phone number can be cancelled

### ✏ Updating Account Details
- Requires re-authentication (username + password)
- Options: update username, email, phone number, or password

---

## ⚠ Known Issues & Limitations

- **Passwords are stored in plain text** — no hashing is used. Not suitable for production.
- **SQL Injection risk** — queries use string formatting (`.format()`). Should be replaced with parameterised queries.
- **No seat availability check** — flights have no actual seat limits enforced.
- **Flight data is regenerated on every booking** — the `flight_status` table is wiped and repopulated each time a booking is initiated, which could cause issues if multiple users book simultaneously.
- **Cancellation deletes all bookings for a phone number**, not just the selected flight — the `DELETE` query should use `flight_no` as a filter too.
- **Update password bug** — the update password query currently updates `phone_num` instead of `password` (line with `new4`).
- **Superscript font map** — the `get_super()` function has some character mismatches in the mapping table.
- **No input length validation** on several fields (e.g., seat count maximum of 10 is stated but not enforced).

---

## 🚀 Future Improvements

- [ ] Password hashing (e.g., `bcrypt`)
- [ ] Parameterised SQL queries to prevent injection
- [ ] Seat availability tracking
- [ ] Admin panel for managing flights
- [ ] Flight number validation when booking
- [ ] GUI version (Tkinter or web-based)
- [ ] Email confirmation on booking
- [ ] Proper cancellation by flight number (not just phone number)

---

## 👤 Author

Built as a Python + MySQL terminal project — **Icarus Aviation**.  
*"The world on wings"* ✈️
