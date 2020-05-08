# IITD Forum

IITD Forum is a web-application developed using the Python based Django web framework. It is a multi-user social network, customised to be used by IITD undergraduate students, with a responsive interface created with the Bootstrap framework, and highly adaptive to all screen sizes (Smartphone, Tablet, PC).

#### Screenshots of the application on all screen sizes:
<!--Screenshots in all screen sizes-->

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Responsive/phone.jpg?raw=true" alt="Phone"
	title="Site on a phone" width="270" height="585" />
  <img src="https://github.com/architb12/collab/blob/master/Screenshots/Responsive/ipad.jpg?raw=true" alt="iPad"
	title="Site on an iPad" width="384" height="512" />
  <br>
  <img src="https://github.com/architb12/collab/blob/master/Screenshots/Responsive/pc.jpg?raw=true" alt="Laptop"
	title="Site on a laptop" width="720" height="450" />

## Developers
* [Archit Bubna](https://github.com/architb12), IIT Delhi
* [Ritvik Gupta](https://github.com/ritvikgupta199), IIT Delhi


## Note 
* This application is not developed, used or endorsed by the Indian Institute of Technology, Delhi. This is an independent project by Ritvik Gupta and Archit Bubna.
* This application is temporarily deployed at http://ritvikgupta199.pythonanywhere.com/.
* There might be some minor glitches in the application hosted at the above url. These are mainly due to the improper deployment of the application at the moment.
* Installations required for running the application on a local server are mentioned in the *requirements.txt* file.
* The admin site for the repository can be accessed from http://127.0.0.1:8000/admin/ on the local server.
* The user credentials for the Admin account are
	* Username : admin
	* Password : adminpassword


## Key Features
The application provides the user with all the fundamental functionalities of a social-network.
### Account creation and setup
The application consists of a secure registration and login system. After signing up, a user can follow an interactive 3-step procedure to setup their profile. The procedure is customised for IIT Delhi undergraduate students. 

#### Screenshots of the Account Creation process:
<!--Set up, signup and login form screenshots-->
<img src="https://github.com/architb12/collab/blob/master/Screenshots/AccountCreation/login.jpg?raw=true" alt="Login"
	title="Login page" width="720" height="450" />
<img src="https://github.com/architb12/collab/blob/master/Screenshots/AccountCreation/signup.jpg?raw=true" alt="Sign Up"
	title="Sign Up page" width="720" height="450" />
<img src="https://github.com/architb12/collab/blob/master/Screenshots/AccountCreation/setup1.jpg?raw=true" alt="Setup"
	title="Setting up the profile" width="720" height="450" />
<img src="https://github.com/architb12/collab/blob/master/Screenshots/AccountCreation/setup2.jpg?raw=true" alt="Setup"
	title="Setting up the profile" width="720" height="450" />
<img src="https://github.com/architb12/collab/blob/master/Screenshots/AccountCreation/setup3.jpg?raw=true" alt="Setup"
	title="Setting up the profile" width="720" height="450" />

### The Profile Page
<!--Profile  page pic -->
The user may upload a profile picture by simply clicking on their existing profile picture on their profile page. A user may edit any of their credentials, including their username, email, name, bio, date of birth, hostel, department, and password.

The profile page consists of a user's details and a 'bio', which can modified by the user at any time. The profile page also displays all of the posts written by the user.

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Profile/profile.jpg?raw=true" alt="Profile"
	title="Profile Page" width="720" height="450" />

### Posts
<!-- Post view-->
A user may write a post of upto 5000 characters, which will be visible to all other users on the Forum. 

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Posts/post.jpg?raw=true" alt="Post"
	title="Post" width="720" height="450" />
  
###### Likes
<!--liker modal-->
A user may 'like' a post by clicking the 'heart' icon at the bottom of the post. The application allows all users to view the number of likes on a post, and the list of users who have liked the post. A user may view the list of likers by clicking on the text that displays the number of likes for the post.

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Likes/likes_pc.jpg?raw=true" alt="Likes"
	title="Likes for a post" width="720" height="450" />

###### Comments
A user may write a comment on any post on the Forum. The comment will be visible to all other users on the Forum. 
###### Deletion
<!---deletion modal -->
A user may delete any of their own posts and comments by clicking on the trash-icon next to the post/comment.

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Delete/delete_pc.jpg?raw=true" alt="Delete"
	title="Delete a post" width="720" height="450" />
  
###### Character limit
The character limit for posts and comments are 5000 characters and 500 characters respectively. The application displays a real-time character counter as one enters input into the post/comment creation fields, for the user to check if they are within the limit.

###### Spam Prevention
In order to prevent spamming, the application does not allow a user to create more than 10 posts or 100 comments within a span of 24 hours.

###### Tagging users
<!--screenshot of tag suggestions-->
While writing a post or a comment, a user may tag any user on the Forum by simply typing their username after an '@' symbol. As soon as a user enters the '@' symbol into the input field, real-time tag suggestions appear, which narrow down on the basis of the characters typed by the user after the '@' symbol. The suggestions narrow down on the basis of the appearance of the user's input string in the names/usernames of users registered on the Forum.

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Tagging/tags.jpg?raw=true" alt="Tagging"
	title="Tagging other users" width="720" height="450" />

### Notifications
<!--View with notifications showing, view with non-zero number on bell icon-->
Notifications are created in two scenarios:
* Every time the user is tagged in a comment/post by some other user.
* Every time another user comments on the user's post

The notifications can be viewed by clicking the bell-icon in the navigation bar, which shows the number of unseen notifications on it. Every time a user clicks on a notification, they are directed to the respective post, where the notification was generated. On visiting the post, all notifications for that user that were generated on this post are marked as 'seen'.
The user may also mark all notifications as 'seen' by simply clicking on the 'Mark all as read' button on the bottom of the notification list. For each user, only the last 10 notifications are stored, and older notifications are deleted.


#### Screenshot of the Notification panel of a user:

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Notifications/notifications.jpg?raw=true" alt="Notifications" title="Notifications of a user" width="720" height="450" />

### Pagination
On each page, the content loads as the user scrolls down to the bottom of the loaded content.

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Pagination/pagination.jpg?raw=true" alt="Pagination" title="New content loads as a user scrolls down" width="270" height="585" />

### Search bar
<!--View with search bar open with suggestions-->
A user may access the search bar by clicking on the 'search-icon' on the navigation bar. The search bar allows the user to search for any user registered on the Forum. The search results are shown in real-time, i.e. as the user types into the search bar, and the results appear on the basis of the presence of the input string in the names/usernames of registered users.

#### Searching for a user:

<img src="https://github.com/architb12/collab/blob/master/Screenshots/Search/search_pc.jpg?raw=true" alt="Search" title="Searching a user" width="720" height="450" />
<img src="https://github.com/architb12/collab/blob/master/Screenshots/Search/search_phone.jpg?raw=true" alt="Search" title="Searching a user" width="270" height="585" />










