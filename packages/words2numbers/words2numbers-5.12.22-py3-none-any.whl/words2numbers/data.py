from collections import OrderedDict
import re

ANDS = ["and"]
POINTS = ["point"]
NEGATIVES = ["negative", "neg", "minus"]

ZEROS = (("zero", 0))

ONES = OrderedDict([
    ("zero", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
])
ONES.update([(str(val), val) for val in ONES.values()])
ONES.update([(str(-val), -val) for val in ONES.values()])


TEENS_AND_TEN = OrderedDict([
    ("ten", 10),
    ("eleven", 11),
    ("twelve", 12),
    ("thirteen", 13),
    ("fourteen", 14),
    ("fifteen", 15),
    ("sixteen", 16),
    ("seventeen", 17),
    ("eighteen", 18),
    ("nineteen", 19),
])
TEENS_AND_TEN.update([(str(val), val) for val in TEENS_AND_TEN.values()])
TEENS_AND_TEN.update([(str(-val), -val) for val in TEENS_AND_TEN.values()])

TENS = OrderedDict([
    ("twenty", 20),
    ("thirty", 30),
    ("forty", 40),
    ("fifty", 50),
    ("sixty", 60),
    ("seventy", 70),
    ("eighty", 80),
    ("ninety", 90),
])
TENS.update([(str(val), val) for val in TENS.values()])
TENS.update([(str(-val), -val) for val in TENS.values()])

HUNDRED = {"hundred": 100}

MULTIPLES = OrderedDict([
    ("hundred", 100),
    ("thousand", 1000),
    ("million", 1e6),
    ("billion", 1e9),
    ("trillion", 1e12),
    ("quadrillion", 1e24),
    ("quintillion", 1e30),
    ("sextillion", 1e36),
    ("septillion", 1e42),
    ("octillion", 1e48),
    ("nonillion", 1e54),
    ("decillion", 1e60)
])
MULTIPLES.update([(str(val), val) for val in MULTIPLES.values()])

ORDINAL_ONES = OrderedDict([
    ("first", 1),
    ("second", 2),
    ("third", 3),
    ("fourth", 4),
    ("fifth", 5),
    ("sixth", 6),
    ("seventh", 7),
    ("eighth", 8),
    ("ninth", 9),
])
ONES.update(ORDINAL_ONES)

ORDINAL_TEENS_AND_TEN = OrderedDict([
    ("tenth", 10),
    ("eleventh", 11),
    ("twelfth", 12),
    ("thirteenth", 13),
    ("fourteenth", 14),
    ("fifteenth", 15),
    ("sixteenth", 16),
    ("seventeenth", 17),
    ("eighteenth", 18),
    ("nineteenth", 19),
])
TEENS_AND_TEN.update(ORDINAL_TEENS_AND_TEN)

ORDINAL_TENS = OrderedDict([
    ("twentieth", 20),
    ("thirtieth", 30),
    ("fortieth", 40),
    ("fiftieth", 50),
    ("sixtieth", 60),
    ("seventieth", 70),
    ("eightieth", 80),
    ("ninetieth", 90),
])
TENS.update(ORDINAL_TENS)

ORDINAL_MULTIPLES = OrderedDict([
    ("hundredth", 100),
    ("thousandth", 1000),
    ("millionth", 1e6),
    ("billionth", 1e9),
    ("trillionth", 1e12),
    ("quadrillionth", 1e24),
    ("quintillionth", 1e30),
    ("sextillionth", 1e36),
    ("septillionth", 1e42),
    ("octillionth", 1e48),
    ("nonillionth", 1e54),
    ("decillionth", 1e60)
])
MULTIPLES.update(ORDINAL_MULTIPLES)

ORDINAL_SUFFIXES = ["st","th", "rd", "nd"]

ORDINALS = OrderedDict()
ORDINALS.update(ORDINAL_ONES)
ORDINALS.update(ORDINAL_TEENS_AND_TEN)
ORDINALS.update(ORDINAL_TENS)
ORDINALS.update(ORDINAL_MULTIPLES)

ALL_NUMS = OrderedDict()
ALL_NUMS.update(ONES)
ALL_NUMS.update(TEENS_AND_TEN)
ALL_NUMS.update(TENS)
ALL_NUMS.update(MULTIPLES)

neg_nums = [(val*-1, val*-1) for n, val in ALL_NUMS.items() if n not in ORDINALS]
ALL_NUMS.update(neg_nums)

ALL_VALID = OrderedDict()
ALL_VALID.update(ALL_NUMS)
string_keys = dict(zip(tuple(map(str, ALL_NUMS.values())), ALL_NUMS.values()))

#ALL_NUMS.update(string_keys)

other = POINTS+ANDS+NEGATIVES
ALL_VALID.update(list(zip(other, range(len(other)))))
ALL_VALID.update(ORDINALS)

#_neg_nums = [-1*val for val in ALL_NUMS.values()]
#NEGATIVE_ALL = NEGATIVES + _neg_nums + list(map(str, _neg_nums))
#ALL_NUMS.update(zip(list(map(str, _neg_nums)), _neg_nums))
#ALL_NUMS.update(zip(_neg_nums, _neg_nums))

SUFFIXES = OrderedDict([
    ("k", 1000),
    ("m", 1e6),
    ("b", 1e9),
    ("g", 1e9),
])

SUFFIXES_BY_NAME = OrderedDict([
    ("kilo", 1000),
    ("mega", 1e6),
    ("giga", 1e9),
])

INFORMAL_EXACT = OrderedDict([
    ("single", 1),
    ("couple", 2),
    ("half", 0.5),
    ("quarter", 0.25),
    ("pair", 2),
    ("few", 3),
    ("dozen", 12),
])

# multiplyable such that NUM couples, NUM pairs, NUM couples of # a number can follow this, such that: 2 couples, 35 pairs, or 10 dozens
INFORMALS_MULTIPLYABLE = OrderedDict([
    ("couples", 2),
    ("pairs", 2),
    ("dozens", 12),
    ("quarters", 0.25),
    ("halves", 0.5),
])

INFORMAL_ALL = OrderedDict()
INFORMAL_ALL.update(INFORMAL_EXACT)
INFORMAL_ALL.update(INFORMALS_MULTIPLYABLE)


_tens="|".join(TENS.keys())
_ones="|".join([n for n in ONES if n!="zero"])
_ordinal_ones="|".join(ORDINAL_ONES.keys())
_teens = "|".join([n for n in TEENS_AND_TEN if n!="ten"])
_negs = "|".join(NEGATIVES)
_points = "|".join(POINTS)

# tens-ones eg twenty-five, seventy-six
TEN_HYPHEN_ONE = re.compile(f"({_tens})-({_ones}|{_ordinal_ones})")

# one eleven, two sixteen
SKIP_HUNDRED_1 = re.compile(fr"({_ones})\s+({_teens})")

# one twenty, two ninety
SKIP_HUNDRED_2 = re.compile(fr"({_ones})\s+({_tens})")

# one twenty five
SKIP_HUNDRED_3 = re.compile(fr"({_ones})\s+({_tens})\s+({_ones})")

_back_neg_or_float_number = r""
# float number regex 
FLOAT_NUMBER_REGEX = r"[-+]?[\d]+(?:[',]\d\d\d)*(([\.]\d*)([eE][-+]?\d+)|([\.]\d*)|([eE][-+]?\d+))"
DOT_FLOAT_NUMBER_REGEX = r"[-+]?[\.]\d+(([eE][-+]?\d+)|([eE][-+]?\d+))?"
FLOAT_NUMBER_REGEX = fr"({FLOAT_NUMBER_REGEX}|{DOT_FLOAT_NUMBER_REGEX})"

# integer
NEGATIVE_INTEGER_REGEX = r"[-][\d]+(?:[',]\d\d\d)*"

# any Number
NEG_OR_FLOAT_NUMBER_REGEX = fr"({FLOAT_NUMBER_REGEX}|{NEGATIVE_INTEGER_REGEX})"

# any spelled number
NUMBER_SPELLED = "|".join(list(map(str, ALL_NUMS.keys())))

# (negative)? 230 ((point) 5 7 or five seven)?
_all_ones = list(map(str, ONES.values()))+list(ONES.keys())
MIXED_SPOKEN_REGEX = (
    r"((_negs)\s)?"
    r"[\d]+"
    r"("
    r"(\spoint(\s(_ones))+\s(_powers))"
    r"|"
    r"(_powers)"
    r")").replace("_negs", _negs) \
.replace("_ones", "|".join([n for n in _all_ones])) \
.replace("_powers", "|".join([n for n in MULTIPLES if n!="hundred"]))

# any Number followed by multiple 2.3 million
_multiples = "|".join(n for n in MULTIPLES if n!="hundred")
FLOAT_FOLLOWED_BY_POWER_REGEX = r"_neg_or_float_number\s{1,2}(_multiples)".replace("_neg_or_float_number", FLOAT_NUMBER_REGEX) \
.replace("_multiples", _multiples)

# any Number followed by a multiple suffix
_suffixes = "".join(SUFFIXES.keys())
FLOAT_FOLLOWED_BY_SUFFIX_REGEX = r"(({_negs})\s)?{_neg_or_float_number}[{_suffixes}]".format(_neg_or_float_number=NEG_OR_FLOAT_NUMBER_REGEX, _suffixes=_suffixes, _negs=_negs)

# infomals couple, pair, dozen...
_informal = "|".join(INFORMAL_EXACT.keys())
INFORMALS_EXACT_REGEX = r"\b((1|0|one|zero)\s)?({_informal})\b".format(_informal=_informal)

_informals_multiplyable = "|".join(INFORMALS_MULTIPLYABLE.keys())
INFORMALS_MULTIPLYABLE_REGEX = r"({_neg_or_float_number}\s)?({_informals_multiplyable})".format(_neg_or_float_number=NEG_OR_FLOAT_NUMBER_REGEX,_informals_multiplyable=_informals_multiplyable)

_ordinal_suffixes = "|".join(ORDINAL_SUFFIXES)
ORDINAL_NUMERAL_REGEX = r"\d+({_ordinal_suffixes})".format(_ordinal_suffixes=_ordinal_suffixes)

#below_hundred = f"({_ones})|({_teens})|({_tens})"
#ten_one = fr"({_tens})[\s\-]({_ones})"
#comma_space = r"\s{,2}?[,]?\s{1,2}"
#hundred = (
#    fr"(({_ones})\s)?"
#    "hundred"
#    r"("
#    r"\s(and\s)?"
#    "("
#    f"({ten_one})"
#    "|"
#    f"({_ones})"
#    "|"
#    f"({_teens})"
#    "|"
#    f"({_tens})"
#    "))?"
#)
#part = f"({hundred})|({below_hundred})"
#end = fr"({hundred})|((and\s)?({below_hundred}))"
#number = (
#    fr"({part})"
#    )
#number = re.compile(number, re.IGNORECASE)
#text = "seven hundred and eighty eight thousand six hundred and twenty nine"
#for m in number.finditer(text):
#    if m.group():
#        print(m)