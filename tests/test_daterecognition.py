from daterecognition import __version__
from daterecognition.parser import CoreDateParser
import daterecognition.formats as FORMATS

def test_version():
    assert __version__ == '0.1.0'

def test_success():
    texts = {
        'S1': 'Tomorrow is January 01 2019.',
        'S2': 'entries are due by January 04, 2017 at 8:00pm',
        'S3': 'created 01/15/2005 by ACME Inc. and associates.'
    }
    
    dp = CoreDateParser(formats=FORMATS.USA,start_year=2015,end_year=2020)

    #S1
    s1_dates = dp.parse_string(texts.get("S1"))
    s1_answer = [{
        "string": "january 01 2019",
        "char_start_idx": 12,
        "char_end_idx": 26,
        "date_format": r"%B %d %Y",
        "token_start_idx": 2,
        "token_end_idx": 4
    }]
    for e in s1_dates:
        assert(e in s1_answer)
    assert(len(s1_dates) == len(s1_answer))

    #S2
    s2_dates = dp.parse_string(texts.get("S2"))
    s2_answer = [{
        "string": "january 04, 2017",
        "char_start_idx": 19,
        "char_end_idx": 34,
        "date_format": r"%B %d, %Y",
        "token_start_idx": 4,
        "token_end_idx": 6
    }]
    for e in s2_dates:
        assert(e in s2_answer)
    assert(len(s2_dates) == len(s2_answer))

    #S3
    s3_dates = dp.parse_string(texts.get("S3"))
    s3_answer = [
        {
            "string": "01/15/20",
            "char_start_idx": 8,
            "char_end_idx": 15,
            "date_format": r"%m/%-d/%y",
            "token_start_idx": 1,
            "token_end_idx": 1
        },
        {
            "string": "01/15/20",
            "char_start_idx": 8,
            "char_end_idx": 15,
            "date_format": r"%m/%d/%y",
            "token_start_idx": 1,
            "token_end_idx": 1
        }
    ]
    for e in s3_dates:
        assert(e in s3_answer)
    assert(len(s3_dates) == len(s3_answer))