import sys
import traceback

def show_failure():
    s = traceback.extract_stack()
    f = s[-3]
    print '%s:L%s %s' % (f[0], f[1], f[3])

def assert_equal(actual, expected, msg=None):
    if actual != expected:
        show_failure()
        print "Actual: %s" % actual
        print "Expect: %s" % expected
        if msg:
            print msg

def assert_not_equal(actual, expected, msg=None):
    if actual == expected:
        show_failure()
        print "Actual: %s" % actual
        print "Expect: %s" % expected
        if msg:
            print msg

def assert_true(expr, msg=None):
    if not expr:
        show_failure()
        print "False"
        if msg:
            print msg

def assert_that(expr):
    assert_true(expr)

module = sys.modules[__name__]
setattr(module, 'assert_that', module.__dict__['assert_true'])
[setattr(module, ''.join([s.title() for s in k.split('_')]), v)
        for k, v in module.__dict__.items() if 'assert' in k]
