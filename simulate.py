import threading
import requests

BASE = "http://127.0.0.1:8000"


def hit(endpoint: str, name: str):
    r = requests.post(f"{BASE}{endpoint}", json={"passenger_name": name})
    print(name, endpoint, r.json())


def run(endpoint: str, seats: int, passengers: list[str]):
    requests.post(f"{BASE}/reset", params={"seats": seats})
    threads = []
    for p in passengers:
        t = threading.Thread(target=hit, args=(endpoint, p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("FINAL STATE:", requests.get(f"{BASE}/state").json())
    print("-" * 60)


if __name__ == "__main__":
    passengers = ["Passenger_A", "Passenger_B", "Passenger_C"]

    print("=== UNSAFE (race condition) ===")
    run("/book/unsafe", seats=1, passengers=passengers)

    print("=== SAFE (mutex lock) ===")
    run("/book/safe", seats=1, passengers=passengers)
