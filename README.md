# 📍 Booking System Overbooking Demo (Critical Section)

This project demonstrates how **overbooking happens** in a booking system due to **race conditions**, and how the problem relates to **critical sections** in operating systems and concurrent programming.

The system simulates multiple booking requests hitting the same resource at the same time, showing why synchronization is essential in real-world systems like airlines, hotels, and logistics platforms.

---

## 🧠 Why This Project Exists

Overbooking is not magic — it’s a **concurrency bug**.

When multiple processes or threads access shared data **without synchronization**, they can:
- Read the same availability
- Update it simultaneously
- Cause inconsistent system state

This project visually and programmatically demonstrates that issue.

---

## 🚀 Features

- Python backend for booking logic
- Simulation of concurrent booking requests
- Simple HTML frontend
- Clear demonstration of race conditions
- Educational focus on critical sections

---

## 📂 Project Structure

Final_Assignment/
│
├── app.py # Backend booking logic
├── simulate.py # Simulates concurrent booking attempts
├── index.html # Simple frontend UI
├── requirements.txt # Python dependencies
├── readme.md # Previous README version
└── .gitignore


---

## 🛠 Requirements

- Python 3.10+
- Modern web browser (optional, for UI)

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sitorabonuu/Final_Assignment.git
cd Final_Assignment


pip install -r requirements.txt
python app.py
uvicorn app:app --reload
python simulate.py

5️⃣ Open Frontend (Optional)

Open index.html in your browser.
