# Booking System Overbooking Demo (Critical Section)

This project demonstrates how overbooking happens due to a race condition and how to prevent it using synchronization (
mutex lock).

## Requirements

- Python 3.10+

## Run backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
