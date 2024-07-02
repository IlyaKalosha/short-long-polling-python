import time

import requests


def long_polling(url, timeout):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            print(f"Data received: {data}")

            if data.get('status') == 'completed':
                print(f"Polling completed. Time {(time.time() - start_time)}")
        else:
            print(f"Unexpected status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error occurred: {e}")


url = "http://localhost:8000/long_poll"
timeout = 60  # Timeout after 60 seconds
long_polling(url, timeout)
