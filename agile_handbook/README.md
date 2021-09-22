This repository has the simple task of creating an agile way for write
a SELF check-in patiente consult, using register and authentication,
and for the doctor a simple anamnesis, saving the IDs on a data-base, 
improving time when this patient returns other time.

It will basically, at scratch, be a portfolio website written on python's
Django REST Framework, and I wish to finish late octuber 2021, at least
my MVP (Minimum Value Product), updating every day my progress. 

Most of the documentation used for this API can be found at:
https://www.django-rest-framework.org/

My time schedule will follow KANBAN methodology for stipulate new 
assignments, for MVP:

- Use Git for Commit CULTURE:
    + Every successful test attempt, commit to Github's account;
    + If fails attempting any new task for website, push old commit;
    + Create few branches;

- Create Register/Login Page:
    + Identification, unique users;
    + Add permissions for superusers, OnlyRead for normal users;
    + Register rules, password using number, UPCASE, lowcase and $#!;

- Create Pagination | Site Framework:
    + Different pages for different functions
    >>> Front End:
    + HOME PAGE;
    + ABOUT US;
    >>> Back End:
    + REGISTER PAGE;
    + APPOINTING;
    + ANAMNESIS for Doctors;
    + TREATMENT and OBSERVATIONS fields;

- Leading With Appointments:
    + Create a realtime appointment's agenda;
    + Send emails automatically for returning;
    + Try to create a timeline progress;

- Deploy:
    + Finally deploy site using Kubernetes, maybe;


Plans for the future, when I finish my MVP:

----------------- COMING SOON ----------------------