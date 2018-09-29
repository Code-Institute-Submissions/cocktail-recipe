Cocktails 

The brief was to "Create a web application that allows users to store and easily access cooking recipes"
My girlfriend love drinking cocktails together so that is where the idea for making a cocktail recipe book. 

Many people like cocktails but hear the name and have no idea what's in them. Now they can stored there cocktails 
and it yummy yum or what ever pleases them. 

UX

As the user loads up the page they will see a call to action that will lead them add a recipe page. 
Once they have click add cocktail they brought back to the home page were they can see there new cocktail recipe.
This list does a nice popout from the main page, it will show the name, author and details. 
If the user wishes to edit there recipe they can with a button that will take them to an editing page.
If they wish to delete the recipe they can also do that with a simple click of button.

After the user has added a few recipes they can get a full run down in a form of a pie chart of what the most used
spirts are. 

The cocktail recipes that have been entered and the diffculty level of the coctail came from the below link. 
https://uk.thebar.com/cocktail-recipes 

Features 
The features on this page are as follows. 
    creating a recipe
        A diffculty level
        Allergic to stawberries
        Multple selection of spirts that can be added rather than one. 
    seeing a detailed list of recipes
    The ability to edit and delete recipes
    A pie chart that shows the most used spirts in the lists that have been created. 

Features that could be implemented in the future.
    I would have liked to add some recipes that the user could use as a starting point and 
    remove anything they wished.

Technologies Used 

https://materializecss.com/
    Used for styling and front end such as form building and Jquary set up. 

https://uk.thebar.com/cocktail-recipes
    Cocktail ideas and inspiration for the diffculty setting on the form,
    
https://google.github.io/material-design-icons/
    backing up files 
https://pixabay.com/en/editors_choice/
    Picking free images 
http://jinja.pocoo.org/docs/2.10/templates/#if
    refencing on how to use jinja
https://jsonformatter.curiousconcept.com/
    formmatting my json files in mlab correctly
https://www.chartjs.org/
    Builing my pie chart.
https://code.jquery.com/jquery-3.3.1.js
    To run Jquery 
https://mlab.com/
    The database I used.

Testing
    To ensure each part of the project worked after each edit I would go and test the site. 
    I started by installing Flask so that I could have my page running and use the error messages to see
    where problems came from. 
    Next I installed heroku so that I could send back ups and run my site there too.
    
    With Flask installed I was able to start building a base html page that all other pages would have. 
    Following the way the mini project built its functions with python I went step by step with each function until
    I was happy it was working with out any error.
    
    After the main boilerplate was in I connected mLab to python and cloud9 and set up my json file within it.
    I started with a recipe page that would be the main page and put together a basic list
    structure using materialize.
    
    Once connected I built the basic form page to check that the any form completed would feed into the data base. 
    Then I started filling out the form adding extra parts to it. 
    Adding and edit button to be used for the next stage.
    
    The next stage was the editing page again using the mini projects steps and python code I was able to edit 
    both the list and the data base. The first issue I had with this was I was adding to the list rather than editing.
    My mentor Jim pointed that out and suggested ways to fix it. 
    
    After the editing was completed I added a simple delete button some minor miss speling caused some errors.
    
    Using a tool from materialize called Parallax I put in my base html file so that there would be images on each page 
    that flow under each of function.  
    
    I set to work building a pie chart from chart.js and with the help of some  youtube videos built the chart on its on
    page for testing. The biggest diffculty of the project was linking the data base to the chart as they are two different
    coding structures. Speaking with my mentor Jim he helped me build a function using a for loop and JSON dump to link to
    javascript. As the mlab database is in a simalar format to Javascript I was able to get the chart to read it. 
    the hard part came with getting Javascript to accept the Jinja. Cloud9 may give an error message but the page it self 
    worked because it was accepting the format. 
    
    Once all functions were in place and working I set to getting the page to look more interesting.
    I adding a simple card under the list so the user could find the pie chart easily.
    Adding the tool bar and burger so when the page when reduce down it would work on mobile 

Credits 

Images taken from 
https://pixabay.com/en/editors_choice/

I recieved inspiration from 
Jim Richmond 
Niel 
Gabriela 
