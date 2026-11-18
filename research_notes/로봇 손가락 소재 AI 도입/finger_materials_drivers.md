# 로봇 손가락(로봇 손·그리퍼) 소재 구성과 AI/ML 도입의 기술적 동인

작성 기준일: 2026-11-18. 표기: **[원문확인]** = 1차 원문을 직접 받아 해당 문장을 확인함 / **[언론·기업주장]** = 기업 페이지·보도·2차 사이트 내용 / **[미확인(스니펫)]** = 검색 스니펫으로만 봤고 원문은 열지 못함. 각 항목 끝 괄호는 (출처 발행/게재 연도 · 확인일 2026-11).
범위 메모: 금전·투자·시장 내용은 제외함. 가격이 언급된 1차 문헌(LEAP, ORCA, CRAFT)도 가격 수치는 옮기지 않음.

---

## Q1. 로봇 손가락 각 부위에는 오늘날 어떤 소재가 쓰이고, 대표 물성값과 알려진 고장 모드는 무엇인가?

### Takeaway
연구용·상용 다관절 손은 대체로 **단단한 링크(PLA 등 3D 프린팅 플라스틱이나 금속) + 부드러운 실리콘/우레탄 손끝 피부 + 고분자 섬유 텐던(UHMWPE/Dyneema, 나일론 꼰줄)** 조합으로 수렴하고 있다. 소프트 그리퍼는 실리콘 엘라스토머(Ecoflex·Dragon Skin), TPU(Fin-Ray·플렉셔), 입자 재밍(커피 가루+라텍스 막), 전기접착(DEA 전극), 게코형 미세쐐기(Sylgard 170)를 쓴다. 1차 문헌에서 확인된 주요 고장은 다음과 같다. 손끝 실리콘 피부 열화(약 2,000~4,000회 파지), VBTS 실리콘 젤의 천공·찢김(10–15 N 반복하중에서 250–500회), 텐던 크리프·마모·느슨해짐, TPU 플렉서 관절의 피로 파단.

### Cited Findings

#### (a) 부위별 소재 맵: 강체 다관절 손
- **LEAP Hand (CMU, 2023)**: 손바닥은 단단하게, 손끝은 "soft rubber fingertips"로 만들었다고 저자가 직접 서술. 3D 프린팅으로 제작했고 표준 3D 프린터로 사내 수리가 가능하다고 강조. 직접구동(손가락 관절 모터) 구조. [원문확인] — [LEAP Hand, arXiv 2309.06440](https://ar5iv.labs.arxiv.org/html/2309.06440) (2023)
  - 반대 근거: 커뮤니티 위키는 LEAP 손끝을 TPU/NinjaFlex로 적음. 논문 표현("rubber")과 다르므로 어느 쪽인지 확정하지 못함. [미확인(스니펫)] — [web-3kk wiki](https://web-3kk.pages.dev/en/knowledge/hardware/hands/leap-hand)
- **ORCA Hand (ETH Zürich, 2025)**: 17자유도 텐던 구동 손이다. 구성은 다음과 같다.
  - 뼈대: FDM 프린팅 **PLA**.
  - 피부: 실리콘 주조 피부("silicone-cast skin").
  - 텐던: 관절마다 **나일론 섬유를 지름 0.4 mm 로프로 꼰 낚싯줄 2가닥**(굴곡근·신전근).
  - 텐던 경로: PLA에 직접 닿지 않도록 **매끈한 금속 핀/로드**로 우회해 마찰과 마모를 줄였다.
  - 배선: 지름 0.2 mm 구리선을 **PTFE 튜브** 안으로 통과시켰다.
  - 손끝 센서: FSR 박막 압력센서를 PLA 백플레이트에 붙이고 실리콘 몰딩 피부로 덮었다. 피부가 순응적이고 표면이 불규칙해서 접촉점에 따라 힘이 다르게 감쇠되므로 **이진(binary) 접촉 판정**만 썼다.
  [원문확인] — [ORCA, arXiv 2504.04259](https://arxiv.org/html/2504.04259) (2025)
- **CRAFT Hand (2026)**: 손가락 마디는 단단한 **PLA**, 손가락 관절은 부드러운 **TPU**로 만든 하이브리드 강-연 설계. 15개 모터가 텐던으로 구동한다. 설계 취지는 "충격과 접촉 불확실성이 몰리는 관절에 순응성을 두고, 기하학적 예측성과 하중 경로가 중요한 링크는 강체로 둔다"는 것. [원문확인] — [CRAFT, arXiv 2603.12120](https://arxiv.org/html/2603.12120v1) (2026-03)
- **Shadow Dexterous Hand**: 20개 모터, 텐던 구동, 24자유도. 일부 손끝에는 Shadow Tactile Fingertip(STF)이 기본 장착되고 업그레이드할 수 있다. 손끝·텐던의 구체적 소재는 페이지에 공개돼 있지 않다. [언론·기업주장] — [Shadow Robot](https://www.shadowrobot.com/dexterous-hand-series/) (확인 2026-11)
- **Allegro Hand**: 제조사 페이지에 16자유도 모델과 9자유도 모델이 있고, 360° 전방위 압력감응 촉각센서 탑재 모델과 비전 기반 촉각 + 손바닥 압력 감지 조합 모델이 있다. 손끝·링크 소재는 명시돼 있지 않다. [언론·기업주장] — [allegrohand.com](https://www.allegrohand.com/) (확인 2026-11)
- **Figure 03 손 (2025-10 발표)**:
  - 손끝을 더 부드럽고 적응적으로 만들어 접촉 면적을 늘렸다고 함.
  - 시판 촉각센서는 실사용 내구성이 부족하다고 판단해 자체 1세대 촉각센서를 개발했다고 함. 설계 원칙은 "극한 내구성, 장기 신뢰성, 고충실도 감지".
  - **각 손끝 센서가 3 g 수준의 힘을 감지**한다고 함.
  - 손바닥 카메라를 내장했다고 함.
  - 몸체 쪽에는 다밀도 폼과 세탁 가능한 직물 소재 "soft goods"를 쓴다고 함.
  [언론·기업주장, 기업 원문 확인] — [Figure, "Introducing Figure 03"](https://www.figure.ai/news/introducing-figure-03) (2025-10)
- **Sanctuary AI 유압 손(Phoenix 계열)**: 제조사 페이지는 17자유도와 통합 촉각센서, "광범위한 내구 시험으로 고듀티 연속운전 검증", 저압·소유량 유압과 자동 고장 보호를 주장한다. 손끝 소재와 시험 사이클 수는 공개하지 않았다. [언론·기업주장] — [Sanctuary AI Hydraulic Hands](https://sanctuary.ai/solutions/hydraulic-hands/) (확인 2026-11)
  - 2차 출처의 주장(손가락 패드 7셀 마이크로 기압계 배열·5 mN 감지, 액추에이터 20억 회 무누설 시험)은 1차 근거를 찾지 못함. [미확인(스니펫)] — [heymanoid](https://heymanoid.pages.dev/robots/sanctuary-phoenix/), [robozaps](https://blog.robozaps.com/b/sanctuary-ai-phoenix-review)
- **Unitree Dex5-1**: 자유도 20(능동 16 + 4). 손 하나에 압력센서 94개가 있다(손바닥 2×5, 손가락 패드·손끝마다 2×3 배열). 감지 범위 10 g–2,500 g, 손끝 힘 10 N, 무게 1.1 kg. 손끝 소재는 공개돼 있지 않다. [언론·기업주장, 제조사 사양표 확인] — [Unitree Dex5-1](https://www.unitree.com/Dex5-1) (확인 2026-11)
- **Inspire RH56 계열**: 리셀러·애그리게이터 페이지 기준으로 "all-metal" 골격이다. RH56H1은 촉각 감지점 260개(손끝 170 + 손바닥 90)로 표기됐고, 저항식·정전용량식 촉각 옵션이 있다. 출처 간 무게·센서 수가 다르다. [미확인(스니펫)] — [Knox Labs RH56F1](https://www.knoxlabs.com/products/inspire-robots-rh56f1-dexterous-hand), [humanoid.guide RH56H1](https://humanoid.guide/product/rh56h1/)
- **Tesla Optimus (V3 특허 해설)**: 2차 해설 사이트에 따르면 V3는 전완부 액추에이터에서 원격 텐던으로 약 22개 관절을 구동한다. 특허 문서가 "백만 사이클 내구성"과 단순한 제조 형상을 강조한다고 전한다. 텐던·손끝 소재의 1차 출처는 확인하지 못함. [언론·기업주장(2차)] — [humanoid.guide, Tendon-driven hands](https://humanoid.guide/?p=16664) (2026)

#### (b) 부위별 소재 맵: 소프트 그리퍼·손가락
- **공압 실리콘 손가락 소재 물성(제조사 값)**:
  - **Ecoflex 00-30**: Shore 00-30, 인장강도 약 200 psi(≈1.4 MPa), 파단연신율 약 900%. [미확인(스니펫)] — [Smooth-On compare](https://www.smooth-on.com/compare/4922/4985/ecoflex-00-20--ecoflex-00-30/)
  - **Dragon Skin 30**: Shore A 30, 인장 500 psi(3.45 MPa), 파단연신율 약 364%(ASTM D412). [미확인(스니펫)] — [FormX Dragon Skin 30](https://www.formx.eu/p/product/dragon-skin-30/skin30x/)
  - Ecoflex 00-30은 Shore 00 척도라서 Shore A 값과 직접 비교할 수 없다. [미확인(스니펫)]
- **제조사 데이터시트만으로는 부족하다는 지적**: UCL의 소프트로봇 재료 DB 논문은 "초탄성 재료는 제조사 데이터시트만으로 선택할 수 없다"고 결론 내렸다. 대변형 범위에서 인장시험 데이터로 초탄성 구성모델을 비선형 최소자승으로 맞춰 공개 DB로 제공했다. 점탄성, 이전 하중이력에 의한 손상, **Mullins 효과**는 다루지 못했다고 한계를 밝혔다. [원문확인] — [Marechal et al., "Towards a Common Framework and Database of Materials for Soft Robotics" (UCL repo)](https://discovery.ucl.ac.uk/10112846/1/Towards_a_Common_Framework_and_Database_of_Materials_for_Soft_Robotics___Revision2.pdf) (2021, Soft Robotics 게재본 수정고) / DB: github.com/LucMarechal/Soft-Robotics-Materials-Database
- **온습도 의존성**: Yale Faboratory는 Ecoflex 00-30과 Dragon Skin 10의 거동을 온도·습도 범위에서 특성화했다. 데이터시트 값만으로는 액추에이터 거동을 예측하기 어렵다는 취지다. [미확인(스니펫)] — [Porte et al. 2023, Yale](https://www.eng.yale.edu/Faboratory/publications\journal\2023\Porte%20-%202023%20-%20Characterization%20of%20temperature%20and%20humidity%20dependence%20in%20soft%20elastomer%20behavior.pdf)
- **Fin-Ray 손가락**: 학습 기반 Fin-Ray 설계 연구는 **TPU 95A(영률 26 MPa)**로 손가락을 제작했다. "소프트 손의 기능은 구조와 재료의 고유 순응성에 크게 좌우된다"고 서술한다. [원문확인] — [Deng & Li, "Learning Optimal Fin-Ray Finger Design for Soft Grasping", Front. Robot. AI (PMC7907605)](https://www.frontiersin.org/articles/10.3389/frobt.2020.590076/full) (2021)
- **입자 재밍 그리퍼**: 개별 손가락 대신 입자 덩어리를 막에 넣는다. 물체에 누르면 입자가 형상을 감싸고, 진공을 걸면 수축·경화해 센서 피드백 없이 잡는다. 파지력은 **마찰·흡착·기계적 맞물림(interlocking)** 세 메커니즘에서 나온다. [원문확인(초록)] — [Brown et al., PNAS 2010 (PMC2973877)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=2973877) (2010)
  - 커피 가루와 라텍스 풍선 막의 구체 사양은 본문을 열지 못해 확인하지 못함.
- **전기접착(EA) 소프트 손가락**: Shintake et al.(Adv. Mater. 2016)은 맞물린(interdigitated) 전극을 써서 **단일 전압으로 굽힘(DEA)과 전기접착을 동시에** 구현했다. 사전 연신 엘라스토머 양면에 전극을 두었다.
  - 기존 DEA 전극 배치보다 전기접착력이 10배 이상이라고 보고.
  - 그리퍼 약 1.5 g, 닫힘 약 100 ms.
  - 학위논문 기준 전단력 3.5 N/cm².
  [미확인(스니펫)] — [SPIE Newsroom](https://spie.org/news/6409-soft-compliant-gripper-for-safe-manipulation-of-extremely-fragile-objects), [EPFL thesis TH6855](https://infoscience.epfl.ch/record/215319/files/EPFL_TH6855.pdf?version=1) (2016)
- **게코형 건식 접착 손가락**: Stanford·JPL 계열 그리퍼는 **Sylgard 170 실리콘**을 왁스 몰드에 스핀코팅·경화해 미세 쐐기(밑변 15 µm, 높이 46 µm, 폭 200 µm)를 만든다. 우표 크기 타일에 쐐기 수십만 개가 있고, 케이블 장력으로 접착을 켠다. 패치·뉴스 기반 정보다. [미확인(스니펫)] — [US Patent 11872691](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11872691), [Stanford Daily 2023](https://stanforddaily.com/2023/02/01/lab-develops-stickiest-non-sticky-material/)
  - Astrobee용 게코 접착 그리퍼는 2019년 ISS로 발사돼 궤도 실험을 했다. [미확인(스니펫)] — [arXiv 2009.09151](https://arxiv.org/abs/2009.09151)
- **비전 기반 촉각(VBTS) 손끝 젤**: GelSight 계열 표준 젤은 투명 실리콘 베이스층(Smooth-On **Solaris, Shore A 15**)과 불투명 이미지 전사층(**EcoFlex 00-10**)으로 이루어진다. 비교군 폴리우레탄 젤은 **Clear Flex 50(Shore A 50)** 베이스와 **VytaFlex 40** 전사층을 쓴다. [원문확인] — [Benchmarking Resilience and Sensitivity of Polyurethane-Based VBTS, arXiv 2511.07797](https://arxiv.org/html/2511.07797v1) (2025-11)
  - GelSight Mini 데이터시트는 젤 내구 등급을 "1000 Coin Presses"로 표기하고, 카트리지를 공구 없이 교체할 수 있다고 한다. 2025-01에는 "최대 40% 내구성 향상" 젤을 발표했다(사내 시험 기준). [언론·기업주장/미확인(스니펫)] — [Anzu/GelSight 발표](https://www.anzupartners.com/2025/01/06/gelsight-extends-life-and-durability-of-gelsight-mini-with-new-gels/)
  - GelSlim(2018)은 더 질긴 젤, 직물 피부, 강체 몸체로 3,000회 이상 파지 시험을 했다. [미확인(스니펫)] — [GelSlim, arXiv 1803.00628](https://arxiv.org/html/1803.00628)

#### (c) 텐던·케이블 소재와 고장
- ORCA는 "텐던 구동은 **마찰 누적, 마모, 시간에 따른 느슨해짐(slack)**이 정밀도와 수명에 영향을 준다"고 적었고, 금속 핀 우회로 대응했다. [원문확인] — [ORCA](https://arxiv.org/html/2504.04259) (2025)
- 텐던 암 논문은 Dyneema의 고하중 크리프 저항을 높이려고 **사전 인장·열처리 Dyneema**를 써서 신율을 1% 미만으로 낮췄다. [미확인(스니펫)] — [arXiv 2307.02654](https://arxiv.org/pdf/2307.02654) (2023)
- 2차 해설 두 곳의 종합:
  - UHMWPE(Dyneema)가 주류다. 무게 대비 강하고 작은 풀리에서 유연하며 마찰이 낮다. 다만 반복하중에서 크리프로 길어지면서 보정이 깨진다.
  - 아라미드(Kevlar·Technora)는 크리프가 적지만 풀리 접촉부에서 빨리 마모된다.
  - 강철 케이블은 손가락의 작은 굽힘 반경에서 피로 균열이 생긴다.
  - 결국 소재 선택은 "크리프·굴곡피로·마모·마찰 사이의 절충"이다.
  [언론·기업주장(2차)] — [humanoid.guide](https://humanoid.guide/?p=16664) (2026); "비처리 Dyneema 로프는 반복하중에서 신율 9% 이상, 500사이클 넘어서도 증가" 수치는 출처 불명 위키라 [미확인(스니펫)] — [aiwiki tendon_driven](https://aiwiki.ai/wiki/tendon_driven)
- DLR/ESA Spacehand는 텐던 후보 섬유를 대상으로 진공 태양광 모사, 진공 감마선 조사, 여러 재료 위 미끄럼 내구, 모사하중 크리프 시험을 했다. [미확인(스니펫)] — [DLR elib 114155](https://elib.dlr.de/114155/1/95690_Chalon.pdf)

#### (d) 1차 문헌에서 확인한 내구성·고장 수치
- **ORCA**:
  - 연속 10,000회 이상(약 20시간) 운전에서 하드웨어 고장이 없었다.
  - 파지 2,250회 동안 파손, 모터 정지, 과도한 텐던 느슨해짐이 없었다.
  - 한계: **실리콘 피부 열화로 피부와 FSR 사이에 공극이 생겨 감지 임계값이 상승**했다. 손끝 5개 중 2개에서 **약 2,000~4,000회 파지 후** 발생했다. 신호선(0.2 mm 구리선) 단선도 손끝 3개에서 발생했다.
  [원문확인] — [ORCA](https://arxiv.org/html/2504.04259) (2025)
- **VBTS 실리콘 젤**: 4 mm 구형 압자로 15 N 압축을 1,000회 가하는 시험에서 실리콘 샘플 1·2가 **250–500회 사이에 천공·찢김으로 파국 파손**했다. 폴리우레탄 젤은 1,000회 동안 판독값 변화가 작았다. 저자들은 1,000회를 "센서 수명 근사치"로 설정했다. 실리콘 젤의 알려진 고장 모드는 **연마·긁힘·찢김에 의한 이미지 전사층 마모**와 **실리콘–아크릴 창 박리**다. 실리콘–아크릴 결합강도가 낮은 문제는 기존 대책들로도 해결되지 않았다. [원문확인] — [arXiv 2511.07797](https://arxiv.org/html/2511.07797v1) (2025-11)
- **TPU 플렉서 관절**: CRAFT는 "소프트 플렉서 관절은 반복 굽힘에서 피로가 누적돼 결국 파단된다"고 적었다. 대책으로 PIP·DIP 관절을 롤링 접촉(rolling-contact)으로 바꿔 TPU 면에 하중을 분산시켰다. 또 단일 텐던이 PIP·DIP를 함께 당기면 하중과 자세에 따라 굽힘 분배가 달라져 예측 제어가 어렵다고 지적했다. [원문확인] — [CRAFT](https://arxiv.org/html/2603.12120v1) (2026)

#### (e) 마찰
- Liu & Howe(Harvard)는 엘라스토머 손끝(외피 **Dragon Skin 30**)의 미끄럼 실험을 했다. 고무 마찰은 **수직력 Fn과 접촉속도 v에 강하게 의존하고 큰 확률적 성분**을 가진다. Ft/Fn 비는 한 번의 미끄럼 안에서도 크게 변하고, 에피소드마다 최대값이 달라진다. 따라서 상수 µ를 가정하는 쿨롱 모델은 미끄럼을 놓친다. 대안으로 µ = β0 + β1·v + β2·Fn + ε 형태의 회귀식을 제안했다. [원문확인] — [Liu & Howe, "Beyond Coulomb: Stochastic Friction Models for Practical Grasping and Manipulation" (NSF PAR)](https://par.nsf.gov/servlets/purl/10485527) (게재 연도 원문 표지에서 미확인, NSF PAR 등재)

### Inferences
- 공개 사양이 많은 연구용 손(LEAP, ORCA, CRAFT)은 "**강체 PLA 링크 + 실리콘/TPU 연질부 + 고분자 섬유 텐던**"으로 수렴한다. 상용 손(Shadow, Unitree, Figure, Sanctuary)은 감지 성능을 공개하지만 피부·패드 소재는 대부분 공개하지 않는다. 그래서 상용 손의 소재 맵은 공백이 크다.
- 손끝 피부는 감지 민감도(부드러움)와 내구성(경도·인열강도·접착력) 사이에서 절충해야 한다. VBTS 비교(Shore A 15 실리콘 대 Shore A 50 우레탄)와 ORCA 피부 열화가 같은 절충을 보여준다. Figure가 "시판 센서가 실사용을 견디지 못했다"고 한 주장도 같은 맥락이다.
- 1차 문헌 내구 시험은 대체로 10³~10⁴회에 그친다(ORCA 2,250회와 10,000회 이상, VBTS 1,000회). 기업 주장(Optimus "백만 사이클", Sanctuary "20억 사이클")과는 3~6자릿수 차이가 나며, 후자는 검증되지 않았다.

### Gaps
- Shadow, Allegro, Inspire, Tesla Optimus, Figure 03, Sanctuary 손끝 패드의 **소재명·Shore 경도·마찰계수** 1차 공개값을 찾지 못함.
- 손끝 소재별 **마찰계수 정량값**(예: 실리콘 대 우레탄 대 직물, 건조·습윤)을 1차로 확보하지 못함. Liu & Howe는 µ가 상수가 아님을 보였지만, 본 노트에 옮길 대표 수치는 추출하지 못함.
- Ecoflex·Dragon Skin 공압 손가락의 **피로 수명(사이클)·히스테리시스 수치·사용 온도범위**를 1차 원문으로 확인하지 못함(Yale 온습도 논문 원문 미열람).
- 재밍 그리퍼 본문(입자 종류, 막 재질, 파지력)과 게코 그리퍼의 학술 원문(Science Robotics 2017 여부)을 열지 못함.

---

## Q2. 기존 방법(물리 모델, 시행착오)으로 손가락 소재를 설계하기 어려운 이유는 무엇인가? 리뷰의 진술은?

### Takeaway
리뷰와 1차 논문이 꼽는 어려움은 다섯 가지다. ① 연질재료의 **비선형·히스테리시스·크리프·드리프트**가 해석 모델과 보정을 무력화한다. ② **FEM은 정확하지만 비싸고 수렴이 어렵다**. ③ 소재·형상·제어가 결합된 **고차원 비선형 설계공간**을 손으로 탐색할 수 없다. ④ **접촉·마찰은 쿨롱 가정이 깨지고 확률적**이다. ⑤ 주조 기반 제작과 내구 시험이 **느리고 노동집약적**이다.

### Cited Findings
- Kim et al. 리뷰(PLoS ONE 2021)의 진술:
  - "강체 로봇에 비해 소프트 로봇은 모델링·보정·제어에서 문제가 있다. 연질재료의 고유 특성이 비선형성과 히스테리시스로 복잡한 거동을 낳기 때문이다."
  - "구조적 순응성과 재료의 점탄성이 비선형성과 히스테리시스로 인해 복잡하고 예측 불가능한 거동을 만든다."
  - "크리프, 드리프트, 높은 자유도가 히스테리시스를 키운다. 이 때문에 소프트 그리퍼를 수학적으로 모델링하고 소프트 센서를 보정하기 어렵다."
  - "초탄성 특성이 비선형성, 큰 히스테리시스, 크리프, 드리프트를 일으켜 예기치 않은 물리·전기 응답을 낳는다."
  - "로딩·언로딩 사이 큰 히스테리시스 루프가 전통적 해석·실험 방법을 복잡하게 만든다."
  [원문확인] — [Kim et al., "Review of machine learning methods in soft robotics", PLoS ONE (PMC7891779)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/) (2021-02)
- Fin-Ray NN 최적화 논문: "FEM은 비선형 탄성재료와 복잡한 구조를 시뮬레이션할 수 있지만 **계산 비용이 크고 수렴 문제가 생길 수 있다**." [원문확인] — [Multi-Objective NN-Assisted Design Optimization of Soft Fin-Ray Fingers, arXiv 2506.00494](https://arxiv.org/html/2506.00494) (2025)
- 소프트 그리퍼 공동설계(co-design) 논문: "설계–제어 결합 탐색공간은 **고차원이고 고도로 비선형**이다. 두 요소는 시간 척도도 크게 다르다. 설계는 제조 시점에 바뀌고 제어는 실시간으로 갱신된다." 또 기존 계산 설계·공동설계 접근은 "계산 비용이 크고 새로운 물체나 작업으로 일반화하기 어렵다." [원문확인] — [Yi et al., "Co-Design of Soft Gripper with Neural Physics", arXiv 2505.20404](https://arxiv.org/html/2505.20404) (2025)
- SoRoForge: "소프트 로봇의 중대한 한계는 설계·제작이 어렵다는 점이다. 대부분의 설계는 **시행착오로 수작업** 생성된다." [원문확인] — [Smith et al., SoRoForge (matterassembly.org)](https://matterassembly.org/publications/smith2023soroforge/) (2023)
  - 같은 그룹 2021년 논문: 대부분의 액추에이터는 노동집약적 다단계 주조로 만들어지고, 주조 공정 제약이 설계공간 자체를 좁힌다. [미확인(스니펫)] — [Smith 2021 CASE](https://matterassembly.org/assets/pdf/preprints/2021_Smith_Seamless_Acuator_Synthesis_CASE_2021.pdf)
- UCL 재료 DB: "초탄성 재료는 제조사 데이터시트만으로 선택할 수 없다." 점탄성과 Mullins 효과 같은 이력 의존 손상은 아직 모델에 반영되지 않았다. [원문확인] — [Marechal et al.](https://discovery.ucl.ac.uk/10112846/1/Towards_a_Common_Framework_and_Database_of_Materials_for_Soft_Robotics___Revision2.pdf) (2021)
- 접촉·마찰 모델링:
  - Liu & Howe: 쿨롱 법칙은 µ를 상수로 보지만 엘라스토머 손끝 마찰은 Fn·v 의존적이고 확률적이다. 쿨롱 모델은 실제 두 번째 미끄럼을 "완전히 놓쳤다". [원문확인] — [NSF PAR 10485527](https://par.nsf.gov/servlets/purl/10485527)
  - Kasolowsky & Bäuml: 촉각 피부의 공간 응답을 시뮬레이션할 때 어려운 점은 점 접촉이 아닌 **소프트 접촉(접촉 패치)**을 모델링해야 한다는 것이다. 강체 시뮬레이터가 주는 침투 깊이는 부정확해서 힘 평형으로 다시 계산해야 했다. [원문확인] — [arXiv 2409.12735](https://arxiv.org/html/2409.12735) (2024)
  - HydroShear: 기존 강체 접촉, 페널티 기반 소프트 접촉, 하이드로엘라스틱 근사는 전단 의존 작업에서 sim-to-real 격차를 메우지 못한다. 센서 부정확성이나 신호 열화 같은 "tactile shadowing" 효과를 모델링하지 않기 때문이다. [원문확인] — [HydroShear, RSS 2026](https://roboticsproceedings.org/rss22/p155.pdf) (2026-07)
- 촉각 신호: "촉각센서 신호는 노이즈가 많고 고차원이며 복잡하고, 필수 정보와 무관 정보가 섞여 있다. 이런 문제를 다룰 신호처리·ML 방법이 아직 부족하다." 압저항 감지는 히스테리시스 영향이 크다. [원문확인] — [Sensors 2017 리뷰 "Novel Tactile Sensor Technology and Smart Tactile Sensing Systems" (PMC5713637)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5713637) (2017)
  - 2025 촉각 데이터 표현 리뷰: 복잡한 비평면 형상에 고밀도 taxel이 넓게 분포하면 taxel 공간 보정이 특히 어렵다. 여러 센서 하드웨어에 두루 통하는 자율 보정법은 아직 없는 미해결 문제다. [원문확인] — [Representing Data in Robotic Tactile Perception – A Review, arXiv 2510.10804](https://arxiv.org/html/2510.10804v1) (2025-10)
- 2023 Annual Review of Control, Robotics, and Autonomous Systems(ETH 저장본)는 향후 과제로 "복잡한 재료, 정확한 모델링, 고급 제어, 지능적 거동"을 든다. PDF 다운로드가 HTML(차단)로 반환돼 원문을 확인하지 못함. [미확인(스니펫)] — [annurev-control-062322-100607 (ETH)](https://research-collection.ethz.ch/bitstream/20.500.11850/595503/2/annurev-control-062322-100607.pdf)
- 소프트로봇 적응성 서베이(UCL): 제조 공차와 재료 노화 같은 편차 때문에 제어 전략을 로봇 간에 일반화하기 어렵다. [미확인(스니펫)] — [UCL survey](https://discovery.ucl.ac.uk/10211643/1/A_Survey_on_Soft_Robot_Adaptability_Implementations_Applications_and_Prospects_Survey.pdf)

### Inferences
- 어려움은 손가락 부위별로 다른 물리에서 생긴다.
  - 피부: 초탄성·점탄성·Mullins 효과·마모.
  - 관절: 플렉서 피로, 비균일 굽힘 분배.
  - 텐던: 크리프·마찰 누적.
  - 표면: 확률적 마찰, 소프트 접촉 패치.
  각 물리가 하나의 해석모델로 묶이지 않아서 "모델 기반 설계 → 시제품 → 내구 시험" 루프가 길고 비싸진다.
- 내구성 문제(피부 열화 2,000~4,000회, 젤 천공 250~500회)는 수백~수천 회 실측해야 드러난다. 그래서 시행착오 한 번의 비용이 크다는 점은 1차 데이터에서 간접적으로 확인된다.

### Gaps
- "내구 시험이 느려서 ML을 도입했다"는 인과를 **명시한** 리뷰 문장은 찾지 못함. 1차 논문의 시험 설계에서 추론한 것이다.
- Science Robotics, Nature Machine Intelligence, Advanced Materials, IEEE T-RO의 리뷰는 Cloudflare/유료벽으로 원문을 열지 못해 직접 인용이 없다.

---

## Q3. 연구자들은 왜 손가락 소재·손끝 설계에 ML/AI를 적용하기 시작했는가?

### Takeaway
ML 도입의 동기는 Q2의 다섯 장벽에 일대일로 대응한다.
- ① 비선형·히스테리시스 센서와 액추에이터의 **데이터 기반 보정·모델링**: 해석모델보다 정확하다고 보고됨.
- ② **FEM 대리모델(surrogate)**: 비싼 시뮬레이션을 학습된 신경망으로 바꿔 빠르고 미분 가능한 최적화를 가능하게 함.
- ③ 소재 강성 분포와 파지 자세의 **공동설계**.
- ④ 확률적 마찰과 접촉 이벤트를 데이터로 추정·정렬하는 **sim-to-real**.
- ⑤ 노이즈 많은 고차원 **촉각 신호 해석**.
- 보조적으로, 실험 수가 많이 드는 **재료·공정 최적화에 베이지안 최적화**를 씀.

### Cited Findings
- **보정·모델링**:
  - Kim et al.: "ML은 해석·실험 접근으로 쉽게 표현되지 않는 비선형성과 히스테리시스를 고려해 소프트 센서를 정확히 특성화·보정할 수 있다."
  - "딥러닝 모델이 비선형성과 히스테리시스 같은 소프트 로봇의 기존 문제를 해결했고, 비딥러닝 접근보다 성능이 좋았다고 보고됐다."
  - 히스테리시스 모델 파라미터는 데이터 기반 접근에서 ML 알고리즘이나 볼록 최적화로 최적화된다.
  - 이 리뷰는 ML 적용을 소프트 센서, 소프트 액추에이터, 응용(웨어러블 등)으로 분류하고, 비지도 학습 연구는 적다고 지적한다.
  [원문확인] — [Kim et al. PLoS ONE 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)
- **FEM 대리모델**: Fin-Ray 논문은 "ML 같은 데이터 기반 방법과 FEM의 결합이 소프트로봇 모델링·개발에 새 기회를 연다"고 쓴다. 선행연구 사례:
  - FEM으로 만든 데이터셋으로 신경망을 학습해 총 접촉력과 변형을 FEM과 비슷한 정확도로 계산.
  - PINN이 실측 데이터를 더했을 때 FEM보다 정확도가 향상됨.
  [원문확인] — [arXiv 2506.00494](https://arxiv.org/html/2506.00494) (2025)
- **소재–형상–제어 공동설계**: Yi et al.은 시뮬레이션 데이터로 학습한 "neural physics" 대리모델(빠르고 미분 가능)을 쓴다. 이 모델로 3D 프린팅 플렉서 손가락의 **블록 단위 강성 분포와 파지 자세를 함께 최적화**했다. 시뮬레이션과 실하드웨어 모두에서 기준 설계보다 파지 성공률이 크게 높았다고 보고. [원문확인] — [arXiv 2505.20404](https://arxiv.org/html/2505.20404) (2025)
- **학습 기반 형상 설계**: Deng & Li는 작업 제약을 "grasp quality function"(winding number 기반 경험적 지표)으로 묶어 TPU 95A Fin-Ray 손가락 형상을 최적화했다. 이 품질함수는 다른 소프트로봇에도 쓸 수 있다고 한다. [원문확인] — [Front. Robot. AI 2021](https://www.frontiersin.org/articles/10.3389/frobt.2020.590076/full)
- **생성적·진화적 설계 + 자동 제작**: SoRoForge는 유전 알고리즘, 생성적 인코딩, FEM 해석, 다재료 적층제조를 결합했다. 수작업 설계와 같은 출력을 내는 데서 시작해 사용자 지정 성능의 새 액추에이터 생성까지 시연. [원문확인] — [SoRoForge](https://matterassembly.org/publications/smith2023soroforge/) (2023)
- **재료·공정 최적화**:
  - 비틀림-코일 고분자 액추에이터: 가능한 공정 조합 1,089개 중 62개만 제작하고 베이지안 최적화(가우시안 프로세스)로 구동 변형률 1.25에 도달. [미확인(스니펫)] — [Zhang et al., Materials & Design 2025 (Aalto)](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat/)
  - 자기치유 엘라스토머 조성 BO 탐색(학회 포스터)과 Elastosil 기반 DEA self-driving lab 프리프린트(2026)도 있지만 폐루프 조성 최적화는 아직 초기 단계. [미확인(스니펫)] — [U. Dayton poster](https://ecommons.udayton.edu/stander_posters/3375), [arXiv 2604.02609](https://arxiv.org/html/2604.02609v1)
- **촉각 신호 해석**:
  - Sensors 2017 리뷰는 "복잡한 신호를 다룰 ML 방법이 부족하다"는 문제의식에서 ML·신호처리 중심 리뷰를 썼다. [원문확인] — [PMC5713637](https://pmc.ncbi.nlm.nih.gov/articles/PMC5713637)
  - 2024 Sensors 리뷰는 ML 기여를 센서 설계, 보정·보상, 물체 인식·분류, 거동 예측의 4영역으로 정리한다. [미확인(스니펫)] — [MDPI Sensors 24(10):2958](https://www.mdpi.com/1424-8220/24/10/2958/html)
  - Frontiers 사설은 로봇 손 촉각이 감지점이 희소하고 공간 해상도가 낮아서 제한된 스트레인 게이지 데이터로 ML이 접촉 정보를 추론하는 연구를 소개한다. [미확인(스니펫)] — [Editorial: Tactile Intelligence in Robots (PMC7531175)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7531175/)
- **마찰·접촉의 sim-to-real**:
  - Liu & Howe는 단일 미끄럼 스트로크에서 회귀로 마찰 파라미터를 추정하는 실용 모델을 제안했다. 데이터가 Fn–v 공간을 넓게 덮을수록 파라미터 추정 분산이 줄었다. [원문확인] — [NSF PAR](https://par.nsf.gov/servlets/purl/10485527)
  - HydroShear는 하이드로엘라스틱 전단 시뮬레이션으로 **제로샷 sim-to-real 촉각 강화학습** 정책을 학습했다. [원문확인] — [RSS 2026 p155](https://roboticsproceedings.org/rss22/p155.pdf)
  - 2026 프리프린트들은 실측 접촉 데이터로 신경 순방향 동역학을 학습해 시뮬레이션을 현실에 맞추거나(2601.12796), 접촉 개시·종료 시점을 정렬한다(2606.11767). [미확인(스니펫)] — [arXiv 2601.12796](https://web3.arxiv.org/pdf/2601.12796), [arXiv 2606.11767](https://arxiv.org/html/2606.11767v2)
- **하드웨어가 학습을 위해 설계되는 흐름**: LEAP는 "머신러닝용 손 하드웨어는 내구성, 반복성, 다용도성을 갖추고 이상적으로 인간형이어야 한다"고 썼다. CRAFT는 "학습 정책이 기대하는 곳에 접촉을 둘 만큼 정확하면서, 데이터 수집 중 피할 수 없는 충돌·미끄럼을 견딜 만큼 강건해야 한다"는 긴장을 강체 링크 + TPU 관절 소재 배치로 풀었다. [원문확인] — [LEAP](https://ar5iv.labs.arxiv.org/html/2309.06440), [CRAFT](https://arxiv.org/html/2603.12120v1)
- **기업 측 동기**: Figure는 촉각센서를 자체 개발한 이유로 시판 센서의 실사용 내구 한계를 든다. Sanctuary는 촉각센서가 "더 풍부한 행동 데이터"를 만든다고 강조한다. 손끝 소재와 센서가 **학습 데이터 생성 장치**로 다뤄지고 있다는 뜻이다. [언론·기업주장] — [Figure 03](https://www.figure.ai/news/introducing-figure-03), [Sanctuary](https://sanctuary.ai/solutions/hydraulic-hands/)

### Inferences
- AI 도입은 "재료를 새로 발견"하는 쪽(조성 탐색)보다 "**이미 쓰는 엘라스토머·TPU의 비선형 거동을 데이터로 다루고, 그 위에서 형상·강성 분포·제어를 함께 최적화하는**" 쪽이 1차 문헌에서 훨씬 성숙했다. 엘라스토머 조성 자체의 ML/자율실험은 2025–2026년에도 포스터·프리프린트 단계에 머무는 것으로 보인다(확인된 범위 기준).
- 역방향 인과도 있다. 손 하드웨어(LEAP, ORCA, CRAFT)는 학습 정책의 데이터 수집을 견디도록 소재를 고르고 배치한다. 따라서 "AI가 소재 설계를 돕는다"와 "AI(학습 기반 조작)가 소재 요구사항을 바꾼다"는 두 방향을 구분해 서술할 필요가 있다.

### Gaps
- Science Robotics, Nature Machine Intelligence, Advanced Materials, IEEE T-RO 리뷰(ML for soft robotics, tactile skin, gripper design)를 직접 열지 못해 해당 저널의 인용 문장이 없다. 대신 PLoS ONE, Sensors, Frontiers, arXiv와 RSS 원문으로 대체했다.
- 손끝 피부의 **마모·피로 수명을 ML로 예측**한 1차 연구는 이번 조사에서 찾지 못함.
- Tesla, Figure, Sanctuary가 소재 설계에 AI를 쓰는지에 대한 공개 근거는 없음(공개된 AI 활용은 제어·정책 학습 쪽).

---

### 접근 상태 로그 (2026-11-18)
| host | result | purpose |
|---|---|---|
| eutils.ncbi.nlm.nih.gov (efetch PMC) | 성공 (PMC7891779, PMC5713637, PMC7907605 전문 / PMC2973877 초록만) | ML 소프트로봇 리뷰, 촉각 리뷰, Fin-Ray 학습, 재밍 그리퍼 |
| arxiv.org / ar5iv.labs.arxiv.org | 성공 | LEAP, ORCA, CRAFT, Fin-Ray NN, co-design, VBTS 우레탄, 촉각 표현 리뷰, Kasolowsky |
| arxiv.org/abs/2009.09151, 2604.20295 | 부분 (abs 페이지만, 관련 수치 없음) | 게코 Astrobee, ETac |
| discovery.ucl.ac.uk (PDF) | 성공 | 소프트로봇 재료 DB (Marechal et al.) |
| research-collection.ethz.ch (Annual Review PDF) | 실패 (PDF 대신 HTML 반환) | Annual Review CRAS 2023 |
| par.nsf.gov (PDF) | 성공 | Liu & Howe 확률적 마찰 모델 |
| roboticsproceedings.org (PDF) | 성공 | HydroShear RSS 2026 |
| matterassembly.org | 성공 | SoRoForge |
| www.mdpi.com/2297-8747/28/2/53 | 실패 (321바이트, 차단) | 소프트로봇 설계 리뷰 |
| www.figure.ai | 성공 | Figure 03 손 |
| www.shadowrobot.com | 성공 (소재 정보 없음) | Shadow Hand |
| www.allegrohand.com | 성공 (소재 정보 없음) | Allegro |
| sanctuary.ai | 성공 | 유압 손 |
| www.unitree.com/Dex5-1 | 성공 | Dex5-1 사양 |
| humanoid.guide | 성공 (2차 출처) | 텐던 소재·Optimus V3 해설 |
| anzupartners.com | 실패 (본문 거의 없음) | GelSight 젤 내구성 발표 |
| WebFetch 도구 | 사용 안 함 (세션에서 고장 안내) | — |
| Smooth-On, FormX, SPIE, EPFL, Stanford Daily, USPTO, Yale, Aalto 등 | 검색 스니펫만 | 엘라스토머 물성, 전기접착, 게코, 온습도, BO |
