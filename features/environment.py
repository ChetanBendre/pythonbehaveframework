def before_step(context, step):
    print("before step",end='')
    context.cc = "chetan"


def after_step(context, step):
    print("after_step step", end='')
    print(context.cc)

def before_scenario(context, scenario):
    print("beofre scenario", end="")


def after_scenario(context, scenario):
    print("after scenario",end="")


def before_feature(context, feature):
    print("before feature",end="")


def after_feature(context, feature):
    print("after feature")


def before_tag(context, tag):
    print("before tag", end="")


def after_tag(context, tag):
    print("after tag",end="")


def before_all(context):
    print("before all",end='')


def after_all(context):
    print("after all", end='')

