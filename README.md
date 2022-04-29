# Engage Fitness

Enagae Fitness is a industry ready finess application helping users acheive their ultimate fitness goals. In the wake of COVID-19 the fitness industy took a massive hit with people unable to leave their homes and visit a gym. The fitness industy had to venture into the world of tech to help their client meet their fitness goals at home. Thankfully Engage Fitness offers daily workouts from qaulified personal trainers. The site offers full interactive services where users can comment on their experiences using a particular work out. If a user feels they need more support or a 1-2-1 session they can use the booking service where they can book in a time with a personal trainer.

![Home-Page](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/homepage.PNG)

[Deployed Site](https://engagefitness.herokuapp.com/)



## User Experience 

I wanted to create a web based applicaion allowing users to log in and view workout content. These workouts come with pictures, discription and videos. Users can comment on each workout to feedback their experience. Users can also use the booking service where they can book in time with a PT. They will receive confirmation of this via email with a zoom link. Due to the goal of this application authorised users can only comment on workouts. Staff users and admin users can create workouts, edit works outs & delete workouts via the sites interface. Did not provide this full fucntionality to all users as this would defeate the purpose of the site. 

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

- This area features a general infomration section which explains what the sites offers.
- This area also features a client reviews section.

![Info-Area](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/info-section.PNG)
![Reviews](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/reviews.PNG)

### Nav Bar

- This area has links to relevant social media

![Footer](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/footer.PNG)

### Content List

- This area features a list of each workout posted.
- The user can click on "view workout" for more detais. 

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
- When user clicks book the site will check if there is avaliabilty within the database. 

![Booking-Page](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/booking.PNG)

### Create Workout

- This area is restricted to only admin & staff users.
- This will generate a form where the select user an post a workout of their choice
- For this area there is a default image as an exisiting bug relatig to cloudinary is preventing adding new images. 

![Create-Workout](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/create.PNG)
![Create-Workout-Form](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/create-form.PNG)

### Edit Workout

- This area is restricted to only admin & staff users.
- This will generate a form where the select user can edit a selected post.
- For this area there is a default image as an exisiting bug relatig to cloudinary is preventing adding new images. 

![Edit-Workout](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/edit-delete.PNG)
![Edit-Workout-Form](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/edit-form.PNG)

### Delete Workout

- This area is restricted to only admin & staff users.
- This section will offer the option to delete the selected post of revent back to the worout list. 

![Delete](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/delete.PNG)


## Database Model

- Here is a diagram of my database model used in this project.

![Data-Model](https://github.com/CharlesB91/engage-fitness/blob/main/static/img/read-me-img/delete.PNG)




































