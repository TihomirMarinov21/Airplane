# ✈️ Airplane Passenger Registration System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![NiceGUI](https://img.shields.io/badge/Framework-NiceGUI-green)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **Python GUI application built with NiceGUI** that simulates an airplane system where users can:

- Register passengers
- Assign seats
- Simulate takeoff and landing
- Display crew and passenger information
- Prevent duplicate seat reservations

This project demonstrates **GUI design, async programming, and object-oriented Python**.

---

# 🚀 Features

### ✈️ Flight Simulation
- Simulated **takeoff and landing**
- Real-time **altitude updates**
- Dynamic **flight status messages**
- Interactive **altitude slider**

---

### 👥 Passenger Registration
Passengers can register through an interactive form:

- First name
- Last name
- Age
- Row selection
- Seat selection
- Luggage size
- Check-in status

✔ Input validation included  
✔ Seat reservation system prevents duplicates

---

### 📊 Passenger Table
Displays all registered passengers including:

- Name
- Age
- Row
- Seat
- Luggage size
- Check-in status

---

### 👨‍✈️ Crew Generation
The system automatically generates:

- **2 pilots**
- **4 crew members**

Each crew member has randomly generated:

- Name
- Age

---

# 🖼 Demo

## Main Interface
<img width="753" height="681" alt="Screenshot 2026-03-08 100632" src="https://github.com/user-attachments/assets/166c2597-c530-42ec-9d9b-4e58726ebf35" />

## Passenger Registration Dialog
<img width="722" height="949" alt="Screenshot 2026-03-08 100424" src="https://github.com/user-attachments/assets/d917d22c-b530-460b-9991-16189a49fb76" />

## Passenger Table
<img width="743" height="760" alt="Screenshot 2026-03-08 100510" src="https://github.com/user-attachments/assets/8c359a6a-fac9-48b5-ada6-bf2ef4ed3ede" />

## Flight Simulation
<img width="446" height="187" alt="Screenshot 2026-03-08 100534" src="https://github.com/user-attachments/assets/897b94b0-1c17-414f-b4fb-af2eeddea541" />
<img width="365" height="155" alt="Screenshot 2026-03-08 100557" src="https://github.com/user-attachments/assets/5e88b765-2000-4e18-bdcb-421d6bc73904" />
<img width="345" height="124" alt="Screenshot 2026-03-08 100611" src="https://github.com/user-attachments/assets/47f9162f-b6d2-4d57-b829-5e2b5099dc17" />

# 🛠 Technologies Used

- **Python**
- **NiceGUI**
- **Asyncio**
- **HTML / CSS**
- **Object-Oriented Programming**

---

# 📂 Project Structure

```
airplane-passenger-system
│
├── main.py
├── classes.py
├── ui_elements.py
│
├── images
│   ├── main_ui.png
│   ├── dialog.png
│   ├── passenger_table.png
│   └── flight.gif
│
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/airplane-passenger-system.git
```

Navigate to the folder

```bash
cd airplane-passenger-system
```

Install dependencies

```bash
pip install nicegui
```

---

# ▶️ Running the Application

Run the main file:

```bash
python main.py
```

NiceGUI will start a local server.

Open in your browser:

```
http://localhost:8080
```

---

# 🧠 How the System Works

### Airplane Class
Handles:

- Current altitude
- Passenger count
- Takeoff simulation
- Landing simulation

---

### Seat Reservation System

To prevent duplicate seat booking:

```python
taken_seats = set()
```

Seats are stored as:

```python
(row, seat)
```

If a seat is already taken, the system shows a **notification warning**.

---

# 📚 Learning Goals

This project helped practice:

- GUI development with **NiceGUI**
- **Async programming** in Python
- **Object-Oriented Design**
- **Dynamic UI updates**
- **Input validation**

---

# 🔮 Future Improvements

Possible upgrades:

- Seat map visualization
- Passenger editing / deletion
- Flight destination system
- Multiple airplanes
- Database storage
- Authentication system

---

# 👨‍💻 Author

Developed as a Python GUI project using **NiceGUI**.

If you like the project ⭐ consider giving it a star on GitHub!
