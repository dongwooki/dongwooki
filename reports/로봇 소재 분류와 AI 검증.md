# 검증대에 선 AI, 로봇 소재 지도를 다시 그리다

재료공학의 로봇 영역에 인공지능이 들어온 이유는 세 가지다. 신소재 하나를 상용화하기까지 **평균 약 20년**이 걸리는 시행착오식 개발이 한계에 부딪혔다. 계산과 AI가 만든 후보가 실험 능력을 압도했다. GNoME은 **220만 개 구조와 38.1만 개의 신규 안정상**을 내놓았지만, 그중 실험으로 확인된 것은 GNoME이 직접 만든 것이 아니라 **ICSD에 이미 독립적으로 보고된 구조와 일치한 736개**였다. 그리고 휴머노이드가 대당 **약 4 kg의 NdFeB 자석**과 무게의 **약 56%를 차지하는 액추에이터**를 요구하면서, 희토류·감속기·경량재·소프트 소재를 더 빨리 찾아야 할 산업적 이유가 생겼다. 이번 라운드에서는 이전 보고서의 스니펫 기반 주장을 원문과 대조했다. 그 결과 성과의 핵심은 "발견"이 아니라 **"표본 효율적 최적화"**로 정리된다. 42개 연구·63개 벤치마크를 메타분석한 결과 자율실험실(SDL)은 같은 성능에 도달하는 데 필요한 실험 수를 기준 전략(주로 무작위 샘플링) 대비 **중앙값 6분의 1**로 줄였다. 반면 A-Lab은 2026년 1월 정정에서 "새로운"의 뜻을 "과학계가 아니라 예측 플랫폼에 새로운"으로 바꿨다. 정정 후 수치는 보고된 성공 40건 중 36건, 표적 57개 중 36개로, 분모만 다를 뿐 둘 다 맞다. MatterGen이 합성한 TaCr₂O₆도 **1971년에 보고된 화합물**과 같다는 비판을 받았다. 로봇 소재를 12개 카테고리로 분류해 보면 AI는 저렴한 시뮬레이터가 있는 곳(메타물질, 4D 프린팅, 자성 소프트 복합체)과 센서 신호 해석에서 가장 성숙했다. 그러나 휴머노이드 원가의 약 절반을 차지하는 액추에이터 소재(자석, 감속기 강, PEEK)와 LCE·이온성·전기유압 액추에이터의 소재 설계에서는 거의 비어 있다. **ML로 설계한 소재를 양산 로봇에 썼다고 공개한 OEM은 2026년 11월 현재 없다.** 남은 과제는 무질서를 고려한 신규성 검증, 실험 수 기준의 투명한 가속 보고, 소프트 소재의 표준 내구성 데이터, 그리고 액추에이터 소재를 "합성부터 시험까지" 닫는 폐루프다. 이번 라운드에서는 환경을 무제한 네트워크로 바꾼 뒤 원문 대부분을 curl로 직접 읽었다. 남은 차단은 출판사 봇 방어와 유료벽 같은 사이트 측 문제다(맨 뒤 "접근 상태 및 조사 한계" 참조).

> 표기 규칙: **원문 확인**은 논문·정정 공고·정부·기관·회사 1차 문서를 직접 읽은 경우다. **언론·기업 주장**은 회사 발표나 언론 본문으로만 확인되고 독립 검증이 없는 경우다. **미확인**은 원문에 접근하지 못했거나 검색 요약(스니펫)으로만 본 경우다. 동료심사 여부는 따로 적었다.

## 20년 개발 주기와 '예측 과잉', 대당 4 kg의 자석이 AI를 불러들였다

### 시행착오 패러다임의 비용이 정책 문구가 되었다

출발점은 시간이다. 미국 재료게놈이니셔티브(MGI) 2011년 백서는 첨단소재를 "**at least twice as fast as possible today, at a fraction of the cost**"로 발견·개발·제조·배치하겠다고 썼다(원문 확인)([MGI white paper](https://www.mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf)). 2021년 MGI 전략계획은 3대 목표(소재혁신 인프라 통합, 소재 데이터 활용, 인력 양성) 가운데 첫째에 "modular, **autonomous**, integrated, high-throughput experimental tools"를 넣었다. 둘째 목표에서는 "AI-driven robotic systems"에 의한 자율 소재 연구를 서술했다(원문 확인)([MGI 2021 Strategic Plan](https://www.mgi.gov/sites/mgi/files/MGI-2021-Strategic-Plan.pdf)). IFP 보고서도 소재가 실험실에서 배치까지 "on average 20 years"가 걸린다고 정리한다([IFP](https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf)). 토론토대 Acceleration Consortium은 이 문제를 **"20년·1억 달러를 1년·100만 달러로"**라는 구호로 압축했다([U of T Engineering News](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/)). 한국 과학기술정보통신부도 2026년 전략에서 소재 연구가 연구자의 경험과 반복 실험에 의존해 **개발부터 상용화까지 10~20년 이상** 걸린다고 진단했다([디지털타임스(다음)](https://v.daum.net/v/20260430155346042)).

시간 문제 밑에는 탐색 공간의 크기가 있다. 30개 이하 중원자로 된 안정한 소분자만 **10^60개 이상**으로 추정된다([arXiv 1510.07512](https://arxiv.org/pdf/1510.07512)). 고처리량 DFT 데이터베이스는 ML의 연료가 되었다. AFLOW의 합금 열역학 항목은 2017년 **170만 건 이상**으로 늘었다([AFLOW Fleet](https://ar5iv.labs.arxiv.org/html/1712.00422)). 그러나 서로 다른 HT-DFT 데이터베이스 간 차이가 DFT와 실험 간 차이에 맞먹는 경우가 많다는 분석도 있다([arXiv 2007.01988](https://arxiv.org/abs/2007.01988v2)). 계산만으로는 정답을 얻을 수 없고, 실험 데이터를 대량으로 만들어야 한다는 결론이 여기서 나왔다.

### GNoME의 '736개'는 합성 실적이 아니라 독립 보고 구조와의 일치다

2023년 11월 Google DeepMind의 GNoME 원문은 Materials Project 기준 convex hull 아래에 있는 **220만 개 구조**를 보고했다. 그중 갱신된 hull 위의 신규 항목은 **381,000개**로, 이를 더한 안정 결정은 모두 421,000개다. 초록의 "736 have already been independently experimentally realized"는 본문에서 "ICSD에 모인 실험 구조 중 736개가 GNoME가 독립적으로 얻은 구조와 일치한다"는 뜻으로 설명된다(원문 확인)([Nature s41586-023-06735-9](https://www.nature.com/articles/s41586-023-06735-9)). 이전 보고서가 쓴 "독립 합성 736개"는 GNoME가 합성했다는 뜻으로 읽히면 틀린다. 예측 수십만 개 대 실험 확인 수백 개라는 격차 자체는 그대로다. 이 격차가 "AI가 제안하고, 로봇이 합성·분석하고, 그 결과로 모델이 다시 학습하는" 폐루프 자율실험실의 직접적 근거가 되었다. 로봇은 24시간 실험하고 실패한 실험까지 표준 형식으로 기록하며, 위험 물질에 사람이 노출되는 것을 줄인다([NCSU](https://cbe.ncsu.edu/?p=24420)). 아시아에서는 인구 구조도 명분이 된다. KAIST 서동화 교수는 POSCO홀딩스와 만든 양극재 자율실험실을 연구 인력 감소에 대한 대응으로 설명했다([KAIST 뉴스](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)).

### 로봇이 쓰는 소재는 비선형이고, 공급망은 좁다

"로봇 영역"에는 반대 방향도 있다. 로봇은 소재를 만드는 도구이자 소재를 소비하는 쪽이다. 소프트 로봇의 센서·액추에이터 소재는 **비선형성과 히스테리시스**가 강해 물리 모델만으로는 설계·제어가 어렵다. 이것이 ML 도입의 핵심 동기다([PMC7891779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)). 설계 공간도 거대하다. 자성 소프트 시트 로봇의 자화·형상 조합은 **약 1.2×10^752개**로 추산된다(원문 확인)([PMC11947188](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947188/)). LCE 수영 로봇 연구는 345,600개 파라미터 조합을 진화 알고리즘으로 탐색했다([arXiv 2503.00204](https://arxiv.org/pdf/2503.00204v3)).

산업 쪽 압력은 휴머노이드에서 나온다. IDTechEx는 "around 56 percent of the humanoid's weight is from the actuators alone"이라고 추정한다. 그 구조 부품은 "steel (predominantly) and aluminum alloys"에 의존한다(원문 확인)([Robotics & Automation News, IDTechEx 기고](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)). 이 56%는 **무게** 지표다. 이전 노트에서 "Morgan Stanley: 액추에이터 = BOM 56%"로 옮겨진 수치는 원문 근거를 찾지 못했다. 비용 쪽 공개 수치는 Morgan Stanley Robot Almanac의 **Optimus Gen 2 BOM 약 46,000달러 중 액추에이터 약 22,000달러(약 48%)**다([Yahoo Tech/SCMP 보도](https://tech.yahoo.com/science/articles/china-packs-patent-punch-race-093000841.html)). BofA는 2030년 중국산 휴머노이드 BOM을 **리니어 액추에이터 27%, 로터리 액추에이터 24%, 손 19%**로 제시했다([BofA Institute](https://institute.bankofamerica.com/content/dam/transformation/physical-ai-part-2.pdf)). 액추에이터는 BOM의 "약 절반", 손까지 넣으면 그 이상이다. Adamas Intelligence는 고급 휴머노이드 한 대에 **약 4 kg의 NdFeB**가 들어간다고 본다(원문 확인)([Adamas 2026-04-14](https://www.adamasintel.com/humanoid-robotics-sector-accelerates-on-multiple-commercialization-fronts-in-march/)). 중국은 2025년 4월 Sm·Gd·Tb·Dy·Lu·Sc·Y 7종을 라이선스제로 묶었다. 같은 해 10월 확대 조치는 유예되었는데, 상무부가 2026년 11월 9일 그 유예를 **2027년 1월 10일까지 두 달 연장**했다(언론 본문 확인)([The Star/Reuters](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/11/09/china-extends-suspension-of-rare-earth-export-controls-until-january); [Benchmark](https://source.benchmarkminerals.com/article/china-extends-pause-on-rare-earth-and-battery-export-controls-until-2027)). 희토류 저감 자석, 경량 구조재, 고에너지 배터리를 더 빨리 찾아야 한다는 요구가 AI 소재 탐색과 직접 연결된다.

### 각국 정책은 '데이터베이스'에서 '자율실험실 예산 항목'으로 옮겨갔다

미국이 의제를 세우고 각국이 1~5년 안에 따라가는 패턴이 두 번 반복되었다. 2011년 MGI 이후 일본·영국·중국이 데이터 인프라를 깔았다. 2025~2026년에는 미국 Genesis Mission에 이어 한국 K-문샷이 나왔는데, 이번에는 자율실험실이 중심이다. 이번 검증으로 가장 크게 바뀐 것은 미국 수치의 해석이다. 이전 보고서가 "충돌"로 기록한 **2.93억 달러와 3.2억 달러는 서로 다른 발표**였다. 3.2억 달러는 2025년 12월의 AI 인프라 투자(American Science Cloud 등)이고, 2.93억 달러(정확히 2억 9,376만 달러)는 2026년 3월 17일 공고된 RFA다([Covington](https://www.insidegovernmentcontracts.com/2026/03/doe-announces-a-new-funding-opportunity-under-the-genesis-mission/)). 행정명령 자체에는 금액이 없지만, 2026년 10월에는 **국립연구소 주도 로봇·자율과학 테스트베드 4곳에 3년간 3,000만 달러**라는 구체적 예산 항목이 생겼다([DOE Fact Sheet](https://www.energy.gov/articles/fact-sheet-energy-department-ushering-golden-age-american-science)). EU BIG-MAP 예산도 바로잡혔다. CORDIS 원문 기준 €1,600만이 아니라 **€19,997,812.50**이다([CORDIS 957189](https://cordis.europa.eu/project/id/957189)).

| 국가·지역 | 시기 | 프로그램 | 규모·목표 | 검증 상태 |
|---|---|---|---|---|
| 미국 | 2011 / 2021 | MGI 백서, 2021 전략계획 | "at least twice as fast"; 자율·고처리량 실험 도구를 Goal 1에 명시 | 원문 확인 ([백서](https://www.mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf); [2021 계획](https://www.mgi.gov/sites/mgi/files/MGI-2021-Strategic-Plan.pdf)) |
| 미국 | 2023 | NSF DMREF | 7,250만 달러·4년 과제 37건, 61개 대학 연구자 161명 | 원문 확인 ([NSF](https://www.nsf.gov/news/nsf-invests-72m-design-revolutionary-materials)) |
| 미국 | 2025-11-24 | Genesis Mission (EO 14363) | 우선 도메인에 critical materials 포함; 240일 내 "robotic laboratories and production facilities" 역량 검토; 금액 조항 없음 | 원문 확인 ([govinfo](https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21665.htm)) |
| 미국 | 2025-12 | DOE AI 인프라 투자 | 3.2억 달러(American Science Cloud, Transformational AI Models Consortium 등); 로봇 실험실 14건·AI 연구 37건 세부는 미확인 | 법률사무소 원문 확인, 세부 미확인 ([Covington](https://www.insidegovernmentcontracts.com/2026/03/doe-announces-a-new-funding-opportunity-under-the-genesis-mission/)) |
| 미국 | 2026-03-17 | DOE RFA DE-FOA-0003612 | 2.9376억 달러; Phase I 50만~75만 달러(9개월), Phase II 600만~1,500만 달러(3년); 21개 영역 | 원문 확인 ([energy.gov](https://www.energy.gov/articles/energy-department-announces-293-million-funding-support-genesis-mission-national-science)) |
| 미국 | 2026-07-22 | 백악관 ">$5B" 발표, 1차 278개 과제 | 15개 이상 기관 "commitments"; 과제 주도 기관은 국립연구소 87, 대학 168, 기업 19, 비영리 4; "Achieving AI-Driven Autonomous Laboratories", "Designing Materials with Predictable Functionality" 과제 | 원문 확인 ([White House](https://www.whitehouse.gov/releases/2026/07/45502/); [energy.gov](https://www.energy.gov/articles/secretary-energy-chris-wright-announces-first-genesis-mission-projects-selected-accelerate)) |
| 미국 | 2026-10-08 | 2차 발표 | 1년차 297개 과제; 로봇·자율과학 테스트베드 3,000만 달러; NSF·DOE 자율실험실·장비 1억 달러 이상; NSF 프로그래머블 클라우드 랩 4억 달러(7월); 산업계 24억 달러 약정; 총 60억 달러 이상 | 원문 확인 ([DOE](https://www.energy.gov/articles/fact-sheet-energy-department-ushering-golden-age-american-science); [White House](https://www.whitehouse.gov/fact-sheets/2026/10/fact-sheet-trump-administration-announces-the-most-ambitious-set-of-science-initiatives-this-century/)) |
| 캐나다 | 2023-04 | Acceleration Consortium | C$2억(CFREF); IFP 집계로 캐나다 SDL 공공·민간 투자 5억 달러 이상 | 기관 보도·IFP 원문 ([U of T](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/); [IFP](https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf)) |
| EU | 2020-09~2024-02 | BIG-MAP (Battery 2030+) | 총비용·EU 기여금 €19,997,812.50, DTU 조정, 참여자 38개 | 원문 확인 ([CORDIS](https://cordis.europa.eu/project/id/957189)) |
| EU | 2024-02-27 | COM(2024)98 첨단소재 전략 | Technology Council 설치; "€5억 파트너십(2025~2027)"은 EUR-Lex 접근 실패로 미확인 | 일부 원문 확인 ([EC R&I](https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/chemicals-and-advanced-materials/advanced-materials-industrial-leadership_en)) |
| 영국 | 2015~2026 | Henry Royce Institute; AI for Science Strategy | £2.35억(2015); AI for Science 최대 £1.37억 | 이전 라운드 출처, 이번 미재확인 ([UKRI](https://www.ukri.org/who-we-are/epsrc/centres-and-institutes/henry-royce-institute/); [GOV.UK](https://www.gov.uk/government/publications/ai-for-science-strategy/ai-for-science-strategy)) |
| 중국 | 2026-07 | 베이징 AI 과학연구 실행방안(2026~2028) | 5대 차원의 첫째가 자율실험실 시스템, 18개 과제, 6대 분야에 소재과학 포함, dry–wet 폐루프, 자율실험실 표준·등급 평가 | 원문 확인 ([Beijing gov](https://english.beijing.gov.cn/investinginbeijing/InvestmentSpecial/DigitalEconomy/PolicesAndInterpretations/202607/t20260715_4763931.html)) |
| 일본 | 2025-12 / ~2050 | NIMS DICE(MEXT 마테리얼 DX 플랫폼, ARIM·DxMT와 연계), pinax 무상 공개; 문샷 목표 3 | 2050년 자연과학에서 스스로 생각하고 행동하는 AI 로봇; JST 페이지는 범용 자율 휴머노이드 중심으로 재편, e-skin·전신 촉각 과제 포함 | 원문 확인 ([DICE](https://dice.nims.go.jp/en/about.html); [NIMS](https://www.nims.go.jp/press/2025/12/a5kbo700000092mp-att/202512230.pdf); [내각부](https://www8.cao.go.jp/cstp/english/moonshot/sub3_en.html); [JST](https://www.jst.go.jp/moonshot/en/program/goal3/)) |
| 한국 | 2026-04-30 | AI 소재 R&D 플랫폼 구축 전략(2026~2030) | 4대 자율실험센터(이차전지, 수소·에너지, 우주항공·모빌리티 금속·복합재·세라믹, 유기반도체·디스플레이); AI-Ready 데이터 5년 1,000만·10년 5,000만 건; 석사 300·박사 75명 이상; **예산은 원문에 없음** | 언론 본문 확인 ([동아사이언스](https://v.daum.net/v/20260430101533808); [디지털타임스](https://v.daum.net/v/20260430155346042)) |
| 한국 | 2026-02-25 / 09-30 / 10-01 | K-문샷 | 12대 미션에 소재(희토류 대체·저감 영구자석) 포함; 희토류 산학연 협의체 출범, 중희토류 완전 배제·경희토류 극저감 공정, 1단계 2027~2029; 총예산 미확인 | 언론·KDI 재게시 확인 ([뉴시스](https://www.newsis.com/view/NISX20260225_0003525436); [머니투데이](https://www.mt.co.kr/tech/2026/09/30/2026093015522912240); [KDI](https://eiec.kdi.re.kr/policy/materialView.do?num=287736)) |
| 한국 | 2026-08-11 | 자율실험실 산·학·연 협의체 | 수요기업 50개사와 대학·연구기관 30여 곳, 합계 "80여 개 기관"; 위원장 정유성(서울대) | 언론 본문 확인 ([아시아경제](https://view.asiae.co.kr/article/2026081109490769317); [Asia Business Daily](https://view.asiae.co.kr/en/article/2026081015043638880)) |

정책 목표치는 2배(MGI, Genesis의 "double scientific productivity"), 5배 이상(BIG-MAP), 10~20배(Acceleration Consortium) 사이에 흩어져 있다. 측정된 근거는 다음 절의 "실험 수 기준 중앙값 6배"다. 이 수치는 최적화 캠페인 단위의 효율이지, 실험실에서 시장까지의 전체 기간이 아니다.

## 자율실험실은 실험 수를 중앙값 6분의 1로 줄였지만, '신소재 발견' 주장은 크게 줄어들었다

### 단일 목적 루프에서 다중 에이전트까지, 헤드라인 수치는 대부분 원문과 일치한다

2016년 미 공군연구소의 ARES는 in situ 라만을 목적함수로 **600회 이상 자율 실험**을 돌려 탄소나노튜브 성장을 학습했다([AF.mil](https://www.af.mil/News/Article-Display/Article/982368/afrl-system-revolutionizes-research-process/)). 2020년 리버풀대의 이동형 로봇 화학자는 "batched Bayesian search"로 **8일간 10개 변수 공간에서 688회 실험**을 수행해 초기 배합보다 **6배 활성이 높은 광촉매**를 찾았다(원문 확인)([Nature s41586-020-2442-2](https://www.nature.com/articles/s41586-020-2442-2)). 2022년 CMU의 Clio+Dragonfly는 **2 근무일·42회 실험으로 고속충전 전해질 6종**을 찾았다. 같은 장치로 한 무작위 탐색보다 6배 빨랐고, 220 mAh 흑연∥NMC532 파우치셀에서 최고 셀끼리 비교하면 **13%**, 최악 셀끼리 비교하면 5% 개선되었다(원문 확인)([Nature Communications](https://www.nature.com/articles/s41467-022-32938-1)). 2023년 USTC 로봇 AI 화학자는 화성 운석 원소로 **300만 개 이상 조성**을 탐색해 10 mA cm⁻²에서 **55만 초 이상** 안정한 OER 촉매(과전압 445.1 mV)를 만들었다. 서지는 Nature Synthesis 3권(2024)이고, 2023년 11월 13일은 온라인 게재일이다(원문 확인)([Nature Synthesis](https://www.nature.com/articles/s44160-023-00424-1)). 2024년 Science의 RoboChem은 인라인 벤치탑 NMR과 폐루프 BO로 기존 공정보다 수율과 공간-시간 수율을 높였다(초록 확인)([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1126/science.adj1817&format=json&resultType=core)). 널리 인용되는 "약 80% 사례에서 문헌보다 높은 수율"은 논문 수치가 아니다. **무작위로 고른 문헌 4편을 재현한 결과**에 대한 연구책임자의 보도자료 발언이고, 나머지 20%는 "비슷했다"([UvA HIMS](https://hims.uva.nl/content/news/2024/01/autonomous-synthesis-robot-uses-ai-to-speed-up-chemical-discovery.html)). 같은 해 리버풀 후속 연구(Nature 635)는 KUKA 이동 로봇이 UPLC-MS와 벤치탑 NMR을 사람과 공유하면서 휴리스틱 판단기로 재현성을 확인했다. 다만 정량 헤드라인은 없다([Nature s41586-024-08173-7](https://www.nature.com/articles/s41586-024-08173-7)). 2025년 아르곤연구소 Polybot은 importance-guided BO로 7차원 공정 공간을 탐색해 **평균 4,500 S/cm 이상**의 투명 전도막을 만들었다(원문 확인)([Nature Communications](https://www.nature.com/articles/s41467-024-55655-3)).

### AI는 다섯 층에 들어가지만, 성과의 엔진은 베이지안 최적화이고 Level 5는 아직 없다

SDL에서 AI는 다섯 층에 들어간다. 표적·가설 생성(GNoME, Materials Project), 레시피·실험 계획(문헌 학습 NLP·LLM, BO·능동학습), 로봇 실행과 오케스트레이션, 특성분석 자동 해석(XRD 상 판별, NMR 해석, 현미경 제어), 추론·지식 축적(다중 에이전트, 자연어 사전지식)이다. 동료심사된 정량 성과(6배 활성, 6배 가속, 4,500 S/cm)는 거의 모두 **가우시안 과정 기반 BO** 같은 표본 효율적 블랙박스 최적화에서 나왔다. LLM은 계획·코드·도구 연결을 맡는 "접착제"다. ChemCrow는 예측한 절차가 용매 부족이나 잘못된 정제 동작 때문에 그대로 실행되지 않는 한계를 스스로 보고했다([Nature MI](https://www.nature.com/articles/s42256-024-00832-8.pdf)). 한국화학연구원(KRICT)의 대화형 AI는 LLM이 자연어 가설을 **BO의 사전평균 함수와 제약**으로 바꾸고, 데이터가 가설과 모순되면 사전을 끄는 AWCD를 붙였다. 이 연구는 J. Chem. Inf. Model.(2026)에 동료심사 논문으로 실렸다. 다만 검증은 Ugi 반응과 P3HT-CNT 복합체 **데이터셋**에서 이루어졌고, 물리 SDL에서 한 것은 아니다(원문 확인)([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1021/acs.jcim.6c00976&format=json&resultType=core)).

자율성 수준은 아직 표준이 없다. Tom 등의 Chem. Rev.(2024) 리뷰는 하드웨어·소프트웨어 자율성 등급을 조합해 레벨을 정의한다. 이 리뷰는 "Level 2 and 3 SDLs make up the vast majority"이고, 단순한 과제에서는 Level 4가 시연되었지만 "a true Level 5 SDL remains an unattained goal"이라고 본다(원문 확인)([PMC11363023](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11363023&rettype=xml)). MITRE의 Tobias와 Wahab(R. Soc. Open Sci. 2025)는 1차원 Level 1~5 체계와 하드웨어(L0~3)×소프트웨어(L0~3)의 2차원 체계를 함께 제시한다. 이들도 Level 4(Adam과 Eve)가 문헌상 최고이며 Level 5는 미실현이라고 본다(원문 확인)([PMC12368842](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12368842&rettype=xml)). Volk과 Abolhasani는 자율도를 piecewise, semi-closed loop, closed-loop, self-motivated의 4단계 서술형으로 나눈다(원문 확인)([Nature Communications](https://www.nature.com/articles/s41467-024-45569-5)). 세 체계의 숫자는 서로 맞지 않는다. 그러나 "대부분 Level 2~3, Level 5 없음"이라는 결론은 같다.

### '6배'는 실험 수 기준이며, 무작위 탐색 대비다

보스턴대 Adesiji 등은 "self-driving lab"으로 검색한 111개 연구 중 직접 벤치마크를 보고한 것이 40%뿐임을 확인했다. 이들이 **42개 연구·63개 벤치마크**를 분석한 결과, 가속 계수(AF)는 **1.3~100 범위에 중앙값 6**이었다(원문 확인)([arXiv 2508.06642](https://arxiv.org/pdf/2508.06642); 저널판 [Digital Discovery 5(1) 14–27](https://api.crossref.org/works/10.1039/D5DD00337G)). 여기서 AF는 같은 성능에 도달하는 데 필요한 **실험 수의 비**(n_ref/n_AL)이고, 기준 전략은 주로 무작위 샘플링이다. AF는 차원이 높을수록 커졌다. 향상 계수(EF)는 두 자릿수 이상 차이 났지만 **차원당 10~20회 실험**에서 정점을 찍었다. 따라서 "SDL이 인간보다 6배 빠르다"는 표현은 틀리다. 벽시계 시간이나 인간 전문가 대비 수치가 아니기 때문이다. Clio의 "무작위 대비 6배"나 Burger의 "6배 활성"과는 숫자만 같을 뿐 개념이 다르다. Volk과 Abolhasani가 자율도, 운영 수명, 처리량, 실험 정밀도, 소재 사용량, 접근 가능한 파라미터 공간, 최적화 효율의 **7개 지표**를 함께 보고하자고 제안한 이유도 여기 있다. 최적화 속도 하나로는 연구 간 비교가 안 된다는 것이다(원문 확인)([Nature Communications](https://www.nature.com/articles/s41467-024-45569-5)). 언론이 쓴 "인간이면 2,000년"([Phys.org](https://phys.org/news/2023-11-ai-chemist-catalyst-oxygen-production.pdf)) 같은 표현은 측정값이 아니라 외삽이다.

| 시스템 | 시기 | 정량 결과(검증 후) | 검증 상태 |
|---|---|---|---|
| AFRL ARES (CNT) | 2016~17 | 자율 실험 600회 이상 | 기관 보도 ([AF.mil](https://www.af.mil/News/Article-Display/Article/982368/afrl-system-revolutionizes-research-process/)) |
| 리버풀 이동형 로봇 화학자 | 2020 | 8일, 688회, 10변수, 광촉매 활성 6배 | 동료심사, 원문 확인 ([Nature](https://www.nature.com/articles/s41586-020-2442-2)) |
| CMU Clio + Dragonfly | 2022 | 2 근무일·42회, 전해질 6종, 무작위 대비 6배, 셀 +13%(최고)/+5%(최악) | 동료심사, 원문 확인 ([Nat. Commun.](https://www.nature.com/articles/s41467-022-32938-1)) |
| LBNL A-Lab | 2023, 2026-01 정정 | 원래 41/58(71%), 인간 개입 포함 43(78%) → 정정 후 36/57(63%), 보고 성공 40건 중 36건 정확, 4건 불확정 | 동료심사 + 정정, 원문 확인 ([Nature](https://www.nature.com/articles/s41586-023-06734-w); [정정](https://www.nature.com/articles/s41586-025-09992-y)) |
| USTC 로봇 AI 화학자 | 2023/2024 | 300만 개 이상 조성, 445.1 mV, 55만 초 이상 | 동료심사, 원문 확인 ([Nat. Synth.](https://www.nature.com/articles/s44160-023-00424-1)); "−37 °C"·"2,000년"은 미확인·외삽 |
| UvA RoboChem | 2024 | 수율·공간-시간 수율 향상(초록); 80%·주 10~20분자는 보도자료 발언 | 초록 원문 확인 + 언론 ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1126/science.adj1817&format=json&resultType=core); [UvA](https://hims.uva.nl/content/news/2024/01/autonomous-synthesis-robot-uses-ai-to-speed-up-chemical-discovery.html)) |
| 리버풀 이동 로봇 탐색 합성 | 2024 | 장비 공유, 휴리스틱 판단기, 정량 헤드라인 없음; "1.75 m 로봇"은 미확인 | 동료심사, 원문 확인 ([Nature](https://www.nature.com/articles/s41586-024-08173-7)) |
| ANL Polybot | 2025-02 | 7차원, 평균 4,500 S/cm 이상 | 동료심사, 원문 확인 ([Nat. Commun.](https://www.nature.com/articles/s41467-024-55655-3)) |
| MARS (선전) | 2026 | LLM 에이전트 19개·도구 16개, 10회 반복 내 페로브스카이트 나노결정 최적화 | 미확인(스니펫) ([Phys.org](https://phys.org/news/2026-01-multi-agent-ai-robots-automate.html)) |
| KRICT 대화형 AI | 2026-07 | LLM→BO 사전, 비가이드 BO 대비 가속(데이터셋 검증) | 동료심사, 초록 확인 ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1021/acs.jcim.6c00976&format=json&resultType=core)) |
| KIST 스마트랩 | 2025-12 | 작년 "1만 회 → 200회", 최근 촉매 24회·일주일 남짓(별개 성과); 기자는 MITRE 기준 레벨 3으로 분류 | 언론 주장 ([서울경제(다음)](https://v.daum.net/v/20251217175541326)) |
| KAIST–POSCO 양극재 자율실험실 | 2025-08 | 탐색 기간 93% 단축; "12배 이상"은 **24시간 운용·500회 가정** 시 84일→6일 추정 | 기관 보도자료 원문 확인, 실측 아님 ([KAIST](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)) |
| KIMS 오토노머스 랩 | 2025-06 | 아크 멜터·튜브 퍼니스·XRD·인장시험 로봇화, "수개월~수년을 몇 주로" | 언론 주장 ([헤럴드경제(다음)](https://v.daum.net/v/20250629140135289)) |
| SynAgent | 2026-09 | 18회 실험으로 LiCoO₂ 박막 최적 기판온도 구간 | 프리프린트 ([arXiv](https://arxiv.org/abs/2609.18598)) |
| Lila Sciences | 2026 | 3개월 2,942개 촉매, Pd계 6개 계열, 1,000시간 이상 산성 시험에서 Ru와 동등, 표준 실험실 대비 17배, 시료당 인력 90% 이상 감소 | 기업 주장(회사 원문 확인) ([Lila](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem)) |
| Radical AI | 2026 | 6개월 합금 1,200종, "DARPA 최고 프로그램의 약 10배 속도" | 기업 주장 ([Radical AI](https://www.radical-ai.com/news)) |

한국 사례 가운데 동료심사에 도달한 것은 KRICT 논문과, 서울대·KAIST·KIST·KRICT·삼성종합기술원 등 저자 21명이 쓴 리뷰 "Self-driving laboratories in Korea"(Digital Discovery 5(5), 2026)뿐이다(서지 원문 확인)([Crossref](https://api.crossref.org/works/10.1039/D6DD00024J)). 리뷰 본문은 RSC의 봇 방어 때문에 읽지 못했다. 한국경제의 "데이터 확보 12배 늘었다"는 제목은 조건부 추정치를 실적처럼 표현한 것이다([한국경제](https://www.hankyung.com/article/2025080386861)).

### A-Lab·GNoME·MatterGen은 같은 이유로 신규성을 잃었다

**A-Lab**의 원래 논문 제목은 "…accelerated synthesis of **novel** materials"였고, 초록은 17일간 58개 표적 중 41개의 신규 화합물(71%)을 합성했다고 주장했다(원문 확인)([OSTI 저자 원고](https://www.osti.gov/pages/servlets/purl/2281696)). 2024년 3월 Leeman, Schoop, Palgrave 등은 PRX Energy에서 부분 성공을 포함한 43개 산물을 모두 검토했다. 이들은 "at time of publication, **none of the materials produced by A-lab were new**"라고 결론지었다. 오류 분포는 "주장된 성공" 36건 중 명백히 부정확한 적합이 18건, 보고 CIF와 다른 CIF 사용이 8건, 알려진 무질서 버전이 있는데 양이온 질서 증거가 없는 경우가 24건, ICSD에 이미 있는 화합물이 3건이었다(원문 확인)([NSF PAR](https://par.nsf.gov/servlets/purl/10532478)). Nature는 2026년 1월 19일 **저자 정정**(Nature 650, E1)을 냈다. 철회가 아니라 정정이다. 정정문은 신규성 주장이 "new to the prediction platform, not necessarily new to science"라는 뜻이었다고 인정했다. 회절 패턴을 수작업으로 재분석해 "36 of its 40 reported successes"에서 결론이 맞았고 4건은 불확정이라고 밝혔으며, 학습 데이터에 잘못 들어 있던 Zn₂Cr₃FeO₈을 제외했다(원문 확인)([Nature 정정](https://www.nature.com/articles/s41586-025-09992-y)). 정정 후 본문 초록은 "36 compounds from a set of 57 targets"(63%)로 바뀌었고, 제목의 "novel"은 "inorganic"으로 교체되었다(원문 확인)([Nature](https://www.nature.com/articles/s41586-023-06734-w)). 정정은 무질서 버전 문제(24/36)를 직접 반박하지 않는다. "과학계에 새롭지 않다"고 인정해 쟁점을 우회했다. C&EN 기사에 실린 Palgrave의 "덜 흥미로워졌지만 그렇게 결함이 많지는 않다"는 평가는 로그인 장벽 때문에 이번에도 원문 확인이 안 되었다([C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01)).

**GNoME**에 대해 Cheetham과 Seshadri(Chem. Mater. 2024)는 신규성·신뢰성·유용성을 모두 갖춘 화합물의 증거가 "scant"하다고 썼다. 384,870개 항목의 공간군 분포는 ICSD와 "strikingly different"했다. ICSD에서 각각 약 8%인 Pnma와 P2₁/c 대신 Pm(12.7%)과 P1(10.2%)이 상위를 차지했고, Pnma는 16위(1.56%)였다. Pm·Ac·Pa 같은 방사성 원소 화합물도 18,000개 이상 포함되어 있었다(원문 확인)([PMC11044265](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11044265&rettype=xml)). **MatterGen**은 체적탄성률 목표 200 GPa로 생성한 후보에서 출발했다. 목표값마다 후보 8,192개를 만들어 75개로 거르고, 전문가 검토를 거친 4개를 합성했으며 그중 1개가 성공했다. 측정값은 최대 169 GPa(4회 평균 158±11 GPa)로 "목표의 20% 이내"였다. 저자들도 합성물이 예측된 정렬 구조의 "compositionally disordered version"임을 밝혔다(원문 확인)([Nature s41586-025-08628-5](https://www.nature.com/articles/s41586-025-08628-5)). 평균값 158 GPa를 쓰면 오차는 약 21%다. Juelsholt(Mater. Horiz. 2026)는 무질서 형태로 합성된 Ta₁/₃Cr₂/₃O₂가 "**first described in 1971** and included in MatterGen's training dataset"인 Ta₁/₂Cr₁/₂O₂와 동일하다고 지적했다(초록 원문 확인)([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1039/D6MH00268D&format=json&resultType=core)). 이전 보고서의 "1972년"은 1971년으로 고친다. MatterGen이 무질서 인식 매처를 도입했는데도 ICSD에 있는 무질서상과 같은 물질을 "new"로 분류했다는 점이 비판의 핵심이다.

세 사례의 공통 구조는 분명하다. DFT·생성 파이프라인은 실제로는 자리 무질서 고용체인 물질을 정렬된 단위세포로 출력한다. 자동 신규성 검사는 이를 걸러내지 못한다. 자동 XRD 정련은 표적이 합성되었다고 잘못 "확인"한다. 그래서 자동 특성분석은 처리량의 병목이면서 결과의 정확도를 좌우하는 병목이기도 하다. 2026년 9월에는 AI가 제안한 초전도체를 사전 등록된 "물리 판정"으로 검증하자는 프리프린트가 "생성은 발견이 아니다"라는 표어를 내걸었다([arXiv 2609.10614](https://arxiv.org/html/2609.10614)).

### 자본은 검증된 산출물보다 앞서 달린다

산업 구조는 세 층이다. 첫째 층은 빅테크가 공개하는 기반 모델과 데이터(GNoME, MatterGen·MatterSim, Meta OMol25·UMA)다([Meta AI](https://ai.meta.com/blog/meta-fair-science-new-open-source-releases/)). 둘째 층은 연산·도구(NVIDIA ALCHEMI 등)다([ENEOS](https://www.hd.eneos.co.jp/english/news/release_information/year/2025/20251205_02_01_mr03/)). 셋째 층은 물리적 폐루프 실험실이다. 첫째 층이 무료로 풀리면서 대형 투자는 실험실을 가진 기업에 몰렸다. 검증 결과 투자 수치 대부분은 맞았지만, 리드 투자자와 2026년 라운드에는 수정이 필요하다.

| 기업 | 자금 조달(검증 후) | 비고 | 검증 상태 |
|---|---|---|---|
| Periodic Labs (미국) | 2025-10 시드 3억 달러, a16z 리드(Felicis 참여), 투자 전 기업가치 10억 달러 | 2026년 70억~75억 달러 보도는 회사 미확인; 연구 성과 공식 발표 없음 | 언론 본문 확인 ([SiliconANGLE](https://siliconangle.com/2025/10/01/periodic-labs-raises-300m-accelerate-scientific-research-ai/); [periodic.com](https://periodic.com/)) |
| Lila Sciences (미국) | 시리즈 A 3.5억 달러(누적 5.5억 달러), 기업가치 13억 달러 이상 | 2026-06 약 20억 달러 조달·투자 전 85억 달러 **협상 보도**(회사 논평 거부); Genesis Lighthouse Phase I 3건 선정 | 회사 원문 + 언론 ([Lila](https://www.lila.ai/news); [Bloomberg Law](https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation); [Lila Genesis](https://www.lila.ai/news/powering-american-science-lila-to-join-does-genesis-mission)) |
| CuspAI (영국) | 2026-07-20 시리즈 B 4.5억 달러, 기업가치 26억 달러, **Kleiner Perkins·NEA 리드**, Bezos Expeditions 상당 참여 | AI Materials Foundry 회원 45곳 이상(Nvidia·Samsung·Meta 등) | 언론 본문 확인 ([SiliconANGLE](https://siliconangle.com/2026/07/20/ai-materials-science-startup-cuspai-raises-450m-funding/)) |
| Radical AI (미국) | 시드 5,500만 달러(RTX Ventures 리드); 2026년 신규 라운드 없음 | 2026-02 브루클린 네이비야드에 뉴욕주 첫 완전 자율 소재 실험실 개소, 하루 약 100회 실험 설계 | 언론 본문 확인 ([BK Reader](https://www.bkreader.com/business-innovation/radical-ai-opens-nys-first-autonomous-materials-lab-11801540)) |
| DP Technology (중국) | 시리즈 C 8억 위안 이상(약 1.1억 달러) | 국가 연계 펀드 참여 | 이전 라운드 언론 ([SCMP](https://www.scmp.com/business/companies/article/3337648/ai-science-start-dp-technology-raises-us114-million-series-c-round)) |
| Path Robotics (미국) | 2026-11 시리즈 E 3억 달러, 투자 후 24.5억 달러, Georgian 리드, Naver Ventures 신규, 누적 6.1억 달러 이상 | 2026-08 HII와 6억 달러 성과 연동 생산 계약; Automate.org의 22.5억 달러는 오류로 보임 | 언론 본문 확인 ([Robotics 24/7](https://www.robotics247.com/article/path-robotics-announces-300m-series-e-financing-at-2.45b-valuation); [TNW](https://thenextweb.com/news/path-robotics-300m-series-e-2-45bn-valuation)) |
| Google DeepMind 영국 자동화 소재 랩 | 2025-12 발표, 2026년 개소 예정 | 2026-11 현재 개소 확인 자료 없음 | 미확인 ([TechRadar](https://www.techradar.com/pro/google-deepmind-partners-with-the-uk-government-for-science-breakthroughs-cleaner-energy)) |

기업 성과 수치는 대부분 자체 발표다. LG AI연구원은 EXAONE Discovery로 **후보 42만 개를 하루 만에 걸러** LG생활건강의 탈모 후보 성분을 찾았다고 밝혔다. 기존 방식으로는 22개월이 걸린다는 것이 LG의 설명이다. LG는 소재 기반 모델이 합성 결과를 예측하고 로봇이 실험하는 자율실험실 계획도 내놓았다(언론 본문 확인)([Korea Times](https://www.koreatimes.co.kr/business/companies/20260914/lg-ai-research-seeks-to-address-industrial-challenges-with-expert-ai-models)). Microsoft와 PNNL은 **3,200만 후보 → 약 50만 → 800 → 150 → 23개**로 깔때기를 좁혔다. 23개 중 5개는 기지 물질이어서 신규는 18개이고, 이전 보고서의 "18 vs 23" 충돌은 이것으로 풀린다. 리튬은 최대 약 70% 줄일 수 있다고 했지만, 회사 스스로 "the exact chemistry is subject to optimization"이라는 단서를 달았다(회사 원문 확인)([Microsoft Source](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)). 이런 사례는 "후보 도출 시간(시간~일)"을 "시장 출시 시간"처럼 보이게 한다. 인증·스케일업·신뢰성 평가는 여전히 수년이 걸린다. 시장 규모 추정은 범위 정의에 따라 한 자릿수 이상 차이 난다. IDTechEx는 외부 제공 소재 인포매틱스 시장을 **2034년 7.25억 달러(2025년 대비 CAGR 9.0%)**로 본다(원문 확인)([IDTechEx](https://www.idtechex.com/en/research-report/materials-informatics-2025/1096)). CuspAI 한 회사의 기업가치가 이 시장 전체의 세 배를 넘는다. 투자자는 소프트웨어 매출이 아니라 소재 IP와 제품의 가치를 사고 있지만, AI가 발견한 소재가 대규모로 상용화된 사례는 아직 공개되지 않았다. 제도도 같은 방향을 가리킨다. 미국 특허청(USPTO)은 2025년 11월 28일 AI 보조 발명 가이던스를 "rescinded in its entirety"로 폐지하고 개정 가이던스로 대체했다. 새 가이던스는 AI를 "instruments used by human inventors"로 본다(원문 확인)([govinfo FR 2025-21457](https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21457.htm)). 한국 지식재산처는 검증하지 않은 AI 생성 데이터로 출원하면 실시가능성 결여로 거절될 수 있다고 경고했다([Law Times](https://www.lawtimes.co.kr/news/articleView.html?idxno=227594)). 로봇 실험실은 발견 엔진이면서 특허용 실시가능성 데이터를 만드는 장치이기도 하다.

제조 현장의 자율은 실험실보다 한 단계 늦다. 로봇 적층제조의 강화학습 연구는 대부분 시뮬레이션에 머물러 있다([Whiterose review](https://eprints.whiterose.ac.uk/id/eprint/240849/1/1-s2.0-S1526612526004342-main.pdf)). 상업적으로 가장 앞선 것은 Path Robotics의 AI 비전 자율 용접이지만, 고객 생산성 지표를 독립적으로 검증한 자료는 없다.

## 로봇 소재 분류 체계

로봇 소재를 12개 카테고리로 나누면, AI가 들어간 정도는 시장에서의 중요도와 거꾸로 움직인다. 휴머노이드의 무게와 원가를 지배하는 강체 액추에이터 계열(자석, 감속기 강, 베어링, 구조용 플라스틱)은 성숙한 상용 소재다. 그런데 이 계열에서는 AI가 소재 조성이 아니라 부품 형상(위상최적화)이나 공정 감시 수준에만 들어가 있다. 반대로 시장 규모가 작은 소프트·마이크로 소재에서는 시뮬레이터나 디코딩 문제가 잘 정의되어 있어 ML 역설계가 활발하다. 한 가지 단서가 있다. 아래 표의 강체 계열 수치 일부는 첫 라운드에서 검색 요약으로 모은 것이고, 이번 라운드에서 원문으로 재확인한 항목과 그렇지 않은 항목을 검증 상태 열에서 구분했다.

### 카테고리 개관

| # | 카테고리 | 대표 소재 | 주요 적용 부품 | 기술 성숙도 | 핵심 공급망·상용화 이슈 | AI 적용 성숙도 |
|---|---|---|---|---|---|---|
| 1 | 구조재 | Al 합금(기계가공·다이캐스트), Mg, Ti(LPBF), 고강도강, CFRP, PEEK·CF-PEEK, PA-GF, PC-ABS | 링크, 하우징, 외장, 섀시, 일부 감속기 | 상용 | 맞춤형 비중 80~90%, CNC→금형 공정 전환, PEEK 과열 | 중간: ML 합금 설계(Mg)는 실험 검증, 위상최적화는 상용 CAD, 로봇 양산 적용은 없음 |
| 2 | 구동·모터/자석 | 소결 NdFeB(Dy/Tb 결정립계확산), FeN, MagNex, 전기강판, Cu 권선 | 프레임리스·코어리스 관절 모터 | NdFeB 상용, FeN 파일럿 | 중국 7종 중희토류 라이선스 유지, 확대분 유예 2027-01-10 | 낮음~중간: AI 조성 탐색은 기업 주장 단계 |
| 3 | 동력전달·관절 | 플렉스플라인 합금강, 베어링강, Si₃N₄ 볼, 그리스, 힘줄 섬유 | 하모닉·RV·유성 감속기, 롤러스크루, 베어링 | 상용 | 일본 과점(Nabtesco, HDS), 롤러스크루 중국 수입의존 | 낮음: 피로강·윤활 ML은 학술 단계, 로봇 미적용 |
| 4 | 에너지 | Li-ion 팩, 황화물계 전고체, 구조형 팩 소재 | 몸통 배터리 | Li-ion 상용, 전고체 소량 | 리튬, 사람 곁 안전 인증 | 중간: AI 스크리닝(MS–PNNL), 자율실험실(KAIST–POSCO) |
| 5 | 전자·센싱·열관리 | GaN 인버터, 17-4PH·경질 Al 플렉셔, 자기식 엔코더, 열전도 테이프 | 관절 드라이버, 힘/토크 센서, 엔코더 | 상용 | 관절 내 발열, 공개 데이터 부족 | 공백 |
| 6 | 손·외피·케이블 | 다밀도 폼·텍스타일, 힘줄, PUR/TPE 외피, Class 6 무산소동 | 손가락, 외피, 하네스 | 상용(외피는 소모품화) | 손·피부 소재 비공개 | 소재 설계는 공백, 촉각 디코딩은 활발 |
| 7 | 소프트 액추에이터(인공근육) | DE, HASEL, SMA/SMP, LCE, TCP 섬유, 하이드로젤, IPMC, 자성 복합체, 공압 엘라스토머 | 인공근육, 소프트 그리퍼 | 대부분 시제품, NiTi·공압 그리퍼 상용 | 내구성 데이터와 표준 부재 | 편차 큼: SMA·자성 복합체·TCP는 성숙, LCE·IPMC·HASEL 소재 설계는 공백 |
| 8 | 신축 센서·전자피부 | 압저항(CNT, AgNW, EGaIn), 용량형, 압전(PVDF), 마찰전기, 이온성, 멤리스터 나노와이어, 자성 피부, 광학 | 촉각 피부, 손끝 | 실험실~초기 상용 | 실사용 내구성 | 디코딩은 성숙, 소재 설계는 초기 |
| 9 | 신축 전도체·전자 | EGaIn 액체금속, PEDOT:PSS, 금 박막 나노복합체, 신축 Zn‖MnO₂ 전지 | 배선, 전극, 전원 | 실험실 | 확장 공정 미정 | 초기: 로봇+ML 워크플로 1건(2026) |
| 10 | 기능성 구조 | 자가치유 PU, 입자·층 재밍, SMP 격자, 메타물질, 키리가미, 4D 프린팅 복합체 | 외피, 가변강성 관절, 충격흡수 | 실험실~시제품 | — | 높음: 역설계 성숙 |
| 11 | 마이크로·의료·바이오하이브리드 | NdFeB-실리콘, 광응답 LCE, Pt 나노모터, 배양 근육+스캐폴드, 개구리 세포 | 마이크로로봇, 바이오하이브리드 손 | 실험실·전임상 | 생체 적합성, 규제 | 제어 중심, 소재·형태 설계 일부 |
| 12 | 친환경·생분해 | 젤라틴 바이오젤, 생분해 HASEL, PLGA, 실크 | 일회성·환경 로봇 | 실험실 | — | 낮음: 분해 예측 ML과 리뷰 단계 |

### 1. 구조재: 기계가공에서 금형 공정으로, PEEK는 '과열' 경고

구조재의 가장 확실한 변화는 소재보다 공정에서 일어나고 있다. Figure 03은 "Figure 02 was primarily designed to be manufactured with CNC machining"이었던 데서 다이캐스팅·사출·프레스 중심으로 바뀌었고, 질량은 9% 줄었으며, BotQ 1세대 라인은 연 12,000대 규모다(회사 원문 확인)([Figure](https://www.figure.ai/news/introducing-figure-03)). 이 전환이 맞다면 소재 선택 기준은 비강성에서 주조성·사출성·금형 비용으로 옮겨간다. PEEK에 대해서는 이전 노트의 인용 방향을 바꿔야 한다. Kingfa의 로봇기술 총괄 위페이(Yu Fei)가 한 말의 요지는 채택 확산이 아니라 경고였다. 그는 "the hype surrounding the concept has significantly outpaced its actual practical value"라고 말했다(인터뷰 원문 확인)([Gasgoo](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)).

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 공급망·상용화 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| Al 합금(기계가공재, 다이캐스트) | 링크 튜브, 액추에이터 하우징, 팔 주물, AMR 섀시, 배터리 외함 | 액추에이터 구조부품은 "steel (predominantly) and aluminum alloys" 의존(IDTechEx) ([R&A News](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)); Figure 03 다이캐스트 전환 | 상용 | 금형 공정 전환; 대당 Al kg 수치는 비공개(IDTechEx 유료) | ML 주조합금 설계 리뷰 존재, 로봇 적용 없음 ([JMI](https://www.oaepublish.com/articles/jmi.2025.99), 미확인(스니펫)) |
| Mg 합금(무희토 Mg-Al-Zn-Ca-Mn 등) | 경량 하우징·프레임 | ML 설계 Mg-2Al-1Zn-0.6Ca-0.4Mn: UTS 344 MPa·연신 21.3%; MZAX2000: 395 MPa·17.9% | 학술·일부 상용 | 부식; 1차 Mg 중국 의존(미확인) | 동료심사(초록 스니펫, 원문 미대조) ([JMI 2025](https://www.oaepublish.com/articles/jmi.2024.92); [J. Magnesium Alloys](https://doaj.org/article/0b1d91fb06334606986c0d9a8c4fd201)) |
| Ti 합금(LPBF) | 고하중 브래킷, 프린팅 노드 | — | 틈새 | 비용, 항공 수요와 경쟁 | LPBF ML: Ti-45Nb에서 기공은 해치 간격·출력, 미용융 Nb는 출력·주사속도가 좌우 ([UVic](https://dspace.library.uvic.ca/items/189ed91b-b50f-48cb-9b64-69049f3a03e6), 미확인(스니펫)) |
| CFRP, CF 열가소성 | 사지 외피, 대퇴·하퇴 링크 | 비강성 | 시제품 | 비용, 접합 | 로봇 특화 ML 소재 설계 없음; Husky Carbon은 Grasshopper 진화 솔버로 생성설계 (원문 확인) ([arXiv 2104.05834](https://arxiv.org/abs/2104.05834)) |
| PEEK, CF-PEEK | 외장, 관절, 감속기 부품 | 밀도 약 1.3 g/cm³(Al의 약 절반); Huaxiang Qiyuan 개질 PEEK 유성감속기 270 g(금속 대비 약 70% 경량), PEEK 구조로 대당 5.3 kg 절감 | 초기 채택(Tesla·Unitree·Agibot 채택은 기사 서술) | 2024년 PEEK 시장 61억 위안, 휴머노이드 수요 2027년 40억 위안 이상 전망; "확장 가능한 응용 미형성" | AI 없음; Optimus Gen 2 "PEEK로 10 kg 감량·30% 속도 향상"은 블로그 주장, Tesla 미확인 ([Gasgoo](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673); [peekchina](https://peekchina.blogspot.com/2024/12/why-peek-is-key-material-for-teslas.html)) |
| 범용 엔지니어링 플라스틱(PA-GF, PC-ABS, POM) | 외장, 커버, 부싱 | 휴머노이드 1대에 플라스틱 6~10 kg, 재료비 1,000위안 이상; 맞춤형 80~90%, 양산 전 배합·구조 3~5회 조정 | 상용 | CNC에서 사출로 전환 | 없음 (기업 인터뷰 원문 확인) ([Gasgoo](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)) |
| AM 격자·위상최적화 구조 | 다리, 팔, 링크 | 사족보행 위상최적화 다리: 나일론 PA2200, FEM E₀ 1,700 MPa; EPFL 격자 다리는 자체 무게 3배 이상 지지·7.5 mm/s 보행 | 시제품, 상용 CAD | — | AI 위상최적화 모듈형 팔(2025, 원문 확인) ([FH OÖ](https://pure.fh-ooe.at/en/publications/ai-driven-topology-optimized-modular-robotic-arm-design-for-legge/)); 다리 ([Sci. Rep. 2023](https://www.nature.com/articles/s41598-023-32106-5), 원문 확인); EPFL ([PMC12266121](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12266121/), 미확인(스니펫)); XPeng IRON 격자 "근육"은 2차 주장 ([FacFox](https://facfox.com/docs/kb/3d-printed-photopolymer-lattices-the-hidden-muscle-behind-xpengs-humanoid-robot)) |

### 2. 구동·모터/자석: 문제는 총량이 아니라 Dy·Tb 접근권이다

대당 NdFeB 약 4 kg을 IDTechEx가 말한 연 100만 대 규모(원문 미확인)에 곱해도 연 수천 톤이다. Adamas가 전망한 2040년 세계 수요 **88만 톤 이상**에 비하면 작다([Oregon Group](https://theoregongroup.com/latest-news/where-will-the-metals-for-the-robot-revolution-come-from/)). 따라서 병목은 총량보다 중희토류(Dy·Tb) 접근과 수출 라이선스다. Adamas의 극단 시나리오(2040년 100억 대면 현재 NdFeB 생산의 186배 필요)는 상한선 사고실험으로 읽어야 한다([Adamas 2025-02-14](https://www.adamasintel.com/humanoid-robots-and-the-future-of-motors-and-ndfeb-markets/)). 정책은 이 지점을 겨누고 있다. 한국 K-문샷 소재 미션은 "중희토류 완전 배제 및 경희토류 극저감" 영구자석 공정과 폐자석 회수를 2027년부터 개발한다([KDI](https://eiec.kdi.re.kr/policy/materialView.do?num=287736)). Genesis Mission 2차 선정에는 UIUC의 희토류 추출용 redox-active 리간드 설계(AXIS)와 ORNL의 양자자석 역설계가 들어 있다([energy.gov](https://www.energy.gov/articles/energy-department-announces-new-genesis-mission-awards-advance-super-intelligence-science)). 그러나 로봇 모터용 자석에서 결정립계확산 Dy 저감을 ML로 최적화한 원문은 찾지 못했다.

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 공급망 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 소결 NdFeB(NdPr, Dy/Tb 결정립계확산) | 모든 관절의 프레임리스 토크·코어리스 모터 로터 | 고 (BH)max, 고온 보자력; 대당 약 4 kg(Adamas, 원문 확인); 휴머노이드 약 60 kg 가정(Adamas 인용); 1만 대당 30 t 이상(스니펫) | 상용 | 2025-04 7종 라이선스 유지; 2025-10 확대분 유예 2027-01-10까지; JL Mag는 휴머노이드 수요를 "small pilot orders"로 표현(스니펫) ([faxiangongchang](https://faxiangongchang.com/en/reports/china-rare-earth-magnet-2026)) | 로봇 모터 특화 ML 자석 최적화 원문 없음; MS의 "NdPr 1.3 kg/대", FAI의 "2~4.5 kg"은 미확인 |
| 질화철 FeN(Niron) | 저사양 관절·팬(전망) | 에너지적은 NdFeB보다 낮음(미확인) | 파일럿 → Sartell 공장 연 1,500 t, 2027년 초 가동 | 미 국방부 OSC 최대 1.5억 달러·20년 조건부 대출, 총비용 6.05억 달러, 2공장 연 1만 t 2028년 착공 예정 | 없음 (회사·전문지 원문 확인) ([Mining.com](https://www.mining.com/niron-breaks-ground-on-rare-earth-free-magnet-manufacturing-plant-in-minnesota/); [Charged EVs 2026-08-19](https://chargedevs.com/newswire/niron-magnetics-wins-conditional-150-million-loan-commitment-for-rare-earth-free-magnets/)) |
| AI 설계 무희토 자석 MagNex(Materials Nexus) | 모터 일반(로봇 명시 없음) | 조성 1억 개 이상 탐색, 3개월 개발, 소재비 20%, 소재 탄소배출 70% 감소; Br·Hcj·BHmax 동료심사 데이터 없음 | 실험실 | — | 기업 주장 (원문 확인) ([Mining.com](https://www.mining.com/ai-helps-quickly-develop-rare-earth-free-permanent-magnet/)) |
| 전기강판·SMC, Cu 권선 | 스테이터 | 고주파 철손(데이터 미확보) | 상용 | Cu 가격 | 사례 없음(공백) |

### 3. 동력전달·관절: 소재는 '합금강'까지만 공개되고, 격차는 열처리 노하우다

감속기 소재의 실체는 거의 공개되지 않는다. Harmonic Drive LLC는 플렉스플라인을 "a thin cylindrical cup made from alloy steel"로만 설명한다(원문 확인)([Harmonic Drive](https://www.harmonicdrive.net/technology/harmonicdrive)). 해설 자료는 "Steel grade, grain size control and surface treatment decide fatigue life as much as the drawing does"라고 쓰고, 2024년 파손 분석은 파괴 원인을 개재물이 아니라 조대한 구오스테나이트 결정립에서 찾았다([humanoid.guide](https://humanoid.guide/?p=20671)). 중국산 하모닉 감속기가 Leaderdrive를 통해 **세계 점유율 약 15%(2위)**까지 따라잡은 반면([Gasgoo 2026-08-28](https://autonews.gasgoo.com/articles/news/leaderdrive-plans-hong-kong-ipo-2093357096908443649)) RV 감속기는 뒤처진 이유도 조성보다 공정·열처리 노하우로 설명된다. 원가 비중은 출처마다 다르다. Morgan Stanley Almanac은 Optimus Gen 2 BOM 약 46,000달러 중 액추에이터 22,000~58,000달러를 제시했다. 중국을 뺀 공급망이면 BOM은 131,000달러로 오른다([Yahoo Tech](https://tech.yahoo.com/science/articles/china-packs-patent-punch-race-093000841.html)). Interact Analysis는 액추에이터를 재료비의 30~50%로 본다([Korea JoongAng Daily](https://www.koreajoongangdaily.com/business/actuators-become-new-battleground-in-humanoid-robot-race/12288658)). AI는 기어·베어링 강에서 학술 단계다. TU Delft는 전이학습과 진화 알고리즘으로 "only tens of fatigue data points"만으로 피로 저항 강을 고처리량 설계했다(원문 확인)([TU Delft](https://repository.tudelft.nl/record/uuid:470d0944-7409-4633-9e61-23092137c72d)). 그러나 이 연구를 포함해 로봇 감속기에 적용된 사례는 없다.

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 공급망 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 플렉스플라인 합금강(강종 비공개; 담금질·질화 설계 예) | 하모닉 감속기(손목, 팔꿈치, 어깨) | 피로파괴가 주 고장 모드; 결정립·열처리가 수명 좌우 | 상용 | HDS 약 50%(스니펫) ([marketresearch](https://marketresearch.com/GlobalInfoResearch-v4117/Global-Strain-Wave-Gearing-Devices-39350161)), Leaderdrive 약 15%·2026-08 H주 홍콩 상장 승인 | FE+S-N 피로해석(학술) ([DOAJ](https://doaj.org/article/0b39259eca3f4d018806d054cb9b857e), 미확인(스니펫)) |
| RV 사이클로이드 디스크·핀 기어(40CrNiMoA 계열로 보도) | 산업용 팔 베이스·어깨 | 비틀림 강성, 내충격 | 상용 | Nabtesco "약 60%"(회사 자료), 제3자 추정 35~60% | 없음 ([Plant Automation](https://www.plantautomation-technology.com/suppliers/nabtesco-motion-control-inc), 회사 주장) |
| 유성 롤러스크루(PRS)·볼스크루용 베어링강(강종 미확인) | 리니어 액추에이터 | 하중 용량, 나사 연삭 정밀도; 개당 1,350~2,700달러(MS·JPM 귀속 상충) | 상용 | GSA·Rollvis·Ewellix·SKF가 70% 이상, 중국 수입의존 약 80%(스니펫); Optimus PRS 14개 vs 4개 상충 | 없음 ([holistic.news](https://holistic.news/en/planetary-roller-screws-essential-for-robotics/)) |
| 하이브리드 Si₃N₄ 볼 베어링 | 크로스롤러·출력 베어링 | 강 대비 최대 약 40% 경량, 충격에 취성(스니펫) | 상용 틈새 | — | 없음 ([Barden](https://www.bardenbearings.co.uk/hybrid-bearings)) |
| 그리스·윤활제 | 감속기, 스크루 | 마찰·마모·수명 | 상용 | — | 스태킹 앙상블로 아미드계 그리스 R² 0.9939(마찰계수)·0.9535(마모흔) ([Friction](https://sciopen.com/article/10.26599/FRICT.2025.9440982), 미확인(스니펫)); 산업 적용 없음 |
| ML 설계 기어·피로강 | 일반 기어(로봇 미적용) | 수십 개 피로 데이터로 설계(TU Delft); ORNL 베이나이트강은 52100 대비 내마모(풍력, 스니펫) | 학술 | — | TU Delft 원문 확인; ORNL 미확인 ([ORNL](https://ornl.gov/technology/202405685)) |
| 힘줄 섬유(UHMWPE, 아라미드, LCP·ePTFE, 강선) | 손가락 구동 | UHMWPE는 강하지만 크리프; 아라미드는 크리프가 적지만 마모가 빠름; 강선은 작은 굴곡반경에서 피로 파손 | 상용·연구 | Optimus 힘줄 소재 비공개(강선 설은 티어다운 근거 없음) | 없음 (해설 원문 확인) ([humanoid.guide](https://humanoid.guide/?p=16664)) |

### 4. 에너지: 2.3 kWh 팩, 구조형 외함, 그리고 전고체의 첫 시장

휴머노이드 팩은 2.3 kWh 근처에 모인다. Figure F.03의 사양은 "2.3 kWh enables 5 hours of run time at peak performance", 능동냉각 2 kW 급속충전, UN38.3·UL2271 동시 인증 추진이다. 외함은 "high strength stamped steel, die cast aluminum and structural adhesives"로 만들고, 열폭주 전파 차단에 단열 포팅을 쓰며, 셀 간 와이어본드를 퓨즈처럼 동작하게 조정했다(회사 원문 확인)([Figure](https://figure.ai/news/f-03-battery-development)). 이전 노트의 "1.2 kWh" 표기는 원문과 맞지 않는다. 로봇은 소량이지만 사람 곁에서 쓰여 안전에 프리미엄을 내는 시장이다. 그래서 전고체 배터리 업체가 로봇을 첫 시장으로 겨냥한다는 해석이 나온다.

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 공급망 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| Li-ion 셀·팩(Figure F.03) | 몸통 배터리 | 2.3 kWh, 피크 5시간, 2 kW 충전, UN38.3·UL2271 | 상용 | 리튬 | 없음 (회사 원문 확인) |
| 구조형 팩 소재 | 외함, 열폭주 차단, 셀 연결 | 프레스 강판·다이캐스트 Al·구조용 접착제, 단열 포팅, 퓨즈형 와이어본드 | 상용 | — | 없음 (회사 원문 확인) |
| Optimus Gen 2 팩 | 몸통 배터리 | 약 2.3 kWh·52 V | — | — | Morgan Stanley 티어다운 추정, Tesla 미확인 ([liveinthefuture](https://liveinthefuture.org/stories/optimus-battery-irrelevance-43-robot-model-s-math)) |
| 전고체(황화물 등) | 휴머노이드 팩 | CALB 450 Wh/kg 이상 주장; XPeng IRON 소량 생산; Farasis 2025-09 황화물 샘플 출하 | 소량·샘플 | — | 미확인(스니펫) ([Gasgoo](https://autonews.gasgoo.com/articles/icv/will-robots-be-the-first-to-sample-solid-state-batteries-2052295407034589184)); TrendForce 2035년 로봇 전고체 수요 74 GWh 전망 ([TrendForce](https://www.trendforce.com/presscenter/news/20260128-12902.html)) |
| Na-Li 혼합 고체전해질(MS–PNNL) | 차세대 셀 | 3,200만→23개(신규 18개), 80시간, Li 최대 약 70% 감소 | 실험실 | 리튬 저감 | 기업 주장(회사 원문 확인); 물질명 "N2116"은 원문에 없음 ([Microsoft](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)) |
| 양극재(KAIST–POSCO) | 차세대 셀 | 탐색 기간 93% 단축; 12배는 24시간·500회 가정 추정 | 실험실, 2026년 이후 POSCO N.EX.T Hub 적용 계획 | — | 자율실험실(기관 원문 확인, 실측 아님) ([KAIST](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)) |
| 고체 Li 이온 전도체 후보 | — | GNoME이 기존 연구보다 25배 많은 후보 제시 | 계산 | — | 언론 ([VentureBeat](https://venturebeat.com/ai/google-deepminds-materials-ai-has-already-discovered-2-2-million-new-crystals/)) |

한국 AI 소재 전략의 첫 자율실험센터가 양극재·액체전해질·고체전해질을 다루는 이차전지 센터라는 점도 이 카테고리와 직접 맞물린다([동아사이언스(다음)](https://v.daum.net/v/20260430101533808)).

### 5. 전자·센싱·열관리: GaN은 관절 안으로, 열은 여전히 미문서화 영역

관절 일체형 드라이버의 소재 전환은 GaN이 주도한다. EPC91120은 지름 32 mm 보드에 EPC23102 GaN 하프브리지 3개를 얹었다. 15~55 V에서 21 A 피크(15 ARMS 연속)를 내고, 히트싱크 없이 26 °C에서 7 ARMS, 모터 케이싱에 장착하면 15 ARMS를 흘리며, 자기식 엔코더 인터페이스를 내장한다(전문지 원문 확인)([Power Electronic Tips](https://www.powerelectronictips.com/three-phase-gan-driver-fits-32-mm-robotic-joints/)). Infineon의 "관절 70개·전력 스위치 600개"라는 주장은 원문을 확인하지 못했다. 원문이 확인된 Infineon 측 발언은 오히려 "GaN Does Not Replace Silicon"이라는 공존론과 최고 성능 관절에서는 전환이 느릴 것이라는 전망이다([All-About-Industries](https://www.all-about-industries.com/how-infineon-powers-the-joints-of-humanoid-robots-with-gan-a-c1b49d5c860ed39961e2c4e400e662d0/)).

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 공급망 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| GaN 전력소자 | 관절 3상 인버터 | EPC91120: 32 mm, 15~55 V, 15 ARMS 연속, 무방열판 7 ARMS | 상용 | 반도체 공급 | 없음; EPC91122·91132 신제품은 Cloudflare로 미확인 |
| 힘/토크 센서 플렉셔(경화강, 17-4 스테인리스, 경질 Al) | 발목·손목 6축 센서 | ATI Mini85: 경화강 트랜스듀서+항공용 Al, 고항복강도 스테인리스 와이어 EDM 가공; KSensors는 17-4 스테인리스 또는 경질 Al | 상용 | — | 없음 (회사 원문 확인) ([New Equipment Digest](https://www.newequipment.com/classified/mini85-force-torque-sensor-for-humanoid-robots-170211.html); [KSensors](https://ksensors.co.kr/en/?p=287205)) |
| 엔코더(자기식, 광학식 유리·Mylar 디스크) | 관절 위치 측정 | 자기식 16~18-bit로 보행로봇에서 선호; 광학식은 최대 24-bit지만 충격·습기에 취약 | 상용 | — | 없음 (미확인(스니펫)) ([PatSnap Eureka](https://eureka.patsnap.com/article/optical-encoders-vs-magnetic-encoders-in-precision-robotics)) |
| 열계면 소재(얇은 열전도 테이프·패드) | 관절 내부 방열 | 1차 데이터 없음 | 상용 | 공간 제약 | 공백 (벤더 자료만) ([ysdiecut](https://www.ysdiecut.com/?p=42243)) |

### 6. 손·외피·케이블: 외피는 '의류'가 되고, 손 소재는 여전히 비공개

외피는 구조재에서 소모품으로 바뀌고 있다. Figure 03은 끼임 방지용 "multi-density foam"을 "soft textiles"로 덮었다. 이 소재는 "fully washable"이고 공구 없이 교체되며, 상업 고객은 내절단 소재를 고를 수 있다. 손끝 센서는 3 g의 힘을 감지한다. Figure는 기존 상용 촉각센서가 "could not withstand real-world use"라고 판단해 자체 개발했다고 밝혔다. 그러나 센서와 피부 소재명은 공개하지 않았다(회사 원문 확인)([Figure](https://www.figure.ai/news/introducing-figure-03)). Tesla Optimus 손은 손 22 DoF에 손목·전완 3 DoF를 더했고, 모든 액추에이터를 전완으로 옮겨 탄성 케이블 힘줄로 당긴다([Electrek](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/)). 2026년 11월 5일 공개된 특허 출원 US 2026/0346473 A1은 하나의 "floating tendon-like cable"이 두 관절을 구동하는 구조다. 다만 기사는 "A patent application is not a product commitment"라는 단서를 달았다([TeslaNorth](https://teslanorth.com/2026/11/06/tesla-robot-hand-tendon-cable-fingers/)).

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 공급망 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 다밀도 폼 + 소프트 텍스타일 | 전신 외피 | 세척 가능, 공구 없이 교체, 내절단 옵션 | 상용(Figure 03) | 소모품화 | 없음 (회사 원문 확인) |
| 손끝 소프트 소재·촉각센서 | 손가락 | 3 g 감지, 손바닥 카메라 | 상용 시제품 | 소재 비공개 | 디코딩 중심 (회사 원문 확인) |
| 힘줄 구동 손(Optimus, Shadow) | 손가락 관절 | Optimus 손 22 DoF; Shadow Hand 모터 20개·24 DoF 힘줄 구동 | 시제품·연구용 상용 | 힘줄 소재 비공개(Shadow의 Dyneema는 2차 출처) | 없음 ([Shadow Robot](https://www.shadowrobot.com/dexterous-hand-series/)) |
| 로봇 케이블(PUR/TPE 외피, Class 6 무산소동, 주석도금 구리 편조 차폐) | 관절 통과 하네스 | igus chainflex CF9 TPE ±90° 비틀림, CFROBOT PUR·전체 차폐; Joca 2,000만 회 이상 굴곡 시험(벤더) | 상용 | — | 없음 (벤더 원문 확인) ([igus](https://www.igus.com/info/robotic-cables); [Joca](https://joca-cable.com/robot-cable/960-cy-p/)) |

강체 로봇 계열 전체에서 확인된 사실이 하나 있다. Tesla, Figure, Unitree, Hyundai·Boston Dynamics, LG, Rainbow Robotics 가운데 **ML 설계 소재나 생성설계 부품을 양산에 썼다고 공개한 곳은 없다.** Boston Dynamics는 CES 2026 Atlas의 56 DoF, 50 kg 들어올리기 같은 사양은 공개했지만 구조재는 공개하지 않았다([Boston Dynamics](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/)). 한국 기업은 액추에이터 조립·양산에 집중한다. Hyundai Mobis는 Atlas 액추에이터를 2028년 3만 대 규모로 양산할 계획이지만, CES 시제품에는 해외산 액추에이터가 쓰였다([Korea JoongAng Daily](https://www.koreajoongangdaily.com/business/actuators-become-new-battleground-in-humanoid-robot-race/12288658)). LG Axium은 2027년 외부 공급이 목표이고 SPG와 감속기 제휴를 맺었다([Korea Herald](https://www.koreaherald.com/article/10808594)). 감속기와 소재는 여전히 외부에 의존한다.

### 7. 소프트 액추에이터(인공근육): 계열 간 수치가 자릿수로 다르고, AI의 침투도도 그렇다

소프트 액추에이터는 계열마다 변형률·응력·속도·효율이 자릿수로 다르다. 그래서 수치는 단위와 출처를 붙여서만 비교해야 한다. DE의 "VHB 380% 이상"은 **면적** 변형률이다. Pelrine 등 2000년 Science 초록의 헤드라인은 실리콘 117%, 아크릴 215%로 측정 방식이 다르다([OpenAlex](https://api.openalex.org/works/doi:10.1126/science.287.5454.836)). 380%, 7.2 MPa, 이론 에너지밀도 3.4 MJ/m³(골격근 0.07 MJ/m³)는 공저자 Pei 그룹의 리뷰에 실린 값이다([NSF PAR](https://par.nsf.gov/servlets/purl/10128818)). IDTechEx는 휴머노이드에서 강체 액추에이터가 "continue to be the mainstay"이고, 소프트 액추에이터는 하이브리드 설계에서 일부 역할을 할 것으로 본다([R&A News](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)).

| 소재 | 메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 상용화 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 유전 엘라스토머(DE: VHB 4910, Elastosil 등 실리콘) | 유연 전극 사이 Maxwell 응력 | VHB 면적 변형률 >380%, 7.2 MPa(리뷰); Pelrine 초록 실리콘 117%·아크릴 215% | 시제품, 일부 틈새 상용 | 고전압, 절연파괴 수명 | **DEA 로봇 시험 SDL**: 수명 최대 100% 향상, 최적 DEA 사족보행이 무구속 체중의 100% 이상(액추에이터 무게의 700% 이상) 하중, "first … self-driving lab approach into robotic actuator design" 주장(프리프린트, 초록 확인) ([arXiv 2602.20963](https://export.arxiv.org/api/query?id_list=2602.20963)); 물리정보 하이브리드 NN이 FEM 대비 <5% 오차(프리프린트) ([arXiv 2202.12977](https://arxiv.org/pdf/2202.12977)) |
| 전기유압(HASEL, Peano-HASEL) | 정전기 zipping으로 유체 이동 | Peano-HASEL 선형 수축 최대 10%, 900%/s, 50 Hz, 자기 무게 200배 이상 들어올림 | 시제품, 스핀오프 | 힘·변형률 한계 | 소재 설계 ML 없음; 스펙트럼 부분다양체 데이터 모델로 HASEL-클러치 관절 실시간 제어, 추종오차 대폭 감소(프리프린트) ([Kellaris 2018](https://api.openalex.org/works/doi:10.1126/scirobotics.aar3276); [arXiv 2601.03247](https://export.arxiv.org/api/query?id_list=2601.03247)) |
| 꼬임·코일 고분자 섬유(TCP: 나일론 낚싯줄 등) | 가열 시 코일 꼬임 풀림 | 수축 49%, 동일 길이·무게 근육보다 100배 이상 무거운 하중, 5.3 kW/kg, 비히스테리시스·장수명(원문 확인) | 시제품 | 열구동 효율 | **이산 BO**: 가능한 1,089개 조합 중 62개만 제작해 구동 변형률 1.25 달성(3개 공정 변수, Materials & Design 2025, 원문 확인) ([Haines 2014](https://api.openalex.org/works/doi:10.1126/science.1246906); [Aalto](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat)) |
| CNT 얀 근육 | 이온·열 구동 | 코일 CNT 얀 수축 일 3.78 kJ/kg | 실험실 | 비용 | ML 없음(비ML 장력 최적화만) ([UT Dallas](https://utd-ir.tdl.org/items/ebf1c023-506f-44a6-bc37-e1b2e066ac13)) |
| 형상기억합금(NiTi, NiTiHf)·형상기억고분자(SMP) | 마르텐사이트↔오스테나이트 상변태, 유리전이 | NiTiHf는 Ni 49.8→51.3 at.%에서 Ms가 약 500 °C→−200 °C로 변할 만큼 조성에 민감(스니펫) | NiTi 와이어 상용, NiTiHf 시제품 | — | NASA ML: Ni-Ti 다성분 합금 8,000종 이상·37개 원소·52개 입력, 신규 실험으로 검증(원문 확인), MAE 14.8 °C 등 구체값은 **미확인** ([NTRS 20220014943](https://ntrs.nasa.gov/citations/20220014943)); ML 발견 Ni49.7Ti26.6Hf23.7 Af 403.5 °C(스니펫) ([J. Mater. Sci.](https://link.springer.com/article/10.1007/s10853-022-07793-6)); SMP 격자 역설계로 기록적 회복응력(동료심사, 스니펫) ([NSF PAR](https://par.nsf.gov/servlets/purl/10403742)) |
| 액정 엘라스토머(LCE) | 네마틱↔등방 전이, 배향장 프로그래밍 | DLP 프린팅 LCE 63 J/kg·0.18 MJ/m³; 그래핀-LCE 섬유 650 J/kg·293 W/kg(근육의 약 17배·6배) (원문 확인) | 실험실·시제품 | 느린 응답 | FEM 1,500회 학습 대리모델(학회 초록) ([APS](https://meetings-archive.aps.org/mar/2023/b14/1)); 수반 감도 기반 경사 최적화 ([PMC11125878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11125878/)); BO는 미세로봇 광패턴 보행에만 적용, **소재·공정 BO는 공백** ([PMC8302124](https://pmc.ncbi.nlm.nih.gov/articles/PMC8302124/); [PMC9646516](https://pmc.ncbi.nlm.nih.gov/articles/PMC9646516/)) |
| 하이드로젤(PNIPAM, PAAm/알지네이트 이중망) | 팽윤·수축, LCST 전이 | 이번 조사에서 수치 미확보 | 실험실 | 속도·강도 | PAAm/알지네이트 배합 BO(동료심사) ([PMC11422183](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11422183/)); 메타섬유 강화 하이드로젤 GAN 역설계 ([PMC11165469](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11165469/)); 저가 "frugal twin" SDL로 PNIPAM LCST 최적화(프리프린트) ([arXiv 2509.05351](https://arxiv.org/html/2509.05351v1)) |
| 이온성 EAP(IPMC, 이온겔) | 이온 이동에 의한 굽힘 | 수치 미확보 | 실험실·틈새 | 수분·히스테리시스 | 3D 프린팅 IPMC의 **BO 학습제어**로 시변 동역학 완화(Sci. Rep. 2019, 원문 확인) ([PMC6877587](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6877587/)); 소재 설계 ML 없음; KAIST Ionograsper의 AI 결합은 계획 단계 ([Newswise](https://www.newswise.com/articles/kaist-develops-a-venus-flytrap-inspired-robot-hand-material-that-senses-objects-and-grasps-them-under-light)) |
| 자성 소프트 복합체(NdFeB 미립자/실리콘) | 외부 자기장 하 프로그램된 자화 | 설계공간 시트 약 1.2×10^752, 빔 약 1.8×10^53; 생성 설계 500만 개 공개 DB | 실험실·전임상 | NdFeB | NN 예측+저비용 시뮬레이션(MAP-Elites 계열)으로 자화·형상 공동최적화, 직관 설계가 이륙에 실패한 점프 과제 성공(Nat. Commun. 2025, 원문 확인) ([PMC11947188](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947188/)); "53회·1.5×10⁷ 평가"는 미확인 |
| 공압 엘라스토머(Ecoflex, Dragon Skin, DLP 수지) | 챔버 가압 팽창 | KAIST·KIST DLP 엘라스토머: 점도 약 2,500 mPa·s, 파단연신율 600% 초과, 그리퍼 200 kPa 이상에서 유리병·달걀·마우스 파지 | 그리퍼 상용 | 점도-신축성 상충 | **36개 배합**으로 회귀 대리모델 학습(BO 아님, BO는 향후 과제), Nat. Commun. **2026-06-04**(원문 확인) ([nature.com](https://www.nature.com/articles/s41467-026-73735-4)); "1 kg 물병"은 본문에서 미확인; 확산모델 팽창 구조·ETH 저차원 공동설계는 프리프린트 ([arXiv 2603.06497](https://arxiv.org/html/2603.06497v1)) |
| 자가치유 인공근육(3층 구조) | 손상 감지 피부+자가치유 TPE | ICRA 2025 최우수논문 후보 | 실험실 | — | 손상 감지·치유 제어 수준 ([UNL](https://ncmn.unl.edu/news/husker-engineers-advance-work-intelligent-self-healing-technology/)) |

이 표에서 패턴이 보인다. 대형 합금 데이터베이스가 있는 SMA는 조성→물성 지도학습이 가능하다. 시뮬레이터가 싼 자성 복합체와 LCE 배향장은 대리모델 설계 루프가 돈다. 실험이 비싼 TCP 섬유, 하이드로젤, DEA 수명은 BO와 SDL로 간다. 화학이 복잡하고 시험이 느린 LCE 배합, 이온성 고분자, HASEL 유전액은 소재 설계 ML이 비어 있다. 신뢰성(사이클 수명, 절연파괴)이 최대 변형률 대신 ML의 목표로 떠오르는 것은 새로운 흐름이다.

### 8. 신축 센서·전자피부: ML은 신호를 읽는 데 능하고, 소재를 만드는 데는 아직 초기다

e-skin에서 ML은 이제 기본 해석 도구다. 이번 검증으로 대표 사례의 정체와 수치가 정리되었다. 이전 보고서의 "Nature Materials 2025 다중 모달 e-skin"은 서울대 고승환 교수 그룹의 논문 "Unisensory processing of interleaving memristive nanowires…"였다. 이 논문은 2025년 10월 24일 온라인에 게재되었고 2026년 3월호에 실렸다. 단일 멤리스터 나노와이어 네트워크가 열·기계 감지를 16 Hz로 전환하며, 초록에 확인되는 수치는 "20 household objects with **83% accuracy**"다(원문 확인)([nature.com](https://www.nature.com/articles/s41563-025-02373-w)). 많이 인용되는 **65%→95%**는 언론 보도에만 있는 수치다([ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing)).

| 변환 방식 | 대표 소재 | ML 사례와 수치 | 성숙도 | 검증 상태 |
|---|---|---|---|---|
| 압저항 | EGaIn 미세채널/실리콘, CNT·그래핀·AgNW 망 | EGaIn-실리콘 장갑 제스처 인식: 랜덤포레스트 약 97.3%, LDA 약 87.4% | 실험실~상용(촉각 패드) | 동료심사(스니펫) ([PMC8125695](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8125695/)) |
| 용량형 | 엘라스토머 유전체+신축 전극 | 신축 감지 장갑이 상용 데이터 장갑보다 손 자세 복원 35% 향상 | 상용(장갑, 어레이) | 동료심사(스니펫) ([NSF PAR](https://par.nsf.gov/biblio/10602565-interactive-hand-pose-estimation-using-stretch-sensing-soft-glove)) |
| 마찰전기 | 다공성 PDMS, 불소고분자 | 마찰전기-용량 하이브리드 12개 샘플 98.46%; SVM 그리퍼 98.1% | 실험실 | 동료심사(스니펫) ([PMC11543809](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11543809/); [RePEc](https://ideas.repec.org/a/nat/natcom/v11y2020i1d10.1038_s41467-020-19059-3.html)) |
| 멤리스터 나노와이어(서울대) | 단일층 멤리스터 나노와이어 | 손끝 센서 1개로 가정용품 20종 83%; 65%→95%는 언론 | 실험실 | 83% 원문 확인, 65→95% 언론 |
| 3D 구조형 다층(칭화대 3DAE-Skin) | 피부 층별 모듈러스를 모사한 3D 배치 | 법선력·전단력·변형률 분리, 촉각으로 모듈러스·곡률 측정(초록); 센서 240개·약 0.1 mm 분해능·딥러닝은 연구자 인터뷰 | 실험실 | 초록 원문 확인, 240개·0.1 mm는 언론 ([OpenAlex](https://api.openalex.org/works/doi:10.1126/science.adk5556); [China Daily](https://govt.chinadaily.com.cn/s/202406/05/WS6673996e498ed2d7b7eb0c2c/chinese-scientists-design-bio-inspired-3d-e-skin.html)) |
| 광 변조 다중 모달(SuperTac) | 두께 1 mm 광필드 변조 피부+마찰전기+관성 | 힘 0.06 N, 위치 0.4 mm, 온도 0~90 °C, 근접 15 cm 미만, 질감·재질 등 94% 초과; 촉각 언어모델 DOVE 85억(논문) vs 8.5억(칭화대 보도) 매개변수 상충 | 실험실 | 원문 확인(2026-01-15) ([nature.com](https://www.nature.com/articles/s44460-025-00006-y); [Tsinghua](https://www.tsinghua.edu.cn/info/1175/123978.htm)) |
| 자성 피부 | 정현파 자화 필름(약 0.5 mm)+홀 센서 | 법선·전단력 자체 분리, 딥러닝으로 60배 초해상 | 실험실 | 초록 원문 확인 ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Soft%20magnetic%20skin%20for%20super-resolution%20tactile%20sensing%22&format=json)) |
| 압전·인공피부 역설계 | PVDF·BaTiO₃ 복합체 등 | 소규모 데이터 ML로 물성→구조 역설계, 기존 대비 효율 최소 4자릿수 향상 | 실험실 | 프리프린트(초록 확인) ([arXiv 2304.04609](https://export.arxiv.org/api/query?id_list=2304.04609)) |
| 자가치유 감지 피부 | 자가치유 하이드로젤 등 | 5,000회 탐침 학습 후 위치 2.3 mm, 손상 후 200회 미만 탐침으로 전이학습 재적응; 옥스퍼드 피부는 10초 안에 기능 약 80% 회복 | 실험실 | 이전 라운드 출처 ([DOAJ](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d); [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:149873d8-5227-4cbb-a6f8-5dc61f397e9d)) |

92~100% 분류 정확도는 대부분 약 12개 물체로 된 작은 닫힌 집합에서 나온 것이다. 일반화를 보여주지 않으므로 논문 간 비교는 무의미하다. ML이 신호 해석에서 하는 일은 단순한 소프트웨어 개선이 아니다. 성긴 센서와 단순한 배선으로도 쓸모를 만들어 소재 설계의 자유도를 넓힌다. 그러나 감지 소재 자체(배합, 미세구조)를 ML로 설계한 사례는 액추에이터보다도 드물다.

### 9. 신축 전도체·전자: 2026년, 로봇이 만들고 ML이 고른 첫 신축 전극

첫 라운드에서 이 카테고리는 "ML은 하류(디코딩)에만 있다"고 정리되었다. 이번 검증에서 그 판단을 일부 뒤집는 논문이 확인되었다. 메릴랜드대 Po-Yen Chen 그룹은 2026년 1월 19일 Nature Communications에 신축 전극 설계 워크플로를 발표했다. 이 워크플로는 **로봇 자동화 실험, 능동학습 ANN 앙상블, 유한요소 시뮬레이션**을 묶었다. 그 결과 얇은 금 층을 입힌 미세 텍스처 나노복합체를 찾았고, 그림 설명에 따르면 이 소재는 **1,000% 이상 신장에서도 금속 수준의 전도도**를 유지한다. 같은 전극에 Zn과 MnO₂를 전착해 변형에 둔감한 신축 Zn‖MnO₂ 전지도 만들었다(원문 확인)([PMC12916966](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916966/)). 이는 이번 조사에서 확인된 유일한 ML 연계 신축 전지 결과다.

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 금 박막 미세텍스처 나노복합체 + 신축 Zn‖MnO₂ 전지(UMD) | 변형 둔감 전극, 신축 전원 | 1,000% 이상 신장에서 금속 수준 전도도(그림 설명) | 실험실 | 스케일업 미정 | 로봇 자동화+능동학습 ANN+FE(동료심사, 원문 확인) |
| 신축 전도체 분류기(같은 계열로 추정) | — | 조성 286개로 SVM 학습 후 능동학습·증강으로 1만 점 이상 | 학회 | — | 미확인(학회 초록 스니펫) ([AIChE 2022](https://www.aiche.org/academy/conferences/aiche-annual-meeting/2022/proceeding/paper/697f-automatic-stretchable-conductor-design-and-fabrication-machine-learning)) |
| PEDOT:PSS 투명 전도막 | 전극, 센서 | Polybot 7차원 공정에서 평균 4,500 S/cm 이상 | 실험실 | — | SDL 최적화(동료심사, 원문 확인) ([Nat. Commun.](https://www.nature.com/articles/s41467-024-55655-3)); 신축성 PEDOT:PSS 배합 ML은 없음 |
| 액체금속 EGaIn | 신축 배선, 센서 | 제스처 장갑 97.3%(디코딩) | 실험실 | — | ML 소재 설계 없음; CMU Majidi 그룹은 소프트 센싱 ML 리뷰(2020) ([Crossref](https://doi.org/10.1002/aisy.201900171)) |

### 10. 기능성 구조: 시뮬레이터가 있는 곳에서 AI 역설계가 가장 성숙했다

자가치유, 가변강성, 메타물질, 키리가미, 4D 프린팅은 AI 역설계가 가장 확립된 영역이다. 순방향 모델(ResNet, GNN, VAE)이 많고, 목표(응력-변형 곡선, 목표 형상)가 분명하며, FEM 데이터가 싸기 때문이다. 가장 인상적인 새 근거는 소규모 데이터 능동학습이다. 형광 자가치유 폴리우레탄 연구는 **실험 데이터 20개**만으로 기계적 성능과 치유를 함께 최적화했다. 종합 성능 지표의 상대오차는 12% 미만이었고, 이산 성능 데이터가 있으면 15개 시료로도 최적에 도달했으며, 평균 R²는 0.8을 넘었다. 기존 기준 모델은 테스트 R²가 0.10~0.40까지 떨어지는 과적합을 보였다(원문 확인)([PMC12758484](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758484/)). 이 논문의 최초 게재일은 2025년 12월 23일이고 2026년 권호에 실렸다.

| 소재 | 적용 부품·메커니즘 | 핵심 물성·대표 수치 | 성숙도 | 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 자가치유 폴리우레탄 | 로봇 외피, 인공근육 층 | 20개 실험, 상대오차 <12%, R² >0.8, NSGA-III 파레토 | 실험실 | 강도-치유 상충 | 화학정보 능동학습(Chem. Sci., 원문 확인); EU SHERO(약 €300만) ML 손상 감지·치유 ([The Robot Report](https://www.therobotreport.com/machine-learning-self-healing-soft-robotics/)) |
| 기계적 메타물질(트러스, 격자) | 충격흡수, 관절 컴플라이언스 | 목표 비선형 응답 역설계 | 실험실~시제품 | 제조 결함 | Harvard Bertoldi 신경망 가속 진화전략(Adv. Mater. 2022) ([Harvard MRSEC](https://mrsec.harvard.edu/research/highlight_222.php)); GraphMetaMat 그래프 생성(Nat. Mach. Intell. 2025) ([Berkeley](https://engineering.berkeley.edu/news/2025/07/a-smarter-approach-to-designing-metamaterials/)); 트러스 그래프 VAE ([Nat. Commun. 2023](https://www.nature.com/articles/s41467-023-43217-y)); LCE 메타물질 NN+진화전략 ([BUAA](https://research.buaa.edu.cn/zh/publications/inverse-design-of-smart-mechanical-metamaterials-based-on-liquid-/)) |
| 충격흡수 적층 구조 | 보호 구조 | ML 유도 실험 25,000회 이상 | 실험실 | — | BU SDL(프리프린트) ([arXiv 2308.02315](https://pdf.arxiv.org/pdf/2308.02315)) |
| 키리가미 시트 | 변형 가능 외피, 그리퍼 | 목표 형상 역설계 | 실험실 | — | 지도 오토인코더(Phys. Rev. Res. 2020) ([APS](https://archive.aps.org/mar/2020/m34/4)); 군집·탠덤 NN·기호회귀 ([npj Comput. Mater. 2022](https://www.nature.com/articles/s41524-022-00873-w)) |
| 4D 프린팅 능동 판(능동/수동 복셀) | 형상 변환 구조 | 목표 3D 형상 변화 역설계 | 실험실 | — | ResNet 순방향+ML-GD·ML-EA 역설계, Stanford Zhao 그룹(Nat. Commun. 2024, 원문 확인) ([OpenAlex](https://api.openalex.org/works/doi:10.1038/s41467-024-49775-z)) |
| 입자·층 재밍(가변강성) | 가변강성 관절, 그리퍼 | 층 재밍 FE가 "수십 시간" 걸려 ML 대리모델로 대체 | 실험실 | — | 가상일 원리 기반 회색상자 NN(J. Bionic Eng. 2024, 서지 확인) ([Crossref](https://doi.org/10.1007/s42235-024-00563-x)); UC Berkeley ML 최적화 3D 프린팅 재밍(학회, 스니펫); 층 재밍 대리모델(스니펫) ([NSF PAR](https://par.nsf.gov/servlets/purl/10557920)) |

### 11. 마이크로·의료·바이오하이브리드: ML은 주로 제어에 있고, 설계는 몇 개의 예외다

마이크로·의료 로봇에서 ML은 주로 제어에 쓰인다. 대표 사례가 자성 마이크로로봇의 3D 위치를 강화학습으로 자율 제어한 Nature Machine Intelligence(2024) 연구다([MDPI review](https://mdpi.com/2227-7390/12/14/2180)). 소재·형태 설계의 예외는 몇 개다. 제노봇 연구에서는 AI 시뮬레이션이 찾은 반원환(C자) 형태가 구형 클러스터의 최대 2회 자기복제를 **최대 4회**로 늘렸다(원문 확인)([PMC8670470](https://pmc.ncbi.nlm.nih.gov/articles/PMC8670470/)). 촉매 나노모터에 대해서는 2019년의 검증된 ML 설계 논문 한 편이 있다. 13개 특징과 4개 알고리즘으로 속도·정화 효율을 예측했고(평균 절대오차 0.10, 0.12), 모델로 설계한 Pt 코팅 나노모터는 **예측오차 15% 미만**이었다(초록 확인)([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Accelerated%20Design%20of%20Catalytic%20Water-Cleaning%20Nanomotors%20via%20Machine%20Learning%22&format=json)).

| 소재 | 적용·메커니즘 | 핵심 수치 | 성숙도 | 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| NdFeB·강자성 입자/실리콘·PDMS, 자성 하이드로젤 | 외부 자기 토크·힘으로 구동하는 마이크로·밀리로봇 | 직관 설계가 실패한 점프 성공(Nat. Commun. 2025) | 실험실·전임상 | 생체 적합성 | NN+시뮬레이션 공동설계(원문 확인); RL 제어(동료심사, 리뷰 경유) |
| 광응답 LCE | 구조광 구동 마이크로로봇 | 수치 미확보 | 실험실 | — | GP-BO 보행 학습(2018, 제어 최적화) ([ar5iv 1809.03225](https://ar5iv.labs.arxiv.org/html/1809.03225)) |
| Pt·Janus 촉매 나노모터 | 화학 추진 | 설계 모터 예측오차 <15% | 실험실 | — | 그래디언트 부스팅 지도학습(ACS AMI 2019, 초록 확인); ML 추적(Nanoscale 2023)은 특성분석 용도 ([ScienceDaily](https://www.sciencedaily.com/releases/2023/11/231114143902.htm)) |
| 개구리 세포(제노봇) | 섬모 구동, 운동학적 자기복제 | 복제 최대 2회→4회 | 실험실 | 윤리·규제 | 진화·AI 형태 설계(PNAS 2021, 원문 확인) |
| 배양 쥐 근육+소프트 스캐폴드(ETH) | 액체 속 점프·보행 | 계산상 2층 근육/스캐폴드 적층이 유리 | 실험실 | 조직 변이성 | 계산 공동설계(Nat. Commun. 17:10732, 2026); ML 여부 미확인 ([Netzwoche](https://www.netzwoche.ch/news/2026-11-01/ein-kleiner-sprung-fuer-den-muskel-ein-grosser-schritt-fuer-die-robotik)) |
| 배양 인간 근육 다발(도쿄대 MuMuTA) | 다섯 손가락 바이오하이브리드 손 | 길이 18 cm, 10분 전기자극 후 피로, 1시간 내 회복, 액체 속 매달아야 작동 | 실험실 | 영양 공급, 수명 | **ML 없음** (Sci. Robotics 2025-02) ([News-Medical](https://www.news-medical.net/news/20250214/Biohybrid-hand-with-muscle-tissue-mimics-real-life-movements.aspx)) |

### 12. 친환경·생분해: 성능은 비분해 소재에 근접했지만 ML은 리뷰 단계다

생분해 액추에이터는 성능에서 비분해 소재를 따라잡았다. 이번 검증으로 사이클 수의 귀속도 정리되었다. 생분해 고분자 필름, 에스테르계 액체 유전체, NaCl 함유 젤라틴 하이드로젤로 만든 전기유압 액추에이터는 "**200 V/μm**"까지 안정 동작하고 "more than **100,000** actuation cycles"를 견딘다. 이것은 Rumley 등(Science Advances, 2023-03-22)의 수치다(원문 확인)([OpenAlex](https://api.openalex.org/works/doi:10.1126/sciadv.adf5551)). "**33만 회 이상** 무고장"은 Baumgartner 등(Nature Materials, 2020)의 젤라틴 바이오젤 공압 코끼리 코 액추에이터에 대한 수치다. 다만 초록에는 없고 언론 보도로만 확인된다([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41563-020-0699-3%22&format=json); [SYFY Wire](https://www.syfy.com/index%2Ephp/syfy-wire/biodegradable-robot-made-of-food-safe-ingredients)).

| 소재 | 적용·메커니즘 | 핵심 수치 | 성숙도 | 이슈 | AI 적용 사례와 검증 상태 |
|---|---|---|---|---|---|
| 생분해 HASEL(생분해 필름, 에스테르 유전체, 젤라틴 전극) | 전기유압 | 200 V/µm, 10만 회 이상 | 실험실 | — | 없음 (원문 확인) |
| 젤라틴-글리세롤 바이오젤 | 공압 굽힘 | 33만 회 이상(언론); 분해 진행 시 성능 저하를 FEM이 R² 최대 0.997로 재현 | 실험실 | 습도 의존 | 물리·FEM 모델(ML 아님) ([Frontiers 2021](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.760485/full)) |
| 생분해 전자 포함 소프트 로봇(서울대 강승균 교수) | 임무 후 흙으로 돌아가는 로봇 | — | 실험실 | — | ML 없음 (Nature Sustainability 2026-03, 언론) ([Asiae](https://view.asiae.co.kr/en/article/2026031309094463564)) |
| PLGA, 실크 | 생분해 마이크로로봇 | — | 실험실 | 산성 분해 산물 | PLGA 분해 거동 ML 예측(2026, 스니펫) ([MGEA](https://journal.hep.com.cn/mgea/EN/10.1002/mgea.70062)); 생분해 소프트 로봇 소재 ML 리뷰 ([Discover Materials 2026](https://link.springer.com/article/10.1007/s43939-026-01059-7)); 로봇 수준 ML 설계 없음 |

### 소재 계열별 AI 성숙도 요약

| 단계 | 소재 계열 | 주된 AI 역할 | 대표 근거(검증 상태) |
|---|---|---|---|
| A. 산업 도구화 | 구조 링크·브래킷(형상) | 위상최적화·생성설계 CAD | MX3D·ABB 팔 부품 생성설계(스니펫) ([Digital Engineering 24/7](https://www.digitalengineering247.com/article/mx3d-makes-3d-printed-robotic-arm-lenovo-and-amd-partner-for-new-workstation-autodesk-releases-generative-design-extension-more)); Figure 03은 금형 공정 전환(AI 언급 없음) |
| B. 동료심사 실험 검증(로봇 부품 직결) | TCP 섬유, 자성 소프트 복합체, DLP 엘라스토머, 자가치유 PU, 4D 프린팅 판, 신축 전극(UMD) | BO·능동학습, NN 대리모델+진화·경사, 로봇+ML 워크플로 | Aalto 62/1,089, Karacakol 2025, KAIST·KIST 2026, Chem. Sci. 20개, Sun 2024, Chen 2026 (모두 원문 확인) |
| B′. 동료심사 실험 검증(로봇 미적용) | 경량 Mg 합금, 피로강, SMA(NiTi·NiTiHf) | 대리모델·해석형 ML 합금 설계 | Mg 344·395 MPa(스니펫), TU Delft(원문 확인), NASA 8,000종 데이터셋(원문 확인) |
| C. 계산·시뮬레이션 설계 위주 | 메타물질·키리가미, LCE 배향장, 바이오하이브리드 형태, 재밍 | 생성모델, 대리모델, 진화 탐색 | GraphMetaMat, Bertoldi 2022, 제노봇, 재밍 회색상자 NN |
| D. 기업 주장·파일럿 | 무희토 자석, 고체전해질, 양극재 | 대규모 스크리닝, 자율실험실 | MagNex, MS–PNNL, KAIST–POSCO (회사·기관 원문 확인, 독립 검증 없음) |
| E. 디코딩·제어 중심 | e-skin 전반(압저항·마찰전기·자성·광학), IPMC, HASEL, 마이크로로봇 | 분류·초해상, 학습제어, RL | 서울대 83%, SuperTac >94%, IPMC BO 제어, HASEL 스펙트럼 모델 |
| F. 공백 | 감속기 강종·윤활(산업), 전기강판·SMC, PEEK·CFRP·엘라스토머 외피, 열계면·EMI, LCE 배합·공정, 이온성·HASEL 소재, CNT 얀, PEDOT:PSS·EGaIn 배합, PLGA·실크 로봇 | — | 원문으로 확인된 로봇 특화 ML 소재 설계 없음 |

요약하면 "ML이 소재를 설계한다"는 주장은 검증된 시뮬레이터가 있는 곳(자성, 4D 프린팅, 메타물질)과 실험이 짧고 싼 배합 최적화에서 가장 강하다. 화학이 복잡하고 수명 시험이 느린 시스템에서는 약하다. 그리고 그 약한 곳이 휴머노이드 원가의 중심과 겹친다.

## 남은 병목은 데이터·고체 핸들링·신규성 판정·내구성이며, 해법은 '검증 가능한 자율성'이다

### 데이터와 벤치마크: 알고리즘보다 편향과 누수가 먼저다

소재 ML의 첫 제약은 데이터다. 반응 수율 예측 모델은 측정 잡음에는 강하지만, 실패한 반응을 보고하지 않는 인간 선택 편향에는 크게 흔들린다([phys.org](https://phys.org/news/2022-06-clearer-negative-experimental-results-reaction.amp)). 무작위 분할 대신 군집 단위 교차검증(LOCO-CV)을 하면 일반화 성능이 "크게 과대평가"되어 있었음이 드러난다([Digital Discovery MatFold](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)). Materials Project로 학습한 모델은 새로 추가된 항목에서 성능이 급락했다([arXiv 2210.13597](https://www.arxiv.org/pdf/2210.13597)). 자가치유 PU 연구의 기준 모델이 테스트 R² 0.10~0.40으로 떨어진 것도 같은 문제다([PMC12758484](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758484/)). SDL 벤치마크 자체도 문제다. SDL 연구의 60%가 직접 벤치마크를 보고하지 않는다([arXiv 2508.06642](https://arxiv.org/pdf/2508.06642)). 해법은 세 갈래로 수렴한다. 첫째, FAIR 인프라다. OPTIMADE는 2026년 3월 현재 20개 데이터베이스 제공자와 2,500만 개 이상 소재를 하나의 API로 묶었다([arXiv 2603.23536](https://arxiv.org/html/2603.23536v1)). 둘째, 실패를 포함한 전수 기록이 가능한 SDL 자체가 음성 데이터 부족을 해결한다. KAIST–POSCO 실험실도 성공·실패 데이터를 모두 DB에 쌓는다([KAIST](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)). 셋째, 국가 단위 AI-ready 데이터(한국 1,000만→5,000만 건)와 보고 규범이다. AF·EF를 무작위 기준선 대비로 보고하고 Volk·Abolhasani의 7개 지표를 함께 쓰는 것이 최소 기준이 되어야 한다. 산업 컨소시엄의 데이터 신탁이나 연합학습 같은 IP 보존형 공유 사례는 이번에도 찾지 못했다.

### 신규성 판정: 무질서 인식과 사람의 결정학 검토를 루프에 넣어야 한다

A-Lab·GNoME·MatterGen 논쟁이 남긴 교훈은 구체적이다. Leeman 등은 다섯 가지를 권고했다. 새롭다고 할 때 어떤 의미인지 밝힐 것, 계산 예측에서 조성 무질서를 명시적으로 고려할 것, 적합도 통계만으로 성공을 판정하지 말 것, 조성 측정을 구조 측정만큼 중시할 것, 그리고 "inverse Occam's razor"를 피할 것이다([NSF PAR](https://par.nsf.gov/servlets/purl/10532478)). Juelsholt는 MatterGen 사례에서 무질서 인식 매처만으로도 부족하며 "rigorous human verification"이 필요하다고 결론지었다([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1039/D6MH00268D&format=json&resultType=core)). 이를 SDL 설계로 옮기면 세 가지가 필요하다. 첫째, 학습 데이터와 ICSD의 정렬·무질서 상을 모두 대조하는 신규성 게이트다. 둘째, 자동 Rietveld 결과를 조성 분석(EDS 등)과 교차 확인하는 다중 모달 판정이다. 셋째, 정정 사례처럼 사후 동료심사를 받는 수작업 재분석 단계다. Genesis Mission의 "Designing Materials with Predictable Functionality" 과제가 예측·합성·특성분석을 하나의 폐루프로 묶은 것은 방향이 맞다([White House](https://www.whitehouse.gov/releases/2026/07/45502/)). 다만 판정 기준을 공개하는지가 관건이다.

### 하드웨어: 소재 SDL은 분말과 고체를 다뤄야 한다

소재 SDL의 하드웨어 문제는 화학·바이오 SDL보다 어렵다. NIST는 박막·벌크·분말이 각각 다른 핸들링을 요구한다며 고체 시료 이송을 소재 자동화의 고유 과제로 꼽았다([NIST](https://www.nist.gov/node/1874991)). 분말 XRD의 종단간 자동화는 시료 준비 때문에 특히 어렵다([arXiv 2501.06847](https://arxiv.org/html/2501.06847v1)). 토론토 그룹은 SDL을 염두에 두고 장비를 설계하는 제조사가 거의 없다고 지적했다([Chemspeed](https://www.chemspeed.com/news/autonomous-chemical-experiments-challenges-and-perspectives-on-establishing-a-self-driving-lab)). 해법은 모듈화와 네트워크화다. 장비 통신 표준 SiLA 2와 ROS를 결합하고([SLAS Technology](https://real.mtak.hu/206359/1/02_1-s2.0-S2472630324000505-main.pdf)), 기존 장비를 사람과 공유하는 이동 로봇(리버풀 2024)과 저가 "frugal twin"([Digital Discovery](https://pubs.rsc.org/en/content/articlehtml/2024/dd/d4dd00059e))을 쓰며, 상호운용성·안전·재현성 표준을 세우는 것이다([Strathprints, Pickles et al.](https://strathprints.strath.ac.uk/95936/7/Pickles-etal-Matter-2026-community-discussion-on-harmonizing-and-accelerating-self-driving-laboratories.pdf)). 정책은 공유 시설로 수렴하고 있다. NSF는 프로그래머블 클라우드 랩에 4억 달러를 배정했다([White House](https://www.whitehouse.gov/fact-sheets/2026/10/fact-sheet-trump-administration-announces-the-most-ambitious-set-of-science-initiatives-this-century/)). 베이징 방안은 자율실험실 표준과 등급별 평가를 과제로 넣었고([Beijing gov](https://english.beijing.gov.cn/investinginbeijing/InvestmentSpecial/DigitalEconomy/PolicesAndInterpretations/202607/t20260715_4763931.html)), 한국 협의체는 레퍼런스 자율실험실과 표준 정립을 임무로 삼았다([아시아경제](https://view.asiae.co.kr/article/2026081109490769317)).

### 모델과 안전: OOD 일반화와 에이전트형 LLM

모델의 핵심 약점은 분포 밖(OOD) 일반화다. MatBench 상위 GNN들은 OOD 과제에서 오히려 덜 견고했다([arXiv 2401.08032](https://arxiv.org/pdf/2401.08032.pdf)). Matbench Discovery의 범용 원자간 퍼텐셜은 안정성 사전 선별에서 F1 0.57~0.82였다([LBL](https://eta-publications.lbl.gov/bibcite/reference/36666)). 대응책은 불확실성 정량화다. 범용 퍼텐셜의 이종 앙상블로 만든 불확실성 지표는 실제 오차를 잘 따라갔고, 텅스텐에서는 DFT 데이터의 약 4%만으로 전체 학습 성능에 도달했다([arXiv 2507.21297](https://arxiv.org/html/2507.21297v1)). 실험실을 구동하는 LLM 에이전트는 새로운 위험을 낳는다. LabSafety Bench는 765개 객관식 문항과 404개 현실 실험실 시나리오(개방형 과제 3,128개)로 19개 LLM·VLM을 평가했다. 위험 식별에서 **70%를 넘은 모델은 없었다**. 이 연구의 최종 게재지는 Nature Machine Intelligence 8권(2026)이다(원문 확인)([arXiv 2410.14182](https://arxiv.org/abs/2410.14182)). 이전 노트의 "520개 시나리오"는 오류다. SciHazard는 12개 분야의 유해 질문 2,400개와 과잉안전 질문 600개로 31개 모델을 평가했고, 딥리서치 에이전트의 평균 위해 점수가 표준 LLM보다 **32.3% 높았다**. 이 연구는 NeurIPS 2026 E&D 트랙에 채택되었다(원문 확인)([arXiv 2607.18665](https://arxiv.org/abs/2607.18665)). 다만 SciHazard의 에이전트는 웹·도구 연구 에이전트이지 물리 실험실을 구동하는 SDL 에이전트가 아니다. 따라서 "에이전트화가 위험을 키운다"는 간접 증거로만 쓸 수 있다. 안전은 모델 정렬만으로는 부족하다. 경계가 정해진 실험실 인터페이스, 시약 화이트리스트, 사람의 승인 게이트처럼 하드웨어·API 계층에서 설계해야 한다([arXiv 2608.23104](https://arxiv.org/pdf/2608.23104)). 소재 SDL 전용 안전 벤치마크는 여전히 없다.

### 로봇 소재: 내구성 데이터, sim-to-real, 그리고 닫히지 않은 액추에이터 루프

AI로 설계한 로봇 소재가 실험실을 벗어나려면 내구성을 넘어야 한다. 기존 액추에이터는 5~10년 연속 운전을 견디지만, 소프트 공압 액추에이터는 피로·박리·마모로 훨씬 빨리 열화한다. 수명 연구도 제한적이고 파편화되어 있다. HKUST는 그래서 표준 내구성 시험 프로토콜을 제안했다([HKUST](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)). 표준 피로 데이터가 없으면 ML은 수명을 학습할 수 없다. DEA 시험 SDL이 수명을 최적화 목표로 삼은 것([arXiv 2602.20963](https://export.arxiv.org/api/query?id_list=2602.20963))과 NeurIPS 2026이 소프트 액추에이터의 장기 복원력을 AI 과제로 제시한 것([NeurIPS 2026](https://neurips.cc/virtual/2026/167788))은 이 방향의 첫걸음이다. 시뮬레이션 쪽에서는 소프트 소재의 초탄성·소성·이방성 구성 법칙이 필요하다([arXiv 2512.15994](https://arxiv.org/html/2512.15994v1)). 고충실도 FEA는 실시간보다 수백 배 느리고, 공동설계 기법은 구현 가능성을 보장하지 못한다([arXiv 2505.03761](https://arxiv.org/abs/2505.03761)). 제안된 해법은 학습형 잔차 보정([arXiv 2603.22039](https://arxiv.org/pdf/2603.22039))과 프로토타이핑을 루프에 넣는 것이다. 가장 큰 구조적 빈칸은 따로 있다. 2026년 11월 현재 **소프트 로봇 액추에이터 소재를 자율로 합성·제작하고 시험까지 하는 폐루프 SDL은 없다.** 존재하는 것은 셋으로 나뉜다. 액추에이터의 자율 *시험*(DEA SDL), 전도체의 로봇 자동 *합성+시험*(UMD), 그리고 수작업 합성 위에서 돌리는 BO·능동학습(Aalto TCP, 자가치유 PU, KAIST·KIST 엘라스토머)이다. 이 셋을 잇는 것이 다음 이정표다.

| 문제 | 핵심 증거 | 제안된 해법 |
|---|---|---|
| 선택 편향·음성 데이터 부족 | 실패 반응 미보고가 모델을 왜곡 | SDL 전수 기록, 실패 결과 출판, FAIR(OPTIMADE, NOMAD) |
| 벤치마크 누수·OOD 과대평가, 가속 보고 불투명 | MatFold, MLIP Arena, SDL 60%가 벤치마크 미보고 | LOCO-CV, 무작위 기준선 대비 AF·EF 보고, 7개 지표 동시 보고 |
| 신규성 오판(무질서 상) | A-Lab 24/36 무질서 버전, MatterGen 1971년 화합물 | 무질서 인식 매칭+조성 측정, 결정학자 검토, 사후 재분석 |
| 분말·고체 핸들링, 특성분석 자동화 | NIST, 분말 XRD 자동화 난점 | 범용 시료 홀더, SiLA 2/ROS, 인라인 센싱 |
| 비용·통합 역량 | 실제 구축된 SDL이 적음 | frugal twin, 클라우드 랩(NSF 4억 달러), 국가 공유 자율실험센터 |
| 자율성 수준 비표준 | Tom·MITRE·Volk 체계 불일치, Level 5 없음 | 하드웨어×소프트웨어 2차원 등급 표준화 |
| LLM 에이전트 안전 | LabSafety 70% 미만, SciHazard +32.3%(간접) | 경계 인터페이스, 승인 게이트, SDL 전용 벤치마크 |
| 소프트 소재 내구성·sim-to-real | 피로·박리, FEA 속도·정확도 한계 | 표준 내구성 프로토콜, 수명을 ML 목표로, 잔차 학습 |
| 액추에이터 소재 폐루프 부재 | 시험 SDL과 합성 SDL이 분리 | DEA·LCE·HASEL 대상 합성+시험 통합 SDL |
| 휴머노이드 핵심 소재의 AI 공백 | 자석·감속기 강·PEEK에 로봇 특화 ML 없음, OEM 공개 사례 없음 | 희토류 저감 자석 계산-로봇 파이프라인, 피로강 ML의 감속기 적용 |

## 검증이 바꾼 수치와 아직 남은 상충

### 정정·정밀화된 주요 수치

| 항목 | 이전 보고서·노트 | 검증 후 | 상태 |
|---|---|---|---|
| A-Lab 정정 후 결과 | 36/40 vs 36/57 충돌 | 둘 다 맞음: 정정 공고는 보고 성공 40건 중 36건, 본문은 표적 57개 중 36개(63%); 원래 41/58, 인간 개입 포함 43 | 원문 확인 |
| A-Lab "신규" 정의 | 플랫폼 기준 신규 | "new to the prediction platform, not necessarily new to science"; 제목 novel→inorganic; Zn₂Cr₃FeO₈ 제외 | 원문 확인 |
| GNoME 736 | 독립 합성 736개 | ICSD에 독립 보고된 실험 구조 중 GNoME 구조와 일치한 736개(GNoME가 합성한 것 아님); 신규 381,000·총 421,000 | 원문 확인 |
| MatterGen 선행 화합물 | 1972년 보고 | 1971년 최초 기술된 Ta₁/₂Cr₁/₂O₂ | 초록 원문 확인 |
| MatterGen "20% 이내" | — | 최대 측정값 169 GPa 기준; 평균 158 GPa면 약 21% | 원문 확인 |
| SDL 중앙값 6배 | 기준 전략 대비 6배 가속 | 같은 성능 도달에 필요한 실험 수의 비, 주로 무작위 대비; 42개 연구·63개 벤치마크, 범위 1.3~100 | 원문 확인 |
| Clio +13% | 상용 기준 대비 약 13% | 최고 셀끼리 +13%, 최악 셀끼리 +5% | 원문 확인 |
| RoboChem 80% | 약 80% 사례에서 문헌보다 높은 수율 | 무작위 문헌 4편 재현에 대한 연구책임자 발언, 나머지 20% 비슷 | 언론(보도자료) |
| USTC 서지 | Nature Synthesis 2023-11 | 온라인 2023-11-13, Nature Synthesis 3권(2024) | 원문 확인 |
| 액추에이터 56% | BOM 56%(Morgan Stanley) | **무게** 56%(IDTechEx); BOM은 MS Almanac 약 48%, BofA 2030년 51%(손 별도 19%) | 원문 확인 |
| KAIST–POSCO 12배 | 연구자 주도 대비 데이터 12배 | 24시간 운용·500회 가정 시 추정(84일→6일), 93% 단축 | 기관 원문 확인(추정치) |
| KIST "1만→24회" | 1만 회 탐색을 24회로 | "1만 vs 200"(작년)과 "촉매 24회"(최근)는 별개 성과 | 언론 |
| KAIST·KIST 엘라스토머 | Nat. Commun. 2025, 6배 신장 | 2026-06-04 게재, 파단연신 >600%, 36개 배합 회귀 대리모델(BO 아님) | 원문 확인 |
| 서울대 e-skin | Nature Materials 2025, 65→95% | 온라인 2025-10-24·2026-03호, 초록은 20종 83%; 65→95%는 언론 | 부분 원문 확인 |
| Northwestern 자동 설계 | 약 26초 | 논문은 "less than 30 s", 10회 설계 시도; MIT Rus 공저 | 원문 확인 |
| LabSafety Bench | NeurIPS 2025, 시나리오 520개 | Nat. Mach. Intell. 8, 20–31(2026), 시나리오 404개 | 원문 확인 |
| BIG-MAP 예산 | €1,600만 vs €2,000만 | €19,997,812.50 | 원문 확인 |
| Genesis DOE 자금 | 2.93억 vs 3.2억 달러 충돌 | 서로 다른 발표: 3.2억(2025-12 인프라), 2.9376억(2026-03 RFA) | 원문·법률 분석 확인 |
| Genesis 278개 과제 | 연구소 16·대학 142·기업 157 | 이 수치는 참여 기관 수; 과제 주도는 87·168·19·4; 2026-10에 297개 | 원문 확인 |
| 중국 희토류 유예 | 2026-11-10 만료 | 2027-01-10까지 2개월 연장(11-09 발표) | 언론 본문 확인 |
| CuspAI 리드 | Bezos·Kleiner 공동 리드 | Kleiner Perkins·NEA 리드, Bezos Expeditions 상당 참여 | 언론 본문 확인 |
| Periodic 리드 | a16z vs Felicis | a16z 리드, Felicis 참여 | 언론 본문 확인 |
| MS–PNNL 후보 수 | 18 vs 23 | 23개 중 5개 기지 → 신규 18개 | 회사 원문 확인 |
| 자율실험실 협의체 | 80여 기관 vs 50개사 | 수요기업 50 + 대학·연구기관 30여 = 80여 | 언론 본문 확인 |
| USPTO 가이던스 | 철회 | 2025-11-28 전면 폐지 후 개정 가이던스로 대체 | 원문 확인 |
| Figure F.03 외함 | 프레스 강판+주조 Al | 프레스 강판·다이캐스트 Al·구조용 접착제, 단열 포팅; 1.2 kWh 표기는 오류 | 회사 원문 확인 |
| Kingfa PEEK | 채택 확산 | 핵심 메시지는 과열 경고; 플라스틱 대당 6~10 kg | 인터뷰 원문 확인 |
| 생분해 액추에이터 사이클 | 귀속 불명 | 10만 회 이상·200 V/µm = Rumley 2023; 33만 회 이상 = Baumgartner 2020(언론) | 부분 원문 확인 |
| Niron 대출 날짜 | 2026-08-07 | 확인한 기사 게시일 2026-08-19 | 언론 확인 |

### 여전히 상충하거나 확인되지 않은 수치

| 항목 | 상충·미확인 내용 | 상태 |
|---|---|---|
| 대당 희토류 | Adamas 약 4 kg NdFeB(확인) vs FAI 2~4.5 kg·Dy 35~79 g, MS NdPr 1.3 kg | 후자 미확인 |
| 액추에이터 원가 비중 | MS 약 48%, BofA 51%+손 19%, Interact 30~50%, "60% 근처" 관측, Leaderdrive 기사의 "하모닉 감속기만 30~35%" | 정의 차이, 마지막은 신뢰도 낮음 |
| 감속기 점유율 | Nabtesco 약 60%(회사) vs 35~60%(제3자), 이전 노트의 53%; HDS 50%(스니펫) | 회사 주장·미확인 |
| Optimus 롤러스크루 | 14개 vs 4개(종아리); 개당 가격의 MS vs JPM 귀속 | 미확인 |
| Optimus PEEK | 10 kg 감량·30% 속도 향상; 대당 PEEK 6.6 kg vs 10.5 kg 추정 | 블로그·업계 홍보 |
| IDTechEx 전망 | "2030년경 100만 대", "80% 산업용" | 공개 원문에 없음(유료 본문) |
| Goldman Sachs 상향 | 2035년 650만 대·1,380억 달러 | 미확인 |
| Infineon·EPC | "관절 70개·스위치 600개", EPC91122·91132 사양 | 봇 차단으로 미확인 |
| SuperTac DOVE | 85억(논문) vs 8.5억(칭화대 보도) 매개변수 | 상충 |
| 칭화대 3DAE-Skin | 센서 240개·0.1 mm·딥러닝 | 언론 인터뷰만 |
| Karacakol 데이터셋 | "53회·1.5×10⁷ 평가" vs 논문의 "500만 설계" | 전자 미확인 |
| NASA NiTi ML | MAE 14.8 °C·7.2 °C·0.36% | 미확인 |
| HASEL 변형률 | Donut 약 50%·평면 79% | 2차 출처만 |
| VHB 변형률 | 리뷰 380%(면적) vs Pelrine 초록 215% | 측정 방식 차이 |
| KAIST 엘라스토머 | "1 kg 물병 파지" | 본문에서 미발견 |
| USTC | "−37 °C 안정성", "인간이면 2,000년", 300만 vs 370만 조성 | 미확인·외삽 |
| 리버풀 2024 | "1.75 m 로봇" | 미확인 |
| MARS | LLM 19개·도구 16개, 10회 반복 | 스니펫 |
| GNoME 무질서 비율 | Margraf의 80~84% 무질서 추정 | 2차 출처 |
| A-Lab 언론 인용 | Palgrave "덜 흥미롭지만 덜 결함", 수작업 XRD 약 12% 오귀속 보도 | 로그인 장벽·스니펫 |
| 투자 | Periodic 2026년 70억~75억 달러; Lila 시리즈 B(협상 보도); Orbital Materials 5,000만 vs 2억 달러 | 회사 미확인 |
| DeepMind 영국 랩 | 2026년 개소 | 개소 확인 없음 |
| 정책 예산 | 한국 AI 소재 전략·K-문샷 총예산, EU €5억 파트너십, Genesis 3.2억 달러 세부, DMREF 2021 6,530만 달러 | 원문에 없음·접근 실패 |
| Acceleration Consortium SDL 수 | 6개 vs 7개 | 미해결 |
| MarketsandMarkets 시장 수치 | 소재 인포매틱스·실험실 자동화 | 403으로 미확인 |
| Lila 비용 주장 | "백금보다 1,000배→10,000배 저렴"으로 배수가 커짐, 새 데이터 없음 | 기업 주장 확대 ([Mentat](https://mentat-s3r.pages.dev/finds/lila-sciences-platinum-free-catalysts-10000x-cheaper)) |

### 동료심사 결과와 기업·언론 주장의 구분

| 검증 수준 | 대표 주장 | 판단 |
|---|---|---|
| 동료심사 + 원문 확인 | Burger 6배 활성, Clio 42회·6배, Polybot 4,500 S/cm, SDL 중앙값 AF 6, Aalto 62/1,089, Karacakol 2025, KAIST·KIST 2026, Chem. Sci. 20개, UMD 신축 전극, Rumley 10만 회 | 정해진 공간의 최적화 성과로서 가장 신뢰할 만함 |
| 동료심사 후 정정·비판 | A-Lab(정정), GNoME 신규성, MatterGen TaCr₂O₆ | 플랫폼 능력 실증으로는 유효, "신소재 발견"은 축소해서 읽어야 함 |
| 동료심사(데이터셋·시뮬레이션 검증) | KRICT JCIM 2026, 4D 프린팅·메타물질 역설계 | 물리 시스템 실증 전 단계 |
| 프리프린트 | DEA 시험 SDL, SynAgent, HASEL 스펙트럼 모델, BU 25,000회, PNIPAM frugal twin | 동료심사 전 |
| 기관·기업 원문(독립 검증 없음) | KAIST–POSCO 93%·12배(추정), MagNex, MS–PNNL, Lila 2,942개·17배, Radical 1,200종, LG 1일 vs 22개월, Niron | 회사 발표, 독립 감사 없음 |
| 언론 보도만 | KIST 24회, KIMS 몇 주, 서울대 65→95%, RoboChem 80% | 1차 수치 미확인 |
| 블로그·확인 불가 | Optimus PEEK 10 kg·30%, Optimus 강선 힘줄 | 근거 부족 |

## 결론

이번 검증이 바꾼 그림은 이렇다. 로봇과 AI가 소재공학에서 낸 가장 확실한 가치는 새 물질의 발견이 아니다. **실험 수를 한 자릿수 배 줄이는 최적화**와 **실패까지 기록하는 재현 가능한 데이터**다. 수치를 원문과 대조하자 과장의 방향이 일관되게 드러났다. 무게 지표가 원가 지표로, 조건부 추정이 실적으로, 실험 수 기준이 시간 기준으로, 독립 보고 구조와의 일치가 합성 실적으로 옮겨져 있었다. 2027년에 지켜볼 지표도 그래서 기업가치나 후보 수가 아니다. 스타트업과 국가 프로그램이 무질서를 고려한 신규성 판정과 무작위 기준선 대비 가속 보고를 채택하는지가 관건이다. 자율실험실의 역할은 발견 엔진에서 **검증 엔진**으로 옮겨가고 있다. 로봇이 만든 특성분석 데이터는 신규성 판정, 특허 실시가능성, 투자 신뢰에 공통으로 쓰이는 자산이 되었다.

소재 분류 체계가 주는 새 통찰은 AI의 침투도가 시장 중요도와 반대로 놓여 있다는 점이다. AI는 시뮬레이터가 싸고 목표가 분명한 메타물질·자성 복합체·4D 프린팅, 그리고 센서 디코딩에서 성숙했다. 반면 휴머노이드 원가의 절반을 쥔 자석·감속기 강·엔지니어링 플라스틱과, 수명이 병목인 LCE·이온성·전기유압 액추에이터 소재에서는 거의 비어 있다. 따라서 다음 기회는 두 갈래다. 하나는 수명을 목적함수로 삼아 액추에이터 소재를 **합성부터 시험까지 닫는 SDL**이다. 다른 하나는 공급망 리스크가 가장 큰 **중희토류 저감 자석과 감속기 피로강을 겨냥한 계산-로봇 파이프라인**이다. 한국은 두 갈래에 필요한 조각을 모두 갖고 있다. 영구자석을 소재 미션으로 둔 K-문샷, 이차전지·모빌리티 자율실험센터, 80여 기관의 협의체, 그리고 액추에이터 양산에 나선 Mobis·LG다. 다만 지금의 한국 성과 수치는 대부분 기관 발표 수준이므로, 동료심사된 지표로 먼저 뒷받침해야 한다.

## 접근 상태 및 조사 한계

조사는 두 단계로 진행되었고, 단계마다 접근 조건이 달랐다. **첫 라운드**(이전 보고서 작성 시점)의 클라우드 세션은 Default 환경의 "limited" 네트워크 정책 아래 있었다. 허용 목록이 짧아 학술지·언론·정부 사이트를 직접 가져오는 시도는 거의 모두 실패했다. 노트에는 `getaddrinfo ENOTFOUND`로, 직접 점검에서는 프록시 403으로 기록되었다. 웹 검색만 정상이었으므로 그때의 근거는 검색 결과 요약과 스니펫이었다. 이번 라운드의 두 분류 노트(강체·휴머노이드, 소프트·마이크로)도 처음에는 같은 조건에서 스니펫으로 작성되었다. **두 번째 단계**에서는 사용자가 환경의 네트워크 접근을 unrestricted로 바꿨다. 그 뒤 대부분의 사이트가 Bash `curl`(에이전트 프록시 경유)로 열렸다. 그러나 WebFetch 도구는 여전히 DNS 단계에서 `getaddrinfo ENOTFOUND`를 반환했다. 같은 시각 curl로 arxiv.org가 200을 반환했으므로 이는 네트워크 정책이 아니라 WebFetch 도구 쪽 문제다. 그래서 네 개의 검증 노트는 모든 원문을 curl로 받아 BeautifulSoup·pdftotext로 추출해 읽었다. 그래도 일부 사이트는 계속 실패했다. 아래 표는 모든 노트의 "접근 상태 로그"에서 네트워크 변경 **이후에도** 실패한 호스트를 중복 없이 원인별로 묶은 것이다. 이 차단들은 출판사 봇 방어, 로그인·유료벽, 서버 오류, 요청 한도에서 생긴 **사이트 측 문제**이므로, 환경의 네트워크 설정을 바꿔서는 풀리지 않는다. 검색 색인의 영어권 편향 때문에 중국어(CNKI)·일본어(J-STAGE) 원어 자료도 충분히 다루지 못했다.

| 원인 | 호스트(결과) | 필요했던 자료 |
|---|---|---|
| 출판사·사이트 봇 방어(Cloudflare) | pubs.acs.org(403), pubs.rsc.org(403, articlehtml·landing·pdf 모두), www.science.org(403), journals.aps.org(403), chemrxiv.org(403), www.sciencedirect.com(403), europepmc.org 웹 UI(403), www.anl.gov(403), newscenter.lbl.gov(403), discovery.ucl.ac.uk(403), www.newswise.com(403), computing.mit.edu(403), epc-co.com(403), xenospectrum.com(403), www.wisdomtree.com(403), marketresearch.com(403), core.ac.uk(403) | Chem. Mater.·Chem. Rev.·JACS 원문, 한국 SDL 리뷰·Juelsholt 본문, RoboChem 본문, PRX Energy 출판사판, Leeman 프리프린트, Materials & Design 본문, Polybot·A-Lab 보도자료, EPC 신제품, MS NdPr 1.3 kg, HDS 점유율, iCub 토크센서 |
| 봇 방어(AWS WAF·CAPTCHA·클라이언트 챌린지) | www.chemistryworld.com(405 WAF captcha), www.eurekalert.org(202 빈 응답 또는 403), link.springer.com(Client Challenge), www.federalregister.gov HTML(CAPTCHA), eur-lex.europa.eu(202 빈 응답), mouser.vn·.com·.at·.in(Access denied), www.hpcwire.com(403), fourweekmba.com(403), www.futureelectronics.com(403), ornl.gov(403), zenodo.org API(403), www.spglobal.com(403) | Palgrave·Ceder 인용 기사, KRICT·서울대 영문 보도자료, NiTi ML 논문, COM(2024)98 €5억, Infineon 70/600, ML 베이나이트강, Karacakol 데이터셋, 희토류 분석 |
| 로그인·유료벽 | cen.acs.org(리드 문단 이후 로그인), www.reuters.com(401), www.marketsandmarkets.com(403), IDTechEx 보고서 본문(유료; 추정 ID가 다른 보고서 반환), Nature·Science 유료 본문(Pelrine 2000, Baumgartner 2020, 고승환 2025는 초록만), news.bloomberglaw.com(앞부분만 공개) | A-Lab 정정 C&EN 본문, Lila 13억 달러 단독, 시장 규모, 휴머노이드 소재 kg/대, VHB·330,000회·65→95% 원 수치 |
| JS 전용 페이지 | pmc.ncbi.nlm.nih.gov 기사 페이지(JS 봇 챌린지), s-space.snu.ac.kr(JS 필수) | PMC 본문(E-utilities로 우회), 한국 SDL 리뷰 리포지토리 사본 |
| 요청 한도(429) | api.openalex.org(약 10회 후 429), dealroom.co(429), api.crossref.org(간헐 429·500, 재시도 성공) | 초록·메타데이터, Periodic 70억 달러 보도 |
| 서버 오류·연결 실패·DNS | nanonet.mext.go.jp·dxmt.mext.go.jp(CONNECT 502), english.mofcom.gov.cn(DNS 해석 실패), www.kaist.ac.kr(연결 리셋), news.liverpool.ac.uk(302 후 500), hdl.handle.net(500), livrepository.liverpool.ac.uk(403 Apache), www.businesswire.com(HTTP/2 INTERNAL_ERROR), doaj.org API(타임아웃) | MEXT ARIM·DxMT 예산, MOFCOM 영문 공고, KAIST 메인, Liverpool 2024 보도자료, 한국 리뷰 핸들, Burger 저자 원고, EPC 보도자료, 플렉스플라인 강종 논문 |
| 404(URL 변경·삭제·추정 경로) | english.cas.cn(USTC 보도자료), smartcity.go.kr(K-문샷 안건 PDF), www.nsf.gov(2021 DMREF), periodic.com/blog, www.cusp.ai/news, www.pnnl.gov, www.nabtesco.com, zanerobotics.substack.com, goldmansachs.com report.pdf, deepmind.google 추정 URL, research-and-innovation.ec.europa.eu IAM4EU | USTC −37 °C, K-문샷 예산, DMREF 6,530만 달러, 회사 원문, 40CrNiMoA, GS 원보고서, DeepMind 랩 개소 |

우회 경로는 잘 작동했다. PMC 본문은 **NCBI E-utilities**(efetch JATS XML)로, 출판사가 막힌 논문의 초록은 **Europe PMC REST API**로 읽었다. A-Lab 정정 전 원고는 **OSTI**, Leeman 등의 전문과 Pei 리뷰는 **NSF PAR**, 프리프린트는 **arXiv**(abs·PDF·export API)에서 받았다. 서지 관계와 정정 연결은 **Crossref**와 OpenAlex로 확인했다. **nature.com**은 차단 없이 OA 전문과 유료 논문의 초록을 제공했다. 정부 원문은 govinfo.gov, energy.gov, whitehouse.gov, Federal Register API, CORDIS, NASA NTRS, 내각부·JST·NIMS에서, 기관 리포지토리는 Aalto와 TU Delft에서, 한국 기관·언론은 v.daum.net, news.kaist.ac.kr, 아시아경제에서 정상적으로 읽혔다.

## 후속 조사 제안

| 공백 | 왜 중요한가 | 제안 방법 |
|---|---|---|
| A-Lab 정정 첨부(주석 원고, SI 수정본)와 4개 불확정 화합물 이름, C&EN 본문 | 대표 사례의 잔여 쟁점(무질서 버전 24/36) 확인 | nature.com 정정 첨부 PDF 다운로드, C&EN 기관 구독 |
| 한국 SDL 리뷰(Digital Discovery 2026) 본문과 KIST·KAIST·KIMS 동료심사 논문 | 한국 성과가 언론 수준에 머묾 | RSC 기관 접속 또는 SNU 리포지토리(브라우저), 각 기관 논문 추적 |
| 액추에이터 소재 합성+시험 폐루프 SDL, LCE 배합·공정 BO, 이온성·HASEL 소재 ML | 로봇용 소재의 핵심 빈칸 | DEA SDL 전문, MPI-IS·ETH·Harvard·KAIST 그룹 추적, NeurIPS 2026 복원력 과제 |
| 휴머노이드 소재 kg/대(Al·Mg·강·PEEK), 감속기·롤러스크루 강종, 티어다운 | 공급망 수요 정량화 | IDTechEx 유료 본문, 티어다운(iFixit 등), CNKI 중국어 문헌 |
| 로봇 모터 자석의 ML 최적화(결정립계확산 Dy 저감), MagNex 자기 성능 | 가장 큰 공급망 리스크와 AI의 연결 | Materials Nexus 기술 자료, 특허(G16C+H01F), K-문샷 희토류 협의체 과제 |
| OEM의 ML 소재·생성설계 사용 여부(Tesla, Figure, Unitree, Hyundai, LG, Rainbow) | "AI 설계 소재 양산 사례 없음" 판단의 검증 | 특허·IR·채용공고, 공급사 발표 |
| 소프트 액추에이터 피로 수명 분포와 표준 시험 데이터 | 내구성 고려 소재 설계의 전제 | HKUST 프로토콜 기반 문헌 수집, DEA SDL 데이터 |
| 미확인 수치(NASA MAE, Karacakol 53회, 칭화대 240개, SuperTac 매개변수, Infineon 70/600) | 표에 남은 미확인 항목 정리 | Springer·Zenodo·Mouser 브라우저 접근, 저자 문의 |
| 정책 예산(한국 AI 소재 전략·K-문샷, EU €5억, Genesis 3.2억 세부, 240일 로봇 실험실 검토 보고서) | 정책 판단의 근거 | msit.go.kr 첨부 PDF, EUR-Lex 브라우저 접근, energy.gov 2025-12 보도자료 |
| 2027-01-10 이후 중국 희토류 통제 상태 | 로봇 자석 공급의 단기 변수 | MOFCOM 공고, Reuters·Benchmark 후속 |
| 스타트업 산출물 검증(Periodic, Lila 논문 동료심사, Radical 합금, DeepMind 영국 랩) | 밸류에이션과 산출물의 괴리 | arXiv·학술지 추적, 회사 공식 발표 |
| SDL 구축비·발견당 비용·독립 ROI | IFP에도 단가가 없음 | NC State SDL Futures, DOE RFI 응답, Genesis 테스트베드 결과 |
| 소재 SDL 전용 LLM 에이전트 안전 벤치마크, 에너지·연산 발자국 | 확산 단계의 거버넌스 | AI 안전 연구기관, Genesis·베이징 표준 문서 |
| 중국·일본 원어 자료(CNKI, J-STAGE), MEXT ARIM·DxMT 예산 | 영어권 편향 보정 | 원어 검색, MEXT 사이트 재시도 |
| IP 보존형 데이터 공유(연합학습, 데이터 신탁) | 데이터 병목의 제도적 해법 | CuspAI Foundry·한국 협의체 운영 규약 조사 |
