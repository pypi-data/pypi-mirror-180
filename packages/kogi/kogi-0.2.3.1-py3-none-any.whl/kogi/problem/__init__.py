import traceback
from kogi.logger import kogi_print
from .drill import kogi_judge, judge_cpc
from .atcoder import download_atcoder_problem


def atcoder_detector(directive, raw_cell):
    if 'https://atcoder.jp/contests/' in directive:
        return 'atcoder'
    return None


def atcoder_judge(ipy, raw_cell, directive):
    data = download_atcoder_problem(directive)
    if 'error' in data:
        kogi_print(data['error'])
    elif 'problem_id' in data:
        kogi_print('コギーがAtCoderの問題を発見し、テストケースを実行しようとしています')
        kogi_judge(ipy, raw_cell, data, judge_cpc)
    else:
        kogi_print('問題が見つかりません。')
    return None
