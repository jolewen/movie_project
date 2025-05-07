# Movie Project
Demo for Movie Project I \& II

## How to run
For all modules when run, the working directory 
is assumed to be project root, i.e. the directory of this README.md and the main.py.
This ensures relative path consistency across all methods, 
as well as easier containerization into Docker. 

## Modules
### movie_storage.py
Layer that manages db interaction as read and write.
This way, the type of db could be switched out without touching 
either CLI or MovieManager logic.
Examples when switching to SQL:
* add_movies would use:
    ```sql
    INSERT INTO table_name (column1, column2, ...)
    VALUES (value1, value2, ...);
    ```
* update_movies would use:
    ```sql
    UPDATE table_name 
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
    ```

### movie_manager
Layer to handle logic on the data.
This encompasses for example validation for the CRUD methods
as well as analytics calculation.
Decouples user interaction, analysis logic and database interactions. 

### cli
Handles input querying from the user, as well as display of results and options.
Is not concerned with the data or database themselves.