# UX

## Strategy

The purpose of this website is to create a community-based review site for co-op videogames where people can share their experiences and thoughts on videogames that they have played. The target audience is people who want help with deciding what the next co-op game they should to play or just are interested in sharing and reading others reviews of co-op games. 

## Scope

Site owners’ goal: To create a community where people who have a common interest for playing co-op videogames can share reviews and experiences playing different games with each other. In the future the site owner could also be making money on the site if it becomes big enough that they can advertise games on the site and have add-links to places where you can purchase the videogames. 

User’s goal: To share their own experiences playing coop videogames and take part of other people’s experiences.

### User stories 

As an anonymous user 
-	I want to be able to register to join the community.
-	I want to be able to see the reviews and titles that others have posted.
-	I want to be able to search amongst the posts if I am looking for something specific.
-   I want to be able to find the website's social channels.

As a registered user 
- I want to be able to log in to my account.
-	I want to be able write my own game reviews. 
-	I want to be able to delete my own game reviews.  
-	I want to be able to edit game reviews that I have already posted.  
-	I want to be able to add an image and information to my profile. 
-	I want to be able to add a new game title. 
-	I want to be able to delete a game title that I have added, including the reviews added to that title. 
-	I want to be able to edit a game title that I have added. 
-	I should not be able to edit the game titles or reviews that others have shared. 

## Structure

Since the main purpose of this website is for people to share can take part of each other reviews playing coop videogames this is the most important part of the website and everything else implemented on the website it there to support this function. This make the reviews the most important content on the website also so they will be easy to access even before signing up to the website as a user. 

## Skeleton

Figma was used to create wireframes that are linked below.

- [Desktop](static/wireframes/desktop-wireframes.pdf)
- [Desktop when logged in](static/wireframes/desktop-wireframes-logged-in.pdf) 
- [Tablet](static/wireframes/tablet-wireframes.pdf) 
- [Tablet when logged in](static/wireframes/tablet-wireframes-logged-in.pdf) 
- [Mobile](static/wireframes/mobile-wireframes.pdf) 
- [Mobile when logged in](static/wireframes/mobile-wireframes-logged-in.pdf)

## Surface 

### Colors

The colors choosen for this project are choosen to create a visual intrest with a dark background and stronger colors used on elements that should be highlighted. 
![Color scheme](static/images/color-scheme.jpeg)
### Typography
The fonts choosen for the project are found on Google Fonts. Montrerrat are used for the headings in the project and Raleway are used for the body text, these were suggested as a popular paring by Google Fonts. The fallback font for both fonts is Sans-Serif. 

# Database structure

The database was stroed in three different collections users, titles and reviews, shown below. the collections all have relations between the, the reviews and titles and connected by the created_by which is the session user that creates the title or review, this connection is made so that it is able to check if the review or title are created by the user if the user wants to dele or edit a game title or reviews so that onely the user that created it can do that and not the other users. This is also done so that the user can see all the reviews and titles that they have added on their profile page. 

The reviews are connected to the game titles by the title_id which is added to the review when created. This connection is done to be able to show all the reviews that belond to a specific game title om the selected game title template. This connection also made the function to delete all the reviews that belongs to a specific game title if that title is removed and to be able to calculate the avrage rating of a game title from the reviews that belongs to that specific title. 

| Users | |
| ------ | ------ |
| _id | ObjectId |
| username | string |
| email | string |
| password | string |
| favourite_game | string |
| profile_image_url | string |

| Titles | |
| ------ | ------ |
| _id | ObjectId |
| title_name | string |
| image_url | string |
| description | string |
| consoles | array |
| co_op_type | array |
| created_by | string |

| Reviews | |
| ------ | ------ |
| _id | ObjectId |
| title_id | string |
| review | string |
| rating | int32 |
| created_by | string |

# Features 

## Existing features

- Navbar 
    - The navbar contains links to navigate to different parts of the website and the logo. The navbar is sticky so that the user always easily can navigate to different parts of the webpage.
    - As an anonymous user you will have access to the pages Home, Log In and Resgister in the navbar. 
    - As a regitstered user logged in to your account you will have access to the pages Home, Profile, New Game Title, and Log Out in the nabar.
- Footer 
    - The footer contains links to social media and the logo. 
- Home page 
    - Navbar (described under navbar) 
    - The homepage contains a hero image underneath the navbar. 
    - Below the hero image it is a search field so that the user immediately can start searching amongst the game titles on the website and see their reviews.
    - Underneath the search field are the game titles presented. Clicking on a game title takes the user to the selected game title page for that specific game title. 
    - Footer (described under footer) 
- Selected game title 
    - Navbar (described under navbar) 
    - The selected game title page contains a card with an image of the selected game title and all the information avalible on that title.
    - If the user are a registred user that are logged in to their account there is also a add review button on the game title where the user can add their own review to that specific game title. 
    - Underneath the game title all the reviews to that specific game title are presented.
- Log In page
    - Navbar (described under navbar) 
    - The log in page contains a field for filling in your username and password and a button to log in to your account as a registered user.
    If the user inputs correct username and password of an existing user this brings the user to their profile page with the flash message "Welcome, username"shown. 
    If the user trys to log in with either the wrong password or username the flash message "Incorrect username and/or password" appears.
    - Footer (described under footer) 
- Register page
    - Navbar (described under navbar) 
    - The register page will contain a field for filling in your Username, email address, password and a button to register as a user on the webpage. 
    - Footer (described under footer)
- Profile page 
    - Navbar (described under navbar) 
    - On the profile page the user can see the information they have added to their profile.
    - Underneath the profile area the user can see all the titles and reviews that they have added to the website and can edit or delete them.  
    - Footer (described under footer)
- Edit profile page 
    - Navbar (described under navbar) 
    - On the edit profile page the user can change their profile, they can add a profile image and their favorite game. 
    - Footer (described under footer)
- New review page
    - Navbar (described under navbar) 
    - This page contains the function to add a new review to a title. The user writes their review and their rating and then they can submit the review to the website on the submit button. 
    - Footer (described under footer) 
- Edit review page
    - Navbar (described under navbar)
    - This page contains the function to edit a review that the user has previously added to a game title. The current review and rating are already filled in on this page and the user can make the canges and then save the changes on the edit review button. 
    - Footer (described under footer)
- New Title page 
    - Navbar (described under navbar) 
    - The new title page contains the function to add a new game title to the webpage. The user fills out the title of the game, adds a URL to an image, a description of the game, the console it is available on, and if you can play it local, online or both and then they can submit the new title to the webpage on the submit button. 
    - Footer (described under footer) 
- Title page 
    - Navbar (described under navbar) 
    - The title page contains all the information on the game title, the title, average rating, consoles, if you can play it local or online, a description and a button to add a new review to that game title. 
    - Underneath the game title are all the reviews that are added to that specific game title. 
    - Footer (described under footer) 

## Features left to implement

# Technologies Used 

- [HTML5](https://en.wikipedia.org/wiki/HTML5) used to make the structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) used to add style to the project. 
- [Python3](https://www.python.org/) 
- [JQuery](https://jquery.com/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
- [PyMongo]() 
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
- [MongoDB](https://www.mongodb.com/) used to host the database.
- [Heroku](https://www.heroku.com/) used to deply live website. 
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
- [Materialize](https://materializecss.com/) used to style certain elements and to make the website responsive. 
- [Font Awesome](https://fontawesome.com/) used for the icons in the footer. 
- [Google Fonts](https://fonts.google.com/) was used to import the fonts used in the project. 
- [Gitpod](https://www.gitpod.io/) used to develop the project. 
- [Github](https://github.com/) used to store the project. 
- [Figma](https://www.figma.com/) used to make wireframes for the project.  
- [Illustrator](https://www.adobe.com/products/illustrator.html) used to make some changes in the hero image. 
- [RandomKeyGen](https://randomkeygen.com/) to generate the SECRET KEY.  

# Testing

For lenth reasons the testing part is in a sepeate document. Click [here](TESTING.md) to go to the testing document.

# Deployment 

# Credits 

## Code 

## Media 

## Acknowledgements 