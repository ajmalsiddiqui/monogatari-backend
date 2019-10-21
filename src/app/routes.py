from flask import Flask, request, json, send_from_directory, send_file

from app import app

from story_generator.generator import generate_story as gen_story
from image_fetch.fetch import fetch_images
from keyword_extractor.extractor import extract_keywords

# Serve the home page
@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/story')
def serve_story():
  return app.send_static_file('story/index.html')

@app.route('/generate-story')
def generate_story():
  '''
  Generates a story along with images given a prompt.

  Parameters:
  prompt: The prompt required to generate a story
  (optional) images: Number of images to be generated for the story. Defaults to 5
  '''

  status = 200
  response = {}

  try:
    prompt = request.args.get('prompt')
    print(prompt)
    if prompt is None:
      status = 400
      response = {
        'status': 400,
        'message': 'Missing required parameters: prompt'
      }
    else:
      images = int(request.args.get('images')) if request.args.get('images') else 5

      story_paras = gen_story(prompt)

      # Find keywords from the story in order to query for the images
      story = ''.join(story_paras)
      print('story: {}'.format(story))
      query = extract_keywords(story)
      queries = query.split('\n')
      if len(query) == 0:
        #! TODO handle this
        print('empty query, setting query to input prompt')
        queries = prompt

      # if len(queries) > 5:
      #   queries = queries[:5]

      print('query: {}'.format(queries))

      urls = []

      for query_keyword in queries:
        new_urls = fetch_images(query_keyword)
        # No images were found
        if new_urls[0] == None:
          continue
        
        # Add the first new URL to the list
        counter = 0
        current_url = new_urls[counter]
        while current_url in urls:
          counter += 1
          current_url = new_urls[counter]
        urls += [new_urls[counter]]
      
      if len(urls) < 5:
        urls += [None] * (5-len(urls))

      parts = [i for i in range(len(story_paras))]

      story_parts_with_urls = [ 
        {'text': story_para,
        'url': para_url } 
        for story_para, para_url in zip(story_paras, urls)]

      story_full = dict(zip(parts, story_parts_with_urls))

      response = {
        'status': 200,
        'story': story_full
      }
  except Exception as e:
    print(e)
    status = 500
    response = {
      'status': 500,
      'message': 'Internal server error',
      'error': '{}'.format(e)
    }

  return json.dumps(response), status