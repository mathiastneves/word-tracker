# Word Tracker
#### Video Demo:  <https://studio.youtube.com/video/6dNxK1eDzoM/>
#### Description:

## INTRODUCTION
Word tracker allows parents to track new words spoken by babies/toddlers and when they started speaking them.

## FUNCTIONALITY
Word tracker was built using HTML, CSS, Bootstrap, Flask and SQL.
The functionality is simple - you can add new words and the date when the child started to use it using the main form.
The age is calculated automatically based on the date of birth (using Python's datetime module to generate the total number of months)
The header displays the child's name, age, and total amount of words. These are set in the main app.py file, and inserted dynamically into the template using Jinja.
Jinja is also used for the main table of words - allowing the table to expand as necessary whenever the user adds new words.
This is done using a for loop that iterated through the main SQL table.
All words added by the user are stored in a SQL table - which means that they are stored for later use. This was an important piece of the problem,
as the same table needs to be used for months to track the child's progress.

## IMPROVEMENTS
There are many improvements that can be done in future releases
1) Allowing users to remove or edit words (especially important if one or more words are mispelled)
2) Allow users to create an account and login - which would enable them to access the spreadsheet frm any device
3) Allow the creation of multiple children
4) Potentially using localStorage instead of a SQL database, for a more simple solution

## MOTIVES
Tracking how many words a child is using and by which age is important to identify speech delay, and when an intervention with a speech therapy might be necessary.
Identifying speech delay as soon as possible can help to provide children with the tools they need to achieve expected learning outcomes for their age.

## HOW TO RUN
With all files in place (CSS in the /static folder, index.html in the /templates folder) this can be run using Flask (e.g. flask run) and accessing the main page via the URL provided

## DETAILS
### APP.PY
This is the main file to set up the settings of Word Tracker. You can set up the child's Name and Date of Birth here, which will be implemented in HTML using a Jinja placeholder.
App.py also links to the word-tracker SQL database.
index() is set up for two main cases: GET and POST. If index.html is reached using GET, the page will be rendered displaying the form and table of words.
However if the path is accessed via POST (when the form is submitted), the SQL database will be updated with the form's data.
Before inserting the data into the database, the age is calculated by the difference between the data selected and the child's date of birth (set up as a main variable)

### INDEX.HTML
This is the main html file for the Word Tracker. It contains 3 main sections: a header div displayed at the top, containing the placeholders for name, age and number of words; 2) a form to submit new words; 3) a dynamic table implemented with Jinja and styled with Bootstrap. Index.html also links to Bootstrap and the styles.css stylesheet.

### STYLES.CSS
The main stylesheet for the word tracker. Joyful colors were selected due to the subject matter of the app, while being flexible for kids of any gender. The main headers use a serif font (Georgia) while the remaining content uses Helvetica as a sans serif font. 
