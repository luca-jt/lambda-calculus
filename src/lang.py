# basics
Y = lambda f: ((lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y))))
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
ZERO = lambda f: lambda x: x
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)

def to_numeral(number):
    if number == 0:
        return ZERO
    else:
        return SUCC(to_numeral(number - 1))


# cons list
CAR = lambda p: p(TRUE)
CDR = lambda p: p(FALSE)
CONS = lambda h: lambda t: lambda f: f(h)(t)
HEAD = lambda l: CAR(CDR(l))
TAIL = lambda l: CDR(CDR(l))
LIST = CONS(TRUE)(TRUE)

INSERT_FRONT = lambda l: lambda e: CONS(FALSE)(CONS(e)(l))
IS_EMPTY = lambda l: CAR(l)
APPEND = Y(lambda f: lambda l: lambda e: IS_EMPTY(l)(lambda _: INSERT_FRONT(l)(e))(lambda _: CONS(FALSE)(CONS(HEAD(l))(f(TAIL(l))(e))))(TRUE))
REVERSE = Y(lambda f: lambda l: IS_EMPTY(l)(lambda _: LIST)(lambda _: APPEND(f(TAIL(l)))(HEAD(l)))(TRUE))
MAP = Y(lambda f: lambda p: lambda l: IS_EMPTY(l)(lambda _: LIST)(lambda _: INSERT_FRONT(f(p)(TAIL(l)))(p(HEAD(l))))(TRUE))
RANGE = Y(lambda f: lambda a: lambda b: GTE(a)(b)(lambda _: LIST)(lambda _: INSERT_FRONT(f(SUCC(a))(b))(a))(TRUE))
REDUCE = Y(lambda f: lambda r: lambda l: lambda v: IS_EMPTY(l)(lambda _: v)(lambda _: f(r)(TAIL(l))(r(HEAD(l))(v)))(TRUE))
FILTER = lambda f: lambda l: (REDUCE(lambda x: lambda xs: f(x)(APPEND(xs)(x))(xs))(l)(LIST))
LENGTH = lambda l: REDUCE(lambda x: lambda n: SUCC(n))(l)(ZERO)
INDEX = Y(lambda f: lambda n: lambda l: (IS_ZERO(n)(lambda _: HEAD(l))(lambda _: f(PRED(n))(TAIL(l)))(TRUE)))
MERGE = lambda a: lambda b: IF_THEN_ELIF_THEN_ELSE(IS_ZERO(LENGTH(a)))(b)(IS_ZERO(LENGTH(b)))(a)(IF_THEN_ELSE(LT(HEAD(a))(HEAD(b)))(INSERT_FRONT(MERGE(TAIL(a))(b))(HEAD(a)))(INSERT_FRONT(MERGE(a)(TAIL(b)))(HEAD(b))))
DROP = lambda n: lambda l: n(TAIL)(l)
TAKE = Y(lambda f: lambda n: lambda l: (OR(IS_EMPTY(l))(IS_ZERO(n))(lambda _: LIST)(lambda _: (INSERT_FRONT(f(PRED(n))(TAIL(l)))(HEAD(l))))(TRUE)))

# boolean algebra
IF_THEN_ELSE = lambda b: lambda x: lambda y: b(x)(y)
IF_THEN_ELIF_THEN_ELSE = lambda b: lambda x: lambda p: lambda y: lambda z: IF_THEN_ELSE(b)(x)(IF_THEN_ELSE(p)(y)(z))
NOT = lambda b: IF_THEN_ELSE(b)(FALSE)(TRUE)
AND = lambda p: lambda q: p(q)(FALSE)
NAND = lambda p: lambda q: AND(NOT(p))(NOT(q))
OR = lambda p: lambda q: p(TRUE)(q)
NOR = lambda p: lambda q: OR(NOT(p))(NOT(q))
XOR = lambda p: lambda q: AND(OR(p)(q))(NOT(AND(p)(q)))
IMPL = lambda p: lambda q: OR(NOT(p))(q)
EQUIV = lambda p: lambda q: AND(IMPL(p)(q))(IMPL(q)(p))


# numbers
IS_ZERO = lambda n: n(lambda x: FALSE)(TRUE)
GTE = lambda a: lambda b: IS_ZERO(MINUS(b)(a))
LTE = lambda a: lambda b: IS_ZERO(MINUS(a)(b))
GT = lambda a: lambda b: IS_ZERO(MINUS(SUCC(b))(a))
LT = lambda a: lambda b: IS_ZERO(MINUS(SUCC(a))(b))
MIN = lambda a: lambda b: LTE(a)(b)(a)(b)
MAX = lambda a: lambda b: GTE(a)(b)(a)(b)

NUMBER = lambda n: to_numeral(n)
ONE = NUMBER(1)
PLUS = lambda m: lambda n: m(SUCC)(n)
MINUS = lambda m: lambda n: n(PRED)(m)
MULT = lambda m: lambda n: lambda f: m(n(f))
DIV = Y(lambda f: lambda a: lambda b: LT(a)(b)(lambda _: ZERO)(lambda _: SUCC(f(MINUS(a)(b))(b)))(ZERO))
MOD = Y(lambda f: lambda a: lambda b: LT(a)(b)(lambda _: a)(lambda _: f(MINUS(a)(b))(b))(ZERO))
IS_EVEN = lambda n: IS_ZERO(MOD(n)(NUMBER(2)))
IS_ODD = lambda n: NOT(IS_EVEN(n))
EXP = lambda m: lambda n: n(m)
FACTORIAL = FAC = Y(lambda f: lambda n: IS_ZERO(n)(lambda _: ONE)(lambda _: MULT(n)(f(PRED(n))))(ZERO))
FIB = Y(lambda f: lambda n: LTE(n)(NUMBER(2))(lambda _: ONE)(lambda _: PLUS(f(PRED(n)))(f(PRED(PRED(n)))))(ZERO))
IS_EQUAL = lambda m: lambda n: AND(GTE(m)(n))(LTE(m)(n))


BOOL_TO_INT = lambda x: IF_THEN_ELSE(EQUIV(x)(TRUE))(ONE)(ZERO)
INT_TO_BOOL = lambda x: IF_THEN_ELSE(IS_ZERO(x))(FALSE)(TRUE)

#FOR_EACH =
