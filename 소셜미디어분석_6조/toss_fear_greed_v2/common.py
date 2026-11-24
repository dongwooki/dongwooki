"""공통 규칙. 류창민 toss_fear_greed 코드의 규칙을 그대로 따른다.
- 전처리: featurize.py와 같음 (멘션 → @사용자, 종목명 → 종목, 숫자 → 0)
- 한 달: 전월 27일 ~ 당월 27일 전 (make_sample.py, apply_all2.py)
- 거래일 배정: 20:00 이후 글과 휴장일 글은 다음 거래일, 09:00 전은 그 거래일의 야간 (build_index.py)
"""
import bisect
import json
import os
import re
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))
HERE = os.path.dirname(os.path.abspath(__file__))
LABELS5 = ["greed", "fear", "neutral", "irrelevant", "unsure"]
MENTION = re.compile(r"#\[[^\]]*\]\(\d+\)")
ALIASES = "삼전 하닉 하이닉스 에코프로 엘지 현차".split()
NXT_START = "2025-03-04"   # 대체거래소(넥스트레이드) 거래 시작일


def load_sectors(base):
    path = os.path.join(base, "sectors.json")
    if not os.path.exists(path):
        path = os.path.join(HERE, "sectors.json")
    return json.load(open(path, encoding="utf-8"))


def stock_maps(sectors):
    sector = {c: s for s, v in sectors.items() for c in v}
    name = {c: n for v in sectors.values() for c, n in v.items()}
    return sector, name


def make_cleaner(sectors):
    names = sorted({n for v in sectors.values() for n in v.values()}, key=len, reverse=True)
    pat = re.compile("|".join(map(re.escape, names + ALIASES)))

    def clean(s):
        return re.sub(r"\d+", "0", pat.sub("종목", MENTION.sub("@사용자", s or "")))
    return clean


def month_of(ts):
    """ISO 시각(UTC 또는 시간대 포함) → 27일 기준 달."""
    t = datetime.fromisoformat(ts).astimezone(KST)
    if t.day >= 27:
        return f"{t.year}-{t.month:02d}"
    y, m = (t.year, t.month - 1) if t.month > 1 else (t.year - 1, 12)
    return f"{y}-{m:02d}"


def slot_of(t):
    """KST datetime → 30분 칸 문자열."""
    return t.strftime("%Y-%m-%dT%H:") + ("30" if t.minute >= 30 else "00")


def load_trading_days(base):
    import pandas as pd
    return pd.read_csv(os.path.join(base, "trading_days.csv"))["date"].astype(str).tolist()


def make_tday(td):
    """30분 칸 → (거래일, 'day'|'night'). build_index.py·analysis_presentation.py와 같은 규칙."""
    def to_tday(slot):
        d, hm = slot[:10], slot[11:]
        if hm >= "20:00":
            i = bisect.bisect_right(td, d)
            return (td[i] if i < len(td) else None), "night"
        i = bisect.bisect_left(td, d)
        if i >= len(td):
            return None, None
        t = td[i]
        return t, ("night" if (t != d or hm < "09:00") else "day")
    return to_tday


def batches(spec, label_dir=None):
    """'b00-b16 b31' 같은 표기 → 묶음 이름 목록. 'all'이면 labels 폴더 전체."""
    if spec == "all" and label_dir:
        return sorted(os.path.basename(p)[:-6] for p in os.listdir(label_dir) if p.endswith(".jsonl"))
    out = []
    for s in spec.split():
        if "-" in s:
            a, b = (int(x[1:]) for x in s.split("-"))
            out += [f"b{i:02d}" for i in range(a, b + 1)]
        else:
            out.append(s)
    return out


def write_json(path, obj):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, default=float)
