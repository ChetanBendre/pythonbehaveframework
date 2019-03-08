Feature: Dropdown page

  @dd
  Scenario: verify count links on home page
    Then verify page by url as https://the-internet.herokuapp.com/
    Then click on Dropdown link of home page
    Then verify page by url as https://the-internet.herokuapp.com/dropdown
    Then select Option 1 by visibletext
    Then select 2 by value
    Then select 1 by index