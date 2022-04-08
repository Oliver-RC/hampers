1) Wireframes
2) Update User Stories in github agile kanban board
4) model diagram lucid chart for flow of data
5) include social media sign in (time permitting)
6) fix nav on mobile
7) shopping bag bug - to fix at the end
8) pagination?
9) fix carousel and footer issue
10) product reivews = check if user purchased?
11) add more products
12) Ger support on add button
13) https://extendsclass.com/python-formatter.html


- stripe payment system
- amazon aws services
- django allauth (authorisation functionality)
- favicon.io
- reference boutiquo ado as resource and inspirational project
- jquery for javascript sort functionality


# Celebrate with Hampers

Celebrate with Hamper is an e-commerce website built to showcase their restaurant, allowing a wider target audience to discover what's on offer. There is a page showcasing their menu and latest blog articles. Furthermore users can register up to the site and log in to their account allowing them to 'like' blogs by the restaurant, providing the owners with subtle feedback on which blogs are the most popular. Users can book a table reservation and even sign up to their newsletter email subscription. Whilst signed in, the user is able to see their future table booking and has the functionality to edit, cancel or add.

This is a full-stack project built using Python + Django, HTML, CSS and JavaScript and is for educational purposes. 

![Responsive Mockup](x)

## Showcase

A deployed link to the website can be found [here](x)

## User Experience (UX)

 ### User Stories
 - In the planning stages of the app, I used a UX approach by applying various user stories and the different stages of using the app, to create a list of builds needed to make the application fit for purpose, both for frontend users and backend admin users.
 - I used the Github Projects, Kanban tool as my agile tool to manage the planning and structure of the build.

  #### First Time Visitor Goals
   1. As a first time visitor I want to understand what the site is about and who the site is intended for. Starting with the title and core content of the index page, these elements should give a clear idea.
   2. As a first time visitor I want to be able to clearly navigate around the site knowing which page I am on and what information I should expect to find.
   3. As a first time visitor the flow of each page should read top to bottom with the interactive content following suit. The home / index page should then allow the user to flow onto the next relevant page.
   4. As a first time visitor I want the content to be in a consistent and simple structure from page to page. Navigation bar at the top, main body of the page and footer at the bottom.
   5. As a first time visitor the interactive content should be intuitive and not require content heavy text to explain how to use.
   6. As a first time visitor I want to see specific restaurant content like opening times, directions, the menu, blog and to book a table.
   7. As a first time visitor I do not want to necessarily register as a user to book a table, nor restrict me from signing up to the newsletter or read the blogs.
   8. As a first time visitor I have the option to register and sign up to an account which gives me access to further functionality such as manage bookings or like blogs.
  
  #### Returning Visitor Goals
   1. As a returning visitor I want to know the benefits of registering as a user and then easily see if I am logged in or not. 
   2. As a returning visitor I want to be able to locate the social media links in order to gain further insight and information but delivered through the different platforms: Youtube, Instagram, Facebook and Twitter.
   3. As a returning visitor I want to be able to sign up to the newsletter subscription and received email confirmation confirming that I am signed up.
   4. As a returning visitor having an account I want to be able to book a table reservation but then be able to edit, delete or add bookings to my account and see their status. 
   5. As a returning visitor having an account I want to be able to like the blog posts as I normally would with any other social media blog site.
  
  #### Frequent User Goals
   1. As a frequent user when I return to the site I want to remain logged in to my account so I can quickly navigate to 'my bookings' page enabling a quick view and access to the bookings functionality.
   2. As a frequent user I will be reading more content onsite therefore want the blogs to be clicked into to open up the content to read and on the menu page, to click into the meals to read specific information on each meal.
   3. As a frequent user I want my blog likes to remain at the status I left them last time I was on the site.
   4. As a frequent user I want the restaurant to update the menu meals regularly to keep me interested along with the blog posts so I know the latest news.
   5. As a frequent user as I interact with the sites content I want messages to appear on the page informing me if I have submitted or actioned any details.
  
  #### Admin User Goals
   1. As an admin user I can log in allowing access to the websites backend database.
   2. As an admin user I can view the table bookings made and either approve or delete the booking. 
   3. As an admin user I can view the users who have signed up to the newsletter and/or registered an account.
   4. As an admin user I can add, edit or delete meals from the menu and also add, edit and delete meal categories.
   5. As an admin user I can add, edit or delete blogs. I also have the option to leave as a draft or post to go live on the frontend.
   6. As an admin user I can add, edit or delete different table configurations for the restaurant allowing users to select the correct table.

## Design

 ### Key User Features
  - Responsive site adapting to the screen size with the content not affected.
  - An index page providing the first time users with all the key information needed to know what the site is about.
  - Restaurant menu page outlining the meal choices available with further links to the specific meal page providing more information.
  - Bookings page for all users (signed up or not) to send a table reservation request.
  - Newsletter page for all users to sign up to the restaurants newsletter email subscription.
  - Blog page for users to see the latest blog news sent out by the restaurant.
  - My Bookings page (only for users signed into their account) allowing users to book, edit or cancel table reservations.
  - Registration and Log In/Out page for users to sign up or log in to an account. 
  - Links to external social media pages in the footer so site visitors can navigate (on a different tab) to further restaurant content. 
 
 ### Structure
  - The site is made up of an initial home page, menu page, book now page, newsletter page, blog page, register page, log in page and my bookings page for logged in users.
  - Each page only has the relevant content expected in order to keep the site simple to understand. Every page is in a consistent style, format and layout aiding usability.
  - Bootstrap grid layout system has been used to create a responsive site.
  - Layout design of each page:
    1. Navigation bar at the top with page title to the left and page links to the right.
    2. Rotational uber image under the navigation bar for inspiration and reaffirming to the user it is a restaurant site.
    3. Title of the page and paragraph of text advising the user of the page and its use.
    4. Core content of the page.
    5. Social media footer at the bottom.
    6. Consistent colour scheme throughout each page specifically on the header / nav bar, page link buttons and footer.
 
 ### Colour Scheme
  - Colour scheme of the site designed using: https://coolors.co/
  - The header and nav bar are made up using the leading colour of the site, that being Oxford Blue. Dark Sienna drives the visual presence of the icons onsite, with headings complimented in Charcoal. Both Cadet Blue Crayola and Papaya Whip are supporting colours used sparingly in the lower levels such as blog details.
  - The button colours led by Bootstraps classes with Secondary a leading complimentary choice. Danger colour has been used appropriately with the cancelling of reservation button, likewise 'update reservation' in their Info class colour.
  - Each clickable button or heading link with have hover effects be it underline on heading links or colour change on the buttons. This reinforces the clickable element.
  ![Site Colour Scheme](x)
 
 ### Typography
  - Google Fonts has been used to stylise the text on site with headings and paragraphs complementing each other. Both modern styles with the headings eye catching and paragraphs content clear to read on smaller screens.
  - The [Lilita One](x) font is used for the headings throughout the site with Cursive as the fallback.
  - The [PT Sans Narrow](x) font is used for the content paragraphs of the site with Sans-Serif as the fallback.
 
 ### Imagery
  - Underneath the navigation bar, there is a Bootstrap carousel which rotates through three images. These are focused on served food within a restaurant sitting and provide a visual representation of the website. This is stored in the Cloudinary database.
  - Each menu item is supported with a visual image of the dish supporting user experience. This is stored in the Cloudinary database.
  - Each blog post has a relevant supporting image with ties into the content of the blog. This is stored in the Cloudinary database.
  - Icons feature heavily in the additional 'detail led' card navigation section on the landing page. Again, rather than text heavily and users having to read the information, these icons give an indication of what the heading link, links to. Icons have been sourced from fontawesome.

 ### Admin Database
  - The backend admin database has been created with the restaurants needs at the forefront. Within the project there are four main apps which have been created individually for simplicity and to separate out the tasks and the storing of data.
  - Blog database: to store 'draft' and 'posted' blogs created by the restaurant. Functionality allows to store unfinished blogs, post blogs, delete and update blogs. Also gives customers the option to like each blog.
  - Bookings database: There are two models, one for the restaurant table size choices, the owner can edit, add and delete table sizes to suit whats available and thus allowing customers to book the right table size. The other model for bookings. This is where the admin staff can see the bookings submitted via the form. On here they have the functionality to change the status of the booking to 'confirmed' in order to provide feedback to the customer. The admin staff can also access the customers details if needed to reach out directly to the user who booked the table.
  - Menu database: Two models, one for meal categories for the admin staff to assign categories to meals i.e starter, main or dessert. The option to add categories, amend or delete. Changes here are directly portrayed on the frontend. The second model for adding meals to the menu. The admin staff can publish the meal or leave as draft, whichever is needed. All relevant meal details found here e.g. price, vegetarian option, meal image, which again will directly show on the sites frontend when published. 
  - Newsletter database: The model stores all customers who sign up to the newsletter subscription. Admin staff can view customer name and email data if needed.

## Wireframe
 - Following the initial user stories, design and features. I mocked up the wireframe of the site to incorporate all must have pages and features. 
 - I used a desktop approach for this as it would be the largest screen size to make the content work. Bootstrap grid system helps to flex the content to mobile, so I felt it would be beneficial to design using the most challenging screen size for the project, larger desktop.
   - [Wireframe Link](x)

## Current Features

 ### Navigation Bar
 - A responsive navigation bar featured on all pages of the site. As the width exceeds 992px the burger menu is replaced with the title of the pages. As you hover over the page links, the text colour brightens.
 - This section allows the user to easily navigate from page to page without having to use the back button or relooping back to the home page.
 - If the user is logged in, the 'register' and 'log in' pages will revert to 'my bookings' and 'log out'. The 'my bookings' page is restricted so that only logged in users can see. Likewise when 'log in' changes to 'log out', this is a clear indication to the user of their status (signed in or out).
 
 ![Nav Bar](x)
 
 ### Carousel and Opening Paragraph
 - A carousel image section provides the user with inspirational and relevant content to the reason of the site. The carousel rotates through three images which keeps the user interested and on the site for longer. 
 - Supporting the image carousel is a page header below with supporting text. This is crucial as it informs the user about which page they are on and the reason for the page.

 ![Opening Content](x)

 ### Detail Navigation
 - An additional navigation section has been built into the home page which supports those users who require further information about the features and pages of the site without having to navigation to every page.
 - A title when clicked on navigates to the relevant page, with an underline hover effect. Each page is supported with a relevant icon, again a further reference point, for those users who prefer or need visual hints.

 ![Detail Nav](x)

 ### Latest News
 - A snapshot of the blogs that have been posted by the restaurant. The users who first land on the page will get a feel for the type of blog / news content that comes out from the restaurant without having to navigate to the blog page specifically.
 - This data is stored in the database and is updated when the restaurant admin post a new blog article. 

 ![Latest News](x)

 ### Opening Hours and Directions
 - The final piece of information you would expect from a restaurant site, opening and closing hours along with directions to the restaurant.
 - Google Maps API has been used to generate the iframe map. The user can interact with the map and click to open a new tab to take them directly to Google Maps.

 ![Hours and Directions](x)
 
 ### The Footer
 - The footer section houses icons of the relevant social media platforms available which allows the user to click on, thus directing them to the relevant social page. The link will open up in a new tab as it gives the user the option to remain on the current page or click onto the social media tab that has just opened.
 - The footer encourages the user to keep connected via social media. It also gives the user confidence of the business / brand given the multiple social platforms used.
 - The footer is responsive and featured at the bottom on all four pages. The footer is identical on each page to provide a consistent look and ease of navigation.

 ![Footer](x)
 
 ### Menu Page
 - A Bootstrap accordion component houses all the menu information for the user. The menu categories make up the clickable expand sections which allows the user to only open up the category of food they are interested in. The category heading is also collapsible.
 - Restaurant Admin manage the data shown here to the user. All changes made to both categories or meals will be automatically shown within the accordion.
 - The meal 'view details' button, when clicked on will take the user to the meal detail page showing more information on that specific meal.

 ![Menu](x)

 ### Book Now Page
 - The Book Now page consists of a form that the user will fill in and submit to the restaurant. Once submitted a message will appear advising the user of the table booking submission and how the restaurant will contact you to confirm, be it via phone if not a signed in user, or via 'My Booking' page, reservation status field.
 - If the user misses a required field the form will advise the user that details are needed and only once the form has been completed, will it get submitted to the restaurant.

 ![Book Now](x)

 ### Newsletter Page
 - On the Newsletter page a form is presented and once fully completed and submitted will sign up the provided email address to the restaurants newsletter subscription.

 ![Newsletter](x) 

 - An email will be sent to the address provided by the user to confirm their sign up.
 
 ![Email](x)

 ### Blog Page
 - Restaurant posted blogs are shown to users on the Blog page. Every blog is shown on an individual card with a supporting image, author of the blog from the restaurant, the date of the post, how many likes and a small exert on the content. 
 - Each blog title and exert can be clicked on to take the user to the blog detail page. 
 - If the user is logged in then they will be able to 'like' the blog post on the detail page. This gives the restaurant owners good feedback about which news blogs are liked and those that are not. This in turn will help the restaurant to know what their target audience are interested in hearing about.

 ![Blog](x)

 ### Register, Log In / Out Pages
 - If users create an account it allows them to 'like' blog posts and also gives them additional functionality regarding their table bookings. On all pages, a message will show providing the user with feedback on their actions.
 - The register page presents a form to the user to complete to sign up.
 - The log in page asks for the username and password of the account so the user can sign in and interact with the blogs and future bookings.
 - The log out page allows the user to log out of the site.

 ![Register](x)
 ![Log In](x)
 ![Log Out](x)

 ### My Bookings Page
 - The 'My Bookings' page will show the signed in user, only their bookings made via the 'Book Now' form. 
 - Bookings submitted on the 'Book Now' form when signed in will appear in a table allowing the user to edit or delete their bookings.
 - There is a button to 'Book a Table' for user to navigate to the booking form page allowing ease of navigation for all things bookings.
 - The details of each booking is shown in a table format, more importantly for the user, they will see the status of the booking, and whether its been confirmed by the restaurant.

 ![Bookings](x)
 
 ### Responsive Site
 - The site uses Bootstraps grid layout system to create a responsive site across the various screen sizes. It is a mobile first flexbox grid. Where content flexes it will span down the screen without compromise to the content.
 ### Accessibility
 - The carousel images all have an alt attribute taking into account users who are visually impaired. The site has contrasting background colours to text enabling an easy read. Background button colours have been set to match the relevant pages defined colour. Semantic HTML has been used to support machines to understand the layout of the site. All links have hover over effect.
 
## Features Left to Implement
 - Database functionality on Bookings app:
   - Restrict dates available for the customer, maximum 3 month future bookings.
   - Automated unavailable dates for customers once the maximum number of bookings have been hit.
   - email confirmation sent to the customer once the status of the booking has been updated by the restaurant.
 - Create a customer account page which shows the user their account information, is editable and can be deleted. Also advises if they are signed up to the newsletter subscriptions.
 - Improve user authentication process by introducing forgotten password reset.
 - Newsletter subscription email content to be built into the database allowing the restaurant admin to draft, post and delete content. Once posted the email is sent to the subscribed users.
 - A contact us page for the user to directly get in touch with the restaurant. A standard element on most sites.

## Technologies Used

 ### Languages Used
  - [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [HTML](https://en.wikipedia.org/wiki/HTML5)
  - [CSS](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
 
 ### Frameworks, Libraries & Resources Used
  - Django: the framework used to build the project and apps.
  - Heroku: used to deploy my project and incorporate their postgreSQL resource.
  - Cloudinary: used to store my database images.
  - Bootstrap: used to support the frontend design and responsive layout of the site. Key components used to improve the UX of the site.
  - Google Inspect: used to amend and fix display issues along with reviewing responsive break points on each pages content.
  - Balsamiq: used to create the wireframe during the design process.
  - Gitpod: used for writing the code and using the command line to commit and push to GitHub.
  - Git: used for version control through the gitpod terminal to commit to Git and push to GitHub.
  - GitHub: used to store the projects code after being pushed from Git. Used to host repository.
  - Google Fonts: used to import the 'Lilita One' font with 'Cursive' as the fallback font for the headings and 'PT Sans Narrow' font with 'Sans-Serif' as the fallback font for the content of the site.
  - Google Maps API: used to assign an API to my project for google maps and thus allowing an iframe of the map on my home page.
  - Font Awesome: used for icons in the home page detail navigation section and footer social media links. Needed for site aesthetic and UX purposes.
  - Coloors: used to select the sites colour palette.
  - Pexels: used for blog and meal specific images.
  - Unsplash: used for blog and meal specific images.
  - Free Formatter: Both html and css code was passed through the formatter to beautify and format my code.
  - ami.responsivedesign used to create my responsive design file.

## Testing
 - I used a combination of manual and automated testing to ensure the application works as intended and meets the users demands. Each user story was applied to the testing, checking that first time users, returning users, frequent users and admin users saw and used the site as intended.
 - Whilst understanding my user stories, I used the in-built github projects, kanban board, to identify the key building blocks to my site, which aided my progress throughout the build. This made sure that I developed a site fit for my users and when testing the site, the outcome was as expected.
 - The Kanban board can be found on this [link](x)
 ![Kanban Board](x)
 - The Lucid chart can be found on this [link](x)
 ![Lucid Chart](x)
 
 ### Manual Testing
  - Myself and three other family members tested the application. We used a checklist to check all pages loaded correctly with the content expected, the interactive elements worked as intended i.e. buttons, links etc, the forms submitted and authentication worked. The manual tests throughly assess the code written in html, css, python and javascript. Please see the following manual tests checklist and outcome:
  ![Manual Test Checklist](x)
  [Manual Test Link](x)
  - Examples of manual testing:
   - Booking form valid submission error checked:
   ![Booking form valid submission error checked](x)
   - Booking form valid form submitted message confirming:
   ![Booking form valid form submitted message confirming](x)
   - My Bookings page, delete a booking with secondary ask:
   ![My Bookings page, delete a booking with secondary ask](x)
  - The devices used to test the application on were:
    - Samsung Note 10
    - Samsung S7
    - iphone 10
    - iphone SE
    - Asus 13" laptop
    - Microsoft Surface
    - iPad Mini
  - The operating systems and browsers used to test the application on were:
    - Microsoft operating system
    - iOS operating system
    - Google Chrome
    - Microsoft Edge
    - Firefox
    - Safari
 
 ### Automated Testing
  - I have run a number of automated tests across the views, models and forms files in each app. Whilst my testing was mainly manual based, I wanted to incorporate key automated tests.
  - Within the views I tested each app view loaded the correct page and template.
  - In the forms I checked the data entry and excluded fields worked as intended.
  - I tested the model for the menu and category app, in that it allowed the storing of data and returned the correct string. 

 ### Google Inspect
  - Constantly using Google Inspect in the devtools to check my layout, make amendments, re-check and therefore delivering an end result that fits the brief and user goals. A mobile first design approach with the help of Bootstrap grid system. 
 
 ### Code Validator Testing
  - All of my code has been passed through the necessary validators with no errors.
  
  #### HTML - 
   - All HTML validation was passed through the official W3C validator.
   ![HTML Validation](x)
  
  #### CSS - 
   - No errors were found when passing through the official (Jigsaw) validator.
   ![CSS Validation](x)
  
  #### JavaScript - 
   - JS Hint Checker was used to highlight any functional errors, none returned. Warning about using 'let', with it being available in ES6, however I am happy with my Javascript code functioning as intended.

  #### Python - 
   - PEP8 online check used to check all my python code written in the app. I can confirm all code meets the PEP8 standard and checked through the online tool. I had to remove whitespace from a number of files along with the line of code being too long. 
 
 ### Performance Testing

  #### Lighthouse - 
   - Tested the site on Google Developer Tools Lighthouse for desktop and mobile with good results on both. Performance, accessibility and SEO scored top marks. Best practices at 87 due to browser errors but nothing of concern which impacts the site useability and performance. On mobile, performance dropped to 87 due to image size. I have reformatted and reduced pixel sizes without compromising on desktop performance.
     - Desktop:
       ![Lighthouse Results Desktop](x)
     - Mobile:
       ![Lighthouse Results Mobile](x)
  
  #### Wave - 
   - Tested on [Wave](https://wave.webaim.org/) which helped me with accessibility, making sure my layout and design worked well with screen readers. No errors detected or contrast errors.
   ![Wave](x)
 
 ### Bugs and Fixes
  - When I initially deployed the app to Heroku, the main carousel images in the base.html file did not load nor did many css properties. I had to remove the image files stored in the static folder and upload to cloudinary, then amend the image source link.
  - When reviewing the site content, the images of both the blog detail page and meal detail page would shrink the image to fit. I have changed the viewport height in order to show the images correctly.
  - In the 'My Bookings' page, when using a small screen, the user does have to scroll right to see all the boking details. I have reduced the size of the table however I have not been able to completely change the layout to display vertically. I have used Bootstraps responsive class however, a further fix is needed to improve the UX on this page.
  - Part way through the development when migrating a new model change, it encountered an integrity error. This resulted in having to dumpdata from the other models and saving the information in a json file. I have kept the json data files in the app for safe keeping. 
  - On the home page, latest news feed, the tiles overspill making them look off center on smaller devices. I believe this is a bug as I have tried, max-width, viewport width without any success.
  - The menu page accordion, should normally be displayed open, so the blue hover colour is displayed, however I wanted the accordion to be closed when the page opened so the user could see the menu categories. There is a bug that will not allow me to change the blue hover. A further fix is required to improve the UX.

## Deployment
 - I used Github to manage the development stages, pushing my updated files to the main branch of the repository. It is the Github main branch that has been used to deploy the app through Heroku. Steps below show the process in the deployment stages.

 ### Create, update and Push to main branch in Github
   - The Code Institute gitpod-full-template was used as a template for the application. 
   - Click 'use this template' button to copy and then create your own repository.
   - Once the repository has been created you can then click on the 'gitpod' green button to take you to the development environment whereby you can start coding the app.
   - Any updates to the code will need to be added, committed and pushed to the main branch.
   - Just before you deploy the app to Heroku, you will need to change the DEBUG status in settings to False.
 
 ### Cloning
  - To make a local clone:
   - Log into GitHub or create an account and navigate to the gitpod repository [here](x).
   - Under the repository name, above the list of files, click on a button called 'Clone'.
   - If cloning with HTTPS, make sure HTTPS is underlined and then click on the clipboard icon to copy. Once clicked the icon will turn to a tick.
   - Open your local IDE open the terminal.
   - Change the current working directory to the location where you want the cloned directory to be.
   - Type git clone, and then paste the URL you copied earlier.
   - Press enter to create your local clone. 
 
 ### Hosting on Heroku
  - The site is hosted on Heroku due to the languages used and the database required for the application. The deployed version uses the main branch in the GitHub repository. In order to deploy in Heroku please use the following steps:
   - Log in to Heroku by creating an account or using an existing profile.
   - Click 'new' and create a new app by entering the name of the app and region you work.
   - In the app, go to settings as you will need to set up the relevant config vars. The most important variable is the secret key which keeps your application secure.
   - Navigate to the resource section as you now need to select a database. I used Heroku Postgres.
   - Settings and database complete, now to deploy. Connect heroku to your github repository by going to the deploy tab, Deploy a GitHub branch manually. Chose the branch 'main' and click 'deploy branch' button.
   - Heroku will now build the app. Once the build log has completed, you can then click on 'view' to open up your application.

## Credits
 - When building the application I have constantly had to refer to a number of documents and sites of resource online in order to overcome challenges in my code. Below is a list of credits and resources used.

  - [Code Institue sample README file](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md) helped me to further build my own README.
  - [Code Institue old sample README file](https://github.com/Code-Institute-Solutions/SampleREADME#readme) helped me with additional content to further build my own README.
  - [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) was referenced for the languages used in this project. 
  - [W3schools](https://www.w3schools.com/) for various code information and trouble shooting, especially python.
  - [Django Documentation](https://docs.djangoproject.com/en/4.0/) for various code information and trouble shooting with the Django framework.
  - [Harvester](https://www.harvester.co.uk/) for the initial design and content research of a restaurant app.
  - [Dennis Ivy](https://dennis-sourcecode.herokuapp.com/) Django videos to help go through the framework and understand various key features.

 ## Acknowledgements
  - Brian Macharia - Mentor support. A thank you for your guidance throughout the early build of the project.
  - Code Institue Slack Community - A great resource and helpful community supported me through the challenges encountered.
  - Tutor Support - amazing help from a number of tutors when I really did struggle to overcome the issues myself.

**This project is for educational use only and was created for the Code Institue Portfolio Project 5: E-commerce Applications**