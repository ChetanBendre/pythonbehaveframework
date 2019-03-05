Feature: Home page

  @hh
  Scenario: verify count links on home page
    Then verify page by url as https://the-internet.herokuapp.com/
    Then verify count of links is 41
