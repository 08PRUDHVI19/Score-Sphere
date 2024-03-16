# Score Sphere

Score Sphere is a project aimed at simplifying the process of accessing and viewing academic results for students at Vignan College. The traditional PDF format for result distribution poses challenges for students, making it difficult to check their grades and SGPA efficiently. Additionally, calculating CGPA is not readily available.

## Problem Statement

Vignan College distributes student results in PDF format, consisting of columns containing student registration IDs, semester subjects, and rows representing each student's grades and SGPA. However, navigating through multiple PDFs to check results for multiple semesters is cumbersome and time-consuming.

## Solution Overview

Score Sphere addresses these challenges by storing all student details and results in a database and providing a user-friendly website interface for accessing this information. Key features include:

- **Ease of Access:** Results can be viewed using a simple URL, accessible anytime, anywhere.
- **Comprehensive Results Viewing:** Students can view all their semester results in a single place on the website, avoiding the need to navigate through multiple PDFs.
- **Downloadable PDFs:** Users have the option to download PDFs containing results for all completed semesters.

## Technologies Used

- **Django:** Django web framework is utilized for building the website and managing backend functionalities.
- **SQLite Database:** SQLite is employed as the backend database for storing student details and results.
- **Pandas:** Pandas library is integrated into Django to facilitate seamless integration of CSV file data into the SQLite database, enabling efficient data manipulation.
- **HTML/CSS/JavaScript:** Frontend development technologies are used for designing the user interface of the website.

## Database Model

The database model for Score Sphere includes the following entities:

         +-----------+     +-------------+
         |  Student  |     |   Semester  |
         +-----------+     +-------------+
         | reg_no    |     | semester    |
         | name      |     | start_year  |
         | email     |     | end_year    |
         +-----------+     +-------------+
              |                   |
              |                   |
              |                   |
              |                   |
              |                   |
              |                   |
              |                   |
         +-----------+     +-------------+
         |   Result  |     |  Course     |
         +-----------+     +-------------+
         |  grade    |     | semester    |
         +-----------+     |  code       |
         |student_id |     |  name       |
         |course_id  |     |  credits    |
         +-----------+     +-------------+
              |                   |
              |                   |
              |                   |
              |                   |
              |                   |
              |                   |
              |                   |
         +-----------+     +-------------+
         | SemResult |     
         +-----------+     
         | SGPA      |     
         | student_id|     
         |semester_id|     
         +-----------+     


## Usage

- Users can search their results with their credentials (registration ID)
- Upon the user registration ID, users can view their semester-wise results, download PDF of their all semesters.



