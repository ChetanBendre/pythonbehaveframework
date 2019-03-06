Feature: Multiple Windows page

  @mw
  Scenario: verify count links on home page
    Then verify page by url as https://the-internet.herokuapp.com/
    Then click on Multiple Windows link of home page
    Then verify page by url as https://the-internet.herokuapp.com/windows
    Then click on Click Here link of windows page
    Then switch to another window with title as New Window
    Then verify page by url as https://the-internet.herokuapp.com/windows/new
    Then verify element text as New Window
