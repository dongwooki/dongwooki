# 로봇 손가락의 구조·구동·표면 소재에 대한 AI/ML 적용 현황 (촉각 센싱 제외)

작성 기준일: 2026-11-18. 표기: **[원문확인]** = 원 논문의 초록 또는 본문을 직접 읽음(arXiv abs, nature.com, Europe PMC 초록). **[언론·기업주장]** = 보도자료·언론·기업 자료. **[미확인(스니펫)]** = 검색 스니펫이나 2차 요약만 봄. 날짜는 게재일(또는 arXiv 최초 제출일)입니다.

## 1. 소프트 손가락·그리퍼: FEM 대리모델, 역설계/생성설계, 엘라스토머 배합 최적화, Fin-Ray, 메타물질 손끝, 가변강성

### Takeaway
2026년 기준으로 가장 구체적인 "AI로 손가락 소재 자체를 설계한" 사례는 KAIST·KIST·SeoulTech의 Nature Communications 논문(2026-06-04)입니다. 33개 배합 데이터와 회귀 대리모델로 DLP 인쇄 가능한 엘라스토머를 찾았습니다. 점도는 약 2,500 mPa·s, 파단 연신율은 600% 초과이며, 3지 공압 그리퍼가 1 kg 물병과 달걀을 집었습니다. 다만 이 연구는 베이지안 최적화(BO)가 아니라 회귀 대리모델 기반 선택이고, 저자들도 GP+BO는 향후 과제라고 적었습니다. 형상 측면에서는 "FEM 데이터 → 신경망 대리모델 → GA/NSGA-II/BO/RL" 파이프라인이 표준이 되었습니다. 반면 가변강성(재밍·LMPA·SMP) 손가락에 ML을 적용한 연구는 거의 찾지 못했습니다.

### Cited Findings
**(a) AI 최적화 3D 프린팅 엘라스토머 (KAIST·KIST·SeoulTech)**
- 논문: Song Y., Park B., Jeon S., Kweon H., Lee S.(이승철, KAIST), Na J., "Machine learning guided formulation design of digital light processing printable elastomers beyond viscosity stretchability tradeoff", *Nat. Commun.* 17, 7167. 접수 2025-10-14, 수락 2026-05-18, 온라인 게재 2026-06-04, Version of record 2026-07-24. 오픈액세스. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 배합 공간: 아크릴레이트 4성분(PUDA 폴리우레탄 디아크릴레이트, IBOA, EHMA, MAA). 인쇄 불가능한 고점도 배합도 일부러 포함해, 모델이 인쇄 가능 경계를 외삽하지 않고 학습하도록 했습니다. 소량 몰드 경화로 물성을 측정해 "프린팅 제약과 물성 측정을 분리"한 것이 핵심 기법입니다. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 데이터와 모델: 33개 배합을 실험 측정했습니다. 학습 대상은 점도(η), 인장탄성률(E), 파단 연신율(ε), 특성 경화시간(t100)의 회귀 대리모델입니다. 교차검증 R²는 점도 0.870±0.052, 연신율 0.645±0.374, 탄성률 0.768±0.149, t100 0.839±0.120입니다. 연신율 예측 정확도는 상대적으로 낮습니다. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 결과: ML 추천 레진(MLR)의 배합비는 PUDA:IBOA:EHMA:MAA = 50:30:16:4 wt%입니다. 점도는 약 2,500 mPa·s로, 상용 DLP 레진 요구 기준인 5,000 mPa·s 미만을 만족합니다. 파단 연신율은 600% 초과입니다. 비교로, PUDA 80 wt% 배합은 점도가 약 3.5×10⁴ mPa·s여서 인쇄할 수 없었습니다. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 내구성: 200% 변형 100사이클에서 잔류변형이 약 10사이클 후 약 30%로 안정화되었습니다. 공압 액추에이터 50회 구동 후 X선 현미경(XRM)으로 내부 손상을 평가했습니다. 액추에이터는 0, 70, 150 kPa에서 순차 굽힘을 보였고, FEM 예측 팁 변위와 비교 검증했습니다. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 그리퍼: 3개 액추에이터(각각 굽힘 세그먼트 6개 직렬)로 구성했습니다. 물을 채운 1 kg 플라스틱 병을 들어 옮겼고, 유리병·달걀·달걀판·컴퓨터 마우스를 흔들어도 미끄러짐이나 손상 없이 파지했습니다. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 저자들은 데이터셋이 작아 일반화에 한계가 있을 수 있다고 인정했습니다. GP 대리모델과 BO를 이용한 순차 실험설계는 향후 과제로 명시했습니다. 따라서 이 연구를 "BO로 최적화했다"고 표현하면 부정확합니다. [원문확인] — [Nature Communications](https://www.nature.com/articles/s41467-026-73735-4)
- 보도자료는 2026-09-01 KAIST가 배포했습니다. 언론 일부는 "1 kg"을 "1리터 병"으로 표기했고, "6배 이상 늘어난다"는 표현도 썼습니다(원문의 600% 초과와 일치). [언론·기업주장] — [EurekAlert/KAIST](https://www.eurekalert.org/news-releases/1142057), [Interesting Engineering](https://interestingengineering.com/ai-robotics/soft-robotic-hand-grips-fragile-eggs), [KAIST 국문](https://www.kaist.ac.kr/news/html/news/?mode=V&mng_no=66470)

**(b) FEM 대리모델과 형상 역설계**
- SPADA (Yao, He, Maiolino, arXiv 2023-05-31): 벨로우즈형 공압 액추에이터를 다룹니다. FEM 데이터로 학습한 ANN 대리모델을 GA 안에 넣고, 3D 조각별 일정곡률(PCC) 분할과 결합해 목표 형상에 맞는 설계변수를 역산합니다. 2D 목표형상 정합 RMSE는 4.16, 2.70, 2.51 mm이고, 오픈소스 GUI 툴박스로 공개되었습니다. [원문확인] — [arXiv:2305.19509](https://arxiv.org/abs/2305.19509)
- Generalized Task-Driven Design (Yao, Howard, Maiolino, arXiv 2026-03-20): 모듈 단위 고충실도 FEM에서 축소차수 대리 관절모델을 만들고, 이를 의사강체모델(PRBM)에 넣습니다. 메타모델이 설계변수를 대리모델로 사상합니다. 벨로우즈 공압 액추에이터와 텐던 구동 소프트 손가락에서 sim-to-real을 검증했고, RL 기반 소프트 그리퍼 co-design과 진화최적화 형상정합을 시연했습니다. 초록에 정량 수치는 없습니다. [원문확인] — [arXiv:2603.19794](https://arxiv.org/abs/2603.19794)
- Co-Design of Soft Gripper with Neural Physics (arXiv 2025-05-26): 플렉셔 기반 소프트 손가락의 블록별 강성분포와 파지 자세를 동시에 최적화합니다. 균일압력 텐던 모델로 시뮬레이션 데이터셋을 만들고, 미분 가능한 신경망 대리모델을 학습해 end-to-end로 최적화했습니다. 강성은 구조 파라미터로 바꿔 3D 프린팅했습니다. 초록은 "기준 설계 대비 시뮬레이션·하드웨어 모두에서 유의하게 우수"하다고만 적었고 수치는 없습니다. [원문확인] — [arXiv:2505.20404](https://arxiv.org/abs/2505.20404)
- PINN-Ray (arXiv 2024-07-11): Fin-Ray 손가락 변형을 모델링하는 물리정보신경망입니다. 최소 퍼텐셜에너지 원리와 실험 데이터를 손실함수에 넣었습니다. 데이터 동화를 적용한 뒤 FEM보다 높은 정확도를 보였다고 주장합니다. [원문확인] — [arXiv:2407.08222](https://arxiv.org/abs/2407.08222)
- 물리유도 딥러닝 대리모델(공압 소프트 손가락, IEEE RA-L, 2024-12)도 있다는 검색 요약을 봤지만 원문은 확인하지 못했습니다. [미확인(스니펫)] — [ORA Oxford](https://ora.ox.ac.uk/objects/uuid:699fe236-f1cd-4ce4-92a2-7e00acb34bdb)

**(c) Fin-Ray 손가락의 ML·최적화 설계**
- Ghanizadeh 외 (arXiv 2025-05-31, 오류 수정 후 major revision): FEM 120회로 원통 파지 데이터셋을 만들었습니다. 설계변수 3개(전면·지지 빔 두께, 크로스빔 두께, 크로스빔 간격)를 입력으로, 접촉력과 2방향 팁 변위를 출력으로 하는 MLP를 학습했습니다. 최대 접촉력과 최대 팁 변위의 상충관계는 NSGA-II로 파레토 해를 구했습니다. 직접 탐색에는 FEM이 약 50,000회 필요하다고 언급합니다. 결과는 시뮬레이션 중심입니다. [원문확인] — [arXiv:2506.00494](https://arxiv.org/abs/2506.00494); 50,000회 수치는 [미확인(스니펫)] — [arXiv html v1](https://arxiv.org/html/2506.00494v1)
- Fin-Bayes (Wang X., Wang B., Pinskier J., Xie Y., Brett J., Scalzo R., Howard D., CSIRO 계열): 형상·재료·접촉 비선형을 고려한 FEM과 다목적 BO로 순응성(compliance)과 접촉력을 동시에 최적화합니다. 자동 시험 리그와 인쇄된 손가락으로 FEM을 검증했습니다. Scopus 인용은 24회입니다. 게재지와 연도는 확인하지 못했습니다. [원문확인(초록 일부)] — [University of Canberra 포털](https://researchprofiles.canberra.edu.au/en/publications/fin-bayes-a-multi-objective-bayesian-optimization-framework-for-s/)
- Fin-QD (arXiv 2023-11-21): 손가락 배치까지 포함한 설계변수 28개 공간을 다룹니다. SOFA 기반 접촉 FEM으로 MAP-Elites 품질다양성 탐색을 수행해, 형상이 서로 다른 물체별로 다양한 그리퍼 설계를 생성합니다. [원문확인] — [arXiv:2311.12477](https://arxiv.org/abs/2311.12477)
- MAP-Elites와 위상최적화의 결합 (arXiv 2024-07-10): 설계영역 안의 가변 크기 공극(void) 위치와 크기를 진화시켜 소프트 그리퍼의 파지 성능을 높였습니다. [원문확인] — [arXiv:2407.07591](https://arxiv.org/abs/2407.07591)
- Deng & Li, "Learning Optimal Fin-Ray Finger Design for Soft Grasping" (*Front. Robot. AI*, 2021-02): 감김수(winding number)를 파지 품질 함수로 써서 물체별 최적 Fin-Ray 형상을 학습합니다. [미확인(스니펫)] — [PMC7907605](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7907605/)
- 모듈식 몰드와 실제 집기 실험을 반복 루프에 넣은 "reality-assisted BO" 실리콘 손가락 연구도 있습니다(IEEE, 서지 미확인). [미확인(스니펫)] — [IEEE Xplore 10121997](https://ieeexplore.ieee.org/abstract/document/10121997)

**(d) 메타물질·격자 손가락과 손끝**
- TU Delft, 3D 프린팅 경사 격자 다중강성 손가락 (arXiv 2025-01-07, RoboSoft 2025로 보도): 복셀 크기와 단위셀 형상으로 강성을 세밀하게 조정하는 격자를 한 번에 인쇄합니다. 인간형 손가락과 그리퍼로 pick-and-place를 시연했습니다. 초록상 최적화가 ML인지는 명시되어 있지 않습니다. [원문확인] — [arXiv:2501.03763](https://arxiv.org/abs/2501.03763)
- 심층 RL로 메타물질 메커니즘 설계 (arXiv 2024-08-08): 설계영역을 셀과 힌지 조합으로 이산화하고 FEA 데이터로 RL을 수행했습니다. 도어래치 메커니즘에서 인간 설계 대비 보상이 3배였습니다. 소프트 그리퍼 메커니즘으로 확장해 적층제조로 만들고 실험 검증했습니다. [원문확인] — [arXiv:2408.04376](https://arxiv.org/abs/2408.04376)
- CAD·FEM·BO를 결합한 근영(near-zero) 포아송비 메타물질 그리퍼의 "Autonomous Design Discovery" 연구도 있습니다. [미확인(스니펫)] — [IMECE 포스터](https://imece.secure-platform.com/a/solicitations/261/sessiongallery/21465/application/165069)
- 토마토 수확용 옥세틱 격자 하이브리드 6지 그리퍼 (arXiv 2025-10-11): 셀 경사 0°, 30°, 45°, 60°를 FEA와 DIC로 비교했습니다. ML은 쓰지 않은 매개변수 연구입니다. [원문확인] — [arXiv:2510.10016](https://arxiv.org/abs/2510.10016)

**(e) 다중소재 3D 프린팅**
- Vision-controlled jetting (Buchner 외, Matusik, Katzschmann; ETH·MIT·Inkbit, *Nature* 2023-11-15): 스캐닝 피드백 루프로 기계식 평탄화기를 없앴고, 그 덕분에 천천히 경화되는 화학계(티올-엔 등)까지 쓸 수 있습니다. 뼈·인대·텐던을 갖춘 텐던 구동 손을 한 번에 인쇄했습니다. 이 피드백은 "AI 설계"가 아니라 공정 비전 제어입니다. [원문확인(초록)] — [Europe PMC/Nature 10.1038/s41586-023-06684-3](https://www.nature.com/articles/s41586-023-06684-3). 독립 구동 텐던 19개라는 수치는 [언론·기업주장] — [Inkbit/BusinessWire](https://businesswire.com/news/home/20231114468127/en/5556293/Inkbit-Demonstrates-Single-Print-Fabrication-of-Complex-Multi-Functional-Systems-and-Robots)
- 계층적 성능기반 다지 소프트 그리퍼 설계 프레임워크 (arXiv 2024-11-09): Task, Motion, Design의 3계층으로 나누고, Design 계층에서 형상과 재료분포를 매개변수·위상 최적화합니다. 개념 프레임워크이며 정량 결과는 초록에 없습니다. [원문확인] — [arXiv:2411.06294](https://arxiv.org/abs/2411.06294)

**(f) 가변강성 손가락**
- LMPA 사례: 인듐-주석 LMPA(융점 47 °C)와 히팅와이어를 넣은 공압 손가락에 전기접착을 결합했습니다(*Polymers* 2022). Field's metal 입자/실리콘 복합재(Buckner 외 2019)도 있습니다. 둘 다 ML은 쓰지 않았습니다. [미확인(스니펫)] — [PMC9657554](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9657554/), [Yale Faboratory PDF](https://www.eng.yale.edu/Faboratory/publications/journal/2019/Buckner%20et%20al.%20-%202019%20-%20Enhanced%20Variable%20Stiffness%20and%20Variable%20Stretchability%20Enabled%20by%20Phase%E2%80%90Changing%20Particulate%20Additives.pdf)

### Inferences
- 손가락 "소재"의 AI 설계는 배합(재료 화학) 수준과 구조(형상·강성분포·격자) 수준으로 나뉩니다. 2026년까지 정량 성과가 뚜렷한 쪽은 구조 수준입니다. 데이터는 수백~수천 회 FEM이 일반적이고, Fin-Ray 연구는 120회였습니다. 배합 수준은 KAIST 연구처럼 실험 수십 개(33개) 규모의 소데이터 회귀가 현재 수준입니다.
- 대리모델 정확도가 연신율처럼 파괴와 관련된 물성에서 낮다는 점(R² 0.645±0.374)은 내구성과 피로 같은 손가락 수명 지표를 ML로 예측하기가 아직 어렵다는 신호로 해석됩니다.
- 가변강성 손가락(재밍·LMPA·SMP)과 ML의 결합은 공백 영역으로 보입니다.

### Gaps
- Ecoflex, Dragon Skin, TPU 각각의 초탄성 상수를 ML로 보정한 손가락 특화 연구는 정량 원문을 확보하지 못했습니다.
- 재밍·SMP 손가락에 ML을 적용한 사례는 검색에서 찾지 못했습니다.
- Fin-Bayes의 게재지·연도·정량 결과, reality-assisted BO의 서지사항은 미확인입니다.

## 2. 손가락 구동 소재: 인공근육(SMA, TCP/나일론, HASEL, DEA, LCE)과 바이오하이브리드

### Takeaway
인공근육 분야에서 ML의 역할은 대부분 히스테리시스와 비선형 동역학을 보상하는 학습 모델(LSTM, RNN, MLP)에 머뭅니다. 손가락용 인공근육 "소재"를 ML로 설계한 원문 사례는 찾지 못했습니다. 바이오하이브리드 분야에서는 도쿄대 Takeuchi 그룹의 18 cm 인간근육 구동 손(Science Robotics, 2025-02)이 대표 성과입니다. 근조직 다발 하나의 수축력은 약 8 mN, 수축 길이는 약 4 mm이며, AI는 쓰지 않았습니다.

### Cited Findings
- Ren, Morimoto, Takeuchi, "Biohybrid hand actuated by multiple human muscle tissues", *Sci. Robot.* (2025-02-12, DOI 10.1126/scirobotics.adr5512): 얇은 근조직을 다발로 만든 MuMuTA를 케이블 구동으로 다관절 손가락 굴곡에 연결했습니다. 수축력 약 8 mN, 수축길이 약 4 mm이고, 손가락을 개별 제어했습니다. [원문확인(초록)] — [DOI (Europe PMC 초록 확인)](https://doi.org/10.1126/scirobotics.adr5512)
- 같은 연구의 보도 내용: 손 길이 18 cm, 10분 동작 후 피로가 왔다가 1시간 휴식 후 회복했습니다. 무거운 물체는 쥘 수 없고, 텐던 앵커 마찰을 피하려고 액체 속에 매달아야 합니다. [언론·기업주장] — [EurekAlert/U Tokyo](https://www.eurekalert.org/news-releases/1072918), [News-Medical](https://www.news-medical.net/news/20250214/Biohybrid-hand-with-muscle-tissue-mimics-real-life-movements.aspx)
- Peano-HASEL 구동 근골격 인간형 손 (arXiv 2026-03-25): 액추에이터를 전완에 배치하고, 1:2 풀리로 텐던 변위를 증폭했습니다. 운용 전류만 모니터링해 파지를 감지하고 접촉 인지 폐루프를 구현했습니다. 종이풍선 같은 초취약 물체를 비파괴로 파지했습니다. 제어는 규칙 기반이며 ML은 쓰지 않았습니다. [원문확인] — [arXiv:2603.24357](https://arxiv.org/abs/2603.24357)
- HASEL 시스템에 RNN과 MLP를 이용한 패턴매칭 예측제어를 적용한 연구(Dong, 2022)가 있습니다. [미확인(스니펫)] — [Bohrium](https://www.bohrium.com/paper-details/machine-learning-amplified-control-system-for-hasel-actuator-soft-robot-system/864971402757800208-15541)
- 길항 배치 TCP(twisted-coiled polymer) 액추에이터에 LSTM 모델과 MPC를 결합해 위치·강성을 제어한 연구가 있습니다. TCP 자체의 저항 변화를 이용한 자가감지 소프트 손가락(Sun & Zhao)도 있습니다. [미확인(스니펫)] — [NSF PAR](https://par.nsf.gov/servlets/purl/10231284), [Actuators 2023/DOAJ](https://doaj.org/article/19d248f2fc224e04a6e255bcb66b4610)

### Inferences
- 손가락 인공근육에서 AI는 "소재 발견"보다 "소재의 비선형성을 감추는 제어 계층"으로 먼저 들어왔습니다. 대표적 대상은 TCP의 열 히스테리시스와 HASEL의 전기기계 비선형성입니다.
- 바이오하이브리드 손가락은 힘이 mN 수준이고 액중 구동이 필요해, 실용 파지 단계와는 거리가 멉니다.

### Gaps
- SMA 와이어 손가락, DEA 손가락, LCE 손가락에 ML로 설계하거나 제어한 사례는 이번 검색 예산에서 원문을 확보하지 못했습니다. LCE+ML 그리퍼는 검색에서 찾지 못했습니다.
- 인공근육 섬유 소재(나일론 등급, 코일 파라미터)를 ML로 최적화한 손가락 응용은 미확인입니다.

## 3. 텐던·관절: 텐던 소재(UHMWPE/Dyneema, Vectran, 강선), 크리프·마모, 마찰 보상 ML, 구름접촉·플렉셔 관절

### Takeaway
텐던 관련 AI 성과는 대부분 "텐던 힘·마찰의 데이터 기반 모델"입니다. 가장 최근의 정량 사례는 트랜스포머 기반 텐던 힘 모델입니다(arXiv 2026-03). 오차가 최대 모터 힘의 3% 이내이고, sim-to-real 격차를 41% 줄였으며, RL 손끝 자세 추종을 50% 개선했습니다. Dyneema와 Vectran의 크리프·마모를 ML로 모델링한 손가락 연구는 찾지 못했습니다.

### Cited Findings
- Tendon Force Modeling for Sim2Real (arXiv 2026-03-04): 서보 구동 텐던 손가락에서 접촉이 많은 상황의 텐던 힘을 측정하는 전용 테스트벤치를 만들었습니다. 이력(context history)을 쓰는 트랜스포머 모델의 예측 오차는 최대 모터 힘 대비 3% 이내입니다. 이 모델을 GPU 가속 시뮬레이션에 넣어 시험 궤적의 sim-to-real 격차를 41% 줄였고, 실물 손끝 자세 추종을 50% 개선했습니다. [원문확인] — [arXiv:2603.04351](https://arxiv.org/abs/2603.04351)
- 텐던 구동 손 마찰 보상: Palli & Melchiorri(*Mechatronics* 2014)는 수직력 의존 LuGre 모델을 썼습니다. Lange 외(ICRA 2021)는 접촉별 마찰모델을 손가락 전체 모델로 합쳤습니다. AMBIDEX는 점성·쿨롱 마찰 모델에 RNN 텐던 동역학 모델을 더한 하이브리드입니다. 폴리머 텐던의 소성·크리프 히스테리시스를 LuGre 유사 모델로 보상한 연구도 있습니다. [미확인(스니펫)] — [UniBo CRIS](https://cris.unibo.it/handle/11585/242478), [AMiner Lange](https://www.aminer.cn/pub/6179332291e01121e96166dc/friction-estimation-for-tendon-driven-robotic-hands), [AMiner AMBIDEX](https://aminer.org/pub/5ff67ffad4150a363cb3d68c/a-hybrid-dynamic-model-for-the-ambidex-tendon-driven-manipulator)
- TU Delft 학위논문은 인대와 텐던을 비탄성 Dyneema 줄로 만든 인간형 손가락을 다룹니다. 크리프 분석은 초록에 없습니다. [미확인(스니펫)] — [TU Delft repository](https://repository.tudelft.nl/file/File_5f58ce97-f372-47fb-a565-70fc93f85fcc)
- Vision-controlled jetting 손은 인대에 티올-엔 계열 탄성소재를 썼습니다. 폴리아크릴레이트보다 굽힘 후 복원이 빠르다고 보도되었습니다. [언론·기업주장] — [Freethink](https://www.freethink.com/robots-ai/vision-controlled-jetting); 초록 [원문확인] — [Nature](https://www.nature.com/articles/s41586-023-06684-3)

### Inferences
- 텐던 분야에서 AI는 소재 교체보다 "소재 특성(크리프, 마찰, 히스테리시스)을 학습으로 흡수"하는 방향입니다. 3% 오차와 41% 격차 감소 같은 수치는 RL 기반 손 제어의 전제 조건을 개선합니다.

### Gaps
- UHMWPE/Dyneema, Vectran, 강선의 크리프·마모 정량 비교와 ML 수명 예측 원문은 확보하지 못했습니다.
- 구름접촉(rolling-contact) 관절이나 플렉셔 관절 소재를 최적화로 설계한 손가락 사례는 이번 범위에서 찾지 못했습니다. 플렉셔 기반 손가락의 강성분포 co-design(1절, arXiv:2505.20404)이 가장 가까운 사례입니다.

## 4. 마찰·접착 표면: 게코형 건식접착, 전기접착, 미세구조 손끝 패드, ML 마찰 예측

### Takeaway
표면 소재에서 ML 설계가 실험으로 검증된 대표 사례는 Sitti 그룹의 게코형 섬유(fibril) 최적화입니다. BO+FEM 설계가 기존 설계 대비 최대 77% 높은 건식접착을 보였고(*Small* 2021), 전단 최적화 후속 연구도 실험 검증되었습니다(*Small* 2023). 전기접착에서는 랜덤포레스트 대리모델로 2층 보호막의 유전율을 설계한 사례가 있습니다(*Sci. Rep.* 2024). 다만 이 표면들을 실제 로봇 손가락에 장착해 파지 성능을 정량화한 ML 연구는 찾지 못했습니다.

### Cited Findings
- Son 외(Sitti 그룹), "Machine Learning-Based and Experimentally Validated Optimal Adhesive Fibril Designs", *Small* (2021-08-19, DOI 10.1002/smll.202102867): BO와 FEM으로 섬유 형상을 탐색했습니다. 2광자 중합 3D 마이크로프린팅과 PDMS 이중몰딩으로 제작했고, 매끈한 표면에서 기존 설계 대비 최대 77% 높은 건식접착을 보였습니다. 접착은 팁뿐 아니라 3D 스템 형상, 인장변형, 미세가공 한계에도 민감했습니다. [원문확인(초록)] — [DOI/Europe PMC 초록](https://doi.org/10.1002/smll.202102867)
- Dayan 외, "Machine Learning-Based Shear Optimal Adhesive Microstructures with Experimental Validation", *Small* (2023-09-10 온라인, DOI 10.1002/smll.202304437): ML 최적화와 FEM 전단역학을 결합하고 제작 한계를 시뮬레이션에 반영했습니다. 제작한 전단최적 섬유는 표준 형상보다 성능이 우수했습니다. 저자들은 응용처로 로봇 pick-and-place 그리퍼, 등반 로봇, 장갑을 제시했습니다. [원문확인(초록)] — [DOI (Europe PMC 초록 확인)](https://doi.org/10.1002/smll.202304437)
- Park, Chang, Kim, Gwak, Moon, "Superior electroadhesion force with permittivity-engineered bilayer films using electrostatic simulation and machine learning approaches", *Sci. Rep.* (2024-07-24): 저유전 내층과 고유전 외층으로 된 2층 보호막을 쓰면 절연파괴를 견디면서 정전기력을 키울 수 있습니다. 그리퍼 구성 3,000개는 FEA로, 7,000개는 AI로 평가했고 설계변수는 8개입니다. ML 모델은 FEM 1,000 샘플로 학습한 랜덤포레스트(RF)이며, 민감도 분석도 함께 했습니다. 내층과 외층 유전율이 각각 2.5와 4.5인 조합은 정전기력을 "약간" 개선했습니다. [원문확인] — [Scientific Reports](https://www.nature.com/articles/s41598-024-67805-0)
- 비교 기준(비ML): Ruffatto, Shah, Spenko의 전극 패턴 최적화에서는 동심원 패턴이 가장 효과적이었습니다. 문헌값 대비 전단압이 기판에 따라 2.2~15배 개선되었습니다. [미확인(스니펫)] — [core.ac.uk](https://core.ac.uk/download/148016769.pdf)
- Kim 외(*ACS AMI* 2020): 기둥(pillar) 형상 후보 20만 개를 만들고 딥러닝 분류 정확도 99% 이상을 보고했습니다. [미확인(스니펫)] — [Berkeley Gu lab PDF](https://gu.berkeley.edu/wp-content/uploads/2020/05/acsami.0c04123.pdf)

### Inferences
- 표면 소재 ML 설계는 "형상 최적화 → 미세가공 → 접착력 시험" 단계까지는 검증되었습니다. "손가락 장착 → 파지 성공률" 단계는 비어 있습니다.

### Gaps
- 로봇 손끝의 마찰계수나 미끄럼을 소재·텍스처로부터 예측하는 ML 모델(비센싱 목적)의 원문은 확보하지 못했습니다.
- ML 최적화 미세텍스처를 장착한 손가락의 파지력·마모 수명 정량 데이터는 찾지 못했습니다.

## 5. RL·미분가능 시뮬레이션·확산모델을 이용한 손·손가락 형태와 제어의 공동설계

### Takeaway
2023~2026년 공동설계는 확산 생성모델과 형태 조건부 RL 정책으로 빠르게 이동했습니다. DGDM은 0.8초에 설계 하나를 생성하고 성공률을 최적화 기준 대비 31.5%, 비유도 확산 대비 45.3% 개선했습니다. House of Dextra(ICLR 2026)는 설계부터 RL 학습, 제작, 배치까지 24시간 이내로 줄였습니다. 다만 대부분은 형상과 기구학을 설계하며, 소재(강성분포) 변수는 일부 연구에만 들어갑니다(arXiv:2505.20404, DiffuseBot).

### Cited Findings
- Dynamics-Guided Diffusion Model, DGDM (Xu, Ha, Song; arXiv 2024-02-23): 기하 확산모델로 센서 없는 매니퓰레이터 손가락 형상을 생성합니다. 과제 정보 없이 학습한 동역학 네트워크의 그래디언트로 생성을 유도합니다. 성공률은 최적화 기준 대비 31.5%, 비유도 확산 대비 45.3% 높았고, 설계 하나 생성에 0.8초가 걸립니다. [원문확인] — [arXiv:2402.15038](https://arxiv.org/abs/2402.15038)
- House of Dextra: Cross-embodied Co-design for Dexterous Hands (arXiv 2025-12-03, ICLR 2026): 관절·손가락·손바닥 생성까지 포함하는 형태 탐색 공간을 다룹니다. 형태 조건부 교차형태(cross-embodied) 정책으로 평가하고, 접근 가능한 부품으로 실물을 제작합니다. 설계부터 학습, 제작, 배치까지 24시간 미만이며 인핸드 회전으로 검증했습니다. 오픈소스입니다. [원문확인] — [arXiv:2512.03743](https://arxiv.org/abs/2512.03743), [ICLR 2026](https://www.iclr.cc/virtual/2026/poster/10007820)
- DiffuseBot (Wang, Gan, Rus 외; NeurIPS 2023 oral, arXiv 2023-11-28): Point-E 기반 확산모델에 물리 시뮬레이션의 성능 인증과 미분가능 시뮬레이션 기반 co-design을 더했습니다. 소프트 로봇 형태와 제어를 공동 최적화하고, 텐던 구동 그리퍼를 실물로 제작했습니다. [원문확인] — [arXiv:2311.17053](https://arxiv.org/abs/2311.17053). "4~8배 개선" 수치는 애그리게이터 출처라 확인하지 못했습니다. [미확인(스니펫)] — [Emergent Mind](https://www.emergentmind.com/papers/2311.17053)
- Co-Design of Soft Gripper with Neural Physics (arXiv 2025-05): 강성분포(소재 변수)와 파지 자세를 미분가능 신경 대리모델로 공동설계했습니다(1절 참조). [원문확인] — [arXiv:2505.20404](https://arxiv.org/abs/2505.20404)
- RL 기반 소프트 그리퍼 co-design에 축소차수 FEM 대리모델을 쓴 연구(1절 참조). [원문확인] — [arXiv:2603.19794](https://arxiv.org/abs/2603.19794)
- UGG (ECCV 2024): 확산모델로 손 파라미터, 물체, 접촉점을 통합 생성합니다. DexGraspNet에서 SOTA를 보고했으나, 손가락 소재나 형상 설계가 아니라 파지 생성 연구입니다. [원문확인] — [arXiv:2311.16917](https://arxiv.org/abs/2311.16917)

### Inferences
- 공동설계의 병목은 계산에서 제작과 sim-to-real로 옮겨갔습니다. DGDM의 0.8초 생성, House of Dextra의 24시간 미만 사이클이 그 근거입니다. 소재 비선형성을 반영한 대리모델(2603.19794, 2505.20404)이 이 둘을 잇는 역할을 합니다.

### Gaps
- MIT·CMU·ETH·Stanford의 다른 손가락 공동설계 사례(Fit2Form, RoboGrammar 손 적용 등)는 이번 예산으로 원문 확인을 하지 못했습니다.

## 6. 자가치유·내마모 손가락 피부와 AI의 역할

### Takeaway
VUB(Terryn, Vanderborght) 그룹은 Diels-Alder(DA) 열가역 폴리머 기반 자가치유 그리퍼와 손을 2017년부터 이어왔습니다. 소재 계열은 Science Robotics 2017, 상온치유 2020, FFF 인쇄 2020, 재밍 범용 그리퍼 AIS 2023, 흡착컵 2023입니다. AI는 손상 감지와 위치추정 단계에 들어가 있습니다. 5층 신경망 기반 터치 위치추정 오차는 2.3 mm이고, 전이학습으로 200회 미만 탐침만으로 재적응했습니다(2022, 스니펫). 치유 소재 자체를 AI로 설계한 손가락 사례는 찾지 못했습니다.

### Cited Findings
- Terryn 외(*Sci. Robot.* 2017): DA 폴리머로 만든 소프트 그리퍼와 손이 거시적 손상을 치유했습니다. 이후 연구에서 상온치유 네트워크(*IEEE RAM* 2020, 기존 DA는 80~90 °C 가열 필요), 다중 DA 폴리머 계면 접합(*Actuators* 2020), FFF 적층제조로 만든 FESTO형 핑거 그리퍼(*Soft Robotics* 2020)로 확장했습니다. [미확인(스니펫)] — [DOAJ Actuators 2020](https://doaj.org/article/a7b652ecf0584e6192d682ce92c57598), [IEEE RAM 2020-12](https://nxtbook.com/nxtbooks/ieee/roboticsautomation_december2020/index.php?startid=44), [VUB PDF](https://biblio.vub.ac.be/vubirfiles/55871354/Soft_robotic_actuator_that_can_heals_on_room_temperature_revised_1.pdf)
- Wang, Terryn 외(*Adv. Intell. Syst.* 2023, DOI 10.1002/aisy.202300223): 자가치유 막 안에 강구(steel ball) 입자재밍을 넣은 범용 그리퍼입니다. 긁힘과 천공을 회복하고, 재가공·재활용이 가능합니다. 자가폐쇄·자가치유 다중소재 흡착컵(TU/e 공동)은 상온 1일 이내, 약한 가열 시 1시간 안에 회복합니다. [미확인(스니펫)] — [CiteDrive](https://www.citedrive.com/en/discovery/selfregulated-selfhealing-robotic-gripper-for-resilient-and-adaptive-grasping), [TU/e](https://research.tue.nl/en/publications/selfclosing-and-selfhealing-multimaterial-suction-cups-for-energy/)
- "Learning-Based Damage Recovery for Healable Soft Electronic Skins" (*Adv. Intell. Syst.* 2022-12): 5,000회 탐침 데이터로 5층 신경망을 학습해 터치 위치 2.3 mm, 깊이 95% 정확도를 냈습니다. 상태 모니터링으로 손상과 부분 회복의 위치를 찾았고, 1개 층을 동결한 전이학습으로 200회 미만 탐침만에 재적응했습니다. 이 연구는 피부 센서이므로 본 과제의 비센싱 범위와는 경계에 있습니다. [미확인(스니펫)] — [Deutsche Digitale Bibliothek](https://www.deutsche-digitale-bibliothek.de/item/RKCGI7NXH6OGGCRGG7SJ3DGZ2EFJGZ3H?lang=en), [DOAJ](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d), [Cambridge Eng.](https://www.eng.cam.ac.uk/node/5147)
- 리뷰(Kashef Tabrizian, Terryn, Vanderborght, *AIS* 2025): 자율 치유를 손상 감지, 세정, 폐합, 자극 유발 치유, 회복 평가의 5단계로 나눴습니다. 현재 자가치유 로봇은 대개 여러 차례 사람 개입이 필요하다고 지적합니다. [미확인(스니펫)] — [Deutsche Digitale Bibliothek](https://www.deutsche-digitale-bibliothek.de/item/JOVNUWDA6Q2VPXGJNMU5EETPYU36OZHL)

### Inferences
- 자가치유 손가락에서 AI의 역할은 소재 설계가 아니라, 치유 사이클의 "감지와 회복 평가" 단계를 자동화하는 쪽입니다. KAIST 사례처럼 배합 ML을 DA 네트워크의 치유온도와 기계강도 상충관계에 적용하는 것이 다음 단계로 보이지만, 이는 추론입니다.

### Gaps
- 내마모 손가락 피부(마모율, 사이클 수명)의 ML 예측이나 설계 원문은 찾지 못했습니다.
- 2025년 EMSOR 프로젝트(VUB) 논문들의 주제는 확인하지 못했습니다. — [VUB EMSOR](https://researchportal.vub.be/en/projects/emsor-embodied-multi-modal-sensing-in-self-healing-soft-robots/)

### 접근 상태 로그
| 호스트 | 결과 | 목적 |
|---|---|---|
| www.nature.com (s41467-026-73735-4) | 성공(본문 전체) | KAIST·KIST 엘라스토머 논문의 수치 확인 |
| www.nature.com (s41598-024-67805-0) | 성공(본문) | 전기접착 RF 모델 확인 |
| arxiv.org/abs (19건) | 성공 | 대리모델, Fin-Ray, co-design, 텐던, HASEL 논문 초록 |
| export.arxiv.org API | 실패(DNS 해석 불가) | 초록 일괄 조회 시도 → arxiv.org/abs로 대체 |
| www.ebi.ac.uk (Europe PMC REST) | 부분 성공(일부 요청 30초 타임아웃) | Sci. Robot. 바이오하이브리드 손, Small 2021/2023, Nature 2023 VCJ 초록 |
| researchprofiles.canberra.edu.au | 성공(초록 일부) | Fin-Bayes |
| doaj.org | 응답은 왔으나 초록 추출 실패 | Terryn 2022 AIS |
| www.eurekalert.org | grep 결과 없음(본문 추출 실패) | KAIST 보도자료 → 검색 스니펫으로 대체 |
| WebFetch 도구 | 사용 안 함(지시에 따라 고장으로 간주) | — |
