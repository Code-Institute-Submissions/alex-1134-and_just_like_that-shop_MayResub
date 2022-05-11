# Milestone Project 4: Backend Development (HTML5, CSS3, JAVASCRIPT, PYTHON, DJANGO, MYSQL)

The aim of this project is to design and build a front- and back-end interactive site that will allow the user to add data to its database. The user should be able to engage with the data and add / edit / delete the data on the site and purchase chosen items.

## Second Hand / Vintage Store
The idesa of this project is a second hand outlet of outfits that three main characters wear in the HBO series "And Just Like That". "And Just Like That" is a continuation of the hit "Sex and The City" tv show and originally this store was supposed to sell outfit from both shows but since the original series finished almost twenty years ago, it was better just to focus on the outfits from the new show.

So the idea is that the owner of the store collects whatever items can be found (from places like eBay, Vestiaire Collective, private collectors etc) and re-sales them on the website. It is quite hard to come across these items (but not impossible because it has been done in real life) therefore all the items in the store have quantity of 1. As the new chapter of the show was airing on HBO, every piece of wardrobe that was worn on it, becamey sold out on the spot.

For each item, the User sees a screenshot from the scene where it was worn and next to it there is a photo of the "real" item.

It is worth noticing that almost all the items that the main characters wear are high fashion, has very high prices on the items. The postal fee is only 2% of the order price but in this case it becomes a lot, however clothes like that cannot be delivered by standard mail, therefore the delivery fee is also used on postal insurance.

Deployed project can be found here: https://ajlt-closet.herokuapp.com/
Admin credentials for the database:
Admin - admin
Password - admin

## User Experience(UX)

        1. Users can access all items choosing by a character, they can also sort them in different ways. Since all items are in quantiny of one and it's a small store, sold items are not removed but kept for display. When rating items from high to low, we saw the unrated items first because they are still avaialable (therefore not rated) and we want to push slaes of them. For the purpose of showing that rating works, I manually changed ratings of some items.

### User Stories

        1. First Time Visitors Goals:
        
            a. A First Time Visitor should be able to identify the purpose of the site by entering the main page which clearly states the purpose that it serves. Purchases can be made with or without registration to The Closet (the shop).

            b. A First Time Visitor should be able to easily navigate through the website's content. The menu is clearly separated from the rest of the content in both desktop and mobiles versions and the Search Bar is available as well.

        2. Returning / Frequent Visitor Goals: 

            a. A Returning Visitor (1) will come back for items if they find them interesting and affortable.

            b. A Returning Visitor (2) will come back to enjoy new contents of The Closet, possibly to buy more items if they can afford it. 

            c. A Returning Visitor (3) will come back for both options 1 and 2. 

### Customer Stories
[Customer Stories](media/customer-stories.jpg)
### Management Stories
[Management Stories](media/management-stories.jpg)
 
 ### Design

    1. Colour Scheme

        Lively colours are used to reflect the vibe of the show and the characters. They always wear design that are "out there".


### Wireframes

* [1](media/wire.jpg)

## Features

* Responsive on all device sizes.
* Interactive elements, will serve its purpose with or without the user's input and engagement.
* Stripe payments


## Technologies used

    Google Fonts
    Font Awesome
    GitHub
    Heroku
    Query 
    Stripe
    MySQL
    AWS
    Bootstrap
    Django


 ### Languages Used

 * HTML
 * CSS
 * JAVASCRIPT
 * Python

## Code Testing

  No errors in the workspace:
  [Warnings](media/warnings.jpg)
    

## Browser Compatibility Testing
  
   * The Website was tested on Google Chrome, Safari, Internet Explorer and Firefox browsers.

   * It was also viewed on different devices such as PCs, mobile phones, different models of iPhones, tablets, iPads and laptops.

   * Hyperlinks were tested



## Manual Testing

  In order to make sure that everything works fine on the website a series of tests was conducted:

   * Every link in both Logged In / Logged Out option was checked
   * New users and stock items were added, removed or edited.
   * Every link on the page was clicked on to make sure they work

    Payments were tested here:

    * [Test 1](media/payment-confirmation.jpg)

    Email servis / password change (emails come from my google account "me.coding.bee@gmail.com")
    * [Test 2](media/password-change.jpg)
    * [Test 3](media/email-confirm.jpg)
    * [Test 4](media/email-confirm2.jpg)

### Existing Bugs

    I had some problems with the register function and everytime when I changed small things to see if it works, I commented the commit "test". That's why there are so many "test" commits - they are commits with very, very small changes, like removing a comma or a word.

    After registering we get redirected to a page that seems to have nothing on it, but there is content under the header. We also get an email asking us to confirm registration:
[check here](media/bug1.jpg), so it works but the problem is that on this one particular page I can't change anything. When I try to    find "confirm-email" in my workspace, I get no results. So that's a feature that needs fixing but the registration functionality itself works. I tried sorting this out in many different ways, contacted Tutoring and since I ran out of time, I can just mention this here in README. 


## Deployment

  The website was deployed on Heroku. In order to do so, I logged into my GitHub account, found the repository and then connected my Gitub account to my Heroku account and deployed it from there.
     
  In order to clone this project and run it locally: 
   * log into GitHub account (using Chrome) 
   * install Gitpod extensions for Chrome 
   * restart the browser
   * go to the project's repository
   * click on the green Gitpod button - this will open a new workspace that will enable to work on the code locally
     
  Due to problems      with Heroku, automatic deploys are not possible these days, therefore these steps have to be followed to deploy a project (f     ound in Code Institute's Slack group):
    * [D eployment 1](media/deploy-1.jpg)
    * [Deployment 2](media/deploy-2.jpg)
   
# # Future Features
 
* UX  improvements for readability
* Ad ding more characters from the show to the website
* C o-operation with the Instagram account where photos were found
* Adding fronted stock managemnt - since the idea of the website is to be a small shop ran by one person, managing in through backend   s eems good enough. If the shop were ever to grow and needed easier navigation - the settings are already there in AWS.
 
##  Credits
  
To create my code I followed the Boutique Ado Project from Code Institute and also I watched the tutorials listed below.
 
htt ps://www.youtube.com/watch?v=yOmxJbZjTnU
ht tps://www.youtube.com/watch?v=M7PR-Qs50EA
h ttps://www.youtube.com/watch?v=41NOoEz3Tzc
 
Creating SKU's: 
https://fitsmallbusiness.com/sku-numbers/
     
     
All the photos in The Closet come from:
https://www.instagram.com/justlikethatcloset/
    
Background photo:
https://www.apartmenttherapy.com/sex-and-the-city-carrie-bradshaw-apartment-2018-259443
    
Additional help:     
https://stackoverflow.com/
https://reddit.com
Code Institute Tutoring 