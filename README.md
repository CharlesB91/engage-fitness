# Engage Fitness

Engage Fitness is a industry ready fitness application helping users achieve their ultimate fitness goals. In the wake of COVID-19 the fitness industry took a massive hit with people unable to leave their homes and visit a gym. The fitness industry had to venture into the world of tech to help their client meet their fitness goals at home. Thankfully Engage Fitness offers daily workouts from qualified personal trainers. The site offers full interactive services where users can comment on their experiences using a particular work out. If a user feels they need more support or a 1-2-1 session they can use the booking service where they can book in a time with a personal trainer.

![Home-Page](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/homepage.PNG)

[Deployed Site](https://engagefitness.herokuapp.com/)


## User Experience 

I wanted to create a web based application allowing users to log in and view workout content. These workouts come with pictures, description and videos. Users can comment on each workout to feedback their experience. Users can also use the booking service where they can book in time with a PT. They will receive confirmation of this via email with a zoom link. Due to the goal of this application authorised users can only comment on workouts. Staff users and admin users can create workouts, edit works outs & delete workouts via the sites interface. Did not provide this full functionality to all users as this would defeat the purpose of the site. 

## User Stories

[Kanban Board](https://github.com/CharlesB91/engage-fitness/projects/1)

### Unauthorised Users

- USER STORY: View Home Page - General Site info & Reviews.
- USER STORY: Account registration.

### Authorised Users

- USER STORY: Site Content List.
- USER STORY: Open a tutorial.
- USER STORY: View comments.
- USER STORY: Comment on a tutorial.
- USER STORY: Book Appointments.
- USER STORY: Avoid Double Bookings - Appointment Booker.

### Staff Users

- USER STORY: Create Workout (Staff only site access).
- USER STORY: Edit Workout (Staff only site access).
- USER STORY: Delete Workout (Staff only site access).

### Admin User

- USER STORY: Approve comments.
- USER STORY: Manage posts.

## Design

### Wireframe

[Wireframes](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/wireframes.png)

### Colour

![Colour-Pallet](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/colours.PNG)

- For this area i focused on only 2 particular colours.
- #8ca1a5 for the nav bar.
- #fffff for the background colour - feel this creates a great contract between this and the typography as i was looking for this to stand out.
- I used the built in colours from materialize.css for the buttons within the site.

### Typography

- For this area i focused one font which is "Bebas Neue", cursive; as feel this crates an assertive tone. This was used from Google Fonts.

## Features

### Nav Bar

- This is where the user can navigate easily to each section of the site. 
- There are 2 different types of nav bars depending on users authentication status.

![Not-Authenticated](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/nav.PNG)
![Authenticated](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/nav2.PNG)

### Home Page

- This area features a general information section which explains what the sites offers.
- This area also features a client reviews section.

![Info-Area](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/info-section.PNG)
![Reviews](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/reviews.PNG)

### Nav Bar

- This area has links to relevant social media

![Footer](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/footer.PNG)

### Content List

- This area features a list of each workout posted.
- The user can click on "view workout" for more details. 

![Content-List](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/content-list.PNG)

### Content Detail

- This area features a detailed description of the workout.
- This will include an image, video tutorial, step-by-step instruction.

![Content-detail](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/detail-section.PNG)
![Content-detail](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/detail-section2.PNG)

### Comments

- This area users can add comments on their feedback or anything in general.
- Comments are approved by admin.

![Comments](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/comments.PNG)

### Booking Page

- This area user can book virtual PT sessions.
- They are asking for name, email, start date & start time, End date & End Time - Future feature would be to have end date auto generating as same date as start. 
- When user clicks book the site will check if there is availability within the database. 

![Booking-Page](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/booking.PNG)

### Create Workout

- This area is restricted to only admin & staff users.
- This will generate a form where the select user an post a workout of their choice
- For this area there is a default image as an existing bug relating to cloudinary is preventing adding new images. 

![Create-Workout](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/create.PNG)
![Create-Workout-Form](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/create-form.PNG)

### Edit Workout

- This area is restricted to only admin & staff users.
- This will generate a form where the select user can edit a selected post.
- For this area there is a default image as an existing bug relating to cloudinary is preventing adding new images. 

![Edit-Workout](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/edit-delete.PNG)
![Edit-Workout-Form](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/edit-form.PNG)

### Delete Workout

- This area is restricted to only admin & staff users.
- This section will offer the option to delete the selected post or revert back to the workout list. 

![Delete](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/delete.PNG)

## Database Model

- Here is a diagram of my database model used in this project.

![Data-Model](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/Diagram.drawio.png)

## Technologies Used

- HTML5
- CSS3
- JS 
- JQUERY
- Python
- Django
- Postgres SQL
- Materialize CSS

## Testing

### W3C Validator

#### HTML Validator 

- The only errors picked up in this area seem to stem from summernote. 

#### CSS Validator 

- The only error showing in this area is.
- Value Error : letter-spacing only 0 can be a unit. You must put a unit after your number : 0.4.
- I am unable to locate this within my code therefore i suspect its related to materlizse css.

### JsHint 

- No errors showing in area. 
- Console is logging the following error - The HTML Control provided is not a valid Input Text type.
- However is is related to the datetime picker. This error does not appear when on the booking page. 

### Pep8 Checker 

- Pyton code has been ran thrown this with no errors.
- Have not ran setting.py through this as this code already comes inclusive with django. 

### Googe Lighthouse

- Google lighthouse has been used to test accessibility of this site. This shows above 90

![Lighthouse](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/lighthouse.PNG
)

### Manual Testing

- Can a user sign up - Yes
- Can a user log in - Yes
- Can a user view content list - Yes
- Can a user view work out - Yes
- Can a user post a comment - Yes
- Can a user book an appointment - Yes
- Will the appointment booker advise if appointment double booked - Yes
- Can a staff/admin user create a workout - Yes
- Can a staff/admin user edit a workout - Yes
- Can a staff/admin user delete a workout - Yes

## Bugs

### Resolved Bugs

- Date and time picker. Originally database was set up with data and time in separate schemas. This provided really difficult for the database to query for available appointments. Discovered this query should be inclusive and data and time together. Implemented a data time picker (https://github.com/fawadtariq/materialize-datetimepicker)
- Data time Picker format issue. When appointment was being booked django was throwing a formatting error. Discovered that data time picker had to be formatted a certain way. Reached out Tutor Support & Stackoverflow (https://stackoverflow.com/questions/70085722/date-time-field-django-models)
- Deployment Issue - Site was not rendering when site has been deployed - This was due to a summer note issue. Updated requirements txt which resolved this issue. 
- Site was throwing 500 error when rendering. This was due to a broken html tag. 

### Unresolved Bug

- The only Unresolved bug which remains is when creating & editing working out I could not upload an image to cloudinary. Searched stackoverflow and cloudinary however could not find solution. If a new workout is created via the interface a default image is selected. Images can be uploaded successfully via django admin site. 


## Deployment
 
Deploying the project using Heroku:

1. Login to [Heroku](https://dashboard.heroku.com/apps) and Create a New App

2. Give the App a name, it must be unique, and select a region closest to you

3. Click on 'Create App', this will take you to a page where you can deploy your project

4. Click on the 'Resources' tab and search for 'Heroku Postgres' as this is the add-on you will use for the deployed database

5. Click on the 'Settings' tab at the top of the page. The following step must be completed before deployment. 

6. Scroll down to 'Config Vars' and click 'Reveal Config Vars'. Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py as a root level file.

The env.py files is where the projects secret environment variables are stored. This file is then added to a gitnore file so it isn't stored publicly within the projects repository.

7. Next, the secret key needs to be created within the projects env.py file on GitPod and then added to the Config Vars on Heroku. Once added, go to the settings.py file on GitPod.

8. Within the [settings.py](settings.py) file you need to import several libraries:
    ```python
    from pathlib import Path
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
    import env
    ```

9. Then, we need to replace the current secret key with ```os.environ.get('SECRET_KEY)'```, that we set within the env.py file.

10. Once the secret key is replaced, scroll down to DATABASES to connect to the Postgres database. Comment out the current code and add the following python dictionary: 
```python
DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
```

11. The next step is to connect the project to cloudinary, which is where the static files will be stored. You can find a full explanation of how to use cloudinary [here](https://cloudinary.com/documentation/django_integration)

12. Then on Heroku add to the Config Vars, DISABLE_COLLECTSTATIC = 1, as a temporary measure to enable deployment without any static files, this will be removed when it is time to deploy the full project.

13. Next we need to tell Django where to store the media and static files. Towards the bottom of settings.py file we can add:

```python
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

14. Then we need to tell Django where the templates will be stored. At the top of settings.py, under BASE_DIR (the base directory), add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS': [].

15. Now we have to add our Heroku Host Name into allowed hosts in settings.py file:

```python
ALLOWED_HOSTS = ['YOUR-APP-NAME-HERE', 'localhost']
```

16. Finally, to complete the first deployment set up of the skeleton app, create a Procfile so that Heroku knows how to run the project. Within this file add the following: web: gunicorn APP-NAME.wsgi Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.

17. Now, go to the 'Deploy' Tab on Heroku. Find the 'Deployment Method' section and choose GitHub. Connect to your GitHub account and find the repo you want to deploy. 

18. Scroll down to the Automatic and Manual Deploys sections. Click 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed the code.

21. Once the project is finished deploying, click 'Open App' to see the newly deployed project.

22. Before deploying the final draft of your project you must:

- Remove staticcollect=1 from congifvars within Heroku
- Ensure DEBUG is set to false in settings.py file or:
  Set DEBUG to development with: development = os.environ.get('DEVELOPMENT', False) above it.

## Making a Local Clone
 
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/CharlesB91/engage-fitness)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
 
    $ `https://github.com/CharlesB91/engage-fitness`
 
7. Press Enter. Your local clone will be created.
 
```shell
$ git clone https://github.com/CharlesB91/engage-fitness
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
 
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

You will need to also install all required packages in order to run this application on Heroku, refer to [requirements.txt](requirements.txt)
* Command to install this apps requirements is `pip3 install -r requirements.txt`

## Credits

- Code Institute Blog site walk through - This provided me with logic code to create my content list, content detail and comments feature. 
- [DarshanDev](https://www.youtube.com/watch?v=yenjz1Wv9Yo) - This provided logic code for booking system. 
- [Stackoverflow](https://stackoverflow.com/questions/70085722/date-time-field-django-models) - This helped me resolve my formatting within the datetime picker. 
- Tutor support - This guided me on how to query database for appointment booker. 
- [DennisIvy](https://www.youtube.com/watch?v=EX6Tt-ZW0so) - Provided logic on how to implement full CRUD. 
- [fawadtariq](https://github.com/fawadtariq/materialize-datetimepicker) - materlizse css datetime picker.