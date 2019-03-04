Feature: Home page
  Background:
    Given user has launched "https://the-internet.herokuapp.com" in "chrome" browser

  @hh
  Scenario: verify count links on home page
    Then verify page by "url" as "https://the-internet.herokuapp.com"
    Then verify count of links is 41


#  @cc
#  Scenario Outline: verify linktext on homepage
#    Then verify page by "url" as "<b_name>"
#    Examples:
#    |b_name|
#    |https://the-internet.herokuapp.com|
#    |firefox|
##    |ie     |

