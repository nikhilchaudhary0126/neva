# Neighborhood Evacuation

## Inspiration

Recent events in Ukraine motivated us to create a web app that would allow civilians to fulfill their immediate needs for shelter, evacuation and supplies. Whether it be the prospect of unexpected war or unavoidable natural disasters, we need these evacuation protocols to ensure the safety of people living in affected areas. Evacuation is made easy with the use of this app, which has the potential to save numerous lives.

## What it does?
* Helps you find shelter, supplies and evacuation routes in times of need.
* Allows registered users to post locations for the new shelters or evacuation routes or where to find the essential supplies in the time of emergency or war like situations.

## How we built it
* We used Python and Django web framework to develop this webapp.
* We used below Cloud services and APIs :

| API/Cloud Service  | Usage |
| ------------- | ------------- |
| Google Maps API | Used to show locations based on posts |
| Google Place search API | Used to find geo-location of an address |
| GCloud MySQL DB | Used to store and fetch user posts |
| GCloud App Engine| Created a deployment to host app on GCloud| 


## Challenges we ran into
* We were initially trying to integrate google maps through KML file but we were not able to integrate it with maps so we had to change our approach and build it using Java script google api.
* Although we faced challenges to host our app on Google Cloud Compute, but we were able to complete the web app and able to deliver functioning output on localhost.

## Accomplishments that we're proud of
We were successfully able to integrate Google-map APIs with our webapp and able to deliver results in defined timeline. 

## What's next for Neighborhood Evacuation
* Win a title in the hackathon.
* Share the repo with the world for whoever would want to extend the scope of this project.
We can expand it for more calamity and different type of categories can be added so that more people can take benefit of that.
* In addition, we can add more checks so that any one can not add the random information and avoid misinformation
