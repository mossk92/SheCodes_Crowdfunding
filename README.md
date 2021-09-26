# DRF Crowdfunding: Django Project Starter
Backend coding for Crowdfunding app - frontend to come!

## Page Links
    Github Repository:
        https://github.com/mossk92/SheCodes_Crowdfunding
    
    Deployed Project (Heroku):
        https://still-sierra-85574.herokuapp.com/projects/

### Portfolio
    Due
        Sunday 26th September at 11.59pm.

    Description
        Kickstarter, Go Fund Me, Kiva, Change.org, Patreon... All of these different websites have something in common: they provide a platform for people to fund projects that they believe in, but they all have a slightly different approach. You are going to create your own crowdfunding website, and put your own spin on it!

    Project Requirements:
        Starter files are provided for this project. In the first session working on this project, as a class, we will go through those starter files and get everyone’s project up and running. Part 1 and Part 2 also have setup steps that we will do as a class. We strongly recommend that you refrain from starting Part 1 or Part 2 until after we have completed the setup in class.

    Submission Requirements:
        Please submit the following:
            ● A link to the GitHub repository containing the code for your project.
            ● A link to the deployed project.
            ● A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
            ● A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
            ● A screenshot of Insomnia, demonstrating a token being returned.
            ● Step by step instructions for how to register a new user and create a new project (i.e. endpoints andbody data).
            ● Your refined API specification and Database Schema.

#### App Details
    Name:       CrowdMentor
    Tagline:    Linking dreamers with achievers
    Purpose:    Providing a platform to advertise development areas that 
                users are looking to improve on (such as soft skills, 
                leadership, physical work, technical work etc.)
    Audience:   Project Owners - Those with specific skill sets to develop
                Crowdfunders: Those with skills and time to mentor/tutor
    Exchange:   Reward based – not financial, funders are volunteers
    Example:    Project Owner: User adds a project that says they are looking 
                to learn Python with a specific interest in being able to build 
                a game
                Crowdfunders: Search by their skills to find a match that they are comfortable with. They can then pledge time to assist (such as 4x 1hr sessions)

##### Features
    Existing:
        ● Create Account
            - Including Name
            - Including Biography
            - Date automatically generated
            - Authorised User can change details
            - Authorised User can delete profile
        ● Create Project
            - Limited only to users
            - Including location
            - Including category
            - Date automatically generated
            - Authorised User can change details
            - Authorised User can delete profile
            - Sum of all pledges
        ● Create Pledge
            - Limited only to users
        ● Admin Page
            - Able to access Users
            - Able to access Projects
            - Able to access Pledges       

    Still to come:
        ● Search functionality
            - By active projects
            - By category
            - By description
            - By location
        ● Way for pledgers to connect to project owners and vice versa
            - I.E direct message 
        ● Responsive design for web and mobile
        ● Optionality for Pledgers to organise masterclasses by sending request to a group of project owners with similar categories
        ● Setting goal to either time (hr) which is the default but also give option for date where a pledge has to commit all (e.g commit to assisting to meet that goal)

###### Screenshots
    ● GET Requests:
<img width="942" alt="Heroku_GET_Users_All" src="https://user-images.githubusercontent.com/86653337/134788998-86087af6-acc7-463a-8e73-ed5669003d70.png">
<img width="942" alt="Heroku_GET_Users_Specified" src="https://user-images.githubusercontent.com/86653337/134789006-2fe685f5-03c6-424d-a718-78ba6fb757ea.png">
<img width="942" alt="Heroku_GET_Projects_All" src="https://user-images.githubusercontent.com/86653337/134789009-84c1368b-b669-4456-b402-e491ce5bdec7.png">
<img width="942" alt="Heroku_GET_Projects_Specified" src="https://user-images.githubusercontent.com/86653337/134789010-f710e1cb-33cc-4448-8c7c-77e819d02db0.png">
<img width="942" alt="Heroku_GET_Pledges_All" src="https://user-images.githubusercontent.com/86653337/134789013-a5a5746f-b523-4d1a-9a4d-82304f69fbfd.png">
<img width="942" alt="Heroku_GET_Pledges_Specified" src="https://user-images.githubusercontent.com/86653337/134789017-30d29bbc-24cc-4895-b83f-10cc01a2f264.png">

    ● POST Requests:
<img width="942" alt="Heroku_POST_Users" src="https://user-images.githubusercontent.com/86653337/134789034-a85efa32-8f68-4128-b384-6300aca38044.png">
<img width="942" alt="Heroku_POST_Token" src="https://user-images.githubusercontent.com/86653337/134789037-54a8ae56-478b-4eb2-b85b-4dbf91bd74de.png">
<img width="942" alt="Heroku_POST_Projects" src="https://user-images.githubusercontent.com/86653337/134789040-b0129c69-5144-4b80-a1d7-899f554e40eb.png">
<img width="942" alt="Heroku_POST_Pledges" src="https://user-images.githubusercontent.com/86653337/134789043-914e1ba6-ed98-4c84-ac8b-f95b40e3db5c.png">

    ● PUT Requests:
<img width="942" alt="Heroku_PUT_Users" src="https://user-images.githubusercontent.com/86653337/134789054-9783c19a-d53f-4aec-bf40-6188ab024805.png">
<img width="942" alt="Heroku_PUT_Projects" src="https://user-images.githubusercontent.com/86653337/134789055-c4183797-71fd-44f3-bc2b-69dd200b7e2f.png">

    ● DELETE Requests:
<img width="942" alt="Heroku_DEL_Pledges" src="https://user-images.githubusercontent.com/86653337/134789063-fac26af7-3f6f-4c45-8620-6a894b2a7a05.png">
<img width="942" alt="Heroku_DEL_Projects" src="https://user-images.githubusercontent.com/86653337/134789066-9bd8f182-2370-4dc9-ba32-457e50d6f7e0.png">
