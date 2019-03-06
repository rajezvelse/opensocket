import os

SETTINGS = {
    "SERVER_HOST": "0.0.0.0",
    "SERVER_PORT": 8000,
    "DATABASE_URL": "sqlite:///data/db/opensocket.db"
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_SETTINGS = {
    "REQUEST_MAX_SIZE": 100000000,  # 100 megabytes
    "REQUEST_BUFFER_QUEUE_SIZE": 100,
    "REQUEST_TIMEOUT": 60,  # 60 seconds
    "RESPONSE_TIMEOUT": 60,  # 60 seconds
    "KEEP_ALIVE": True,
    "KEEP_ALIVE_TIMEOUT": 5,  # 5 seconds
    "WEBSOCKET_MAX_SIZE": 2 ** 20,  # 1 megabytes
    "WEBSOCKET_MAX_QUEUE": 32,
    "WEBSOCKET_READ_LIMIT": 2 ** 16,
    "WEBSOCKET_WRITE_LIMIT": 2 ** 16,
    "GRACEFUL_SHUTDOWN_TIMEOUT": 15.0,  # 15 sec
    "ACCESS_LOG": True,
}
