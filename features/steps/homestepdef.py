from behave import given, then


@given(u'user has launched {url} in {browser_name} browser')
def step_impl(context, url, browser_name):
    print(url, browser_name, end=' ')


@then(u'verify page by {assertion_type} as {expected_value}')
def step_impl(context, assertion_type, expected_value):
    print("verify page",end='')
    context.abc = "sdfs"

@then(u'verify count of links is {expected_count}')
def step_impl(context, expected_count):
    print("link count is",end='')


