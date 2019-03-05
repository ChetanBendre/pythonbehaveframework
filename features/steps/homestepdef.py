from behave import given, then
import generic.seleniumbase as sb

@given(u'user has launched {url} in {browser_name} browser')
def step_impl(context, url, browser_name):
    print(url, browser_name, end=' ')


@then(u'verify page by {assertion_type} as {expected_value}')
def step_impl(context, assertion_type, expected_value):
    actual_value = sb.get_page_details(assertion_type)
    assert actual_value == expected_value, (actual_value, "is not matching with",expected_value);


@then(u'verify count of links is {expected_count}')
def step_impl(context, expected_count):
    elements = sb.identify_element("tagname","a",True)
    actual_count = len(elements)
    expected_count = int(expected_count)
    assert actual_count == expected_count, (actual_count,"is not matching with",expected_count)


