# IITD Forum

IITD Forum is a web-application developed using the Python based Django web framework. It is a multi-user social network, customised to be used by IITD undergraduate students, with a responsive interface created with the Bootstrap framework, and highly adaptive to all screen sizes (Smartphone, Tablet, PC).

<!-All 3 sizes--->

## Developers
* [Archit Bubna](https://github.com/architb12), IIT Delhi
* [Ritvik Gupta](https://github.com/ritvikgupta199), IIT Delhi


## Note 
* This application is not developed, used or endorsed by the Indian Institute of Technology, Delhi. This is an independent project by Ritvik Gupta and Archit Bubna.
* This application is temporarily deployed at http://ritvikgupta199.pythonanywhere.com/.
* Installations required for running the application on a local server are mentioned in the *requirements.txt* file.


## Key Features
The application provides the user with all the fundamental functionalities of a social-network.
### Account creation and setup
The application consists of a secure registration and login system. After signing up, a user can follow an interactive 3-step procedure to setup their profile. The procedure is customised for IIT Delhi undergraduate students. 

<!-set up pics, signup and login form --->

### The Profile Page
<!--Profile  page pic -->
The user may upload a profile picture by simply clicking on their existing profile picture on their profile page. A user may edit any of their credentials, including their username, email, name, bio, date of birth, hostel, department, and password.

The profile page consists of a user's details and a 'bio', which can modified by the user at any time. The profile page also displays all of the posts written by the user.

### Posts
<!-- Post view-->
A user may write a post of upto 5000 characters, which will be visible to all other users on the Forum. 
###### Likes
<!--liker modal-->
A user may 'like' a post by clicking the 'heart' icon at the bottom of the post. The application allows all users to view the number of likes on a post, and the list of users who have liked the post. A user may view the list of likers by clicking on the text that displays the number of likes for the post.
###### Comments
A user may write a comment on any post on the Forum. The comment will be visible to all other users on the Forum. 
###### Deletion
<!---deletion modal -->
A user may delete any of their own posts and comments by clicking on the trash-icon next to the post/comment.
###### Character limit
The character limit for posts and comments are 5000 characters and 500 characters respectively. The application displays a real-time character counter as one enters input into the post/comment creation fields, for the user to check if they are within the limit.
###### Tagging users
<!--screenshot of tag suggestions-->
While writing a post or a comment, a user may tag any user on the Forum by simply typing their username after an '@' symbol. As soon as a user enters the '@' symbol into the input field, real-time tag suggestions appear, which narrow down on the basis of the characters typed by the user after the '@' symbol. The suggestions narrow down on the basis of the appearance of the user's input string in the names/usernames of users registered on the Forum.

### Notifications
<!--View with notifications showing, view with non-zero number on bell icon-->
Notifications are created in two scenarios:
* Every time the user is tagged in a comment/post by some other user.
* Every time another user comments on the user's post

The notifications can be viewed by clicking the bell-icon in the navigation bar, which shows the number of unseen notifications on it. Every time a user clicks on a notification, they are directed to the respective post, where the notification was generated. On visiting the post, all notifications for that user that were generated on this post are marked as 'seen'.
The user may also mark all notifications as 'seen' by simply clicking on the 'Mark all as read' button on the bottom of the notification list. For each user, only the last 10 notifications are stored, and older notifications are deleted.

### Pagination
On each page, the content loads as the user scrolls down to the bottom of the loaded content.

### Search bar
<!--View with search bar open with suggestions-->
A user may access the search bar by clicking on the 'search-icon' on the navigation bar. The search bar allows the user to search for any user registered on the Forum. The search results are shown in real-time, i.e. as the user types into the search bar, and the results appear on the basis of the presence of the input string in the names/usernames of registered users.










