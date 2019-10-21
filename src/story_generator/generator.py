import os
from pathlib import Path

import gpt_2_simple as gpt2

M124_models_relative_path = '{}/../../../models'.format(__file__)

RUN1_models_relative_path = '{}/../../../models/checkpoint'.format(__file__)

def generate_story(prompt, model='run1'):
  '''
  ! STUB
  ! TODO Complete this method

  Generates a story given a prompt.

  Returns an array of paragraphs.
  '''
  model_relative_path = '{}/../../../models'.format(__file__) if model == '124M' else '{}/../../../models/checkpoint'.format(__file__)
  models_path = Path(model_relative_path).resolve()
  print(models_path)
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess, model_name=model, model_dir=models_path)

  t = gpt2.generate(sess,
    model_name=model,
    model_dir=models_path,
    prefix=prompt,
    length=350,
    temperature=0.7,
    top_p=0.9,
    nsamples=1,
    batch_size=1,
    return_as_list=True,
    truncate='<|endoftext|>')
  # print(t)
  # print(str(t).split('===================='))
  # print('---')
  # print(t)
  # s = t[0]
  # print(s)
  # l = s.split('.')
  # print(l)
  # return l
  # return [
  #   'The frontend is cool. The backend is even cooler.',
  #   'The backend is cool. The frontend is bad.',
  #   'Naruto will be the next hokage. Sakura is useless.',
  #   'Tank pe chadenge. Sabse ladenge.',
  #   'Wowie. This is cool cool.'
  # ]
  return t[0].split('\n\n') if model == '124M' else t[0].split('\n')

if __name__ == '__main__':
  generate_story('Once upon a time there lived a beautiful princess')