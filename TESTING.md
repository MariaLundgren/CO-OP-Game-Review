# Testing 

## Validation 

## Features 

### Navbar

#### Manual testing of Navbar

- Clicking on the logo reloads the homepage. 
- Clicking on the home link reloads the homepage. 
- Clicking on the Log In link brings user to Log In page.
- Clicking on the Register link brings user to Register page. 
- Clicking on the Profile link brings user to Profile page. 
- Clicking on the New Game Title link brings user to New Game Title page. 
- Clicking on the Log Out link removes user from session cookie and brings user to Log In page. 
- Hovering over the liks to make sure they become darker when hovering over them. 
- Scrolling down the page the navbar stays at the top of the browser window.
- This was repeated on all pages to make sure the navbar works on every page.

### Footer 

#### User stories testing Footer

- I want to be able to find the website's social channels.
    - In the footer there are links to the website's social media channels.

#### Manual testing of Footer

- Clicking the Facebook icon brings user to facebook.com in a new browser window.
- Clicking the Instagram icon brings user to instagram.com in a new browser window.
- Hovering over the contact link and social icons to make sure they become lighter when hovering over them.
- This was repeated on all pages to make sure the footer works on every page.

### Home

#### User stories testing Home 

- I want to be able to search amongst the posts if I am looking for something specific.
    - On the homepage the user can search among the titles for a specific game title.

#### Manual testing of Home

- Searching for a existing game title and i get that game title displaying underneath the searchfield.
Also tested to search in all lower and uppercase to see that this also works, and this also displays the game title.
-  Searching for a title that don't exist in the DB and this shows the text "couldn't finde game title", as expected. 
- Clicking on the restet button after a search and this shows all tha added game titles again, as expected. 
- Clicking on the card of a geme title brings me to the selected game title page of that specific title.

### Selected Game Title

#### User stories testing Selected Game Title

- I want to be able to see the reviews and titles that others have posted.
    - On the selected game title page the user cal see all the avalible information about the selected game title. 
    Underneath the game title the user can also see all the reviews that have been added to that speceific game title.

#### Manual testing of Selected Game Title

- Visit the selected game title page as an anonymous user to make sure the add game title button isn't appearing.
- Visit the site as a regitred user that are logged in to their account and the add a review button is visible. 
- Hovering over add review button to make sure it become lighter when hovering over.
- Clicking on add review button and this brings the user to the add review page.

### Log In

#### User stories testing Log In

- I want to be able to log in to my account.
    - On the Log In page the user can Log In to their account with their username and password. 

#### Manual testing of Log In

- Trying to log in without filling out the username field and a message appears to fill out this field.
- Trying to log in with the wrong username and the flash message "Incorrect username and/or password" appears.
- Trying to log in without filling out the password field and a message appears to fill out this field.
- Trying to log in with the wrong password and the flash message "Incorrect username and/or password" appears.
- Trying to log in with the wrong username and the wrong password the flash message "Incorrect username and/or password" appears.
- Trying to log in with an existing user and correct password and this brings me to the profile page of this user,
and shows flash message "Welcome, username". 

### Register

#### User stories testing Register

- I want to be able to register to join the community.
    - On the register page an anonymous user can register by adding a username, emailadress and password to get an account and become a registered user.

#### Manual testing of Register

- Trying to register without filling out the username field and a message appears to fill out this field.
- Trying to register a username with less than 5 characters and a message appears that the username must match requested format. 
- Trying to register a username with more than 15 characters and the form wont let me fill in more than 15 characters. 
- Trying to register a username with a charachter that is not allowed and a message appears that the username must match requested format. 
- Trying to register without filling out the email field and a message appears to fill out this field.
- Trying to register without filling out the password field and a message appears to fill out this field.
- Trying to register a password with less than 5 characters and a message appears that the username must match requested format.
- Trying to register a password with more than 15 characters and the form wont let me fill in more than 15 characters. 
- Trying to register a password with a charachter that is not allowed and a message appears that the username must match requested format. 
- Trying to register a user with a username that already exist in the db and flash message "Username already exist. Please choose another username." appears. 
- Trying to register with all the forms filled out correctlly and the user gets redirect to their profile page with the flash message "Registration Successful" showing, and the user gets added to the users collection in mongodb. 

### Profile

#### User stories testing Profile

- I want to be able to delete my own game reviews.  
    - On the users profile page they can see all the reviews that the user have added. 
    On each review there are a delete button that the user can click on if they want to delete that specific review.
- I want to be able to delete a game title that I have added, including the reviews added to that title. 
    - On the users profile page they can see all the game titles that the user have added. 
    On each game title there are a delete button that the user can click on if they want to delete that specific title,
    the user will also delete all the reviews that have been added to that game title even if added by another user.

#### Manual testing of Profile

- Hovering over edit profile button to make sure it become lighter when hovering over.
- Clicking on edit profile button and this takes the user to edit profile page.
- Hovering over delete buttons on reviews and game titles to make sure it become lighter when hovering over.
- Clicking on delete button on review and this deletes the review and flash message "Review deleted" appears.
- Clicking on delete button on game title and this deletes the title and flash message "Title deleted" appears.
- Hovering over edit buttons on reviews and game titles to make sure it become lighter when hovering over.
- Clicking on edit button on review and this takes the user to edit review page. 
- Clicking on edit button on game title and this takes the user to edit title page.
- Clicking on the card of a geme title brings me to the selected game title page of that specific title.
- Saving the url for a logged in users profile page and tries to access it after logging out and this redirects the user to the log in page.
- Saving the url for a logged in users profile page and tries to access it after logging in as a different user and this brings the user to their own profile page.

### Edit Profile

#### User stories testing Edit Prfofile

- I want to be able to add an image and information to my profile.
    - On the edit profile page the user can edit their profile, the user can add/edit their profile image
    and edd/edit what their favourite game is. 

#### Manual testing of Edit Profile
- Try to add an image in the input field for image url and clicking on edit profile button.
This brings the user back to the profile back, an image is shown on the profile, flash message "Profile Updated" appears,
and the image url is stored on the user in the db. 
- Tryes to add more than 30 characters in favourite game input field and the field wont let me put in more than 30 characters. 
- Try to add a favourite game in the input field for favourite game and clicking on edit profile.
This brings the user back to the profile back, a favourite game is shown on the profile, flash message "Profile Updated" appears,
and the favourite game is stored on the user in the db. 
- Saving the url for the edit profile page and tries to access it after logging out and this redirects the user to the log in page.
- Saving the url for the edit profile page and tries to access it after logging in as a different user and this brings the user to their
own edit profile page. 

### New Review

#### User stories testing New Review
- I want to be able write my own game reviews. 
    - On the add review page a registered user that are logged in to their account can add a review to a game title and
    add a rating from one to five.

#### Manual testing of New Review
- Trying to add a review without filling out the review field and a message appears to fill out this field. 
- Trying to add a review with less than 20 charachters and a message appears that the text needs to be 20 charachters or more. 
- Trying to add a review without chhosing a rating and a message appers that i need to select one item from the list. 
- Trying to add a review with both field filled out correcttly and the user gets redirected back to the selected game title page,
a flash message appear with the text "review added", the review are added underneath the game title with the rating and the review
gets added to the reviews collection in mongodb.
- Saving the url for the add a review page and tries to access it after logging out and this redirects the user to the log in page.

### Edit Review

#### User stories testing Edit Review

-	I want to be able to edit game reviews that I have already posted.
    -    On the edit review page the user can change a review and rating that has been added by the user. 
- I should not be able to edit the game titles or reviews that others have shared.  
    - On the edit review page there are security so that the user can't edit a review if they aren't a registed user that are logged in to their account, if another user has created that game title or if the title has alrady been deltet fom the db. 

#### Manual testing of Edit Review

- Trying to delete the review and save the changes on the review and a message appears to fill out this field.
- Trying to change the review to be less than 20 characthers and a message appears that the text needs to be 20 charachters or more.
- Trying to edit the review and save the changed and the user gets redirected back to the profile page, a flash message appears with the text "review updated", the review and rating has been changed and the changes gets added to the review in mongodb. 
- Saving the url for the edit review page and tries to access it after logging out and this redirects the user to the log in page.
-  Saving the url for the edit review page as one user and tries to access it after loggin in as a differnt user and this redirects the user to the home page with a flash message "You don't have access to the page you tried to visit" shows.
- Saving the url for the edit a review page for one review that then are deleted and try to access the url and the user gets redirected back to the home page with a flash message "The review you are trying to edit don't exist" shows. 

### New Title 

#### User stories testing New title

- I want to be able to add a new game title. 
    - On the add game title a registred user that are logged in can add a game title to the website. 


#### Manual testing of New Title 

- Trying to add a game title without filling out the title field and a message appears to fill out this field. 
- Trying to add a game title with the title field beeing less than five charachters and a message appears that the text needs to be five charachters or more.
- Trying to add a game title without filling out the image URL field and a message appears to fill out this field. 
- Trying to add a game title without filling out the description field and a message appears to fill out this field. 
- Trying to add a game title with the description field beeing less than 20 charachters and a message appears that the text needs to be 20 charachters or more.
- Trying to add a game title without chosing at least one console and a message appears to select an item from the list. 
- Trying to add a game title without chosing at least one option in coop experience and a message appears to select an item from the list. 
- Trying to add a game title with all field filled out correcttly and the user gets redirected back to the selected game title page,
a flash message appear with the text "Game title added", the game title are added and the game title
gets added to the titles collection in mongodb.
- Saving the url for the add game title page and tries to access it after logging out and this redirects the user to the log in page.
-  Saving the url for the title page page as one user and tries to access it after loggin in as a differnt user and this redirects the user to the home page with a flash message "You don't have access to the page you tried to visit" shows.
- Saving the url for the game title page for one game title that then are deleted and try to access the url and the user gets redirected back to the home page with a flash message "The title you are trying to edit don't exist" shows. 

### Edit Title

#### User stories testing Edit Title

- I want to be able to edit a game title that I have added.
    - On the edit title page the user can make changes on a game title that has been added by the user.
- I should not be able to edit the game titles or reviews that others have shared.  
    - On the edit title page there are security so that the user can't edit a game title if they aren't a registed user that are logged in to their account, if another user has created that game title or if the title has alrady been deltet fom the db. 

#### Manual testing of Edit Title

- Trying to delete the test in title field and save the changes on the game title and a message appears to fill out this field.
- Trying to change the title field to be less than five characthers and a message appears that the text needs to be five charachters or more.
- Trying to delete the text in image URL field and save the changes on the game title and a message appears to fill out this field.
- Trying to delete the text in description field and save the changes on the game title and a message appears to fill out this field.
- Trying to change the description field to be less than 20 characthers and a message appears that the text needs to be 20 charachters or more.
- Trying to take away the choosen consoles and save the changes on the game title and a message appears to select an item from the list.
- Trying to take away the choosen coop experience and save the changes on the game title and a message appears to select an item from the list.
- Trying to edit a game title with all fields filled out and save the changed and the user gets redirected back to the profile page, a flash message appears with the text "title updated", the game title has been changed and the changes gets added to the titles in mongodb. 
- Saving the url for the edit title page and tries to access it after logging out and this redirects the user to the log in page.

### Title

#### User stories testing Title 

- I want to be able to see the reviews and titles that others have posted.
    - On the titles page the user can see all the avalible information on a specific game title and all the reviews that have been added to that specific game title.

#### Manual testing of Title

- Visiting the title page as an anonymous and the button to add a review to the game title don't show. 
. Visting the user as a registered user logged in to teir account and th button to add a review to the game title shows. 
- Clicking on the add review button and this takes the user to the page to add a review to that game title. 

## Responsiveness 

## Browsers 

## Performance with lighthouse 

## Bugs 