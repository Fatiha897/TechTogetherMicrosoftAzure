# Marco Solo 

Motivation:
- Everyone loves to travel, but not everyone has the financial means to do so. BUT traveling doesn't need to be expensive, and it's possible to do so within a budget given an easy way to access trip information and create an easy-to-access and easy-to-update itenrary.

What It Is: 
- Marco Solo is a web-based platform where users can plan a budget for their trip while also lowering their carbon footfrint. Users start off by entering where they're traveling from, where they're traveling to, the length of their trip, and their desired budget. The site walks them through methods of transport, hotels, and possible food spots which could their budget range, and then presents them with a summary of what their possible trip itenerary. 

How It Was Built: 
- Bootstrap 5 to create HTML templates for UI
- Python Flask for application layer of platform
- OpenAI chatGPT for transport, hotel, and food location generations --> This eliminated the need for using multiple APIs, by creating prompts for chatGPT to respond to on the back-end that could then be displayed on the front-end

Challenges we ran into:
- Training the AI to give the desired format of responses. This issue was resolved, but may need follow ups in the future. 
- Parsing AI-generated text. This issue is still in progress.
- Sending data between HTML and the Flask app. This issue was resolved.

Accomplishments that we're proud of:
- Training the AI to model responses that we could more easily parse through our responses. 
- Our ability to problem solve on the fly and use new technologies that were able to adapt to our needs as we fleshed out the vision of our project. Originally, we spent a lot of time trying to figure out which APIs would be best suited to our needs and would fit the limitations we had for hosting and our knowledge of different technologies - going through paid and open source options for maps, geolocation data, and merchant information. Eventually we were able to create a MVP that focuses on the functionality of our code rather than API integration. 

What we learned:
- Parsing information and working with many technologies and API in tandem with each other on the same project - more so than anything we've done before this project had a lot of dependencies that we learned to work with and integrate to make something more powerful than just the sum of its parts.

What's next for Marco Solo:
- Using NLP-parsing with APIs like ones provided by Google Cloud or FOSS options would allow us to more easily parse generated responses and update user information more easily.
- Integrating a maps API for the future iterations of the website. 
