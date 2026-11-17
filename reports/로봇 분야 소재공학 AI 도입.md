# 로봇과 AI, 소재 개발의 시계를 다시 맞추다

재료공학에 인공지능이 들어온 이유는 두 가지가 겹쳤기 때문이다. 신소재 하나를 시장에 내놓기까지 **10~20년, 최대 약 1억 달러**가 드는 시행착오식 개발 방식이 한계에 부딪혔다. 그리고 고처리량 계산과 AI가 **수백만 개의 후보 물질을 쏟아냈지만 실제로 합성된 것은 수백 개에 그쳤다**(GNoME 220만 개 예측, 독립 합성 736개). 이 간극을 메우려고 "AI가 제안하고, 로봇이 합성·분석하고, 결과로 모델이 다시 학습하는" 폐루프, 즉 자율실험실(self-driving lab, SDL)이 등장했다. 반대 방향에서도 수요가 생겼다. 소프트 액추에이터, 전자피부, 메타물질, 휴머노이드 부품처럼 로봇이 쓰는 소재는 비선형성과 히스테리시스가 강하고 설계 공간이 거대하다. 그래서 물리 모델만으로 설계하기 어렵고, 데이터 기반 역설계가 필요해졌다. 성과는 분명하지만 영역에 따라 편차가 크다. **정해진 공간 안의 최적화**에서는 동료심사 문헌 기준으로 기준 전략 대비 **중앙값 약 6배 가속**이 확인되었다. 로봇용 소재에서도 1,089개 조합 중 62개만 만들어 최적 액추에이터를 찾거나, 다중 모달 전자피부의 인식 정확도를 65%에서 95%로 끌어올리는 등 부품·구조 수준의 실증이 쌓였다. 반면 **"신소재 발견"이라는 주장**은 크게 흔들렸다. A-Lab은 2026년 1월 Nature 정정으로 신규성 주장을 축소했고, GNoME과 MatterGen도 "이미 알려진 무질서 상을 새 정렬 구조로 오인했다"는 비판을 받았다. 한편 민간 자본(Periodic Labs, Lila Sciences, CuspAI 등)은 검증된 산출물보다 훨씬 앞서 달리고 있다. 남은 과제는 데이터 편향·누수, 분말·고체 핸들링과 특성분석 자동화, 분포 밖(OOD) 일반화와 LLM 에이전트 안전, 소프트 소재의 내구성과 sim-to-real 격차, 인력과 비용이다. 전문가들이 제시하는 해법은 처리량 경쟁에서 **"검증 가능한 자율성"**으로 옮겨가고 있다. 다만 이 보고서는 네트워크 정책 때문에 학술·언론·정부 원문에 직접 접근하지 못한 채 검색 결과 요약을 근거로 작성되었다. 따라서 핵심 수치는 원문과 대조해 확인해야 한다(아래 "접근 차단 사이트 및 조사 한계" 참조).

## 20년·1억 달러의 개발 주기와 '예측 과잉'이 AI와 로봇을 불러들였다

### 시행착오 패러다임의 비용이 정책 의제가 되었다

AI 도입의 출발점은 시간이다. 미국 재료게놈이니셔티브(MGI)는 2011년 백서에서 첨단소재를 "지금보다 최소 두 배 빠르게, 비용은 일부만 들여" 발견·개발·제조·배치하겠다는 목표를 세웠다([MGI white paper](https://mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf)). JACS 관점 논문도 전통적 소재 발견에 "평균 최대 20년"이 걸린다고 정리한다([JACS perspective](https://iris.polito.it/bitstream/11583/2981642/1/jacs.2c06833.pdf)). 토론토대 Acceleration Consortium은 이 문제를 **"소재 하나당 20년·1억 달러를 1년·100만 달러로"**라는 구호로 압축했다([U of T Engineering News](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/)). 한국 과학기술정보통신부도 2026년 전략에서 기존 소재 연구가 "연구자의 경험과 반복 실험에 의존"해 **개발부터 상용화까지 10~20년 이상** 걸린다고 진단했다([다음/뉴스 2026-04-30](https://v.daum.net/v/20260430155346042); [헤럴드경제](https://www.heraldk.com/article/2026042918221956653)). 2011년 미국, 2016년 중국, 2023년 캐나다, 2026년 한국이 같은 틀을 쓴다. "10~20년을 절반으로, 또는 1~2년으로" 줄이는 것이 AI 소재 정책의 표준 명분이 되었다.

시간 문제 밑에는 탐색 공간의 크기가 있다. 30개 이하 중원자로 된 안정한 소분자만 **10^60개 이상**으로 추정되며, 무기 원소를 더하면 공간은 더 커진다([arXiv 1510.07512](https://arxiv.org/pdf/1510.07512)). 이 공간을 직관과 반복 실험으로 훑는 것은 불가능에 가깝다. 2010년대 초부터 고처리량 DFT 데이터베이스가 ML이 쓸 "연료"를 공급하기 시작했다. AFLOWLIB은 첫 논문에서 15만 건 이상이던 합금 열역학 항목이 2017년 **170만 건 이상**으로 늘었다([AFLOWLIB](https://bsg.byu.edu/docs/papers/aflowlib.pdf); [AFLOW Fleet](https://ar5iv.labs.arxiv.org/html/1712.00422)). 그러나 Hegde 등은 서로 다른 HT-DFT 데이터베이스 간 차이가 DFT와 실험 간 차이에 맞먹는 경우가 많다고 보였다([arXiv 2007.01988](https://arxiv.org/abs/2007.01988v2)). 계산만으로는 신뢰할 만한 정답을 얻을 수 없고, 실제 실험 데이터를 대량으로 만들어야 한다는 결론이 여기서 나왔다.

### 계산이 만든 '예측 과잉'이 로봇 실험을 필연으로 만들었다

2023년 11월 Google DeepMind의 GNoME은 **220만 개의 결정 구조를 예측**했다. 그중 약 38만 개를 안정한 것으로 판정해 Materials Project에 추가했지만, 당시 독립적으로 합성된 것은 **736개**뿐이었다([Berkeley Lab News](https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/)). 예측과 합성 사이의 이 수천 배 격차가 로봇 자율실험의 직접적 근거다. 로봇은 24시간 쉬지 않고 실험을 반복한다. 실패한 실험까지 표준화된 형식으로 기록하며, 위험 물질에 사람이 노출되는 것을 줄인다([NCSU](https://cbe.ncsu.edu/?p=24420); [UvA chapter](https://pure.uva.nl/ws/files/225440366/Chapter_1.pdf)). 미국 MGI의 2021·2024 문서도 "확장 가능하고 공유 가능한 형식의 고품질·재현 가능한 데이터"를 만드는 자율 시스템을 요구한다([IFP](https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf), 검색 요약만 확인). 아시아에서는 인구 구조도 명분이 된다. KAIST 서동화 교수는 POSCO홀딩스와 만든 양극재 자율실험실을 연구 인력 감소(저출생)에 대한 대응으로 설명했다([Asiae](https://www.asiae.co.kr/en/article/2025080309221574066)). 일본 SDL 리뷰는 2023년 세계 산업용 로봇 시장에서 일본 점유율이 46%라는 점을 SDL 전략의 기반으로 든다([RSC Digital Discovery](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d4dd00387j), 검색 요약).

### 로봇이 쓰는 소재는 비선형성과 공급망 때문에 AI 설계가 필요했다

"로봇 영역"에는 반대 방향도 있다. 로봇은 소재를 만드는 도구이면서 소재를 소비하는 쪽이기도 하다. 소프트 로봇의 센서·액추에이터 소재는 **비선형성과 히스테리시스** 때문에 모델링과 제어가 어렵다. PLoS ONE 리뷰는 이 점을 ML 도입의 핵심 동기로 정리한다([PMC7891779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)). 설계 공간도 크다. 액정 엘라스토머(LCE) 수영 로봇 연구는 **345,600개 파라미터 조합** 중 가장 빠른 설계를 진화 알고리즘으로 찾았다([arXiv 2503.00204](https://arxiv.org/pdf/2503.00204v3)). 산업 쪽 압력은 휴머노이드 붐에서 나온다. 휴머노이드 한 대에는 **NdFeB 희토류 영구자석이 약 3.5~4 kg** 들어간다는 추정이 있다([Meticulous Research](https://www.meticulousresearch.com/meticulous-next/humanoid-robot-components-outlook-2026-2036)). Adamas Intelligence는 NdFeB 자석을 로보틱스의 최대 장애물로 꼽는다. 일론 머스크는 2025년 1분기 실적 발표에서 Optimus 생산이 중국의 희토류 자석 수출 통제에 묶여 있다고 말했다([Adamas Intelligence](https://www.adamasintel.com/humanoid-robots-and-the-future-of-motors-and-ndfeb-markets/)). 정밀 감속기 증설에는 24~36개월이 걸린다. S&P Global은 금속 공급 부족이 로봇 확산을 늦출 수 있다고 경고했다([S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/2/robot-rise-could-be-slowed-by-metals-shortage-98483872)). IDTechEx는 2026~2027년을 휴머노이드가 파일럿에서 양산으로 넘어가는 전환기로 본다([IDTechEx](https://idtechex.com/en/research-report/humanoid-robots/1149)). 희토류 저감 자석, 경량 구조재, 고에너지 배터리를 더 빨리 찾아야 한다는 산업적 동기가 AI 소재 탐색과 직접 연결되는 것이다.

### 각국 정책은 '데이터베이스'에서 '자율실험실'로 옮겨갔다

정책의 흐름은 미국이 의제를 세우고 1~5년 안에 각국이 따라가는 패턴을 두 번 반복했다. 2011년 MGI 이후 일본 MI2I(2015), 영국 Royce(2015), 중국 재료게놈공정(2016)이 데이터·계산 인프라를 깔았다. 2025~2026년에는 미국 Genesis Mission에 이어 한국 K-문샷(언론은 "美 제니시스 미션 맞선 K-문샷"으로 보도)이 나왔고, 이번에는 자율실험실이 중심이다([뉴시스 2026-02-25](https://www.newsis.com/view/NISX20260225_0003525436)).

| 국가·지역 | 시기 | 프로그램 | 규모·목표 | 출처 |
|---|---|---|---|---|
| 미국 | 2011 | Materials Genome Initiative | "2배 빠르게"; 2016년까지 연방 투자 2.5억 달러 이상 | [NIST MGI at 5](https://www.nist.gov/system/files/documents/2018/06/26/mgi-accomplishments-at-5-years-august-2016.pdf) |
| 미국 | 2025-11 | Genesis Mission (EO 14363) | 핵심 소재를 우선 분야로 지정, 240일 내 국립연구소의 로봇 실험실·AI 주도 실험 역량 검토; 2026-03 DOE 공모 약 2.93억 달러(3.2억 달러라는 분석도 있음); 2026-07 50억 달러 이상 약정 발표(이차 출처) | [MoFo](https://www.mofo.com/resources/insights/251211-executive-order-establishes-genesis-mission); [HPCwire](https://www.hpcwire.com/2026/03/18/doe-announces-293m-funding-opportunity-as-genesis-mission-moves-toward-operational-phase/); [GrantedAI](https://grantedai.com/blog/doe-genesis-mission-293-million-ai-scientific-discovery-funding-strategy-2026); [AI Weekly](https://aiweekly.co/alerts/trump-unveils-5b-genesis-mission-doe-picks-278-ai-projects) |
| 캐나다 | 2023-04 | Acceleration Consortium (CFREF) | C$2억(캐나다 대학 사상 최대), U of T C$1.3억 추가 | [U of T Engineering](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/) |
| EU | 2020~2024 | BIG-MAP (Battery 2030+) | 발견 속도 5배 이상; 예산 €1,600만(Fraunhofer) vs €2,000만(CIDETEC) | [Fraunhofer ISC](https://isc.fraunhofer.de/en/press-and-media/press-releases/EU-project-BIG-MAP-development-of-the-next-generation-of-super-batteries.html); [CIDETEC](https://energystorage.cidetec.es/proyectos/big-map) |
| EU | 2024-02 | COM(2024)98 첨단소재 전략 | AI 기반 Materials Commons; 2025~2027 파트너십 €5억 목표 | [EC R&I](https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/key-enabling-technologies/chemicals-and-advanced-materials/advanced-materials-industrial-leadership_en) |
| 영국 | 2015~2026 | Henry Royce Institute; AI for Science Strategy | £2.35억(2015); AI for Science 최대 £1.37억 | [UKRI](https://www.ukri.org/who-we-are/epsrc/centres-and-institutes/henry-royce-institute/); [GOV.UK](https://www.gov.uk/government/publications/ai-for-science-strategy/ai-for-science-strategy) |
| 중국 | 2016 / 2025 / 2026 | 재료게놈공정 중점 R&D; 국무원 "AI+" 의견; 베이징 AI 과학연구 실행계획(2026~2028) | 개발 기간·비용 절반; 자율실험실 시스템을 첫 축으로 | [Engineering](https://www.engineering.org.cn/en/article/28200/detail); [Geopolitechs](https://www.geopolitechs.org/p/china-releases-ai-plus-policy-a-brief); [Beijing gov](https://english.beijing.gov.cn/investinginbeijing/InvestmentSpecial/DigitalEconomy/PolicesAndInterpretations/202607/t20260715_4763931.html) |
| 일본 | 2015~2020 / ~2050 | NIMS MI2I; 문샷 목표 3 | 2050년까지 자율적으로 과학 원리를 발견하는 AI 로봇 | [NIMS](https://archive.nims.go.jp/eng/news/press/2015/09/201509020.html); [내각부](https://www8.cao.go.jp/cstp/english/moonshot/sub3_en.html) |
| 한국 | 2019 → 2026 | 소부장 R&D(5조 원 이상) → AI 소재 R&D 플랫폼 구축 전략(2026~2030), K-문샷, 자율실험실 산·학·연 협의체 | AI-ready 데이터 5년 1,000만 건·10년 5,000만 건, 분야별 24시간 'AI소재 전용 자율실험센터', 석사 300명·박사 75명 이상 양성; 바이오 자율실험실 2028년까지 495억 원 | [뉴시스 2019](https://www.newsis.com/view/NISX20190827_0000752621); [다음](https://v.daum.net/v/20260430101533808); [아시아경제](https://view.asiae.co.kr/article/2026081109490769317); [헤럴드](https://biz.heraldcorp.com/article/10780079) |

정책 목표치는 2배(MGI), 절반(중국), 5배 이상(BIG-MAP), 10~20배(Acceleration Consortium) 사이에 흩어져 있다. 실측 근거는 다음 절에서 볼 "SDL 캠페인당 중앙값 약 6배"다. 이 수치는 실험 단위의 최적화 속도를 잰 것이지, 실험실에서 시장까지 걸리는 전체 기간을 잰 것이 아니다.

## 자율실험실은 '최적화'에서 중앙값 6배 가속을 입증했다

### 단일 목적 루프에서 LLM 에이전트 실험실까지 10년의 진화

자율실험실은 10년 사이 크게 바뀌었다. 2016년 미 공군연구소(AFRL)의 ARES는 in situ 라만 분광을 목적함수로 삼아 **600회 이상 자율 실험**으로 탄소나노튜브 성장 속도를 학습했다([AF.mil](https://www.af.mil/News/Article-Display/Article/982368/afrl-system-revolutionizes-research-process/)). 2020년 리버풀대 Cooper 그룹의 이동형 로봇 화학자는 레이저 내비게이션으로 실험실을 돌아다녔다. 10개 변수 공간에서 **8일간 688회 실험**을 수행했고, 초기 배합보다 **6배 활성이 높은 광촉매**를 찾았다([Liverpool repository](https://livrepository.liverpool.ac.uk/3095139/)). 같은 해 UBC의 Ada는 박막 정공수송층의 이동도를 베이지안 최적화로 끌어올렸다([UBC CAIDA](https://caida.ubc.ca/node/59)). 2022년 CMU의 Clio+Dragonfly는 **42회 실험, 이틀 작업으로 고속충전 전해질 6종**을 찾았다. 같은 로봇에서 무작위 탐색보다 6배 빨랐고, 파우치셀에서 상용 기준 대비 약 13% 개선을 보였다([Nature Communications](https://www.nature.com/articles/s41467-022-32938-1.pdf)).

2023년 말에는 대형 사건이 몰렸다. 버클리연구소 A-Lab(17일간 58개 목표 중 41개 "신규" 화합물 합성 주장), 중국과기대(USTC)의 로봇 AI 화학자, GPT-4 기반 Coscientist가 연달아 발표되었다. USTC 시스템은 화성 운석 원소로 **300만 개 이상 조성 공간**을 탐색해 OER 촉매를 만들었고, 이 촉매는 10 mA cm⁻²에서 55만 초 이상 안정했다([CAS](https://english.cas.cn/newsroom/cas_media/202311/t20231115_643207.shtml)). Coscientist는 Opentrons와 Emerald Cloud Lab을 조작해 Pd 촉매 Suzuki·Sonogashira 커플링을 최적화했다([PMC10733136](https://pmc.ncbi.nlm.nih.gov/articles/PMC10733136)). 2024년에는 IBM RoboRXN 위에서 18개 전문 도구를 쓴 ChemCrow([Nature MI](https://www.nature.com/articles/s42256-024-00832-8.pdf)), 문헌보다 나은 수율을 **약 80% 사례**에서 낸 암스테르담대 RoboChem([UvA HIMS](https://hims.uva.nl/content/news/2024/01/autonomous-synthesis-robot-uses-ai-to-speed-up-chemical-discovery.html)), 1.75 m 이동 로봇 두 대가 사람과 같은 장비(UPLC-MS, 벤치탑 NMR)를 공유하며 탐색 합성을 판단한 리버풀 후속 연구가 나왔다([Liverpool news](https://news.liverpool.ac.uk/?p=123346)). 3개 대륙 5개 실험실을 하나의 캠페인으로 묶어 **유기 고체 레이저 소재 21종**을 찾은 "분산형 SDL"도 이 시기 성과다([Materials Square](https://community.materialssquare.com/t/21-new-laser-materials-uncovered-in-groundbreaking-global-study/355)). 2025년 아르곤연구소 Polybot은 7차원 공정 공간에서 PEDOT:PSS계 투명 전도막의 **평균 전도도를 4,500 S/cm 이상**으로 올리고 데이터를 공개했다([ANL](https://www.anl.gov/article/selfdriving-lab-transforms-materials-discovery)).

2026년의 키워드는 다중 에이전트와 국가 인프라다. 선전 그룹의 MARS는 **LLM 에이전트 19개와 도메인 도구 16개**를 로봇 실험과 묶어 페로브스카이트 나노결정 합성을 10회 반복 안에 최적화했다([Phys.org](https://phys.org/news/2026-01-multi-agent-ai-robots-automate.html), 검색 요약). 일본 NIMS는 오래된 액체 핸들러까지 SDL로 엮는 오픈소스 오케스트레이터 NIMS-OS/NIMO를 공개했다([NIMS MDR](https://mdr.nims.go.jp/datasets/05a74658-08b8-433a-8106-5c98dfb3a0bd?locale=en)). KRICT는 연구자의 자연어 경험을 실험 계획의 사전지식으로 바꾸는 대화형 AI를 내놓았다([EurekAlert](https://www.eurekalert.org/news-releases/1148248)).

### AI는 다섯 층에 들어가지만, 실증 성과의 엔진은 여전히 베이지안 최적화다

SDL에서 AI는 다섯 층에 들어간다. (1) 표적·가설 생성(DFT/ML 안정성 예측, GNoME·Materials Project), (2) 레시피·실험 계획(문헌 학습 NLP·LLM, 베이지안 최적화·능동학습), (3) 로봇 실행과 오케스트레이션(고정 워크셀, 이동 매니퓰레이터, 클라우드 랩, LLM 도구 사용), (4) 특성분석 자동 해석(ML 기반 XRD 상 판별, NMR/MS 해석, 물리 기반 현미경 제어), (5) 추론·지식 축적(다중 에이전트, 자연어 사전지식)이다. A-Lab은 문헌으로 학습한 레시피 모델과 열역학 기반 능동학습을 결합했다([OSTI](https://www.osti.gov/pages/servlets/purl/2281696)). ORNL은 시료의 **1% 미만**만 촬영한 상태에서 출발해 물리 기반 ML로 주사탐침현미경을 자율 운용했다([ORNL](https://www.ornl.gov/news/self-driving-microscopes-discover-shortcuts-new-materials)).

그러나 동료심사를 거친 정량 성과(6배 활성, 6배 가속, 4,500 S/cm, 80% 수율 우위)는 거의 모두 **가우시안 과정 기반 베이지안 최적화**라는 표본 효율적 블랙박스 최적화에서 나왔다. LLM은 범용성을 높이는 "접착제" 역할을 한다. 계획을 세우고, 코드를 생성하고, 도구를 연결한다. 신뢰성은 아직 부족하다. ChemCrow는 예측한 절차가 "용매 부족", "잘못된 정제 동작" 때문에 그대로 실행되지 않는 한계를 스스로 보고했다([Nature MI](https://www.nature.com/articles/s42256-024-00832-8.pdf)). 2026년 9월 리뷰도 LLM 에이전트는 계획·도구 조정에 가장 유용하며, 최적화·물리적 타당성·안전에는 여전히 전문 기법과 명시적 제약이 필요하다고 평가했다([Nanowerk](https://www.nanowerk.com/spotlight/spotid=70238.php), 검색 요약).

### 측정된 가속은 '6배'이고, '2,000년→6주'는 측정값이 아니다

보스턴대 연구진은 SDL 문헌을 메타 분석했다. 보고된 **가속 계수(AF)의 중앙값은 6**이었고, 파라미터 공간의 차원이 높을수록 커졌다. 향상 계수는 두 자릿수 이상 차이가 났다([arXiv 2508.06642](https://arxiv.org/pdf/2508.06642); [Digital Discovery](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00337g)). Volk과 Abolhasani는 자율도, 운영 수명, 처리량, 실험 정밀도, 소재 사용량, 접근 가능한 파라미터 공간, 최적화 효율이라는 **7개 성능 지표**를 제안했다. 그러면서 최적화 속도는 연구 간 비교가 어렵고 무작위 샘플링 같은 기준선과 비교해야 한다고 경고했다([NC State](https://news.ncsu.edu/?p=770545)). 이 기준으로 보면, 언론이 붙인 "인간보다 1,000배 빠른 로봇"([THE](https://www.stg.timeshighereducation.com/node/696379))이나 USTC 촉매의 "인간이면 2,000년" 같은 표현은 측정된 가속이 아니라 외삽이다([Phys.org](https://phys.org/news/2023-11-ai-chemist-catalyst-oxygen-production.pdf)).

| 시스템 | 시기 | 정량 결과 | 검증 수준 |
|---|---|---|---|
| AFRL ARES (CNT 성장) | 2016~17 | 자율 실험 600회 이상 | 동료심사·기관 보도 ([AF.mil](https://www.af.mil/News/Article-Display/Article/982368/afrl-system-revolutionizes-research-process/)) |
| 리버풀 이동형 로봇 화학자 | 2020 | 8일 688회, 광촉매 활성 6배 | 동료심사 Nature ([Liverpool](https://livrepository.liverpool.ac.uk/3095139/)) |
| CMU Clio + Dragonfly | 2022 | 42회 실험으로 전해질 6종, 무작위 대비 6배, 고속충전 13% 개선 | 동료심사 Nat. Commun. ([Nature](https://www.nature.com/articles/s41467-022-32938-1.pdf)) |
| LBNL A-Lab | 2023, 2026 정정 | 41/58 "신규" → 정정 후 36건(플랫폼 기준 "신규") | 동료심사 + 정정, 논쟁 중 ([C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01?sc=230901_cenrssfeed_eng_latestnewsrss_cen)) |
| USTC 로봇 AI 화학자 | 2023 | 300만 개 이상 조성 공간, 445.1 mV 과전압, 55만 초 이상 안정 | 동료심사 Nat. Synth. ([CAS](https://english.cas.cn/newsroom/cas_media/202311/t20231115_643207.shtml)) |
| UvA RoboChem | 2024 | 주당 10~20개 분자, 약 80% 사례에서 문헌보다 높은 수율 | 동료심사 Science ([UvA](https://hims.uva.nl/content/news/2024/01/autonomous-synthesis-robot-uses-ai-to-speed-up-chemical-discovery.html)) |
| ANL Polybot | 2025 | 7차원 공정, 평균 4,500 S/cm 이상 | 동료심사 Nat. Commun. ([ANL](https://www.anl.gov/article/selfdriving-lab-transforms-materials-discovery)) |
| NIMS 고분자 SDL | 2025 | 연 1만 개 이상 시료 | 학회 초록 ([CSJ](https://pub-files.atlas.jp/fs/public/csj105th/ver_28/session/en/1E_F40101-03.pdf)) |
| KIST 스마트랩 | 2025-12 | 약 1만 회 탐색 대상을 24회 실험으로, 1주 미만 | **언론 보도만** ([Daum](https://v.daum.net/v/20251217175541326)) |
| KAIST·POSCO 양극재 자율실험실 | 2025-08 | 연구자 주도 대비 데이터 12배 | **기업·언론 주장** ([Asiae](https://www.asiae.co.kr/en/article/2025080309221574066)) |
| MARS (선전) | 2026 | 10회 반복 내 페로브스카이트 나노결정 최적화 | 동료심사 Matter ([Phys.org](https://phys.org/news/2026-01-multi-agent-ai-robots-automate.html)) |
| SynAgent | 2026-09 | 18회 실험으로 LiCoO₂ 박막 최적 기판 온도 구간 탐색 | **프리프린트** ([arXiv](https://arxiv.org/abs/2609.18598)) |
| Lila Sciences | 2026-09 | 3개월 2,942개 촉매, Pd계 산성 OER 1,000시간 이상 | **기업 발표 + 프리프린트** ([Unite.AI](https://www.unite.ai/lila-sciences-ai-lab-uncovers-palladium-catalysts-for-green-hydrogen/)) |

### 제조 현장의 '자율'은 실험실보다 한 단계 늦다

로봇 기반 소재 가공과 제조(적층제조, 용접, 복합재)에서도 ML은 들어와 있다. 다만 주로 in situ 모니터링, 결함 탐지, 파라미터 조정 수준이다. 2026년 리뷰에 따르면 로봇 적층제조의 강화학습 연구는 대부분 시뮬레이션에 머물러 있고, 디지털 트윈이나 축소 모델로 폐루프 학습까지 간 연구는 소수다([Whiterose review](https://eprints.whiterose.ac.uk/id/eprint/240849/1/1-s2.0-S1526612526004342-main.pdf)). DED/WAAM에서도 제한적인 폐루프 제어와 장비 간 일반화 실패가 핵심 과제로 꼽힌다([MDPI Metals](https://mdpi.com/2075-4701/15/9/966)). 상업적으로 가장 앞선 사례는 AI 비전 기반 자율 로봇 용접이다. Path Robotics는 2026년 11월 **기업가치 24.5억 달러에 3억 달러 시리즈 E**를 유치했다([Robotics 24/7](https://www.robotics247.com/article/path-robotics-announces-300m-series-e-financing-at-2.45b-valuation)). 다만 고객 생산성 지표를 독립적으로 검증한 자료는 없다.

## 로봇용 소재에서 AI는 원자보다 배합·구조·형태를 설계한다

### 데이터 희소성이 방법론을 결정한다

로봇용 소재에서 AI가 다루는 대상은 원자 배열보다 한 단계 위다. 배향장(director field), 격자 위상, 엘라스토머 배합, 몸체 형상이 주 대상이다. 방법은 데이터가 얼마나 있느냐에 따라 갈린다. 실험 데이터가 적으면 베이지안 최적화와 능동학습을, 시뮬레이터가 싸면 대리 신경망과 진화·경사 탐색을, 미분 가능한 시뮬레이터가 있으면 확산모델 기반 공동설계를 쓴다. 대표 사례는 다음과 같다. 열구동 코일형 고분자 액추에이터 연구는 이산 베이지안 최적화로 **1,089개 공정 조합 중 62개만 제작해 1.25의 구동 변형률**을 달성했다([Aalto](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat/)). 자성 소프트 캔틸레버의 역설계 모델은 R² 0.9490을 기록했다([Springer](https://link.springer.com/article/10.1007/s10999-025-09773-5)). LCE 기반 스마트 메타물질은 신경망과 진화 전략으로 응력-연신 응답을 정밀 역설계했다([BUAA](https://research.buaa.edu.cn/zh/publications/inverse-design-of-smart-mechanical-metamaterials-based-on-liquid-/)). 한국에서는 KAIST·KIST·서울과기대 팀이 AI로 DLP 3D 프린팅용 고무형 소재의 최적 배합을 찾았다. 이 소재는 **원래 길이의 6배 이상** 늘어나도 찢어지지 않았고, 이를 쓴 소프트 로봇 손은 달걀부터 1 kg 물병까지 쥐었다(Nature Communications, 2025)([AlphaGalileo](https://www.alphagalileo.org/en-gb/Item-Display/ItemId/277480)).

### 메타물질과 몸체 설계는 진화 탐색에서 생성모델로 넘어갔다

메타물질에서는 그래프 기반 생성 설계가 주류가 되었다. UC Berkeley의 GraphMetaMat(Nature Machine Intelligence, 2025년 7월)은 3D 트러스 메타물질을 그래프로 처음부터 쌓아 올린다. 노드와 엣지를 반복해서 더하면서 목표 응력-변형 곡선에 맞추고, 제조 결함 제약도 반영한다([Berkeley Engineering](https://engineering.berkeley.edu/news/2025/07/a-smarter-approach-to-designing-metamaterials/)). 트러스 격자의 비선형 거동을 담은 그래프 VAE 잠재공간도 2023년 Nature Communications에 실렸다([Nature Communications](https://www.nature.com/articles/s41467-023-43217-y)). 몸체와 소재의 공동설계 쪽에서는 속도가 크게 빨라졌다. 노스웨스턴대 Kriegman 그룹은 형태 없는 블록에서 걷는 소프트 로봇을 노트북으로 **약 26초** 만에 설계했고, 이를 실리콘으로 주조해 실제로 걷게 했다(PNAS, 2023)([ScienceDaily](https://sciencedaily.com/releases/2023/10/231003173425.htm)). MIT CSAIL의 DiffuseBot은 확산모델 샘플링에 미분 가능한 소프트바디 시뮬레이션을 결합해 6개 과제에서 비교 기법을 앞섰다(NeurIPS 2023)([NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8b1008098947ad59144c18a78337f937-Abstract.html)). 2025년 MIT의 확산모델 재설계 점프 로봇은 곡선형 "드럼스틱" 링크로 에너지를 더 저장해, 사람이 설계한 버전보다 **약 41% 높이** 뛰었고 착지 성능은 84% 개선되었다([MIT Schwarzman College](https://computing.mit.edu/news/using-generative-ai-to-help-robots-jump-higher-and-land-safely/)). 흐름을 정리하면, 블랙박스 진화 탐색(2020~2021)에서 미분 가능·확산 기반 공동설계(2023~2025)를 거쳐 그래프·연산자 학습으로 소재 아키텍처 자체를 역설계하는 단계(2025~2026, 상당수는 프리프린트)로 이어진다([arXiv 2508.13097](https://arxiv.org/pdf/2508.13097); [arXiv 2601.11126](https://arxiv.org/pdf/2601.11126)).

### 전자피부에서 ML은 '싸고 성긴 센서'를 쓸모 있게 만드는 소재 설계 수단이다

전자피부(e-skin)에서 ML은 이제 신호 해석의 기본 도구다. 2025년 Nature Materials의 열·기계 다중 모달 e-skin은 단일 모달로는 약 **65%이던 분류 정확도를 결합 시 95%**로 높였다. 무선 보드를 단 손끝 버전은 일상 물체 20종을 83% 정확도로 식별했다([ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing), 언론 요약). 2026년 1월 Nature Sensors의 SuperTac은 힘 0.06 N, 위치 0.4 mm의 정밀도를 보고했다([ElectronicsForU](https://www.electronicsforu.com/?p=194182), 검색 요약). 자가치유 소재와 ML의 결합도 자연스럽다. 소재가 회복되면 학습이 신호 매핑을 복구하는 식이다. 케임브리지 연구에서 자가치유 감지 피부는 5,000회 탐침 학습 후 터치 위치를 2.3 mm로 추정했고, 손상 후에는 전이학습으로 **200회 미만 탐침**만에 재적응했다([DOAJ](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d)). 옥스퍼드의 고속 자가치유 e-skin은 10초 안에 기능의 약 80%를 회복했다고 보고했다([Oxford ORA](https://ora.ox.ac.uk/objects/uuid:149873d8-5227-4cbb-a6f8-5dc61f397e9d)). 이런 성과는 단순한 소프트웨어 개선이 아니다. EIT 방식이나 단일 시트형 피부처럼 배선과 소재 구조를 단순하게 만들 수 있게 하므로 소재 설계의 수단이기도 하다.

### 휴머노이드와 AI 소재의 연결은 아직 '스타트업 주장'과 '범용 플랫폼'을 거친다

휴머노이드 산업의 소재 병목(희토류 자석, 감속기, 경량재, 배터리)과 AI 소재 탐색은 개념상 바로 이어진다. 그러나 이번 조사에서 Tesla, Figure, Unitree, 현대차·Boston Dynamics, 삼성·레인보우로보틱스, UBTech, Xiaomi 가운데 **AI 기반 소재 개발 프로그램을 공개한 곳은 찾지 못했다**. 현재 연결 고리는 스타트업과 범용 플랫폼이다. 영국 Materials Nexus는 AI로 1억 개 이상 조성을 걸러 희토류 없는 자석 "MagNex"를 약 3개월 만에 개발했다고 밝혔다. 희토류 자석 대비 소재 비용 약 20%, 탄소배출 약 70% 감소를 주장하지만, **잔류자화·보자력·에너지적 같은 자기 성능 비교는 공개되지 않았고**, 로봇 모터에 채택된 사례도 없다([New Atlas](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery/)). 배터리 쪽에서는 GNoME이 기존 연구보다 25배 많은 고체 리튬이온 전도체 후보를 제시했다([VentureBeat](https://venturebeat.com/ai/google-deepminds-materials-ai-has-already-discovered-2-2-million-new-crystals/)). Microsoft와 PNNL은 3,200만 후보에서 출발해 **리튬을 약 70% 덜 쓰는 고체전해질** NaxLi3−xYCl6을 합성했지만 양산 단계는 아니다([Utility Dive](https://www.utilitydive.com/news/pnnl-microsoft-artificial-intelligence-research-battery/704176/)). 휴머노이드 경량화에서는 PEEK가 알루미늄 골격 무게를 40% 줄이고 Optimus Gen2가 10 kg을 감량했다는 이야기가 돈다. 그러나 출처는 블로그뿐이고 Tesla가 확인한 바 없다([PEEK China blog](https://peekchina.blogspot.com/2025/05/exploring-lightweight-materials-in.html)). 한국 배터리 업계는 InterBattery 2026에서 로봇을 새 수요처로 내세웠다([Korea Times](https://www.koreatimes.co.kr/amp/business/tech-science/20260302/interbattery-2026-to-become-battlefield-for-courting-robotics-firms)). 로봇과 소재의 관계가 "AI가 로봇용 소재를 빠르게 찾는다"와 "로봇이 소재 기업의 새 시장이 된다"라는 두 방향으로 동시에 움직이는 셈이다. 학계 리뷰는 여전히 냉정하다. Science Robotics(2025)는 대부분의 소프트 로봇이 외부 자극을 인위적으로 조작해야 하는 "초보적" 물리지능 수준에 머물러 있다고 평가했다([Yale Faboratory](https://www.eng.yale.edu/faboratory/publications\journal\2025\Chen%20-%202025%20-%20Advancing%20physical%20intelligence%20for%20autonomoussoft%20robots.pdf)). 새로운 소프트 로봇 소재 화학(예: 새 LCE)을 처음부터 끝까지 합성하는 폐루프 SDL은 이번 조사에서 확인되지 않았다. 확인된 것은 파라미터 최적화 수준의 연구다.

## 자본은 검증된 산출물보다 먼저 달려가고 있다

### 빅테크는 기반 모델을, 스타트업은 '물리적 실험실'을 판다

산업 구조는 세 층으로 정리된다. 첫째 층은 빅테크가 공개하는 기반 모델과 데이터다. GNoME, Microsoft MatterGen과 MatterSim, Meta FAIR의 OMol25(1억 건 이상 DFT 계산, 약 60억 CPU-시간)와 UMA가 여기에 속한다([Meta AI](https://ai.meta.com/blog/meta-fair-science-new-open-source-releases/)). 둘째 층은 연산·도구다. NVIDIA ALCHEMI가 대표적이며, ENEOS는 이를 써서 액침냉각 후보 약 1,000만 개와 OER 촉매 후보 약 1억 개를 "수 주" 만에 평가했다고 발표했다([ENEOS](https://www.hd.eneos.co.jp/english/news/release_information/year/2025/20251205_02_01_mr03/)). 셋째 층은 폐루프 실험실이다. DeepMind는 2025년 12월 Gemini 기반 자동화 소재 실험실을 2026년 영국에 열겠다고 발표했지만, 2026년 11월 현재 개소는 확인되지 않았다([TechRadar](https://www.techradar.com/pro/google-deepmind-partners-with-the-uk-government-for-science-breakthroughs-cleaner-energy)). 빅테크가 첫째 층을 무료로 풀면 "모델만 가진" 스타트업은 설 자리가 좁아진다. 2025~2026년 대형 투자가 물리적 실험실을 가진 기업에 몰린 이유를 이것으로 설명할 수 있다.

| 기업 | 최근 자금 조달 | 시점 | 비고 |
|---|---|---|---|
| Periodic Labs (미국) | 시드 3억 달러; 2026년 약 70~75억 달러 가치 협상 보도 | 2025-09/10; 2026 | 리드 투자자 a16z vs Felicis로 보도 엇갈림, 2026 라운드 미확정 ([SiliconANGLE](https://siliconangle.com/2025/10/01/periodic-labs-raises-300m-accelerate-scientific-research-ai/); [Contrary](https://research.contrary.com/company/periodic-labs/quick-facts)) |
| Lila Sciences (미국) | 누적 약 5.5억 달러, 가치 13억 달러 이상; 2026 시리즈 B 20억 달러 설(說) | 2025; 2026-06 | 시리즈 B는 미확정 ([Sacra](https://sacra.com/c/lila-sciences/); [Caplight](https://www.caplight.com/company/lila-sciences)) |
| CuspAI (영국) | 시리즈 A 1억 달러 → 시리즈 B 약 4.5억 달러(가치 26억 달러) | 2025-09 → 2026-07 | 45개 이상 파트너의 AI Materials Foundry, 삼성벤처스·현대차 참여 ([Sifted](https://sifted.eu/articles/cuspai-lands-450m-round-to-accelerate-ai-materials-discovery)) |
| Radical AI (미국) | 시드 5,500만 달러 | 2025-07 | 하루 최대 50회 실험(목표 100회), 일부 공정은 반자율 ([R&D World](https://www.rdworldonline.com/how-radical-ai-is-building-a-self-driving-materials-lab/)) |
| DP Technology (중국) | 시리즈 C 8억 위안 이상(약 1.1억 달러) | 2025-12 | 국가 연계 펀드 참여 ([SCMP](https://www.scmp.com/business/companies/article/3337648/ai-science-start-dp-technology-raises-us114-million-series-c-round)) |
| Path Robotics (미국) | 시리즈 E 3억 달러(가치 24.5억 달러; Automate.org는 22.5억 달러) | 2026-11 | AI 자율 용접 ([The Next Web](https://thenextweb.com/news/path-robotics-300m-series-e-2-45bn-valuation); [Automate.org](https://www.automate.org/robotics/industry-insights/path-robotics-raises-300m-at-2-25b-valuation)) |

시장 규모 추정은 범위 정의에 따라 한 자릿수 이상 차이가 난다. IDTechEx는 외부 제공 소재 인포매틱스 시장을 **2034년 7.25억 달러**로 본다([IDTechEx](https://www.idtechex.com/ja/research-report/materials-informatics-2025/1096)). MarketsandMarkets는 일반 실험실 자동화 시장을 2030년 90.1억 달러로 추정한다([Barchart](https://www.barchart.com/story/news/35736121/lab-automation-market-growth-drivers-and-opportunities-marketsandmarkets)). Astute Analytica는 "실험실 자동화와 SDL"을 합쳐 2035년 200억 달러로 본다([Astute Analytica](https://www.astuteanalytica.com/industry-report/lab-automation-and-self-driving-lab-market)). Lux Research는 2025년 한 해에만 소재 인포매틱스 스타트업에 6억 달러 이상이 투자되었다고 집계했다([Lux Research](https://luxresearchinc.com/blog/a-guide-to-using-ai-in-materials-rd/)). CuspAI 한 회사의 기업가치(26억 달러)가 IDTechEx가 추정한 2034년 시장 전체의 세 배를 넘는다. 투자자들은 소프트웨어 매출이 아니라 소재 IP와 제품에서 나올 가치를 사고 있다는 뜻이다. 그러나 AI가 발견한 소재가 대규모로 상용화된 사례는 아직 공개되지 않았다.

### 기업 성과 수치는 대부분 자체 발표이며 '후보 도출 시간'과 '시장 출시 시간'을 섞는다

산업 현장의 정량 성과는 거의 모두 기업 사례 연구와 보도자료에서 나온다. Citrine은 Dorfner의 배합 개발 기간을 84% 줄였다고 밝혔다. HRL의 3D 프린팅용 항공 알루미늄 합금은 실험 기간을 "수년에서 수일로" 줄였고, 논문 발표 약 2년 뒤 상용 제품이 나왔다고 소개한다([Citrine HRL](https://CITRINE.IO/wp-content/uploads/2021/04/Case-Study-HRL-AM-powder-development.pdf)). LG AI연구원은 EXAONE Discovery로 42만 개 후보를 하루 만에 걸러 신소재 성분을 찾았다고 밝혔다. 기존 방식으로는 22개월이 걸렸다는 것이 LG의 설명이다([Korea Herald](https://www.koreaherald.com/article/10872720)). Microsoft Discovery는 PFAS 없는 액침냉각제 시제품을 약 200시간 만에 찾았다고 했다([VentureBeat](https://venturebeat.com/ai/microsoft-just-launched-an-ai-that-discovered-a-new-chemical-in-200-hours-instead-of-years)). 모두 **독립 감사가 없는 기업 주장**이다. 이런 사례는 "후보 도출 시간(시간~일)"을 "시장 출시 시간"처럼 보이게 하는 경향이 있다. 실제 소재 인증, 스케일업, 신뢰성 평가는 여전히 수년이 걸린다(PNNL 전해질은 양산 전 단계). 로봇 액추에이터, 배터리, 경량 합금처럼 내구성이 중요한 로봇 소재에서 이 간극은 특히 크다. 특허 제도도 같은 방향을 가리킨다. 한국 지식재산처의 AI 시대 특허 출원 가이드는 검증하지 않은 AI 생성 실험 데이터로 출원하면 실시가능성 결여로 거절되거나 무효가 될 수 있다고 경고한다. AI가 설계한 화합물과 부품 형상에는 재현성 증거가 필요하다는 것이다([Law Times](https://www.lawtimes.co.kr/news/articleView.html?idxno=227594)). 로봇 실험실은 이런 맥락에서 발견 엔진이면서 동시에 특허용 실시가능성 데이터를 만드는 장치이기도 하다.

## A-Lab·GNoME·MatterGen 논쟁은 '발견'의 기준을 다시 썼다

### 세 개의 대표 성과가 같은 이유로 비판받았다

2023~2025년 AI 소재 분야를 대표한 세 성과가 모두 고체화학자들로부터 같은 방식의 비판을 받았다. **A-Lab**(Nature, 2023년 11월)은 17일간 58개 목표 중 41개의 "신규" 화합물을 합성했다고 주장했다. UCL의 Palgrave와 프린스턴의 Schoop은 자동 XRD 정련이 "매우 초보적"이었고, 예측 화합물의 약 3분의 2가 이미 알려진 무질서 화합물의 정렬 버전이라고 반박했다([Chemistry World](https://chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article); [Nature News](https://www.nature.com/articles/d41586-023-03956-w)). 2024년 PRX Energy 논문에서는 "출판 시점에 새로운 소재는 하나도 없었다"고 결론지었다([NSF PAR](https://par.nsf.gov/servlets/purl/10532478)). Ceder는 MnAgO₂ 등 일부가 신규가 아님을 인정하면서도, 목표는 "최고 수준의 인간이 할 수 있는 일"이 아니라 "자율실험실이 할 수 있는 일"을 보이는 것이었다고 반론했다([Ceder LinkedIn](https://www.linkedin.com/pulse/regarding-our-recent-a-lab-article-gerbrand-ceder-0sz6c)). 결국 Nature는 **2026년 1월 19일 저자 정정(Author Correction)**을 냈다. 논문은 철회되지 않았다. 대신 "신규"의 의미를 "과학계에 새로운 것"이 아니라 "예측 플랫폼에 새로운 것"으로 재정의했고, 학습 데이터에 있던 Zn₂Cr₃FeO₈을 제외했다. Palgrave는 논문이 "덜 흥미로워졌지만 그렇게 결함이 많지는 않다"고 평했지만, Schoop은 완전히 만족하지 않았다([C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01?sc=230901_cenrssfeed_eng_latestnewsrss_cen); [UMN experts](https://experts.umn.edu/en/publications/author-correction-an-autonomous-laboratory-for-the-accelerated-sy/)).

**GNoME**에 대해서는 Cheetham과 Seshadri가 Chem. Mater.(2024)에서 비판했다. 유용한 예측은 **신뢰성·신규성·유용성**을 모두 갖춰야 하는데, 이 세 조건을 충족하는 화합물의 증거는 "빈약하다(scant)"는 것이다. 384,870개 조성의 상당수가 이미 ICSD에 있는 구조를 취하고, 실제로는 정렬되지 않을 금속 이온 배열에 기대고 있으며, 기능이 입증되지 않아 아직 "소재"로 볼 수 없다고 지적했다([PMC11044265](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265)). Seshadri는 "AI 자체의 문제가 아니라 사용 방식의 문제"라고 했고, DeepMind는 "모든 주장을 고수한다"고 답했다([The Register](https://www.theregister.com/2024/04/11/google_deepmind_material_study/)). Johannes Margraf는 GNoME의 안정 예측 중 80~84%가 실제로는 무질서 상일 가능성이 높다고 추정했다(이차 출처)([hyper.ai](https://hyper.ai/en/stories/44d9f45779e4d8c1b15691c9a6245a19)). **MatterGen**(Nature, 2025년 1월)에 대해서는 Juelsholt가 Materials Horizons(2026)에서 비판했다. 실험으로 검증된 "신규" TaCr₂O₆은 1972년에 보고된 Ta₁/₂Cr₁/₂O₂와 동형이고 학습 데이터에도 있었으며, 합성 시료는 무질서 상이었다는 것이다. Juelsholt는 "예측 화합물 하나하나를 사람이 검사해야 신규성을 보장할 수 있다"고 결론지었다([Materials Horizons](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d6mh00268d)). Microsoft는 무질서 인식 구조 매칭 알고리즘을 대응책으로 제시했지만([Microsoft Research blog](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai)), Juelsholt에 대한 직접 반박은 확인되지 않았다.

세 사례에는 공통 구조가 있다. (i) DFT·생성 파이프라인은 실험적으로 자리 무질서 고용체인 물질을 정렬된 단위세포로 출력한다. (ii) ICSD 조회나 구조 매처 같은 자동 신규성 검사는 이를 걸러내지 못한다. (iii) 자동 XRD 정련은 표적이 합성되었다고 잘못 "확인"한다. 그래서 자동 특성분석은 처리량만의 병목이 아니다. 결과가 맞는지를 좌우하는 정확도의 병목이기도 하다. 이 논쟁 이후 독립적인 실험 검증이 AI 소재 분야에서 신뢰를 얻는 기준이 되었다. 2026년 9월에는 AI가 제안한 초전도체를 사전 등록된 "물리 판정" 절차로 검증하자는 프리프린트가 "생성은 발견이 아니다"라는 표어를 내걸기도 했다([arXiv 2609.10614](https://arxiv.org/html/2609.10614)).

### 동료심사 결과와 기업·언론 주장을 구분해야 한다

| 검증 수준 | 대표 주장 | 판단 |
|---|---|---|
| 동료심사 + 독립 재현·비판 통과 | Clio 6배, Burger 6배 활성, RoboChem 80%, Polybot 4,500 S/cm, SDL 중앙값 AF 6 | 정해진 공간의 최적화 성과로서 가장 신뢰할 만함 |
| 동료심사 후 정정·논쟁 중 | A-Lab(정정), GNoME 신규성, MatterGen TaCr₂O₆ | 플랫폼 능력 실증으로는 유효, "신소재 발견" 주장은 축소해서 읽어야 함 |
| 프리프린트 | A-Lab GPSS, SynAgent, Lila 촉매, 확산모델 기반 팽창 구조 | 동료심사 전 |
| 기업·언론 주장 | KIST "24회 실험", KAIST·POSCO "12배 데이터", MagNex 비용 20%, LG "1일 vs 22개월", Citrine 84%, CoolScan 4배, Lila "백금보다 1,000배→10,000배 저렴" | 독립 검증 없음. Lila 비용 주장은 반복 인용되면서 배수가 커졌고 새 데이터는 없음([Mentat](https://mentat-s3r.pages.dev/finds/lila-sciences-platinum-free-catalysts-10000x-cheaper)) |
| 블로그·확인 불가 | Optimus PEEK 10 kg 감량·30% 속도 향상 | 근거 부족 |

### 출처마다 다른 수치

| 항목 | 수치 A | 수치 B | 비고 |
|---|---|---|---|
| A-Lab 정정 후 결과 | 보고된 성공 40건 중 36건 정확, 4건 불확정([C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01?sc=230901_cenrssfeed_eng_latestnewsrss_cen)) | 목표 57개 중 36개([kingy.ai](https://kingy.ai/mathematics-science-breakthrough-tracker/records/science-correction-2026-a-lab-autonomous-materials/); [Nanowerk](https://www.nanowerk.com/spotlight/spotid=70238.php)) | 정정문 원문 미확인. 수작업 XRD 재검토에서 약 12% 오귀속이라는 보도도 있음([Helix/Medill](https://helix.medill.northwestern.edu/2026/04/21/ai-generated-crystals-scientists-weigh-risks-and-rewards-automated-materials-discovery/), 스니펫) |
| A-Lab 비판 대상 수 | "신규" 41개 | 43개 중 약 3분의 2([postcutoff](https://postcutoff.com/e/2023-11-29-a-lab-autonomous-synthesis-dispute/)); 35개 분석([The Register](https://www.theregister.com/2024/01/31/ai_chemistry_research_disputed/)) | 이차 출처 간 불일치 |
| GNoME 안정 구조 수 | 약 38만 개([LBNL](https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/)) | 384,870개 조성([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265)) | 독립 합성: 736개(2023) vs DeepMind의 "700개 이상" |
| USTC 탐색 공간·기간 | 300만 개 이상, 약 6주([CAS](https://english.cas.cn/newsroom/cas_media/202311/t20231115_643207.shtml)) | 370만 개 이상(같은 CAS 기사와 [SCMP](https://www.scmp.com/news/china/science/article/3195880/chinese-made-robot-pushing-boundaries-chemical-and-clean-energy)를 인용한 다른 노트); "2개월 vs 인간 2,000년"([China Daily](https://subsites.chinadaily.com.cn/hefeiht/2023-11/16/c_939441.htm)) | 학습 데이터도 "이론 3만+실험 240" vs "논문 5만 편 이상"으로 엇갈림 |
| Microsoft/PNNL 최종 후보 | 23개(5개는 기존 물질)([Microsoft](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)) | 18개([Utility Dive](https://www.utilitydive.com/news/pnnl-microsoft-artificial-intelligence-research-battery/704176/)) | — |
| Genesis Mission DOE 공모 | 약 2.93억 달러([HPCwire](https://www.hpcwire.com/2026/03/18/doe-announces-293m-funding-opportunity-as-genesis-mission-moves-toward-operational-phase/)) | 3.2억 달러([GrantedAI](https://grantedai.com/blog/doe-genesis-mission-293-million-ai-scientific-discovery-funding-strategy-2026)) | 50억 달러 이상 약정은 이차 출처 |
| BIG-MAP 예산 | €1,600만([Fraunhofer](https://isc.fraunhofer.de/en/press-and-media/press-releases/EU-project-BIG-MAP-development-of-the-next-generation-of-super-batteries.html)) | €2,000만([CIDETEC](https://energystorage.cidetec.es/proyectos/big-map)) | — |
| Acceleration Consortium SDL 수 | 7개([Global News](https://globalnews.ca/news/9657567/ai-canada-university-of-toronto-self-driving-lab-research-grant-acceleration-consortium)) | 6개([U of T Engineering](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/)) | — |
| Path Robotics 기업가치 | 24.5억 달러([Robotics 24/7](https://www.robotics247.com/article/path-robotics-announces-300m-series-e-financing-at-2.45b-valuation)) | 22.5억 달러([Automate.org](https://www.automate.org/robotics/industry-insights/path-robotics-raises-300m-at-2-25b-valuation)) | — |
| Orbital Materials 시리즈 B | 5,000만 달러(2026-05)([Fortune](https://fortune.com/2026/05/28/exclusive-orbital-industries-raises-50-million-series-b-funding-round-ai-to-discover-exotic-new-materials/)) | "2억 달러, 가치 12억 달러"([Salestools](https://salestools.io/report/orbital-materials-raises-200m-series-b)) | 후자는 미검증 |
| Polybot 게재지 | Nature Communications 2025(DOI로 확인)([RePEc](https://ideas.repec.org/a/nat/natcom/v16y2025i1d10.1038_s41467-024-55655-3.html)) | 검색 요약상 "Computing & AI Connect 2026" | DOI 기준이 맞음 |

## 남은 병목은 데이터·고체 핸들링·검증·내구성이며, 해법은 '검증 가능한 자율성'이다

### 데이터: 알고리즘보다 편향과 누수가 먼저 문제다

소재 ML의 첫 번째 제약은 알고리즘이 아니라 데이터다. Strieth-Kalthoff 등은 반응 수율 예측 모델이 측정 잡음에는 강하지만, 실패한 반응을 보고하지 않는 **인간 선택 편향**에는 크게 흔들린다는 것을 보였다([phys.org](https://phys.org/news/2022-06-clearer-negative-experimental-results-reaction.amp)). 데이터 중복과 누수는 정확도를 부풀린다. 초전도 Tc 모델을 군집 단위로 떼어내 교차검증(LOCO-CV)하자, 무작위 분할에서 보였던 일반화 성능이 "크게 과대평가"되어 있었음이 드러났다([Digital Discovery MatFold](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)). Materials Project로 학습한 모델은 새로 추가된 항목에서 성능이 급락했다([arXiv 2210.13597](https://www.arxiv.org/pdf/2210.13597)). 0 K DFT 안정성은 유한 온도 효과를 무시하고, 문헌에서 추출한 합성 레시피 모델은 합성 가능성을 과대평가한다([arXiv 2602.04075](https://arxiv.org/pdf/2602.04075)). 생성모델의 신규성 실패도 같은 뿌리에서 나온다. 학습 데이터의 이웃을 다시 찾아내면 보상받는 구조인 것이다. 해법은 세 갈래로 수렴한다. 첫째, FAIR 인프라다. OPTIMADE는 2026년 3월 현재 20개 데이터베이스 제공자와 2,500만 개 이상 소재를 하나의 API로 묶었다([arXiv 2603.23536](https://arxiv.org/html/2603.23536v1)). NOMAD Oasis는 연구실이 데이터를 "선택적으로 공유"하게 해 IP 우려를 일부 덜어준다([FAIRmat](https://indico.desy.de/event/45458/contributions/178565/attachments/94106/127917/20241128_PUNCH_FAIRmat_SB.pdf)). 둘째, 실패를 포함한 모든 시도를 기록하는 SDL 자체가 음성 데이터 부족을 해결하는 구조적 수단이다. 셋째, 국가 단위의 AI-ready 데이터 구축이다. 한국의 1,000만→5,000만 건 목표가 그 예다([다음](https://v.daum.net/v/20260430155346042)). 다만 산업 컨소시엄의 데이터 신탁이나 연합학습 같은 IP 보존형 공유 사례는 이번 조사에서 찾지 못했다.

### 하드웨어: 소재 SDL은 액체가 아니라 분말과 고체를 다뤄야 한다

소재 SDL의 하드웨어 문제는 화학·바이오 SDL보다 어렵다. NIST는 박막, 벌크, 분말이 각각 다른 핸들링을 요구한다며 "고체 시료를 옮기는 것"을 소재 자동화의 고유 과제로 꼽고, 범용 시료 홀더를 제안했다([NIST](https://www.nist.gov/node/1874991)). 분말 XRD의 종단간 자동화는 분말 취급과 시료 준비 때문에 특히 어렵다([arXiv 2501.06847](https://arxiv.org/html/2501.06847v1)). 토론토 그룹은 "SDL을 염두에 두고 제품을 설계하는 장비 제조사가 거의 없다"고 지적했다([Chemspeed](https://www.chemspeed.com/news/autonomous-chemical-experiments-challenges-and-perspectives-on-establishing-a-self-driving-lab)). Chem. Commun.(2025)은 실제로 구축·운용된 SDL이 적은 주된 이유로 학제 간 협업과 시스템 통합의 어려움을 들었다([Chem. Commun.](https://pubs.rsc.org/he/content/articlehtml/2025/cc/d5cc01959a)). 해법은 모듈화와 네트워크화다. 장비 통신 표준 SiLA 2와 로보틱스 미들웨어 ROS의 결합([SLAS Technology](https://real.mtak.hu/206359/1/02_1-s2.0-S2472630324000505-main.pdf)), 기존 장비를 사람과 공유하는 이동 로봇(리버풀), 고가 SDL의 핵심 원리만 담은 저가 "frugal twin"([Digital Discovery](https://pubs.rsc.org/en/content/articlehtml/2024/dd/d4dd00059e)), 그리고 유연한 플랫폼·AI 의사결정·분산 실험실 네트워크를 묶은 "SDL 2.0" 로드맵([Materials Horizons](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d5mh01984b))이 제시되어 있다. Pickles 등(Matter, 2026)은 독점 소프트웨어와 기관 간 칸막이를 극복하려면 상호운용성·안전·재현성 표준이 필요하다고 정리했다([Strathprints](https://strathprints.strath.ac.uk/95936/7/Pickles-etal-Matter-2026-community-discussion-on-harmonizing-and-accelerating-self-driving-laboratories.pdf)). 합성 가능성 예측도 병행해야 할 과제다. 열역학적 안정성은 유용한 1차 필터일 뿐 충분조건이 아니며([Bartel group](https://bartel.cems.umn.edu/sites/bartel.cems.umn.edu/files/2026-08/schlesinger.bartel_2026-materhoriz.pdf)), SynthNN과 SynCoTrain 같은 ML 기반 합성가능성 모델이 그 빈틈을 메우려 하고 있다.

### AI 모델과 안전: OOD 일반화와 에이전트형 LLM의 위험

모델 쪽의 핵심 약점은 분포 밖(OOD) 일반화다. MatBench 상위 GNN들은 OOD 과제에서 CGCNN이나 ALIGNN보다 오히려 덜 견고했다([arXiv 2401.08032](https://arxiv.org/pdf/2401.08032.pdf)). Matbench Discovery의 범용 원자간 퍼텐셜은 안정성 사전 선별에서 F1 0.57~0.82를 기록했지만, 저자들 스스로 회귀 지표와 실제 분류 과제가 어긋난다고 밝혔다([LBL](https://eta-publications.lbl.gov/bibcite/reference/36666)). MLIP Arena는 기존 벤치마크가 데이터 누수와 오차 지표 의존에 시달린다고 보고했다([NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/file/bfa45223cc236855dbaa5c468c809896-Paper-Datasets_and_Benchmarks_Track.pdf)). 대응책은 불확실성 정량화(UQ)다. PNNL은 MACE-MP-0에 판독층 앙상블과 분위 회귀를 적용했다([PNNL](https://www.pnnl.gov/publications/uncertainty-quantification-neural-network-potential-foundation-models)). 기존 범용 퍼텐셜의 이종 앙상블로 만든 불확실성 지표는 실제 오차를 잘 따라갔고, 텅스텐에서는 DFT 데이터의 약 4%만으로 전체 학습 성능에 도달했다([arXiv 2507.21297](https://arxiv.org/html/2507.21297v1)). 실험실을 직접 조작하는 LLM 에이전트는 새로운 위험을 낳는다. LabSafety Bench에서 19개 LLM·VLM 중 **어느 모델도 위험 식별 70%를 넘지 못했고**, 화학 시나리오에서 가장 약했다([arXiv 2410.14182](https://arxiv.org/pdf/2410.14182)). SciHazard(2026)에서는 딥리서치 에이전트의 평균 위해 점수가 일반 LLM보다 32.3% 높았다([alphaXiv 2607.18665](https://www.alphaxiv.org/abs/2607.18665)). 도구 사용과 실험실 구동이라는 에이전트 층이 위험을 키운다는 뜻이다. 따라서 안전은 모델 정렬만으로는 부족하다. 경계가 정해진 실험실 인터페이스, 시약 화이트리스트, 사람의 승인 게이트처럼 하드웨어·API 계층에서 설계해야 한다([arXiv 2608.23104](https://arxiv.org/pdf/2608.23104)). 소재 SDL을 운용하는 LLM 에이전트에 특화된 안전 벤치마크는 아직 없다.

### 로봇용 소재: 내구성 데이터와 시뮬레이션 정확도가 모자라다

AI로 설계한 로봇 소재가 실험실을 벗어나려면 내구성 문제를 넘어야 한다. HKUST 리뷰(2026)에 따르면 기존 액추에이터는 5~10년 연속 운전을 견디지만, 소프트 공압 액추에이터는 피로, 박리, 마모로 훨씬 빨리 열화한다. 수명 연구는 "제한적이고 파편화"되어 있어 HKUST는 표준 내구성 시험 프로토콜을 제안했다([HKUST](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)). Chem. Soc. Rev.(2024)는 "내구성을 좇다 보면 부드러움을 잃을 수 있다"는 상충 관계를 짚었다([Chem. Soc. Rev.](https://pubs.rsc.org/en/content/articlehtml/2024/cs/d3cs01017a)). 표준화된 피로 데이터가 없으면 ML은 수명을 예측하도록 학습될 수 없다. 표준 시험 프로토콜이 내구성까지 고려한 소재 발견의 전제 조건인 이유다. 시뮬레이션도 문제다. 소프트 소재를 정확히 모델링하려면 초탄성, 소성, 이방성 구성 법칙이 필요하다([arXiv 2512.15994](https://arxiv.org/html/2512.15994v1)). 고충실도 FEA는 실시간보다 수백 배 느리고, 공동설계 기법은 계산에 치중해 실제 구현 가능성을 보장하지 못한다([arXiv 2505.03761](https://arxiv.org/abs/2505.03761)). 제조 결함 자체도 sim-to-real 오차의 원인이다. 제안된 해법은 시뮬레이터 위에 학습형 보정을 얹는 잔차 학습([arXiv 2603.22039](https://arxiv.org/pdf/2603.22039)), 실물 프로토타이핑을 루프에 넣는 공동설계, 표준 내구성 벤치마크다.

### 사람과 조직: 역량 집중과 공유 인프라

SDL을 구축하려면 로봇, AI, 소재 지식을 함께 갖춘 인력과 큰 자본이 필요하다. 그래서 역량은 소수 기관과 국가에 집중된다. 클라우드 랩은 구독형 원격 접근으로 민주화를 약속하지만, "흥미롭지만 우려도 낳는다"는 평가를 받는다([NSF PAR](https://par.nsf.gov/servlets/purl/10500964)). 각국 정부의 대응은 공유 시설 모델로 수렴하고 있다. 미국 MGI의 자율 소재혁신 인프라(AMII) 워크숍과 DOE의 2025년 1월 자율실험 RFI가 있고([Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01161.htm)), 한국은 분야별 자율실험센터와 석·박사 융합인재 양성을 추진한다([다음](https://v.daum.net/v/20260430155346042)). 영국 Royce CEO는 연합형 국가 자율실험실을 주장했다([Royce](https://www.royce.ac.uk/?p=18280)). 반면 소재 기반 모델과 SDL의 에너지·연산 발자국, 자율실험실에 대한 구체적 규제는 이번 조사에서 신뢰할 만한 자료를 찾지 못했다.

| 문제 | 핵심 증거 | 제안된 해법 |
|---|---|---|
| 선택 편향·음성 데이터 부족 | 실패 반응 미보고가 모델을 왜곡 | SDL의 전수 기록, 실패 결과 출판, FAIR(OPTIMADE·NOMAD) |
| 벤치마크 누수·OOD 과대평가 | MatFold, Omee, MLIP Arena | LOCO-CV, 전향적 과제 기반 평가, 물리 기반 시험 |
| 신규성 오판(무질서 상) | A-Lab, GNoME, MatterGen | 무질서 인식 매칭, 전문 결정학자 검토, 신뢰성·신규성·유용성 기준 |
| 분말·고체 핸들링, 특성분석 자동화 | NIST, 분말 XRD 자동화 난점 | 범용 시료 홀더, SiLA/ROS, 인라인·in situ 센싱 |
| 비용·통합 역량 | 구축된 SDL 수가 적음 | frugal twin, 클라우드 랩, 국가 공유 자율실험센터 |
| LLM 에이전트 안전 | LabSafety 70% 미만, SciHazard +32.3% | 경계 인터페이스, 승인 게이트, 자율 수준(L0~L5) 등급화(표준은 미정) |
| 소프트 소재 내구성·sim-to-real | 피로·박리, FEA 속도와 정확도 한계 | 표준 내구성 프로토콜, 잔차 학습, 프로토타이핑 인더루프 |

## 결론

이번 조사로 바뀐 그림은 이렇다. 지금까지 소재공학에서 로봇과 AI가 결합해 낸 가장 확실한 가치는 "새 물질의 발견"이 아니다. 정해진 공간 안에서 실험 횟수를 한 자릿수 배 줄이는 **표본 효율적 최적화**와, 실패를 포함한 **재현 가능한 데이터를 만드는 기계**라는 점이다. A-Lab 정정과 GNoME·MatterGen 비판 이후, 자율실험실의 역할은 발견 엔진에서 **검증 엔진**으로 옮겨가고 있다. 로봇이 생성한 합성·특성분석 데이터는 신규성 검증, 특허 실시가능성 입증, 투자자 신뢰 확보에 모두 쓰이는 공통 자산이 되었다. 앞으로의 경쟁력은 처리량보다 자동 특성분석의 정확도와 독립 검증 체계에서 갈릴 것이다. 2027년에 지켜볼 지표도 기업가치나 후보 수가 아니다. Periodic Labs, Lila, CuspAI 같은 스타트업 주장이 동료심사와 독립 합성을 통과하는지가 관건이다.

로봇 쪽에서 보면 두 흐름이 아직 만나지 않았다. AI 소재 플랫폼(GNoME, MatterGen, SDL)과 휴머노이드 산업의 실제 병목(희토류 자석, 배터리, 경량재, 내구성 있는 소프트 소재)은 개념상 바로 맞물리지만, 이를 공개적으로 잇는 OEM 프로그램은 확인되지 않았다. 학계의 로봇 소재 AI 성과도 대부분 배합·구조·형태 최적화에 머물러 있다. 그래서 다음 단계의 기회는 **"로봇이 로봇용 소재를 만드는" 폐루프**에 있다. 내구성 표준 데이터를 갖춘 소프트 액추에이터·e-skin 전용 SDL, 그리고 희토류 저감 자석을 대상으로 한 계산-로봇 파이프라인이 그 예다. 정책(데이터 1,000만 건, 24시간 자율실험센터, 자율실험실 협의체)과 로봇·배터리 수요 산업을 함께 가진 한국은 이 결합을 시도하기 좋은 위치에 있다. 다만 지금까지의 한국 성과 수치(KIST 24회, KAIST·POSCO 12배)는 언론 보도 수준이다. 동료심사된 지표로 뒷받침하는 것이 먼저다.

## 접근 차단 사이트 및 조사 한계

이번 조사는 클라우드 세션에서 이루어졌다. 이 세션의 네트워크 정책은 Default 환경의 "limited" 접근 수준이고, 허용 목록에는 주로 시험 준비 관련 사이트로 이루어진 짧은 목록만 들어 있다. 그 결과 학술지, 언론, 정부 사이트의 페이지를 직접 가져오는 시도는 모두 실패했다. 연구 노트에는 `getaddrinfo ENOTFOUND`(DNS 해석 불가)로 기록되었고, 별도 직접 점검에서는 프록시가 403으로 거부했다. 둘 다 허용 목록 밖 호스트를 막는 같은 정책에서 나온 현상이며, 유료 구독벽이나 404 오류가 아니다. 반면 **웹 검색은 정상 작동**했다. 따라서 이 보고서의 근거는 원문 전문이 아니라 **검색 결과 요약과 스니펫**이다. Nature, Science, RSC, ACS 논문의 수치, 특히 A-Lab 정정 수치, Genesis Mission 예산, 기업 투자액은 원문과 대조해 확인할 것을 권한다. 직접 점검에서는 arxiv.org, nature.com, pubs.rsc.org, chemistryworld.com, pubs.acs.org, science.org, scholar.google.com, mgi.gov, sciencedirect.com, pmc.ncbi.nlm.nih.gov, msit.go.kr, kist.re.kr, en.wikipedia.org, google.com이 모두 프록시에서 거부되었다. 차단을 풀려면 클라우드 환경 설정의 **Allowed domains**에 이 도메인들을 추가하거나 더 넓은 네트워크 접근 수준을 선택하면 된다([Claude Code 클라우드 환경 네트워크 접근 문서](https://code.claude.com/docs/en/cloud-environments#network-access)). 검색 색인이 미국 중심이어서 한국어·중국어·일본어 원어 자료(CNKI, J-STAGE 등)도 충분히 다루지 못했다.

| 호스트 | 필요했던 주제 | 실패 사유 |
|---|---|---|
| pubs.rsc.org | 한국 SDL 리뷰(Digital Discovery 2026), SDL 2.0(Materials Horizons 2026), Chem. Commun., Chem. Soc. Rev. 원문 | DNS ENOTFOUND(노트); 직접 점검 시 프록시 거부 |
| www.chemistryworld.com | A-Lab에 대한 Palgrave·Schoop 비판 상세 | DNS ENOTFOUND(노트 2건); 직접 점검 시 프록시 거부 |
| www.nature.com | Nature Reviews Materials 2022 리뷰, A-Lab 저자 정정문, Nature Materials e-skin 논문 원문 | DNS ENOTFOUND(노트); 직접 점검 시 프록시 거부 |
| arxiv.org | 자율 발견 커뮤니티 관점(2304.11120) 등 arXiv 원문 전반 | DNS ENOTFOUND(노트); 직접 점검 시 프록시 거부 |
| pmc.ncbi.nlm.nih.gov | A-Lab·Coscientist 원문, GNoME 비판(Cheetham & Seshadri) 전문 | 연속 차단으로 시도 중단(노트); 직접 점검 시 프록시 거부 |
| pubs.acs.org | USTC 다중 에이전트 로봇 화학자(JACS 2025) 지표, C&EN 관련 원문 | 시도 중단(노트); 직접 점검 시 프록시 거부 |
| mgi.gov | MGI 백서·전략 원문 | 시도 중단(노트); 직접 점검 시 프록시 거부 |
| science.org | RoboChem, 글로벌 유기 레이저 SDL 캠페인(Science 2024) 원문 | 직접 점검 시 프록시 거부 |
| sciencedirect.com | SDL 지속가능성 리뷰(Next Materials 2026) 등 Elsevier 원문 | 직접 점검 시 프록시 거부 |
| scholar.google.com | 서지·인용 교차 검증 | 직접 점검 시 프록시 거부 |
| msit.go.kr | 과기정통부 AI 소재 전략·자율실험실 보도자료 원문 | 시도 중단(노트); 직접 점검 시 프록시 거부 |
| kist.re.kr | KIST 스마트랩 "24회 실험" 원 자료 | 직접 점검 시 프록시 거부 |
| en.wikipedia.org | 배경 사실 확인 | 직접 점검 시 프록시 거부 |
| google.com | 일반 검색·검증 | 직접 점검 시 프록시 거부 |
| v.daum.net | KIST 스마트랩 기사(2025-12), 과기정통부 AI 소재 R&D 플랫폼 전략 기사(2026-04) | DNS ENOTFOUND(노트 2건) |
| phys.org | MARS 다중 에이전트 실험실(Matter 2026) 상세 | DNS ENOTFOUND |
| www.lila.ai | Lila Sciences 시설·성과 | DNS ENOTFOUND |
| www.nanowerk.com | 2026년 9월 LLM 에이전트 자율 소재 실험실 리뷰 | DNS ENOTFOUND |
| roboticsresear.ch | IDTechEx "휴머노이드 시장의 신소재 기회" 기사 | DNS ENOTFOUND |
| www.govinfo.gov | Genesis Mission 행정명령(EO 14363) 원문 | DNS ENOTFOUND |
| newsseoul.co.kr | 과기정통부 자율실험실 기사 | DNS ENOTFOUND |
| ifp.org | IFP "Scaling Materials Discovery with Self-Driving Labs"(SDL 비용 수치 포함 가능) | DNS ENOTFOUND(노트 2건) |
| www.technologyreview.com | AI 소재 스타트업 투자 개관(2025-12) | DNS ENOTFOUND |
| www.smarttoday.co.kr | 국내 자율실험실 스타트업 투자(2026-10) | DNS ENOTFOUND |
| finance.yahoo.com | Reuters 단독: Lila 1.15억 달러 추가 조달, 가치 13억 달러 이상 | DNS ENOTFOUND |
| helix.medill.northwestern.edu | A-Lab 2026년 정정(41→36) 상세 | DNS ENOTFOUND |
| siliconangle.com | CuspAI 4.5억 달러 시리즈 B 상세 | DNS ENOTFOUND |
| strathprints.strath.ac.uk | Pickles et al., Matter 2026 SDL 조화 논의 | DNS ENOTFOUND |
| energy.gov, nsf.gov, motir.go.kr, korea.kr, cordis.europa.eu, jst.go.jp, utoronto.ca | 미국·EU·일본·캐나다·한국 정책 원문 | 연속 차단 후 시도하지 않음(검색 요약만 사용) |
| PitchBook, CB Insights, Caplight, Sacra, biomed.reviewer.ly, IDTechEx 보고서 본문, Goldman Sachs·Morgan Stanley 보고서 | 투자·시장 수치, 휴머노이드 소재 수요 | 유료·로그인 필요로 시도하지 않음(스니펫 수치는 집계 사이트 데이터로 표기) |

## 후속 조사 제안

| 공백 | 왜 중요한가 | 제안 방법 |
|---|---|---|
| A-Lab 저자 정정문 원문(36/40 vs 36/57) | 가장 많이 인용되는 자율 발견 사례의 정확한 수치 | nature.com 허용 후 2026-01-19 Author Correction과 보충자료 확인 |
| 한국 SDL 성과의 동료심사 지표(KIST 24회, KAIST·POSCO 12배, KIMS 자율 합금 실험실) | 현재는 언론 보도 수준 | Digital Discovery 2026 "Self-driving laboratories in Korea" 원문, 각 기관 논문 확인 |
| 로봇용 신소재(LCE, e-skin, 하이드로겔, SMA/SMP)를 끝까지 합성하는 폐루프 SDL과 LCE 베이지안 최적화 정량 결과 | "로봇을 위한 소재" 방향의 핵심 빈칸 | Science Robotics, Adv. Mater., Nature Communications 표적 검색; 서울대·POSTECH·칭화·도쿄대·ETH·Harvard Wyss 그룹 추적 |
| 휴머노이드 OEM의 AI 소재 프로그램, MagNex 자기 성능, Optimus PEEK 주장 | 산업적 연결 고리 검증 | 기업 IR·특허(Tesla, Figure, Unitree, 현대차, 삼성·레인보우, UBTech, Xiaomi), Materials Nexus 기술 자료 |
| SDL 구축비·발견당 비용·독립 ROI | 투자·정책 판단의 근거 | IFP 보고서, NC State SDL Futures 보고서, DOE RFI 응답 검토 |
| 핵심 리뷰 원문(Tom et al. Chem. Rev. 2024; Abolhasani & Kumacheva Nat. Synth. 2023; L0~L5 자율 수준 문헌) | 분류 체계와 지표의 표준 확인 | 학술 도메인 허용 후 원문 정독 |
| 스타트업·빅테크 주장 검증(Periodic Labs 결과, Lila AISF 개소, DeepMind 영국 실험실 개소, 2026 라운드 확정 여부) | 밸류에이션과 실제 산출물의 괴리 판단 | 회사 공식 발표, arXiv·학술지, Reuters·Bloomberg 원문 |
| AI 소재·자율실험실 분야 특허 지형(G16C + autonomous laboratory), 지식재산처 통계, USPTO 지침 철회 1차 확인 | 실시가능성 요건과 경쟁 구도 | Google Patents·PATENTSCOPE 질의, USPTO 공지 원문 |
| 중국·일본 원어 자료(CNKI, J-STAGE), 일본 MI2I 이후 사업(DICE, ARIM), 중국 MOST 예산 | 영어권 편향 보정 | 원어 검색, 기관 보도자료 |
| 소재 SDL 전용 LLM 에이전트 안전 벤치마크, 자율실험실 규제, 에너지·연산 발자국 | 확산 단계의 거버넌스 | AI 안전 연구기관·OSHA 계열 지침, 정책 RFI 응답 |
| 제조 현장 ML 폐루프의 정량 성과(AM 불량률, 용접 생산성; HD현대 등) | 실험실 밖 확산 여부 | 기업 사례, 독립 감사 자료 |
| 소프트 액추에이터 피로 수명 분포(사이클 수) 데이터 | 내구성 고려 소재 설계의 전제 | HKUST 프로토콜 기반 문헌 수집 |
| K-문샷·과기정통부 AI 소재 전략 총예산, Genesis Mission 공식 수치, 2026-11-10 이후 중국 희토류 수출통제 유예 상태 | 정책·공급망 판단의 최신성 | msit.go.kr, energy.gov, 중국 상무부 원문 |
| 연합학습·데이터 신탁 등 IP 보존형 데이터 공유, 로봇 소재용 PINN | 데이터 병목의 제도적 해법 | 산업 컨소시엄(CuspAI Foundry, 자율실험실 협의체) 운영 규약 조사 |
