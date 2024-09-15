import time
import requests
from obswebsocket import obsws, requests as obs_requests

# Configuration
TWITCH_CLIENT_ID = 'your_twitch_client_id'
TWITCH_CLIENT_SECRET = 'your_twitch_client_secret'
TWITCH_CHANNEL_NAME = 'twitch_channel_name'
OBS_WS_HOST = 'localhost'
OBS_WS_PORT = 4444
OBS_WS_PASSWORD = 'your_obs_password'

def get_twitch_access_token(client_id, client_secret):
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()['access_token']

def is_twitch_channel_live(access_token, client_id, channel_name):
    url = f'https://api.twitch.tv/helix/streams?user_login={channel_name}'
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return bool(data['data'])

def get_obs_streaming_status(ws):
    response = ws.call(obs_requests.GetStreamingStatus())
    return response.getStreaming()

def start_obs_stream(ws):
    if not get_obs_streaming_status(ws):
        ws.call(obs_requests.StartStreaming())

def stop_obs_stream(ws):
    if get_obs_streaming_status(ws):
        ws.call(obs_requests.StopStreaming())

def main():
    access_token = get_twitch_access_token(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
    was_live = False

    ws = obsws(OBS_WS_HOST, OBS_WS_PORT, OBS_WS_PASSWORD)
    ws.connect()

    while True:
        try:
            is_live = is_twitch_channel_live(access_token, TWITCH_CLIENT_ID, TWITCH_CHANNEL_NAME)
            if is_live and not was_live:
                print(f'{TWITCH_CHANNEL_NAME} is live. Starting OBS stream...')
                start_obs_stream(ws)
                was_live = True
            elif not is_live and was_live:
                print(f'{TWITCH_CHANNEL_NAME} is not live. Stopping OBS stream...')
                stop_obs_stream(ws)
                was_live = False
        except Exception as e:
            print(f'Error: {e}')
        
        time.sleep(60)  # Check every 60 seconds

    ws.disconnect()

if __name__ == '__main__':
    main()
