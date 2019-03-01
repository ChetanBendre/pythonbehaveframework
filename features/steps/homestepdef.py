from behave import given


@given(u'user has launched {url} in {browser_name} browser')
def step_impl(context, url, browser_name):
    print(url, browser_name, end=' ')

