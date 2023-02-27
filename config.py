import os
import logging
from dotenv import load_dotenv

if os.path.exists('config.env'):
    load_dotenv('config.env', override=True)


class Config:
    def __init__(self) -> None:
        self.SESSION: str = os.environ.get('SESSION', 'AgAvGsx3xprOUr4guSDFDqZt41sbcwI4aiRxb-tFIJ0q3sz6D4uAiYsSQp0TsbrZgwmDnK0sXL82ahMMKvmAr9PgJPTMNq7EzR--TSp4dfSrKq795WNvAHxI8NPErClnso6VNZ5cStwqAKyMF7bdX49z0aQPEBWTFPXtVx6BbmA154ykGBfPvVFISAzJTAhZgrfIJMeb2r48WUbL2qB9ze4TqkREYTXCTdF1lMqr5Hkp_n0Gle7-k-w0LQ7SWTiTLPuiPhmRa3Vc7MEdZUjgcnoMv7T-PuJ31OjMiqKLG5B2Y8QdP57IfjpC1OepdOyPitVzftch8pgsPKibrV2EQCT6AAAAAU9z4jMA')
        self.API_ID: str = os.environ.get('API_ID', '12878302')
        self.API_HASH: str = os.environ.get('API_HASH', '1ce756e879790d465304f48c36294883')
        self.SUDO: list = [int(id) for id in os.environ.get(
            'SUDO', ' ').split() if id.isnumeric()]
        if not self.SESSION or not self.API_ID or not self.API_ID:
            print('Error: SESSION, API_ID and API_HASH is required.'
                  'Please check your config.env file.')
            quit(0)
        self.SPOTIFY: bool = False
        self.SPOTIFY_CLIENT_ID: str = os.environ.get('SPOTIFY_CLIENT_ID', 'af511d12d0e8472997bba14292efb0c3')
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get(
            'SPOTIFY_CLIENT_SECRET', '3dd2d7951aed42778aa5fcb365b31109')
        _log_level = os.environ.get('LOG_LEVEL', 'error').lower()
        if _log_level == 'error':
            self.LOG_LEVEL = logging.ERROR
        elif _log_level == 'info':
            self.LOG_LEVEL = logging.INFO
        elif _log_level == 'debug':
            self.LOG_LEVEL = logging.DEBUG
        else:
            self.LOG_LEVEL = logging.ERROR
        self.PREFIXES: list = os.environ.get('PREFIX', '!').split()
        self.DEFAULT_LANG: str = os.environ.get('DEFAULT_LANG', 'tr').lower()
        self.DEFAULT_STREAM_MODE: str = 'audio' if (os.environ.get(
            'DEFAULT_STREAM_MODE', 'audio').lower() == 'audio') else 'video'


config = Config()
