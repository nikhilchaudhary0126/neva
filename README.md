# Neighborhood Evacuations

### Inspiration

Recent events in Ukraine motivated us to create a web app that would allow civilians to fulfill their immediate needs for shelter, evacuation and supplies. Whether it be the prospect of unexpected war or unavoidable natural disasters, we need these evacuation protocols to ensure the safety of people living in affected areas. Evacuation is made easy with the use of this app, which has the potential to save numerous lives.

### What it does?
* Helps you find shelter, supplies and evacuation routes in times of need.
* Allows registered users to post locations for the new shelters or evacuation routes or where to find the essential supplies in time of emergency or war like situations.

### Application Flow
* Simply check the homepage for finding shelters, supplies or evacuation routes

<img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Home.jpg" alt="BFS" width="300" height="200"> 

* Registered users can login and new users can register for new post creations.

<img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Login.jpg" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Register.jpg" alt="BFS" width="300" height="200">

* To create a post click Post and choose options:

<img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Post%20options.jpg" alt="BFS" width="300" height="200">

* The map gets updated after you create a post with details:

<img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Flow-before.jpg" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Flow-post.jpg" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/neva/blob/main/outputs/Flow-after.jpg" alt="BFS" width="300" height="200">

### Runtime Instructions
* This webapp uses external apis and keys which should be defined in local runtime environments.

* Install all python packages using:

```pip3 install -r requirements.txt```
* Run the webapp at localserver

```python3 manage.py runserver```
