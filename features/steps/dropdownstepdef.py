from behave import given, then
import generic.seleniumbase as sb

iddropdown = "dropdown"


@then(u'select {value} by {selection_type}')
def step_impl(context, value, selection_type):
    element = sb.identify_element('id',iddropdown)
    sb.select_value_from_dropdown(element,selection_type,value)
