# FIT9136: Assignment 2 - Student Information Management System

This repository contains the work and materials for Assignment 2 of the FIT9136 unit (Algorithms and programming foundations in Python).

## Project Description
This project involves designing and implementing a Student Information Management System (SIMS) that demonstrates understanding of file handling, classes and methods, as well as testing strategy in Python. The system features multiple user roles (Admin, Teacher, Student), each with varying levels of access to different operations. The application will manage user and unit information through two files, `user.txt` and `unit.txt`, located in the `data` folder.

## Features
### Common Features for All Users
- **Login:** Authenticate users based on their credentials.
- **Exit:** Allows users to exit the application.

### Admin Features
- **Search User Information:** Search for specific user details.
- **List All Users' Information:** Display information of all users.
- **List All Units' Information:** Display information of all units.
- **Enable/Disable User:** Toggle the active status of a user.
- **Add/Delete User:** Manage the user list by adding or removing users.
- **Log Out:** Log out from the admin account and return to the main menu.

### Teacher Features
- **List All Teaching Units Information:** Display information of all units taught by the teacher.
- **Add/Delete a Unit:** Manage the unit list by adding or removing units.
- **List All Students’ Information and Scores of One Unit:** Display student details and scores for a specific unit.
- **Show the Avg/Max/Min Score of One Unit:** Display the average, maximum, and minimum scores for a specific unit.
- **Log Out:** Log out from the teacher account and return to the main menu.

### Student Features
- **List All Available Units Information:** Display information of all available units.
- **List All Enrolled Units:** Display information of units the student is enrolled in (maximum of 3 units).
- **Enroll/Drop a Unit:** Manage unit enrollment by adding or removing units.
- **Check the Score of a Unit:** Display the score for a specific unit.
- **Generate Score:** Generate and display scores.
- **Log Out:** Log out from the student account and return to the main menu.

## User Management
Logging out under Admin, Teacher, or Student accounts will not exit the program. After logging out, the program will return to the main menu and prompt the user to log in again. The program will continue to run until the user chooses to exit the application.

## Project Structure
The project consists of five classes, each defined in a separate Python file, and one main Python file to execute the program:

- **main.py:** The entry point of the application. Manages the main menu and user login.
- **admin.py:** Contains the Admin class with methods for admin-specific operations.
- **teacher.py:** Contains the Teacher class with methods for teacher-specific operations.
- **student.py:** Contains the Student class with methods for student-specific operations.
- **user.py:** Contains the User class, a base class for common user attributes and methods.
- **unit.py:** Contains the Unit class to handle unit-related operations and information.

## Data Files
The application uses two text files to store user and unit information:

- **data/user.txt:** Stores user details such as username, password, role, and status.
- **data/unit.txt:** Stores unit details such as unit code, unit name, and scores.

