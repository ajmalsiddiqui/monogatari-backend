import os
import sys

from environs import Env

class Config:
  PIXABAY_API_URL = 'https://pixabay.com/api/'
  PIXABAY_API_KEY = os.environ.get('PIXABAY_API_KEY')

  def __init__(self):
    try:
      env = Env()
      # ! TODO check if env file exists and env is dev before trying to read it
      env.read_env()
      if not PIXABAY_API_KEY:
        raise Exception('Missing required app configuration parameter: PIXABAY_API_KEY')
    except Exception as e:
      print(e)
      sys.exit(1)