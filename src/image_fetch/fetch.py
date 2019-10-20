from image_fetch.search_apis import pixabay_image_search, bing_image_search

def fetch_images(query, api='bing', num=5):
  '''
  ! STUB
  ! TODO Complete this method
  !TODO Implement the num thing

  Fetches URLs of images based on the query given. 

  Parameters
  query: query to fetch images
  (optional) api: API to fetch images. Defaults to Bing. Can use pixabay
  (optional) num: number of images to fetch. Defaults to 5.

  Returns a list of URLs.
  '''
  if api == 'bing':
    return bing_image_search(query)
  elif api == 'pixabay':
    return pixabay_image_search(query)
  else:
    raise Exception('Unsupported value of api parameter: {}'.format(api))

  # return [
  #   None,
  #   None,
  #   None,
  #   None,
  #   None
  # ]

