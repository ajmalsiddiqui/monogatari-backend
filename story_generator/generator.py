import gpt_2_simple as gpt2
def generate_story(prompt):
  '''
  ! STUB
  ! TODO Complete this method

  Generates a story given a prompt.

  Returns an array of paragraphs.
  '''
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess, model_name='124M')
  t = gpt2.generate(sess,
                model_name='124M',
                prefix=prompt,
                length=100,
                temperature=0.7,
                top_p=0.9,
                nsamples=5,
                batch_size=5
                )
  s = t[0]
  l = s.split('.')
  return l
