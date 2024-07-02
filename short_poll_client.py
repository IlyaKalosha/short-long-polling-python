import time
import requests


def short_polling(url, interval, timeout):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                data = response.json()
                print(f"Data received: {data}")

                if data.get('status') == 'completed':
                    print(f"Polling completed. Time {(time.time() - start_time)}")
                    break
            else:
                print(f"Unexpected status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error occurred: {e}")

        if time.time() - start_time > timeout:
            print("Polling timeout exceeded.")
            break

        time.sleep(interval)


url = "http://localhost:8000/short_poll"
interval = 5  # Poll every 5 seconds
timeout = 60  # Timeout after 60 seconds
short_polling(url, interval, timeout)
