from flask import Flask, request, json

from app import app

from story_generator.generator import generate_story as gen_story
from image_fetch.fetch import fetch_images

@app.route('/')
def index():
  return 'Hello from the Monogatari API'

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

      story = gen_story(prompt)

      # ! TODO add logic to select keywords
      query = story[0]
      urls = fetch_images(query)

      response = {
        'status': 200,
        'story': story,
        # These URLs will come from the search API
        'urls': urls
      }
  except Exception as e:
    status = 500
    response = {
      'status': 500,
      'message': 'Internal server error',
      'error': '{}'.format(e)
    }

  return json.dumps(response), status