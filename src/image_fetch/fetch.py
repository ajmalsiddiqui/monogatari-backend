import requests

from app import app

def pixabay_image_search(query,
lang='en',
image_type='all',
orientation='all',
safesearch='true'):

  '''
  Uses the Pixabay API to fetch image URLs
  '''

  try:
    pixabay_url = app.config['PIXABAY_API_URL']
    pixabay_api_key = app.config['PIXABAY_API_KEY']

    if not pixabay_api_key or not pixabay_url:
      raise Exception('App missing required parameters: PIXABAY_API_URL or PIXABAY_API_KEY')

    response = requests.get(
      pixabay_url,
      params={
        'q': query,
        'lang': lang,
        'image_type': image_type,
        'orientation': orientation,
        'safesearch': safesearch,
        'key': pixabay_api_key
      }
    )
    
    data = response.json()
    if int(data['totalHits']) > 0:
      urls = [hit['webformatURL'] for hit in data['hits']]
      print(urls)
      return urls
    else:
      # raise Exception('No results found')
      return [None, None, None, None, None]

  except Exception as e:
    print(e)
    return None

def fetch_images(query, num=5):
  '''
  ! STUB
  ! TODO Complete this method
  !TODO Implement the num thing

  Fetches URLs of images based on the query given. 

  Parameters
  query: query to fetch images
  (optional) num: number of images to fetch. Defaults to 5.

  Returns a list of URLs.
  '''

  return pixabay_image_search(query)

  # return [
  #   None,
  #   None,
  #   None,
  #   None,
  #   None
  # ]

