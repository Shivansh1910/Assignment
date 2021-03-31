# Assignment

frontend and backend names are self explanatory

frontend - http://localhost:4200/
backend - http://127.0.0.1:8000/

frontend has seprate register links for both candidate and admin/manager
manager login- http://localhost:4200/#/regm this link can be closed once all managers are registered and from django admin they can be given is_staff/admin permission to make the login in django-admin

Common Login Page for both and as per their features redirected to candidate page or manager page

Manager has ability to add/ modify candidate's name and certificates. Also manager can add certificate of any event. 
Certificate can be empty as well as written text but be in jpg and it should have 1 word or saprated by _ like eureka or eureka_jr not eureka jr. this can be extented to image and other format as well if required.

All Templates uploaded will be saved in media/sample dir of backend with the name of event.jpg

Candidates can download available certificate in pdf format
