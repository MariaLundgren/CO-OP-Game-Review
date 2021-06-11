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

#### User stories testing footer

- I want to be able to find the website's social channels.
    - In the footer there are links to the website's social media channels.

#### Manual testing of Navbar

- Clicking the Facebook icon brings user to facebook.com in a new browser window.
- Clicking the Instagram icon brings user to instagram.com in a new browser window.
- Hovering over the contact link and social icons to make sure they become lighter when hovering over them.
- This was repeated on all pages to make sure the footer works on every page.

### Home

#### User stories testing Home 

-	I want to be able to search amongst the posts if I am looking for something specific.
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

### Profile

### Edit Profile

### New Review

### Edit Review

### New Title 

### Edit Title

### Title

## Responsiveness 

## Browsers 

## Performance with lighthouse 

## Bugs 