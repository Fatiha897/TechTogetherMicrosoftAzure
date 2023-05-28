# Marco Solo 

## Inspiration

Everyone loves to travel, but not everyone has the financial means to do so. BUT traveling doesn't need to be expensive, and it's possible to do so within a budget given an easy way to access trip information and create an easy-to-access and easy-to-update itinerary.

## What it does

Marco Solo is a web-based platform where users can plan a budget for their trip while also lowering their carbon footprint. Users start off by entering where they're traveling from, where they're traveling to, the length of their trip, and their desired budget. The site walks them through methods of transport, hotels, and possible food spots which could their budget range, and then presents them with a summary of what their possible trip itinerary.

Marco Solo is a Flask web app using ChatGPT responses to allow users to create a budget for their solo travel trips that shows them different options, factoring in cost and carbon emissions, to help them construct their ideal budget. 

## How we built it
##### Bootstrap

Bootstrap5 to create HTML templates for UI. CSS- and Sass-powered templates and pre-generated components to allow for visually appealing design in our compacted timeline. 

##### Flask

Python web-application creation for dynamically generated pages. Flask enabled us to generate our pages as information relevant to the user popped up. 

##### TomTom Maps API

For geolocation of selected locations. 

##### ChatGPT Integration

To give information on transport, hotel, and food location generations. This eliminated the need for using multiple APIs, by creating prompts for chatGPT to respond to on the back-end that could then be displayed on the front-end. 

## Challenges we ran into

 - Training the AI to give the desired format of responses. This issue was resolved, but may need follow ups in the future.
 - Parsing AI-generated text. This issue is still in progress.
 - Sending data between HTML and the Flask app. This issue was resolved.

## Accomplishments that we're proud of

Training the AI to model responses that we could more easily parse through our responses. 

We're proud of our ability to problem solve on the fly and use new technologies that were able to adapt to our needs as we fleshed out the vision of our project. Originally, we spent a lot of time trying to figure out which APIs would be best suited to our needs and would fit the limitations we had for hosting and our knowledge of different technologies - going through paid and open source options for maps, geolocation data, and merchant information. Eventually we were able to create a MVP that focuses on the functionality of our code rather than API integration. 

## What we learned

We learned a lot about parsing information and working with many technologies and API in tandem with each other on the same project - more so than anything we've done before this project had a lot of dependencies that we learned to work with and integrate to make something more powerful than just the sum of its parts. 

## What's next for Marco Solo

In future, using NLP-parsing with APIs like ones provided by Google Cloud or FOSS options would allow us to more easily parse generated responses and update user information more easily. 

Additionally, integrating the TomTom Maps API to show the regional map of different areas and provide search for places of interest, calculating routes between different areas and even more functionality would create a more powerful app. 
