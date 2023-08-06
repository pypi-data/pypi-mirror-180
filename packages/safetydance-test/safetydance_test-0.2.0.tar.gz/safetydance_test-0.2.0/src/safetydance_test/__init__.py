# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound


from importlib import import_module
from safetydance import get_context, script, step_data, step_decorator, Step, NestingContext
from safetydance.extensions import enter_step, exit_step


class TestStepPrefix:
    ...


Given = step_data(TestStepPrefix)
When = step_data(TestStepPrefix)
Then = step_data(TestStepPrefix)
And = step_data(TestStepPrefix)


class ScriptedTest(Step):
    def __call__(self, *args, **kwargs):
        __tracebackhide = True
        if self.f is None:
            self.rewrite()
        parent_context = get_context()
        context = NestingContext(parent=parent_context) 
        calling_module = import_module(self.f.__module__)
        effective_TestStepPrefix = \
                getattr(calling_module, 'TestStepPrefix', None) or TestStepPrefix
        test_step_prefix = effective_TestStepPrefix()
        context[Given] = test_step_prefix
        context[When] = test_step_prefix
        context[Then] = test_step_prefix
        context[And] = test_step_prefix
        enter_step(context, self)
        self.f(*args, **kwargs)
        exit_step(context, self)


@step_decorator
def scripted_test(f):
    return script(f, script_class=ScriptedTest)
