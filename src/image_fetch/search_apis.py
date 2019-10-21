import requests

from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

from app import app

# def bing_image_search(query):
#   subscription_key = app.config['AZURE_SECRET_KEY']

#   client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

#   image_results = client.images.search(query=query)

#   if image_results.value:
#     num_urls = len(image_results.value)
#     # return num_urls, [(value.thumbnail_url, value.content_url) for value in image_results.value]
#     print(image_results.value[0])
#     urls = [result['content_url'] for result in image_results.value]
#     print(urls)
#     return urls
#   else:
#     # TODO dude, figure something better than this out you n00b
#     # return 0, []
#     return [None, None, None, None, None]

def bing_image_search(query):
  try:
    subscription_key = app.config['AZURE_SECRET_KEY']
    azure_url = app.config['AZURE_IMAGE_API_URL']

    response = requests.get(
      azure_url,
      params={
        'q': query + 'illustrations',
        'count': 1
      },
      headers={
        'Ocp-Apim-Subscription-Key': subscription_key
      }
    )
      
    data = response.json()

    # print(data['value'][0])

    if len(data['value']) > 0:
      urls = [result['contentUrl'] for result in data['value']]
      return urls
    else:
      return [None, None, None, None, None]
  except Exception as e:
    print(e)

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