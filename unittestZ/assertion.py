import sys
import traceback
from cStringIO import StringIO

def show_failure():
    s = traceback.extract_stack()
    f = {}
    for e in s[::-1]:
        if 'assert' in e[3]:
            f = e
    print '%s:L%s %s' % (f[0], f[1], f[3])

def fail(msg=None):
    _stderr = sys.stderr
    sys.stderr = _stringio = StringIO()
    raise AssertionError(msg)

def assert_equal(actual, expected, msg=None):
    if actual != expected:
        show_failure()
        print "Actual: %s" % actual
        print "Expect: %s" % expected
        fail(msg)

def assert_not_equal(actual, expected, msg=None):
    if actual == expected:
        show_failure()
        print "Actual: %s" % actual
        print "Expect: %s" % expected
        fail(msg)

def assert_true(expr, msg=None):
    if not expr:
        show_failure()
        print "False"
        fail(msg)

def assert_false(expr, msg=None):
    if expr:
        show_failure()
        print "False"
        fail(msg)

def assert_raises(exception, func, *args, **kwds):
    _stdout = sys.stdout
    sys.stdout = _stringio = StringIO()

    exception_raised = False
    try:
        func(*args, **kwds)
    except exception:
        exception_raised = True
    finally:
        sys.stdout = _stdout
        if not exception_raised:
            show_failure()
            fail(str(exception) + ' not raised')

def untitle(s):
    return s[0].lower() + s[1:]

module = sys.modules[__name__]
setattr(module, 'assert_that', module.__dict__['assert_true'])
setattr(module, 'assert_equals', module.__dict__['assert_equal'])
[setattr(module, untitle(''.join([s.title() for s in k.split('_')])), v)
        for k, v in module.__dict__.items() if 'assert' in k]
