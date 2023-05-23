TL;DR Additional resources, summary of the lecture, homework ideas 

# Additional resources

1. How to create custom template tags and filters [Django docs](https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/)
2. Comprehensive tutorial on templates in [RealPython](https://realpython.com/django-templates-tags-filters/)
3. Django template inheritance article [HERE](https://medium.com/it-paragon/built-templates-views-using-inheritance-in-django-framework-597265eee9ec)
4. Deployment and static files in the [Django docs](https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/) or in this [shiny article](https://hackernoon.com/the-developers-guide-to-preparing-django-applications-for-production-9f2l33kv)
5. Sending emails with Django: [First](https://www.accordbox.com/blog/how-to-develop-responsive-html-email-in-django/) and [Second](https://www.youtube.com/watch?v=A-7vGF_pEss)
6. Docker + Django, mission possible: [Article](https://hackernoon.com/streamlining-your-django-development-environment-with-docker-containers)
7. Django all in one [article](https://www.digitalocean.com/community/tutorials/working-with-django-templates-static-files)

# Lecture summary
   1. MTV - model, template, view
   2. PostgreSQL as persistent relational database vs. Redis as in-memory database
   3. Why HTML is static and can't show the dynamic context?
   4. DTL - Django template language built-in in Django, builds on top of HTML, making it dynamic
   5. Template variables - {{ variable_name }} - coming with peace from the view's context
      1. Naming limitations - no spaces, no dots, no underscores at the start, no pure integers
      2. SSR - server side rendering (parse the template on the server and send the result to the client as html)
      3. CSR - client side rendering (send the template to the client and let the browser parse it)
      4. Access the variable's attributes - {{ variable_name.attribute_name }} vs. variable_name['attribute_name']
      5. Function calls - {{ variable_name.function_name }} (no brackets)
   6. Template filters - {{ variable_name|filter_name }} - can accept arguments
      1. Built-in filters - https://docs.djangoproject.com/en/4.2/ref/templates/builtins/
      2. Custom filters - https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/#writing-custom-template-filters
   7. Template tags - {% tag_name %} - for loops, if statements, csrf_token, url, 
      1. Built-in tags - https://docs.djangoproject.com/en/4.2/ref/templates/builtins/
      2. Custom tags (simple_tag, inclusion_tag) - https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/#writing-custom-template-tags
   8. Template inheritance - {% extends 'base.html' %} - base.html, child templates, blocks
      1. {% block block_name %} - in the base.html
      2. {% block block_name %} - in the child template
      3. include - {% include 'partial.html' %}
   9. Static files - {% load static %} - css, js, images, fonts (incl. settings)
   10. Bootstrap - https://getbootstrap.com/docs/5.0/getting-started/introduction/

### [HINT] To add an app to the project folder
    1. python manage.py startapp <app_name>
    2. move the app folder into the project
    3. open <app_name>/apps.py and change the name to be <project_name>.<app_name>
    4. open settings.py and add the app to INSTALLED_APPS with the same name "<project_name>.<app_name>"
    5. In project/urls.py include the apps urls like `path('opt_prefix/', include("<project_name>.<app_name>.urls"))`


# Potential homework?!

_Hint: see the bottom of the file for project like tasks (after 5)_

1. Task 1:
   1. Open the first link in the additional resources.
   2. Read about custom template tags and filters.
   3. Create a custom template tag that will take a list of strings and return the first 3 characters of each string.
   4. Use it in a template to display the first 3 characters of each string in a list.

2. Task 2:
   1. Create a base.html with block placeholders for the title and the content of the page.
   2. Extend it in all other templates.
   3. Define the title and the content in the child templates (use the same blocks).
   4. Create a partial template with a navigation bar.
   5. Include the partial in the base.html
   6. Create an `inclusion_tag` that will take a list of links and return a navigation bar with the links.
   7. Use the template tag in the partial template to display the links in the navigation bar.

3. Task 3:
   1. Create a view with a template
   2. Create a context that has random True or False value
   3. Create a partial that will display a message if the value is True
   4. Include the partial in the template, but give it a different context name and use it in the partial
   5. Create a template tag that will take a context name and display the message if the value is True

4. Task 4:
   1. Create a view with a template
   2. Extend the base.html in the template
   3. Create a button and style it using Bootstrap
   4. Refactor the button by placing it in a partial template
   5. Include the partial in the template, but give it a parameter for the button text and a background color (as class)
   6. Create a main.js file and include it as static in the template
   7. Add a click event listener to the button
   8. Create a function that will send a GET request to another view
   9. Create a view that will return a JSON response
   10. Create a new paragraph in the template and display the response in it

5. Task 5:
   1. Create a view with a template
   2. Add a random number to the view context in the range of 1-3. Pass it to the template
   3. Create a partial template that will display a message if the number is 1
   4. In the partial template include another partial template
   5. Define a custom simple_tag that will take the number and return a new random value
   6. Use the tag in the most inner partial template to display the new random value

6. Task 6 (mini project):
   1. Create a new project in Pycharm
   2. Create a new app in the project (see the hint in the lecture summary)
   3. Set the urls and create 3 views with templates.
   4. In each view create a context. It should contain:
      1. A list of links (use a common function between the views)
      2. If the user is authenticated (use a common function that will return True or False randomly)
      3. The current time
      4. A random color (use a function that will return a random color from a list)
   5. Create a base.html with a navigation bar
   6. Create a custom template tag that will take a list of links and return a navigation bar with the links
   7. Use the template tag in the base.html
   8. Style it using Bootstrap (use the color in the context)

    When the task is completed, you should have a project with 3 pages that have a navigation bar with links and a random color.
    If the user is authenticated, the navigation bar should have a logout link, otherwise it should have a login link.
    The page content should display the current time and the random color should be used as a background color for the page.
    The text of the page should read: Don't worry, be happy!

7. Task 7 (mini project):
   1. Create a new virtual environment using the terminal (hardcore I know!)
   2. Turn on the virtual environment (use source)
   3. Install Django in the environment
   4. Create a new project in the environment
   5. Create a new app in the project (see the hint in the lecture summary)
   6. Use a docker container for the database + pgadmin
   7. Set the DB settings in the project's settings.py
   8. Create a new database in pgadmin
   9. Create a new view with a template
   10. Create a new context that will contain a list of columns and a list of objects (use a function to generate Client instances - each should have the same properties as the columns)
   11. Create a base.html with blocks for the title, the  and the content. Extend it in the view template.
   12. Create a partial template that will display a table with the columns and the objects
   13. Include the partial in the view template
   14. Style the table using Bootstrap (check the docs for the table class or component)