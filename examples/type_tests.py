from typing import TypedDict, Unpack, Any, TypeVar, NotRequired
from collections.abc import Iterable, Callable

class SubStruct(TypedDict):
    x: int
    y: int

type POINT = tuple[int, int] | tuple[ int, int, int]

class MyStruct(TypedDict):
    foo: str
    bar: int
    point: SubStruct
    tup: POINT | None

class MyStruct2(TypedDict):
    foo: str
    bar: int
    points: list[POINT]

class Color(TypedDict):
    rgb: tuple[
        int,
        int,
        int,
        NotRequired[int]
        ]

class MyClass(object):
    def __init__(self, **data: Unpack[MyStruct]) -> None:
        self.data: MyStruct = data

    def add(self, *opt: MyStruct) -> None:
        _foo = self.data['point']['x']

        _x = self.data['point']

        self.data['point'] = {'x': 1, 'y':5}

        _combined = self.data['bar']
        _xx = opt
        _yy= opt[1]['foo']

    def add2(self, **opt: MyStruct) -> None:
        _foo = self.data['point']['x']

        _xx = opt['foo']['foo']

    def add3(self, opt: MyStruct) -> None:
        _foo = self.data['point']['x']

        _xx = opt['point']['x']

type TaggedTuple[*Ts] = tuple[str, *Ts]

def decorator[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs)
    return wrapper

class Container[T]:
    def __init__(self, items: Iterable[T] = ()):
        self.items = list(items)

    def __getitem__(self, item: int) -> T:
        return self.items[item]

    def __setitem__(self, key: int, value: T) -> None:
        self.items[key] = value

    def __delitem__(self, key: int) -> None:
        del self.items[key]

    def __iter__(self) -> Iterable[T]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.items})"

def mytest():
    x: SubStruct = { 'x': 5, 'y': 2}
    y: MyStruct = {'foo':'kjl','bar': 10, 'point': {'x': 5, 'y':10}, 'tup': (5, 3, 4)}

    thing: MyStruct2 = {
        'foo': 'test',
        'bar': 10,
        'points': [(5,0),(3,6)]
    }

    clr: Color = Color(rgb=(4, 5, 6, 7))


    for k in thing:
        pts = [k]
        print(f'{k}:')

    test_obj = MyClass(foo='some', bar=10, point={'x': 10, 'y':5}, tup=None)

    test2 = MyClass(foo='ff', bar=5, point={'x':4, 'y':3}, tup=None)

    _thing = test_obj.data['point']['x']

    _rr: Container[int] = Container[int](items=[1])

    _x = len(_rr)

    for www in _rr.items:
        print(www)

    _tt: TaggedTuple[str, str] = ('3', '3', 'xx')

    sfd = _tt[1]

mytest()
