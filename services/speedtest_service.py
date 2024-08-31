import speedtest
import time
import logging

def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbits/s
        upload_speed = st.upload() / 1_000_000    # Convert from bits/s to Mbits/s
        ping = st.results.ping
        return {
            'download_speed': download_speed,
            'upload_speed': upload_speed,
            'ping': ping
        }
    except Exception as e:
        logging.error(f"Error during speed test: {e}")
        raise


def simulate_real_time_speedtest():
    results = {'download_speed': 0, 'upload_speed': 0, 'ping': 0}
    for _ in range(30):  # Simulate 30 seconds of real-time updates
        results['download_speed'], results['upload_speed'], results['ping'] = run_speedtest()
        time.sleep(1)  # Update every second
        yield results
