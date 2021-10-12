# tw-clone
This is a social media clone by django

# TODO

- [X] Add account app and a custom user model
- [x] Add twit app 
- [x] Create Twit model 
- [x] Create TimeLine view 
- [x] Create timeline.html for TimeLine view
- [x] Fix showing image less twit bug
- [x] Add profile_photo field to User mdoel
- [x] Add profile_photo field to UserAdmin fieldsets
- [x] Add login url to account app 
- [x] Create login.html and styles.css for login page
- [x] Add crispy_forms and widget_tweaks app to project
- [x] Create Twit view at account app 
- [x] Add create_twit.html for Twit view
- [x] Add base.html at templates/twit and set timeLine.html with block in base.html
- [x] Add forms.py at account app and create a form for Twit view
- [x] Change profile picture size and padding at create_twit.html
- [x] Change font at timeLine.html and create_twit.html
- [x] Add templatetags folder at twit app
- [x] Create templatetags/base_tags.py file and Make twit_bar inclusion_tag
- [x] Make twit/partial/create_twit.html 
- [x] Add {% twit_bar %} to base.html at twit folder
- [x] Fix sending twit bug from account/twit url 
- [x] Fix sendign twit from '' url at twit app
- [x] Fix ImageField view in template
- [x] Fix upload image bug
- [x] Fix Login url for authenticated users
- [x] Add Logout option at create_twit.html for account and twits apps
- [x] Add password forget and it's html files and urls
- [x] Add bio field to user model and set it for create_twit.html at account app

# Following and Followrs section

- [x] Add Profile view in account/views.py
- [x] Create base_profile.html 
- [x] Create profile.html for Profile view
- [x] Set profile.html and create_twit.html for extends from base_profile.html
- [x] Fix reverse bug in account/twit page
- [x] Change ordering in TimeLine and Twit views
- [x] Delete Twit view from account.views and it's url from account.urls
- [x] Create following inclusion tag in twit/template_tags/base_tags.py
- [x] Add post def to Profiel view at account.views
- [x] Add follow.html by following base tag to base_profile.html
- [x] Set number of twit in follow.html
- [x] Change following inclusion tag name to follow_info and follow.html to follow_info.html
- [x] Add following inclusion tag to base_tags.py
- [x] Add UserFollowing model to account/models.py
- [x] Change post def in Profile view to handel post req 


# Register 
- [x] Add register.html and activate_account.html 
- [x] Add Registration and activate views in account.views
- [x] Fix new user twit don't showing in timeline
- [x] Fix Redirect to login view by active account success link
- [x] Fix Register.html template showing error's
- [x] Fix default profile photo
- [x] Create Edit profile button in profile.html
- [x] Create Edit profiel page
- [x] update user information by edit_profile.html form

 
