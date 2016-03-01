*** Settings *** 
Library  robotpageobjects.Page
Resource	Resources//LoginPage.txt

* Variables *
${non_var}                  ${None}

*** Test Cases *** 
Test login with valid credentials
	Login to the outfittery website "shrishinde86@gmail.com" "Qawzsx!3" "True"
	Test case cleanup

Test login with invalid credentials
	Login to the outfittery website "xyz@gmail.com" "asdasda" "${non_var}"
	Test case cleanup

# This test validates some part of the most basic use case new user can try
Test 'LET'S GO!' link from home page
	validate lets go option
	Test case cleanup

# This test also validates some part of the most basic use case new user can try	
Test 'Register Now' option to register new user
	validate leisure selection alert
	Test case cleanup
	
***** Keyword ****
Test case cleanup
	robotpageobjects.Page.Close