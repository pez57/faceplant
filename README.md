# FACEPLANT - Plant Based Recipe Community
![Image of responsive home page](media/readme/responsive.png)
 [View site here](https://faceplant-pp4.herokuapp.com/)

---

## About
Are you looking for new vegan recipes so good you'll want to plant your face right in? Then you have come to the right place! 

FACEPLANT is a fully responsive website dedicated to sharing tried and tested recipes with its community. Users can view recipes, submit their own, and leave comments expressing their adoration or adaptions.

---

## Contents

---

## Target Audience
The Faceplant website is targeted toward users with an interest in plant-based, vegan food that want to join a community of like-minded food lovers. 

## Features
### Home Page
Users to the site are immediately greeted with the site logo in the nav bar and a welcome message at top of the loaded page. The nav bar contains the necessary links to access the main features of the site and is stuck at the top of the page so that the user can navigate to these links when scrolling down.

![Image of mobile navbar and submenu](media/readme/mobnav.png)

The Welcome Message for an unauthenticated user displays the website logo, a brief about message and a call to action with a Register and Login button.

![Image of guest welcome message](media/readme/guestwcmmssg.png)

Logged-in users are greeted with a Welcome Back message, logged in as: "user" info, and an "Add Recipe" button replacing the registration buttons.

![Image of logged-in user welcome message](media/readme/userwcmmssg.png)

Below the Welcome Message is the recipe feed which displays all uploaded recipes in the most recent order. Each recipe preview shows a featured image, Author username, recipe title, the date and time of upload, and a like counter.

![Image of recipe preview](media/readme/recipepreview.png)

At the bottom of the page is the footer. This contains social media icon links, a copyright mark, and a small Faceplant logo that takes the user back to the home page.

![Image of page footer](media/readme/footer.png)

### Full Recipe Detail Pages
When a user clicks on the title of a recipe preview they will be taken to the full recipe detail page. The top of the page contains the featured image, title, author username, upload time & date, like button and counter, and the recipe description.

![Image of recipe detail top of page](media/readme/detailtop.png)

The ingredients section contains a list of required ingredients and the servings quantity. The method section is an ordered list of steps to create the recipe. On large displays, these sections are side by side, on medium to small displays they are in columns.

![Image of ingredients and method sections](media/readme/ingmethsect.png)

Logged-in users can submit comments at the bottom of the recipe page. Once the comment is submitted there is a success message notifying the user that their comment has been sent for approval. All comments need approval from the admin before they are published. Approved comments are on display to all users.

![Image of comments section](media/readme/comments.png)

### Add Recipe Page
Authenticated users can add their own recipes to the website. To do this, simply click the Add Recipe button on the homepage or in the Recipes submenu in the navbar.
This will take the user to the recipe form. The form requires all but the image fields to be completed to submit. A placeholder image is used when a user doesn't upload an image or if there is an error during upload.

![Image of recipe form top](media/readme/recipeform1.png)
![Image of recipe form bottom](media/readme/recipeform2.png)

### Category Pages
The recipes are assigned one of four categories chosen by the author: Breakfast, Lunch, Dinner and Sweets. The user can view only the recipes in a selected category by accessing the sub menu in the recipes section of the nav bar. Each category page displays only the recipes assigned to that category in the most recent order.

![Image of lunch category page](media/readme/categorypages.png)

### 404 & 500 Pages
If a user encounters a server error or unknown page they are directed to a custom error page. This page gives the user an "Oops! You are lost" message and a link to go back home.

![Image of error page](media/readme/errorpages.png)

### User Registration, Login & Logout
Users are taken to the selected form which will only be submitted when fields are correctly entered. If the wrong info is entered there will be an error message displayed.

![Image of login page](media/readme/loginform.png)

---

## Design
### Theme
The theme of Faceplant was inspired by modern duotone design and branding for vegan food companies. My design aim was to let the recipe previews and full recipe details be the focal point, with simple modern contrast between navigation and background colors.

### Color Palette

![Image of color palette](media/readme/palette.png)

### Logo
I wanted the branding logo to be a subtle nod to the plant-based theme of the project. To achieve this I used a fontawesome leaf icon colored green from my color palette. I chose the Koulen font for the logo because it looks modern and is uppercase by default which gives an immediate impact.

![Image of logo](media/readme/logo.png)

### Fonts
The two complementary fonts I used were both imported from google.fonts
* Logo - Koulen: Uppercase and impactful
* Text Content - Roboto: Modern and familiar

### Wireframes
I used Balsamiq to draft the layout for the Home page and Recipe Detail page. This helped me scope the amount of content needed to achieve a clean layout with the required content. My final design relates closely to these wireframes.
* Home Page - Includes Nav Bar, Welcome banner and registration buttons, and recipe preview images.

![Home page wireframe](media/readme/homewireframe.png)

* Recipe Detail Page - Includes main image, Ingredients & Method cards, and a comment section.

![Recipe Detail Wireframe](media/readme/recipedetailwireframe.png)

---

## User Experience
### User Stories
* Admin Only
    1. As a site Admin I can login as a superuser so that I can access admin tools. (Must-Have)
    2. As an Admin I can Approve Comments so that I can monitor the context of interaction and keep the site a safe space. (Should-Have)
    3. As a site Admin I can create, read, update and delete posts so that I can manage the site content. (Must-Have)
* Users
    1. As a User I can use the site on any size screen so that the design and UX is consistent on any device. (Must-Have)
    2. As a User I can navigate to previous pages and access home simply so that I can access familiar pages and use the site with ease. (Must-Have)
    3. As a User I can register and login so that I can like, comment and add recipes. (Must-Have)
    4. As a site User I can view recipe previews so that I can choose which recipe to read. (Must-Have)
    5. As a site User I can click on a recipe so I can open the full post and view the full content. (Must-Have)
    6. As an authenticated User I can create a recipe post so that I can create and share my own content. (Must-Have)
    7. As an authenticated User I can edit/update and delete my previous recipes so that I can keep my recipes relevant. (Must-Have)
    8. As an authenticated User I can be notified on screen when I create edit & delete a recipe so that I know there were no errors. (Should-Have)
    9. As an authenticated User I can click one button on the home page to add a new recipe so that I can instantly interact with the site. (Could-Have)
    10. As an authenticated User I can like & unlike recipes so that I can interact with other users' recipes. (Should-Have)
    11. As an authenticated Site User I can comment on a recipe so that I can interact with the faceplant community. (Should-Have)
    12. As a User I can view all recipes so that I do not have to return to the home page every time I want to view all. (Should-Have)
    13. As an authenticated User I can add a category to my recipe so that it can be filtered into the related category. (Should-Have)
---

## Agile
I managed my tasks for this project using the Github kanban Agile project management tool. I created my User Stories labelling them "Must-Have" for strictly necessary tasks, "Should-Have" for desired tasks, or "Could-have" for tasks that are not necessary for the required functionality.
All User Stories started in the "To Do" board, moved to "In Progress", and once completed the User Story was moved to the "Done" board and then marked as issue closed.

![Image of kanban board](media/readme/kanban.png)

The only incomplete User Stories are labelled as Could-Have and will be worked on in the future.

---

Data Model

![Data model graph image](media/readme/datamodel.png)

---

## Manual Testing
### Navbar and Footer
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Navbar Logo | Click "FACEPLANT" logo | Returns the user to the home page. | ✓ |
| Navbar Home | Click "Home" | Returns the user to the home page. | ✓ |
| Navbar Register | Click "Register" | Takes the user to the Register page. | ✓ |
| Navbar Login | Click "Login" | Takes the user to the login page. | ✓ |
| Navbar Logout for authenticated users only | Click "Logout" | Takes the user to the logout confirmation page. | ✓ |
| Navbar Recipes Dropdown | Click "Recipes" logo | Displays Recipes sub-menu. | ✓ |
| Recipes sub-menu links for guest users | Click links | Takes the user to the relevant pages. | ✓ |
| Recipes sub-menu links for authenticated users | Click links | Takes the user to the relevant pages. | ✓ |
| Navbar small/medium screens | Click the hamburger icon | The Login, Register, Logout and Recipes sub-menu are available and work the same way as on large screens. | ✓ |
| Footer Socials Icons | Click Social Media icons | Each link opens a new tab to the corresponding social media website | ✓ |
| Footer Logo | Click small "FACEPLANT" logo | Takes any user to the home page | ✓ |

### Home Page
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Welcome Greeting banner guest user | Click the "Register" button | Takes the user to the Register page. | ✓ |
| Welcome Greeting banner guest user | Click "Login" button | Takes the user to the Login page. | ✓ |
| Welcome Greeting banner when logged in | Click "Add Recipe" button | Takes the user to the Add Recipe page. | ✓ |
| Recipes Feed | Scroll down page | Displays up to six recipes in a most recent order. | ✓ |
| Pagination | Click "Next" | If over six recipes are in the feed, the next button appears above the footer and takes the user to the next page of recipes. | ✓ |
| View Recipe Detail | Click any recipe title | Takes the user to the correct recipe page. | ✓ |
| Responsive layout | Use Smaller Screen | The recipe previews will change from rows to columns on smaller devices | ✓ |

### Add Recipe Page
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Form text input fields required | Click the "Submit" button with no text entered in each field | Autoscrolls to highlighted empty input field. | ✓ |
| Form submitted | Enter required text to input fields and click submit | Submitted form returns the user to the full recipe details page and displays a success message | ✓ |
| Recipe Image | Click the "Choose File" button and upload a custom image | The correct uploaded image is displayed in recipe detail. | ✓ |
| Placeholder Image | Do not upload custom image | Placeholder image should be displayed in recipe detail. | ✓ |
| Responsive layout | Use Smaller Screen | All fields can be read and used on smaller devices. | ✓ |

### View Recipe Detail Page
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Display full recipe | Scroll through content | All recipe detail will be displayed in relevant areas. | ✓ |
| Like counter guest user | Click the "like" icon | Icon should do nothing and like count will not increment | ✓ |
| Like counter logged in user | Click the "like" icon | Icon should change to a solid color and like count will increment by 1 | ✓ |
| Comment Section guest user | Click the "Register" & "Login" buttons | Buttons should open the corresponding pages | ✓ |
| Comment Section logged in user | Enter text into the "Leave a comment" box & click the "Submit" button | Comment input box should disappear and a green comment approval message should appear | ✓ |
| Responsive layout | Use Smaller Screen | Each section will change to columns on smaller devices | ✓ |

### Categories
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Display correct Category recipes | Click Each Category in sub-menu | Corresponding Category title banner and only recipes in each category should be displayed. | ✓ |
| Responsive layout | Use Smaller Screen | The recipe previews will change from rows to columns on smaller devices | ✓ |

### Edit Recipe
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Edit Button exists | View recipe you did not create | No edit button displayed. | ✓ |
| Edit Button exists | View recipe you did create | Edit button will be displayed next to date added. | ✓ |
| Edit Button | Click the "Edit" button | Will take the author of the recipe to the edit form with previous data still intact and ready for editing. | ✓ |

### Delete Recipe
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Delete Button exists | View recipe you did not create | No delete button displayed. | ✓ |
| Delete Button exists | View recipe you did create | Delete button will be displayed next to Edit button. | ✓ |
| Delete Button | Click the "Delete" button | Will take the author of the recipe to the delete confirmation page. | ✓ |
| Delete Confirmation | Click the confirm delete button | Will delete the recipe from the database, take the user to the all recipes page and display "recipe has been deleted" green success message. | ✓ |

### Authentication
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Register a new user | Click the "Register" button and enter the required information | The registration form is validating automatically if the username is valid and if the passwords match and are valid. Otherwise, an error message is shown. | ✓ |
| Login | Click the "Login" button and enter username and password | The Login form is validating if the correct username and password is entered. Otherwise, an error is shown | ✓ |
| Successful registration / login | Finish registration / login process | Temporary success message appears. The user has logged in automatically and is redirected to the homepage which displays the signed-in user under the Welcome Back message. | ✓ |
| Author access to delete and edit | Add /add or /delete to the URL of author-owned recipe | Author will have access to the edit and delete pages | ✓ |
| User access to delete and edit | Add /add or /delete to the URL of non-owned recipe | User will be redirected to a 404 Page | ✓ |
| Unauthenticated user access to Add Recipe | Add /add to the homepage URLs | No Add Recipe buttons are viewable in the menu or welcome page. If user adds /add to the home URL they will be redirected to the Sign In page | ✓ |
| Author access to delete and edit | Add /add or /delete to the URL of author-owned recipe | Author will have access to the edit and delete pages | ✓ |

### 404/500
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Custom Error Pages  | Access 404/500 page | Both error pages will display styled pages inline with the rest of the site and show a custom "Lost" message with a link to the home page. | ✓ |

### Admin
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Admin Panel  | Access Admin panel when signed in as a superuser | Admin has access to all admin tools | ✓ |

### Success Messages
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Success Message JavaScript Function  | Login and add, edit and delete a test recipe | Success message will hide after 5 seconds of successful recipe update | ✓ |

---

## User Story Testing
### Admin:
* As a site Admin, I can login as a superuser so that I can access admin tools.
    * Admin superusers have access to the admin panel via  /admin. There they have full access to admin tools.

* As a site Admin, I can create, read, update and delete recipes so that I can manage the site content.
    * Use the admin panel and click on recipes. This provides the admin with the necessary tools to view, create, edit & delete recipes made by all users.  

* As an Admin I can Approve Comments so that I can monitor the context of user interaction and keep the site a safe space.
    * Within the Comments section of the admin panel, all submitted comments have approved status. To approve comments, select the comment and select “approve comment” from the dropdown menu and click the “Go” button.


### User:
* As a site user, I can register and login to the site so that I can like, and comment on recipes.
    * Users can Register or Login via the nav bar or welcome banner on the home page with one click.
    * The register page requests unique username(required), E-mail(optional) and password.
    * The Login page simply requests a username and password. 
    * Once logged in users can comment & like any recipe.

* As a site User/Admin, I can view posts so that I can choose which recipe to read.
    * All recipes can be viewed by any user via the home page or the View All category in the nav bar menu.

* As a site user, I can click on a recipe & view the full content.
    * Click the title of a recipe, this will take you to the full recipe detail page.

* As a logged-in user/admin, I can like & unlike recipes so that I can interact with recipes.
    * Once logged in the user can click the outlined “like” icon, once clicked the icon becomes a solid colour and the counter adds 1.
    * To unlike, the user can click the “like” icon which reverts to outlined style, and the counter removes 1 from total likes.


* As a Site User/Admin, I can Like and comment on a recipe so that I can interact with the Faceplant community.
    * Once logged in users can comment & like any recipe.

* As an authenticated user I can create a recipe post so that I can create and share my own content.
    * Once logged in, users have access to the “Add Recipe” form.
    * All fields are required and once submitted their recipe is added to the site.


* As a user, I can edit/update and delete my previous recipes so that I can keep my recipes relevant.
    * Once logged in, users can edit only their own recipes. To do this the user has access to the “Edit” & “Delete” buttons on their authored recipe detail pages.
    * The edit button opens the form which can be edited and submitted.
    * The delete button takes the user to a Delete Confirmation page with a “confirm” button. Clicking this will permanently delete the recipe.

* As a user, I can add a tag to the recipe so that the recipe can be filtered into related tags.
    * The category drop-down menu in the Add Recipe form contains each meal category. 
    *The Recipes sub-menu in the nav bar contains the Categories menu which will display only the recipes within that category.

* As an authenticated user I can click one button on the home page to add a new recipe so that I can instantly interact with the site.
    * The “Register” & “Login” buttons on the homepage welcome banner are replaced with the “Add Recipe” button once signed in. This opens the Add Recipe form with one click.

* As a user, I can view all recipes so that I do not have to return to the home page every time I want to view all.
    * The All Recipes option in the nav bar drop-down menu displays all recipes.
    * This page is the redirect page after deleting a recipe.

* As a user, I can be notified on-screen when I create edit & delete a recipe so that I know there were no errors.
    * Success messages appear after a recipe has been created, edited or deleted.
    * These appear at the top of the page and disappear after 5 seconds.

* As a user, I can be directed to a site-styled page not found page when I try to access unauthenticated pages so that I know I am on the Faceplant site.
    * Page not found - If a user tries to access a page that doesn’t exist or they do not have authority to access (deleting another users recipe) they are directed to a page with a “Go Home” button styled with the same base HTML as the rest of the site.

* As a user, I can navigate to previous pages and access home simply so that I can access familiar pages and use the site with ease.
    * The sticky nav bar has a home link and also the Faceplant logo directs users to the home page.
    * The footer also has the faceplant logo which directs back to home.

* As a user, I can intuitively understand what criteria I need to input on the form so that my recipe displays correctly.
    * The form has relevant titles for each input field.
    * The Ingredients and Method input fields have placeholder text prompting the user to use bullet points or a numbered list selectable from the toolbar.

* As a User, I can use the site on any size screen so that the design and UX is consistent on any device.
    * Screen sizes below 1000px wide trigger a hamburger menu icon to appear.
    * The site is responsive and has been tested on multiple screen sizes:
        * Desktop 16:9
        * Ipad air
        * Samsung S20 Ultra
        * iPhone 12pro
        * Google Pixel 6
        * Google Pixel 2

## Validation
### HTML
All custom-written HTML code in my templates file has been tested using: https://validator.w3.org/ 
* Results
    * All custom HTML has no errors and one warning
    * Errors that do occur are caused by generated code within Django templating tags and Summernote

![Image of validation results](media/readme/htmlvalidationwarning.png)

### CSS
CSS was also validated using: https://validator.w3.org/ 
* Results: No Errors or Warnings founds
### Python
All Python code conforms to the pep8 style guide and only linting errors are due to Django.

### Lighthouse
I generated Lighthouse reports in chrome dev tools for the Home, Recipe Detail, and Category pages. All of which had no red warning scores. The performance score is not where I would like it but this is an issue regarding my image sizes and will work on this in the future.

Average mobile score:

![image of lighthouse score](media/readme/lighthouse.png)

---

## Bugs
Chrome Developer tools were used extensively in the project to check and manipulate problems with design, layout and HTML rendering.
### Resolved Bugs
* Add Recipe form submit 404 Page not found.
    * Solution was to use get_success_url method to create the new URL after successful form submission.
* Add Recipe form upload image was not saving.
    * Solution was to add `enctype="multipart/form-data"` attribute to the form.
* Unauthenticated users could access Add and Edit URLs
    * Solution was to use the `LoginRequiredMixin` mixin in my Add, Edit and Delete views.
* Summernote text fields not responsive
    * Solution was to add a custom CSS media query to resize the Iframe for smaller screens. 

### Existing Bug
There is one issue regarding the footer on some pages. The footer can have a blank space below it if the content does not fill the display. I will fix this in the future as it does not interfere with the overall functionality of the application.

---
## Future Improvements
There are further functionality and improvements I would like to implement:
* User profile
    * Users will be able to have their own profile page with a dashboard
    * Links to their own published recipes
    * A favourites section
    * Notifications for likes and comments on their recipes
* Favourites
    * User ability to click a favourite button on recipes
* Styled Admin Page
    * Admin page to reflect the styling of the main site
* Improve Lighthouse Performance Score

---
## Deployment
### Cloning the repository
To clone the repository, follow these steps:

1. Log into Github and open this repo: https://github.com/pez57/faceplant
2. Above the list of files, click on Code, and a dropdown menu is presented with different options.
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be.
6. Type git clone, and then paste the URL copied earlier (step 3).
7. Press Enter to create your local clone.

### Environment Variables
Create an env.py file. The following variables are required for this project:

* SECRET_KEY: "create your own or generate random".
* CLOUDINARY_URL: Copy your CLOUDINARY_URL e.g. API Environment Variable from Cloudinary Dashboard (create a free Cloudinary account [here](https://cloudinary.com/)).
* DATABASE_URL: This is the value of DATABASE_URL in Heroku (step 5 of the next section), located in the Settings Tab, in Config Vars.
* In settings.py change the ALLOWED_HOSTS values to use your localhost and Heroku app name.

### Deploying to Heroku
To deploy to Heroku follow these steps:

1. Log into Heroku and locate the "New" button, on the top right end side of your dashboard page.
2. Click on "Create new app", select your region and pick a name for your project.
3. On top of the next page there is a navigation bar, select "Settings".
4. In "Settings" add buildpack Python.
5. Add Database to App Resources. This is located in the Resources Tab, Add-ons, search and add e.g. "Heroku Postgres".
6. In the Settings Tab, in Config Vars, make sure you have the DATABASE_URL added with the previous step and add the other variables: SECRET_KEY and CLOUDINARY_URL. Make sure you have the same variables here and in your env.py.
7. On the navigation bar on top of the page, select now "Deploy".
8. Select deployment method "Github" and search for your repository.
9. Proceed to link the Heroku app to the repository by clicking on "Connect".
10. Click on Deploy.

---

## Technologies
### Languages
* [Python](https://www.python.org/)
* [JavaScript](https://www.javascript.com/)
* [HTML](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://www.w3schools.com/css/)

### Workspace
* [Gitpod](https://www.gitpod.io/) Was used as my IDE workspace.

### Development Tools & Apps
* [Django](https://www.djangoproject.com/) Framework was used to build this project.
* [Bootstrap](https://getbootstrap.com/) Framework was used to create a responsive front end.
* [allauth](https://django-allauth.readthedocs.io/) Was used to handle authentication.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Was used to control the rendering behaviour of my Django forms.
* [Summernote](https://github.com/summernote/django-summernote) Was used as an improved WYSIWYG editor for some of my form text inputs.
* [Autoslug](https://django-autoslug.readthedocs.io/en/latest/) Was used to generate slugs from the recipe title.
* [Cloudinary](https://cloudinary.com/documentation/django_integration) Used to upload form images and store them remotely.
* [Graphviz](https://graphviz.org/) Was used to produce my data model graph.
* [Postgres](https://www.heroku.com/postgres) Database
* [Heroku](https://django-autoslug.readthedocs.io/en/latest/) Was used to deploy the project.
* https://favicon.io/ Was used to generate the favicon
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) were used extensively to check and test responsiveness and HTML rendering.
* [Google Fonts](https://fonts.google) Supplied my fonts used.
* [Fontawesome](https://fontawesome.com/) Supplied the icons I used in the branding logo and like button.

### Version Control
* [git](https://git-scm.com/) was used to add, commit and push changes to my code.
* [Github](https://github.com/) is where my pushed code is stored.

---

## Credits

### Code
* Code Institute Blog walkthrough 
    * My comment model was adapted from this walkthrough
    * Set up steps and settings configuration

* [VeryAcademy](https://www.youtube.com/c/veryacademy) Youtube channel has many videos I found helpful to give me extra knowledge in understanding models and making my views. I also learned about Django mixins from this channel.

* [Stackoverflow](https://stackoverflow.com/) Was a valuable resource when trying to overcome issues throughout this project. I didn't need to post any of my own problem statements as I found information from previous posts that steered me in the right direction. 

* CI Tutor service helped me overcome: 
    * Issues I had with my database when I changed my model.
    * My uploaded images not being displayed on published recipes.
    * My edit view would not load previously submitted text.

* Bootstrap 
    * Nav Bar Template adapted from [here](https://startbootstrap.com/template/scrolling-nav)
    * Footer Temolate adapted from [here](https://mdbootstrap.com/docs/standard/navigation/footer/)

### Content

* Color Palette image generated by [coolors.co](https://coolor.co)

* Recipe Photos from these free stock photo resources
    * [Pexels](https://pexels.com)
    * [unsplash](https://unsplash.com/)


### Acknowledgements

* I'd like to thank my mentor Reuben Ferrante for his support and valuable feedback throughout this project.
* The CI slack community and Tutor session for the helpful support.
