# 정책·자금·산업 주장 원문 검증 (AI + 로봇 소재공학), 2026-11-17 기준

> 방법: 이전 라운드(`로봇 분야 소재공학 AI 도입/drivers_policy.md`, `industry_market.md`)는 검색 스니펫에만 의존했다. 이번에는 네트워크가 열린 상태에서 `curl`로 원문 페이지를 직접 받아 텍스트를 추출해 읽었다. WebFetch 도구는 여전히 `ENOTFOUND`를 반환했으므로 사용하지 않았다(맨 끝 로그 참조).
> 등급: **VERIFIED** = 1차 출처(정부·기관·회사 원문)를 직접 읽음 / **PARTIALLY VERIFIED** = 신뢰할 만한 2차 원문(언론 기사 본문)을 직접 읽었거나 1차 출처가 일부만 확인됨 / **UNVERIFIED** = 원문 접근 실패, 또는 검색 요약에만 근거함.
> 판정: 이전 스니펫 기반 주장이 **맞음 / 틀림 / 뉘앙스 필요** 중 무엇인지 각 항목에 표기했다.

## 1. 미국 Genesis Mission (EO 14363), DOE 자금 공모, 2026년 7월 ">$5B / 278개 과제"

### Takeaway
EO 14363 원문을 확인했다. 원문은 "critical materials"를 우선 도메인으로 명시하고, 240일 안에 "robotic laboratories" 역량을 검토하도록 규정한다. 다만 EO 자체에는 금액이 없다. 2026년 3월 공모는 **$293M**(정확히 $293.76M, DE-FOA-0003612)이다. **$320M**은 2025년 12월에 별도로 발표된 DOE 인프라 투자로, 같은 공모가 아니다. 2026-07-22의 ">$5B 연방 약정"과 "278개 과제"는 백악관과 DOE 원문으로 모두 확인했다. 이후 2026년 10월에 1년차 포트폴리오가 297개 과제로 늘었다.

### Cited Findings
- **[VERIFIED] EO 14363 원문.** 제목은 "Executive Order 14363 of November 24, 2025, Launching the Genesis Mission"이고, 90 FR 55035–55039(2025-11-28 게재, FR Doc 2025-21665)에 실렸다. 판정: 맞음 — [govinfo.gov EO 원문](https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21665.htm); [whitehouse.gov](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/)
  - Sec. 3(a)(vi): Platform은 "experimental and production tools to enable autonomous and AI-augmented experimentation and manufacturing in high-impact domains"를 제공한다.
  - Sec. 3(e) 원문: "Within 240 days of the date of this order, the Secretary shall review capabilities across the DOE national laboratories and other participating Federal research facilities for **robotic laboratories and production facilities with the ability to engage in AI-directed experimentation and manufacturing**, including automated and AI-augmented workflows and the related technical and operational standards needed."
  - Sec. 4(a): DOE는 60일 안에 "at least 20 science and technology challenges"를 제출해야 한다. 우선 도메인은 "(i) advanced manufacturing; (ii) biotechnology; (iii) **critical materials**; (iv) nuclear fission and fusion energy; (v) quantum information science; and (vi) semiconductors and microelectronics"이다.
  - 기타 기한: 90일 컴퓨팅 자원 식별(3(c)), 120일 초기 데이터·모델 자산 식별(3(d)), 270일 초기 운영능력 시연(3(f)), 1년마다 보고(Sec. 6).
  - 금액 조항은 없다. "subject to the availability of appropriations"(Sec. 7(b))라고만 되어 있다. 따라서 EO가 신규 예산을 직접 배정하지 않는다는 이전 분석은 원문과 일치한다.
- **[VERIFIED] 백악관 팩트시트(2025-11-24).** "The Order directs the Department of Energy to create a closed-loop AI experimentation platform that integrates our Nation's world-class supercomputers and unique data assets to generate scientific foundation models and **power robotic laboratories**." 우선 분야로는 biotechnology, critical materials, nuclear fission and fusion, space exploration, QIS, semiconductors를 든다(EO 본문에는 없는 space exploration이 팩트시트에만 들어 있다) — [WH Fact Sheet](https://www.whitehouse.gov/fact-sheets/2025/11/fact-sheet-president-donald-j-trump-unveils-the-genesis-missionto-accelerate-ai-for-scientific-discovery/)
- **[VERIFIED] DOE $293M 공모.** DOE는 "$293 million Request for Application (RFA), 'The Genesis Mission: Transforming Science and Energy with AI'"를 공고했고, NOFO 번호는 DE-FOA-0003612이다. 지원 대상은 advanced manufacturing, biotechnology, **critical materials**, nuclear energy, QIS 등 "over 20 national challenges"이다.
  - Phase I: $500K–$750K, 9개월. Phase II: $6M–$15M, 3년.
  - 마감: Phase I 신청서와 Phase II 의향서는 2026-04-28, Phase II 신청서는 2026-05-19. 웨비나는 2026-03-26.
  - 출처: [energy.gov 보도자료](https://www.energy.gov/articles/energy-department-announces-293-million-funding-support-genesis-mission-national-science)
  - 법률사무소 Covington의 분석은 발행일을 **2026-03-17**, 예상 총액을 **"$293.76 million"**, 대상 영역을 **21개**(DOE가 앞서 지정한 26개 과제 중에서 선정)로 적었다 — [Inside Government Contracts (Covington)](https://www.insidegovernmentcontracts.com/2026/03/doe-announces-a-new-funding-opportunity-under-the-genesis-mission/)
  - MeriTalk에 따르면 26개 우선 과제에 "achieving AI-driven autonomous laboratories"가 들어 있다 — [MeriTalk](https://www.meritalk.com/articles/doe-announces-293m-in-ai-research-funding-under-genesis-mission/)
- **[PARTIALLY VERIFIED] $320M의 정체.** Covington 원문: "Shortly after the launch of the Mission, DOE announced **$320 million** in investments in the AI infrastructure for the Mission, including the American Science Cloud and the Transformational AI Models Consortium." 판정: **이전의 "$293M vs $320M 충돌"은 틀린 프레이밍이다.** 두 숫자는 서로 다른 발표다. $320M은 2025년 12월 인프라 투자이고, $293M은 2026년 3월 공모다. 검색 요약에 따르면 $320M은 American Science Cloud, Transformational AI Models Consortium, 로봇·자동화 실험실 과제 14개, 기초 AI 연구 37건의 4개 축으로 구성된다. 이 세부 구성은 energy.gov 원문에서 확인하지 못했다 — [Covington](https://www.insidegovernmentcontracts.com/2026/03/doe-announces-a-new-funding-opportunity-under-the-genesis-mission/); [GrantedAI 블로그](https://grantedai.com/blog/doe-genesis-mission-320-million-ai-science-foundation-models-strategy-2026)
- **[VERIFIED] 2026-07-22 백악관 ">$5B".** 제목은 "Trump Administration Announces More Than $5 Billion for the Genesis Mission, a National Mission on AI for Science"(게시 2026-07-22)이다. 판정: 맞음.
  - OSTP 국장 Michael Kratsios가 "more than $5 billion in Federal commitments"를 발표했다. 참여 기관은 "More than 15 Federal agencies"이다.
  - 신규 과제 원문: "**Achieving AI-Driven Autonomous Laboratories**: DOE, HHS, NSF, and NIST will build autonomous laboratories that leverage robotics, edge AI, and real-time analysis to enable self-driving experimentation at unprecedented scale…"
  - 또 다른 과제 원문: "**Designing Materials with Predictable Functionality**: DOE will pair … materials datasets, and physics-informed AI models in **closed-loop experimentation that couples prediction, synthesis, and characterization**…"
  - NNSA의 "Accelerating Materials Discovery, Production, and Qualification for Strategic Deterrence", DOT·DOE의 인프라 신소재 과제도 포함됐다.
  - 출처: [whitehouse.gov 2026-07-22](https://www.whitehouse.gov/releases/2026/07/45502/)
- **[VERIFIED] 278개 과제(2026-07-22, DOE).** 과제 주도 기관 분포는 "278 awards: 87 led by DOE and NNSA National Laboratories, 168 led by universities, 19 led by companies, and 4 led by nonprofit organizations"이다. 참여 기관 분포는 "342 participating institutions: 16 DOE and NNSA National Laboratories, 142 universities, 157 companies, 13 nonprofit organizations, and 14 other institutions"이다. 최대 과제는 원자력 분야 3년 $60M이다. RFA 응모는 "the largest response to a funding opportunity in DOE history"였다.
  - 판정: 맞음, 단 뉘앙스가 필요하다. 이전 노트의 "16 labs / 142 universities / 157 companies / 13 nonprofits"는 **과제 수가 아니라 참여 기관 수**다. 과제를 주도한 기업은 19곳에 그친다.
  - 출처: [energy.gov](https://www.energy.gov/articles/secretary-energy-chris-wright-announces-first-genesis-mission-projects-selected-accelerate)
- **[VERIFIED, 신규] 2026-10-08 업데이트.** DOE는 Phase II 12건($159M)과 Phase I 6건을 추가해 "first-year cohort of **297 projects**"가 됐다고 밝혔다.
  - 소재 관련 Phase II: UIUC의 AXIS(희토류 추출용 redox-active ligand 설계), ORNL의 양자자석 역설계.
  - 같은 날 DOE 팩트시트 원문: "Investing **$30 million over three years in four National Laboratory-led robotics and autonomous-science testbeds**… integrate embodied SI, robotics, laboratory automation, digital twins…"
  - 출처: [energy.gov Phase II](https://www.energy.gov/articles/energy-department-announces-new-genesis-mission-awards-advance-super-intelligence-science); [DOE Fact Sheet 2026-10-08](https://www.energy.gov/articles/fact-sheet-energy-department-ushering-golden-age-american-science)
- **[VERIFIED, 신규] 백악관 2026-10-08 팩트시트.**
  - 산업계가 Genesis Mission Consortium에 "$2.4B in SI for science tools and compute credits"를 약정했다. NVIDIA $1B, AMD $500M, OpenAI $200M, Anthropic·Google 각 $150M 등이다.
  - "NSF and DOE announced an investment of **over $100 million in SI-enabled scientific instrumentation and autonomous laboratories**… This follows NSF's July announcement of a **$400 million investment in programmable cloud labs**."
  - 전체 패키지는 "over $6 billion in investments"이다.
  - 출처: [WH Fact Sheet 2026-10](https://www.whitehouse.gov/fact-sheets/2026/10/fact-sheet-trump-administration-announces-the-most-ambitious-set-of-science-initiatives-this-century/)
- **[VERIFIED] "과학 생산성 2배" 목표.** 1차 출처 문구는 세 가지다. DOE "Designed to double America's scientific productivity", DOE 팩트시트 "the Genesis Mission's goal of doubling the scientific productivity and impact", 백악관 "aiming to double America's R&D output". 판정: 이전 노트가 2차 출처(GrantedAI)에만 기댔던 주장이 1차 출처로 확인됐다 — [energy.gov](https://www.energy.gov/articles/secretary-energy-chris-wright-announces-first-genesis-mission-projects-selected-accelerate); [whitehouse.gov](https://www.whitehouse.gov/releases/2026/07/45502/)
- **[VERIFIED] DOE 과제 페이지의 소재·자율실험 사례.**
  - PNNL: SciLink 다중 에이전트 플랫폼으로 핵심소재 선택적 침전 공정을 closed-loop로 최적화한다.
  - LLNL: BIND(희토류 선택 단백질 설계).
  - Sandia/CASUS: MALA(ML 기반 DFT 대체).
  - LANL: URSA 에이전트.
  - 출처: [energy.gov National S&T Challenges](https://www.energy.gov/undersecretaryforscience/genesis-mission/genesis-mission-national-science-and-technology-challenges)

### Inferences
- Genesis Mission에서 "로봇 실험실"은 EO(2025-11), 7월 과제("Achieving AI-Driven Autonomous Laboratories"), 10월 예산($30M 로봇 테스트베드, NSF·DOE $100M+, NSF $400M 클라우드 랩)으로 이어지며 점점 구체적인 예산 항목이 됐다. 다만 ">$5B"는 15개 이상 기관이 기존 예산을 합산한 "commitments"이고, 순증 예산이라는 증거는 없다.
- 소재 관련 내용은 핵심소재·희토류(공급망)와 "Designing Materials with Predictable Functionality"(closed-loop 합성·특성평가)의 두 축이다.

### Gaps
- energy.gov의 $320M(2025-12) 원 보도자료는 직접 열지 못했다. 그래서 로봇 실험실 14건과 AI 연구 37건이라는 세부 구성은 미확인이다.
- ">$5B"의 기관별 내역은 백악관 원문에 없다.
- 240일 로봇 실험실 역량 검토(기한 약 2026-07-22)의 결과 보고서는 공개된 것을 찾지 못했다.

## 2. MGI 2011 백서 목표, 2021 전략계획, NSF DMREF 금액

### Takeaway
MGI 백서의 "twice as fast … at a fraction of the cost" 문구와 2021 전략계획의 3대 목표를 원문으로 확인했다. NSF DMREF 2023년 $72.5M/37건도 NSF 원문으로 확인했다. 2021년 $65.3M은 NSF URL이 404여서 원문을 확인하지 못했다.

### Cited Findings
- **[VERIFIED]** MGI 백서(2011-06) 원문: "This initiative offers a unique opportunity for the United States to discover, develop, manufacture, and deploy advanced materials **at least twice as fast as possible today, at a fraction of the cost**." 판정: 맞음 — [mgi.gov 백서 PDF](https://www.mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf)
- **[VERIFIED]** MGI 2021 전략계획(2021년 11월): "Goal 1. Unify the Materials Innovation Infrastructure / Goal 2. Harness the Power of Materials Data / Goal 3. Educate, Train, and Connect the Materials R&D Workforce."
  - Goal 1 목표 중 하나: "Leverage advances and bolster development of modular, **autonomous**, integrated, high-throughput experimental tools—from lab to manufacturing."
  - Goal 2는 "advent of 'autonomous' materials research … AI-driven robotic systems"를 서술하고, ARES OS™ 자율연구로봇 사례를 소개한다.
  - 판정: 맞음. 다만 자율실험은 Goal 1과 Goal 2 양쪽에 걸쳐 있다.
  - 출처: [mgi.gov 2021 Strategic Plan PDF](https://www.mgi.gov/sites/mgi/files/MGI-2021-Strategic-Plan.pdf)
- **[VERIFIED]** NSF 2023 DMREF 발표 원문: "A $72.5 million investment … will fund 37 new four-year projects"; "161 researchers at 61 universities across 30 states"; "Since 2012, DMREF has been NSF's primary response to the federal Materials Genome Initiative." 판정: 맞음 — [NSF](https://www.nsf.gov/news/nsf-invests-72m-design-revolutionary-materials)
- **[UNVERIFIED]** 2021년 $65.3M/37건은 NSF 페이지가 HTTP 404를 반환해 원문을 확인하지 못했다(이전 스니펫 수치 유지). 2012년 $12M(Nanowerk)은 이번에 재확인을 시도하지 않았다.

### Gaps
- DMREF 누적 총액, 2025–26년 DMREF 공모 금액은 미확인이다(NSF 공모 페이지에는 금액이 노출되지 않았다).

## 3. 한국: AI 소재 R&D 플랫폼 전략(2026-04-30), K-문샷(2026-02-25), 자율실험실 협의체(2026-08-11)

### Takeaway
AI 소재 전략의 정량 목표는 언론 본문으로 확인했다. 핵심 목표는 AI-Ready 데이터셋 1,000만 건(5년)과 5,000만 건(10년), 4대 자율실험센터, 석사 300명·박사 75명이다. 그러나 **예산 금액은 어느 원문에도 없다.** K-문샷의 소재 미션은 희토류 대체·저감·재활용 영구자석으로 확인됐고, 총예산은 미확인이다. 자율실험실 협의체는 2026-08-11 실제로 출범했다. **"80여 개 기관"과 "약 50개 기업"은 서로 모순되지 않는다.** 수요기업 50개사에 대학·연구기관 30여 곳(그리고 공급기업)을 더한 수치다.

### Cited Findings
- **[PARTIALLY VERIFIED: 언론 본문 2건 직접 확인, msit.go.kr 원 보도자료는 미확인] AI 소재 R&D 플랫폼 구축 전략(2026~2030)(안).** 2026-04-30 제8회 과학기술관계장관회의에서 발표됐다. 출처: [동아사이언스(다음)](https://v.daum.net/v/20260430101533808); [디지털타임스(다음)](https://v.daum.net/v/20260430155346042)
  - 4대 전략: "AI 모델 독자 개발·자율실험센터 구축·국가 데이터 통합 플랫폼 운영·융합형 인재 양성".
  - 모델: 6대 물성(기계·자기·전기·화학·열·광학)을 예측하는 '물성 AI 모델', 물성 간 상관관계를 다루는 '다중 물성 AI 모델', '소재AI 특화모델', 그리고 이를 하나로 묶는 'AI 소재 연구동료'.
  - 자율실험센터: "소재 합성부터 시작품 제조까지 24시간 자동화로 실험·검증하는" 4곳이다.
    - 이차전지: 양극재·액체전해질·고체전해질.
    - 수소·에너지: 전기화학·열촉매·광촉매.
    - 우주항공·모빌리티: 알루미늄·니켈합금·티타늄·마그네슘 등 금속·복합재·세라믹.
    - 유기반도체·디스플레이.
    - 센터들은 클라우드 기반 '자율실험센터 네트워크'로 연결된다.
  - 데이터: '국가소재연구데이터통합센터(가칭)'를 2026년 하반기에 지정한다. 기존 '소재연구데이터생태계플랫폼'은 '국가소재연구데이터통합플랫폼(가칭)'으로 개편한다. "AI-Ready 데이터셋으로 5년 이내 1000만 건, 10년 이내 5000만 건".
  - 인재: "석사 300명, 박사 75명 이상".
  - 판정: 이전 노트의 수치는 모두 맞음.
  - **예산: 두 기사 본문 모두 금액이 없다.** 검색으로도 찾지 못했다. MOTIE '첨단소재 특화형 AX플랫폼'(145.5억 원)은 별도 부처의 별도 사업이므로 이 전략의 예산으로 쓰면 안 된다.
- **[PARTIALLY VERIFIED] K-문샷 추진전략(2026-02-25).**
  - 국가AI전략위원회 제2차 전체회의에서 심의·의결됐다. 2대 전략은 '국가과학AI연구센터(가칭)' 중심의 데이터·GPU·AI모델·**자율실험실** 통합, 그리고 "피지컬AI, 우주, 반도체, 양자 등 8대 분야 12대 국가적 미션"이다. 미션별 PD 책임운영체계를 두고 "2035년까지 가시적 성과"를 내는 것이 목표다. 헤드라인은 "美 제니시스 미션 맞선 'K-문샷'"이다 — [뉴시스 2026-02-25](https://www.newsis.com/view/NISX20260225_0003525436)
  - 2026-04 아시아경제(영문)에 따르면 "double research productivity by 2030"과 "solve 12 major national scientific challenges by 2035"가 목표다 — [Asia Business Daily](https://www.asiae.co.kr/en/article/2026041711312776843)
  - 로드맵(2026-09-30 제13회 과학기술관계장관회의)의 12개 분야는 신약·BCI·태양전지·핵융합·SMR선박·피지컬AI·휴머노이드·우주데이터센터·**소재**·반도체·양자·AI과학자다. AI과학자 미션은 PD가 공석이어서 11개 분야 로드맵만 의결됐다. "소재 분야에서는 희토류를 대체하거나 수입량을 줄이기 위해 영구자석 원천기술을 확보할 계획". 1차 목표 기한은 2029년이다 — [머니투데이 2026-09-30](https://www.mt.co.kr/tech/2026/09/30/2026093015522912240)
  - 소재 미션 세부(KDI 경제정보센터의 과기정통부 자료 재게시): 2026-10-01 'K-문샷 희토류 산학연 협의체'가 출범했다. 2027년부터 "중희토류 완전 배제 및 경희토류 극저감" 영구자석 제조공정과 폐영구자석 회수기술을 개발한다. 1단계는 2027~2029년(원천기술), 2단계는 2030~2033년(고도화·실증)이다 — [KDI 경제정보센터](https://eiec.kdi.re.kr/policy/materialView.do?num=287736)
  - **예산: 미확인.** 2027년 정부 R&D 예산안 39.5조 원(+11.2%)은 검색 요약에서만 봤으며 K-문샷 전용 금액이 아니다.
  - smartcity.go.kr의 K-문샷 안건 PDF는 HTTP 404였다(삭제됐거나 경로가 바뀐 것으로 보인다).
- **[PARTIALLY VERIFIED: 언론 본문 2건] 자율실험실 산·학·연 협의체 출범.**
  - "On August 11, the Ministry of Science and ICT and the Korea Basic Science Institute (KBSI) held an inauguration ceremony … at El Tower in Seoul"; "the first time in Korea that a national-level consultative body for autonomous laboratories … has been officially organized" — [Asia Business Daily 영문](https://view.asiae.co.kr/en/article/2026081015043638880)
  - 구성: 위원장은 정유성(서울대), 간사는 국가과학AI연구센터와 KBSI 공동이다. 국문 기사 원문은 "파크시스템스, 에이치비솔루션 등 공급기업과 삼성종합기술원, SK하이닉스 등 수요기업 50개사, 대학·연구기관 30여개가 참여"이고, 출범식 참석자는 "400여명"이다. 영문 기사 부제는 "Over 80 Organizations Including Samsung Advanced Institute of Technology and SK hynix" — [아시아경제 국문 2026-08-11](https://view.asiae.co.kr/article/2026081109490769317)
  - 판정: 출범은 맞음. 인원 수는 뉘앙스가 필요하다. "80여 개 기관"은 수요기업 50개사와 대학·연구기관 30여 곳을 더한 수치다. 공급기업이 50개사에 포함되는지는 국문 원문 문장만으로는 모호하다.
  - 임무: 기술·플랫폼·표준 정립, 레퍼런스 자율실험실 구축, 수요기업 실증·민간 확산. K-문샷의 "핵심 기반"으로 규정됐다.
  - 주의: 국문 기사는 사전 보도 시제("개최한다")이고, 영문 기사는 완료 시제("held")다. 과기정통부·KBSI 보도자료 원문은 열지 못했다.

### Gaps
- msit.go.kr 보도자료 목록은 접근됐다(HTTP 200). 그러나 해당 보도자료 본문과 첨부 PDF는 찾지 못해 예산 정보 유무를 1차로 확인하지 못했다.
- K-문샷 총예산, AI 소재 전략 예산, 자율실험센터별 예산은 모두 미확인이다.

## 4. EU: BIG-MAP 예산, Advanced Materials 전략 2024(€500M 파트너십)

### Takeaway
CORDIS 원문 기준 BIG-MAP의 총비용과 EU 기여금은 모두 **€19,997,812.50(약 €20M)**이다. 이전의 "€16M"은 틀렸고, CIDETEC의 €20M이 맞다. COM(2024)98 발표일(2024-02-27)과 Technology Council은 확인했다. 그러나 "€500M 파트너십" 수치는 EU 원문에서 확인하지 못했다.

### Cited Findings
- **[VERIFIED]** CORDIS BIG-MAP 원문(CORDIS에서 직접 확인).
  - Grant agreement ID 957189, Start date 2020-09-01, End date 2024-02-29.
  - Funded under "EXCELLENT SCIENCE - Future and Emerging Technologies (FET)".
  - Total cost €19,997,812.50, EU contribution €19,997,812.50.
  - Coordinated by Danmarks Tekniske Universitet(덴마크).
  - 설명문은 "34 partners from 15 countries"라고 하지만, CORDIS 참여자 목록에는 "Participants (38)"로 나온다.
  - 판정: **€16M은 틀림, €20M이 맞음.**
  - 출처: [CORDIS 957189](https://cordis.europa.eu/project/id/957189)
- **[VERIFIED]** EC R&I 페이지: "The European Commission published the Communication 'Advanced Materials for Industrial Leadership' on 27 February 2024." Technology Council은 Commission Decision C(2024)4749로 설치됐고 2차 회의는 2025-06-25였다. 같은 페이지 본문에 €500M 수치는 없었다 — [EC R&I](https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/chemicals-and-advanced-materials/advanced-materials-industrial-leadership_en)
- **[UNVERIFIED]** "€500M(2025–2027), 민간 ≥€250M" 파트너십 수치는 EUR-Lex COM(2024)98 원문이 HTTP 202(봇 챌린지)로 빈 응답을 반환해 확인하지 못했다. IAM4EU 페이지로 추정한 URL은 404였다. 이전 스니펫(EU Monitor) 수치를 그대로 두되 미검증으로 표시한다.

## 5. 중국: 희토류 수출통제 유예(만료 2026-11-10) 이후 상태, 베이징 AI 과학연구 방안(2026–2028)

### Takeaway
2026-11-09 상무부(MOFCOM)가 유예를 **2개월 연장해 2027-01-10까지** 연장했다(Reuters 기사 전재본과 Benchmark Minerals 본문으로 확인). 2025년 4월에 도입된 7종 중희토류 통제는 계속 유효하다(검색 요약 근거). 베이징 방안의 5대 차원과 18개 과제는 베이징시 영문 원문으로 확인했다.

### Cited Findings
- **[PARTIALLY VERIFIED: Reuters 전재 기사와 업계 매체 본문]** "The Ministry of Commerce said in a short statement on Nov 9 that the suspension would be extended for two months until Jan 10, 2027. It gave no other details." 이 연장은 미·중 무역협상 중 발표된 "broader suspension of trade countermeasures and tariffs"의 일부다. 이 기사는 트럼프가 11월 하순 선전(深圳) APEC에서 시진핑과 만날 예정이라고 전한다 — [The Star (Reuters 전재) 2026-11-09](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/11/09/china-extends-suspension-of-rare-earth-export-controls-until-january)
- **[PARTIALLY VERIFIED]** Benchmark 원문: "China has extended its suspension of the export controls on rare earths, lithium ion batteries and graphite anode materials it announced in October 2025. The extension runs only until 10 January 2027… MOFCOM published the notice on 9 November, a day before the original suspension was due to expire." — [Benchmark Source](https://source.benchmarkminerals.com/article/china-extends-pause-on-rare-earth-and-battery-export-controls-until-2027)
- **[UNVERIFIED: 검색 요약만]** 유예 대상은 2025년 10월 확대분(홀뮴·에르븀·툴륨·유로퓸·이터븀, 가공기술·장비, 역외 적용 규정)이다. 2025년 4월 7종(Sm, Gd, Tb, Dy, Lu, Sc, Y) 통제는 계속 유효하다. S&P Global 원문은 HTTP 403이었다.
- **[미확인] MOFCOM 1차 공고.** mofcom.gov.cn의 2026년 공고 목록(제20~57호)은 접근됐다(HTTP 200). 그러나 첫 페이지에서 11-09 연장 공고를 찾지 못했다(별도 발표 형식이었을 수 있다). english.mofcom.gov.cn은 DNS 해석에 실패했다.
- **[VERIFIED] 베이징 방안 해설(2026-07).** 출처: [Beijing gov 영문 해설](https://english.beijing.gov.cn/investinginbeijing/InvestmentSpecial/DigitalEconomy/PolicesAndInterpretations/202607/t20260715_4763931.html)
  - 원문: "The Plan focuses on five key dimensions: **autonomous laboratory systems**, high-value scenario applications, scientific model systems, scientific data infrastructure, and innovation ecosystems. It sets out **18 specific tasks**."
  - 원문: "a new dry lab—wet lab closed-loop research model"
  - 6대 중점 분야: "high energy physics, **materials science**, healthcare, life sciences, quantum technology, and bio-breeding"
  - 자율실험실을 "core platforms"로 규정하고 표준·등급별 평가·다원화된 자금 정책을 마련한다.
  - 판정: 맞음. 다만 금액이나 수치 목표는 해설에 없다.

## 6. 일본: MI2I 이후 프로그램(NIMS DICE, ARIM, Moonshot 목표 3)

### Takeaway
NIMS DICE는 MEXT '마테리얼 DX 플랫폼 구상'의 데이터 중핵거점(MDPF)이 운영한다. ARIM(데이터 생성)과 DxMT(데이터 활용 연구)가 함께 이 구상을 이룬다(NIMS 원문). 2025-12-23에는 ML 분석환경 'pinax'를 무상으로 공개했다. Moonshot 목표 3에는 "2050년 자연과학에서 스스로 생각하고 행동하는 AI 로봇 시스템" 하위목표가 여전히 있다. 다만 2025-12 이후 신임 PD 체제의 JST 페이지는 휴머노이드와 범용 로봇 중심으로 재편됐다.

### Cited Findings
- **[VERIFIED]** DICE 원문: "'DICE' is a digital innovative collaborative ecosystem for materials research provided by the NIMS Materials Data Platform (MDPF)"; "under the Ministry of Education, Culture, Sports, Science and Technology's 'Materials DX Platform Initiative'"; "MDPF collaborates with the Advanced Research Infrastructure for Materials and Nanotechnology (**ARIM**) and the Data creation and utilization-type MaTerial R&D project (**DxMT**)" — [dice.nims.go.jp](https://dice.nims.go.jp/en/about.html)
- **[VERIFIED]** NIMS 보도자료(2025-12-23): MDPF의 신규 서비스로 "pinax"를 12월 23일부터 국내 대학·기업 연구자에게 무상 제공한다. 기존 서비스는 MatNavi, RDE(데이터 축적·공용), MDR(논문·데이터 리포지토리), MInt(통합형 재료개발 시스템)다 — [NIMS 보도자료 PDF](https://www.nims.go.jp/press/2025/12/a5kbo700000092mp-att/202512230.pdf)
- **[VERIFIED]** 내각부 Moonshot 목표 3 원문: "Development of an automated AI robot system that aims to discover impactful scientific principles and solutions, by thinking and acting in the field of natural science, by 2050"; 2030 이정표는 "…support the process of discovery for scientific principles and solutions to specific problems by 2030." PD는 KUNIYOSHI Yasuo(도쿄대) — [Cabinet Office](https://www8.cao.go.jp/cstp/english/moonshot/sub3_en.html)
- **[VERIFIED]** JST 목표 3 페이지: 신규 비전은 "general-purpose autonomous humanoid AI robots"이고, 과제 목록에 e-skin, 전신 촉각(EIT) 등 로봇 소재·센서 과제가 들어 있다. "AI-robots that conduct scientific experiments in challenging environments … By 2050 AI-robots will discover their own…"(Harada 과제) 서술도 남아 있다 — [JST Moonshot Goal 3](https://www.jst.go.jp/moonshot/en/program/goal3/)
- **[UNVERIFIED]** ARIM(nanonet.mext.go.jp)과 DxMT(dxmt.mext.go.jp) 사이트는 프록시에서 CONNECT 502로 접근에 실패했다. 예산과 참여기관 수는 확인하지 못했다.

## 7. 스타트업·빅테크 주장

### Takeaway
회사 원문으로 확인한 항목은 Periodic $300M 시드, Lila $350M 시리즈 A(누적 $550M)와 "2,942 catalysts", CuspAI $450M 시리즈 B(기업가치 $2.6B), Path $300M 시리즈 E(기업가치 $2.45B), LG EXAONE Discovery(42만 후보, 1일 vs 22개월), Microsoft/PNNL(32M→23, 그중 18개 신규)이다. Periodic $7.5B와 Lila 시리즈 B는 **보도만 있고 회사 확인이 없다.** DeepMind 영국 자동화 소재 랩의 **개관 확인 자료는 찾지 못했다.** Radical AI의 2026년 신규 투자는 없다.

### Cited Findings
- **Periodic Labs**
  - **[VERIFIED: 회사 사이트]** "we are building AI scientists and the autonomous laboratories for them to operate"; 목표 중 하나는 "discover superconductors that work at higher temperatures". 투자자 서술: "backed by … including **a16z**, as well as **Felicis**, DST, NVentures, Accel and individuals including Jeff Bezos, Elad Gil, Eric Schmidt, and Jeff Dean." 회사 사이트에는 금액이 없다 — [periodic.com](https://periodic.com/)
  - **[PARTIALLY VERIFIED: 언론 본문]** SiliconANGLE(2025-10-01): "$300 million … Andreessen Horowitz led the seed"; Bloomberg 인용 "pre-money valuation of $1 billion"; 자율 분말합성 랩. 판정: 리드 투자자 혼선은 a16z가 리드이고 Felicis는 참여사라는 것으로 정리된다 — [SiliconANGLE](https://siliconangle.com/2025/10/01/periodic-labs-raises-300m-accelerate-scientific-research-ai/)
  - **[UNVERIFIED]** 2026년 ~$7B(2026-03 Bloomberg 보도), $7.5B·≥$500M(AMP 리드 보도): 회사 발표가 없다. Forge Global에는 2026-06 $7.5B로 올라 있으나 Contrary는 미확정으로 본다(검색 요약). Dealroom 원문은 HTTP 429로 막혔다.
  - 2026년 연구 성과(초전도체 등)를 발표한 회사 원문은 찾지 못했다(periodic.com/blog는 404).
- **Lila Sciences**
  - **[VERIFIED: 회사 뉴스 페이지]** "Lila Sciences closed a $350M Series A, bringing total funding to $550M, to scale its AI Science Factories"; 시리즈 A 최초 $235M; Reuters 단독 "tops $1.3 billion valuation with new Nvidia backing"(2025-10-14) 링크 — [lila.ai/news](https://www.lila.ai/news)
  - **[VERIFIED: 회사 주장]** "Lila's AI-directed lab screened **2,942 catalysts** for green hydrogen in three months, identifying 6 palladium-based families"; 선두 촉매는 1,000시간 이상 산성 시험에서 루테늄과 동등했다; "screened catalysts 17 times faster than a standard lab, cutting human hands-on time per sample over 90%". 판정: 맞음. 단 회사 자체 주장이며, 관련 논문 제목은 "AI-guided high-throughput discovery of iridium- and ruthenium-free palladium-oxide catalysts for durable acidic oxygen evolution"로 "human-supervised closed-loop"로 표현된다 — [Lila 기사](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem)
  - **[VERIFIED, 신규]** Lila는 Genesis Mission Lighthouse Challenge에서 Phase I 3건에 선정됐다. 파트너는 Caltech·LBNL, Northwestern·Argonne, NLR(National Laboratory of the Rockies)이다 — [Lila](https://www.lila.ai/news/powering-american-science-lila-to-join-does-genesis-mission)
  - **[PARTIALLY VERIFIED: Bloomberg Law 본문 직접 확인, 회사 미확인]** 2026-06-03: "in talks to raise about **$2 billion** at an expected valuation of about **$8.5 billion before the new money**"; "anchored by … CalPERS and Nvidia Corp.'s NVentures"; Lila와 CalPERS는 논평을 거부했다. 판정: 이전의 "$2.0B 시리즈 B, $10.5B"는 뉘앙스가 필요하다. 이는 협상 보도이고, $10.5B는 투자 후 기업가치를 추정한 값이다 — [Bloomberg Law](https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation)
  - **[UNVERIFIED]** "AISF(AI Science Factory) 개관": Lila 뉴스 페이지에 시설 개관 공지가 없다.
- **CuspAI**
  - **[PARTIALLY VERIFIED: 언론 본문]** SiliconANGLE(2026-07-20): "$450 million … Series B round values it at **$2.6 billion**. The deal was led by **Kleiner Perkins and NEA** with a 'significant contribution' from Bezos Expeditions"; AI Materials Foundry "more than 45 members, including Nvidia, Samsung, Meta"; MIRA 플랫폼. 판정: 금액·가치·날짜는 맞음. 리드 투자자는 이전 노트의 "Bezos·Kleiner 공동리드"가 아니라 **Kleiner Perkins와 NEA**다 — [SiliconANGLE](https://siliconangle.com/2026/07/20/ai-materials-science-startup-cuspai-raises-450m-funding/)
  - cusp.ai/news는 404였다(회사 원문 미확인).
- **Google DeepMind 영국 자동화 소재 랩**
  - **[UNVERIFIED: 개관]** 2025-12 발표(2026년 개관 예정, Gemini 통합, 초전도체·반도체·배터리 소재 대상)만 확인된다. 2026-11 현재 개관 보도는 검색으로도 찾지 못했다. deepmind.google 블로그 첫 페이지에 관련 글이 없었고, 추정 URL은 404였다.
- **Radical AI**
  - **[PARTIALLY VERIFIED]** BK Reader(2026-02-01): Hochul 주지사가 브루클린 네이비야드의 "New York's first fully autonomous materials science lab" 개관을 기념했다. "around 100 AI-driven experiments daily" 규모로 설계됐고, $4M 프로젝트에 ESD 세액공제 최대 $2M이 붙으며 일자리 115개가 예상된다. "$55 million in seed funding led by RTX Ventures"; "a Department of Energy partner in the White House Genesis Mission"; AFWERX 고엔트로피 합금 계약 — [BK Reader](https://www.bkreader.com/business-innovation/radical-ai-opens-nys-first-autonomous-materials-lab-11801540)
  - **[VERIFIED: 회사 주장]** 회사 뉴스 페이지: "in six months, Radical's closed-loop AI powered lab has produced **1,200 alloys** — nearly 10x the pace of the best prior DARPA program"; TIME 2026 Best Inventions 선정 — [radical-ai.com/news](https://www.radical-ai.com/news)
  - 2026년 신규 투자 라운드는 찾지 못했다(검색 요약 기준).
- **Path Robotics**
  - **[PARTIALLY VERIFIED: 언론 본문 2건]** "$300 million in Series E financing at a post-money valuation of **$2.45 billion**, led by … Georgian" — [Robotics 24/7](https://www.robotics247.com/article/path-robotics-announces-300m-series-e-financing-at-2.45b-valuation)
  - 2026-08 HII와 "$600 million performance-based production agreement"(해군 조선)를 맺었다. 같은 기사에 직원 97% 증가 언급이 있다.
  - 기존 투자자 Addition, Drive, IronArc, Tiger Global, Yamaha Motor Ventures가 참여했고, 신규로 D. E. Shaw Ventures와 **Naver Ventures**가 들어왔다. 누적 투자액은 "more than $610m"이며, 2026-11-10 전후 보도다 — [The Next Web](https://thenextweb.com/news/path-robotics-300m-series-e-2-45bn-valuation)
  - 판정: 맞음. Automate.org의 $2.25B는 틀린 것으로 보인다.
- **LG AI Research EXAONE Discovery**
  - **[PARTIALLY VERIFIED: 언론 본문 2건]** 2026-09-14 AI Talk Concert 2026 발표: "EXAONE Discovery screened 420,000 candidate substances for LG Household & Health Care and found ramsidil in one day … usual discovery process … can take 22 months." 자율실험실 계획: "a foundation model for materials development will predict the outcomes of new material synthesis, while robotic equipment conducts experiments" — [Korea Times](https://www.koreatimes.co.kr/business/companies/20260914/lg-ai-research-seeks-to-address-industrial-challenges-with-expert-ai-models)
  - Korea Herald는 성분명을 "Rhamsydil"로 표기하고 탈모 치료 후보 성분이라고 설명한다 — [Korea Herald](https://www.koreaherald.com/article/10872720)
- **Microsoft/PNNL 전해질**
  - **[VERIFIED: Microsoft 원문]** 같은 기사 안에 두 수치가 함께 나온다. 도입부는 "winnow 32 million potential inorganic materials to **18 promising candidates** … in just 80 hours"이다. 본문 깔때기는 32M → ~500,000 → 800 → 150 → "**23 – five of which were already known**"이다.
  - 판정: **18과 23은 모순이 아니다.** 23개 중 이미 알려진 5개를 빼면 신규 후보가 18개다 — [Microsoft Source](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)

## 8. SDL 비용: IFP "Scaling Materials Discovery with Self-Driving Labs"

### Takeaway
IFP 보고서(Charles Yang, Launch Sequence 시리즈)에는 SDL 1개당 구축비 같은 단가 수치가 **없다.** 들어 있는 금액은 정책 금액이다. 캐나다 공공·민간 투자 $500M 이상, DOE에 제안하는 $80M 프로그램, ARPA-E $40M, CHIPS R&D $100M이다.

### Cited Findings
- **[VERIFIED]** 원문: "Canada has invested over **$500 million** of public and private funding into self-driving labs." — [IFP PDF](https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf)
- **[VERIFIED]** 원문: "DOE has not to date provided any specific programmatic funding for national labs to scale this key infrastructure. Allocating an **$80 million program** for self-driving labs would represent a step change."
- **[VERIFIED]** 원문: "DOE's ARPA-E created a **$40 million** program for self-driving labs to discover new chemical catalysts and CHIPS R&D created a **$100 million** program for self-driving labs to accelerate the discovery of semiconductor material."
- **[VERIFIED]** 그 밖의 원문: "taking on average 20 years from lab to deployment"; "self-driving labs can execute hundreds of experiments per day". 정책 제안은 OSTP가 MGI를 통해 국가 SDL 컨소시엄과 "Grand Challenges in Autonomous Scientific Discovery" 로드맵을 만들고, 초당적 DOE AI Act를 통과시키는 것이다.
- 판정: 이전 노트의 "IFP cost figures"는 **뉘앙스가 필요하다.** 단가가 아니라 프로그램 규모 금액이다. 보고서는 2025년(Genesis Mission 이전)에 작성됐고, 그 뒤 DOE가 $30M 로봇 테스트베드 등을 실제로 배정했다(1절 참조).

## 9. USPTO AI 보조 발명 가이던스 "철회"(2025-11-28)

### Takeaway
철회는 맞지만, 정확히는 **"rescind and replace"(폐지 후 대체)**다. 2025-11-28 Federal Register에 "Revised Inventorship Guidance for AI-Assisted Inventions"(90 FR 54636)가 게재되면서 2024-02-13 가이던스는 전면 폐지됐다. 단일 인간 발명자 사안에서 Pannu 요소를 적용하던 접근이 철회됐고, AI를 "도구"로 보는 전통적 착상(conception) 기준으로 일원화됐다.

### Cited Findings
- **[VERIFIED]** 원문: "The guidance issued on February 13, 2024, titled 'Inventorship Guidance for AI-Assisted Inventions' is **rescinded in its entirety**. The approach set forth in that guidance, which relied on the application of the Pannu factors to AI-assisted inventions, is withdrawn." — [govinfo.gov FR Doc 2025-21457](https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21457.htm); [FederalRegister API 메타데이터](https://www.federalregister.gov/api/v1/documents/2025-21457.json)
- **[VERIFIED]** 원문: "The same legal standard for determining inventorship applies to all inventions, regardless of whether AI systems were used … There is no separate or modified standard for AI-assisted inventions."
- **[VERIFIED]** 원문: "AI systems, including generative AI and other computational models, are instruments used by human inventors. They are analogous to laboratory equipment, computer software, research databases…"
- **[VERIFIED]** AI를 발명자로 기재한 출원은 35 U.S.C. 101과 115에 따라 거절된다. 여러 사람이 관여한 경우에는 Pannu 요소가 계속 적용된다. Docket은 PTO-P-2025-0014다.
- 판정: 날짜(2025-11-28)는 맞음. 내용은 "철회 후 개정 가이던스로 대체"로 서술해야 정확하다.

## 10. 시장 규모: IDTechEx, MarketsandMarkets

### Cited Findings
- **[VERIFIED: 리포트 랜딩 페이지]** IDTechEx "Materials Informatics 2025-2035: Markets, Strategies, Players": "The global market for external provision of materials informatics will reach **US$725 million by 2034**, representing **9.0% CAGR vs. 2025**." 판정: 맞음 — [IDTechEx](https://www.idtechex.com/en/research-report/materials-informatics-2025/1096)
- **[UNVERIFIED]** MarketsandMarkets 소재정보학 시장 수치(2023년 $129M → 2028년 $276M, CAGR 16.3%)와 실험실 자동화 수치는 리포트 페이지와 보도자료 페이지가 모두 HTTP 403(봇 차단)이어서 확인하지 못했다.

### Inferences
- 시장 추정의 범위(외부 MI 서비스 시장 수억 달러)와 개별 스타트업 기업가치(CuspAI $2.6B 확인, Lila·Periodic은 보도상 $8.5B~$10.5B와 $7.5B)의 괴리는 여전히 유효한 관찰이다. 다만 Lila·Periodic 수치는 미확정임을 명시해야 한다.

## 이전 스니펫 기반 주장 판정 요약

| 주장 | 판정 | 근거 등급 |
|---|---|---|
| EO 14363: critical materials, 240일 로봇 실험실 검토 | 맞음 | VERIFIED |
| DOE 공모 $293M vs $320M "충돌" | 틀린 프레이밍. $293M(2026-03-17 RFA)과 $320M(2025-12 인프라)은 별개 | VERIFIED / PARTIAL |
| 2026-07 >$5B, 278개 과제 | 맞음. 16/142/157/13은 참여 기관 수. 2026-10에 297개로 증가 | VERIFIED |
| Genesis "생산성 2배" | 맞음(1차 출처로 확인) | VERIFIED |
| MGI 2011 "twice as fast" | 맞음 | VERIFIED |
| MGI 2021 3대 목표 | 맞음 | VERIFIED |
| NSF DMREF 2023 $72.5M/37 | 맞음 | VERIFIED |
| NSF DMREF 2021 $65.3M | 미확인(404) | UNVERIFIED |
| 한국 AI 소재 전략: 1,000만/5,000만 건, 4센터, 석사 300·박사 75 | 맞음 | PARTIAL(언론 본문) |
| 한국 AI 소재 전략 예산 | 원문에 없음 | 미확인 |
| K-문샷 12대 미션, 소재 = 영구자석 | 맞음 | PARTIAL |
| K-문샷 예산 | 미확인 | 미확인 |
| 자율실험실 협의체 출범(2026-08-11), 80여 기관 vs 50개사 | 맞음. 50개 수요기업과 30여 대학·연구기관을 합쳐 80여 기관 | PARTIAL |
| BIG-MAP €16M | 틀림. CORDIS 기준 €19,997,812.50 | VERIFIED |
| EU 2024 €500M 파트너십 | 미확인(EUR-Lex 접근 실패) | UNVERIFIED |
| 중국 희토류 유예 2026-11-10 만료 | 2027-01-10까지 2개월 연장(11-09 발표) | PARTIAL |
| 베이징 AI 과학 방안: 5대 차원, 자율실험실 | 맞음. 18개 과제, 6대 분야에 소재 포함 | VERIFIED |
| Periodic $300M 시드 | 맞음(a16z 리드, Felicis 참여) | PARTIAL / VERIFIED |
| Periodic 2026 $7.5B | 보도만 있음 | UNVERIFIED |
| Lila $350M 시리즈 A, 누적 $550M | 맞음 | VERIFIED |
| Lila 2,942 촉매 | 맞음(회사 주장, 3개월, 6개 계열, 17배) | VERIFIED(회사) |
| Lila 시리즈 B $2B | 협상 보도($8.5B pre) | PARTIAL |
| CuspAI $450M, $2.6B, 2026-07-20 | 맞음. 리드는 Kleiner와 NEA | PARTIAL |
| DeepMind 영국 랩 개관 | 개관 확인 없음 | UNVERIFIED |
| Radical AI 랩 개관, $55M 시드 | 맞음. 2026 신규 라운드 없음 | PARTIAL |
| Path $300M 시리즈 E, $2.45B | 맞음 | PARTIAL |
| LG EXAONE 42만 후보, 1일 vs 22개월 | 맞음(회사 발표 보도) | PARTIAL |
| MS/PNNL 18 vs 23 | 둘 다 맞음(23 = 18 신규 + 5 기지) | VERIFIED |
| IFP SDL "비용" | 단가 없음. 프로그램 금액만 있음($500M, $80M, $40M, $100M) | VERIFIED |
| USPTO 가이던스 철회 2025-11-28 | 맞음. 정확히는 폐지 후 개정 가이던스로 대체 | VERIFIED |
| IDTechEx $725M/2034, CAGR 9.0% | 맞음 | VERIFIED |
| MarketsandMarkets 수치 | 미확인(403) | UNVERIFIED |

## 접근 상태 로그

모든 시도는 2026-11-17에 이뤄졌다. 기본 도구는 `curl -sSL`(에이전트 프록시 경유, 일반 브라우저 User-Agent)이다. WebFetch 도구는 1회 시험했고 실패했다.

| 호스트 | 결과 | 시도한 내용 |
|---|---|---|
| www.mgi.gov (WebFetch) | **실패: getaddrinfo ENOTFOUND**(WebFetch 도구 자체의 DNS·허용목록 문제. 같은 호스트가 curl로는 200) | WebFetch 동작 확인 |
| www.govinfo.gov | 성공 200 | EO 14363 원문, USPTO FR Doc 2025-21457 원문 |
| www.whitehouse.gov | 성공 200(검색 3페이지만 404) | EO, 2025-11 팩트시트, 2026-07-22 >$5B, 2026-07 Golden Age, 2026-10 팩트시트 |
| www.federalregister.gov | HTML 문서 페이지는 **봇 차단(unblock.federalregister.gov CAPTCHA)**. 원문 txt도 같은 차단. **API(/api/v1)는 성공 200** | EO, USPTO 가이던스 메타데이터 |
| www.energy.gov | 성공 200(추정 URL 1건은 404) | Genesis 메인, $293M 보도자료, 278개 과제, Phase II, 10월 팩트시트, 과제 페이지, 뉴스 목록 |
| meritalk.com / www.meritalk.com | 성공 200 | $293M RFA 기사 |
| www.hpcwire.com | **403**(봇 차단) | $293M 기사 |
| www.insidegovernmentcontracts.com | 성공 200 | Covington: $293.76M, 21개 영역, $320M 설명 |
| grantedai.com | 성공 200(302 리디렉트 후) | $320M 블로그(2차 출처) |
| mgi.gov / www.mgi.gov | 성공 200(추정 경로 1건 404) | MGI 백서 PDF, 2021 전략계획 PDF, 홈 |
| www.nsf.gov | 2023 DMREF 200. **2021 DMREF 기사 404**. DMREF 공모 페이지 200 | DMREF 금액 |
| ifp.org | 성공 200 | IFP SDL 보고서 PDF |
| cordis.europa.eu | 성공 200 | BIG-MAP 예산 |
| research-and-innovation.ec.europa.eu | 200(Advanced Materials 페이지). **404**(IAM4EU 추정 URL) | COM(2024)98, €500M 파트너십 |
| eur-lex.europa.eu | **HTTP 202 빈 응답**(봇 챌린지로 추정), 2회 | COM(2024)98 원문 |
| v.daum.net | 성공 200 | 2026-04-30 AI 소재 전략 기사 2건 |
| view.asiae.co.kr | 성공 200 | 자율실험실 협의체 국문·영문 |
| www.asiae.co.kr | 성공 200 | K-문샷 2026-04 영문 기사 |
| www.newsis.com | 성공 200 | K-문샷 2026-02-25 |
| www.mt.co.kr | 성공 200 | K-문샷 로드맵 2026-09-30 |
| eiec.kdi.re.kr | 성공 200 | K-문샷 희토류 협의체·영구자석 미션 |
| smartcity.go.kr | **404** | K-문샷 안건 PDF |
| www.msit.go.kr | 200(보도자료 목록). 개별 보도자료는 찾지 못함 | AI 소재 전략 원 보도자료·예산 |
| www.korea.kr | 200(목록, 무관 기사 1건) | 정책브리핑 원문 |
| www.mofcom.gov.cn | 성공 200 | 2026 공고 목록(11-09 연장 공고는 찾지 못함) |
| english.mofcom.gov.cn | **실패: curl (6) Could not resolve host**(DNS) | 영문 MOFCOM |
| www.thestar.com.my | 성공 200 | Reuters 전재: 희토류 유예 연장 |
| source.benchmarkminerals.com | 성공 200 | 희토류 유예 연장 |
| www.spglobal.com | **403**(봇 차단·페이월) | 희토류 유예 연장 |
| www.reuters.com | **401**(Reuters 봇 차단·로그인 필요), 2건 | 중국 뉴스, Lila $1.3B 단독 |
| english.beijing.gov.cn | 성공 200 | 베이징 AI 과학연구 방안 해설 |
| www.idtechex.com | 성공 200 | MI 시장 전망 |
| www.marketsandmarkets.com | **403**(봇 차단), 2건 | 소재정보학 시장 리포트·보도자료 |
| www.jst.go.jp | 성공 200 | Moonshot 목표 3 |
| www8.cao.go.jp | 성공 200 | Moonshot 목표 3(내각부) |
| www.nims.go.jp | 200(pinax 보도자료 PDF). **404**(MaDIS 추정 URL) | DICE·MDPF |
| dice.nims.go.jp | 성공 200 | DICE 소개 |
| nanonet.mext.go.jp | **실패: CONNECT tunnel failed, 502**(프록시·원격 연결 실패), 2건 | ARIM |
| dxmt.mext.go.jp | **실패: CONNECT tunnel failed, 502** | DxMT |
| periodic.com | 200(홈). **404**(/blog) | Periodic Labs 원문 |
| siliconangle.com | 성공 200 | Periodic 시드(2025-10-01), CuspAI 시리즈 B(2026-07-20) |
| techcrunch.com | 200(검색 페이지. Periodic 관련 2026 기사 없음) | Periodic 2026 소식 |
| dealroom.co | **429**(요청 과다·레이트리밋) | Periodic $7B 보도 |
| www.lila.ai | 성공 200 | 뉴스 목록, 2,942 촉매 기사, Genesis 선정 |
| news.bloomberglaw.com | 성공 200(기사 앞부분 공개) | Lila 시리즈 B 협상 |
| www.cusp.ai | **404**(/news) | CuspAI 원문 |
| deepmind.google | 200(블로그 목록, 압축 해제 후). **404**(UK 파트너십 추정 URL) | 영국 자동화 랩 |
| www.radical-ai.com | 성공 200 | 회사 뉴스 |
| www.bkreader.com | 성공 200 | Radical AI 랩 개관 |
| www.robotics247.com | 성공 200 | Path 시리즈 E |
| thenextweb.com | 성공 200 | Path 시리즈 E 상세 |
| news.microsoft.com | 성공 200 | MS/PNNL 18 vs 23 |
| www.pnnl.gov | **404**(추정 URL) | PNNL 원 보도자료 |
| www.koreaherald.com | 성공 200 | LG EXAONE Discovery |
| www.koreatimes.co.kr | 성공 200 | LG EXAONE Discovery |
| WebSearch(검색 도구) | 성공(9회) | 원문 위치 탐색: DICE, $293M, 희토류, DeepMind, Periodic, Lila, K-문샷 예산, AI 소재 예산, Radical |
