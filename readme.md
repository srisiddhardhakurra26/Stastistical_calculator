# Project 2

For this project, you need to fix 16 tests by running each test individually and fixing the error. Many of the errors
are just the wrong text being displayed or it is not redirecting the user to the proper web page; however, some
errors are more challenging.


## NOTE:  YOU WILL NEED TO RUN THE COMMANDS TO INSTALL:

pip3 install -r requirements.txt (could be pip instead of pip3)
flask db init
flask db migrate -m 'first migration'
flask db upgrade
Submit the link to the repo on GitHub Classroom here.

## DON'T FORGET TO COMMIT YOUR MIGRATION FILES OR IT WILL FAIL!

## How to complete the project

### Fix each test in order by running pytest tests/<replace with name of test>.py

1. test_about_page.py
2. test_index_page.py
3. test_login_bad_password.py
4. test_login_dashboard.py
5. test_login_success.py
6. test_login_user_not_found.py
7. test_logout.py
8. test_profile_controller.py
9. test_profile_model.py
10. test_registration_duplicate_fail.py
11. test_registration_success.py
12. test_sample_authenticated_menu.py
13. test_sample_login_redirect.py
14. test_sample_model.py
15. test_sample_route.py
16. test_sample_unauthenticated_menu.py

## Unit Videos

1. [Project Overview and Instructions](https://youtu.be/KmB3ZhFnsZg)

## When complete your program should work like this:

1. A user goes to the homepage
2. A user clicks on the link for "Calculate Sample"
3. If the user is not logged in they are prompted to login and after login they are redirected to a sample calculation form.
4. The sample calculation form should have a dropdown form control to select the z-score / confidence.
5. Once the user enters the values they should press the submit button and be redirected to a list of sample size calculations that they have previously entered.
