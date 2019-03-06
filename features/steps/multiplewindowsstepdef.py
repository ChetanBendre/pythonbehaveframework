from behave import given, then
import generic.seleniumbase as sb

cssTextElement = 'h3'

@then(u'click on {linkname} link of windows page')
def step_impl(context,linkname):
    element = sb.identify_element('linktext', linkname)
    sb.perform_action('click',element)


@then(u'switch to another window with title as {window_title}')
def step_impl(context,window_title):
    sb.switch_to_another_window(window_title)


@then(u'verify element text as {expected_value}')
def step_impl(context,expected_value):

    element =sb.identify_element('css',cssTextElement)
    actual_value = sb.perform_action('gettext',element)
    assert actual_value == expected_value

