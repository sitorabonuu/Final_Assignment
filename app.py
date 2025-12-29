from fastapi import FastAPI
from pydantic import BaseModel
import time
import threading

app = FastAPI(title="Overbooking Demo (Critical Section)")

AVAILABLE_SEATS = 1

CONFIRMED_BOOKINGS = []

seats_lock = threading.Lock()


class BookRequest(BaseModel):
    passenger_name: str
    flight: str = "IST-NMA"


@app.get("/state")
def state():
    return {
        "available_seats": AVAILABLE_SEATS,
        "confirmed_bookings": CONFIRMED_BOOKINGS,
        "confirmed_count": len(CONFIRMED_BOOKINGS),
    }


@app.post("/reset")
def reset(seats: int = 1):
    global AVAILABLE_SEATS, CONFIRMED_BOOKINGS
    AVAILABLE_SEATS = seats
    CONFIRMED_BOOKINGS = []
    return {"ok": True, "available_seats": AVAILABLE_SEATS}


@app.post("/book/unsafe")
def book_unsafe(req: BookRequest):
    global AVAILABLE_SEATS, CONFIRMED_BOOKINGS

    seats = AVAILABLE_SEATS

    time.sleep(0.05)

    if seats <= 0:
        return {"status": "DENIED", "reason": "No seats left (unsafe)"}

    AVAILABLE_SEATS = seats - 1
    CONFIRMED_BOOKINGS.append(req.passenger_name)

    return {"status": "CONFIRMED", "mode": "unsafe", "remaining": AVAILABLE_SEATS}


@app.post("/book/safe")
def book_safe(req: BookRequest):
    global AVAILABLE_SEATS, CONFIRMED_BOOKINGS

    with seats_lock:
        if AVAILABLE_SEATS <= 0:
            return {"status": "DENIED", "reason": "No seats left (safe)"}

        time.sleep(0.05)
        AVAILABLE_SEATS -= 1
        CONFIRMED_BOOKINGS.append(req.passenger_name)

        return {"status": "CONFIRMED", "mode": "safe", "remaining": AVAILABLE_SEATS}
