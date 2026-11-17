# 강체·휴머노이드·산업용 로봇 소재 분류: 1차 출처 검증과 공백 보완

작성일 2026-11-17. 대상 문서: `taxonomy_rigid_humanoid.md`. 그 문서는 검색 스니펫만으로 작성됐다.

**방법.** 이번에는 Bash `curl`로 원문 페이지를 직접 받아 HTML을 걷어내고, 핵심 문장을 grep으로 확인했다. WebFetch는 한 번도 시도하지 않았다(지시에 따름). 보조로 WebSearch를 약 17회 썼다.

**판정 등급.**
- **VERIFIED**: 원문에서 해당 문장이나 수치를 직접 확인했다.
- **PARTIALLY VERIFIED**: 일부만 확인했거나, 2차 출처 본문에서만 확인했거나, 수치에 차이가 있다.
- **UNVERIFIED**: 원문에 접근하지 못했거나(차단·404), 원문에서 해당 내용을 찾지 못했다.

**출처 태그.** [CO] 회사 주장, [RPT] 애널리스트·시장보고서, [IND] 독립 매체·학술, [SNIP] 검색 요약만 확인(원문 미확인).

---

## Q1. 핵심 수치 검증 (IDTechEx, MS/GS/BofA BOM, NdFeB, 수출통제, Nabtesco·Leaderdrive, MagNex, Niron, Figure, Kingfa, Infineon, EPC, MS–PNNL)

### Takeaway
- **확인된 것.** 기존 문서의 큰 그림은 대체로 맞다.
  - IDTechEx의 "액추에이터가 휴머노이드 무게의 약 56%"는 IDTechEx 기고문 원문으로 확인된다.
  - Figure F.03 배터리의 2.3 kWh·5시간·2 kW·UN38.3/UL2271, Niron 1,500 t/년 공장, MagNex 주장, Leaderdrive 글로벌 점유율 약 15%도 원문으로 확인됐다.
- **틀린 것.** "Morgan Stanley: 액추에이터 = BOM의 56%"는 원문 근거를 찾지 못했다.
  - 무게 56%(IDTechEx)가 BOM 56%로 잘못 옮겨졌을 가능성이 크다.
  - MS의 실제 공개 수치(2025-12 Robot Almanac 보도)는 Optimus Gen 2 BOM 약 $46k, 그중 액추에이터 약 $22k다. 비율로 약 48%다.
- **새로 확보한 것.** BofA는 2030년 BOM 구성을 직접 공개했다.
  - 리니어 액추에이터 27%, 로터리 24%, 손 19%다.
- **수정이 필요한 것.** Kingfa 인터뷰는 원문을 보니 "PEEK 과열" 경고가 핵심이었다. 기존 문서의 인용 방향을 바꿔야 한다.

### Cited Findings

#### IDTechEx "Materials for Humanoid Robots 2026–2036"
- **[VERIFIED, RPT] 액추에이터 무게 비중.** "IDTechEx's analysis estimates that around 56 percent of the humanoid's weight is from the actuators alone."
  - 같은 글은 액추에이터 구조 부품이 "steel (predominantly) and aluminum alloys"에 의존해 무게와 배터리 효율에 부담을 준다고 썼다.
  - 출처: [Robotics & Automation News, 2026-07-30 (IDTechEx 기고)](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)
- **[VERIFIED, RPT] 보고서가 다루는 소재와 예측 범위.**
  - 10년 수요 예측의 소재 구분: "metal alloys (steel, aluminum & magnesium), rare-earth permanent magnets, engineering plastics (e.g., PEEK, PC-ABS), and more"
  - 분석 대상: "over 50 humanoid products and prototypes"
  - 성장률: "47% CAGR for humanoid unit sales expected over the next decade"
  - 출처: [IDTechEx 기고, roboticsresear.ch, 게시 2026-06-02 / 수정 2026-06-29](https://roboticsresear.ch/articles/34801/emerging-materials-opportunities-and-trends-in-the-humanoid-market)
- **[VERIFIED, RPT] 시범에서 생산으로의 전환 시점.** "IDTechEx expects 2026-2027 to represent key transition years, with more players moving from pilot testing toward production readiness and early-scale rollout."
  - 같은 글에 "actual deployment volumes remain below earlier ambitious targets"라는 단서가 붙어 있다.
  - 출처: [roboticsresear.ch 2026-06-02](https://roboticsresear.ch/articles/34801/emerging-materials-opportunities-and-trends-in-the-humanoid-market)
- **[VERIFIED, RPT] 소프트 액추에이터 전망.** IDTechEx는 강체 액추에이터가 "continue to be the mainstay"라고 본다.
  - 소프트 액추에이터 소재로 EAP, SMA, 압전을 들었다.
  - 하이브리드 설계에서 일부 역할을 할 가능성을 언급했다.
  - 출처: [R&A News 2026-07-30](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)
- **[UNVERIFIED] 원문에서 찾지 못한 기존 문서 주장.** 다음 두 가지는 받아 본 두 원문에 없었다.
  - "2030년 무렵 100만 대 접근"
  - "지금까지 휴머노이드의 80%가 산업용으로 설계"
  - 보고서 본문(유료)이나 다른 IDTechEx 기사에 있을 수는 있다. 그 전까지는 2차 인용으로만 다뤄야 한다.

#### Morgan Stanley
- **[VERIFIED, RPT] $5T 시장 전망.** "The humanoids market could surpass $5 trillion by 2050"
  - 2050년까지 "more than 1 billion"대, 그중 "90% used for industrial and commercial purposes"
  - 원문 게시일 2025-05-14
  - 출처: [Morgan Stanley Insights](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050)
- **[VERIFIED via 2차 본문, RPT] Robot Almanac Vol. 3 (2025-12, 저자 32명).** Optimus Gen 2 BOM은 "around US$46,000"이다. 중국을 뺀 공급망에서는 "US$131,000"으로 오른다.
  - 액추에이터 비용: "about US$22,000 to US$58,000"
  - 칩·소프트웨어 비용: "roughly US$3,000 to US$7,000"
  - 휴머노이드 특허(최근 5년): 중국 7,705건, 미국 1,561건
  - 출처: [Yahoo Tech (SCMP 계열 보도), 2025-12-20](https://tech.yahoo.com/science/articles/china-packs-patent-punch-race-093000841.html)
- **[UNVERIFIED] "액추에이터 = BOM 56%"를 MS 수치로 보는 주장.** MS 원문 보고서는 공개되지 않아 확인하지 못했다.
  - 검색 요약에서는 56%가 MS, 일론 머스크, Schaeffler에 제각각 귀속된다. 출처가 혼선이다.
  - 출처: [SNIP: fourweekmba](https://fourweekmba.com/where-the-money-goes-in-humanoid-robotics/) (403으로 접근 불가)
- **[UNVERIFIED] MS의 NdPr 1.3 kg/대.** 이 수치를 담은 WisdomTree 블로그가 Cloudflare 403으로 막혔다.

#### Goldman Sachs
- **[VERIFIED, RPT] 제조원가 하락과 시장 전망.**
  - 제조원가: 2022년 "$50,000 (for lower-end models) and $250,000 (for state-of-the art versions)"에서 2023년 "$30,000 and $150,000"으로 내렸다.
  - "Where our analysts had expected a decline of 15-20% per annum, the cost declined 40%"
  - 2035년 TAM은 "$38 billion", 기존 예측 $6B의 6배 이상이다.
  - 보고서 날짜 2024-01-08, 기사 날짜 2024-02-27
  - 출처: [Goldman Sachs Insights](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035)
  - 보고서 PDF URL은 404였다.
- **[UNVERIFIED] 2035년 650만 대·$138B 상향 수정.** 이번에 확인하지 않았다.

#### Bank of America
- **[VERIFIED, RPT] 중국산 BOM 전망.** "BofA Global Research estimates a built-in China humanoid robot's BOM cost was $35,000 in 2025 but expects it to be roughly cut in half to below $17,000 by 2030."
  - 시범 단계 BOM은 "$90,000 to 100,000 per unit"이다.
  - 출처: [BofA Institute "Physical AI Part 2", 2026-03-12 (PDF)](https://institute.bankofamerica.com/content/dam/transformation/physical-ai-part-2.pdf)
- **[VERIFIED, RPT · 신규] 2030년 BOM 모듈별 구성 (Exhibit 6, "Actuators account for more than 50% of the total BOM cost").**

  | 모듈 | 비중 |
  |---|---|
  | 리니어 액추에이터 | 27% |
  | 로터리 액추에이터 | 24% |
  | 손 | 19% |
  | 제어 | 10% |
  | 비전·센서 | 4% |
  | 에너지 | 4% |
  | 기타 | 12% |

  출처: [BofA Institute PDF](https://institute.bankofamerica.com/content/dam/transformation/physical-ai-part-2.pdf)
- **[IND] 독립 추정과 비교.** Interact Analysis는 액추에이터를 재료비의 "30 to 50 percent"로 본다. "some industry observers place the figure near 60 percent"라는 문장도 함께 실렸다.
  - 출처: [Korea JoongAng Daily, 2026-02-19](https://www.koreajoongangdaily.com/business/actuators-become-new-battleground-in-humanoid-robot-race/12288658)

#### NdFeB와 Adamas
- **[VERIFIED, RPT] 대당 NdFeB 약 4 kg.** "Production is now visibly shifting from pilot-scale to the low tens of thousands of units per year by 2026–2027, with each advanced robot expected to contain ~4 kg of NdFeB magnets depending on degrees of freedom."
  - 출처: [Adamas Intelligence, 2026-04-14](https://www.adamasintel.com/humanoid-robotics-sector-accelerates-on-multiple-commercialization-fronts-in-march/)
- **[VERIFIED, RPT] 극단 시나리오.** 2040년 100억 대 생산이면 현재 연간 NdFeB 생산의 "186-times"가 필요하다. 설비는 "93-fold" 늘어야 한다.
  - 출처: [Adamas, 2025-02-14](https://www.adamasintel.com/humanoid-robots-and-the-future-of-motors-and-ndfeb-markets/)
- **[VERIFIED via 2차, RPT] Adamas 시장 전망 2건.**
  - 2024→2040 NdFeB 수요는 "more than 880,000 tonnes"로 거의 4배가 된다.
  - 휴머노이드 1대 무게는 "approximately 60 kilograms"다(Adamas 연구 인용).
  - 출처: [Oregon Group](https://theoregongroup.com/latest-news/where-will-the-metals-for-the-robot-revolution-come-from/)
- **[PARTIALLY VERIFIED, SNIP] ">30 t per 10,000 humanoids".** "30–40 DoF per professional service humanoid → every 10,000 units consume over 30 tonnes" 문장은 검색 요약에서만 확인됐다.
  - 받아 본 Adamas 3개 페이지 본문에는 없었다.
  - 대당 3 kg 이상이라는 뜻이므로 위의 약 4 kg 수치와 모순되지는 않는다.
  - 출처: [SNIP: adamasintel.com 검색결과](https://www.adamasintel.com/humanoid-robots-and-the-future-of-motors-and-ndfeb-markets/)
- **[UNVERIFIED] FAI 수치.** "2–4.5 kg NdFeB, 0.57–1.3 kg NdPr, 35–79 g Dy"는 Oregon 페이지 본문 grep에서 찾지 못했다.

#### 중국 희토류 수출통제
- **[인용, 별도 검증 완료] 2개월 유예 연장.** 상무부(MOFCOM)는 2026-11-09에 유예를 2개월 연장해 **2027-01-10까지**로 늘렸다. 2025-04에 시작된 7종 중희토류 라이선스제는 그대로 유효하다.
  - 출처: [The Star (Reuters 전재) 2026-11-09](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/11/09/china-extends-suspension-of-rare-earth-export-controls-until-january); 상세는 같은 폴더 `verify_policy_industry.md`

#### Nabtesco (RV 감속기)
- **[PARTIALLY VERIFIED, CO] 약 60% 점유율.** Nabtesco 공급사 프로필 원문에 "holds approximately 60% of the global market share"라는 문장이 있다(정밀 감속기 맥락).
  - 출처: [Plant Automation Technology – Nabtesco Motion Control 프로필](https://www.plantautomation-technology.com/suppliers/nabtesco-motion-control-inc)
  - Nabtesco 브로셔에도 "industrial robot (vertical articulated robot) joints 60% share of global market"이라는 문구가 있다고 하나, 검색 요약으로만 확인했다. 측정 기준은 공개되지 않았다.
  - 따라서 회사 자체 추정치다.
- **[SNIP] 제3자 추정은 35~60%로 엇갈린다.** 기존 문서의 "53%"는 원문을 확인하지 못했다.
  - 출처: [SNIP: evsint](https://www.evsint.com/industrial-robot-reducers-harmonic-cycloidal-rv-comparison-2026/); [SNIP: jaredwatkins research](https://www.jaredwatkins.com/research/robotics/actuators/nabtesco/)

#### Leaderdrive (하모닉 감속기)
- **[VERIFIED, IND (회사 공시 기반)] 점유율과 실적.** "It currently holds a global market share of approximately 15%, ranking second worldwide and first domestically, thereby breaking the long-term monopoly of Japan's Harmonic Drive Systems."
  - 2026년 상반기 매출 3.49억 위안(+38.64%), 순이익 7,011만 위안(+31.25%)
  - 2026-08-26 이사회가 H주 홍콩 상장을 승인했다.
  - 출처: [Gasgoo, 2026-08-28](https://autonews.gasgoo.com/articles/news/leaderdrive-plans-hong-kong-ipo-2093357096908443649)
- **[VERIFIED 문장 / 신뢰도 낮음] 원가 비중 주장.** 같은 기사의 "harmonic reducers account for about 30% to 35% of the cost of a humanoid robot"은 출처가 불명확하다. BofA·MS 구성비와도 잘 맞지 않는다.
- **[UNVERIFIED] "중국 내 30~40%" 점유율.** 원문에서 찾지 못했다.

#### Materials Nexus MagNex
- **[VERIFIED, CO] 회사 주장.** 개발 기간 "in just three months"
  - "can be produced at 20% of the material cost and a 70% reduction in material carbon emissions (kg CO2/kg)"
  - AI 플랫폼이 "over 100 million compositions"를 분석했다.
  - Henry Royce Institute, University of Sheffield와 협업했다.
  - 출처: [Mining.com, 2024-06-11](https://www.mining.com/ai-helps-quickly-develop-rare-earth-free-permanent-magnet/)
- **[미확인] 성능 데이터.** 동료심사 자기특성 데이터(Br, Hcj, BHmax)는 여전히 확인되지 않았다.

#### Niron Magnetics (질화철 FeN)
- **[VERIFIED, CO] Sartell 공장.** Minnesota주 Sartell에 "1,500-ton-per-year" 공장을 착공했다.
  - 면적 190,000 sq ft, "operational in early 2027", 정규직 175명 이상
  - 용도에 "robotics"가 포함된다.
  - 출처: [Mining.com, 2025-09-26](https://www.mining.com/niron-breaks-ground-on-rare-earth-free-magnet-manufacturing-plant-in-minnesota/)
- **[VERIFIED, IND] 미 국방부 대출과 2공장.** 미 국방부 OSC가 "direct loan of up to $150 million over a 20-year term"을 조건부로 약정했다.
  - OSC는 공장 총비용을 "$605 million"으로 본다.
  - 2공장은 "10,000 tons of annual capacity"이며 최종 부지를 선정 중이다. 2028년 착공 예정이다.
  - 출처: [Charged EVs, 2026-08-19](https://chargedevs.com/newswire/niron-magnetics-wins-conditional-150-million-loan-commitment-for-rare-earth-free-magnets/)
  - 기존 문서는 이 건을 "2026-08-07"로 적었는데, 이번에 본 기사의 게시일은 2026-08-19다.

#### Figure F.03 배터리 (Figure 03 로봇)
- **[VERIFIED, CO] 배터리 사양.**
  - "2.3 kWh enables 5 hours of run time at peak performance"
  - "2 kW fast charge with active cooling"
  - "first humanoid robot battery in process to be certified to both UN38.3 and UL2271"
  - 출처: [Figure, 2025-07-17](https://figure.ai/news/f-03-battery-development)
- **[VERIFIED, CO · 소재 신규]**
  - 외함은 "high strength stamped steel, die cast aluminum and structural adhesives"이다. 기존 문서의 "stamped steel + cast Al"을 정정하고, 구조용 접착제를 추가한다.
  - 열폭주 전파 차단에 "thermally insulative potting compound"를 쓴다.
  - "cell-to-cell wirebond interconnect … tuned to act as a fusible element"
  - 출처: [Figure, 2025-07-17](https://figure.ai/news/f-03-battery-development)
  - 기존 문서가 언급한 1.2 kWh 표기는 Figure 원문과 맞지 않는다.

#### Kingfa (PEEK)
- **[VERIFIED, CO 인터뷰] 핵심 메시지는 과열 경고였다.** Kingfa 로봇기술 GM 위페이(Yu Fei)는 "the hype surrounding the concept has significantly outpaced its actual practical value. Scalable application scenarios have yet to materialize"라고 말했다.
  - 출처: [Gasgoo, 2026-09-17](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)
- **[VERIFIED] 같은 기사의 정량 정보.**
  - 휴머노이드 1대에 플라스틱 "approximately 6–10 kilograms"가 들어가고, 재료비는 "exceeds 1,000 RMB"다.
  - "80%–90% of humanoid robot material solutions are highly customized"
  - 양산 전에 소재 배합과 구조를 3~5회 반복 조정한다.
  - 규모가 커지면 CNC 가공이 사출성형으로 바뀐다고 본다.
  - PEEK 밀도는 약 1.3 g/cm³로 Al의 약 절반이다.
  - Tesla, Unitree, Agibot가 PEEK를 쓰기 시작했다(기사 서술).
  - Huaxiang Qiyuan의 개질 PEEK 유성감속기는 270 g으로 동급 금속 대비 약 70% 가볍다. PEEK 구조물로 대당 5.3 kg을 줄였다.
  - PEEK 시장은 2024년 61억 위안이고, 휴머노이드 수요는 2027년 40억 위안을 넘을 것으로 본다.
  - Counterpoint 인용: 2026년 상반기 휴머노이드 출하는 22,000대를 넘었다(전년 대비 약 300% 증가).
  - 출처: [Gasgoo, 2026-09-17](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)

#### Infineon (GaN)
- **[UNVERIFIED (CO, 스니펫만)] "70 joints / 600 power switches".** 원문을 확인하지 못했다.
  - Mouser 4개 미러는 "Access to this page has been denied"(봇 차단)였다.
  - Future Electronics는 403이었다.
  - infineon.com 응용 페이지에는 이 문구가 없었다.
  - 출처: [SNIP: Future Electronics](https://www.futureelectronics.com/resources/featured-products/infineon-solutions-for-motor-control-in-humanoid-robots)
- **[PARTIALLY VERIFIED, IND] PCIM 취재기사.** 확인된 것은 "GaN Does Not Replace Silicon" 공존론과 Infineon 측 발언 "For the absolute high-performance joints, I believe the transition will be slower"다.
  - 검색 요약의 "$500/robot 반도체", "3.3 kW/in³"는 본문 grep에서 찾지 못했다.
  - 출처: [All-About-Industries, 2026-06-15](https://www.all-about-industries.com/how-infineon-powers-the-joints-of-humanoid-robots-with-gan-a-c1b49d5c860ed39961e2c4e400e662d0/)

#### EPC (GaN 관절 드라이버)
- **[VERIFIED, CO via 전문지] EPC91120 사양.**
  - 지름 32 mm, EPC23102 GaN 하프브리지 3개, 15–55 V
  - 21 A peak(15 ARMS 연속), 42 A peak(30 ARMS 펄스)
  - 히트싱크 없이 26°C에서 7 ARMS, 모터 케이싱 장착 시 15 ARMS
  - 자기식 엔코더 인터페이스 내장
  - 출처: [Power Electronic Tips, 2025-11-07](https://www.powerelectronictips.com/three-phase-gan-driver-fits-32-mm-robotic-joints/)
- **[UNVERIFIED] EPC91122(2026-02)와 EPC91132(23 mm, 2026-06).** epc-co.com이 Cloudflare 403을 반환했다.

#### Microsoft–PNNL
- **[VERIFIED, CO] 후보 선별 과정.**
  - "32 million candidates"에서 "about 500,000 mostly new stable materials", 다시 "800"으로 줄였다.
  - 실용성 평가 후 "23 – five of which were already known"이 남았다.
  - 걸린 시간은 "just 80 hours"였다.
  - 리튬 함량을 "possibly by as much as 70 percent" 줄일 수 있다(Li와 Na를 함께 사용).
  - 출처: [Microsoft Source, 2024-01-09](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/)
- **[PARTIALLY VERIFIED] 물질명 "N2116".** 이 페이지 본문에는 이름이 나오지 않는다.
  - Microsoft 측은 "the exact chemistry is subject to optimization and might not work out when tested at larger scale"라고 단서를 달았다.

### Inferences
- **BOM 56% 수치 정리.** MS Almanac의 $22k/$46k ≈ 48%와 BofA의 2030년 액추에이터 51%(27+24, 손 제외)를 보면 "액추에이터 ≈ BOM 절반"은 합리적이다. 손 액추에이터까지 넣으면 60~70%까지 올라갈 수 있다.
  - "56%"는 무게 지표(IDTechEx)로만 확실하다.
  - 최종 보고서에서는 "무게 56%(IDTechEx)"와 "BOM 약 50%(MS·BofA)"를 나눠 적어야 한다.
- **플라스틱과 자석의 무게 비중.** Kingfa의 대당 6~10 kg 플라스틱과 Adamas의 대당 약 60 kg·NdFeB 약 4 kg을 합치면, 휴머노이드 질량에서 플라스틱은 약 10~17%, 자석은 약 7%다.
  - 나머지 약 75%는 금속(Al, 강, 일부 Mg), 배터리, 전자부품으로 추정된다. 서로 다른 출처를 조합한 추정이다.
- **2026년 하반기의 시장 신호.** Kingfa의 PEEK 과열 경고와 Adamas의 "low tens of thousands of units per year by 2026–2027"을 함께 보면, 소재 수요는 2027년까지 톤 단위가 아니라 맞춤형·소량 단계에 머무를 가능성이 크다.

### Gaps
- IDTechEx의 "~100만 대 2030"과 "80% 산업용"은 원문으로 확인하지 못했다(보고서 유료). 시도한 idtechex.com 보고서 URL(ID 1123)은 다른 보고서를 반환했다.
- MS의 NdPr 1.3 kg/대(WisdomTree, Cloudflare)와 FAI의 2–4.5 kg은 미확인이다.
- Nabtesco 60%의 측정 기준과 연도가 공개되지 않았다.
- Infineon "70/600"과 EPC 2026년 신제품은 원문 접근이 차단됐다.

---

## Q2. 공백 보완 1: 소재별 kg/대, 감속기·롤러스크루 강종, 센서·광학·케이블·EMI 소재

### Takeaway
- **소재별 kg/대.** 공개된 정량치는 플라스틱(Kingfa: 대당 6~10 kg)과 NdFeB(Adamas: 약 4 kg)뿐이다. Al·Mg·강의 kg/대 수치는 공개 출처에서 찾지 못했다.
- **강종.** 플렉스플라인은 제조사가 "alloy steel"로만 공개한다. 40CrNiMoA는 RV 사이클로이드 디스크·핀 기어 소재로 2차 출처에 나온다. 20CrMnTi와 GCr15를 휴머노이드 감속기나 롤러스크루에 쓴다는 근거는 찾지 못했다.
- **센서·케이블.** 힘/토크 센서는 고강도 스테인리스(17-4PH 계열)나 경질 Al을 쓴다. 로봇 케이블은 PUR/TPE 외피, Class 6 무산소동, 주석도금 구리 편조 차폐가 표준이다. 둘 다 벤더 원문으로 확인했다.

### Cited Findings

#### 소재별 무게
- **[VERIFIED, CO] 플라스틱.** 휴머노이드 1대에 플라스틱 약 6–10 kg이 쓰인다(Kingfa) — [Gasgoo 2026-09-17](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)
- **[VERIFIED, RPT] NdFeB.** 약 4 kg/대 — [Adamas 2026-04-14](https://www.adamasintel.com/humanoid-robotics-sector-accelerates-on-multiple-commercialization-fronts-in-march/)
- **[VERIFIED, CO] Figure 03 구조 공정 전환.** "While Figure 02 was primarily designed to be manufactured with CNC machining, Figure 03 relies heavily on tooled processes such as die-casting, injection molding, and stamping"
  - Figure 03은 F.02보다 "9% less mass"이다.
  - BotQ 1세대 라인은 연 12,000대다.
  - 출처: [Figure, 2025-10-09](https://www.figure.ai/news/introducing-figure-03)
  - 구조재가 기계가공 Al에서 다이캐스트 Al·사출 플라스틱·프레스 강판으로 옮겨 간다는 1차 근거다.

#### 감속기·롤러스크루 강종
- **[VERIFIED, CO] 플렉스플라인 소재 공개 수준.** Harmonic Drive LLC: "The Flexspline is a thin cylindrical cup made from alloy steel with external teeth on the open end of the cup." 강종은 공개하지 않는다.
  - 출처: [Harmonic Drive LLC, 기술 페이지](https://www.harmonicdrive.net/technology/harmonicdrive)
- **[VERIFIED, IND(해설)] 열처리·결정립이 피로수명을 좌우한다.** "Steel grade, grain size control and surface treatment decide fatigue life as much as the drawing does"
  - 한 설계 예는 "quenched and nitrided alloy steel"을 쓴다.
  - Teshugang 45(1), 2024 파손 분석은 원인을 개재물이 아니라 조대한 구오스테나이트 결정립으로 봤다.
  - 출처: [humanoid.guide – Flexspline](https://humanoid.guide/?p=20671)
- **[SNIP] 40CrNiMoA.** "RV reducer cycloidal discs and pin teeth require specialty alloy steels, typically 40CrNiMoA or equivalent grades"
  - 이 강종은 플렉스플라인용이 아니다.
  - 출처: [SNIP: Zane Robotics substack](https://zanerobotics.substack.com/p/the-technical-gap-in-chinese-robot) (시도한 URL은 404)
- **[SNIP, 신뢰도 낮음] 그 밖의 강종 주장.** 마레이징강 플렉스플라인(PatSnap), SCM440(CNFX)이 언급된다. 둘 다 벤더 블로그 수준이다.
  - 출처: [SNIP: PatSnap](https://www.patsnap.com/resources/blog/articles/5-ways-to-improve-flexspline-wear-in-humanoid-robots/); [SNIP: cnfx](https://cnfx.com/industry/machinery-and-equipment-manufacturing/product/harmonic-drive-gears)
- **[SNIP] AISI 52100(GCr15와 동등).** 풍력 기어박스 표준강으로 ORNL 기술 소개에 나온다. 로봇 롤러스크루와의 연결은 확인하지 못했다.
  - 출처: [SNIP: ORNL 202405685](https://ornl.gov/technology/202405685) (403)

#### 힘/토크 센서
- **[VERIFIED, CO] ATI Mini85 (휴머노이드 발목용 6축 F/T).**
  - "The transducer is made of hardened steel with integral parts made from aircraft aluminum"
  - "EDM wire-cut from high yield-strength stainless steel"
  - 출처: [New Equipment Digest – ATI Mini85](https://www.newequipment.com/classified/mini85-force-torque-sensor-for-humanoid-robots-170211.html)
- **[VERIFIED, CO] 한국 KSensors(FIBOS FARS 시리즈).** 같은 6축 센서를 "17-4 Stainless steel" 또는 "Hard Aluminum Alloy"로 제공한다 — [KSensors](https://ksensors.co.kr/en/?p=287205)
- **[SNIP, IND] iCub 관절 토크센서.** 17-4PH(UTS 1100 MPa, E 200 GPa)를 썼고 히스테리시스가 보고됐다 — [SNIP: core.ac.uk](https://core.ac.uk/download/158801567.pdf) (Cloudflare 403)

#### 엔코더와 광학
- **[SNIP, 벤더·위키 혼재] 엔코더.** 자기식 엔코더가 휴머노이드·보행로봇 관절에서 선호된다.
  - 광학식은 유리나 Mylar 코드 디스크를 쓴다. 충격과 습기(김서림)에 취약하다. 해상도는 최대 24-bit다.
  - 자기식은 16~18-bit다.
  - 출처: [SNIP: PatSnap Eureka](https://eureka.patsnap.com/article/optical-encoders-vs-magnetic-encoders-in-precision-robotics); [SNIP: datainsightsmarket](https://www.datainsightsmarket.com/reports/humanoid-robot-encoder-60865)
- **[VERIFIED, CO] EPC91120이 자기식 엔코더 인터페이스를 내장한다.** 관절 일체형 드라이버가 자기식을 전제로 한다는 간접 근거다 — [Power Electronic Tips](https://www.powerelectronictips.com/three-phase-gan-driver-fits-32-mm-robotic-joints/)

#### 케이블과 EMI 차폐
- **[VERIFIED, CO] igus.**
  - chainflex CF9 제어 케이블: "TPE Jacket … ±90° torsion"
  - CFROBOT3/CFROBOT7: "Outer jacket: PUR", CFROBOT7은 "Overall shield"
  - 출처: [igus robotic cables](https://www.igus.com/info/robotic-cables)
- **[VERIFIED, CO] Joca.** "Fine stranded oxygen-free copper wire … IEC 60228 Class 6", 차폐형 PUR 케이블, "Tested for over 20 million cycles"(벤더 시험) — [Joca 960 CY-P](https://joca-cable.com/robot-cable/960-cy-p/)
- **[SNIP] 차폐 구성.** 주석도금 구리 편조 차폐, 비틀림용 tin-plated copper shield, 이더넷은 포일+편조 — [SNIP: LCSC guide](https://www.lcsc.com/blog/top-robotic-cable-products-selection-guide-for-2026/)

### Inferences
- **Figure 03의 공정 전환이 갖는 의미.** CNC에서 다이캐스팅·사출·프레스로 바뀐 것과 Kingfa의 "CNC→사출" 전망은 같은 방향이다. 소재 선택 기준이 비강성에서 주조성·사출성·금형 비용으로 옮겨 간다.
  - 그렇다면 ADC12·A380급 다이캐스트 Al, PA-GF, PC-ABS의 비중이 커지고, 6061/7075 기계가공재의 비중은 줄어들 것이다. 강종은 원문 미확인인 [BG] 추정이다.
- **F/T 센서 플렉셔.** 고강도 스테인리스(경화강)와 항공용 Al을 함께 쓰는 구성이 관절 센서의 표준으로 보인다.

### Gaps
- Al·Mg·강의 kg/대 공개 수치가 없다(IDTechEx 유료본, 티어다운 미공개).
- 20CrMnTi·GCr15를 감속기나 롤러스크루에 쓴다는 근거가 없다. CNKI 등 중국어 원문은 시도하지 못했다. DOAJ API는 타임아웃이었다.
- LiDAR 창·카메라 광학 소재(PC, 유리, AR 코팅)는 로봇 맥락의 출처를 찾지 못했다.
- 관절 내부 TIM과 EMI 차폐 소재(관절 하우징 도금 등)는 휴머노이드 맥락의 1차 출처를 찾지 못했다.

---

## Q3. 공백 보완 2: 손 힘줄·스킨, 한국·일본 업체

### Takeaway
- **손 소재.** Figure 03은 "multi-density foam + soft textiles, 세척·공구 없이 교체 가능"을 공식 공개했다. Tesla Optimus의 힘줄 소재는 특허·보도 어디에도 명시되지 않았다. Shadow Hand는 힘줄 구동만 원문으로 확인했고, Dyneema 사용은 2차 출처다.
- **한국 업체.** 소재 정보는 거의 공개되지 않았다. 확인된 것은 공급망 구조다.
  - Hyundai Mobis는 Atlas용 액추에이터를 공급하며, 2028년 3만 대 양산 계획이다.
  - CES 2026 시제품에는 해외산 액추에이터가 쓰였다.
  - LG Axium은 2027년 외부 공급이 목표이고, SPG와 감속기 제휴를 맺었다.
- **Harmonic Drive Systems.** 소재로는 "alloy steel"까지만 공개한다.

### Cited Findings

#### Figure 03
- **[VERIFIED, CO] 외피.** "multi-density foam to protect against pinch points, and is covered in soft textiles rather than hard machined parts"
  - "The soft goods are fully washable and can be removed or replaced without tools"
  - 상업 고객은 "more durable, or cut-proof materials" 유니폼을 선택할 수 있다.
  - 출처: [Figure, 2025-10-09](https://www.figure.ai/news/introducing-figure-03)
- **[VERIFIED, CO] 손.** "Each fingertip sensor can detect forces as small as three grams of pressure"
  - Figure는 기존 상용 촉각센서가 "could not withstand real-world use"라고 판단해 자체 개발했다.
  - 손바닥에 카메라를 넣었다.
  - "Softer, more adaptive fingertips"를 적용했다.
  - 촉각센서와 손가락 피부 소재명은 공개하지 않았다.
  - 출처: [Figure, 2025-10-09](https://www.figure.ai/news/introducing-figure-03)

#### Tesla Optimus
- **[VERIFIED, IND] 2026년 특허 출원.**
  - 2026-11-05 공개된 US 2026/0346473 A1은 하나의 "floating tendon-like cable"이 손가락 관절 두 개를 구동하는 저구동(underactuated) 구조다.
  - 2026년 10월에는 엄지·손바닥·손가락용 부드러운 촉각 "skin" 출원이 공개됐다.
  - 기사는 "A patent application is not a product commitment"라고 단서를 달았다.
  - 출처: [TeslaNorth, 2026-11-06](https://teslanorth.com/2026/11/06/tesla-robot-hand-tendon-cable-fingers/)
- **[VERIFIED, IND(해설)] Optimus V3 특허 해설.**
  - 손 22 DoF(손가락당 4), 손가락당 힘줄 3개, 전완 액추에이터
  - 힘줄 소재 비교: UHMWPE는 강하지만 크리프가 있다. 아라미드(Kevlar, Technora)는 크리프가 적지만 마모가 빠르다. LCP와 ePTFE는 특수 용도다. 강선은 굴곡 반경이 작으면 피로 파손된다.
  - Figure 03의 힘줄·구동 방식은 "Undisclosed"로 표기됐다.
  - 출처: [humanoid.guide – Tendon-driven hands](https://humanoid.guide/?p=16664)
- **[SNIP, 상충] 힘줄 소재.** 한 뉴스레터는 Optimus가 "thin steel cables, three per finger"를 쓴다고 서술한다. 티어다운 근거는 없다.
  - 출처: [SNIP: droids substack](https://droids.substack.com/p/the-forearm-is-the-new-hand-inside)

#### Shadow Hand
- **[VERIFIED, CO] 구동.** "Containing 20 motors, the Hand is tendon driven … with 24 degrees of freedom" — [Shadow Robot](https://www.shadowrobot.com/dexterous-hand-series/)
- **[SNIP] Dyneema 사용.** Dyneema 힘줄을 정기 교체한다는 서술은 2차 출처뿐이다 — [SNIP: humanoid.guide](https://humanoid.guide/?p=16664)
- Sanctuary AI의 손 소재는 이번에도 새 원문을 확보하지 못했다.

#### Hyundai / Boston Dynamics Atlas (전동)
- **[VERIFIED, CO] CES 2026 제품판.** 공개일 2026-01-05.
  - "56 degrees of freedom, fully rotational joints"
  - 도달거리 약 2.3 m(7.5 ft), 들어올리기 50 kg(110 lbs), 배터리 자율 교체
  - 2026년 물량은 Hyundai와 Google DeepMind에 배정됐다.
  - 구조재는 공개하지 않았다.
  - 출처: [Boston Dynamics 블로그](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/)
- **[VERIFIED, IND] 액추에이터 공급.** Hyundai Mobis가 Atlas 액추에이터 공급 계약을 따냈고 "plans to mass-produce 30,000 units in 2028"
  - "Prototypes of Hyundai Motor Group's Atlas and LG Electronics' Cloid … used foreign-made actuators"
  - 세계 액추에이터 주요 업체로 Harmonic Drive Systems, Nabtesco, Maxon, Wittenstein이 꼽혔다.
  - Atlas 배터리가 LG에너지솔루션 제품이라는 업계 전언이 관련 기사 제목에 실렸다.
  - 출처: [Korea JoongAng Daily, 2026-02-19](https://www.koreajoongangdaily.com/business/actuators-become-new-battleground-in-humanoid-robot-race/12288658)
  - 같은 기사에 Samsung Electro-Mechanics의 Alva Industries(노르웨이 초소형 모터) 투자도 나온다.

#### LG Electronics
- **[VERIFIED, IND] Axium.**
  - CES 2026에서 액추에이터 브랜드 Axium을 공개했다.
  - 생산 거점은 창원 LG스마트파크다.
  - "a 2027 target for supplying the motorized joints" to other companies
  - 2026년 양산 체계를 갖춘 뒤 자사 CLOiD에 먼저 쓰고, 2030년 산업용 고토크로 확장한다.
  - 감속기 전문업체 SPG와 기술 제휴를 맺었다.
  - Robotis의 우즈베키스탄 액추에이터 공장 지분 투자를 검토 중이다.
  - 출처: [Korea Herald, 2026-07-14](https://www.koreaherald.com/article/10808594)
- **[SNIP] 수주 현황.** IFA 2026(9월)에서 "no orders have been finalized"라고 밝혔다 — [SNIP: The Investor](https://m.theinvestor.co.kr/article/10863966)

#### Rainbow Robotics
- **[SNIP] 사업 현황만 확인.** 삼성전자가 최대주주(35%)다. 로보월드 2026에서 RB-Y2를 공개했다. 소재 관련 정보는 찾지 못했다.
  - 출처: [SNIP: 다음/요약](https://v.daum.net/v/yspWuUqFyp)

#### Harmonic Drive Systems (일본)
- **[VERIFIED, CO] 소재.** 플렉스플라인은 "alloy steel"이다. 회사는 반복 토크 한계 이내에서는 응력이 내구한도 아래라고 주장한다 — [Harmonic Drive LLC](https://www.harmonicdrive.net/technology/harmonicdrive)
- **[SNIP, RPT] 점유율.** Global Info Research 추정 "HDSI … share of 50%"(strain wave gearing 전체)는 검색 요약으로만 확인됐다. 원문은 Cloudflare 403이었다.
  - 출처: [SNIP: marketresearch.com](https://marketresearch.com/GlobalInfoResearch-v4117/Global-Strain-Wave-Gearing-Devices-39350161)
  - Leaderdrive 약 15%(2위)와 같이 보면 대략 정합한다.

### Inferences
- **피부·외피의 소모품화.** Figure 03이 세척·교체 가능한 텍스타일을 채택한 것은 외피 소재가 구조재에서 소모품·의류(내절단 직물 등)로 바뀌고 있다는 신호다.
- **힘줄 크리프와 유지보수.** Tesla 특허 해설이 강조한 "million-cycle durability"는 힘줄 소재의 크리프와 마모가 유지보수 비용을 좌우한다는 뜻이다. UHMWPE와 아라미드 사이의 선택이 실제 쟁점이다.
- **한국 업체의 소재 정보.** 한국 업체는 2026년 기준 액추에이터 조립과 양산 역량에 집중한다. 감속기(SPG, 에스비비테크)와 소재는 아직 외부에 의존한다. 기존 문서의 "반쪽 국산화" 우려(IB토마토)와 같은 방향이다.

### Gaps
- Optimus·Figure·Sanctuary 손의 힘줄과 피부 소재명은 공개된 적이 없다. 티어다운도 없다.
- Atlas·Rainbow·LG CLOiD의 구조재(Al, Mg, CFRP 여부)는 공개 출처가 없다.
- Harmonic Drive Systems 일본어 IR 자료(소재·열처리)는 시도하지 못했다.

---

## Q4. 로봇 부품에 명시적으로 연결된 AI/ML 소재·설계 개발

### Takeaway
"AI가 설계한 소재가 로봇 부품에 양산 적용됐다"는 공개 사례는 2026-11 현재 찾지 못했다. 가장 가까운 사례는 세 갈래다.
1. 기어·베어링 강의 ML 합금설계: ORNL 베이나이트강(52100 대비 내마모), TU Delft 피로강. 모두 로봇용이 아니라 일반 기어용이다.
2. 무희토 자석의 AI 탐색: MagNex. 로봇 모터를 겨냥했다고 명시하지는 않았다.
3. 보행로봇 링크·다리의 위상최적화나 생성설계: 학술 시제품 수준이다.

Unitree, ANYbotics, Autodesk의 공식 사례는 찾지 못했다.

### Cited Findings
- **[VERIFIED, IND(학술)] TU Delft 피로강 설계.** "a machine learning model for predicting the rotating bending fatigue strength and the high-throughput design of fatigue resistant steels"
  - 전이학습과 진화 알고리즘을 결합해 "requiring only tens of fatigue data points"
  - 출처: [TU Delft repository](https://repository.tudelft.nl/record/uuid:470d0944-7409-4633-9e61-23092137c72d)
- **[SNIP, IND] ORNL 베이나이트강.** CALPHAD, ML, 데이터마이닝으로 개발한 나노구조 베이나이트강이다. 건식 미끄럼 마모가 AISI 52100보다 우수하다고 한다. 대상은 풍력 기어박스다.
  - 출처: [SNIP: ORNL](https://ornl.gov/technology/202405685) (403)
- **[SNIP, IND] 기어 접촉피로 전이학습.** 기어 접촉피로 수명을 전이학습으로 예측한 연구가 소개됐다 — [SNIP: J. Mater. Inform. 2026](https://www.oaepublish.com/articles/jmi.2026.06)
- **[SNIP] QuesTek 선례.** QuesTek의 계산 설계 기어강 Ferrium C64/C69(회전익 기어)가 선례다 — [SNIP: DTIC ADA575246](https://apps.dtic.mil/sti/tr/pdf/ADA575246.pdf)
- **[VERIFIED, CO] MagNex.** Q1 참조. 회사는 용도를 모터 전반으로 제시하며, 로봇을 명시한 원문 문장은 없다.
- **[VERIFIED, IND(학술)] 보행로봇용 모듈형 팔 위상최적화.** Edlinger & Nüchter, "AI-driven topology-optimized modular robotic arm design for legged robots"
  - 제1회 German Robotics Conference, 2025-03-14
  - "minimize material usage while maintaining structural performance"
  - 출처: [FH OÖ PURE](https://pure.fh-ooe.at/en/publications/ai-driven-topology-optimized-modular-robotic-arm-design-for-legge/)
- **[VERIFIED, IND(학술)] 사족보행 유연 다리 위상최적화.** 다리를 위상최적화로 설계하고 3D 프린팅했다. 시제품 소재는 나일론 PA2200(EOS), FEM용 E₀는 1700 MPa다.
  - 출처: [Scientific Reports 2023, s41598-023-32106-5](https://www.nature.com/articles/s41598-023-32106-5)
- **[VERIFIED, IND(학술)] Husky Carbon.** Northeastern대의 보행·비행 겸용 로봇이다. "generative design approach using Grasshopper's evolutionary solver"로 설계했다.
  - 검색 요약에 따르면 3D 프린팅 열가소성 수지를 연속 탄소섬유 사이에 끼운 구조다.
  - 출처: [arXiv 2104.05834](https://arxiv.org/abs/2104.05834)
- **[SNIP] 산업 사례.** MX3D·ABB 로봇팔 부품 생성설계(Altair 소프트웨어, 2020), DMG MORI 엔드이펙터 위상최적화가 있다. Autodesk가 직접 공개한 로봇 링크 사례는 찾지 못했다.
  - 출처: [SNIP: Digital Engineering 24/7](https://www.digitalengineering247.com/article/mx3d-makes-3d-printed-robotic-arm-lenovo-and-amd-partner-for-new-workstation-autodesk-releases-generative-design-extension-more); [SNIP: IoT ONE](https://v2.iotone.com/case-study/dmg-mori-redesigns-robotic-end-effector-using-topology-optimization-amp-reusable-workflows/c18484)
- **[VERIFIED, RPT] MS 보고서의 정성 언급.** 중국 부품업체들이 정밀도 격차를 줄이려고 "new design structures, new materials, refined manufacturing processes and AI algorithms"를 쓰고 있다고 썼다. 구체적 사례는 없다.
  - 출처: [Morgan Stanley 2025-05-14](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050)

### Inferences
- 로봇 부품 소재에 AI를 쓰는 사례는 두 층으로 나뉜다. 소재 조성 설계(강·자석)는 실험실 검증 단계다. 부품 형상 설계(위상최적화·생성설계)는 상용 CAD 도구가 이미 있다.
- 두 층을 하나로 묶은 사례, 즉 ML 설계 합금을 ML 최적화 형상에 적용한 로봇 부품은 공개된 것이 없다.
- 최종 보고서의 "AI 성숙도 매트릭스"는 다음처럼 고쳐 쓸 것을 권한다.
  - 기어·베어링 강: "학술 ML 합금설계, 로봇 미적용"
  - 구조 링크: "학술 위상최적화 시제품. Figure 03은 공정을 금형 기반으로 전환(AI 언급 없음)"

### Gaps
- Unitree, ANYbotics, Tesla, Figure가 ML 설계 소재나 생성설계 부품을 공개적으로 언급한 사례가 없다.
- 로봇 모터를 명시한 ML 자석 최적화(예: GBD Dy 저감 ML)는 원문을 찾지 못했다.

---

## 검증 요약표

| 기존 문서 주장 | 판정 | 원문 확인 수치(날짜) |
|---|---|---|
| IDTechEx 액추에이터 = 무게 56% | VERIFIED | "around 56 percent of the humanoid's weight" (2026-07-30) |
| IDTechEx 소재 목록·47% CAGR·50개 이상 제품 | VERIFIED | steel/Al/Mg, REPM, PEEK·PC-ABS (2026-06-02) |
| IDTechEx 2026–27 전환기 | VERIFIED | "key transition years" (2026-06-02) |
| IDTechEx ~2030년 100만 대 / 80% 산업용 | UNVERIFIED | 원문 두 곳에 없음 |
| MS 액추에이터 = BOM 56% | UNVERIFIED(귀속 혼선) | MS Almanac: $22k / $46k ≈ 48% (2025-12) |
| MS $5T by 2050 | VERIFIED | >$5T, ~10억 대, 90% 산업·상업용 (2025-05-14) |
| GS BOM $250k→$150k, -40%, $38B | VERIFIED | $50–250k → $30–150k (2024-01-08/02-27) |
| BofA $35k (중국산, 2025) | VERIFIED | $35k → <$17k (2030), 시범 단계 $90–100k (2026-03-12) |
| Adamas >30 t/1만 대 | PARTIAL(스니펫) | 원문: 대당 ~4 kg NdFeB (2026-04-14) |
| Adamas 880 kt by 2040 | VERIFIED(2차 본문) | Oregon Group 본문 |
| 희토류 통제 유예 | 인용 | 2027-01-10까지 연장 (2026-11-09) |
| Nabtesco RV 53–60% | PARTIAL | 회사 측 ~60%, 제3자 35–60% |
| Leaderdrive 글로벌 약 15% | VERIFIED | ~15%, 세계 2위 (2026-08-28) |
| MagNex 1억 개 이상·3개월·원가 20%·CO2 -70% | VERIFIED(CO) | (2024-06-11) |
| Niron 1,500 t, 2027 가동, $150M | VERIFIED | 2027 초 가동, OSC 최대 $150M·20년, 2공장 1만 t (2025-09-26 / 2026-08-19) |
| Figure F.03 2.3 kWh | VERIFIED | 2.3 kWh, 5 h, 2 kW, UN38.3+UL2271, 강판·다이캐스트 Al·접착제 (2025-07-17) |
| Kingfa PEEK 채택 | VERIFIED + 맥락 수정 | 과열 경고, 플라스틱 6–10 kg/대, 맞춤형 80–90% (2026-09-17) |
| Infineon 70 관절 / 600 스위치 | UNVERIFIED | Mouser 봇 차단, FE 403 |
| EPC91120 32 mm / 7·15 ARMS | VERIFIED | (2025-11-07) |
| EPC91122 / 91132 | UNVERIFIED | epc-co.com Cloudflare |
| MS–PNNL 3,200만→23, 80 h, Li -70% | VERIFIED | (2024-01-09). "N2116" 명칭은 미확인 |

---

## 접근 상태 로그

- **WebFetch**: 이번 세션에서는 시도하지 않았다(지시에 따름).
- **WebSearch**: 약 17회, 모두 성공. 검색 요약으로만 확인한 항목은 본문에 [SNIP]으로 표시했다.
- **curl 설정**: `curl -sSL -m 30 -A "Mozilla/5.0 …"`, 에이전트 프록시 경유.

| 호스트 | 결과 | 목적 |
|---|---|---|
| www.idtechex.com | HTTP 200이지만 추정한 보고서 ID(1123)가 다른 보고서(Biomanufacturing)를 반환. 데이터 없음 | IDTechEx 보고서 목차 |
| roboticsresear.ch | 성공 (200) | IDTechEx 기고문(2026-06-02) |
| roboticsandautomationnews.com | 성공 (200, 2개 페이지) | IDTechEx 액추에이터 기사, MS $3T 기사 |
| www.electronicspecifier.com | 200이지만 목록 페이지가 반환돼 본문 추출 실패 | IDTechEx 보도자료 |
| www.adamasintel.com | 성공 (200, 4개 URL. ?p=16771은 3월 기사와 같은 내용) | NdFeB kg/대, 1만 대당 톤수 |
| theoregongroup.com | 성공 (200) | Adamas·FAI 수치 |
| www.morganstanley.com | 성공 (200, $5T 기사). humanoid-robot-market-china-us는 404 | MS 시장 전망과 BOM |
| tech.yahoo.com | 성공 (200) | MS Robot Almanac BOM 보도 |
| www.goldmansachs.com | 기사 성공 (200). report.pdf는 404 | GS BOM과 TAM |
| institute.bankofamerica.com | 성공 (200, PDF) | BofA $35k와 BOM 구성 |
| fourweekmba.com | HTTP 403 | BOM 2차 정리 |
| xenospectrum.com | HTTP 403 (Cloudflare) | BOM 2차 정리 |
| www.wisdomtree.com | HTTP 403 (Cloudflare), 2개 URL | MS NdPr 1.3 kg, Li 2 kg |
| figure.ai / www.figure.ai | 성공 (200, 2개 페이지) | F.03 배터리, Figure 03 소재 |
| autonews.gasgoo.com | 성공 (200, 2개 페이지. 내용은 JS 내장 텍스트에서 추출) | Kingfa PEEK, Leaderdrive |
| www.mining.com | 성공 (200, 2개 페이지) | Niron, MagNex |
| chargedevs.com | 성공 (200) | Niron OSC 대출 |
| www.mouser.vn / mouser.com / mouser.at / mouser.in | HTTP 200이지만 "Access to this page has been denied" (봇 차단) | Infineon 70/600 주장 |
| www.futureelectronics.com | HTTP 403 | Infineon 70/600 주장 |
| www.infineon.com | 성공 (200)이지만 해당 문구 없음 | Infineon GaN 휴머노이드 페이지 |
| www.all-about-industries.com | 성공 (200), 일부 수치는 본문에서 미발견 | Infineon PCIM 취재 |
| epc-co.com | HTTP 403 (Cloudflare), 2개 URL | EPC 보도자료와 기술 기사 |
| www.powerelectronictips.com | 성공 (200) | EPC91120 사양 |
| www.businesswire.com | 실패 (HTTP/2 stream INTERNAL_ERROR, 추정 URL) | EPC 2026 보도자료 |
| news.microsoft.com | 성공 (200) | MS–PNNL 전해질 |
| www.plantautomation-technology.com | 성공 (200) | Nabtesco 점유율 |
| www.nabtesco.com | HTTP 404 (추정 URL) | Nabtesco 공식 제품 페이지 |
| marketresearch.com | HTTP 403 (Cloudflare) | HDS 50% 점유율 |
| zanerobotics.substack.com | HTTP 404 (URL slug 불일치) | 중국 감속기 강종(40CrNiMoA) |
| humanoid.guide | 성공 (200, 2개 페이지) | 플렉스플라인 강, 힘줄 소재 |
| www.harmonicdrive.net | 성공 (200) | 플렉스플라인 소재 |
| ksensors.co.kr | 성공 (200) | 6축 F/T 센서 소재 |
| www.newequipment.com | 성공 (200) | ATI Mini85 소재 |
| core.ac.uk | HTTP 403 (Cloudflare) | iCub 17-4PH 토크센서 |
| ornl.gov | HTTP 403 | ML 베이나이트 기어강 |
| repository.tudelft.nl | 성공 (200) | ML 피로강 설계 |
| doaj.org (API) | 타임아웃 (30초) | Teshugang 플렉스플라인 논문 강종 |
| bostondynamics.com | 성공 (200) | 전동 Atlas 사양 |
| www.koreajoongangdaily.com | 성공 (200) | Mobis·LG 액추에이터 |
| www.koreaherald.com | 성공 (200) | LG Axium |
| teslanorth.com | 성공 (200) | Tesla 힘줄 특허(2026-11) |
| www.shadowrobot.com | 성공 (200) | Shadow Hand 구동 |
| www.igus.com | 성공 (200) | 로봇 케이블 외피와 차폐 |
| joca-cable.com | 성공 (200) | 케이블 도체와 굴곡 수명 |
| shop.helukabel.com | 200 (내용 미사용) | 케이블 외피 |
| www.nature.com | 성공 (200) | 위상최적화 사족보행 다리 |
| pure.fh-ooe.at | 성공 (200) | AI 위상최적화 팔 |
| arxiv.org | 성공 (200) | Husky Carbon 생성설계 |
