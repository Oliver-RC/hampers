13) https://extendsclass.com/python-formatter.html
- django allauth (authorisation functionality)
- reference boutiquo ado as resource and inspirational project


# Celebrate with Hampers

Celebrate with Hampers is an e-commerce gift shop website for customers seeking to buy gifts for all occasions online. Our USP is that you can not buy these products anywhere else online as they are hand made specifically for the Celebrate with Hampers customer. 

Site users can browse the full product range and purchase items without creating an account. Users who wish to register for an account will be able to save items, post a review on products, save default payment and delivery information and refer back to their previous order history. 

Store owners and site administrators have full CRUD ability to create, edit and remove products from the application, manage stock and product availability, sensor check customer reviews and remove from site and access customer orders.

To test the checkout and card payment functionality, use: 
postal code: 12345
card number: 4242 4242 4242 4242 
expiry date: 04/24
CVC: 242 42424

This is a full-stack project built using Python + Django, HTML, CSS and JavaScript and is for educational purposes. 

![Responsive Mockup](x)

## Showcase

A deployed link to the website can be found [here](https://celebrate-with-hampers.herokuapp.com/)

## User Experience (UX)

 ### User Stories
 - In the planning stages of the application, I used a UX approach by applying various user stories and the different stages of user journeys which helped me to create a list of builds needed to make the application fit for purpose, both for frontend users and backend admin users.
 - I used the Github Projects, Kanban tool as my agile tool to manage the planning and structure of the build. [found here](https://github.com/Oliver-RC/hampers/projects/1)
 - I also documented my key project tasks on excel whilst brainstorming site functionality aligning to my user stories. [found here](x)

  #### First Time Visitor Goals
   1. As a first time visitor I want to understand what the site is about and who the site is intended for. Starting with the title and core content of the home page, these elements should give a clear idea and provide inspiration to purchase products available.
   2. As a first time visitor I want to be able to clearly navigate around the site knowing which page I am on and what information I should expect to find.
   3. As a first time visitor the flow of each page should read top to bottom with the interactive content following suit. The home page should then allow the user to flow onto the next relevant page.
   4. As a first time visitor I want the content to be in a consistent and simple structure from page to page. Navigation bar at the top, main body of the page and footer at the bottom.
   5. As a first time visitor the interactive content should be intuitive and not require content heavy text to explain how to use.
   6. As a first time visitor I want to see specific product details such as an image of the item, price, description.
   7. As a first time I want to see a link to a social media page to gain further information about the business.
   8. As a first time visitor I have the option to register and sign up to an account which gives me access to further functionality such as saving items, saving user details, order history, making reviews on the products.
   9. As a first time visitor I want to make a purchase either as a guest or signed up user.
   10. As a first time visitor once a purchase is made I want to receive a confirmation email to the email address provided.
  
  #### Returning Visitor Goals
   1. As a returning visitor I want to register for an account so I can save my personal details enabling a faster checkout.
   2. As a returning visitor I want to be able to sign up to the newsletter subscription.
   3. As a returning visitor and signed up user I want to be able to leave a review on products.
   4. As a returning visitor and signed up user I want to be able to save products in my saved item list to refer back to. 
   5. As a returning visitor and signed up user I want to be able to see my previous order history.
  
  #### Site Owners / Admin User Goals
   1. As an admin user I can log in to the admin site allowing access to the applications backend database.
   2. As an admin user I can view the signed up registered users.
   3. As an admin user I can view the orders placed by all customers and their details, including delivery info, products bought and total spend.
   4. As an admin user I can add, edit or delete products listed on the site both on the backend or frontend view, plus add, edit or delete their relevant categories and occasions.
   5. As an admin user I can review each product and its stock levels which changes based on customer purchases. I can make the product available on site or not based on stock availability.
   6. As an admin user I can see the reviews made on certain products by which registered account and set its status on whether to show onsite or not.

## Design

 ### Business Model
  - This application is a B2C e-commerce gift store designed with a simple and minimalist format making the products and all images take centre stage. A consistant and user friendly interface.
  - All products are hand crafted and only available on Celebrate with Hampers which is a key USP.

 ### Supported Marketing and SEO
  - Alongside the website, a Facebook Business page has been set up. It can be viewed [here](https://www.facebook.com/Celebrate-with-Hampers-101236122565796)
  ![Facebook Screenshot](x)
  - There is functionality for users of the webite to sign up to a subscription mailing service. I have used [Mailchimp](https://mailchimp.com/). As a site owner, you have the ability to see who has signed up, their audience, and the capability to set up new campigns too. [Mailchimp Audience example](x)
  - Search engine optimisation has been used by creating a sitemap.xml and robots.txt file. Added to the base.html file includes keywords, both short and long and a meta title:
  ![keywords](x)

 ### Structure
  - Responsive site adapting to the screen size with the content not affected.
  - A home page providing the first time users with all the key information needed to know what the site is about.
  - An all products page listing all the products available to buy and a subsequent product details page telling the user more specific product information.
  - Further navigation showing products by user need states, either by product category or occasion.
  - A search bar allowing users to find specific products by key search terms.
  - A saved item list showing users their selected saved items as they have been browsing the site.
  - A bag page showing users which items they have added to their bag ready to make a purchase.
  - Registration and Log In/Out page for users to sign up or log in to an account.
  - An account page showing users their personal details and order history.
  - A checkout page giving users the ability to make a purchase.
  - A newsletter subscription service, provided by mailchimp so user can receive montly newsletters including exclusive offers.
  - Links to external social media pages in the footer so site visitors can navigate (on a different tab) to further content. Facebook business page created, [found here](https://www.facebook.com/Celebrate-with-Hampers-101236122565796)
  - Each page only has the relevant content expected in order to keep the site simple to understand. Every page is in a consistent style, format and layout aiding usability.
  - Bootstrap grid layout system has been used to create a responsive site.
  - Typical page design and layout:
    1. Site title and logo to the left, search bar in the middle of the screen and key user pages to the right.
    2. Navigation bar at the top.
    3. Title of the page so the user knows which page they are on.
    4. Core content of the page.
    5. Subscription sign up on the left of the footer, Social media links in the middle and card logos and privacy policy on the right adhering to GDPR.
    6. Consistent colour scheme throughout each page as the user goes on their shopping journey.
 
 ### Framework and Database
  - The Django framework has been used to build the application due to its 'batteries included' ability. The integrated [Allauth](https://django-allauth.readthedocs.io/en/latest/) application has allowed me to set up site authentication and registration.
  - During the development stage, SQLite was used as it is provided with Django, however once deployed and hosted on Heroku, Postgres was used. Both being relational databases which was required for this project.
  - The models created and used to generate the database are:
    - User - built in Django model to store users basic information
    - UserProfile - to store and update default user details for ordering
    - Category - to associate a category to a product
    - Occasion - to set the occasion to a product
    - Product - the product and its details
    - Reviews - to allow users to provide a review on a product
    - SavedListItems - to save items for users
    - Order - an order is created once a user makes a purchase storing the required information
    - OrderLineItem - a model to hold the specific ordered product information
  - My relational database model below was create with [Lucidchart](https://lucid.co/product/lucidchart)
  ![lucidchart](x)
 
 ### Colour Scheme
  - Colour scheme of the site designed using: https://coolors.co/
  - A simple 4 colour site which results in the product images and prodcuts themselves standing out off the white page. The logo and brand icon in purple with all text in grey. Black font colour for all navigation and headings to stand our as direction elements on the site.
  - Additional standard bootstrap colours have been used on messages and admin links such as edit and delete products.
  ![Site Colour Scheme](x)
 
 ### Typography
  - Google Fonts has been used to stylise the text on site with only one text styled being used for simplicity. That being the Merriweather font with serif as backup if browsers do not support the main font choice.
  - [Merriweather](https://fonts.google.com/share?selection.family=Merriweather:wght@700)
 
 ### Imagery
  - Images on site are key and what should be grabbing the users eye. They provide inspiration and should give the user enough detail to know what the product is.
  - Underneath the navigation bar, on the home page, there is a Bootstrap carousel which rotates through three images. These provide a visual representation of the website.
  - Every listed product should have an image, if not there is a fallback png file. 
  - Icons feature on the brand logo and within the navigation category and occasion elements. They provide visual backup of the related information shown. Further examples being a heart icon shown on the saved item button, a basket shown on the bag page link and the account page has a human outline logo. Icons have been sourced from [Fontawesome](https://fontawesome.com/).

## Wireframe
 - Following the initial user stories, design and features. I mocked up the wireframe of the site to incorporate all must have pages and features. 
 - I used a desktop approach for this as it would be the largest screen size to make the content work. Bootstrap grid system helps to flex the content to mobile, so I felt it would be beneficial to design using the most challenging screen size for the project first.
   - [Wireframe Link Desktop](x)
   - [Wireframe Link Mobile](x)

## Current Features

 ### Page Header
 - A responsive page header featured on all pages of the site. As the width exceeds 992px the burger menu is replaced with the title of the site on the left. In the middle is the search bar and on the right includes page links for 'my account', 'saved items' and bag page linking through to checkout. Underneath is a small welcome message to either a guest or signed in user name.
 - If the user is logged in, the 'my account' drop down menu changes from 'register' and 'log in' to 'account details' and 'log out', if you are a superuser / admin user you will also have the option of 'product management'.
 
 ![Page Header](x)
 
 ### Navigation Bar
 - A responsive navigation bar featured on all pages of the site. As the width exceeds 992px the burger menu is replaced with the page options. As you hover over the page links, the text colour deepens.
 - This section allows the user to easily navigate from page to page without having to use the back button or relooping back to the home page.
 - Shopping users main reason to buy decided the navigation links to show. You either want to see 'all products' or shop by 'category' or by a specific occasion. I believe the type of occasion is the main reason to buy mindset, therefore this has been split our on the nav bar into 'birthdays', 'anniversarys', 'thank you', 'celebration' and 'seasonal'.
 - Included in the navigation bar is a block heading advising the site user of the cost of delivery. An important factor when shopping online.
 
 ![Nav Bar](x)
 
 ### Carousel and Opening Paragraph
 - A carousel image section provides the user with inspirational and relevant content to the reason of the site. The carousel rotates through three images which keeps the user interested and should provide inspiration to go and shop. 
 - Supporting the image carousel is a page header below with supporting text. This is crucial as it informs the user about the site if the images are not enough. Supported with a anchor button taking the user to the product page.

 ![Carousel](x)

 ### Latest Products
 - A section showcasing 4 of the newest prodcuts available on the site. These are ranked by created date and will automatically update as new products are added into the database.
 - This will keep returning shoppers interested as they will see new items on the initial landing page. It will also bring seasonality into the store as we go through the year.
 - All 4 products can be clicked on taking the shopper to the relevant product detail page.

 ![Latest Products](x)
 
 ### The Footer
 - The footer is responsive and featured at the bottom on all pages.
 - On the left is an email signup form giving site users the option to subscribe to monthly newsletters.
 - The middle advises of site copyright and below lists icons of the relevant social media platforms which allows the user to click on, thus directing them to the relevant social page. The link will open up in a new tab as it gives the user the option to remain on the current page or click onto the social media tab that has just opened. A specific Facebook Business page has been created.
 - On the right of the footer are icons of leading payment providers giving the user subtile information that the site is transactionable. Underneath is the privacy policy conforming to GDPR legislation.

 ![Footer](x)
 
 ### All Products Page
 - A page to show all products listed on the site. 
 - Key information shown to the user about how many products on the page, sort by options drop down box and each of the product tiles.
 - Within the drop down of the 'all products' page, are links to 'by price', 'by occasion' and 'by category' which automatically sorts the products by the chosen page. 

 ![All Products](x)

 ### By Category Page
 - A drop down menu for the user to navigate to the cateogries available, be it 'seasonal', 'alcohol', 'chocolate', 'pamper' or 'baby and kids'.
 - Each page link is a filtered version of the all products page. Only products will be shown that are relevant to the category selected.
 - Key information shown to the user about how many products on the page, a link back to the products home page, sort by options drop down box and each of the product tiles.

 ![Category](x)

 ### Occasion Pages
 - For all occasions, a separate navigation link is provided as I beleive this is the key reason to buy mindset. 
 - Each page link is a filtered version of the all products page. Only products will be shown that are relevant to the occasion page selected.
 - Key information shown to the user about how many products on the page, a link back to the products home page, sort by options drop down box and each of the product tiles.

 ![Occasion](x) 

 ### Search Page
 - When a site user enters a search term into the search bar, the application with search for the relevant keyword across the products listed, be it in the title, category, occasion or description. 
 - The results will be shown once the search icon it clicked, or enter pushed.
 - Key information shown to the user about how many products on the page and the search term used, a link back to the products home page, sort by options drop down box and each of the product tiles.

 ![Search](x)

 ### Product Detail Page
 - When the user clicks on the product image they are taken to the product detail page. Here lists specific information about the product including a description, price, category listed, occasion listed, star rating, add to saved items button, quantity button, keep shopping button, add to bag button and reviews section.
 - Depending on if the user is logged in, the saved items button will either be displayed if logged in, or will state, 'sign in to add to saved items'. 
 - Likewise, if the user is signed in, they will be shown a review form to submit a review on the product. This will not be shown if onyl browsing as a guest.

 ![Product Detail](x)

 ### My Account = Register, Log In / Out Pages
 - If you are a guest / logged out user, the register page will apear in the drop down menu under 'My Account'. On here is a form for to the user to complete to sign up.
 - Once completed the registration form, an email will be sent to the address provided to authenticate the user. Click to link in the email to confirm.
 - The user can now log in using the log in page.
 - Once logged in, the log out page will be shown in the drop down menu under the 'My Account' navigation menu.

 ![Register](x)
 ![Registration Email](x)
 ![Log In](x)
 ![Log Out](x)

 ### My Account = Account Details
 - The key benefit of being a signed up user is the ability to store default delivery information and see you previous order history. 
 - The user can update their saved delivery information by clicking the 'update information button'.
 - The user is also able to click on any order number which takes them to the confirmed order details relevant to that order.

 ![Account Details](x)
 ![Order Details](x)

 ### My Account = Product Management
 - If the user is an admin / superuser of the application then a Product Management page will be shown under the My Account drop down menu. This is a frontend page allowing users to add new products into the database. More user friendly than going into the Django Admin pages.

 ![Product Management](x)

 ### Saved Items Page
 - To access the saved items page and use this functionality of the application, the user needs to be signed in to their account.
 - This page displays a list of all products selected to 'save item'. The save item button is shown on the product details page.
 - To un-save the item, a button is displayed on both the product details page, only if the item is already in the list, and on the saved items page.
 - If no products are in the saved items list then a message will appear on the saved items page.

 ![Saved Items - Nothing](x)
 ![Saved Items](x)

 ### Shopping Bag
 - As site users add products to their bag for purchase, these items are listed on the shopping bag page.
 - This page displays the list of products to be purchased along with the item price, quantity in the bag and subtotal.
 - The user has the option to update the quantity of the items in the bag or to remove completely. 

 ![Bag](x)

 ### Checkout
 - Once the user clicks through to the 'Secure Checkout' page, they will be shown a form to complete on the left, asking for delivery and payment information.
 - On the right of the page is a final summary of the products being purchased, their subtotal cost, delivery cost and grand total.
 - A 'Complete Order' button allows users to submit the form and make the purchase. Any incorrect data will through an error message, which is displayed to the user.
 - A successful checkout will advance the user onto the checkout success thank you page showing the user their confirmed order. A subsequent email is also sent to the users provided email address.

 ![Checkout](x)
 ![Checkout Success](x)
 ![Checkout Email](x)

 ### Onscreen Prompt Messages
 - Whilst navigating the site, there are various onscreen messages that will appear in the top right corner of the page.
 - These messages will be shown on user interactions with the site. For example a success checkout or items added to bag:

 ![Messages-1](x)
 ![Messages-2](x)

 ### Site Admin
 - The backend admin of the site allows store owners and admin users to manage the applications data.
 - Users setting and access level can be defined, customer orders viewed and edited, the full product CRUD management of the store, managing stock levels and product availability and managing customer reviews.

 ![Admin](x)

 ### Responsive Site
 - The site uses Bootstraps grid layout system to create a responsive site across the various screen sizes. It is a mobile first flexbox grid. Where content flexes it will span down the screen without compromise to the content.
 
 ### Accessibility
 - The carousel images all have an alt attribute taking into account users who are visually impaired. 
 - The site is minimilist by design allowing images to be the focal point. Text secondary colour has been used along with black to stand out off the white background page colour supported with brand purple in places.
 - Semantic HTML has been used to support machines to understand the layout of the site. 
 - All links have hover over effect.
 
## Features Left to Implement
 - Improve product content by incorporating multiple images and video of the product giving the shoppers more information about their potential purchase.
 - Limit only users who have bought the product to create a review, improving the feedback to other shoppers. As it stands, all logged in users can add reviews showing functionality is there, but in a real world scenario, you would only want customers to review who have bought the product.
 - For store owners and admin users, include a stock alert for when the stock count number drops below a set figure. This giving the owners a prompt to order more stock in before the line goes out of stock.
 - Add a blog page to the site which generates better interaction between the store and its customers. It keeps the content of the site up to date and refreshed whilst engaging with the current and new site users.
 - Better SEO and marketing of the site to improve the google search ranking. 

## Technologies Used

 ### Languages Used
  - [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [HTML](https://en.wikipedia.org/wiki/HTML5)
  - [CSS](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - [jQuery](https://en.wikipedia.org/wiki/JQuery)
 
 ### Frameworks, Libraries & Resources Used
  - Django: the framework used to build the project and apps.
  - Heroku: used to deploy my project and incorporate their postgreSQL resource.
  - Amazon AWS Services: S3 Bucket to store media and static files for the deployed site.
  - Stripe: used to process the user payments and handle webhooks.
  - Bootstrap: used to support the frontend design and responsive layout of the site. Key components used to improve the UX of the site.
  - Facebook Business Pages: used to create the Facebook business page of the site.
  - Mailchimp: used for the subscription service designed for monthly newsletters to signed up users.
  - Google Inspect: used to amend and fix display issues along with reviewing responsive break points on each pages content.
  - Balsamiq: used to create the wireframe during the design process.
  - Lucidchart: used to brainstorm and design the database models of the site.
  - Gitpod: used for writing the code and using the command line to commit and push to GitHub.
  - Git: used for version control through the gitpod terminal to commit to Git and push to GitHub.
  - GitHub: used to store the projects code after being pushed from Git. Used to host repository.
  - Google Fonts: used to import the main font for the project.
  - Font Awesome: used for all icons across the application. Needed for site aesthetic and UX purposes.
  - Coloors: used to select the sites colour palette.
  - Favicon: used for the favicon of the application.
  - Unsplash: used for carousel and product images
  - Free Formatter: Both html and css code was passed through the formatter to beautify and format my code.
  - ami.responsivedesign used to create my responsive design file.

## Testing
 - I used a combination of manual and automated testing to ensure the application works as intended and meets the users demands. Each user story was applied to the testing, checking that first time users, returning users and admin users saw and used the site as intended.
 - The databse models also formed part of the testing making sure the application functioned as needed.
 - Whilst understanding my user stories, I used the in-built github projects, kanban board, to identify the key building blocks to my site, which aided my progress throughout the build. This made sure that I developed a site fit for my users and when testing the site, the outcome was as expected. In the initial stages of design, I brainstormed using an excel spreadsheet.
 - The Kanban board can be found on this [link](x)
 ![Kanban Board](x)
 ![Excel User Stories](x)
 - The Lucid chart can be found on this [link](x)
 ![Lucid Chart](x)
 
 ### Manual Testing
  - Myself and three other family members tested the application. We used a checklist to check all pages loaded correctly with the content expected, the interactive elements worked as intended i.e. buttons, links etc, the forms submitted and authentication worked, payment system processed correctly and successful email sent. The manual tests throughly assess the code written in html, css, python and javascript. Please see the following manual tests checklist and outcome:
  ![Manual Test Checklist](x)
  [Manual Test Link](x)
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
  - A limited number of automated testing has taken place, checking that the home, product and bag page loads as intended.
  - Further automated tests would have been necessary if it were not for the substantial and endless manually testing conducted across the various platforms, devices and systems.

 ### Google Inspect
  - Constantly using Google Inspect in the devtools to check my layout, make amendments, re-check and therefore delivering an end result that fits the brief and user goals. A mobile first design approach with the help of Bootstrap grid system. 
 
 ### Code Validator Testing
  - All of my code has been passed through the necessary validators with no errors.
  
  #### HTML - 
   - All HTML validation was passed through the official W3C validator. Only errors and warnings shown are to do with the implementation of the Django templating language.
   [HTML Validation](https://validator.w3.org/)
  
  #### CSS - 
   - No errors were found when passing through the official (Jigsaw) validator.
   ![CSS Validation](x)
  
  #### JavaScript - 
   - JS Hint Checker was used to highlight any functional errors, none returned.

  #### Python - 
   - PEP8 online check used to check all my python code written in the app. I can confirm all code meets the PEP8 standard and checked through the online tool. I had to remove whitespace from a number of files along with the line of code being too long.
   - I also used a [Python Formatter](https://extendsclass.com/python-formatter.html) which checked pep8 compliant and supported me to beautify my code.
   - Flake8 was also run in the terminal to see any issues.
 
 ### Performance Testing

  #### Lighthouse - 
   - Tested the site on Google Developer Tools Lighthouse for desktop and mobile with good results on both. Performance and SEO scored top marks for desktop with Accessibility disappointing only due to the search button using a logo instead of text which hinders screen readers performance. On mobile, performance dropped to 75 due to image size and not next gen format. I have reformatted and reduced pixel sizes without compromising on desktop performance however have been unable to improve the score.
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