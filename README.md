# FACEPLANT
* build in progress 

## Manual Testing
### Navbar and Footer
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Navbar Logo | Click "FACEPLANT" logo | Returns the user to the home page. | ✓ |
| Navbar Home | Click "Home" | Returns the user to the home page. | ✓ |
| Navbar Register | Click "Register" | Takes the user to the Register page. | ✓ |
| Navbar Login | Click "Login" | Takes the user to the login page page. | ✓ |
| Navbar Logout for authenticated users only | Click "Logout" | Takes the user to the logout confirmation page page. | ✓ |
| Navbar Recipes Dropdown | Click "Recipes" logo | Displays Recipes sub-menu. | ✓ |
| Recipes sub-menu links for guest user | Click links | Takes the user to the relevant pages. | ✓ |
| Recipes sub-menu links for authenticated user | Click links | Takes the user to the relevant pages. | ✓ |
| Navbar small/medium screens | Click the hamburger icon | The Login, Register, Logout and Recipes sub-menu are available and work the same way as on large screens. | ✓ |
| Footer Socials Icons | Click Social Media icons | Each link opens a new tab to the corresponding social media website | ✓ |
| Footer Logo | Click small "FACEPLANT" logo | Takes any user to the home page | ✓ |

### Home Page
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Welcome Greeting banner guest user | Click "Register" button | Takes user to the Register page. | ✓ |
| Welcome Greeting banner guest user | Click "Login" button | Takes user to the Login page. | ✓ |
| Welcome Greeting banner when logged in | Click "Add Recipe" button | Takes user to the Add Recipe page. | ✓ |
| Recipes Feed | Scroll down page | Displays upto six recipes in most recent order. | ✓ |
| Pagination | Click "Next" | If over six recipes in feed, next button appears above footer and takes user to the next page of recipes. | ✓ |
| View Recipe Detail | Click any recipe title | Takes the user to the correct recipe page. | ✓ |
| Responsive layout | Use Smaller Screen | The recipe previews will change from rows to columns on smaller devices | ✓ |

### Add Recipe Page
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Form text input fields required | Click "Submit" button with no text entered in each field | Autoscrolls to highlighted empty input field. | ✓ |
| Form submitted | Enter required text to input fields and click submit | Submitted form returns user to the full recipe details page and displays a success message | ✓ |
| Recipe Image | Click "Choose File" button and upload custom image | The correct uploaded image is displayed in recipe detail. | ✓ |
| Placeholder Image | Do not upload custom image | Placeholder image should be displayed in recipe detail. | ✓ |
| Responsive layout | Use Smaller Screen | All fields can be read and used on smaller devices. | ✓ |

### View Recipe Detail Page
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Display full recipe | Scroll through content | All recipe detail will be diplayed in relevant areas. | ✓ |
| Like counter guest user | Click the "like" icon | Icon should do nothing and like count will not increment | ✓ |
| Like counter logged in user user | Click the "like" icon | Icon should change to a solid color and like count will increment by 1 | ✓ |
| Comment Section guest user | Click the "Register" & "Login" buttons | Buttons should open the corresponding pages | ✓ |
| Comment Section logged in user user | Enter text into the "Leave a comment" box & click "Submit" button | Comment input box should disappear and green comment approval message should appear | ✓ |
| Responsive layout | Use Smaller Screen | Each section will change to columns on smaller devices | ✓ |

### Categories
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Display correct Category recipes | Click Each Category in sub menu | Corresponding Category title banner and only recipes in each category shound be displayed. | ✓ |
| Responsive layout | Use Smaller Screen | The recipe previews will change from rows to columns on smaller devices | ✓ |

### Edit Recipe
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Edit Button exists | View recipe you did not create | No edit button displayed. | ✓ |
| Edit Button exists | View recipe you did create | Edit button will be displayed next to date added. | ✓ |
| Edit Button | Click the "Edit" button | Will take the author of recipe to the edit form with previous data still intact ready for editing. | ✓ |

### Delete Recipe
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Delete Button exists | View recipe you did not create | No delete button displayed. | ✓ |
| Delete Button exists | View recipe you did create | Delete button will be displayed next to Edit button. | ✓ |
| Delete Button | Click the "Delete" button | Will take the author of recipe to the delete confirmation page. | ✓ |
| Delete Confirmation | Click the confirm delete button | Will delete recipe from database, take the user to the all recipes page and display "recipe has been deleted" green success message. | ✓ |

### Authentication
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Register new user | Click "Register" button and enter required information | The registration form is validating automatically if the username is valid and if the passwords match and are valid. Otherwise an error message is shown. | ✓ |
| Login | Click "Login" button and enter username and password | The Login form is validating if correct username and password is entered. Otherwise an error is shown | ✓ |
| Successful registration / login | Finish registration / login process | Temporary success message appears. User is logged in automatically and redirected to homepage which dispalys the signed in user under the Welcome Back message. | ✓ |
| Author access to delete and edit | Add /add or /delete to the url of author owned reipe | Author will have access to the edit and delete pages | ✓ |
| User access to delete and edit | Add /add or /delete to the url of non owned reipe | User will be redirected to a 404 Page | ✓ |
| Unauthenticated user access to Add Recipe | Add /add to the homepage urls | No Add Recipe buttons are viewable in menu or welcome page. If user adds /add to home url they will be redirected to the Sign In page | ✓ |
| Author access to delete and edit | Add /add or /delete to the url of author owned reipe | Author will have access to the edit and delete pages | ✓ |

### 404/500
| Test | Action | Expected Result | Pass |
| ---- | ------ | --------------- | ---- |
| Custom Error Pages  | Access 404/500 page | Both error pages will display styled pages inline with the rest of the site and show a custom "Lost" message with a link to home page. | ✓ |
