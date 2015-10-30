1. Run `pip install .` when inside the same directory as `setup.py`

2. Run `django-admin runserver 8080 --settings=widget_customization.settings`

3. In your browser visit `http://localhost:8080/admin/model_select_customized/book/add/`
(The credentials are username=root, password=qwer)

4. Check out the "Authors" select element. 
    You'll see explanations in the code how that was implemented.
    The simpler (and more hackish) customization (that adds `>>><<<`)is done in the admin
    The more complex customization, that adds the age of the author, is done in models.py

5. This is the end result: Notice the `>>><<<` and the `(year)` close to the name of the authors 

![](https://github.com/vladiibine/django-examples/blob/master/admin-gallery/widget_customization/model_select_customized/static/django-example-1.png)
