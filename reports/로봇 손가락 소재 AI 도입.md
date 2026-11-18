# 로봇 손가락 소재에 AI가 들어온 이유, 적용 방식, 남은 과제

작성 기준일 2026-11-18. 이 보고서는 재료공학 관점에서 로봇 손가락을 이루는 소재에 인공지능(AI)이 왜 도입되었는지, 어떻게 적용되어 무엇을 이루었는지, 무엇이 남았는지를 세 질문 순서대로 정리한다. 표의 '검증상태' 열과 괄호 안의 원문확인·언론·기업주장·미확인 표기는 출처 신뢰도를 뜻한다(부록 A).

## 한눈에 보기

| 질문 | 핵심 답 |
|---|---|
| **1. AI는 왜 도입되었나** | 손가락 소재는 부드러워서 접촉 면적과 감도를 확보해야 하고, 동시에 수천~수백만 회의 파지를 견뎌야 한다. 그런데 엘라스토머의 비선형성·히스테리시스·크리프·드리프트, 비싸고 수렴이 어려운 FEM, 쿨롱 법칙이 맞지 않는 손끝 마찰, 고차원인 소재-형상-제어 설계공간 때문에 물리모델과 시행착오만으로는 설계와 보정이 감당되지 않았다. AI는 이 비이상성을 데이터로 흡수하는 수단으로 들어왔다. |
| **2. 어떻게 적용되었고 무엇을 이끌었나** | 배합 대리모델, FEM 대리모델·역설계, 형태-소재-제어 공동설계, 촉각 신호 해석, 촉각 파운데이션 모델, sim-to-real, 센서 광학·젤 설계, 접착 표면 설계, 힘줄 모델링의 아홉 방식으로 쓰였다. 대표 성과로는 실험 배합 33개로 600% 넘게 늘어나는 프린팅 엘라스토머(KAIST·KIST), 0.8초 만에 손가락 형상을 생성해 성공률을 31.5% 높인 확산모델(DGDM), 기존 설계보다 접착력이 최대 77% 높은 게코형 섬유(BO), sim-to-real 격차를 41% 줄인 트랜스포머 힘줄 모델이 있다. |
| **3. 남은 문제와 해결 방향** | 수명 데이터가 10³~10⁴회 규모에 머물고, 센서 개체 편차와 드리프트 때문에 재보정이 반복되며, 데이터는 카메라 기반 촉각에 편중되어 있다. 시뮬레이터는 점탄성과 마모를 반영하지 못하고, 소재를 합성해 피부로 만들고 촉각·수명까지 시험하는 폐루프는 없다. 표준 내구·감도 프로토콜, 마모·실패 데이터 공개, 센서 불변 표현, real-to-sim 소재 식별, 자동 제조와 자동 수명시험의 결합이 해법이다. |

**핵심 시사점**

1. AI가 로봇 손가락에서 실제로 기여한 일은 새 소재의 발견이 아니다. **이미 쓰는 실리콘·우레탄·TPU·고분자 섬유의 비선형 거동을 데이터로 길들이고, 그 위에서 형상·강성 분포·제어를 함께 최적화하며, 촉각 신호를 해석하는 일**이었다.
2. 인과가 반대 방향으로도 흐른다. **학습 기반 조작이 손가락 소재 선택을 바꾸고 있다.** 연구용 손은 정책 학습의 데이터 수집을 견디도록 소재를 배치하고, 기업은 시판 촉각 센서의 내구성 부족을 이유로 센서를 직접 만든다.
3. 가장 약한 고리는 **수명**이다. 실리콘 촉각 젤은 15 N 반복하중에서 250~500회 만에 뚫렸다. 그런데 손끝 피부의 마모·피로 수명을 ML로 예측한 1차 연구는 찾지 못했다.
4. 2026년 11월 현재 **손가락 피부 소재를 자동으로 합성하고 촉각 성능과 수명까지 시험하는 폐루프 실험실은 없다.** 자동 수명시험과 자동 기계시험이 따로 시연된 단계다.
5. 이 분야의 수치는 원문과 보도가 자주 엇갈린다(서울대 83% 대 95%, SuperTac 8.5B 대 850M, 기업의 "백만 회·20억 회" 내구 주장). **인용 전에 원문 대조가 필수다.**

---

## 0. 조사 범위와 로봇 손가락 소재 구성

**범위:** 이 보고서는 다관절 로봇 손과 소프트 그리퍼의 "손가락"을 이루는 소재(손끝 패드·피부, 촉각 센싱 소재, 소프트 손가락 엘라스토머, 관절·플렉셔, 링크, 힘줄, 마찰·접착 표면, 구동 소재, 자가치유 소재)만 다루고, 감속기·모터·배터리 같은 로봇 일반 소재는 제외한다. 학습 기반 조작 정책은 소재의 요구 특성을 바꾸는 범위에서만 짧게 다룬다(2-2 g).

아래 표가 1~3장의 공통 틀이다. 공개 사양이 많은 연구용 손(LEAP, ORCA, CRAFT)은 **강체 PLA 링크 + 실리콘·TPU 연질부 + 고분자 섬유 힘줄** 조합으로 수렴했다. 반면 상용 손(Shadow, Allegro, Unitree, Figure, Sanctuary, Tesla)은 감지 성능만 밝히고 **손끝·패드 소재명, Shore 경도, 마찰계수는 대부분 공개하지 않는다** ([Shadow Hand](https://www.shadowrobot.com/dexterous-hand-series/); [Allegro Hand](https://www.allegrohand.com/); [Unitree Dex5-1](https://www.unitree.com/Dex5-1); [Sanctuary 유압 손](https://sanctuary.ai/solutions/hydraulic-hands/); [Tesla Optimus 손, Electrek 2024](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/)).

| 부위 | 대표 소재(연구용 · 상용) | 역할 | 요구 특성(수치) | 알려진 고장 모드 |
|---|---|---|---|---|
| 손끝 패드·피부 | 연구: 실리콘 주조 피부(ORCA) ([ORCA, arXiv 2504.04259](https://arxiv.org/html/2504.04259)), "soft rubber" 손끝(LEAP) ([LEAP Hand, arXiv 2309.06440](https://ar5iv.labs.arxiv.org/html/2309.06440)), Dragon Skin 30 외피 ([Liu & Howe, NSF PAR](https://par.nsf.gov/servlets/purl/10485527)) · 상용: Figure 03 "더 부드러운 손끝"(소재 비공개) | 접촉 면적 확보, 마찰, 센서 보호 | 순응성과 인열·접착 강도의 균형 | ORCA 손끝 5개 중 2개에서 **약 2,000~4,000회 파지 후** 피부가 열화해 피부와 FSR 사이에 공극이 생기고 감지 임계값이 올라갔다. 손끝 3개에서는 0.2 mm 구리 신호선이 끊어졌다 ([ORCA](https://arxiv.org/html/2504.04259), 원문확인) |
| 비전기반 촉각 젤 | 연구: 투명 실리콘 Solaris(Shore A15) 기저층 + EcoFlex 00-10 전사층, 비교군 폴리우레탄 Clear Flex 50(Shore A50) + VytaFlex 40 ([VBTS 내구성 벤치마크, arXiv 2511.07797](https://arxiv.org/html/2511.07797v1)) · 상용: GelSight Mini 젤 두께 4.25 ± 0.20 mm ([GelSight Mini 데이터시트](https://pdf.directindustry.com/pdf/gelsight-inc/gelsight-mini/4602322-1082169.html), 기업주장) | 접촉 변형을 카메라 영상으로 변환 | 투명도, 낮은 경도(감도), 얇은 반사 코팅 | 4 mm 구형 압자로 15 N을 반복하면 실리콘 시편 2개가 **250~500회** 사이에 뚫리거나 찢어졌다. PU는 **1,000회** 동안 판독값이 거의 변하지 않았다. 연마 시험에서 실리콘 전사층은 보통 2 m 안에 찢어졌다. 전사층 마모와 실리콘-아크릴 창 박리가 대표 고장이다 ([arXiv 2511.07797](https://arxiv.org/html/2511.07797v1), 원문확인) |
| 전자피부·자기피부 | 연구: 자성 입자 엘라스토머(ReSkin·AnySkin), 두께 0.5 mm 자화 필름 + 홀 센서, Ag/CuOx 멤리스티브 나노와이어, FSR 박막 · 상용: Unitree Dex5-1 압력센서 94개(감지 10~2,500 g), Shadow STF | 힘·위치·온도·미끄럼 감지 | 감도, 낮은 히스테리시스, 교체·재보정 용이성 | 히스테리시스·드리프트·개체 편차. 교체한 피부는 재보정해야 한다(3-1) |
| 소프트 손가락 엘라스토머 | Ecoflex 00-30(Shore 00-30, 파단연신율 약 900%) ([Smooth-On](https://www.smooth-on.com/compare/4922/4985/ecoflex-00-20--ecoflex-00-30/), 미확인), Dragon Skin 30(Shore A30, 인장 3.45 MPa, 연신율 약 364%) ([FormX](https://www.formx.eu/p/product/dragon-skin-30/skin30x/), 미확인), DLP 아크릴레이트 엘라스토머 | 굽힘 구동, 순응 파지 | 대변형, 낮은 잔류변형, 피로 수명 | 공압 소프트 액추에이터는 재료 피로·박리·마모로 열화한다 ([HKUST 내구성 리뷰 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)). 반복 대변형 뒤 잔류변형이 남는다(2-2 b) |
| 관절·플렉셔 | TPU 관절(CRAFT) ([CRAFT, arXiv 2603.12120](https://arxiv.org/html/2603.12120v1)), TPU 95A Fin-Ray(영률 26 MPa) ([Deng & Li, Front. Robot. AI 2021](https://www.frontiersin.org/articles/10.3389/frobt.2020.590076/full)) | 충격과 접촉 불확실성 흡수 | 굽힘 피로 수명, 예측 가능한 굽힘 분배 | 반복 굽힘으로 피로가 쌓여 결국 파단된다. 힘줄 하나가 PIP·DIP 관절을 함께 당기면 하중과 자세에 따라 굽힘 분배가 달라진다 ([CRAFT](https://arxiv.org/html/2603.12120v1), 원문확인) |
| 링크 | FDM PLA(ORCA·CRAFT), 3D 프린팅 손(LEAP) · 상용: 금속 골격(Inspire RH56, 리셀러 표기) ([Knox Labs](https://www.knoxlabs.com/products/inspire-robots-rh56f1-dexterous-hand), 미확인) | 하중 경로와 기하 예측성 | 강성, 현장 수리성 | 힘줄이 PLA에 직접 닿으면 마모된다. ORCA는 금속 핀으로 힘줄 경로를 우회했다 |
| 힘줄 | 지름 0.4 mm 나일론 꼰줄 2가닥(ORCA), UHMWPE(Dyneema), 아라미드, 강선 | 원격 구동력 전달 | 저크리프, 굴곡 피로, 저마찰 | 마찰 누적, 마모, 시간에 따른 느슨해짐(slack)이 생긴다(ORCA). UHMWPE는 크리프로 늘어나 보정이 깨지고, 아라미드는 풀리 접촉부에서 빨리 마모되며, 강선은 작은 굽힘 반경에서 피로 균열이 생긴다 ([humanoid.guide 힘줄](https://humanoid.guide/?p=16664), 2차) |
| 마찰·접착 표면 | Sylgard 170 게코형 미세쐐기(쐐기 높이 46 µm) ([Stanford Daily 2023](https://stanforddaily.com/2023/02/01/lab-develops-stickiest-non-sticky-material/), 미확인), 전기접착 전극, 입자 재밍 막 | 파지력과 미끄럼 억제 | 접착·전단력, 마찰 안정성 | 재밍 그리퍼는 마찰·흡착·기계적 맞물림으로 잡는다 ([Brown et al., PNAS 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2973877/)). 손끝 마찰계수가 장기간 어떻게 열화하는지 측정한 데이터는 찾지 못했다 |
| 구동 소재(인공근육) | 대부분 모터 + 힘줄. 연구: Peano-HASEL, 꼬임 고분자(TCP), 인간 근조직 | 손가락 굽힘 구동 | 힘, 변형률, 속도, 사이클 수명 | 바이오하이브리드 손은 힘이 mN 수준이고 액체 속에서만 작동한다(2-2 f) |
| 자가치유 소재 | Diels-Alder(DA) 열가역 고분자(VUB) | 절단·천공 복구 | 치유 온도, 치유 후 강도 | 기존 DA는 치유에 80~90 °C가 필요하다 ([VUB, Soft Robotics 2020](https://biblio.vub.ac.be/vubirfiles/55950627/soro.2019.0081.pdf), 미확인). 센서 섬유를 넣은 치유형 피부는 재접촉이 불충분하면 섬유가 영구 손실된다 ([Adv. Intell. Syst. 2022](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d), 미확인) |

LEAP 손끝 소재는 출처가 엇갈린다. 논문은 "soft rubber fingertips"라고 썼지만, 커뮤니티 위키는 TPU/NinjaFlex로 적었다 ([LEAP 위키](https://web-3kk.pages.dev/en/knowledge/hardware/hands/leap-hand), 미확인). 이 보고서는 논문 표현을 따른다.

---

## 1. 인공지능은 왜 도입되었나

**답:** 손가락 소재는 "부드러움"과 "질김"이라는 상충하는 요구를 동시에 받는다. 그런데 연질재료의 거동, 접촉·마찰, 촉각 신호가 모두 비선형이고 확률적이어서 기존의 해석모델·FEM·시행착오로는 설계와 보정의 비용이 감당되지 않았다. AI는 이 비이상성을 데이터로 학습해 예측·보정·역설계·해석을 싸게 만들기 때문에 도입되었다.

### 1-1. 손가락 소재에 요구되는 특성

손가락 소재에 대한 요구는 서로 부딪치는 특성의 묶음이다.

| 요구 특성 | 왜 중요한가 | 근거 |
|---|---|---|
| 순응성·접촉 면적 | 부드러운 손끝은 접촉 면적을 넓혀 파지를 안정시킨다. Figure는 03 손의 손끝을 더 부드럽고 적응적으로 바꿨다 | ([Figure 03 공개 2025](https://www.figure.ai/news/introducing-figure-03), 기업주장) |
| 고감도 | 사람 손끝 수준의 힘 감지가 목표다. Figure는 손끝 센서가 **3 g**을 감지한다고 했고, Sanctuary는 손가락 패드에서 **5 mN**을 감지한다고 보도됐다. 연구용 Digit 360의 법선력 분해능은 **1.01 mN**이다. 측정 조건이 달라 직접 비교할 수는 없다 | ([Figure 03](https://www.figure.ai/news/introducing-figure-03), 기업주장; [Sanctuary 발표, BusinessWire](https://www.businesswire.com/news/home/20250226807548/en); [The Rundown](https://robotnews.therundown.ai/p/sanctuarys-touchy-feely-humanoid), 언론; [Digit 360, arXiv 2411.02479](https://arxiv.org/abs/2411.02479)) |
| 내구성 | 감도를 위해 부드럽게 만들수록 빨리 닳는다. 병뚜껑을 조이는 과제에서 실리콘 젤은 16회 만에 찢어졌고 PU 젤은 50회를 모두 마쳤다. 대신 PU는 낮은 하중에서 감도가 떨어지고 유효 힘 범위가 넓어진다 | ([arXiv 2511.07797](https://arxiv.org/html/2511.07797v1), 원문확인) |
| 학습 데이터 수집 내성 | 학습 정책용 손은 정책이 기대하는 곳에 접촉할 만큼 정확하면서, 데이터 수집 중 피할 수 없는 충돌·미끄럼을 견뎌야 한다. LEAP은 "ML용 손 하드웨어는 내구성·반복성·다용도성을 갖춰야 한다"고 썼다 | ([CRAFT](https://arxiv.org/html/2603.12120v1); [LEAP](https://ar5iv.labs.arxiv.org/html/2309.06440)) |
| 교체·재보정 용이성 | 연성 센서는 등각 접촉을 하기 때문에 빨리 열화하고, 시간과 시편에 따라 응답이 달라진다. 그래서 닳은 피부만 바꿔 끼우는 구조가 요구된다 | ([ReSkin, arXiv 2111.00071](https://arxiv.org/abs/2111.00071), 원문확인) |

Figure가 촉각 센서를 직접 개발한 이유도 "시판 센서가 실사용 내구성을 견디지 못했다"는 것이었다 ([Figure 03](https://www.figure.ai/news/introducing-figure-03)). 감도와 내구성의 상충은 연구실과 기업 모두가 겪는 핵심 문제다.

### 1-2. 기존 방식(물리모델·FEM·시행착오)의 한계

위 요구를 기존 방식으로 맞추려 하면 일곱 가지 벽에 부딪힌다.

1. **비선형·히스테리시스·크리프·드리프트.** PLoS ONE 리뷰는 "구조적 순응성과 재료의 점탄성이 비선형성과 히스테리시스로 복잡하고 예측 불가능한 거동을 만든다"고 쓰고, "크리프, 드리프트, 높은 자유도가 히스테리시스를 키워 소프트 그리퍼 모델링과 소프트 센서 보정을 어렵게 한다"고 지적했다 ([Kim et al., PLoS ONE 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/), 원문확인).
2. **FEM의 비용과 수렴 문제.** FEM은 비선형 탄성재료와 복잡한 구조를 시뮬레이션할 수 있지만 "계산 비용이 크고 수렴 문제가 생길 수 있다" ([Fin-Ray NN 최적화, arXiv 2506.00494](https://arxiv.org/abs/2506.00494), 원문확인). 같은 논문은 Fin-Ray 설계를 직접 탐색하려면 FEM이 약 50,000회 필요하다고 언급한다(미확인).
3. **접촉·마찰 모델링의 어려움.** 엘라스토머(Dragon Skin 30) 손끝의 마찰은 수직력과 미끄럼 속도에 강하게 의존하고 큰 확률적 성분을 가진다. 그래서 마찰계수를 상수로 보는 쿨롱 모델은 실제 두 번째 미끄럼을 "완전히 놓쳤다" ([Liu & Howe](https://par.nsf.gov/servlets/purl/10485527), 원문확인). 촉각 피부를 시뮬레이션하려면 점 접촉이 아니라 접촉 패치를 모델링해야 하는데, 강체 시뮬레이터가 주는 침투 깊이는 부정확해 힘 평형으로 다시 계산해야 했다 ([Kasolowsky & Bäuml, arXiv 2409.12735](https://arxiv.org/html/2409.12735)). 강체 접촉, 페널티 소프트 접촉, 하이드로엘라스틱 근사는 모두 전단이 중요한 작업에서 sim-to-real 격차를 메우지 못했다 ([HydroShear, RSS 2026](https://roboticsproceedings.org/rss22/p155.pdf)).
4. **소재-형상-제어 공동설계 공간의 고차원성.** 설계와 제어를 함께 탐색하는 공간은 "고차원이고 고도로 비선형"이다. 게다가 설계는 제조 시점에 정해지고 제어는 실시간으로 바뀌어 시간 척도가 다르다. 기존 계산 설계는 비싸고 새 물체로 일반화하기 어렵다 ([Yi et al., arXiv 2505.20404](https://arxiv.org/abs/2505.20404), 원문확인).
5. **촉각 신호의 고차원성과 노이즈.** 촉각 센서 신호는 "노이즈가 많고 고차원이며, 필수 정보와 무관한 정보가 섞여 있다" ([Sensors 2017 리뷰](https://pmc.ncbi.nlm.nih.gov/articles/PMC5713637)). 비평면 손가락에 taxel이 넓게 퍼지면 공간 보정이 특히 어렵고, 여러 센서에 두루 통하는 자율 보정법은 아직 없다 ([촉각 데이터 표현 리뷰, arXiv 2510.10804](https://arxiv.org/html/2510.10804v1)).
6. **수작업 시행착오 설계.** "대부분의 소프트 로봇 설계는 시행착오로 수작업 생성된다" ([SoRoForge 2023](https://matterassembly.org/publications/smith2023soroforge/), 원문확인). 노동집약적인 다단계 주조 공정의 제약이 설계공간 자체를 좁힌다는 지적도 있다(같은 그룹 2021, 미확인).
7. **제조사 데이터시트만으로는 소재를 고를 수 없다.** UCL 연구진은 "초탄성 재료는 제조사 데이터시트만으로 선택할 수 없다"고 결론짓고 대변형 인장시험으로 구성모델 DB를 만들었다. 그러나 점탄성과 Mullins 효과는 다루지 못했다 ([Marechal et al.](https://discovery.ucl.ac.uk/10112846/1/Towards_a_Common_Framework_and_Database_of_Materials_for_Soft_Robotics___Revision2.pdf), 원문확인).

여기에 수명 시험의 비용이 겹친다. 피부 열화나 젤 천공은 수백~수천 회를 실제로 눌러 봐야 드러나므로 시행착오 한 번이 비싸다(0장 표). 다만 "내구 시험이 느려서 ML을 도입했다"고 명시한 리뷰 문장은 찾지 못했다. 이 부분은 1차 시험 설계에서 끌어낸 추론이다.

### 1-3. 그래서 AI가 제공하는 것

AI는 1-2의 한계마다 대응하는 기능을 제공한다.

| 한계 | AI의 역할 | 근거 |
|---|---|---|
| 비선형·히스테리시스 | 데이터 기반 보정·모델링 | ML은 "해석·실험 접근으로 쉽게 표현되지 않는 비선형성과 히스테리시스를 고려해 소프트 센서를 정확히 보정"하며, 딥러닝이 비딥러닝 접근보다 성능이 좋았다고 보고됐다 ([Kim et al., PLoS ONE 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/), 원문확인) |
| FEM 비용·수렴 | FEM 대리모델 | FEM 데이터로 학습한 신경망이 접촉력과 변형을 FEM과 비슷한 정확도로 계산했고, 물리정보신경망(PINN)에 실측을 더하면 FEM보다 정확했다는 선행연구가 있다 ([arXiv 2506.00494](https://arxiv.org/abs/2506.00494), 원문확인) |
| 접촉·마찰 | 회귀형 마찰 모델, 데이터로 정렬한 sim-to-real | Liu & Howe는 µ = β0 + β1·v + β2·Fn + ε 회귀식을 단일 미끄럼 스트로크에서 추정했다. 데이터가 Fn–v 공간을 넓게 덮을수록 추정 분산이 줄었다 ([Liu & Howe](https://par.nsf.gov/servlets/purl/10485527), 원문확인). HydroShear는 전단 시뮬레이션으로 제로샷 촉각 강화학습을 했다 |
| 고차원 공동설계 | 미분 가능한 신경 대리모델, 확산·진화 탐색 | Yi et al.은 빠르고 미분 가능한 "neural physics" 대리모델로 플렉셔 손가락의 블록별 강성 분포와 파지 자세를 함께 최적화했다 ([arXiv 2505.20404](https://arxiv.org/abs/2505.20404), 원문확인) |
| 촉각 신호 | 학습 디코더 | 9DTact는 물체 175개에서 이미지-힘 약 10만 쌍을 모아 마커 없이 3D 형상과 6D 힘을 복원했고, 처음 보는 물체에도 일반화했다 ([9DTact, arXiv 2308.14277](https://arxiv.org/abs/2308.14277), 원문확인) |
| 수작업 시행착오 | 생성·진화 설계 + 자동 제작 | SoRoForge는 유전 알고리즘, 생성적 인코딩, FEM, 다재료 적층제조를 묶어 사용자 지정 성능의 액추에이터를 생성했다 ([SoRoForge](https://matterassembly.org/publications/smith2023soroforge/), 원문확인) |
| 데이터시트 부족·제조 편차 | 소량 실험 대리모델, 편차를 흡수하는 응답 모델 | ReSkin은 제조 편차와 시간 변화에 강건한 응답 모델을 학습하고, 자기지도 학습으로 적은 데이터만으로 미세 보정한다 ([ReSkin](https://arxiv.org/abs/2111.00071), 원문확인). 배합 대리모델 사례는 2-1에서 다룬다 |

"AI가 소재 설계를 돕는다"는 방향과 "학습 기반 조작이 소재 요구를 바꾼다"는 방향은 구분해야 한다. 후자의 예로 CRAFT는 정확성과 강건성의 긴장을 강체 PLA 링크와 TPU 관절의 배치로 풀었다(0장 표). Sanctuary는 촉각 센서가 "더 풍부한 행동 데이터"를 만든다고 강조한다 ([Sanctuary](https://sanctuary.ai/solutions/hydraulic-hands/), 기업주장). 손끝 소재가 학습 데이터를 생성하는 장치로 취급되기 시작했다는 뜻이다. Tesla·Figure·Sanctuary가 소재 설계 자체에 AI를 쓴다는 공개 근거는 없고, 이들이 공개한 AI 활용은 제어와 정책 학습 쪽이다.

---

## 2. 어떻게 적용되었고 어떤 진전을 이끌었나

**답:** AI는 아홉 가지 방식으로 손가락 소재에 적용되었다. 정량 성과가 가장 뚜렷한 곳은 촉각 신호 해석과 시뮬레이션, 그리고 FEM 대리모델 기반의 형상·강성 설계다. 소재 배합 자체를 ML로 설계한 사례는 2026년에야 처음 나왔다.

### 2-1. AI 적용 방식 유형

| 방식 | 원리 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|---|
| 소재 배합 대리모델·최적화 | 소량 배합 실험으로 물성 회귀모델을 학습하고, 상충하는 물성을 함께 만족하는 배합을 고른다 | KAIST·KIST·서울과기대 DLP 엘라스토머 ([Song et al., Nat. Commun. 17, 7167, 2026](https://www.nature.com/articles/s41467-026-73735-4)) | **배합 33개**로 학습해 PUDA:IBOA:EHMA:MAA = 50:30:16:4 wt%를 추천했다. 점도는 약 2,500 mPa·s로 DLP 기준(5,000 mPa·s 미만)을 만족했고, **파단연신율은 600%를 넘었다** | 원문확인 |
| FEM 대리모델·형상 역설계 | FEM 데이터로 학습한 신경망을 최적화기 안에 넣어 목표 변형에 맞는 형상을 역산한다 | SPADA, 벨로우즈형 공압 손가락 ([SPADA, arXiv 2305.19509](https://arxiv.org/abs/2305.19509)) | ANN 대리모델 + 유전 알고리즘 + 조각별 일정곡률 분할. 2D 목표 형상 정합 RMSE 4.16, 2.70, 2.51 mm. 오픈소스 GUI로 공개 | 원문확인 |
| 형태-소재-제어 공동설계 | 확산모델 생성을 동역학 네트워크의 기울기로 유도하거나, 형태 조건부 정책으로 설계를 평가한다 | DGDM ([DGDM, arXiv 2402.15038](https://arxiv.org/abs/2402.15038)) | 설계 하나를 **0.8초**에 생성한다. 성공률이 최적화 기준선보다 **31.5%**, 유도 없는 확산보다 **45.3%** 높았다 | 원문확인 |
| 촉각 신호 해석·힘 추정 | 결합된 비선형 신호를 학습 모델로 분리하고 taxel 간격보다 세밀한 위치를 추정한다 | 자기 피부(CityU·HKU·CMU) ([Yan et al., Sci. Robot. 2021](https://pubmed.ncbi.nlm.nih.gov/34043530/)) | 두께 약 0.5 mm 정현파 자화 필름 + 홀 센서. 단일 유닛이 법선력과 전단력을 스스로 분리하고, 딥러닝으로 **초해상 정확도를 60배** 높였다 | 원문확인(초록) |
| 촉각 파운데이션 모델 | 라벨 없는 대규모 촉각 영상으로 자기지도 사전학습해 센서와 과제에 두루 쓰는 인코더를 만든다 | Sparsh(Meta) ([Sparsh, arXiv 2410.24090](https://arxiv.org/abs/2410.24090)) | 촉각 영상 **46만 장 이상**으로 사전학습했다. 6개 과제의 TacBench 평균에서 과제·센서별 end-to-end 학습보다 **95.1%** 우수했다 | 원문확인 |
| 시뮬레이션·sim-to-real | 젤 광학·변형을 GPU에서 빠르게 렌더링해 강화학습 데이터를 만든다 | TacSL(NVIDIA) ([TacSL, arXiv 2408.06506](https://arxiv.org/abs/2408.06506)) | 촉각 영상과 접촉력 분포 생성이 이전 최고 수준보다 **200배 이상** 빠르다. 비대칭 actor-critic 증류로 실물 전이를 시연했다 | 원문확인 |
| 센서 광학·젤 설계 최적화 | 물리 기반 광학 시뮬레이터를 순환 고리로 삼아 조명·코팅·형상을 목적함수로 최적화한다 | OptiSense Studio(CMU) ([OptiSense, arXiv 2504.14739](https://arxiv.org/abs/2504.14739)) | 광학 부품을 파라미터화하고 일반화 가능한 목적함수 4개를 두었다. GelSight 4종의 초기 설계를 시뮬레이션에서 최적화해 실제 센서로 옮겼다. 딥러닝이 아닌 시뮬레이션 기반 최적화다 | 원문확인 |
| 표면(접착·마찰) 설계 | FEM 접착 역학 위에서 BO로 미세섬유 형상을 탐색하고 미세가공으로 검증한다 | Sitti 그룹 게코형 섬유 ([Son et al., Small 2021](https://doi.org/10.1002/smll.202102867)) | 2광자 중합 마이크로프린팅과 PDMS 이중몰딩으로 제작했다. 매끈한 표면에서 기존 설계보다 건식접착이 **최대 77%** 높았다 | 원문확인(초록) |
| 힘줄 모델링 | 접촉 이력을 입력으로 받는 트랜스포머가 모터 신호에서 힘줄 장력을 예측하고, 이를 시뮬레이터에 넣는다 | 텐던 손가락 sim2real 힘 모델 ([arXiv 2603.04351](https://arxiv.org/abs/2603.04351)) | 예측 오차는 최대 모터 힘의 **3% 이내**다. 시험 궤적의 sim-to-real 격차를 **41%** 줄였고, 실물 손끝 자세 추종을 **50%** 개선했다 | 원문확인(프리프린트) |

방식은 데이터를 얻는 비용을 따라 갈린다. 시뮬레이터가 있는 형상·광학 설계는 FEM 수백~수천 회나 렌더링으로 학습 데이터를 만든다. 실험이 필요한 배합은 수십 개 규모의 소량 회귀가 현재 수준이다. 촉각 해석은 실제로 누르는 데이터가 싸서 수만~수십만 건 규모로 커졌다.

### 2-2. 부위별 진전

#### (a) 손끝 촉각 센싱 소재

**비전기반 촉각 젤. AI는 젤 영상을 힘으로 바꾸는 해석과 시뮬레이션에서 성숙했다. 젤·코팅 설계는 아직 물리 시뮬레이터와 통계적 실험계획 수준이다.**

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 저마모 젤 공정 | DIGIT(Meta) ([DIGIT, arXiv 2005.14679](https://arxiv.org/abs/2005.14679)) | 안료 전사층, Solaris 베이스, Sil-Poxy 접착의 3단계 공정이다. 마모 패스 15회 뒤 투과율 증가가 0.3%로, GelSight Inc. 젤(918%)보다 훨씬 작았다. 딥러닝 컨트롤러로 유리구슬을 조작했다 | 원문확인 |
| 손가락형 고해상 센서의 젤·코팅 설계 | Digit 360 ([arXiv 2411.02479](https://arxiv.org/abs/2411.02479)) | taxel 약 830만 개, 공간 분해능 7 µm. 실험계획법(DoE)으로 감도를 좌우하는 젤·코팅 변수 6개(반경, 두께, 탄성률 등)를 찾았고, 수작업 도장 대신 은 박막 화학증착으로 코팅을 얇게 했다. 반사층 산란 시뮬레이션으로 Lambertian 표면이 최적임을 보였다 | 원문확인 |
| 3D 프린팅 촉각 엘라스토머 역설계 | i-Tac ([i-Tac, arXiv 2604.10692](https://arxiv.org/abs/2604.10692)) | PolyJet 레진 3종의 혼합물 설계로 조성-투명도·경도 응답곡면을 만들고, desirability 다목적 최적화로 목표 물성을 1회 제작에 맞췄다. 딥러닝은 쓰지 않았다 | 원문확인 |
| 센서 간 힘 라벨 재사용 | TransForce ([TransForce, arXiv 2409.09870](https://arxiv.org/abs/2409.09870)) | 조명·마커가 다른 새 센서로 영상을 번역했다. 힘 오차는 x 0.69 N(전 범위의 5.8%), z 1.11 N(6.9%)이었다. 전단에는 마커가, 법선에는 RGB가 유리했다. 젤 마커와 조명 설계가 학습 성능을 직접 좌우한다는 뜻이다 | 원문확인 |
| 소량 보정 광학 시뮬레이터 | Taxim(CMU) ([Taxim, arXiv 2109.04027](https://arxiv.org/abs/2109.04027)); DiffTactile ([DiffTactile, arXiv 2403.08716](https://arxiv.org/abs/2403.08716)) | Taxim은 실제 데이터 100개 미만으로 보정했고 CPU에서 온라인으로 돈다. DiffTactile은 엘라스토머를 FEM 연체로 모델링하고, 실측으로 기울기 기반 물성 보정을 했다 | 원문확인 |
| 대규모 병렬 촉각 시뮬레이션(2026) | TactileLab ([arXiv 2611.07881](https://arxiv.org/abs/2611.07881)); RevoSim(BrainCo) ([arXiv 2611.08939](https://arxiv.org/abs/2611.08939)) | TactileLab은 연체 대신 강체 계산으로 전단 표현을 만들었다. RevoSim은 압저항 taxel 285개와 시각촉각 손끝 5개를 GPU 한 장에서 최대 4,096개 환경으로 돌린다(실물 전이는 향후 과제) | 원문확인(프리프린트) |

GelSight는 2025년 1월 이후 주문분부터 내구성을 "최대 40%" 높인 Mini용 젤을 넣는다고 발표했다. 사내 시험 기준이다 ([Anzu/GelSight 2025](https://www.anzupartners.com/2025/01/06/gelsight-extends-life-and-durability-of-gelsight-mini-with-new-gels/), 기업주장). 대조 사례도 있다. 교류 전계발광(ACEL) 촉각 영상 소자는 다공성 유전체의 기공 크기를 조절해 공간 강도 편차를 약 9배 줄이고 100 µm 특징까지 영상화했다. AI 없이 소재 공학만으로 계산 복원 단계를 없앤 것이다 ([ACEL, arXiv 2611.19384](https://arxiv.org/abs/2611.19384)). 젤 경도·마커 패턴을 딥 생성모델이나 BO로 설계한 원문은 찾지 못했다.

**전자피부·자기피부. "소재는 싸고 교체 가능하게, 편차는 ML로 흡수"하는 방식이 가장 분명하게 실증되었다.**

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 교체형 자기 피부 | ReSkin(Meta·CMU) ([ReSkin](https://arxiv.org/abs/2111.00071)) | 전자 회로와 자성 입자 엘라스토머 피부를 분리했다. 5만 회 넘는 상호작용을 견디고, 새 피부에 약 200회만 눌러 라벨 없이 적응한다고 보고됐다 ([Meta 블로그](https://ai.meta.com/blog/reskin-a-versatile-replaceable-low-cost-skin-for-ai-research-on-tactile-perception/)) | 원문확인 / 수치는 기업 블로그 |
| 무보정 교체 피부 | AnySkin(NYU·Meta) ([AnySkin, arXiv 2409.08276](https://arxiv.org/html/2409.08276v3)) | 접착제 없이 교체한다. LSTM 슬립 예측은 처음 보는 물체에서 92%였다. 플러그 삽입 과제에서 피부를 바꾸면 정책 성능이 **AnySkin은 13%, ReSkin은 43%** 떨어졌다. DIGIT 기반 정책은 이 정밀 과제에서 성공률이 낮았다 | 원문확인 |
| 자기 피부 초해상 | 2-1 참조. 그리퍼 손끝에 장착해 외란 속에서 깨지기 쉬운 물체를 잡았고, 원격조작으로 바늘에 실을 꿰었다 | 2-1 참조 | 원문확인 |
| 단일 소자 다중모드 | 서울대 고승환 그룹, Ag 코어/CuOx 셸 멤리스티브 나노와이어 ([Kim et al., Nature Materials 2025](https://www.nature.com/articles/s41563-025-02373-w)) | 나노와이어 망 하나가 열·기계 감지를 16 Hz로 전환한다. 손끝 센서 1개와 ML로 생활용품 **20종을 83%** 정확도로 식별했다. **수치 충돌:** 보도는 "단일 모드 약 65%에서 결합 약 95%"라고 했다 ([ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing)). 이 보고서는 원문 초록의 83%를 쓴다 | 원문확인 / 95%는 언론 |
| 광학·마찰전기·관성 융합 피부 | SuperTac, 칭화대 등 ([SuperTac, Nature Sensors 2026](https://www.nature.com/articles/s44460-025-00006-y); [저자 공개 원고](https://linqi-ye.github.io/docs/NATSENSORS.pdf)) | 두께 1 mm 광장 변조 피부(전도성 고분자·형광·반사·지지층)다. 힘 정확도 0.06 N, 위치 0.4 mm, 질감·재질·미끄럼·색 판별 94% 이상, 점자 26자 100%. 단, 로봇 통합 시연에서는 3지 손의 **손끝이 아니라 손바닥에** 장착했다. **수치 충돌:** 촉각 언어모델 DOVE의 파라미터 수가 논문에는 8.5B, 일부 보도에는 850M이다 ([Gizmochina 2026](https://www.gizmochina.com/2026/01/21/chinas-supertac-sensor-enables-human-like-touch-in-humanoid-robots/)) | 원문확인 / 850M은 언론 |
| 3D 구조 피부 | 칭화대 3DAE-Skin ([Liu et al., Science 2024](https://pubmed.ncbi.nlm.nih.gov/38815009/)) | 법선력·전단력·변형을 분리해 측정하고, 접촉만으로 물체의 탄성률과 곡률을 잰다. 초록에는 ML이 명시되어 있지 않다 | 원문확인(초록) |

**AI가 센서 소재·구조를 설계한 사례. "소량 데이터 + 능동학습 + 다목적 최적화" 패턴으로 수렴하고 있다.**

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 인공피부 미세구조 역설계 | 소량 데이터 ML 역설계 ([arXiv 2304.04609](https://arxiv.org/abs/2304.04609)) | 신호 포화를 넘어 선형 응답을 내는 기둥형 미세구조 해 수백 개를 수 시간 안에 예측했다. 종합 효율이 정방향 시행착오보다 최소 4자릿수 높았다 | 원문확인(프리프린트) |
| 압력센서 맞춤 역설계 | Wang et al. ([Adv. Sci. 2026](https://europepmc.org/search?query=DOI%3A10.1002%2Fadvs.202524250)) | SVM으로 실현 가능 경계를 정하고 2단계 능동학습을 결합했다. 감도 **1.2 V/kPa**, 선형성 **R² 0.999**, 범위 **0~400 kPa**로 고감도와 넓은 선형 범위의 상충을 동시에 풀었다. 로봇 파지에도 적용했다 | 원문확인(초록) |
| taxel 배치 | "Which Taxels, Not How Many" ([arXiv 2611.10647](https://arxiv.org/abs/2611.10647)) | 로봇 손 3종에서 접촉 통계로 고른 소수 taxel이 훨씬 큰 균일 배치와 같은 성능을 냈다. 드물게 닿는 위치의 taxel은 없는 것과 같았다 | 원문확인(프리프린트) |

Wang et al.의 대상은 평판형 압력 패드다. 곡면 손끝 형상까지 역설계한 실증은 확인하지 못했다.

#### (b) 소프트 손가락 소재·구조

**배합 수준의 ML은 KAIST 1건이 사실상 전부이고, 구조 수준(FEM 대리모델 + 최적화)은 표준 파이프라인이 되었다.**

KAIST·KIST·서울과기대 연구(2-1)의 핵심 기법은 소량 몰드 경화로 물성을 측정해 "프린팅 제약과 물성 측정을 분리"한 것이다. 인쇄할 수 없는 고점도 배합도 일부러 넣어 모델이 인쇄 가능 경계를 학습하게 했다. PUDA를 80 wt% 넣은 배합은 점도가 약 3.5×10⁴ mPa·s여서 인쇄할 수 없었다. 교차검증 R²는 점도 0.870±0.052, 탄성률 0.768±0.149였다. 반면 **연신율은 0.645±0.374로 가장 낮았다.** 200% 변형 100사이클에서 잔류변형은 약 10사이클 뒤 약 30%로 안정되었다. 그리퍼는 물을 채운 **1 kg 병**을 들고, 달걀·유리병·컴퓨터 마우스를 흔들어도 놓치지 않았다 ([Song et al., Nat. Commun. 2026](https://www.nature.com/articles/s41467-026-73735-4), 원문확인).

이 연구는 **베이지안 최적화(BO)가 아니다.** 저자들은 GP 대리모델과 BO를 향후 과제로 명시했다. 학습 데이터는 33개이고 교차검증에는 기준 배합 3개를 더한 36개를 썼다. 일부 언론은 "1 kg"을 "1리터 병"으로 적었다 ([Interesting Engineering](https://interestingengineering.com/ai-robotics/soft-robotic-hand-grips-fragile-eggs), 언론).

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 축소차수 대리 관절모델 | Yao·Howard·Maiolino ([arXiv 2603.19794](https://arxiv.org/abs/2603.19794)) | 고충실도 FEM에서 만든 대리 관절모델을 의사강체모델에 넣었다. 벨로우즈 손가락과 텐던 소프트 손가락에서 sim-to-real을 검증했다. 초록에 수치는 없다 | 원문확인 |
| Fin-Ray MLP + 다목적 최적화 | Ghanizadeh 외 ([arXiv 2506.00494](https://arxiv.org/abs/2506.00494)) | FEM 120회로 MLP를 학습하고, NSGA-II로 접촉력과 팁 변위의 파레토 해를 구했다. 시뮬레이션 중심이다 | 원문확인 |
| Fin-Ray 다목적 BO | Fin-Bayes(CSIRO 계열) ([Canberra 포털](https://researchprofiles.canberra.edu.au/en/publications/fin-bayes-a-multi-objective-bayesian-optimization-framework-for-s/)) | 형상·재료·접촉 비선형 FEM 위에서 순응성과 접촉력을 함께 최적화하고, 자동 시험 리그로 검증했다. 게재지·연도는 확인하지 못했다 | 원문확인(초록 일부) |
| 품질다양성 탐색 | Fin-QD ([arXiv 2311.12477](https://arxiv.org/abs/2311.12477)); MAP-Elites 위상최적화 ([arXiv 2407.07591](https://arxiv.org/abs/2407.07591)) | 설계변수 28개 공간에서 SOFA 접촉 FEM과 MAP-Elites로 물체별 그리퍼를 생성했다. 후자는 공극 위치·크기를 진화시켜 파지를 개선했다 | 원문확인 |
| 학습 기반 형상 품질함수 | Deng & Li ([Front. Robot. AI 2021](https://www.frontiersin.org/articles/10.3389/frobt.2020.590076/full)) | 감김수(winding number) 기반 파지 품질함수로 TPU 95A Fin-Ray 형상을 최적화했다 | 원문확인 |
| 메타물질 메커니즘 | 심층 강화학습 설계 ([arXiv 2408.04376](https://arxiv.org/abs/2408.04376)) | 셀·힌지로 이산화한 영역에서 FEA 기반 RL을 했다. 인간 설계보다 보상이 3배였고, 소프트 그리퍼 메커니즘으로 확장해 실험 검증했다 | 원문확인 |
| 경사 격자 손가락 | TU Delft ([arXiv 2501.03763](https://arxiv.org/abs/2501.03763)) | 복셀 크기와 단위셀로 강성을 조정한 격자 손가락을 한 번에 인쇄했다. 최적화에 ML을 썼는지는 초록에 없다 | 원문확인 |

다중소재 프린팅도 진전했지만 AI 설계와는 구별해야 한다. 비전 제어 젯팅(Vision-controlled jetting)은 스캐닝 피드백으로 기계식 평탄화기를 없애 천천히 경화되는 티올-엔 계열까지 쓸 수 있게 했고, 뼈·인대·힘줄을 갖춘 손을 한 번에 인쇄했다 ([Buchner et al., Nature 2023](https://www.nature.com/articles/s41586-023-06684-3), 원문확인). 이 피드백은 공정 비전 제어다. 가변강성 손가락은 공백이다. 인듐-주석 LMPA(융점 47 °C)와 전기접착을 결합한 공압 손가락이 있지만 ML은 쓰지 않았다 ([Polymers 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9657554/), 미확인). 재밍·SMP 손가락에 ML을 적용한 사례는 찾지 못했다.

#### (c) 손 형태 공동설계

**공동설계의 병목은 계산에서 제작과 sim-to-real로 옮겨갔다. 다만 대부분은 형상·기구학만 설계하고 소재 변수는 일부에만 들어간다.**

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 센서 없는 손가락 형상 생성 | DGDM(2-1) | 2-1 참조 | 원문확인 |
| 다지 손 교차형태 공동설계 | House of Dextra ([arXiv 2512.03743](https://arxiv.org/abs/2512.03743), ICLR 2026) | 관절·손가락·손바닥까지 생성하고 형태 조건부 정책으로 평가한다. 설계부터 학습·제작·배치까지 **24시간 미만**이었고, 손 안 회전으로 검증했다 | 원문확인 |
| 소프트 로봇 형태·제어 | DiffuseBot ([arXiv 2311.17053](https://arxiv.org/abs/2311.17053), NeurIPS 2023) | 확산모델에 미분 가능 시뮬레이션을 결합해 몸체와 제어를 함께 최적화하고, 텐던 구동 그리퍼를 실물로 만들었다. 흔히 인용되는 "4~8배 개선"은 애그리게이터 요약에서만 확인된다 ([Emergent Mind](https://www.emergentmind.com/papers/2311.17053)) | 원문확인 / 4~8배는 미확인 |
| 강성 분포 + 파지 자세 | Yi et al.(1-3) | 기준 설계보다 시뮬레이션과 하드웨어 모두에서 "유의하게 우수"하다고만 했고 수치는 없다 | 원문확인 |

소재 변수가 들어간 공동설계는 Yi et al.의 강성 분포와 DiffuseBot 정도다. 축소차수 FEM 대리모델(b)은 RL 기반 소프트 그리퍼 공동설계에도 쓰여, 소재 비선형성과 형태 설계를 잇는 다리 역할을 한다 ([arXiv 2603.19794](https://arxiv.org/abs/2603.19794)).

#### (d) 힘줄·관절

**AI는 힘줄 소재를 바꾸기보다 크리프·마찰·히스테리시스를 학습으로 흡수한다.** 트랜스포머 힘줄 모델(2-1)이 가장 최근의 정량 사례다. 비슷한 접근으로 내시경 로봇의 이중 힘줄 루프에서 학습 기반 매핑으로 히스테리시스를 보상해 평균 RMSE를 88.1% 줄인 연구가 있다. 다만 손가락이 아니라 내시경 대상이다 ([SSTL, arXiv 2605.16870](https://arxiv.org/abs/2605.16870), 원문확인). AMBIDEX는 점성·쿨롱 마찰 모델에 RNN 힘줄 동역학을 더한 하이브리드를 쓴다 ([AMBIDEX](https://aminer.org/pub/5ff67ffad4150a363cb3d68c/a-hybrid-dynamic-model-for-the-ambidex-tendon-driven-manipulator), 미확인).

소재 쪽 대응은 여전히 비AI다. Dyneema를 사전 인장·열처리해 신율을 1% 미만으로 낮췄고 ([텐던 암, arXiv 2307.02654](https://arxiv.org/pdf/2307.02654), 미확인), CRAFT는 플렉셔 피로를 줄이려고 PIP·DIP 관절을 롤링 접촉 관절로 바꿔 TPU 면에 하중을 분산시켰다 ([CRAFT](https://arxiv.org/html/2603.12120v1)). UHMWPE·아라미드 힘줄의 크리프·마모를 ML로 예측한 손가락 연구는 찾지 못했다.

#### (e) 마찰·접착 표면

**표면 소재의 ML 설계는 "형상 최적화 → 미세가공 → 접착력 시험"까지 검증되었고, "손가락 장착 → 파지 성공률" 단계는 비어 있다.**

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 접착 최적 섬유 | Son et al. 2021(2-1) | 접착력은 팁뿐 아니라 3D 스템 형상, 인장변형, 미세가공 한계에도 민감했다 | 원문확인(초록) |
| 전단 최적 섬유 | Dayan et al. ([Small 2023](https://doi.org/10.1002/smll.202304437)) | 제작 한계를 시뮬레이션에 넣은 ML 최적화로 표준 형상보다 전단 성능이 우수했다. 응용처로 pick-and-place 그리퍼를 제시했다 | 원문확인(초록) |
| 전기접착 2층 보호막 유전율 | Park et al. ([Sci. Rep. 2024](https://www.nature.com/articles/s41598-024-67805-0)) | FEM 1,000 샘플로 랜덤포레스트를 학습했다. 설계변수 8개, 구성 3,000개는 FEA로, 7,000개는 AI로 평가했다. 내층 2.5·외층 4.5 유전율 조합은 정전기력을 "약간" 개선했다 | 원문확인 |

전기접착 손가락 자체는 맞물린 전극 하나로 굽힘(DEA)과 접착을 함께 구현한 2016년 설계가 기준점이다 ([SPIE Newsroom](https://spie.org/news/6409-soft-compliant-gripper-for-safe-manipulation-of-extremely-fragile-objects), 미확인). 이 설계에는 ML이 없었다.

#### (f) 구동·자가치유

**인공근육 손가락에서 AI는 소재 설계가 아니라 비선형 동역학을 감추는 제어 계층에 머문다. 자가치유 손가락에서는 손상을 감지하는 단계에만 들어왔다.**

| 무엇을 했나 | 대표 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 인간 근조직 구동 손(AI 없음) | 도쿄대 Takeuchi 그룹 ([Ren et al., Sci. Robot. 2025](https://doi.org/10.1126/scirobotics.adr5512)) | 근조직 다발(MuMuTA)의 수축력 약 8 mN, 수축 길이 약 4 mm로 손가락을 개별 굽혔다. 손 길이 18 cm, 10분 동작 후 피로가 오고 1시간 쉬면 회복했다 ([EurekAlert](https://www.eurekalert.org/news-releases/1072918)) | 원문확인(초록) / 피로는 언론 |
| HASEL 근골격 손(ML 없음) | Peano-HASEL 손 ([arXiv 2603.24357](https://arxiv.org/abs/2603.24357)) | 액추에이터를 전완에 두고 1:2 풀리로 힘줄 변위를 증폭했다. 운용 전류만으로 파지를 감지해 종이풍선을 부수지 않고 잡았다. 제어는 규칙 기반이다 | 원문확인 |
| 자가치유 피부의 학습 기반 손상 복구 | Cambridge·VUB ([Adv. Intell. Syst. 2022](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d)) | DA 자가치유 고분자에 복합 섬유를 넣었다. 5층 신경망을 탐침 5,000회로 학습해 위치 2.3 mm, 깊이 95% 정확도를 냈다. 손상·치유 뒤 1개 층을 고정한 전이학습으로 200회 미만 탐침 만에 재적응했다 | 미확인 |
| 자가치유 하이드로겔 피부 | Georgopoulou et al. ([Commun. Mater. 2025](https://library.kab.ac.ug/Record/doaj-art-e1d3878756be4f13ab9aedd158f8e6b7/Description)) | RNN으로 온도와 변형 자극을 98% 정확도로 구분했다 | 미확인 |

인공근육 쪽 ML은 길항 TCP 액추에이터의 LSTM+MPC 위치·강성 제어 ([NSF PAR](https://par.nsf.gov/servlets/purl/10231284)), HASEL의 RNN·MLP 예측제어 ([Bohrium](https://www.bohrium.com/paper-details/machine-learning-amplified-control-system-for-hasel-actuator-soft-robot-system/864971402757800208-15541))처럼 제어 계층에 있다(모두 미확인). SMA·DEA·LCE 손가락을 ML로 설계한 원문은 찾지 못했다.

VUB(Terryn·Vanderborght) 그룹은 DA 자가치유 그리퍼·손을 상온 치유 네트워크(2020) ([IEEE RAM 2020-12](https://nxtbook.com/nxtbooks/ieee/roboticsautomation_december2020/index.php?startid=44)), FFF 인쇄 손가락(2020), 강구 재밍을 넣은 자가조절 그리퍼(2023) ([AIS 2023](https://www.citedrive.com/en/discovery/selfregulated-selfhealing-robotic-gripper-for-resilient-and-adaptive-grasping))로 확장했다(모두 미확인). **연도 충돌:** 이 계열의 첫 Science Robotics 논문("Self-healing soft pneumatic robots")은 2017년으로 알려져 있으나, 한 검색 스니펫은 2021년으로 적었다. 원문으로 확인하지 못했으므로 2017년을 잠정 채택한다. 리뷰는 자율 치유를 손상 감지부터 회복 평가까지 5단계로 나누고, 현재 자가치유 로봇은 대개 여러 차례 사람 개입이 필요하다고 지적했다 ([Kashef Tabrizian et al., AIS 2025](https://www.deutsche-digitale-bibliothek.de/item/JOVNUWDA6Q2VPXGJNMU5EETPYU36OZHL), 미확인). 치유 소재 자체를 AI로 설계한 손가락 사례는 없다.

#### (g) 촉각 손끝이 이끈 조작 성과

촉각 손끝 소재는 학습 기반 조작의 성과로 이어졌고, 그 결과가 다시 소재 요구를 바꾸고 있다.

| 성과 | 사례 | 정량 성과 | 검증상태 |
|---|---|---|---|
| 시각+촉각 물체 추적 | NeuralFeels(Meta·CMU, DIGIT) ([arXiv 2312.13469](https://arxiv.org/abs/2312.13469)) | 재구성 F-score 81%, 평균 포즈 드리프트 4.7 mm. 시각 가림이 심할 때 시각 단독보다 추적이 최대 94% 개선됐다 | 원문확인 |
| 비전 없는 Baoding 회전 | Shadow Hand Lite, 이진 촉각 ([arXiv 2610.23438](https://arxiv.org/abs/2610.23438)) | 고장 taxel을 흉내 낸 도메인 랜덤화로 제로샷 전이해 180° 회전을 **225회 연속**(112.5바퀴) 달성했다 | 원문확인(프리프린트) |
| 촉각 사전학습 VTLA 모델 | Spark-0 ([arXiv 2610.22342](https://arxiv.org/abs/2610.22342)) | 1,000시간 분량의 전손 촉각 인간 조작 데이터로 사전학습했다. 촉각을 뺀 경우보다 성공률이 **52.5%에서 71.7%**로 올랐다 | 원문확인(프리프린트) |
| 촉각 모터 적응 | TMA, Unitree G1 + BrainCo Revo2 ([arXiv 2611.18976](https://arxiv.org/abs/2611.18976)) | 시뮬레이션에서만 학습한 정책으로 상용 문손잡이 4종을 열었고, RMA와 반응형 촉각 기준선을 크게 앞섰다 | 원문확인(프리프린트) |

저해상도·이진 촉각이라도 시뮬레이션 정합을 잘하면 강한 성능이 나온다. AnySkin과 DIGIT의 비교와 함께 보면, 정책 학습에는 "고해상도 젤"보다 **"내구성 있고 시뮬레이션하기 쉬운 피부"**가 유리하다는 신호로 읽힌다(추론). Meta가 손끝·손바닥 촉각을 하나의 손에 통합하는 Digit Plexus 플랫폼을 낸 것도 같은 흐름이다 ([Meta AI 블로그](https://ai.meta.com/blog/fair-robotics-open-source/)).

### 2-3. 종합 평가

**답:** 손가락 소재에서 AI 성숙도는 "그 소재의 거동을 싸게 데이터로 만들 수 있는가"에 비례한다. 누르기만 하면 데이터가 나오는 촉각 해석과 FEM이 있는 형상 설계는 성숙했다. 합성이 필요한 배합과 장기 시험이 필요한 수명은 비어 있다.

| 부위/소재 | AI 성숙도 | 이유 |
|---|---|---|
| 촉각 신호 해석·센서 간 전이·파운데이션 모델 | **상** | 수십만 장 규모 사전학습, 교체 피부의 무보정 정책 전이, 초해상이 원문으로 검증됐다 |
| 촉각 시뮬레이션·sim-to-real | **상** | GPU 병렬 시뮬레이터와 제로샷 전이 사례가 많다. 다만 젤을 선형탄성으로 근사한다 |
| 소프트 손가락 형상·강성 분포(Fin-Ray, 플렉셔, 벨로우즈) | **상** | FEM 대리모델 + GA·NSGA-II·BO·MAP-Elites가 표준이 되었고 실물 검증도 있다 |
| 손 형태 공동설계 | **중~상** | 0.8초 생성, 24시간 사이클이 나왔지만 소재 변수는 드물다 |
| 전자피부 미세구조 역설계 | **중** | 소량 데이터 능동학습으로 감도·선형성 상충을 풀었지만 평판 패드에 머문다 |
| VBTS 젤·코팅·광학 설계 | **중** | 물리 시뮬레이터 + DoE·응답곡면 수준이다. 딥 생성 설계나 BO는 없다 |
| 접착·마찰 표면 | **중** | 섬유 형상 BO가 실험 검증됐지만 손가락 장착 파지 평가는 없다 |
| 힘줄·관절 | **중**(힘 모델) / **하**(소재) | 트랜스포머 힘 모델은 정량 성과가 있다. 크리프·마모 소재 ML은 없다 |
| 소프트 손가락 엘라스토머 배합 | **중~하** | 동료심사 1건(KAIST)이고, 파괴 관련 물성(연신율)의 예측 정확도가 가장 낮다 |
| 구동 소재(SMA·TCP·HASEL·DEA·LCE·근조직) | **하** | ML은 제어 계층에만 있고, 손가락용 인공근육 소재를 ML로 설계한 사례는 없다 |
| 가변강성(재밍·LMPA·SMP) 손가락 | **하** | ML 적용 사례를 찾지 못했다 |
| 자가치유 피부 | **하** | ML은 손상 감지·재보정에만 쓰였고, 단일 그룹 결과에 집중돼 있다 |
| 마모·피로 수명 예측 | **하** | 손끝 피부 수명을 ML로 예측한 1차 연구가 없다 |

패턴은 분명하다. AI는 **이미 쓰는 엘라스토머·TPU를 새로 발견하기보다 길들였고, 형상·강성·제어를 함께 최적화했으며, 신호를 해독했다.** 동시에 학습 기반 조작이 연구용 손의 소재 선택(교체형 자기 피부, 강체 링크 + TPU 관절, 내구성 우선 손끝)을 주도하기 시작했다. 공백은 재밍·LMPA·SMP 손가락, LCE·SMA·DEA 손가락의 ML, 힘줄 크리프 ML, 마모 수명 예측, AI로 설계한 자가치유 손가락 소재다. 무엇보다 **손가락 피부를 합성하고 촉각·수명까지 시험하는 닫힌 루프는 아직 없다.**

---

## 3. 남은 문제와 해결 방향

**답:** 남은 문제는 여섯 영역이다. 내구성·마모 데이터가 짧고, 센서 비이상성 때문에 재보정이 반복되며, 데이터는 카메라 촉각에 편중됐다. 시뮬레이터는 점탄성·마모를 빼고, 제조는 수작업에 의존하며, 설계를 닫는 실험 루프와 독립 검증이 없다. 공통 해법은 **"수명과 실패까지 기록하는 표준 시험, 물리량 기반의 센서 불변 표현, 소재를 식별하는 real-to-sim, 자동 제조와 자동 시험의 결합"**이다.

여섯 영역은 이어져 있다. 내구성 데이터가 짧으면 마모가 신호를 어떻게 바꾸는지 모르므로 교체할 때마다 재보정해야 하고, 마모 상태가 데이터셋에 없으면 시뮬레이터도 반영할 수 없다. 이 고리를 끊으려면 제조와 시험을 자동화한 폐루프가 필요하다.

### 3-1. 문제 → 원인 → 해결 방향

| 영역 | 문제 | 원인 | 해결 방향 |
|---|---|---|---|
| **내구성·마모** | 수명 데이터가 10³~10⁴회 규모 | 시험 표준이 없고 장기 시험이 비싸다. 소프트 공압 액추에이터 내구성 연구는 "드물고 단편적"이며 많은 연구가 내구성을 아예 평가하지 않는다 ([HKUST 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)). VBTS 벤치마크 저자들도 1,000회는 상대 비교용이지 실제 수명이 아니라고 단서를 달았다 ([arXiv 2511.07797](https://arxiv.org/html/2511.07797v1)) | HKUST 표준 프로토콜과 VBTS의 압축·전단·연마 4종 시험을 채택하고 수명 분포를 보고한다. 다채널 시험 로봇으로 수명을 자동 스캔한다. DEA 시험 로봇은 경계 운전조건에서 수명을 최대 100% 늘렸다 ([arXiv 2602.20963](https://arxiv.org/abs/2602.20963)) |
| | 감도와 내구의 상충 | 질긴 소재(PU)는 저하중 감도가 낮다 | 질긴 소재로 바꾸고 감도 손실은 학습 보정으로 메운다(ReSkin식). 수명을 배합 최적화의 목적함수에 넣는다 |
| | 마모 수명 ML 예측 부재 | 마모·피로 데이터셋이 없다. 파괴 관련 물성은 예측 자체가 어렵다(2-2 b) | 피로·마모 곡선을 표준 형식으로 공개하고, 손상 상태를 입력으로 받는 수명 대리모델을 만든다 |
| **센서 비이상성** | 히스테리시스·드리프트 | 점탄성 소재의 본질이다 | 연속학습으로 보상한다. 연성 센서 손가락에서 LSTM, 리허설 메모리, 기저 신호 정규화를 결합해 드리프트를 다뤘다 ([arXiv 2503.16540](https://arxiv.org/abs/2503.16540)). 히스테리시스 오차를 12.4%에서 1.8%로 줄였다는 보고는 저널 페이지에 철회(retraction) 표시가 함께 떠 있어 확인이 필요하다 ([Sensors and Materials](https://sensors.myu-group.co.jp/sm_pdf/SM4571.pdf)) |
| | 개체 편차·교체 후 신호 이동 | 수작업 제조 편차. 커뮤니티 분석에 따르면 GelSight Mini에서 젤 모델 교체가 센서 유닛 교체보다 신호를 더 크게 바꿨다 ([HF Space 분석](https://yxma-gsmini-gel-wear.static.hf.space/index.html), 미확인·비심사) | 비지도 도메인 적응으로 재보정한다. 마커·조명·탄성률이 다른 센서로 옮겨 수직력 오차 0.102 N(FS 3.4%)을 얻었다 ([arXiv 2407.14380](https://arxiv.org/abs/2407.14380)). 시뮬레이션 센서로 학습한 트랜스포머(SITR)는 신규 센서에 zero-shot 전이했다 ([SITR, arXiv 2502.19638](https://arxiv.org/abs/2502.19638)). 공유 마커 표현 ([GenForce, arXiv 2503.01058](https://arxiv.org/abs/2503.01058))이나 응력 텐서 중간 표현 ([TensorTouch, arXiv 2506.08291](https://arxiv.org/abs/2506.08291))처럼 물리량을 기준 삼아 전이한다 |
| | 온도 의존성 | 손끝 센서의 열 드리프트를 ML로 보상한 연구를 찾지 못했다 | 온도를 입력에 포함한 보정 데이터셋을 만든다 |
| **데이터·벤치마크** | 카메라 기반 편중 | 대규모 데이터가 모두 광학식이다. T3의 FoTa는 13개 센서·11개 과제에서 300만 건 이상을 모았고 다중 핀 삽입 성공률을 촉각 없음보다 53%p 높였다 ([T3, arXiv 2406.13640](https://arxiv.org/abs/2406.13640)). TacQuad·UniTouch도 시각촉각 이미지다 ([AnyTouch, arXiv 2502.12191](https://arxiv.org/abs/2502.12191); [UniTouch, arXiv 2401.18084](https://arxiv.org/abs/2401.18084)) | 압저항·정전용량·자기 피부 데이터셋을 만든다. 소재 물성(탄성률, 경도)과 마모 상태를 메타데이터로 붙인다 |
| | 소재·마모·실패 데이터 부재 | 고장 난 센서의 데이터를 담은 공개 데이터셋이 없다 | 젤 마모 시험 데이터와 고장 taxel 로그를 공개한다. Baoding 연구처럼 고장 taxel을 랜덤화에 쓴다 |
| | 힘이 중요한 과제의 성능 부족 | 모방학습 성능은 아직 "힘이 정말 중요해지는 동역학 수준"에 이르지 못했다 ([힘·촉각 파운데이션 모델 서베이, arXiv 2504.11827](https://arxiv.org/abs/2504.11827)) | 접촉력·슬립 라벨이 있는 공통 벤치마크를 쓰고, 학습 불필요(learning-free) 감도 지표로 하드웨어를 따로 평가한다 |
| **시뮬레이션 격차** | 점탄성·마모 미반영 | 젤을 선형탄성이나 경험적 매핑으로 근사한다. FOTS는 MLP 매핑으로 CPU에서 광학 28.6 fps를 냈지만 다양한 하중에서 영상 합성은 여전히 어렵다 ([FOTS, arXiv 2404.19217](https://arxiv.org/abs/2404.19217)) | 생성모델로 sim 영상을 real로 바꾸거나(확산모델 점자 읽기 75.74%) ([arXiv 2304.01182](https://arxiv.org/abs/2304.01182)), sim과 real을 공통 깊이 맵으로 정렬한다(Tacmap) ([arXiv 2602.21625](https://arxiv.org/abs/2602.21625)). 이와 별도로 미분 가능 FEM으로 소재 물성을 실측에서 역추정하는 real-to-sim 경로를 키운다(DiffTactile 방식) |
| | 센서 열화 미반영 | 기존 접촉 모델은 센서 부정확성·신호 열화("tactile shadowing")를 모델링하지 않는다 ([HydroShear](https://roboticsproceedings.org/rss22/p155.pdf)) | 마모·고장 상태를 시뮬레이터 파라미터로 넣는다 |
| **제조·통합** | 수작업 재현성 | 주조·도장 공정. 수작업 대 프린팅 손끝 센서의 개체 편차를 정량 비교한 연구가 없다 | 비전 제어 젯팅과 FFF 자가치유 손가락 같은 자동 제조로 바꾸고, 편차 감소량을 측정해 학습 보정과 결합한다 |
| | 배선 밀도·단선 | 손끝은 좁고 반복 굽힘을 받는다(ORCA 단선). 고기능 MCU 노드는 비용·지연·전력 때문에 확장성이 떨어진다 | 논리회로 수십 개짜리 노드가 판독 경로를 스스로 재구성하는 e-skin 네트워크(1 kHz에서 1.88 µW/노드) ([Ozaki et al., Nat. Commun. 2025](https://doi.org/10.1038/s41467-025-56596-1)), 전자부를 분리한 자기식 피부를 쓴다 |
| **공동설계·검증** | 합성-시험 폐루프 부재 | 엘라스토머 합성·경화 자동화, 촉각 지표 자동 측정, 장기 내구 시험의 세 고리가 빠졌다. BU의 MAMA BEAR는 2만 5천 회 넘는 실험과 BO로 에너지 흡수 효율 75.2% 구조를 찾았지만, 압축처럼 빠른 기계시험이었고 사람이 주기적으로 개입했다 ([Snapp et al., Nat. Commun. 2024](https://doi.org/10.1038/s41467-024-48534-4)). **수치 충돌:** 언론은 73.3%로 보도했다 ([IoT World Today](https://www.iotworldtoday.com/robotics/robot-uses-ai-in-hunt-for-shock-absorbing-design)). 논문의 75.2%를 쓴다 | 자동 배합·경화, 촉각 감도·히스테리시스 자동 측정, 다채널 수명시험을 한 루프로 묶는다. 목적함수에 초기 감도와 수명을 함께 넣는다 |
| | 연구와 기업 수명 주장의 격차 | 1차 문헌의 시험은 10³~10⁴회다(ORCA는 10,000회 넘게 연속 운전, 파지 2,250회 동안 파손 없음). Optimus V3 특허는 "백만 사이클 내구성"을 강조한다고 2차 해설이 전한다 ([humanoid.guide](https://humanoid.guide/?p=16664)). Sanctuary 액추에이터 20억 회 무누설 시험은 2차 사이트에서만 확인된다 ([heymanoid](https://heymanoid.pages.dev/robots/sanctuary-phoenix/)) | 기업 수명 주장에 시험 조건과 고장 정의를 공개하도록 요구하고, 표준 프로토콜로 독립 시험한다 |
| | 자기보고 성능 주장 | "SDL 최초"(DEA 로봇)와 단일 그룹의 자가치유 결과에 독립 재현이 없다 | 공개 하드웨어(DIGIT, ReSkin, LEAP, ORCA)를 기준선으로 교차 실험실 재현을 한다 |
| | 공동설계에 소재 변수 부족 | DGDM은 센서 없는 형상만 생성한다 | 소재 비선형 대리모델(강성 분포, 축소차수 FEM)을 생성 설계에 연결한다 |

### 3-2. 단기·중기·장기 로드맵

| 단계 | 핵심 행동 | 기대 효과 |
|---|---|---|
| **단기(1~2년)** | ① 손끝 젤·피부·플렉셔에 표준 내구 프로토콜(압축·전단·연마, SPA 프로토콜)을 적용하고 수명 분포와 고장 사진을 공개한다 ② 마모·고장 센서 데이터와 소재 메타데이터를 데이터셋에 넣는다 ③ 교체 피부에 비지도 도메인 적응을 기본 탑재한다 ④ 검증된 소량 배합 대리모델(KAIST)에 GP·BO를 붙여 순차 실험으로 바꾼다 ⑤ 원문·보도 수치를 대조해 인용한다 | 수명과 감도를 공정하게 비교할 수 있다. 가장 싼 공백(배합 BO, 재보정)부터 메운다 |
| **중기(3~5년)** | ① 엘라스토머 자동 배합·경화, 촉각 지표 자동 측정, 다채널 수명시험을 묶은 손가락 소재 폐루프 실험실을 만든다 ② 미분 가능 FEM으로 점탄성·마모 상태를 실측에서 식별해 촉각 시뮬레이터에 넣는다 ③ 압저항·자기 피부용 파운데이션 모델을 만든다 ④ 힘줄 크리프·마모 데이터로 수명 예측 모델을 학습한다 ⑤ 재밍·LMPA·SMP, LCE·SMA·DEA 손가락에 대리모델과 BO를 적용한다 | AI가 "신호 해석"에서 "수명을 아는 소재 설계"로 넘어간다 |
| **장기(5~10년)** | ① 과제에서 손 형태, 소재 분포, 배합까지 내려가는 다중 스케일 공동설계 ② 자가치유 소재의 치유 온도와 강도를 함께 최적화하고, 손상 감지-치유-재보정을 자율화한다 ③ 기업 손과 연구 손을 같은 프로토콜로 독립 시험한다 | "목표 조작 성능 → 손가락 소재·구조 자동 생성 → 자동 수명 검증" 체계 |

순서는 의존성을 따른다. 중기의 폐루프 실험실은 단기에 정한 표준 지표가 있어야 목적함수를 정의할 수 있다. 장기의 다중 스케일 설계는 중기의 real-to-sim 소재 식별과 수명 모델이 있어야 가능하다.

---

## 4. 결론

(1) AI가 로봇 손가락 소재에 도입된 이유는, 손끝이 부드러우면서도 질겨야 하는데 엘라스토머의 비선형·히스테리시스·크리프, 비싼 FEM, 쿨롱 법칙이 맞지 않는 마찰, 고차원 공동설계 공간, 노이즈 많은 촉각 신호 때문에 물리모델과 시행착오로는 설계·보정 비용을 감당할 수 없었기 때문이다. (2) AI는 배합·FEM 대리모델, 확산모델 공동설계, 촉각 해석과 파운데이션 모델, sim-to-real, 광학·표면·힘줄 모델링으로 적용됐다. 그 결과 33개 배합으로 600% 넘게 늘어나는 엘라스토머, 교체해도 정책이 유지되는 자기 피부, 0.8초 만의 손가락 형상 생성, 77% 강한 접착 섬유, 41% 줄어든 힘줄 sim-to-real 격차가 나왔다. (3) 그러나 AI는 새 소재를 찾기보다 기존 소재를 길들이는 데 머물렀고, 수명은 10³~10⁴회 데이터로만 말해지며, 구동·가변강성·자가치유 소재의 ML과 합성-시험 폐루프는 비어 있다. 다음 단계의 관건은 더 큰 모델이 아니라 **수명과 마모를 기록하는 표준 데이터, 소재 상태를 아는 시뮬레이터, 그리고 손가락 피부를 만들고 눌러 보고 닳게 해 보는 자동 실험 루프**다.

---

## 부록 A. 출처 신뢰도 표기

- **원문확인:** 논문 본문·공식 초록·기관 원문을 직접 읽어 수치를 확인했다(프리프린트는 별도 표시).
- **언론·기업주장:** 보도자료, 언론, 기업 발표, 2차 해설에서만 확인했다. 독립 검증이 없다.
- **미확인:** 검색 요약이나 2차 자료로만 확인했고, 원문을 열지 못했거나 원문에서 해당 수치를 찾지 못했다.

## 부록 B. 접근 상태 요약

- 성공: nature.com(본문·메타데이터), arxiv.org의 abs·html·pdf 페이지, NCBI(PubMed·PMC E-utilities)와 Europe PMC REST, NSF PAR, roboticsproceedings.org, 저자 공개 원고, 기업 공식 페이지.
- 실패: Science Robotics·Science·Wiley·MDPI 등 출판사 사이트는 Cloudflare 봇 방어로 열지 못해 PubMed·Europe PMC 초록으로 우회했다. export.arxiv.org API는 DNS 해석에 실패해 abs 페이지를 하나씩 받았다. WebFetch 도구는 DNS 오류로 쓰지 않았다.
- 공백: 상용 손(Shadow, Allegro, Unitree, Inspire, Tesla, Figure, Sanctuary)은 손끝·패드 소재명과 Shore 경도, 내구 시험 조건을 공개하지 않아 소재 맵에 빈칸이 남았다.

## 참고문헌

1. [Shadow Hand](https://www.shadowrobot.com/dexterous-hand-series/)
2. [Allegro Hand](https://www.allegrohand.com/)
3. [Unitree Dex5-1](https://www.unitree.com/Dex5-1)
4. [Sanctuary 유압 손](https://sanctuary.ai/solutions/hydraulic-hands/)
5. [Tesla Optimus 손, Electrek 2024](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/)
6. [ORCA, arXiv 2504.04259](https://arxiv.org/html/2504.04259)
7. [LEAP Hand, arXiv 2309.06440](https://ar5iv.labs.arxiv.org/html/2309.06440)
8. [Liu & Howe, NSF PAR](https://par.nsf.gov/servlets/purl/10485527)
9. [VBTS 내구성 벤치마크, arXiv 2511.07797](https://arxiv.org/html/2511.07797v1)
10. [GelSight Mini 데이터시트](https://pdf.directindustry.com/pdf/gelsight-inc/gelsight-mini/4602322-1082169.html)
11. [Smooth-On](https://www.smooth-on.com/compare/4922/4985/ecoflex-00-20--ecoflex-00-30/)
12. [FormX](https://www.formx.eu/p/product/dragon-skin-30/skin30x/)
13. [HKUST 내구성 리뷰 2026](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)
14. [CRAFT, arXiv 2603.12120](https://arxiv.org/html/2603.12120v1)
15. [Deng & Li, Front. Robot. AI 2021](https://www.frontiersin.org/articles/10.3389/frobt.2020.590076/full)
16. [Knox Labs](https://www.knoxlabs.com/products/inspire-robots-rh56f1-dexterous-hand)
17. [humanoid.guide 힘줄](https://humanoid.guide/?p=16664)
18. [Stanford Daily 2023](https://stanforddaily.com/2023/02/01/lab-develops-stickiest-non-sticky-material/)
19. [Brown et al., PNAS 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2973877/)
20. [VUB, Soft Robotics 2020](https://biblio.vub.ac.be/vubirfiles/55950627/soro.2019.0081.pdf)
21. [Adv. Intell. Syst. 2022](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d)
22. [LEAP 위키](https://web-3kk.pages.dev/en/knowledge/hardware/hands/leap-hand)
23. [Figure 03 공개 2025](https://www.figure.ai/news/introducing-figure-03)
24. [Sanctuary 발표, BusinessWire](https://www.businesswire.com/news/home/20250226807548/en)
25. [The Rundown](https://robotnews.therundown.ai/p/sanctuarys-touchy-feely-humanoid)
26. [Digit 360, arXiv 2411.02479](https://arxiv.org/abs/2411.02479)
27. [ReSkin, arXiv 2111.00071](https://arxiv.org/abs/2111.00071)
28. [Kim et al., PLoS ONE 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)
29. [Fin-Ray NN 최적화, arXiv 2506.00494](https://arxiv.org/abs/2506.00494)
30. [Kasolowsky & Bäuml, arXiv 2409.12735](https://arxiv.org/html/2409.12735)
31. [HydroShear, RSS 2026](https://roboticsproceedings.org/rss22/p155.pdf)
32. [Yi et al., arXiv 2505.20404](https://arxiv.org/abs/2505.20404)
33. [Sensors 2017 리뷰](https://pmc.ncbi.nlm.nih.gov/articles/PMC5713637)
34. [촉각 데이터 표현 리뷰, arXiv 2510.10804](https://arxiv.org/html/2510.10804v1)
35. [SoRoForge 2023](https://matterassembly.org/publications/smith2023soroforge/)
36. [Marechal et al.](https://discovery.ucl.ac.uk/10112846/1/Towards_a_Common_Framework_and_Database_of_Materials_for_Soft_Robotics___Revision2.pdf)
37. [9DTact, arXiv 2308.14277](https://arxiv.org/abs/2308.14277)
38. [Song et al., Nat. Commun. 17, 7167, 2026](https://www.nature.com/articles/s41467-026-73735-4)
39. [SPADA, arXiv 2305.19509](https://arxiv.org/abs/2305.19509)
40. [DGDM, arXiv 2402.15038](https://arxiv.org/abs/2402.15038)
41. [Yan et al., Sci. Robot. 2021](https://pubmed.ncbi.nlm.nih.gov/34043530/)
42. [Sparsh, arXiv 2410.24090](https://arxiv.org/abs/2410.24090)
43. [TacSL, arXiv 2408.06506](https://arxiv.org/abs/2408.06506)
44. [OptiSense, arXiv 2504.14739](https://arxiv.org/abs/2504.14739)
45. [Son et al., Small 2021](https://doi.org/10.1002/smll.202102867)
46. [arXiv 2603.04351](https://arxiv.org/abs/2603.04351)
47. [DIGIT, arXiv 2005.14679](https://arxiv.org/abs/2005.14679)
48. [i-Tac, arXiv 2604.10692](https://arxiv.org/abs/2604.10692)
49. [TransForce, arXiv 2409.09870](https://arxiv.org/abs/2409.09870)
50. [Taxim, arXiv 2109.04027](https://arxiv.org/abs/2109.04027)
51. [DiffTactile, arXiv 2403.08716](https://arxiv.org/abs/2403.08716)
52. [arXiv 2611.07881](https://arxiv.org/abs/2611.07881)
53. [arXiv 2611.08939](https://arxiv.org/abs/2611.08939)
54. [Anzu/GelSight 2025](https://www.anzupartners.com/2025/01/06/gelsight-extends-life-and-durability-of-gelsight-mini-with-new-gels/)
55. [ACEL, arXiv 2611.19384](https://arxiv.org/abs/2611.19384)
56. [Meta 블로그](https://ai.meta.com/blog/reskin-a-versatile-replaceable-low-cost-skin-for-ai-research-on-tactile-perception/)
57. [AnySkin, arXiv 2409.08276](https://arxiv.org/html/2409.08276v3)
58. [Kim et al., Nature Materials 2025](https://www.nature.com/articles/s41563-025-02373-w)
59. [ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing)
60. [SuperTac, Nature Sensors 2026](https://www.nature.com/articles/s44460-025-00006-y)
61. [저자 공개 원고](https://linqi-ye.github.io/docs/NATSENSORS.pdf)
62. [Gizmochina 2026](https://www.gizmochina.com/2026/01/21/chinas-supertac-sensor-enables-human-like-touch-in-humanoid-robots/)
63. [Liu et al., Science 2024](https://pubmed.ncbi.nlm.nih.gov/38815009/)
64. [arXiv 2304.04609](https://arxiv.org/abs/2304.04609)
65. [Adv. Sci. 2026](https://europepmc.org/search?query=DOI%3A10.1002%2Fadvs.202524250)
66. [arXiv 2611.10647](https://arxiv.org/abs/2611.10647)
67. [Interesting Engineering](https://interestingengineering.com/ai-robotics/soft-robotic-hand-grips-fragile-eggs)
68. [arXiv 2603.19794](https://arxiv.org/abs/2603.19794)
69. [Canberra 포털](https://researchprofiles.canberra.edu.au/en/publications/fin-bayes-a-multi-objective-bayesian-optimization-framework-for-s/)
70. [arXiv 2311.12477](https://arxiv.org/abs/2311.12477)
71. [arXiv 2407.07591](https://arxiv.org/abs/2407.07591)
72. [arXiv 2408.04376](https://arxiv.org/abs/2408.04376)
73. [arXiv 2501.03763](https://arxiv.org/abs/2501.03763)
74. [Buchner et al., Nature 2023](https://www.nature.com/articles/s41586-023-06684-3)
75. [Polymers 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9657554/)
76. [arXiv 2512.03743](https://arxiv.org/abs/2512.03743)
77. [arXiv 2311.17053](https://arxiv.org/abs/2311.17053)
78. [Emergent Mind](https://www.emergentmind.com/papers/2311.17053)
79. [SSTL, arXiv 2605.16870](https://arxiv.org/abs/2605.16870)
80. [AMBIDEX](https://aminer.org/pub/5ff67ffad4150a363cb3d68c/a-hybrid-dynamic-model-for-the-ambidex-tendon-driven-manipulator)
81. [텐던 암, arXiv 2307.02654](https://arxiv.org/pdf/2307.02654)
82. [Small 2023](https://doi.org/10.1002/smll.202304437)
83. [Sci. Rep. 2024](https://www.nature.com/articles/s41598-024-67805-0)
84. [SPIE Newsroom](https://spie.org/news/6409-soft-compliant-gripper-for-safe-manipulation-of-extremely-fragile-objects)
85. [Ren et al., Sci. Robot. 2025](https://doi.org/10.1126/scirobotics.adr5512)
86. [EurekAlert](https://www.eurekalert.org/news-releases/1072918)
87. [arXiv 2603.24357](https://arxiv.org/abs/2603.24357)
88. [Commun. Mater. 2025](https://library.kab.ac.ug/Record/doaj-art-e1d3878756be4f13ab9aedd158f8e6b7/Description)
89. [NSF PAR](https://par.nsf.gov/servlets/purl/10231284)
90. [Bohrium](https://www.bohrium.com/paper-details/machine-learning-amplified-control-system-for-hasel-actuator-soft-robot-system/864971402757800208-15541)
91. [IEEE RAM 2020-12](https://nxtbook.com/nxtbooks/ieee/roboticsautomation_december2020/index.php?startid=44)
92. [AIS 2023](https://www.citedrive.com/en/discovery/selfregulated-selfhealing-robotic-gripper-for-resilient-and-adaptive-grasping)
93. [Kashef Tabrizian et al., AIS 2025](https://www.deutsche-digitale-bibliothek.de/item/JOVNUWDA6Q2VPXGJNMU5EETPYU36OZHL)
94. [arXiv 2312.13469](https://arxiv.org/abs/2312.13469)
95. [arXiv 2610.23438](https://arxiv.org/abs/2610.23438)
96. [arXiv 2610.22342](https://arxiv.org/abs/2610.22342)
97. [arXiv 2611.18976](https://arxiv.org/abs/2611.18976)
98. [Meta AI 블로그](https://ai.meta.com/blog/fair-robotics-open-source/)
99. [arXiv 2602.20963](https://arxiv.org/abs/2602.20963)
100. [arXiv 2503.16540](https://arxiv.org/abs/2503.16540)
101. [Sensors and Materials](https://sensors.myu-group.co.jp/sm_pdf/SM4571.pdf)
102. [HF Space 분석](https://yxma-gsmini-gel-wear.static.hf.space/index.html)
103. [arXiv 2407.14380](https://arxiv.org/abs/2407.14380)
104. [SITR, arXiv 2502.19638](https://arxiv.org/abs/2502.19638)
105. [GenForce, arXiv 2503.01058](https://arxiv.org/abs/2503.01058)
106. [TensorTouch, arXiv 2506.08291](https://arxiv.org/abs/2506.08291)
107. [T3, arXiv 2406.13640](https://arxiv.org/abs/2406.13640)
108. [AnyTouch, arXiv 2502.12191](https://arxiv.org/abs/2502.12191)
109. [UniTouch, arXiv 2401.18084](https://arxiv.org/abs/2401.18084)
110. [힘·촉각 파운데이션 모델 서베이, arXiv 2504.11827](https://arxiv.org/abs/2504.11827)
111. [FOTS, arXiv 2404.19217](https://arxiv.org/abs/2404.19217)
112. [arXiv 2304.01182](https://arxiv.org/abs/2304.01182)
113. [arXiv 2602.21625](https://arxiv.org/abs/2602.21625)
114. [Ozaki et al., Nat. Commun. 2025](https://doi.org/10.1038/s41467-025-56596-1)
115. [Snapp et al., Nat. Commun. 2024](https://doi.org/10.1038/s41467-024-48534-4)
116. [IoT World Today](https://www.iotworldtoday.com/robotics/robot-uses-ai-in-hunt-for-shock-absorbing-design)
117. [heymanoid](https://heymanoid.pages.dev/robots/sanctuary-phoenix/)
