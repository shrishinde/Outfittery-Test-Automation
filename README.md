# Outfittery-Test-Automation
Write sample test automation for a website with basic automation framework

### About automation framework
1) This makes use of the https://github.com/ncbi/robotframework-pageobjects framework

2) Test code is written in Python 2.7

3) Test cases are tested with Firefox and chrome browser on windows platform but it should work with Linux as well.

### Steps to install the automation framework

$ pip install robotframework-pageobjects

### How to run the automation tests

From inside repository run following command on windows/linux terminal,

pybot -vbaseurl:https://www.outfittery.com -vbrowser:firefox Tests\Test_Login_Page.robot

### Repository Structure
  modules
    -> These include python files with actual test logic and code

  Tests
    -> This includes test list files in which test cases are mentioned

  Resources
    -> This has files with keywords defined for test cases
