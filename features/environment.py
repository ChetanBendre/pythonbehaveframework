import generic.seleniumbase as sb
import generic.base as bb

def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_scenario(context, scenario):
    values = bb.get_section_data_from_ini_file('data.ini', 'test_01')
    sb.launch_browser_app(values[1][1], values[0][1])


def after_scenario(context, scenario):
    sb.capture_screenshot("./logs/screenshots/"+scenario.name+".png")
    sb.close_browser()


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass


def before_all(context):
    pass


def after_all(context):
    pass
