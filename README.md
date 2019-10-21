# Monogatari

Monogatari: Stories for Us. A system that takes a single line prompt and generates a full short story, complete with pictures to accompany it, from it.

## Problem

Stories are fun! However, it is easy to run out of stories to tell your kids or students. This system takes the slightest hint of human creativity and turns it into a full story, complete with pictures, for an engaging experience. The images are the defining feature - they change the story from a bland blob of text into something lively and attractive. Great way to keep kids engaged while they learn and enjoy. Furthermore, this system has an accessibility tech application - it caters to the niche audience of children with ASD (Autism Spectrum Disorder). Autistic children have difficulties in processing sequential information like text, but are able to learn and follow exceptionally well when pictures and visuals are presented. Our system generates images for the stories as well, which helps autistic kids enjoy them too.

## Challenges

Original GPT-2 model which genetates the stories was inappropriate and bifurcated from the topic. We had to retrain the model on our custom data which we prepared manually in the hack. There were technical problems with backend and integration. Irrelevent images were being displayed by the search API which we solved by adding our own queries to the searches internally. Keyword extraction was ineffective when the text was small.

We were able to switch to a better engine for image search, and we internally augment queries to generate images. In order to make this more powerful, we use topic extraction on the generated stories to construct the query which is used to fetch images.

## Technologies
- OpenAI GPT-2
- Gensim TextRank
- Azure Cognitive Services
- Google Colab
- Python
- HTML
- CSS
- JavaScript