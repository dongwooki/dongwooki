# 로봇용 소재에 AI가 들어온 이유, 적용 방식, 남은 과제

작성 기준일 2026-11-18. 이 보고서는 로봇을 구성하는 소재를 개발하는 데 인공지능(AI)이 왜 쓰이게 되었는지, 어떻게 적용되어 무엇을 이루었는지, 무엇이 남았는지를 세 질문 순서대로 정리한다. 표의 '신뢰도'·'검증상태' 열과 일부 괄호 안의 원문확인·언론·기업주장·미확인 표기는 출처 신뢰도를 뜻한다(부록 A).

## 한눈에 보기

| 질문 | 핵심 답 |
|---|---|
| **1. AI는 왜 도입되었나** | 로봇 소재는 가볍고 강하면서 동시에 늘어나고, 감지하고, 스스로 움직여야 한다. 이 조합을 만족하는 조성·구조의 설계공간은 사람이 훑을 수 없을 만큼 크고(자기 연성 로봇 시트 하나가 약 10^752가지), 거동은 비선형이고 이력(히스테리시스)이 있으며, 수명시험은 느리다. 그래서 적은 실험으로 예측·최적화하고 목표 물성에서 거꾸로 설계해 주는 AI가 필요해졌다. |
| **2. 어떻게 적용되었고 무엇을 이끌었나** | 대리모델, 베이지안 최적화(BO)·능동학습, 역설계·생성모델, 형태-소재-제어 공동설계, 센서 신호 해석, 로봇 자율실험의 여섯 방식으로 쓰였다. 대표 성과로는 1,089개 조합 중 62개만 만들어 인공근육을 최적화한 사례(Aalto), 36개 배합으로 600% 넘게 늘어나는 3D 프린팅 엘라스토머(KAIST·KIST, 2026), 노트북에서 30초 안에 걷는 로봇 몸체를 설계한 사례(Northwestern), 센서 하나로 물체 20개를 83% 정확도로 식별한 전자피부(서울대)가 있다. |
| **3. 남은 문제와 해결 방향** | 성과는 시뮬레이터와 데이터가 싼 영역(메타물질, 4D 프린팅, 자기 연성 복합재, 전자피부 신호 해석)에 몰려 있다. 실제 로봇의 무게와 신뢰성을 좌우하는 자석, 감속기 강, 엔지니어링 플라스틱, LCE·이온성 액추에이터 화학에는 AI 사례가 거의 없다. 해법은 실패·수명 데이터를 포함한 공통 데이터, sim-to-real 보정과 불확실성 정량화, 전문가 검증, 합성부터 피로시험까지 닫힌 자율실험 루프, 그리고 핵심 부품 소재로의 확장이다. |

**핵심 시사점**

1. AI가 로봇 소재에서 실제로 기여한 것은 "새 물질의 발견"보다 **알려진 소재군의 배합·공정·구조를 적은 실험으로 최적화**하는 일이다. 검증된 성과는 대부분 수십 번의 실험이나 값싼 시뮬레이션으로 얻었다.
2. AI가 잘 되는 곳과 안 되는 곳을 가르는 기준은 **데이터를 얻는 비용**이다. 시뮬레이터가 있는 구조·형상 설계는 성숙했고, 합성과 장기 시험이 필요한 화학 소재는 뒤처져 있다.
3. 가장 큰 공백은 **로봇 무게의 절반 이상을 차지하는 관절 부품 소재**(자석, 감속기 강, 윤활, 하우징 플라스틱)다. 이 영역에서 AI 설계 소재가 양산 로봇에 쓰였다는 공개 사례는 없다.
4. 2026년 11월 현재 **소프트 액추에이터 소재를 자동으로 합성하고 수명까지 시험하는 완전 폐루프 자율실험실은 없다.** 자동 시험과 자동 제작이 각각 따로 시연된 단계다.
5. AI 소재 연구의 신규성 주장은 반드시 검증해야 한다. 무기 소재 분야의 대표 성과 세 건(A-Lab, GNoME, MatterGen)이 모두 "이미 알려진 물질"이라는 비판을 받았고, 그중 한 건은 정정됐다.

---

## 0. 조사 범위와 로봇 소재 분류

**범위:** 이 보고서는 로봇 몸체와 부품을 이루는 소재, 곧 "로봇을 위한 소재"만 다룬다. 로봇이 실험을 대신하는 자율실험실(SDL)은 그런 소재를 개발하는 **한 가지 방법**으로만 다루고, 로봇과 무관한 촉매·광물질 발견 사례는 방법론의 교훈(3장)으로만 쓴다.

아래 9개 그룹을 1~3장의 공통 틀로 쓴다. G1~G4는 산업용 로봇·사족 로봇·휴머노이드 같은 강체 로봇의 부품 소재이고, G5~G9는 소프트·마이크로·바이오 로봇에서 두드러지는 기능 소재다. 두 계열은 AI 적용 양상이 뚜렷이 다르므로(2-3), 표의 순서도 이 구분을 따랐다.

| 그룹 | 대표 소재 | 로봇 내 역할 | 요구 특성 |
|---|---|---|---|
| G1 구조·경량재 | Al·Mg·Ti 합금, CFRP, PEEK·PA-GF·PC-ABS, 적층제조 격자 | 링크, 관절 하우징, 외피, 다리 | 비강성, 피로강도, 주조·사출 성형성 |
| G2 모터·자석·전력전자 | 소결 NdFeB(Dy/Tb 첨가), 무희토 자석(FeN 등), 전기강판, 구리, GaN 소자 | 관절 모터, 관절 내장 인버터 | 고에너지적, 고온 보자력, 공급 안정성 |
| G3 관절·감속기·트라이볼로지 | 플렉스플라인 합금강, 베어링강, 그리스, 힘줄(UHMWPE·아라미드) | 하모닉·RV 감속기, 롤러스크루, 손 힘줄 | 피로수명, 내마모, 저크리프 |
| G4 배터리·에너지 | Li-ion(NMC·LFP), 고체전해질, 신축 배터리 | 동력원 | 에너지밀도, 열폭주 안전성, 급속충전 |
| G5 센서·전자피부 | 압저항(CNT·AgNW·액체금속), 정전용량, 압전(PVDF), 마찰전기, 자기 피부, 멤리스터 나노와이어 | 촉각·온도·근접 감지 | 감도, 다중모드, 넓은 면적, 내구성 |
| G6 인공근육·소프트 액추에이터 | 유전 엘라스토머(DE), HASEL, LCE, SMA·SMP, 꼬임 고분자 섬유(TCP), 하이드로겔, IPMC, 자기 연성 복합재, 공압 엘라스토머 | 구동 | 변형률, 응력, 속도, 효율, 사이클 수명 |
| G7 신축 전도체 | 액체금속(EGaIn), PEDOT:PSS, 금속 나노복합 전극 | 배선, 전극, 신축 전자 | 늘어나도 유지되는 전도도 |
| G8 기능성·지능형 구조 | 자가치유 고분자, 재밍(가변강성), 기계 메타물질·키리가미, 4D 프린팅 복합재 | 몸체, 피부, 그리퍼, 충격흡수 | 프로그램 가능한 변형, 손상 복구 |
| G9 마이크로·바이오 로봇 소재 | 자기 마이크로로봇, 촉매 마이크로모터, 생분해 고분자(PLGA·젤라틴), 세포·근육 조직 | 의료·환경용 소형 로봇 | 생체적합, 분해성, 원격 구동 |

---

## 1. 인공지능은 왜 도입되었나

**답:** 로봇 소재는 서로 충돌하는 여러 특성을 한꺼번에 요구하는데, 기존의 시행착오와 물리모델로는 그 조합을 찾는 데 너무 많은 실험과 시간이 든다. AI는 예측·최적화·역설계·신호 해석·자동실험으로 이 비용을 줄이기 때문에 도입되었다.

### 1-1. 로봇 소재에 요구되는 특성

로봇 소재의 요구는 "더 좋은 물성 하나"가 아니라 **여러 물성의 동시 만족**이다.

| 요구 특성 | 왜 중요한가 | 근거 |
|---|---|---|
| 경량·고강도 | 휴머노이드 무게의 약 56%가 액추에이터다. 액추에이터 구조 부품은 주로 강과 Al 합금이라 무게와 배터리 효율에 부담이 된다. 그래서 밀도가 Al의 절반(약 1.3 g/cm³)인 PEEK 같은 플라스틱이 대당 6~10 kg씩 쓰이기 시작했다. | ([IDTechEx 기고, R&A News 2026](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)); ([Gasgoo 2026](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)) |
| 유연·신축 | 인공근육은 사람 근육 수준의 변형과 일을 내야 한다. 꼬인 나일론 섬유는 49% 수축, 5.3 kW/kg의 일을 낸다. | ([Haines et al., Science 2014](https://api.openalex.org/works/doi:10.1126/science.1246906)) |
| 다기능 센싱·구동 | 하나의 피부가 힘·위치·온도·근접·진동을 함께 읽어야 한다. 두께 1 mm 촉각 피부가 힘 0.06 N, 위치 0.4 mm 정확도와 0~90 °C 온도, 15 cm 이내 근접을 함께 측정한 예가 있다. | ([SuperTac, Nature Sensors 2026](https://www.nature.com/articles/s44460-025-00006-y)) |
| 내구성 | 공압 소프트 액추에이터는 피로·박리·마모로 기존 액추에이터(5~10년 연속 운전)보다 훨씬 빨리 열화한다. 하모닉 감속기의 주 파손 모드도 플렉스플라인 피로다. | ([HKUST 내구성 리뷰 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)); ([humanoid.guide 플렉스플라인](https://humanoid.guide/?p=20671)) |
| 안전·인증 | 로봇 배터리는 사람 곁에서 쓰이므로 열폭주 전파 차단 소재와 인증이 필요하다. Figure 03 배터리는 2.3 kWh로 5시간을 운전하며 UN38.3·UL2271 인증을 동시에 추진했다. | ([Figure F.03 배터리 2025](https://figure.ai/news/f-03-battery-development)) |
| 공급 안정성 | 고급 휴머노이드 1대에는 NdFeB 자석이 약 4 kg 들어간다. 중국은 2025년 4월 Dy·Tb·Sm 등 중희토류 7종과 그 자석을 수출 허가제로 묶었다. | ([Adamas 2026](https://www.adamasintel.com/humanoid-robotics-sector-accelerates-on-multiple-commercialization-fronts-in-march/)); ([CSIS](https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions)) |

### 1-2. 기존 개발 방식(시행착오·물리모델)의 한계

위 요구를 사람의 직관과 물리모델만으로 맞추려 하면 다섯 가지 벽에 부딪힌다.

1. **설계공간이 너무 크다.** 자기 연성 로봇의 자화 분포와 형상을 함께 정하는 설계공간은 시트형이 약 1.2×10^752, 빔형이 약 1.8×10^53가지다 ([Karacakol et al., Nat. Commun. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947188/)). 무희토 자석 탐색에서도 1억 개가 넘는 조성이 후보였다 ([Mining.com, MagNex 2024](https://www.mining.com/ai-helps-quickly-develop-rare-earth-free-permanent-magnet/)).
2. **거동이 비선형·이력적·다물리적이다.** 소프트 로봇 소재의 비선형성과 히스테리시스는 모델링과 제어를 어렵게 만들고, 이것이 ML 도입의 직접 동기로 꼽힌다 ([PLoS ONE 리뷰 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)). HASEL 같은 전기유압 근육은 감쇠 실험 자체가 이력을 유발해서 고전적 시스템 식별도 쉽지 않다 ([HASEL 스펙트럼 모델, arXiv 2601.03247](https://arxiv.org/abs/2601.03247)).
3. **소재, 구조, 제어가 얽혀 있다.** 마이크로로봇의 설계-성능 관계는 "고차원·비선형·확률적이며 미지"라고 평가된다 ([Columbia, JACS Au 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10052236)). 고충실도 유한요소해석(FEA)은 실시간보다 수백 배 느려 공동설계 반복에 쓰기 어렵다 ([공동설계 관점 논문, arXiv 2505.03761](https://arxiv.org/abs/2505.03761)).
4. **실험과 수명시험이 느리고 비싸다.** 휴머노이드 소재 솔루션의 80~90%는 맞춤형이고, 양산 전에 배합과 구조를 3~5회 반복 조정한다 ([Gasgoo, Kingfa 인터뷰 2026](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)). 소프트 액추에이터 수명 연구는 "제한적이고 파편화"되어 있다 ([HKUST 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)).
5. **희소 원료를 대체해야 한다.** 비AI 경로인 질화철(FeN) 무희토 자석은 10년 넘게 연구했지만 2024년에도 "아직 준비되지 않았다"는 평가를 받았다 ([New Atlas 2024](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery/)).

정책도 같은 문제를 명분으로 삼았다. 미국 MGI(2011)는 "두 배 빠르게, 훨씬 적은 비용으로"를, 한국 과기정통부(2026)는 "경험과 반복 실험에 의존해 10~20년 이상 걸리는 소재 개발"의 단축을 목표로 내걸었다 ([MGI 백서](https://www.mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf); [디지털타임스 2026-04-30](https://v.daum.net/v/20260430155346042)).

### 1-3. 그래서 AI가 제공하는 것

AI는 1-2의 다섯 한계에 각각 대응하는 다섯 가지 기능을 제공한다.

| AI 기능 | 대응하는 한계 | 근거 사례 |
|---|---|---|
| 대리모델로 빠른 예측 | 느린 시뮬레이션·실험 | 층 재밍(layer jamming) 구조에서 수십 시간 걸리는 FE 해석을 ML 대리모델로 대체했다 ([Zeng & Su, NSF PAR](https://par.nsf.gov/servlets/purl/10557920), 미확인) |
| 적은 실험으로 최적화(BO·능동학습) | 큰 설계공간, 비싼 실험 | 자율실험 42개 연구, 벤치마크 63건을 메타분석한 결과, 같은 성능에 도달하는 데 필요한 실험 수가 무작위 탐색 대비 **중앙값 6배** 적었다 ([Adesiji et al., arXiv 2508.06642](https://arxiv.org/abs/2508.06642), 원문확인) |
| 목표 물성에서 거꾸로 찾는 역설계 | 직관이 닿지 않는 조합 | 소량 데이터 ML로 인공피부 미세구조를 "물성→구조"로 역설계해 기존 절차보다 효율이 최소 10^4배 높았다고 보고했다 ([인공피부 역설계, arXiv 2304.04609](https://arxiv.org/abs/2304.04609), 원문확인·프리프린트) |
| 센서 신호 해석 | 다물리·비선형 신호 | 두께 0.5 mm 자화 필름과 홀 센서로 만든 자기 피부가 딥러닝으로 초해상 정확도를 60배 높였다 ([Yan et al., Sci. Robot. 2021](https://doi.org/10.1126/scirobotics.abc8801), 원문확인) |
| 로봇 자율실험과 폐루프 | 느린 수작업 실험, 24시간 운전 불가 | 이동 로봇 화학자가 8일간 10개 변수 공간에서 688회 실험을 자율 수행했다 ([Burger et al., Nature 2020](https://www.nature.com/articles/s41586-020-2442-2), 원문확인) |

다섯 기능은 따로 쓰이기보다 서로 이어 붙는다. 대리모델이 있어야 BO가 다음 실험을 고를 수 있고, 역설계는 대리모델을 뒤집어 쓰는 것이며, 자율실험은 BO의 제안을 로봇이 실행해 데이터를 다시 모델에 넣는 고리다. 형태-소재-제어 공동설계(2-1)는 이 도구들을 소재 하나가 아니라 로봇 전체에 적용한 형태다. 다만 메타분석의 "6배"는 실험 횟수 기준이고 비교 대상이 주로 무작위 탐색이므로, 사람 전문가보다 6배 빠르다는 뜻으로 읽으면 안 된다.

---

## 2. 어떻게 적용되었고 어떤 진전을 이끌었나

**답:** AI는 여섯 가지 방식으로 적용되었다. 데이터 형편에 따라 쓰는 방식이 갈린다. 실험이 비싸면 BO·능동학습을, 시뮬레이터가 싸면 대리모델과 역설계를, 미분 가능한 시뮬레이터가 있으면 공동설계를 쓴다. 정량 성과가 가장 뚜렷한 곳은 소프트 액추에이터 배합, 기능성 구조, 전자피부 신호 해석이다.

### 2-1. AI 적용 방식 유형

| 방식 | 원리 한 줄 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|---|
| 물성 예측·대리모델 | 조성·공정 데이터로 물성을 회귀하고, 비싼 시뮬레이션·실험을 대체한다 | NASA의 NiTi 형상기억합금 ML ([NASA NTRS, MS&T22 초록](https://ntrs.nasa.gov/citations/20220005395)) | 37개 원소를 포함한 Ni-Ti 다원 합금 8,000종 이상, 입력 52개로 변태온도·이력·변태변형률을 예측했고 신규 실험으로 검증했다. 오차(MAE) 수치는 확인하지 못했다. | 원문확인(학회 초록) |
| BO·능동학습 | 모델의 불확실성이 큰 곳을 골라 다음 실험을 정한다 | Aalto·TUM의 열구동 꼬임 고분자 인공근육 ([Materials & Design 2025](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat)) | 가능한 1,089개 공정 조합 중 **62개만 제작해** 구동 변형률 1.25를 달성했다 | 원문확인 |
| 역설계·생성모델 | 목표 형상·물성을 주면 구조나 배합을 생성한다 | Stanford Zhao 그룹 등의 4D 프린팅 능동 판 ([Sun et al., Nat. Commun. 2024](https://www.nature.com/articles/s41467-024-49775-z)) | ResNet 순방향 예측과 경사하강·진화 알고리즘 역설계로, 목표 3D 형상 변형을 내는 활성·수동 복셀 배치를 찾았다 | 원문확인(초록) |
| 형태-소재-제어 공동설계 | 진화 탐색, 미분 가능 시뮬레이션, 확산모델로 몸체·소재 분포·제어를 함께 최적화한다 | Northwestern·UVM·MIT ([Matthews et al., PNAS 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10576117/)); MIT CSAIL 확산모델 점프 로봇 ([MIT News 2025](https://news.mit.edu/2025/using-generative-ai-help-robots-jump-higher-land-safely-0627)) | 노트북에서 **30초 이내, 설계 시도 10회**로 걷는 몸체를 만들었다. 확산모델이 설계한 링크로 점프 높이가 41% 높아졌고, 착지 시 넘어짐이 84% 개선됐다 | 원문확인 / 언론 |
| 센서 신호 해석(ML 디코딩) | 다중모드·희소 신호를 학습 모델로 해석해 물체·재질을 식별한다 | 서울대 고승환 그룹 멤리스터 나노와이어 센서 ([Kim et al. (서울대 고승환 그룹), Nature Materials 2025](https://www.nature.com/articles/s41563-025-02373-w)) | 손끝 센서 **1개로 가정용품 20종을 83%** 정확도로 식별했다 | 원문확인 |
| 로봇 자율실험(폐루프) | 로봇이 제작·시험하고 AI가 다음 조건을 정한다 | 유전 엘라스토머 액추에이터(DEA) 수명 시험 로봇 ([arXiv 2602.20963, 2026](https://arxiv.org/abs/2602.20963)) | 극한 운전 조건에서 수명을 최대 100% 늘렸다. 최적화한 액추에이터로 만든 사족 로봇은 자기 무게의 100% 넘는 짐을 실었다 | 원문확인(프리프린트 초록) |

방식 선택은 데이터를 얻는 비용을 따른다. 미분 가능한 연성체 시뮬레이터는 소재 물성과 형상의 동시 최적화를 가능하게 했다(MIT ChainQueen) ([Spielberg et al., Robotica 2021](https://cdfg.csail.mit.edu/assets/files/robotica.pdf)). 확산모델 샘플링에 물리 시뮬레이션의 기울기를 결합한 DiffuseBot은 6개 과제에서 몸체와 제어를 함께 설계했다 ([DiffuseBot, NeurIPS 2023](https://arxiv.org/abs/2311.17053)).

### 2-2. 소재 그룹별 진전

**G1 구조·경량재. AI 사례는 학술 합금 설계와 부품 위상최적화에 그친다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 경량 Mg 합금 조성 설계 | ML 해석형 합금 설계 ([J. Mater. Inform. 2025](https://www.oaepublish.com/articles/jmi.2024.92)) | Mg-2Al-1Zn-0.6Ca-0.4Mn 인장강도 344 MPa, 연신율 21.3% | 미확인(검색 초록) |
| 보행 로봇 다리 위상최적화 | 사족 로봇 유연 다리 ([사족 로봇 다리 위상최적화, Sci. Rep. 2023](https://www.nature.com/articles/s41598-023-32106-5)) | 위상최적화 후 나일론 PA2200으로 3D 프린팅 | 원문확인 |
| 보행 로봇 팔 AI 위상최적화 | FH OÖ, German Robotics Conf. 2025 ([FH OÖ, German Robotics Conf. 2025](https://pure.fh-ooe.at/en/publications/ai-driven-topology-optimized-modular-robotic-arm-design-for-legge/)) | 구조 성능을 유지하며 재료 사용 최소화(수치 없음) | 원문확인 |

실제 양산 로봇의 변화는 AI와 무관하다. Figure 03은 CNC 가공 대신 다이캐스팅·사출·프레스 같은 금형 공정에 크게 의존하도록 바뀌었고 이전 모델보다 9% 가볍지만, AI 소재는 언급하지 않았다 ([Figure 03 공개 2025](https://www.figure.ai/news/introducing-figure-03)). 소재 선택 기준이 비강성에서 주조성·사출성으로 옮겨 가는 지금이, 공정 제약까지 넣은 다목적 최적화가 가장 쓸모 있을 시점이다. 그런데도 이 영역의 AI 연구는 조성 설계와 형상 설계가 따로 놀아, ML로 설계한 합금을 ML로 최적화한 형상에 적용한 로봇 부품은 공개된 예가 없다.

**G2 모터·자석·전력전자. 기업 주장 한 건이 사실상 전부다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 무희토 영구자석 조성 탐색 | Materials Nexus MagNex(Sheffield대·Henry Royce Institute 협업) ([Mining.com 2024](https://www.mining.com/ai-helps-quickly-develop-rare-earth-free-permanent-magnet/)) | 1억 개 이상 조성을 스크리닝해 3개월 만에 설계·합성·시험. 잔류자속·보자력·에너지적 같은 동료심사 자기특성 데이터는 없다 | 언론·기업주장 |

Dy 사용량을 줄이는 입계확산 공정을 ML로 최적화해 로봇 모터에 적용했다는 원문은 찾지 못했다. 관절 모터의 핵심 소재 문제(1-1의 Dy/Tb 의존)는 아직 AI의 손이 거의 닿지 않은 영역이다. 자석은 조성만이 아니라 미세조직, 입계상, 소결·확산 공정이 성능을 정하고, 시료 하나를 만들고 측정하는 데 분말 처리와 고온 공정이 필요하다. 구조 시뮬레이션처럼 데이터를 싸게 만들 방법이 없다는 점이 G8과 정반대다. MagNex의 의미는 성능 입증이 아니라 "수억 개 조성 스크리닝 → 수개월 내 합성"이라는 경로가 가능하다는 시연에 있다.

**G3 관절·감속기·트라이볼로지. 일반 기어·베어링용 ML은 있지만 로봇에 적용된 예는 없다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 내피로강 설계 | TU Delft 회전굽힘 피로강도 예측·고처리량 설계 ([TU Delft 피로강 ML](https://repository.tudelft.nl/record/uuid:470d0944-7409-4633-9e61-23092137c72d)) | 전이학습과 진화 알고리즘으로 피로 데이터 수십 개만 사용 | 원문확인 |
| 내마모 베이나이트강 | ORNL, CALPHAD+ML(풍력 기어박스용) ([ORNL 베이나이트강](https://ornl.gov/technology/202405685)) | 건식 미끄럼 마모가 AISI 52100보다 우수 | 미확인 |
| 그리스 배합 최적화 | 아마이드계 그리스 스태킹 앙상블 ([Friction 2025](https://sciopen.com/article/10.26599/FRICT.2025.9440982)) | 마찰계수 R² 0.9939, 마모흔 R² 0.9535 | 미확인 |

하모닉 감속기 제조사는 플렉스플라인을 "합금강"으로만 공개한다 ([Harmonic Drive LLC](https://www.harmonicdrive.net/technology/harmonicdrive)). 강종, 열처리, 결정립 같은 핵심 데이터가 공개되지 않으니 ML 모델을 학습시킬 바탕도 없다. 플렉스플라인 파손 분석은 원인을 개재물이 아니라 조대한 구오스테나이트 결정립으로 지목했다. 즉 성능을 가르는 것은 조성보다 열처리·공정 이력이며, ML이 들어가려면 공정 데이터가 먼저 쌓여야 한다 ([humanoid.guide](https://humanoid.guide/?p=20671)). 손 힘줄도 사정이 같다. UHMWPE는 강하지만 크리프가 있고 아라미드는 크리프가 적지만 빨리 마모되는데, 이 상충을 AI로 다룬 연구는 없다 ([humanoid.guide 힘줄](https://humanoid.guide/?p=16664)).

**G4 배터리·에너지. 배터리 소재 AI 자체는 활발하지만 로봇 전용 사례는 없다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 고체전해질 후보 스크리닝 | Microsoft·PNNL ([Microsoft 2024](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)) | 후보 3,200만 개 → 안정 약 50만 → 800 → 23개(5개는 기존 물질), 80시간. 리튬 사용량을 최대 70% 줄일 가능성. 양산 단계는 아니다 | 언론·기업주장 |
| 급속충전 전해질 자율 최적화 | CMU Clio+Dragonfly ([Dave et al., Nat. Commun. 2022](https://www.nature.com/articles/s41467-022-32938-1)) | 실험 42회, 2근무일 만에 급속충전 전해질 6종을 찾았다(무작위 탐색 대비 6배 빠름). 최고 셀끼리 비교해 4C 충전 후 방전용량 13% 개선(최악 셀끼리는 5%) | 원문확인 |
| 양극재 자율 탐색 실험실 | KAIST·포스코홀딩스 ([KAIST 2025](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)) | 탐색 시간 93% 단축. 단, "24시간 운용·실험 500회 가정" 아래 계산한 추정치다 | 언론·기관발표 |

로봇 배터리는 용량이 작고(Figure 03 2.3 kWh), 사람 곁에서 쓰이므로 안전과 인증이 우선한다. 따라서 로봇 쪽에서 AI가 기여할 지점은 에너지밀도 경쟁보다 열폭주 차단·포팅 소재, 구조 일체형 팩, 신축 배터리(G7) 같은 로봇 고유 요구다. 이 부분에는 아직 AI 사례가 없다.

**G5 센서·전자피부. 신호 해석은 가장 성숙했지만, 센서 소재 자체를 AI로 설계한 사례는 드물다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 다중모드 촉각 디코딩 | 서울대 멤리스터 센서(2-1 참조). 나노와이어 망 하나가 열·기계 감지를 16 Hz로 전환한다 ([Kim et al. (서울대 고승환 그룹), Nature Materials 2025](https://www.nature.com/articles/s41563-025-02373-w)) | 보도에 따르면 열·압력 결합으로 정확도가 약 65%에서 95%로 올랐다 ([ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing)) | 원문확인 / 65→95%는 언론 |
| 광학·마찰전기·관성 융합 피부 | SuperTac, 칭화대 등 ([Nature Sensors 2026](https://www.nature.com/articles/s44460-025-00006-y)) | 질감·재질·미끄럼·충돌·색 인식 94% 이상. 촉각 언어모델 DOVE는 논문에 8.5B, 칭화대 발표에 8.5억(850M) 파라미터로 적혀 서로 다르다 ([칭화대 2026](https://www.tsinghua.edu.cn/info/1175/123978.htm)) | 원문확인 |
| 3D 구조 피부로 탄성률·곡률 측정 | 칭화대 3DAE-Skin ([Liu et al., Science 2024](https://doi.org/10.1126/science.adk5556)) | 법선력·전단력·변형을 분리해 측정. 손끝 크기에 센서 240개, 위치 분해능 약 0.1 mm(언론 인용) ([China Daily](https://govt.chinadaily.com.cn/s/202406/05/WS6673996e498ed2d7b7eb0c2c/chinese-scientists-design-bio-inspired-3d-e-skin.html)) | 원문확인 / 240개는 언론 |
| 마찰전기·액체금속 센서 분류 | 다공성 PDMS 하이브리드 센서 ([Microsyst. Nanoeng. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11543809/)); EGaIn 장갑 ([Sensors 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8125695/)) | 시료 12개 98.46%; 랜덤포레스트 제스처 인식 약 97.3% | 미확인(검색 초록) |
| 손상 후 재보정 | 자가치유 감지 피부+전이학습 ([Adv. Intell. Syst. 2022](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d)) | 터치 위치 2.3 mm. 손상 뒤 200회 미만의 탐침으로 재적응 | 미확인(검색 초록) |
| 자기 피부 초해상 | 2021 Science Robotics 자기 피부(1-3 참조) | 단일 유닛으로 법선력과 전단력을 분리하고, 원격조작으로 바늘에 실을 꿰는 시연을 했다 | 원문확인 |

ML 디코딩의 의미는 정확도 숫자보다 **소재 구성의 단순화**에 있다. 센서 하나나 연속된 피부 한 장에서 여러 정보를 뽑아내면 배선과 소재 층 수가 줄어든다. 반면 상용 휴머노이드는 피부 소재를 공개하지 않는다. Figure 03은 손끝 센서가 3 g의 힘을 감지한다고만 밝혔고, 외피는 다밀도 폼과 세탁·교체 가능한 직물로 바꿨다 ([Figure 03 공개 2025](https://www.figure.ai/news/introducing-figure-03)).

**G6 인공근육·소프트 액추에이터. 배합·공정 최적화에서 정량 성과가 가장 많다. 다만 LCE, HASEL, IPMC에서는 AI가 소재 화학이 아니라 제어·형상 설계에만 쓰였다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 꼬임 고분자 섬유 공정 BO | Aalto·TUM(2-1 참조) | 변수는 합사 수, 꼬임 응력, 코일링 응력 3개였다 | 원문확인 |
| DLP 프린팅 엘라스토머 배합 | KAIST·KIST·서울과기대·KRICT 등 ([Song et al., Nat. Commun. 2026-06](https://www.nature.com/articles/s41467-026-73735-4)) | **배합 36개로** 회귀 대리모델을 만들어 점도와 신축성의 상충을 넘었다. 점도 약 2,500 mPa·s에서 **파단 연신율 600% 초과**. 프린팅한 공압 그리퍼가 200 kPa 이상에서 달걀·유리병·생쥐를 잡았다. BO는 쓰지 않았고 향후 과제로 남겼다 | 원문확인 |
| 자기 연성 소재의 자화·형상 공동설계 | MPI-IS Sitti 그룹 ([Karacakol et al., Nat. Commun. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947188/)) | 신경망 예측과 저비용 시뮬레이션, MAP-Elites 탐색을 결합했다. 직관적 기준 설계보다 점프 성능이 좋았고, 설계 500만 개를 공개 DB로 냈다 | 원문확인 |
| DEA 수명 자동시험 | 2-1 참조. 전압·주파수·전극 농도·충전재를 스캔했다 | 저자들은 "로봇 액추에이터 설계에 SDL을 처음 도입"했다고 주장한다 | 원문확인(프리프린트) |
| SMA 조성 예측 | NASA(2-1 참조); 고온 NiTiHf 탐색 ([J. Mater. Sci. 2022](https://link.springer.com/article/10.1007/s10853-022-07793-6)) | ML이 찾은 Ni49.7Ti26.6Hf23.7의 오스테나이트 종료 온도는 403.5 °C다 | 미확인(검색 초록) |
| 하이드로겔 배합·복합재 | BO로 PAAm/알지네이트 이중망 배합 ([하이드로겔 BO, PMC11422183](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11422183/)); GAN으로 메타섬유 강화 하이드로겔 ([하이드로겔 GAN, PMC11165469](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11165469/)); 저가 자율실험으로 PNIPAM LCST 조정 ([PNIPAM 자율실험, arXiv 2509.05351](https://arxiv.org/abs/2509.05351)) | 정량 수치 미추출 | 미확인 |
| DEA 물성 학습 하이브리드 모델 | 소재 물성을 학습하는 신경망+해석 모델 ([DEA 하이브리드 모델, arXiv 2202.12977](https://arxiv.org/abs/2202.12977)) | FEM 대비 오차 5% 미만, MPC에서 더 적은 반복으로 수렴 | 미확인(프리프린트) |
| 자기 연성 캔틸레버 역설계 | 변형 시뮬레이션으로 학습한 순방향·역방향 모델 ([Int. J. Mech. Mater. Des. 2025](https://link.springer.com/article/10.1007/s10999-025-09773-5)) | 역설계 모델 R² 0.949 | 미확인 |
| IPMC·HASEL(제어층) | 3D 프린팅 IPMC의 BO 학습제어 ([IPMC BO 제어, Sci. Rep. 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6877587/)); HASEL 스펙트럼 부분다양체 데이터 모델 ([HASEL 스펙트럼 모델, arXiv 2601.03247](https://arxiv.org/abs/2601.03247)) | 시변 동특성 보상, 추종 오차 크게 감소. 이오노머나 유전 액체 같은 소재 설계에 ML을 쓴 사례는 없다 | 원문확인 |
| LCE(제어·형상층) | 광 패턴 GP-BO로 LCE 마이크로로봇 보행 학습 ([MPI-IS 2018](https://ar5iv.labs.arxiv.org/html/1809.03225)); 진화 알고리즘으로 345,600개 조합 중 가장 빠른 LCE 수영체 선별 ([LCE 수영체 진화탐색, arXiv 2503.00204](https://arxiv.org/abs/2503.00204)); FEM 1,500회로 학습한 앙상블 모델로 배향장→가열 형상 역설계 ([Kent State, APS 2023](https://meetings-archive.aps.org/mar/2023/b14/1)) | 가교제 비율이나 배향 공정 같은 소재 화학을 BO로 최적화한 동료심사 논문은 찾지 못했다 | 미확인 |

G6의 성과는 대부분 "이미 알려진 소재군 안에서 배합·공정·형상을 고르는" 문제였다. 실험 수십~수백 회, 혹은 값싼 자기·탄성 시뮬레이션으로 풀 수 있었다는 공통점이 있다. 반대로 전압·전해질·액정 배향이 얽힌 HASEL·IPMC·LCE의 소재 화학은 시뮬레이터가 부정확하고 시료 제작이 느려 ML이 제어층에 머물렀다. 이 공백이 3장의 첫 우선순위다.

**G7 신축 전도체. 2026년에 처음으로 "ML이 신축 전극을 설계한" 동료심사 사례가 나왔다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 변형 둔감 신축 전극 설계 | UMD Po-Yen Chen 그룹 ([Yang et al., Nat. Commun. 2026-01](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916966/)) | 로봇 자동실험, 능동학습 신경망 앙상블, FE 해석을 결합해 미세 텍스처 나노복합체를 찾았다. 얇은 금층으로 **1,000% 넘게 늘려도 금속 수준 전도도**(그림 설명)를 유지했다. 그 위에 Zn·MnO2를 전착해 신축 Zn‖MnO2 배터리도 만들었다 | 원문확인 |
| 투명 전도성 고분자 박막 공정 | ANL Polybot ([Wang et al., Nat. Commun. 2025](https://www.nature.com/articles/s41467-024-55655-3)) | 7차원 공정 공간을 BO로 탐색해 평균 전도도 4,500 S/cm 이상. 신축성 자체를 겨냥하지는 않았다 | 원문확인 |

UMD 사례가 중요한 이유는 신축 전도체에서 ML의 역할을 "신호 해석(하류)"에서 "소재 설계(상류)"로 옮겼다는 데 있다. 같은 워크플로로 전극과 배터리를 함께 만들었으므로, 신축 에너지 소자(G4)로 확장할 길도 열었다. PEDOT:PSS나 액체금속 복합재의 배합을 ML로 최적화한 논문은 찾지 못했다. 액체금속 분야의 ML은 주로 센싱·제어 쪽이다 ([Chin et al., Adv. Intell. Syst. 2020](https://doi.org/10.1002/aisy.201900171)).

**G8 기능성·지능형 구조. AI 역설계가 가장 성숙한 영역이다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 자가치유 PU 다목적 최적화 | Liang et al. ([Chem. Sci. 2025-12](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758484/)) | 화학 지식을 넣은 능동학습으로 **실험 20개만** 사용. 그래디언트 부스팅+NSGA-III로 강도와 치유의 파레토 전선을 찾았다. 평균 R² 0.8 이상, 종합지수 상대오차 12% 미만 | 원문확인 |
| 4D 프린팅 형상 역설계 | Sun et al. 2024(2-1 참조) | 2-1 참조 | 원문확인 |
| 비선형 메타물질 역설계 | Harvard Bertoldi 그룹, 신경망 가속 진화전략 ([Harvard MRSEC](https://mrsec.harvard.edu/research/highlight_222.php)) | 목표 비선형 응답을 갖는 구조 설계(Adv. Mater. 2022) | 미확인(기관 요약) |
| 그래프 생성 트러스 메타물질 | UC Berkeley GraphMetaMat ([Berkeley Engineering 2025](https://engineering.berkeley.edu/news/2025/07/a-smarter-approach-to-designing-metamaterials/)) | 제조·결함 제약을 반영해 목표 응력-변형 곡선을 맞추는 3D 트러스 생성(Nat. Mach. Intell. 2025) | 언론·기관발표 |
| 키리가미 역설계 | Northwestern ([npj Comput. Mater. 2022](https://www.nature.com/articles/s41524-022-00873-w)) | 군집화, 탠덤 신경망, 기호회귀 | 미확인 |
| 충격흡수 구조 자율실험 | Boston Univ. ([BU 구조 자율실험, arXiv 2308.02315](https://arxiv.org/abs/2308.02315)) | ML이 이끈 적층제조 구조 실험 25,000회 이상 | 미확인(프리프린트) |
| 형상기억 고분자 격자 | 역설계 ML로 박벽 셀룰러 메타물질 탐색 ([SMP 격자 역설계, NSF PAR 2023](https://par.nsf.gov/servlets/purl/10403742)) | "기록적으로 높은 회복응력" 보고 | 미확인 |
| 팽창형 구조 역설계 | 확산모델로 프로그램 가능한 변형을 갖는 팽창 구조 설계 ([팽창 구조 확산모델, arXiv 2508.13097](https://arxiv.org/abs/2508.13097)) | 정량 미추출 | 미확인(프리프린트) |
| 가변강성 재밍 | 입자 재밍 모듈 그레이박스 신경망 ([J. Bionic Eng. 2024](https://doi.org/10.1007/s42235-024-00563-x)) | 가상일 원리와 신경망을 결합(정량 미추출) | 미확인 |

G8이 앞선 이유는 세 가지다. 목표가 응력-변형 곡선이나 목표 형상처럼 수치로 명확하고, FE 해석으로 학습 데이터를 싸게 만들 수 있으며, 결과를 3D 프린팅으로 곧바로 실물화할 수 있다. 자가치유 PU는 예외적으로 화학 소재인데도 성공했다. 소량 데이터에 화학 지식을 넣는 방식이 데이터 부족을 메울 수 있다는 증거다.

**G9 마이크로·바이오 로봇 소재. 형태 설계는 AI가 맡기 시작했지만, 생체·분해성 소재의 배합은 여전히 공백이다.**

| 무엇을 AI로 했나 | 대표 사례 | 정량 성과 | 신뢰도 |
|---|---|---|---|
| 생체 로봇 형태 설계 | 제노봇 ([Kriegman et al., PNAS 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8670470/)) | AI가 설계한 C자형 몸체가 운동학적 자기복제를 최대 2세대에서 **4세대**로 늘렸다 | 원문확인 |
| 근육-지지체 동시 계산설계 | ETH Zürich ([Wevolver 2026](https://www.wevolver.com/article/one-small-leap-for-a-muscle-one-giant-step-for-robotics)) | 배양 근육과 연성 지지체를 계산으로 함께 설계해 액체 속 점프·보행(Nat. Commun. 2026). ML 사용 여부는 불명 | 언론 |
| 촉매 나노모터 설계 | Zeng et al. ([ACS AMI 2019](https://doi.org/10.1021/acsami.9b14792)) | 특징 13개로 속도와 정화 효율을 예측했다. 모델로 설계한 Pt 나노모터의 예측 오차는 15% 미만 | 원문확인(초록) |
| 생분해 고분자 분해 예측 | PLGA 분해 거동 ML ([MGEA 2026](https://journal.hep.com.cn/mgea/EN/10.1002/mgea.70062)) | 로봇 수준 설계와는 아직 연결되지 않았다 | 미확인 |

생분해 전기유압 액추에이터는 200 V/µm에서 10만 회 넘게 작동해 비분해성 소재와 대등했지만, ML 없이 개발됐다 ([Rumley et al., Sci. Adv. 2023](https://doi.org/10.1126/sciadv.adf5551)). 자기 마이크로로봇에서 AI는 주로 강화학습 기반 위치 제어로 쓰인다 ([MDPI 리뷰 2024](https://mdpi.com/2227-7390/12/14/2180)). 생체 소재는 시료마다 편차가 크고 배양에 며칠씩 걸려 데이터 한 점이 특히 비싸다. 그래서 적은 실험으로 최적화하는 BO·능동학습이 가장 잘 맞는 영역인데도, 조직 배합에 적용한 사례는 아직 없다.

### 2-3. 종합 평가

**답:** AI 성숙도는 "데이터 한 점을 얻는 비용"에 반비례한다. 시뮬레이션이나 신호 데이터가 싼 곳은 성숙했고, 합성과 장기 시험이 필요한 곳은 비어 있다.

| 소재 그룹 | AI 성숙도 | 이유 |
|---|---|---|
| G8 기능성 구조(메타물질·4D·자가치유) | **상** | FE 시뮬레이션이 싸고 목표(응력-변형 곡선, 형상)가 명확하다. 역설계·생성모델과 소량 능동학습이 모두 검증됐다 |
| G5 센서·전자피부 | **상**(신호 해석) / **하**(소재 설계) | ML 디코딩은 표준 도구가 됐다. 그러나 센서 소재의 미세구조·배합을 ML로 설계한 예는 프리프린트 수준이다 |
| G6 인공근육·소프트 액추에이터 | **중** | 자기 연성 복합재, TCP, 엘라스토머, DEA 수명 시험에는 정량 성과가 있다. LCE·HASEL·IPMC는 소재 화학 설계가 공백이다 |
| G7 신축 전도체 | **중** | 2026년 UMD가 첫 설계 사례를 냈다. PEDOT:PSS·액체금속 배합은 공백이다 |
| G4 배터리 | **중** | 일반 배터리 소재 AI(전해질 자율실험, 고체전해질 스크리닝)는 활발하다. 로봇 전용 셀·팩 소재 사례는 없다 |
| G9 마이크로·바이오 | **중~하** | 형태 설계(제노봇)와 나노모터 회귀 모델이 있다. 생체조직·생분해 배합의 ML은 없다 |
| G1 구조·경량재 | **하** | 학술 합금 설계와 위상최적화 시제품에 머문다. 양산 로봇 적용 사례는 없다 |
| G3 감속기·트라이볼로지 | **하** | 일반 기어·베어링 강 ML뿐이다. 로봇 감속기 강종 데이터도 비공개다 |
| G2 모터·자석 | **하** | 동료심사 데이터가 없는 기업 주장(MagNex) 하나뿐이다 |

패턴은 분명하다. AI는 **시뮬레이터와 데이터가 싼 곳**에서 가장 강하다. 메타물질, 4D 프린팅, 자기 연성 복합재, 전자피부 디코딩이 여기에 해당한다. 반대로 **실제 로봇의 무게와 비용을 지배하는 부품**(자석, 감속기 강, 엔지니어링 플라스틱)과 **소프트 액추에이터의 화학**(LCE, 이온성 액추에이터)에서는 가장 약하다. 무엇보다 **소프트 액추에이터 소재를 자동으로 합성하고 끝까지 시험하는 폐루프 실험실은 아직 없다.** 현재는 DEA 자동 *시험*(2026 프리프린트)과 신축 전극 자동 *제작+시험*(UMD 2026)이 따로 존재하는 단계다. 결국 AI의 기여는 "로봇이 실제로 쓰는 소재"보다 "AI가 다루기 쉬운 소재"에 먼저 쌓였고, 이 불일치를 줄이는 것이 3장의 과제다.

---

## 3. 남은 문제와 해결 방향

**답:** 남은 문제는 여섯 영역으로 묶인다. 데이터가 적고 편향되어 있고, 시뮬레이션과 현실 사이에 격차가 있으며, 신규성 검증이 약하다. 폐루프 실험과 스케일업이 빠져 있고, 내구성 표준이 없으며, 핵심 부품 소재와 산업이 연결되지 않았다. 해결의 공통 원칙은 "**실패·수명까지 기록하는 데이터, 불확실성을 아는 모델, 사람의 검증, 닫힌 실험 루프**"다.

여섯 영역은 서로 맞물린다. 데이터가 적고 편향되면(데이터) 모델이 분포 밖에서 틀리고(모델), 틀린 예측을 걸러 낼 검증이 약하면 과장된 주장이 나온다(검증·신뢰). 폐루프 실험실(실험·제조)은 데이터 문제의 구조적 해법이지만, 수명 시험 표준(내구성·표준)이 없으면 그 데이터도 서로 비교할 수 없다. 이 모든 것이 갖춰져도 부품사가 데이터를 내놓지 않으면 산업 적용(산업 연결)으로 이어지지 않는다. 아래 표의 A-Lab·GNoME·MatterGen은 로봇 소재 사례가 아니지만, AI 소재 연구 전체의 검증 기준을 바꾼 사건이라 교훈으로 넣었다.

### 3-1. 문제 → 원인 → 해결 방향

| 영역 | 문제 | 원인 | 해결 방향 |
|---|---|---|---|
| **데이터** | 소량 데이터에서 과적합 | 로봇 소재 실험은 한 번에 수십 점이다. 자가치유 PU 연구에서 기존 모델의 테스트 R²는 0.10~0.40에 그쳤다 ([Chem. Sci. 2025-12](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758484/)) | 화학 지식을 넣은 특징과 능동학습을 쓴다. 전문가의 말을 LLM으로 BO 사전분포로 바꾸고, 데이터와 모순되면 자동으로 끄는 방식으로 콜드스타트를 줄인다 ([KRICT, JCIM 2026](https://doi.org/10.1021/acs.jcim.6c00976)) |
| | 부정 결과 부재 | 실패 실험은 출판되지 않는다. 이 선택 편향은 측정 잡음보다 ML 모델을 더 크게 망친다 ([Strieth-Kalthoff 2022, phys.org](https://phys.org/news/2022-06-clearer-negative-experimental-results-reaction.amp)) | 자율실험으로 성공과 실패를 모두 DB에 쌓는다(KAIST·포스코 양극재 랩 방식) ([KAIST 2025](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)) |
| | 내구성 데이터 부족 | 많은 논문이 내구성을 아예 평가하지 않는다 ([HKUST 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)) | 표준 시험 프로토콜을 채택하고, 로봇이 자동으로 수명을 시험해 사이클 수명 데이터셋을 만든다(DEA 시험 로봇 방식) |
| | 형식 불일치 | 소재 데이터베이스마다 스키마가 다르다. 무기 결정 쪽은 OPTIMADE 공통 API에 20개 제공자, 2,500만 개 이상 물질이 연결됐지만 ([OPTIMADE, arXiv 2603.23536](https://arxiv.org/abs/2603.23536)), 소프트 액추에이터·전자피부에는 이런 공통 스키마가 없다 | 액추에이터 성능·수명 메타데이터 스키마를 만들고, NOMAD Oasis처럼 기관별로 선택 공유하는 연합형 저장소를 쓴다 ([NOMAD, CoRDI](https://doi.org/10.52825/cordi.v1i.376)) |
| **모델** | sim-to-real 격차 | 거친 형상·소재 모델, 제조 결함, 점탄성·소성, 히스테리시스가 원인이다. 모델에 없는 거동이 원인이면 시스템 식별도 실패한다 ([RAFL, arXiv 2603.22039](https://arxiv.org/abs/2603.22039)) | 시뮬레이터 위에 잔차를 학습해 보정하고, 공동설계 루프 안에서 실물 시제품을 만들어 본다 ([공동설계 관점 논문, arXiv 2505.03761](https://arxiv.org/abs/2505.03761)). 모듈형 실리콘 키트로 격차 자체를 측정한다 ([Kriegman et al., sim-to-real 키트](https://arxiv.org/abs/1911.10290)) |
| | 분포 밖 일반화 | 데이터 중복 때문에 무작위 분할 평가가 성능을 부풀린다. 최고 성능 GNN도 분포 밖 데이터에서 크게 떨어진다 ([Omee et al., arXiv 2401.08032](https://arxiv.org/abs/2401.08032)) | 군집 제외 교차검증(MatFold) 같은 분포 밖 분할로 평가하고 ([Digital Discovery 2025](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)), 미래 데이터로 전향적으로 검증한다 ([Matbench Discovery](https://arxiv.org/abs/2308.14920)) |
| | 해석성·불확실성 | 블랙박스 모델은 언제 틀릴지 알려 주지 않는다 | 앙상블·분위수 회귀로 불확실성을 정량화한다 ([PNNL, npj 2025](https://www.pnnl.gov/publications/uncertainty-quantification-neural-network-potential-foundation-models)). 이 불확실성을 BO의 탐색 신호로 다시 쓴다 |
| **검증·신뢰** | 신규성 과장 | A-Lab은 "17일간 58개 표적 중 41개 신물질"을 주장했다가 2026년 1월 "57개 중 36개, 예측 플랫폼에 새로울 뿐 과학에 새롭다는 뜻은 아님"으로 정정했다 ([Nature 정정](https://www.nature.com/articles/s41586-025-09992-y)). 외부 분석은 성공으로 보고된 합성물의 약 3분의 2가 이미 알려진 무질서 버전일 가능성이 높다고 봤다 ([Leeman et al., PRX Energy 2024](https://par.nsf.gov/servlets/purl/10532478)). GNoME의 "실험 실현 736개"도 ICSD에 독립 보고된 구조와 일치했다는 뜻이다 ([Merchant et al., Nature 2023](https://www.nature.com/articles/s41586-023-06735-9)). MatterGen이 생성한 TaCr2O6는 1971년에 보고되어 학습 데이터에 이미 있던 Ta1/2Cr1/2O2와 같다는 반론을 받았다 ([Juelsholt, Mater. Horiz. 2026](https://doi.org/10.1039/D6MH00268D)) | 신뢰성·신규성·유용성 3요건을 적용한다 ([Cheetham & Seshadri 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/)). 무질서를 고려한 구조 대조와 전문가 결정학 검토를 의무화한다. 로봇 소재에서는 "새 물질"보다 "목표 물성 달성과 실물 검증"을 성과 기준으로 삼는다 |
| | 벤치마크 누수·소규모 폐쇄 세트 | 전자피부 분류 정확도 92~100%는 대부분 물체 12개 안팎의 닫힌 세트에서 나왔다(분석) | 개방형·공통 물체 세트와 교차 실험실 평가를 도입한다 |
| | 지표 불일치 | LCE 일밀도는 측정법에 따라 63 J/kg(DLP 프린팅)에서 650 J/kg(그래핀-LCE 섬유)까지 벌어진다 ([DLP 프린팅 LCE, Sci. Adv. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8302124/); [그래핀-LCE 섬유, Nat. Nanotechnol. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9646516/)). 자율실험 가속도 보고도 기준선이 제각각이다 | 자율성·처리량·정밀도 등 7개 공통 지표로 보고한다 ([Volk & Abolhasani 2024](https://www.nature.com/articles/s41467-024-45569-5)). 단위와 시험 조건을 함께 표기한다 |
| **실험·제조** | 폐루프 부재 | KAIST 엘라스토머는 수작업 소량 몰드 경화를 썼다. 자율실험실 대부분은 자율성 2~3단계이고, 완전 자율(5단계)은 아직 없다 ([Tom et al., Chem. Rev. 2024](https://doi.org/10.1021/acs.chemrev.4c00055)) | UMD형 자동 제작과 DEA형 자동 수명시험을 한 루프로 결합한다. 목적함수에 초기 성능과 수명을 함께 넣는다 |
| | 고체·분말 핸들링 | 박막·벌크·분말마다 다른 취급이 필요하다 ([NIST 고체 시료 자동화](https://www.nist.gov/node/1874991)). 자석·합금·세라믹 소재 자동화의 병목이다 | 범용 시료 홀더, 기존 장비를 공유하는 이동 로봇 ([Dai et al., Nature 2024](https://www.nature.com/articles/s41586-024-08173-7)), 표준 통신 프로토콜(SiLA·ROS)을 쓴다 |
| | 스케일업·제조성 | 실험실 최적 배합이 양산 공정(사출·다이캐스팅)에서 재현된다는 보장이 없다. Microsoft도 전해질 후보가 "대규모 시험에서 안 될 수 있다"고 밝혔다 ([Microsoft 2024](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)) | GraphMetaMat처럼 제조 제약을 생성 단계에 넣는다. 공정 변수를 설계 변수에 포함한다 |
| | 에이전트 안전 | LLM이 실험을 계획하는 경우, 평가한 19개 모델 중 위험 식별 정확도 70%를 넘은 모델이 없었다 ([LabSafety Bench, Nat. Mach. Intell. 2026](https://arxiv.org/abs/2410.14182)) | 하드웨어·API 수준의 제한된 인터페이스와 사람의 승인 게이트를 둔다 |
| **내구성·표준** | 소프트 액추에이터 피로수명 | 내구성을 높이면 부드러움이 희생된다 ([Tan et al., Chem. Soc. Rev. 2024](https://pubs.rsc.org/en/content/articlehtml/2024/cs/d3cs01017a)). 인간 근육으로 만든 바이오하이브리드 손은 전기자극 10분 만에 수축력이 피로해진다 ([News-Medical 2025](https://www.news-medical.net/news/20250214/Biohybrid-hand-with-muscle-tissue-mimics-real-life-movements.aspx)) | 수명을 최적화 목표에 넣고(NeurIPS 2026이 장기 내구성을 AI 과제로 제시 ([NeurIPS 2026](https://neurips.cc/virtual/2026/167788))), 자가치유 소재와 전이학습 재보정을 함께 쓴다 |
| | 시험 표준 부재 | 사이클 수, 하중, 환경 조건이 논문마다 다르다 | HKUST가 제안한 공압 액추에이터 내구성 프로토콜 같은 표준을 채택하고, 수명 분포(평균이 아닌 분포)를 보고한다 |
| **산업 연결** | 핵심 부품 소재의 AI 공백 | AI로 설계한 소재가 양산 로봇 부품에 쓰였다는 공개 사례가 없다. 감속기 강종·열처리 데이터가 비공개다 | 부품사와 피로·마모 데이터를 함께 만든다. 일반 기어강 모델(TU Delft, ORNL)을 전이학습으로 로봇 감속기에 확장한다 |
| | 공급망(희토류) | Dy/Tb 의존. 무희토 자석의 AI 주장에 독립 검증이 없다 | AI 탐색 결과를 잔류자속·보자력·에너지적과 고온 감자 시험으로 독립 검증한다. 탐색 대상을 Dy 저감 공정까지 넓힌다 |

### 3-2. 우선순위 로드맵

| 단계 | 핵심 행동 | 기대 효과 |
|---|---|---|
| **단기(1~2년)** | ① 실패 결과와 수명 데이터를 공통 스키마로 공개한다 ② 공압·DEA 액추에이터 내구성 시험 표준을 채택한다 ③ 전자피부 평가에 개방형 물체 세트를 쓴다 ④ 검증된 소량 BO·능동학습(TCP 62/1,089, PU 20회)을 LCE·HASEL·IPMC 배합으로 확장한다 ⑤ 신규성 주장에 전문가 검토를 의무화한다 | 가장 싼 공백(액추에이터 화학)부터 메우고, 성과 비교가 가능해진다 |
| **중기(3~5년)** | ① 소프트 액추에이터 합성·제작·수명시험을 하나로 묶은 폐루프 실험실을 구축한다 ② 공동설계에 sim-to-real 잔차 학습과 불확실성 정량화를 넣는다 ③ 부품사와 감속기 강·그리스·PEEK 복합재의 피로·마모 데이터셋을 공동 구축한다 ④ 무희토·저Dy 자석 후보를 독립 기관에서 자기특성으로 검증한다 ⑤ 제조 제약(사출·주조)을 생성 설계에 통합한다 | AI가 로봇 무게와 신뢰성을 좌우하는 부품 소재로 들어간다 |
| **장기(5~10년)** | ① 조성에서 로봇 거동까지 잇는 다중 스케일 소재-구조-제어 공동설계 ② 실험·시뮬레이션·문헌을 함께 학습하는 다충실도 소재 기초모델에 로봇 소재 데이터를 포함한다 ③ 생분해·바이오하이브리드 소재에서 분해 속도와 성능을 함께 최적화한다 | "목표 로봇 성능 → 소재·구조 자동 생성 → 자동 검증" 체계 |

순서를 이렇게 잡은 이유는 비용과 의존성이다. 단기 항목은 새 장비 없이 기존 방법(BO, 표준 프로토콜, 데이터 공개)을 넓히기만 하면 되고, 중기 폐루프 실험실과 부품 데이터셋은 단기에 쌓인 표준 데이터 위에서만 의미가 있다. 장기의 다중 스케일 공동설계는 소재 수준 모델(중기)과 로봇 수준 시뮬레이터(sim-to-real 보정)가 모두 갖춰져야 가능하다.

---

## 4. 결론

(1) AI가 로봇용 소재에 도입된 이유는, 로봇이 경량·고강도·신축·감지·구동·내구성·공급 안정성을 동시에 요구하는데 그 설계공간이 크고 거동이 비선형적이어서 시행착오와 물리모델만으로는 감당할 수 없었기 때문이다. (2) AI는 대리모델, BO·능동학습, 역설계·생성모델, 공동설계, 신호 해석, 자율실험의 여섯 방식으로 적용됐다. 그 결과 수십 번의 실험으로 인공근육·엘라스토머·자가치유 고분자를 최적화했고, 몇 초 만에 로봇 몸체를 설계했으며, 단일 센서로 물체를 식별하는 진전을 이끌었다. (3) 그러나 성과는 데이터가 싼 구조·형상·신호 영역에 몰려 있고, 로봇의 무게와 신뢰성을 지배하는 자석·감속기·플라스틱과 소프트 액추에이터 화학은 비어 있다. 합성부터 수명시험까지 닫힌 실험 루프도 아직 없다. 다음 단계의 관건은 더 큰 모델이 아니라 실패와 수명을 기록하는 데이터, 현실과의 격차를 아는 모델, 사람의 검증, 그리고 핵심 부품 소재로의 확장이다.

---

## 부록 A. 출처 신뢰도 표기

- **원문확인:** 논문 본문·공식 초록·기관 원문을 직접 읽어 수치를 확인했다(프리프린트는 별도 표시).
- **언론·기업주장:** 보도자료, 언론 기사, 기업 발표에서만 확인했다. 독립 검증이 없다.
- **미확인:** 검색 요약이나 2차 자료로만 확인했고, 원문에 접근하지 못했거나 원문에서 해당 수치를 찾지 못했다.

## 부록 B. 접근 상태 요약

- 1차 조사에서는 세션 네트워크 허용 목록 때문에 대부분의 원문 사이트가 DNS 단계에서 차단되어 검색 요약에만 의존했다.
- 사용자가 설정을 바꾼 뒤에는 curl로 대부분 접근할 수 있었다(Nature, arXiv, PMC E-utilities, Europe PMC API, OSTI, NSF PAR, Crossref, NASA NTRS, 기관 보도자료). WebFetch 도구는 계속 DNS 오류를 냈다.
- 남은 차단은 사이트 측 봇 방어와 유료 장벽이다: ACS, RSC, Science, ScienceDirect, APS, Springer, Chemistry World, C&EN, Reuters, IDTechEx 보고서 본문.
- 이 경우 PMC·Europe PMC·OSTI·arXiv 사본으로 우회했다. 그래도 읽지 못한 수치(NASA NiTi 오차, Karacakol의 "53회 실행", Bertoldi 원문 등)는 "미확인"으로 표시하거나 보고서에서 뺐다.

## 참고문헌

1. [IDTechEx 기고, R&A News 2026](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)
2. [Gasgoo 2026](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)
3. [Haines et al., Science 2014](https://api.openalex.org/works/doi:10.1126/science.1246906)
4. [SuperTac, Nature Sensors 2026](https://www.nature.com/articles/s44460-025-00006-y)
5. [HKUST 내구성 리뷰 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)
6. [humanoid.guide 플렉스플라인](https://humanoid.guide/?p=20671)
7. [Figure F.03 배터리 2025](https://figure.ai/news/f-03-battery-development)
8. [Adamas 2026](https://www.adamasintel.com/humanoid-robotics-sector-accelerates-on-multiple-commercialization-fronts-in-march/)
9. [CSIS](https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions)
10. [Karacakol et al., Nat. Commun. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947188/)
11. [Mining.com, MagNex 2024](https://www.mining.com/ai-helps-quickly-develop-rare-earth-free-permanent-magnet/)
12. [PLoS ONE 리뷰 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)
13. [HASEL 스펙트럼 모델, arXiv 2601.03247](https://arxiv.org/abs/2601.03247)
14. [Columbia, JACS Au 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10052236)
15. [공동설계 관점 논문, arXiv 2505.03761](https://arxiv.org/abs/2505.03761)
16. [New Atlas 2024](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery/)
17. [MGI 백서](https://www.mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf)
18. [디지털타임스 2026-04-30](https://v.daum.net/v/20260430155346042)
19. [Zeng & Su, NSF PAR](https://par.nsf.gov/servlets/purl/10557920)
20. [Adesiji et al., arXiv 2508.06642](https://arxiv.org/abs/2508.06642)
21. [인공피부 역설계, arXiv 2304.04609](https://arxiv.org/abs/2304.04609)
22. [Yan et al., Sci. Robot. 2021](https://doi.org/10.1126/scirobotics.abc8801)
23. [Burger et al., Nature 2020](https://www.nature.com/articles/s41586-020-2442-2)
24. [NASA NTRS, MS&T22 초록](https://ntrs.nasa.gov/citations/20220005395)
25. [Materials & Design 2025](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat)
26. [Sun et al., Nat. Commun. 2024](https://www.nature.com/articles/s41467-024-49775-z)
27. [Matthews et al., PNAS 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10576117/)
28. [MIT News 2025](https://news.mit.edu/2025/using-generative-ai-help-robots-jump-higher-land-safely-0627)
29. [Kim et al. (서울대 고승환 그룹), Nature Materials 2025](https://www.nature.com/articles/s41563-025-02373-w)
30. [arXiv 2602.20963, 2026](https://arxiv.org/abs/2602.20963)
31. [Spielberg et al., Robotica 2021](https://cdfg.csail.mit.edu/assets/files/robotica.pdf)
32. [DiffuseBot, NeurIPS 2023](https://arxiv.org/abs/2311.17053)
33. [J. Mater. Inform. 2025](https://www.oaepublish.com/articles/jmi.2024.92)
34. [사족 로봇 다리 위상최적화, Sci. Rep. 2023](https://www.nature.com/articles/s41598-023-32106-5)
35. [FH OÖ, German Robotics Conf. 2025](https://pure.fh-ooe.at/en/publications/ai-driven-topology-optimized-modular-robotic-arm-design-for-legge/)
36. [Figure 03 공개 2025](https://www.figure.ai/news/introducing-figure-03)
37. [TU Delft 피로강 ML](https://repository.tudelft.nl/record/uuid:470d0944-7409-4633-9e61-23092137c72d)
38. [ORNL 베이나이트강](https://ornl.gov/technology/202405685)
39. [Friction 2025](https://sciopen.com/article/10.26599/FRICT.2025.9440982)
40. [Harmonic Drive LLC](https://www.harmonicdrive.net/technology/harmonicdrive)
41. [humanoid.guide 힘줄](https://humanoid.guide/?p=16664)
42. [Microsoft 2024](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)
43. [Dave et al., Nat. Commun. 2022](https://www.nature.com/articles/s41467-022-32938-1)
44. [KAIST 2025](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)
45. [ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing)
46. [칭화대 2026](https://www.tsinghua.edu.cn/info/1175/123978.htm)
47. [Liu et al., Science 2024](https://doi.org/10.1126/science.adk5556)
48. [China Daily](https://govt.chinadaily.com.cn/s/202406/05/WS6673996e498ed2d7b7eb0c2c/chinese-scientists-design-bio-inspired-3d-e-skin.html)
49. [Microsyst. Nanoeng. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11543809/)
50. [Sensors 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8125695/)
51. [Adv. Intell. Syst. 2022](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d)
52. [Song et al., Nat. Commun. 2026-06](https://www.nature.com/articles/s41467-026-73735-4)
53. [J. Mater. Sci. 2022](https://link.springer.com/article/10.1007/s10853-022-07793-6)
54. [하이드로겔 BO, PMC11422183](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11422183/)
55. [하이드로겔 GAN, PMC11165469](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11165469/)
56. [PNIPAM 자율실험, arXiv 2509.05351](https://arxiv.org/abs/2509.05351)
57. [DEA 하이브리드 모델, arXiv 2202.12977](https://arxiv.org/abs/2202.12977)
58. [Int. J. Mech. Mater. Des. 2025](https://link.springer.com/article/10.1007/s10999-025-09773-5)
59. [IPMC BO 제어, Sci. Rep. 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6877587/)
60. [MPI-IS 2018](https://ar5iv.labs.arxiv.org/html/1809.03225)
61. [LCE 수영체 진화탐색, arXiv 2503.00204](https://arxiv.org/abs/2503.00204)
62. [Kent State, APS 2023](https://meetings-archive.aps.org/mar/2023/b14/1)
63. [Yang et al., Nat. Commun. 2026-01](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916966/)
64. [Wang et al., Nat. Commun. 2025](https://www.nature.com/articles/s41467-024-55655-3)
65. [Chin et al., Adv. Intell. Syst. 2020](https://doi.org/10.1002/aisy.201900171)
66. [Chem. Sci. 2025-12](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758484/)
67. [Harvard MRSEC](https://mrsec.harvard.edu/research/highlight_222.php)
68. [Berkeley Engineering 2025](https://engineering.berkeley.edu/news/2025/07/a-smarter-approach-to-designing-metamaterials/)
69. [npj Comput. Mater. 2022](https://www.nature.com/articles/s41524-022-00873-w)
70. [BU 구조 자율실험, arXiv 2308.02315](https://arxiv.org/abs/2308.02315)
71. [SMP 격자 역설계, NSF PAR 2023](https://par.nsf.gov/servlets/purl/10403742)
72. [팽창 구조 확산모델, arXiv 2508.13097](https://arxiv.org/abs/2508.13097)
73. [J. Bionic Eng. 2024](https://doi.org/10.1007/s42235-024-00563-x)
74. [Kriegman et al., PNAS 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8670470/)
75. [Wevolver 2026](https://www.wevolver.com/article/one-small-leap-for-a-muscle-one-giant-step-for-robotics)
76. [ACS AMI 2019](https://doi.org/10.1021/acsami.9b14792)
77. [MGEA 2026](https://journal.hep.com.cn/mgea/EN/10.1002/mgea.70062)
78. [Rumley et al., Sci. Adv. 2023](https://doi.org/10.1126/sciadv.adf5551)
79. [MDPI 리뷰 2024](https://mdpi.com/2227-7390/12/14/2180)
80. [KRICT, JCIM 2026](https://doi.org/10.1021/acs.jcim.6c00976)
81. [Strieth-Kalthoff 2022, phys.org](https://phys.org/news/2022-06-clearer-negative-experimental-results-reaction.amp)
82. [OPTIMADE, arXiv 2603.23536](https://arxiv.org/abs/2603.23536)
83. [NOMAD, CoRDI](https://doi.org/10.52825/cordi.v1i.376)
84. [RAFL, arXiv 2603.22039](https://arxiv.org/abs/2603.22039)
85. [Kriegman et al., sim-to-real 키트](https://arxiv.org/abs/1911.10290)
86. [Omee et al., arXiv 2401.08032](https://arxiv.org/abs/2401.08032)
87. [Digital Discovery 2025](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)
88. [Matbench Discovery](https://arxiv.org/abs/2308.14920)
89. [PNNL, npj 2025](https://www.pnnl.gov/publications/uncertainty-quantification-neural-network-potential-foundation-models)
90. [Nature 정정](https://www.nature.com/articles/s41586-025-09992-y)
91. [Leeman et al., PRX Energy 2024](https://par.nsf.gov/servlets/purl/10532478)
92. [Merchant et al., Nature 2023](https://www.nature.com/articles/s41586-023-06735-9)
93. [Juelsholt, Mater. Horiz. 2026](https://doi.org/10.1039/D6MH00268D)
94. [Cheetham & Seshadri 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/)
95. [DLP 프린팅 LCE, Sci. Adv. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8302124/)
96. [그래핀-LCE 섬유, Nat. Nanotechnol. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9646516/)
97. [Volk & Abolhasani 2024](https://www.nature.com/articles/s41467-024-45569-5)
98. [Tom et al., Chem. Rev. 2024](https://doi.org/10.1021/acs.chemrev.4c00055)
99. [NIST 고체 시료 자동화](https://www.nist.gov/node/1874991)
100. [Dai et al., Nature 2024](https://www.nature.com/articles/s41586-024-08173-7)
101. [LabSafety Bench, Nat. Mach. Intell. 2026](https://arxiv.org/abs/2410.14182)
102. [Tan et al., Chem. Soc. Rev. 2024](https://pubs.rsc.org/en/content/articlehtml/2024/cs/d3cs01017a)
103. [News-Medical 2025](https://www.news-medical.net/news/20250214/Biohybrid-hand-with-muscle-tissue-mimics-real-life-movements.aspx)
104. [NeurIPS 2026](https://neurips.cc/virtual/2026/167788)
