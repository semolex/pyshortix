# pyshortix
Bootstrap application and set of utils for URL-shortening service.
Demo contains basic functionality to run shortening service - launch it, put valid URL and you will get shortened URL.

Usage:

Go to repository folder.

Create `SQLite` database file and table:

```python utils/create_db.py```

Launch demo application:

```python pyshortix.py```

Now, go to ` http://127.0.0.1:5000/` and you will see page with form for URL submission.

Add some valid URL and now you can use it shortened version.


