"""Tests for pytype_extensions."""

import os

from pytype import errors
from pytype.pytd import pytd_utils
from pytype.tests import test_base
from pytype.tests import test_utils


def InitContents():
  with open(os.path.join(os.path.dirname(__file__), '__init__.py')) as f:
    lines = f.readlines()
  return ''.join(lines)


class CodeTest(test_base.BaseTest):

  def CheckWithErrors(self, code: str) -> errors.ErrorLog:
    extensions_pyi = pytd_utils.Print(self.Infer(InitContents()))
    with test_utils.Tempdir() as d:
      d.create_file('pytype_extensions.pyi', extensions_pyi)
      return super().CheckWithErrors(code, pythonpath=[d.path])


class DecoratorTest(CodeTest):
  """Tests for pytype_extensions.Decorator."""

  def test_plain_decorator(self):
    errorlog = self.CheckWithErrors("""
        import pytype_extensions

        @pytype_extensions.Decorator
        def MyDecorator(f):
          def wrapper(*a, **kw):
            return f(*a, **kw)
          return wrapper


        class MyClz(object):

          @MyDecorator
          def DecoratedMethod(self, i: int) -> float:
            reveal_type(self)  # reveal-type[e1]
            return i / 2

          def PytypeTesting(self):
            reveal_type(self.DecoratedMethod)  # reveal-type[e2]
            reveal_type(self.DecoratedMethod(1))  # reveal-type[e3]


        reveal_type(MyClz.DecoratedMethod)  # reveal-type[e4]
    """)
    self.assertErrorRegexes(errorlog, {
        'e1': r'MyClz', 'e2': r'.*Callable\[\[int\], float\].*', 'e3': r'float',
        'e4': r'Callable\[\[Any, int\], float\]'})

  def test_decorator_factory(self):
    errorlog = self.CheckWithErrors("""
        import pytype_extensions


        def MyDecoratorFactory(level: int):
          @pytype_extensions.Decorator
          def decorator(f):
            def wrapper(*a, **kw):
              return f(*a, **kw)
            return wrapper
          return decorator


        class MyClz(object):

          @MyDecoratorFactory('should be int')  # wrong-arg-types[e1]
          def MisDecoratedMethod(self) -> int:
            return 'bad-return-type'  # bad-return-type[e2]

          @MyDecoratorFactory(123)
          def FactoryDecoratedMethod(self, i: int) -> float:
            reveal_type(self)  # reveal-type[e3]
            return i / 2

          def PytypeTesting(self):
            reveal_type(self.FactoryDecoratedMethod)  # reveal-type[e4]
            reveal_type(self.FactoryDecoratedMethod(1))  # reveal-type[e5]


        reveal_type(MyClz.FactoryDecoratedMethod)  # reveal-type[e6]
    """)
    self.assertErrorRegexes(errorlog, {
        'e1': r'Expected.*int.*Actual.*str',
        'e2': r'Expected.*int.*Actual.*str', 'e3': r'MyClz',
        'e4': r'.*Callable\[\[int\], float\].*', 'e5': r'float',
        'e6': r'Callable\[\[Any, int\], float\]'})


class DataclassTest(CodeTest):

  def test_basic(self):
    self.CheckWithErrors("""
      import dataclasses
      import pytype_extensions

      @dataclasses.dataclass
      class Foo:
        x: str
        y: str

      @dataclasses.dataclass
      class Bar:
        x: str
        y: int

      class Baz:
        x: str
        y: int

      def f(x: pytype_extensions.Dataclass[str]):
        pass

      f(Foo(x='yes', y='1'))  # ok
      f(Bar(x='no', y=1))  # wrong-arg-types
      f(Baz())  # wrong-arg-types
    """)


class AttrsTest(CodeTest):
  """Test pytype_extensions.Attrs."""

  def test_attr_namespace(self):
    self.CheckWithErrors("""
      import attr
      import pytype_extensions

      @attr.s
      class Foo:
        x: int = attr.ib()
        y: int = attr.ib()

      @attr.s
      class Bar:
        x: int = attr.ib()
        y: str = attr.ib()

      class Baz:
        x: int
        y: str

      def f(x: pytype_extensions.Attrs[int]):
        pass

      f(Foo(x=0, y=1))  # ok
      f(Bar(x=0, y='no'))  # wrong-arg-types
      f(Baz())  # wrong-arg-types
    """)

  def test_attrs_namespace(self):
    self.CheckWithErrors("""
      import attrs
      import pytype_extensions

      @attrs.define
      class Foo:
        x: int
        y: int

      @attrs.define
      class Bar:
        x: int
        y: str

      class Baz:
        x: int
        y: str

      def f(x: pytype_extensions.Attrs[int]):
        pass

      f(Foo(x=0, y=1))  # ok
      f(Bar(x=0, y='no'))  # wrong-arg-types
      f(Baz())  # wrong-arg-types
    """)


if __name__ == '__main__':
  test_base.main()
