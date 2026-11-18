# 로봇 손가락 끝(Fingertip)·손가락 피부 촉각 센싱 소재에 대한 AI 적용과 정량 성과

작성 기준일: 2026-11-18. 표기 규칙: **[원문확인]** = 논문 초록/본문, 공식 기업 페이지를 직접 받아 확인함. **[언론·기업주장]** = 보도자료, 기업 발표, 2차 보도(독립 검증 없음). **[미확인(스니펫)]** = 검색 스니펫에서만 확인하고 원문은 열지 못함. 날짜는 공개일(arXiv 제출일 또는 저널 온라인 게재일) 기준이다. 자금·시장 관련 내용은 제외했다.

## Q1. 비전 기반 촉각 센서(VBTS)의 엘라스토머 소재와 ML(깊이/힘 복원, 시뮬레이션과 sim-to-real, 설계 최적화)

### Takeaway
VBTS에서 AI는 세 층위로 들어가 있다. (1) 겔 영상을 힘, 깊이, 슬립으로 바꾸는 학습 디코더(9DTact: 이미지-힘 약 10만 쌍, Sparsh: 46만 장 이상으로 자기지도 사전학습), (2) 엘라스토머 광학과 변형을 재현하는 시뮬레이터(Taxim, TACTO, DiffTactile, TacSL, 2026년의 TactileLab·RevoSim), (3) 겔·코팅·조명 자체를 시뮬레이션 기반 최적화로 설계하는 단계(OptiSense Studio 2025, i-Tac 2026, Digit 360의 DoE·산란 최적화). 이 중 소재 설계 쪽은 아직 "물리 시뮬레이터 + 최적화" 또는 "응답곡면 + 다목적 최적화" 수준이다. 딥러닝 생성 설계로 겔을 설계한 사례는 찾지 못했다.

### Cited Findings
**센서 하드웨어와 겔 소재**
- **DIGIT (Meta, arXiv 2020-05-29) [원문확인]**: 엘라스토머를 3단계로 만든다. 몰드에 실리콘 기반 백색 안료를 에어브러시로 뿌려 이미지 전사층을 만들고, 그 위에 베이스 실리콘을 붓는다. 이 겔을 Smooth-On Sil-Poxy(광학 투명 실리콘 접착제)로 아크릴 창에 붙인다. 겔 실리콘으로는 태양광 셀 코팅용인 Smooth-On Solaris를 쓴다. 카메라는 OVM7692 60 fps, 640x480이고 추정 제조원가는 약 15 USD다. 마모 시험에서 투과율 증가로 잰 열화가 DIGIT 겔은 5/10/15회 패스에서 0/0.3/0.3%였다. 비교군인 [11] 겔은 276/482/805%, GelSight Inc. 겔은 475/662/918%였다. 딥러닝 모델 기반 컨트롤러로 다지 손에서 유리구슬을 조작하는 시연을 했다. — [arXiv 2005.14679](https://arxiv.org/abs/2005.14679)
- **Digit 360 (Meta FAIR, arXiv 2024-11-04) [원문확인]**: 손가락 모양의 반구형 센서로 taxel 약 830만 개를 갖는다. 공간 분해능은 7 µm, 법선력 분해능은 1.01 mN, 전단력 분해능은 1.27 mN이다. 진동은 10 kHz까지 감지하고 열과 냄새(가스)도 감지한다. 온디바이스 NN 가속기로 인간의 반사궁(reflex arc)을 흉내 낸다. 엘라스토머 설계에서는 DoE(실험계획법)로 감도에 영향을 주는 6개 파라미터를 식별했다. 손가락 반경 Rgel, 반사 코팅 두께 Tc, 표면층 두께 Tg, 높이 h, 코팅 탄성률 Ec, 겔 탄성률 Eg다. Tc와 Tg가 두껍거나 컴플라이언스가 낮으면 모서리에 저역통과 필터 효과가 생긴다. 이를 줄이려고 기존 수작업 도장, 에어브러시, 딥코팅 대신 겔 표면에 은(Ag) 박막을 직접 성장시키는 화학증착법을 개발해 코팅을 훨씬 얇게 만들었다. 내부 반사층의 표면 산란을 경면(1°)에서 Lambertian까지 시뮬레이션했고, 배경 조도 균일성을 제약으로 두고 이미지 대비를 최적화했다. 그 결과 Lambertian 표면이 반구를 적분구처럼 작동시킨다는 것을 보였다. 내부 구조 대신 "solid gel + immersion lens"를 써서 조명 아티팩트를 줄였고, 하이퍼피시아이 렌즈와 1.1 µm 픽셀 CMOS를 사용했다. — [arXiv 2411.02479](https://arxiv.org/abs/2411.02479)
- Digit 360은 GelSight가 제조·유통하고 설계와 코드는 공개된다. Sparsh, Digit Plexus와 함께 발표됐다(2024-10-31). **[원문확인: Meta 블로그]** — [Meta AI blog](https://ai.meta.com/blog/fair-robotics-open-source/); [BusinessWire](https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor/)
- **GelSight Mini 겔 [언론·기업주장/미확인(스니펫)]**: 데이터시트상 겔 두께는 4.25 ± 0.20 mm다. 2025-01-03 이후 주문분부터 내구성을 높인 신형 겔이 들어간다는 기업 발표가 있다. 공식 Shore 경도와 마커 사양은 확인하지 못했다. — [GelSight Mini datasheet (DirectIndustry)](https://pdf.directindustry.com/pdf/gelsight-inc/gelsight-mini/4602322-1082169.html); [Anzu/GelSight 발표 2025-01-06](https://www.anzupartners.com/2025/01/06/gelsight-extends-life-and-durability-of-gelsight-mini-with-new-gels/)
- **GelSlim 4.0 (MIT/UMich MMint, arXiv 2024-09-29) [원문확인]**: GelSlim 3.0을 바탕으로 손가락 구조를 단순화하고 렌즈를 제조하기 쉽게 바꿨다. 깊이와 전단장(shear field) 추정 알고리즘을 담은 오픈소스 인식 라이브러리도 함께 제공한다. 재현성은 사용자 테스트로 검증했다. — [arXiv 2409.19770](https://arxiv.org/abs/2409.19770)
- **9DTact (arXiv 2023-08-28) [원문확인]**: 반투명 겔의 광학적·변형 특성을 이용해 마커 없이 3D 형상 복원과 6D 힘 추정을 한다. 175개 물체에서 이미지-힘 약 10만 쌍을 모아 NN을 학습했고, 처음 보는 물체로도 일반화했다. — [arXiv 2308.14277](https://arxiv.org/abs/2308.14277)
- **Evetac (TU Darmstadt, arXiv 2023-12-02) [원문확인]**: RGB 카메라 대신 이벤트 카메라를 쓴다. 각인 마커로 겔 변형을 추적하며 1000 Hz로 온라인 처리하고, 498 Hz까지의 진동을 감지한다. 학습 기반 슬립 검출·예측 모델로 폐루프 파지 제어를 한다. — [arXiv 2312.01236](https://arxiv.org/abs/2312.01236)
- **TacTip 계열 [원문확인]**: Lepora(Bristol)는 광학 촉각 센서의 접촉 포즈 추정용 CNN에 대해, 네트워크와 학습 하이퍼파라미터를 Bayesian optimization으로 탐색했다. 모션 의존 전단을 비라벨 섭동으로 학습 데이터에 넣어 전단에 둔감한 모델을 얻었다. — [arXiv 2003.01916](https://arxiv.org/abs/2003.01916)

**학습 기반 디코딩, 표현 학습, 센서 간 전이**
- **Sparsh (Meta, arXiv 2024-10-31) [원문확인]**: VBTS용 자기지도 표현으로, 마스킹과 self-distillation 방식으로 46만 장 이상의 촉각 이미지에 사전학습했다. 6개 과제로 된 TacBench에서 과제·센서별 end-to-end 학습보다 평균 95.1% 우수했다. 최상위는 Sparsh(DINO)와 Sparsh(IJEPA)였다. 조명과 겔 마킹이 다른 센서들에도 하나의 인코더로 대응하는 것이 목표다. — [arXiv 2410.24090](https://arxiv.org/abs/2410.24090)
- **TransForce (arXiv 2024-09-15) [원문확인]**: 조명 색과 마커 패턴이 다른 새 센서로 이미지를 번역해 기존 이미지-힘 라벨을 재사용한다. 오차는 x 0.69 N(전 범위의 5.8%), y 0.70 N(5.8%), z 1.11 N(6.9%)이었다. 전단 방향 힘에는 마커 모달리티가, 법선 방향에는 RGB가 더 유리했다. 즉 겔 마커와 조명 설계가 학습 성능에 직접 영향을 준다. — [arXiv 2409.09870](https://arxiv.org/abs/2409.09870)

**시뮬레이션과 sim-to-real**
- **TACTO (Meta, arXiv 2020-12-15) [원문확인]**: 렌더링 기반 VBTS 시뮬레이터로 초당 수백 프레임을 낸다. DIGIT와 OmniTact를 지원하고, 100만 회 파지로 파지 안정성 예측을 학습했으며 Sim2Real 개념을 증명했다. — [arXiv 2012.08456](https://arxiv.org/abs/2012.08456)
- **Taxim (CMU, arXiv 2021-09-09) [원문확인]**: example-based GelSight 시뮬레이터다. 변형 형상을 픽셀 강도로 바꾸는 다항식 LUT를 쓰고, 마커 이동은 선형탄성과 중첩 원리로 계산한다. 실제 센서 데이터 100개 미만으로 보정하고 CPU에서 온라인으로 돈다. 기존 기법 대비 픽셀 강도 오차가 가장 낮다. — [arXiv 2109.04027](https://arxiv.org/abs/2109.04027)
- **PBR 시뮬레이터 (CMU, arXiv 2020-12-24, ICRA 2021) [원문확인]**: 물리 기반 렌더링으로 만든 최초의 범용 GelSight 광학 시뮬레이터로, 이후 설계 도구의 기반이 됐다. — [arXiv 2012.13184](https://arxiv.org/abs/2012.13184)
- **DiffTactile (arXiv 2024-03-13) [원문확인]**: 엘라스토머를 FEM 연체로 모델링한 미분가능 촉각 시뮬레이터다. 실측 데이터로 그래디언트 기반 물성 보정을 해서 sim-to-real 격차를 줄인다. 광학 응답은 픽셀 기반 신경 모듈로 추정한다. — [arXiv 2403.08716](https://arxiv.org/abs/2403.08716)
- **TacSL (NVIDIA, arXiv 2024-08-12) [원문확인]**: Isaac Sim 내 GPU 시뮬레이터로, 촉각 이미지와 접촉력 분포 생성이 이전 SOTA보다 200배 이상 빠르다. 비대칭 actor-critic distillation(AACD) RL로 sim-to-real 전이를 시연했다. — [arXiv 2408.06506](https://arxiv.org/abs/2408.06506)
- **TactileLab (arXiv 2026-11-05) [원문확인]**: IsaacLab 기반이다. 연체 물리 대신 강체 시뮬로 접촉면의 접선 운동을 계산해 "simulated tactile flow"(전단 표현)를 만든다. 실제 촉각 영상을 sim의 flow·깊이장으로 번역하는 real-to-sim 기법을 다양한 센서 설계에서 검증했다. — [arXiv 2611.07881](https://arxiv.org/abs/2611.07881)
- **RevoSim (BrainCo, arXiv 2026-11-06) [원문확인]**: Revo3 손의 압저항 taxel 285개와 시각촉각 손끝 5개를 함께 시뮬레이션한다. RTX 5090 한 장에서 최대 4,096개 병렬 환경을 돌린다. 손 안 조작 정책은 시뮬레이션에서만 학습했고, 실제 전이는 향후 과제다. — [arXiv 2611.08939](https://arxiv.org/abs/2611.08939)

**소재·광학 설계 최적화 (VBTS)**
- **OptiSense Studio (CMU Agarwal·Yuan, arXiv 2025-04-20) [원문확인]**: GelSight 설계를 목적함수 기반 최적화 문제로 정식화했다. 광학 부품을 모듈화·파라미터화하고 일반화 가능한 목적함수 4개를 둔 뒤, 물리적으로 정확한 광학 시뮬레이션 안에서 정방향·역방향으로 설계한다. GelSight 4종의 초기 설계를 시뮬레이션에서 최적화해 실제 센서로 옮겼다. — [arXiv 2504.14739](https://arxiv.org/abs/2504.14739)
- 같은 그룹의 학위논문은 이 툴박스로 기존 센서를 최적화하고 신규 센서 GelBelt의 조명을 최적화했다고 보고한다. Communications Engineering 논문은 센서 형상, 조명, 표면 소재가 성능에 미치는 영향을 정량화했다. **[미확인(스니펫)]** — [CMU 학위논문 PDF](https://www.ri.cmu.edu/app/uploads/2026/01/arpit_phd_thesis.pdf); [Illinois Experts 항목](https://experts.illinois.edu/en/publications/vision-based-tactile-sensor-design-using-physically-based-renderi/)
- **i-Tac (arXiv 2026-04-12) [원문확인]**: 3D 프린팅 촉각 엘라스토머 역설계다. PolyJet 다재료 프린팅에 상보적인 레진 3종을 쓰고, 혼합물 설계(mixture design)로 조성과 물성(투명도, 경도)을 잇는 응답곡면모델(ReSM)을 만든다. 그다음 desirability 함수 기반 다목적 최적화로 목표 투명도·경도를 내는 조성 창을 찾아 1회 제작으로 달성한다. 사용한 방법은 고전 통계/RSM이며 딥러닝은 쓰지 않았다. — [arXiv 2604.10692](https://arxiv.org/abs/2604.10692)
- **ACEL 자기발광 촉각 이미징 (arXiv 2026-11-14) [원문확인]**: 교류 전계발광(ACEL) 소자의 다공성 유전체가 압력을 발광 패턴으로 바꾼다. 기공 크기 공학으로 공간 강도 편차를 약 9배 줄이고 100 µm 특징까지 이미징한다. CMOS에 직접 적층하면 두께 5 mm 미만이 될 것으로 "예상"한다(아직 실증 전). 이 연구에서 AI는 쓰이지 않았고 소재 엔지니어링만으로 계산 복원을 없앴다는 점이 대조된다. — [arXiv 2611.19384](https://arxiv.org/abs/2611.19384)
- **SuperTac (Tsinghua SIGS 외, Nature Sensors 2026-01) [원문확인: 저자 공개 PDF]**: 비둘기의 다분광 시각에서 착안했다. 두께 1 mm의 light-field-modulated skin(전도성 고분자층, 형광층, 반사층, 지지층)에 다분광 이미징(중적외선~자외선), 마찰전기(triboelectric), 관성 센싱을 통합했다. 해상도는 0.00545 mm²/pixel이다. 힘 정확도 0.06 N, 위치 정확도 0.4 mm, 온도 0–90 °C, 근접 15 cm 미만, 진동 0–60 Hz를 낸다. 질감, 재질, 미끄럼, 충돌, 색 판별 정확도는 94% 이상이다. 위치·3D 힘 회귀 네트워크(A6000, L1 loss, AdamW)의 MSE는 위치 0.056 mm, 힘 0.0004 N이었다. 점자 26자는 글자당 200샘플로 100% 분류했다. 8.5B 파라미터 촉각 언어모델 DOVE가 해석을 맡는다. 로봇 손 통합에서는 10 DoF 3지 손의 "손바닥"에 장착했다(손끝이 아님). — [저자 공개 PDF](https://linqi-ye.github.io/docs/NATSENSORS.pdf); [NUS iHealthtech 항목](https://ihealthtech.nus.edu.sg/publication/biomimetic-multimodal-tactile-sensing-enables-human-like-robotic-perception). DOVE 파라미터 수는 일부 보도에서 850M으로 다르게 표기됐다 **[언론·기업주장]** — [Gizmochina 2026-01-21](https://www.gizmochina.com/2026/01/21/chinas-supertac-sensor-enables-human-like-touch-in-humanoid-robots/)

### Inferences
- VBTS 소재 설계의 핵심 변수(겔 탄성률, 코팅 두께·탄성률, 반사층 산란, 마커 유무와 패턴, 조명 색)는 이제 시뮬레이터에서 파라미터화된다. 설계 최적화는 이 시뮬레이터를 순환 고리로 삼는다(PBR 시뮬레이터에서 OptiSense, FEM 기반 DiffTactile). 다만 최적화기는 대체로 탐색, DoE, RSM 수준이다. Bayesian/딥 생성 설계가 VBTS 겔에 적용된 원문은 확인하지 못했다.
- 학습 쪽 흐름은 "센서 하나에 모델 하나"에서 범용 인코더(Sparsh)와 도메인 번역(TransForce)으로 옮겨가고 있다. 이는 겔·조명·마커의 제조 편차를 소재로 없애기보다 AI로 흡수하려는 방향이다.
- 2026년 하반기에는 sim-to-real의 병목이 전단 표현과 대규모 병렬화로 옮겨갔다(TactileLab, RevoSim). 연체 FEM의 정확도와 RL 스케일 사이 트레이드오프가 여전히 핵심 쟁점이다.

### Gaps
- GelSight Mini, DIGIT, Digit 360 겔의 Shore 경도 공식 수치는 원문에서 찾지 못했다. DIGIT 논문은 소재명(Solaris)만 제시하고, GelSight는 경도를 공개하지 않았다.
- Digit 360의 Ag 박막 화학증착 공정 조건과 DoE 결과 수치는 본문 일부만 확인했다.
- SuperTac의 DOI와 정확한 게재일은 저자 PDF에 나오지 않았다. 검색 스니펫상 2026-01-15다.
- 마커 패턴 자체를 ML로 최적화한 원문(예: 마커 밀도·배치 학습 최적화)은 이번 조사에서 찾지 못했다.

## Q2. 손끝 전자피부(압저항, 정전용량, 압전, 마찰전기, 자기, 이온, 다중모드): ML 신호 디코딩, 자가보정, 손상 후 전이학습, 초해상

### Takeaway
전자피부에서 ML은 주로 다음 일을 한다. 비선형·결합된 신호의 분리(force decoupling), taxel 간격보다 세밀한 위치 추정(초해상, 60배), 물체·질감·슬립 분류(대체로 83–100%), 제조와 마모 편차의 흡수(ReSkin 자기지도 학습, AnySkin 무보정 교체), 손상 후 재적응(1개 층 고정 후 200회 미만 탐침으로 재학습)이다. 언론 보도와 원문의 수치가 다른 경우가 있어 원문 대조가 필수다. 예: SNU Ko 그룹 논문의 정확도는 원문 83%, 보도 약 95%다.

### Cited Findings
- **자기 피부 초해상 (CityU/HKU/CMU, Science Robotics 2021-02-24) [원문확인: PubMed 초록]**: 두께 약 0.5 mm의 정현파 자화 유연 필름과 Hall 센서로 구성된다. 단일 유닛으로 법선력과 1차원 전단력을 분리(self-decoupling)하고, 딥러닝으로 60배 초해상 정확도를 낸다. 그리퍼 손끝에 장착해 외란 하에서 깨지기 쉬운 물체를 파지하고 원격조작으로 바늘에 실을 꿰었다. — [PubMed 34043530 / doi:10.1126/scirobotics.abc8801](https://pubmed.ncbi.nlm.nih.gov/34043530/)
- **ReSkin (Meta/CMU, arXiv 2021-10-29) [원문확인]**: 자기 센싱으로 전자회로와 수동 인터페이스(자성 입자 엘라스토머)를 분리해 닳은 피부만 교체한다. ML로 제조 편차와 시간 경과에 강건한 응답 모델을 학습하고, 자기지도 학습으로 소량의 저가 데이터만으로 미세 보정한다. — [arXiv 2111.00071](https://arxiv.org/abs/2111.00071)
- **AnySkin (NYU/Meta, arXiv 2024-09-12) [원문확인]**: ReSkin을 개선해 접착제 없이 교체 가능한 자기 촉각 피부의 제작 공정과 설계 도구를 제시했다. "보정 없이 인스턴스 간 정책 일반화"가 되는 최초의 센서라고 주장한다. LSTM 슬립 예측은 처음 보는 물체에서 92% 정확도를 냈다. 플러그 삽입 과제에서 피부를 교체하면 AnySkin 정책 성능은 13%만 떨어졌고, ReSkin은 43% 떨어져 카메라 단독 수준이 됐다. DIGIT 기반 정책은 이 정밀 과제에서 성공률이 낮았다. — [arXiv 2409.08276 (HTML v3)](https://arxiv.org/html/2409.08276v3)
- **SNU 고승환 그룹 (Nature Materials, 온라인 2025-10-24, 권호 2026-03) [원문확인: nature.com 메타데이터 초록]**: 논문명은 "Unisensory processing of interleaving memristive nanowires enabling multimodal sensing at human-scale resolution"이다. Ag 코어와 CuOx 셸의 코어-셸 멤리스티브 나노와이어 네트워크 하나가 멤리스티브 스위칭으로 열과 기계 자극을 모두 감지한다. 두 모드를 16 Hz로 전환하고, 고유 응답 시간은 기계 자극에서 서브마이크로초, 열 자극에서 밀리초 수준이다. 손끝에 센서 1개를 장착하고 ML 모델로 생활용품 20종을 83% 정확도로 식별했다. 무선 스위칭 보드와 다중 어레이도 시연했다. — [Nature Materials doi:10.1038/s41563-025-02373-w](https://www.nature.com/articles/s41563-025-02373-w)
  - **수치 충돌**: 2차 보도는 "단일 모드 약 65%에서 결합 신호 약 95%"로 보도했다 **[언론·기업주장]**. 원문 초록의 수치는 83%다. 보도의 95%는 다른 조건(다중 어레이 등)의 수치일 수 있으나 확인하지 못했다. — [Electronics For You](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robot-touch); [EurekAlert](https://www.eurekalert.org/news-releases/1133642)
  - 같은 그룹의 이전 Nature Electronics 연구는 메타러닝으로 사용자가 바뀌어도 손 제스처를 인식했다 **[미확인(스니펫)]** — [SNU webzine](https://webzine-eng.snu.ac.kr/web/snu_en/vol.05/snu_03.html)
- **Tsinghua 장이후이(Zhang Yihui) 3DAE-Skin (Science 384:987–994, 2024-05-30 Epub) [원문확인: PubMed 초록]**: 힘·변형 센서를 인간 피부의 Merkel 세포와 Ruffini 종말처럼 3D로 배치했다. 법선력, 전단력, 변형을 분리해 감지하고, 촉각 시스템으로 물체의 탄성률과 곡률을 동시에 측정한다. 과일, 빵, 케이크의 신선도별 탄성률 측정을 시연했다. 보도에 따르면 ML 기반 촉각 시스템과 결합했다고 하나, 초록은 ML을 명시하지 않는다. — [PubMed 38815009 / doi:10.1126/science.adk5556](https://pubmed.ncbi.nlm.nih.gov/38815009/); [Tsinghua 보도](https://www.tsinghua.edu.cn/en/info/1418/13543.htm)
- **손상 후 학습 기반 회복 (Cambridge/VUB, Advanced Intelligent Systems 2022-12) [미확인(스니펫)]**: Diels-Alder 자가치유 고분자에 복합 섬유를 넣은 e-skin이다. 5층 NN을 탐침 5,000회로 학습해 위치 정확도 2.3 mm, 깊이 정확도 95%를 냈다. 손상·치유 뒤 1개 층을 고정한 전이학습으로 200회 미만 탐침만에 적응했고, 전체 재샘플링·재학습으로 성능을 완전히 회복했다. 재접촉이 불충분하면 섬유가 영구 손실된다. — [DOAJ 항목](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d); [Cambridge repository](https://www.repository.cam.ac.uk/handle/1810/339730)
- **기타 ML 디코딩 수치 [미확인(스니펫)]**: 손끝 모사 stick-slip e-skin(npj Flex. Electron. 2022)은 미끄럼 검출 100.0%, 재질 분류 93.3%, 거칠기 판별 92.8%를 보고했다. 2023 Adv. Intell. Syst.의 e-skin은 형상 8종 100%, 질감 10종 99.7%를 보고했다. FBG 광섬유 인공피부(J. Lightwave Technol. 2025)는 다중입력 CNN으로 힘 R² 0.96, 직물 20종 질감 94%를 보고했다. — [npj Flex. Electron. s41528-022-00183-7](https://link.springer.com/article/10.1038/s41528-022-00183-7); [DOAJ (AIS 2023)](https://doaj.org/article/8dab11ff43ab4993b5fd6dfd055cb16d); [PolyU 저장소](https://ira.lib.polyu.edu.hk/handle/10397/117148)
- **SuperTac의 마찰전기층**: Q1을 참조한다. 두께 1 mm 피부 안에 전도성 고분자 마찰전기층을 넣어 근접과 재질 판별에 쓴다 **[원문확인]** — [저자 PDF](https://linqi-ye.github.io/docs/NATSENSORS.pdf)

### Inferences
- 자기식(ReSkin, AnySkin, 초해상 자기 피부)은 "소재(자성 엘라스토머)는 싸고 교체 가능하게, 편차는 ML로 흡수"라는 설계 철학을 가장 분명하게 실증한 계열이다. 정량 근거는 피부 교체 시 성능 하락 13%(AnySkin) 대 43%(ReSkin)다.
- 다중모드 단일 소자(Ko 그룹 멤리스티브 나노와이어)는 적층 대신 소재 자체의 스위칭으로 모달리티를 다중화한다. ML은 그 결합 신호를 분류하는 후단을 맡는다. 원문 기준 성능은 센서 1개로 83%여서, 보도된 95%보다 보수적으로 인용해야 한다.
- 손상 후 전이학습은 2022년 연구 이후 손끝 하드웨어에서 정량 후속 연구를 찾기 어려웠다. 산업 적용 단계보다는 연구 단계로 판단한다.

### Gaps
- 압저항 CNT, 그래핀, AgNW, 액체금속 손끝 e-skin을 ML로 디코딩한 최신(2025–2026) 대표 원문은 이번 조사 범위(도구 호출 제한) 안에서 확보하지 못했다.
- 이온 e-skin과 광도파로 손끝 센서의 ML 디코딩 사례도 조사하지 못했다.
- 3DAE-Skin에서 ML이 얼마나 쓰였는지(모델 종류와 정확도)는 초록만으로 확인할 수 없었다.

## Q3. 센싱 소재·구조 자체를 AI로 설계하는 연구 (역설계, BO, 미세구조 최적화, 형상·마커·배치 생성 설계)

### Takeaway
"소재·구조 AI 설계"는 정량 성과가 나오기 시작했다. 대표 사례는 소량 데이터 ML 역설계로 기존 방식보다 4자릿수 이상 효율을 높였다는 2023년 연구, SVM 경계 정의와 이중 능동학습을 결합한 역설계로 1.2 V/kPa·R² 0.999·0–400 kPa를 달성한 2026년 Adv. Sci. 논문, 그리고 VBTS의 광학·엘라스토머 최적화(OptiSense, i-Tac)다. 로봇 손 수준에서는 taxel 배치를 접촉 통계로 정하면 균일 배치보다 훨씬 적은 taxel로 같은 성능을 낸다는 결과가 2026-11에 나왔다.

### Cited Findings
- **Inverse design of artificial skins (arXiv 2023-04-10) [원문확인]**: 소량 데이터 ML로 물성에서 구조를 찾는 역설계를 했다. 종합 효율이 기존 정방향 시행착오 대비 최소 4자릿수 높다. 선형 응답을 위해 신호 포화를 극복하는 해 수백 개를 수 시간 안에 예측했고, 여러 소재에 유효했다. 미세구조는 필러(pillar)형이다(스니펫). — [arXiv 2304.04609](https://arxiv.org/abs/2304.04609)
- **Customizing Tactile Sensors via ML-Driven Inverse Design (Wang B. et al., Advanced Science, 2026-01-28) [원문확인: Europe PMC 초록]**: 데이터 효율적인 미세구조-물성 예측기를 만들었다. SVM으로 실현 가능 경계를 정하고 이중 단계 능동학습을 결합했다. 이 예측기로 다목적 역설계 소프트웨어를 구동해 실시간 맞춤 설계를 한다. 결과 센서는 감도 1.2 V/kPa, 선형성 R² 0.999, 범위 0–400 kPa이고 맥박 측정, 재질 식별, 로봇 파지에 적용됐다. 해석 가능 ML로 미세구조-물성 메커니즘도 분석했다. — [Europe PMC / doi:10.1002/advs.202524250](https://europepmc.org/search?query=DOI%3A10.1002%2Fadvs.202524250)
- **OptiSense Studio (2025-04)와 i-Tac (2026-04)**: Q1을 참조한다. 각각 GelSight 광학 설계와 3D 프린팅 엘라스토머 조성(투명도, 경도)의 역설계다 **[원문확인]** — [arXiv 2504.14739](https://arxiv.org/abs/2504.14739); [arXiv 2604.10692](https://arxiv.org/abs/2604.10692)
- **Digit 360 엘라스토머 DoE와 산란 최적화**: Q1을 참조한다. 6개 소재·형상 파라미터를 DoE로 식별했고, 반사층 산란은 시뮬레이션 최적화로 Lambertian으로 정했다 **[원문확인]** — [arXiv 2411.02479](https://arxiv.org/abs/2411.02479)
- **AnySkin 설계 도구 [원문확인]**: 자기 피부 형상을 위한 설계 도구와 제작 공정을 제시했다. 최적화 알고리즘 여부는 초록에 없다. — [arXiv 2409.08276](https://arxiv.org/abs/2409.08276)
- **"Which Taxels, Not How Many" (arXiv 2026-11-07) [원문확인]**: 로봇 손 3종의 손바닥 내 회전과 파지에서 실험했다. 교사, 학습 절차, 후보 taxel을 고정하고 센서 구성만 바꿨다. 접촉 통계로 고른 소수 taxel이 훨씬 큰 균일 배치와 같은 성능을 냈다. 드물게 접촉되는 위치의 taxel은 촉각 입력이 없는 것과 같았다. 즉 균일 배치는 필요 taxel 수를 과대평가한다. 손 피부 소재의 배치 설계를 데이터 기반으로 정하는 근거가 된다. — [arXiv 2611.10647](https://arxiv.org/abs/2611.10647)
- **BO의 다른 쓰임 [원문확인]**: 촉각 소재가 아니라 컴플라이언트 센서화 손의 파지 전략에 BO를 쓴 연구(arXiv 2024-10-23)가 있다. TacTip CNN 하이퍼파라미터 BO는 Q1을 참조한다. — [arXiv 2410.18237](https://arxiv.org/abs/2410.18237); [arXiv 2003.01916](https://arxiv.org/abs/2003.01916)
- 레이저 유도 그래핀(LIG) 촉각 센서의 제조 파라미터를 SVM 기반 ML과 통계 기준으로 선정한 연구(Lu et al., Adv. Sci. 2023)가 있다 **[미확인(스니펫)]** — [DOAJ](https://doaj.org/article/09425e03a42b4bbe9b0c376474d44267)

### Inferences
- e-skin 쪽 역설계(미세구조에서 감도·선형성·범위)는 "소량 데이터 + 능동학습 + 다목적 최적화" 패턴으로 수렴하고 있다. 손끝용 압력센서의 고질적 트레이드오프(고감도 대 선형·넓은 범위)를 R² 0.999, 0–400 kPa로 동시에 만족시킨 것이 대표 성과다. 다만 대상은 압력 패드형 센서이고, 곡면 손끝 형상의 역설계 실증은 확인하지 못했다.
- VBTS 쪽은 물리 시뮬레이터를 순환 고리로 쓰는 최적화이며, 학습형 surrogate나 생성모델은 아직 드물다. 미분가능 시뮬레이터(DiffTactile)가 소재 물성 역추정에 쓰이고 있어 다음 단계 후보가 될 수 있다(추론).

### Gaps
- 복합재 배합(예: CNT/PDMS 농도)을 Bayesian optimization으로 최적화한 손끝 센서 원문은 이번 조사에서 확보하지 못했다.
- 손끝 형상이나 마커 패턴을 생성 설계(딥 생성모델)로 만든 원문도 찾지 못했다.

## Q4. 상용·준상용 덱스터러스 핸드의 손끝 촉각 통합과, 촉각 손끝으로 가능해진 학습 기반 조작 성과

### Takeaway
휴머노이드 기업의 손끝 촉각 사양은 대부분 기업 주장이다. Figure 03은 3 g, Sanctuary는 5 mN이며 Tesla는 정량 사양 공개를 확인하지 못했다. 소재와 방식은 대부분 비공개다. 반면 학계와 오픈 하드웨어(Meta Digit 360/Plexus, Shadow STF, BrainCo Revo)에서는 촉각 손끝을 쓴 학습 성과가 수치로 나온다. 예: 시각 가림 시 추적 94% 개선, 블라인드 Baoding 225회 연속 회전, 촉각 사전학습으로 성공률 52.5%에서 71.7%.

### Cited Findings
**기업 손끝 촉각**
- **Figure 03 (Figure AI, 2025-10-09 발표) [원문확인: figure.ai 공식 페이지, 수치는 기업주장]**: 시장 제품의 내구성 한계 때문에 1세대 촉각 센서를 자체 개발했다고 한다. 설계 원칙은 극한 내구성, 장기 신뢰성, 고충실도 센싱이다. 각 손끝 센서는 3 g의 힘까지 감지하고, 이로써 Helix가 슬립을 사전에 구분한다고 주장한다. 손끝을 더 부드럽고 적응적으로 만들어 접촉 면적을 늘렸고, 손바닥 카메라를 갖췄다. 센싱 원리와 소재는 공개하지 않았다. — [Figure: Introducing Figure 03](https://www.figure.ai/news/introducing-figure-03)
- **Sanctuary AI Phoenix (2025-02-26) [언론·기업주장]**: 새 촉각 센서로 블라인드 피킹, 슬립 검출, 과도한 힘 제한이 가능하다고 한다. 보도에 따르면 손가락 패드마다 7셀 센서가 있고 5 mN까지 감지한다(인간 약 3 mN). 센싱 방식은 공개하지 않았다. 세대 표기는 보도마다 7세대와 8세대로 엇갈린다. — [BusinessWire](https://www.businesswire.com/news/home/20250226807548/en); [The Rundown](https://robotnews.therundown.ai/p/sanctuarys-touchy-feely-humanoid)
- **Tesla Optimus [언론·기업주장/미확인]**: 2024-11 공개된 손은 22 DoF에 손목·전완 3 DoF가 더해지고 힘줄 구동 방식이다. 2024년 보도는 촉각 통합이 진행 중이라고 했다. 이후 일부 매체는 Gen 3 손끝 촉각 센서와 "4배 감도"를 언급하지만 신뢰도가 낮고 공식 사양은 확인하지 못했다. — [Electrek 2024-11-29](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/); [The Decoder](https://the-decoder.com/tesla-gives-optimus-robot-a-new-hand-with-improved-grip-and-sensors/)
- **Shadow Robot [미확인(스니펫)/기업 페이지]**: "DexTip"이라는 이름의 제품은 확인하지 못했다. Shadow Tactile Fingertip(STF)은 광학식이고 0.01–80 N 범위라고 한다. 데이터시트 스니펫에 따르면 손끝당 17 taxel × 3축 자기장, 51 스트림, 12 bit @ 1 kHz다. Shadow Hand에는 엄지와 검지에 STF가 기본 장착된다. 2026-06 ICRA에서 Shadow 손에 다른 촉각 손끝이 통합 시연됐다는 ARIA 글이 있다. — [Shadow sensors](https://shadowrobot.com/sensors/); [DEX-EE 사양 PDF](https://shadowrobot.com/wp-content/uploads/2026/05/Shadow-DEX-EE-Series-Technical-Specifications.pdf); [ARIA 2026-07-30](https://aria.org.uk/insights/giving-robot-hands-a-sense-of-slip)
- **Meta Digit Plexus (2024-10-31) [원문확인: Meta 블로그]**: 손끝과 손바닥 촉각 센서를 하나의 손에 통합하는 표준화된 하드웨어·소프트웨어 플랫폼이다. Wonik Robotics가 Plexus 기반 차세대 Allegro Hand를 제조·유통하고 "내년"(2025) 출시할 예정이라고 발표했다. — [Meta AI blog](https://ai.meta.com/blog/fair-robotics-open-source/)

**촉각 손끝 기반 학습 조작 성과**
- **NeuralFeels (Meta/CMU, arXiv 2023-12-20; Science Robotics 2024) [원문확인]**: 다지 손에서 시각과 촉각(DIGIT)으로 신경장을 온라인 학습하고 포즈 그래프로 추적한다. 재구성 F-score는 81%, 평균 포즈 드리프트는 4.7 mm(CAD를 알 때 2.3 mm)다. 시각 가림이 심할 때 시각 단독 대비 추적이 최대 94% 개선됐다. — [arXiv 2312.13469](https://arxiv.org/abs/2312.13469)
- **AnyRotate (Bristol, arXiv 2024-05-12) [원문확인]**: 시뮬레이션에서 학습한 고밀도 촉각 정책을 제로샷으로 전이해, 중력 방향과 무관하게 다축 손 안 회전을 한다. 다지 촉각이 불안정 파지를 감지해 반응적 행동을 만든다. — [arXiv 2405.07391](https://arxiv.org/abs/2405.07391)
- **RotateIt (Meta/Berkeley, arXiv 2023-09-18) [원문확인]**: 시각촉각 트랜스포머로 물체 형상과 물성을 온라인 추론하며 손끝 기반 다축 회전을 한다. — [arXiv 2309.09979](https://arxiv.org/abs/2309.09979)
- **블라인드 Baoding (arXiv 2026-10-16) [원문확인]**: Shadow Dexterous Hand Lite에서 고유감각과 이진 촉각만 사용했다. 센서 정렬 시뮬레이션, 촉각 보정, "STuck-AT Taxels" 도메인 랜덤화로 제로샷 전이했다. 180° 회전 225회 연속(112.5바퀴, 약 0.36 rot/s)을 비전 없이 달성했다. 저자들은 감각 방식과 무관하게 하드웨어 최고 기록이라고 주장한다. — [arXiv 2610.23438](https://arxiv.org/abs/2610.23438)
- **Spark-0 (arXiv 2026-10-15) [원문확인]**: 시각-촉각-언어-행동(VTLA) 모델이다. 1,000시간 분량의 전손 촉각 인간 조작 데이터셋 HumanTouch로 사전학습했다. 같은 데이터와 연산에서 촉각을 버린 경우보다 Ego Humanoid 벤치 vision-only 성공률이 52.5%에서 71.7%로 올랐다. — [arXiv 2610.22342](https://arxiv.org/abs/2610.22342)
- **TMA (arXiv 2026-11-13) [원문확인]**: 시뮬레이션에서만 학습한 촉각 기반 모터 적응 정책을 Unitree G1과 BrainCo Revo2 손에 제로샷 전이했다. 상용 원형 문손잡이 4종 열기에서 RMA와 반응형 촉각 기준선을 크게 능가했다. — [arXiv 2611.18976](https://arxiv.org/abs/2611.18976)
- **AnySkin 정책 전이와 Evetac 폐루프 파지**: Q1과 Q2를 참조한다 **[원문확인]**.

### Inferences
- 기업들의 손끝 감도 주장(Figure 3 g ≈ 0.03 N, Sanctuary 5 mN)은 측정 조건이 공개되지 않았다. 같은 기준으로 연구용 Digit 360(1.01 mN 분해능)과 비교할 수 없다.
- 2026년 학습 성과의 흐름은 두 가지다. (a) 저해상도·이진 촉각이라도 시뮬레이션 정합과 랜덤화를 잘 하면 강한 성능이 나온다(Baoding, TMA). (b) 대규모 인간 촉각 데이터 사전학습이 vision-only 정책까지 끌어올린다(Spark-0). 소재 측면에서는 "고해상도 겔"보다 "내구성 있고 시뮬레이션하기 쉬운 피부"가 정책 학습에 유리하다는 신호로 읽힌다. 이는 AnySkin의 DIGIT 대비 결과와도 일관된다(추론).

### Gaps
- Tesla Optimus 손끝 촉각의 방식과 수치, Figure 03 촉각 센서의 소재와 원리는 공식 공개 자료가 없다.
- Wonik Allegro Hand의 Digit Plexus 통합판 출시 여부(2025)는 확인하지 못했다.
- Shadow "DexTip"이라는 명칭의 제품은 찾지 못했다(STF 또는 DEX-EE의 다른 명칭일 가능성이 있다).

### 접근 상태 로그
| Host | 결과 | 목적 |
|---|---|---|
| WebFetch 도구 | 사용 안 함(세션에서 DNS 실패로 알려짐) | — |
| export.arxiv.org (http) | 실패(DNS) | arXiv API |
| export.arxiv.org (https API), arxiv.org/abs·pdf·html | 성공 | 초록 25건 이상, DIGIT·Digit 360 PDF 본문, AnySkin HTML |
| eutils.ncbi.nlm.nih.gov | 성공 | Sci Robot 2021 자기 피부, Science 2024 3DAE-Skin 초록 |
| www.ebi.ac.uk (Europe PMC REST) | 성공 | Adv. Sci. 2026 역설계 초록 |
| www.nature.com | 성공(메타데이터) | Nature Materials Ko 그룹 초록, 날짜, DOI |
| linqi-ye.github.io | 성공(PDF) | SuperTac 저자 공개 원고 |
| www.figure.ai | 성공 | Figure 03 촉각 3 g 원문 |
| ai.meta.com | 성공 | Digit 360, Sparsh, Plexus, Wonik |
| ihealthtech.nus.edu.sg | 응답했으나 관련 텍스트 추출 실패 | SuperTac 서지 |
| anzupartners.com | 응답했으나 본문 추출 실패 | GelSight Mini 신형 겔 |
| Science/Wiley/Springer 출판사 사이트 | 미시도(Cloudflare 예상), 대신 PubMed와 Europe PMC 사용 | — |
| WebSearch | 성공(14회) | 탐색, 스니펫 |
