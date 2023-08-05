__all__ = ['QuickJS']

import json
from typing import Any, Callable

from quickjs import Context
from thresult import Result, Ok, Err


class QuickJS:
    '''
    A class to handle context for JavaScript and Python code
    '''
    context: Context


    def __init__(self):
        self.context = Context()


    @Result
    def eval(self, code: str, as_json: bool=False) -> Any:
        '''
        This method evaluates JavaScript code
        '''
        v = self.context.eval(code)

        if as_json and v is not None:
            v = v.json()
            v = json.loads(v)
            
        return v


    @Result
    def get(self, name: str, as_json: bool=False) -> Any:
        '''
        This method gets value from context by variable name
        '''
        v = self.context.get(name)

        if as_json and v is not None:
            v = v.json()
            v = json.loads(v)

        # NOTE: can return undefined as null (None)
        return v


    @Result
    def get_function(self, name: str, as_json: bool=True) -> Any:
        f: callable = self.get(name)

        def wrapped_f(*args) -> Any:
            r: Any = f(*args)

            if as_json and not isinstance(r, (type(None), str, bool, float, int)):
                r = r.json()
                r = json.loads(r)

            return r

        return wrapped_f


    @Result
    def set(self, name: str, value: Any) -> Any:
        '''
        This method set value in context by name
        '''
        v = self.context.set(name, value)
        return v


    @Result
    def add_callable(self, name: str, fn: Callable) -> Any:
        '''
        This method add Python callable in context by name
        '''
        v = self.context.add_callable(name, fn)
        return v


    def set_memory_limit(self, memory_limit: int):
        '''
        This method set memory limit for code
        '''
        self.context.set_memory_limit(memory_limit)


    def set_time_limit(self, time_limit: int):
        '''
        This method set time limit for code
        '''
        self.context.set_time_limit(time_limit)


    def memory(self) -> dict:
        '''
        This method returns context memory used size
        '''
        return self.context.memory()


    @Result
    def import_js_module(self, path) -> Any:
        '''
        This method loads js module in context
        '''
        # load js module source code
        code: str

        with open(path, 'r') as f:
            code = f.read()

        # eval js module source code
        v = self.context.eval(code)
        return v
