Disclaimer: This repo contains the backend components to your mobile app, so nothing Android related will be in here. 

Overview: There are two interfaces that can be used to modify the database of the app: the Django website and the Spring server API. The Django website is purposely not fully developed, so if you access the localhost address directly the website will return an error. That is intentional as all you need is the admin address, which by default on Django is /admin. (e.g http://127.0.0.1:8000/admin). From there you can directly modify the database by adding, editing and removing entries. The Django website interface should be how students/admin modify the database. 

The Spring server API is an intermediary between the app communicating with the database. You can think of it like how the website utilizes Django as an intermediary to communicate with the database. (The API is critical and should not be removed. Without some form of an API you open the database to major security vulnerabilities.) Similar to how you access different parts of a website by changing the web address, different services of the API are accessed the same way. The Spring server API should be connected to the mobile app.

Technologies Used: Django, Spring, Heroku, IntelliJ, Postman, MySQL

Setting up development: You should follow the Django guides online to get yourself fully acquainted with Django. However, to just get the website running, create a virtual environment on your computer. Download Django. Then start your virtual environment and then navigate to the outermost folder that contains manage.py. In your terminal, type "python manage.py runserver". This should start the development server on localhost. 

The Spring API is trickier to develop for. I used IntelliJ to develop it (which I'll assume here as well) but you can use Eclipse if you want. To start, open the pom.xml file using IntelliJ. Doing so will let IntelliJ that this is a maven project. Once opened, run the MyServer.java file. This should start the Spring API. Although it's possible that you can access the API through a web browser like Chrome, you really should download Postman to test your API. To modify the API, modify the contents of UserController.java in the src folder.

To test your API you need to set up MySQL on your computer as well. To connect it to your Spring Server you need to download a driver (JDBC) and install it.

Technical Side Notes:
-Right now Django and Spring are connected to two different databases. Django uses SQLite while the Spring uses MySQL. You will need to change the Django database to MySQL to ensure compatibility. 
-The other files in the repository are used for deploying on Heroku. It should be just the Procfile and the requirements.txt file.
-