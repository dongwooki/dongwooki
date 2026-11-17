# Materials Taxonomy for Rigid Robots (Industrial Arms, Cobots, AMRs, Quadrupeds, Humanoids) and Where AI/ML Is Applied

Research date: 2026-11-17. Method note: in this session **WebSearch worked, but every WebFetch attempt failed** (DNS/proxy refusal: the hosts were outside the session's allowed network domains). So every finding below comes from search-engine result summaries and snippets, not from full-page reads. Treat numbers as "reported by X, per search snippet". The tags below mark source type:
- **[CO]** company claim / press release
- **[RPT]** analyst or market report, usually cited second-hand
- **[TD]** teardown estimate
- **[PEER]** peer-reviewed or academic
- **[SEC]** secondary trade press or blog
- **[BG]** my own background knowledge, NOT verified this session. These appear only under Inferences.

---

## Q0. Cross-cutting industry data: humanoid BOM, weight shares, market sizes

### Takeaway
Actuators (motor + reducer/screw + bearings + encoder + driver) dominate humanoid materials demand. IDTechEx puts them at about 56% of humanoid weight, and several analysts put them at about 50–60% of BOM cost. The materials questions with the most at stake are therefore magnets, gear/bearing steels, and lightweight structural alloys and plastics. Market-size forecasts differ by an order of magnitude.

### Cited Findings
- **[RPT] IDTechEx, "Materials for Humanoid Robots 2026–2036: Technologies, Players, Forecasts"** (press coverage June–July 2026):
  - about 56% of a humanoid's weight comes from actuators
  - structural actuator parts rely on metal alloys
  - REPMs (NdFeB) are critical for actuator motors
  - the report has 10-year demand forecasts segmented by metal alloys (steel, aluminum and magnesium), rare-earth permanent magnets and engineering plastics (PEEK, PC-ABS)
  - it covers 50+ humanoid products and prototypes
  - the overall humanoid market is expected to "approach a million units around 2030"
  - 47% CAGR in unit sales over the decade
  - 80% of humanoids and prototypes to date were designed for industrial settings
  - 2026–2027 are "key transition years"
  - soft actuators (EAP, SMA, piezo) are being explored, but rigid actuators remain the mainstay
  - Sources: [IDTechEx-hosted article](https://roboticsresear.ch/articles/34801/emerging-materials-opportunities-and-trends-in-the-humanoid-market); [Robotics & Automation News, 2026-07-30](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/); [Electronic Specifier](https://www.electronicspecifier.com/?p=208138); [TimesTech](https://timestech.in/?p=409409). Full report text, tonnage forecasts and price were not accessible (see access log).
- **[RPT, second-hand] Morgan Stanley:**
  - actuators about 56% of total humanoid BOM
  - planetary roller screws $1,350–2,700 each, about a dozen per full-size humanoid
  - one secondary source attributes the same roller-screw price range to J.P. Morgan, an attribution conflict
  - a high-end harmonic reducer is about $800–1,500
  - Sources: [FourWeekMBA](https://fourweekmba.com/what-does-it-cost-to-build-a-humanoid-robot/); [xenospectrum](https://xenospectrum.com/en/humanoid-robot-bom-actuator-cost/); [holistic.news](https://holistic.news/en/planetary-roller-screws-essential-for-robotics/)
- **[RPT, second-hand] X.PIN China supply-chain estimate (2026), shares of component cost:**
  - precision reducers about 21%
  - motors about 19%
  - lead/roller screws about 19%
  - joint hardware total about 59%
  - Source: [search summary of humanoid BOM articles](https://xenospectrum.com/en/humanoid-robot-bom-actuator-cost/)
- **[SEC] humanoid.guide chart:** actuators about 50% of a roughly $50K BOM, end effectors about 15%, sensors about 10% — [humanoid.guide supply chain](https://humanoid.guide/the-humanoid-robot-supply-chain/)
- **[RPT] Goldman Sachs (Jan/Feb 2024):**
  - high-spec humanoid BOM fell about 40%, from about $250k (2022) to about $150k per unit (2023)
  - original humanoid TAM forecast $38B by 2035
  - later revisions reported as 2035 shipments of about 6.5M units (up from 1.38M) and about $138B; the revision is second-hand
  - Sources: [Goldman Sachs report PDF](https://www.goldmansachs.com/intelligence/pages/gs-research/global-automation-humanoid-robot-the-ai-accelerant/report.pdf); [GS $38B article](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035); [humanoid.guide on GS revision](https://humanoid.guide/goldman-raises-2035-humanoid-robot-forecast-to-6-5-million/)
- **[RPT] Bank of America:** BOM of about $35,000 per unit by end-2025 if most components are sourced from China — [FourWeekMBA](https://fourweekmba.com/what-does-it-cost-to-build-a-humanoid-robot/)
- **[RPT] Morgan Stanley (2025):**
  - about $5T humanoid market by 2050 ($4.7T annual hardware revenue in one version)
  - a later note projects a 1 billion-unit installed base by 2050, implying about $7.5T per year on a 6-year replacement cycle
  - China 302.3M units vs US 77.7M by 2050
  - Sources: [Morgan Stanley](https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050); [itiger summary](https://www.itiger.com/news/1124207069)
- **[RPT] TrendForce (2026-01-28):** global humanoid shipments to surpass 50,000 units in 2026; robot solid-state battery demand about 74 GWh by 2035 — [TrendForce press](https://www.trendforce.com/presscenter/news/20260128-12902.html); [Electrek 2026-01-30](https://electrek.co/2026/01/30/report-humanoid-robots-set-to-drive-demand-for-solid-state-batteries/)
- **[CO/SEC] Tesla Optimus Gen 1 (AI Day 2022-09-30):**
  - 28 structural actuators
  - consolidated into 6 or 7 actuator types (sources conflict); one source says 3 rotary + 3 linear
  - hand with 6 actuators and 11 DoF
  - "500 kg" claims are ambiguous between a single leg actuator and the whole system
  - Sources: [engineering.com](https://www.engineering.com/tesla-ai-day-2022-tesla-is-not-a-car-company/); [Robotics 24/7](https://www.robotics247.com/article/tesla_ai_day_2022_optimus_robot); [InsideEVs](https://insideevs.com/news/613692/tesla-humanoid-robot-ai-day-2022/)

### Inferences
- If actuators are 50–60% of BOM and about 56% of mass, then materials for actuators (NdFeB, electrical steel, copper, gear/bearing steels, Al/Mg housings) are where most value and most supply-chain risk sit. Shell and structure plastics matter more for mass than for cost.
- The gap between BoA's $35k (China-sourced) and Goldman's $150k (2023 high-spec) shows that localization in the Chinese component chain is a cost lever as large as any change of material.

### Gaps
- Full IDTechEx tonnage-by-material forecasts (kg per humanoid for Al, Mg, steel, PEEK) could not be retrieved, because idtechex.com and its hosted sites were blocked.
- No primary Morgan Stanley or Goldman report text was read. All BOM shares are second-hand.

---

## Q1. Structural and body materials

### Takeaway
Humanoid and cobot structures are mainly aluminum alloys (machined or die-cast), with magnesium, high-strength steels at load points, CFRP, and a fast-growing share of PEEK/CF-PEEK and glass-filled polyamides for limbs, shells and even reducer parts. Chinese OEMs (Tesla supply chain, Unitree, AgiBot) are publicly adopting PEEK. ML alloy design is most mature for Mg/Al casting alloys.

### Taxonomy table
| Subcategory | Specific materials | Robot components | Key properties | Representative suppliers/examples | Supply-chain issues | AI/ML use |
|---|---|---|---|---|---|---|
| Al alloys | 6061-T6, 7075-T6, die-cast A380/ADC12 [BG] | Link tubes, actuator housings, arm castings, AMR chassis | Specific stiffness, machinability, castability | IDTechEx lists "aluminum & magnesium" as forecast segments ([source](https://roboticsresear.ch/articles/34801/emerging-materials-opportunities-and-trends-in-the-humanoid-market)) | Energy-intensive primary Al; China dominant [BG] | ML casting-alloy design (strength vs. thermal conductivity) ([JMI review](https://www.oaepublish.com/articles/jmi.2025.99)) |
| Mg alloys | AZ-series, rare-earth-free Mg-Al-Zn-Ca-Mn | Lightweight housings, frames | Lowest-density structural metal | Same IDTechEx segment | China supplies most primary Mg [BG]; corrosion | ML found Mg-2Al-1Zn-0.6Ca-0.4Mn: 344 MPa UTS, 21.3% elongation; MZAX2000: 395 MPa UTS, 17.9% elongation ([JMI 2025](https://www.oaepublish.com/articles/jmi.2024.92); [J. Magnesium & Alloys 2025](https://doaj.org/article/0b1d91fb06334606986c0d9a8c4fd201)) |
| Ti alloys | Ti-6Al-4V (LPBF) [BG] | High-load brackets, printed nodes | Strength-to-weight, fatigue | — | Cost; aerospace competition | ML LPBF defect prediction ([Nezhad et al. UVic, Ti-45Nb](https://dspace.library.uvic.ca/items/189ed91b-b50f-48cb-9b64-69049f3a03e6)) |
| High-strength steels | Alloy/bearing steels | Joint shafts, reducer and screw parts (see Q3) | Fatigue, hardness | IDTechEx "steel" segment | — | See Q3 |
| CFRP and CF-thermoplastics | CF/PEEK, CF/epoxy | Limb shells, thigh/shank links, reducer components | Specific stiffness | Tianfeng Securities pairs "PEEK and carbon fiber" as AI-humanoid beneficiaries ([moomoo](https://www.moomoo.com/news/post/36693220/tianfeng-securities-ai-empowers-humanoid-robots-peek-and-carbon-fiber)) | Cost; joining | — (no robot-specific ML-CFRP example found) |
| Engineering plastics | PEEK, PA66-GF, PC-ABS, POM | Shells, covers, bushings, plastic gears, joints | Strength, wear resistance, mouldability | Kingfa Tech (China); Tesla, Unitree, AgiBot reported to use PEEK ([Gasgoo 2026](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)) | 80–90% of humanoid material solutions highly customized | — |
| AM and lattices | Photopolymer lattices, LPBF metals | XPeng IRON limb "muscle" lattices (secondary claim); lattice legs | Tunable stiffness | XPeng IRON ([FacFox](https://facfox.com/docs/kb/3d-printed-photopolymer-lattices-the-hidden-muscle-behind-xpengs-humanoid-robot)); EPFL lattice robot ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12266121/)) | — | Generative and topology optimization (level-set, lattice+skin) patents ([USPTO 11663379](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11663379)) |

### Cited Findings
- **PEEK in Optimus [SEC, unverified, 2024–2025]:** Optimus Gen 2 reportedly lost about 10 kg and walked about 30% faster, credited to PEEK lightweighting; Tesla never confirmed this — [peekchina blog](https://peekchina.blogspot.com/2024/12/why-peek-is-key-material-for-teslas.html); [Brewminate](https://brewminate.com/peek-carbon-fiber-composites-are-driving-the-humanoid-robot-lightweighting-wave/)
- **PEEK content estimate [SEC]:**
  - about 1 kg pure PEEK plus about 8 kg CF/PEEK per robot, given as "about 6.6 kg total" (internally inconsistent in the snippet)
  - another estimate is 105,000 t of PEEK for 10 million robots, about 10.5 kg per robot
  - a PEEK-CF harmonic reducer is claimed at 0.25 kg, more than 56% lighter than metal
  - Sources: [Brewminate](https://brewminate.com/peek-carbon-fiber-composites-are-driving-the-humanoid-robot-lightweighting-wave/); [londonlovesbusiness](https://londonlovesbusiness.com/peek-carbon-fibre-composites-are-driving-the-humanoid-robot-lightweighting-wave/)
- **Kingfa Tech interview (Gasgoo, 2026) [CO]:** Tesla, Unitree and AgiBot "have begun incorporating PEEK"; 80–90% of humanoid material solutions are highly customized — [Gasgoo](https://autonews.gasgoo.com/articles/market-industry/embodied-ai-from-a-materials-perspective-yu-fei-of-kingfa-tech-discusses-industry-challenges-and-material-solutions-2100425756185628673)
- **Korean press:**
  - Hankyung (2026-07) says humanoid skeletons must be "strong yet light" ([한국경제 매거진](https://magazine.hankyung.com/business/article/202607304292b))
  - BizWatch (2026-08-20) says composites and super-engineering plastics are emerging for robot skeletons ([비즈워치](https://news.bizwatch.co.kr/article/industry/2026/08/20/0035))
  - IB Tomato says Korean materials and sensors still depend on imports, a risk of "half localization" ([IB토마토](https://ibtomato.com/View.aspx?no=17642&type=1))
- **Unitree [SEC]:** G1 about 1.3 m and about 35 kg; H1 about 1.8 m and about 47 kg. No body-material specification found — [The Robot Report](https://www.therobotreport.com/unitree-robotics-unveils-g1-humanoid-for-16k/)
- **Figure 03 battery [SEC]:** the battery pack reportedly uses stamped steel and cast aluminum as part of the structure — see Q4.

### Inferences
- [BG] 6061-T6 (about 2.7 g/cc, yield about 275 MPa) and 7075-T6 (yield about 500 MPa) are the usual machined-link alloys in cobots and quadrupeds, and die-cast Al is usual for industrial-arm castings (e.g., the Fanuc and Yaskawa arm families). None of this was verified this session.
- The PEEK numbers come from PEEK-industry and brokerage promotional content and should be labelled "industry-promoted estimates".

### Gaps
- No verified kg-per-humanoid figure for Al, Mg or steel. That is the IDTechEx report's content, which was blocked.
- No teardown-confirmed body material for Unitree, UBTech or Optimus. iFixit has a G1 page, but no material data came up in search.
- No robot-specific ML-designed alloy or composite found in deployment.

---

## Q2. Actuation and motor materials

### Takeaway
Sintered NdFeB, with Dy/Tb added (often by grain-boundary diffusion), is the default magnet in humanoid joint motors (frameless torque, coreless). Estimates of content per humanoid range from about 2 to 4.5 kg of magnet, or about 0.6–1.3 kg of NdPr. China's 2025 export-control regime on Dy, Tb, Sm and magnets is the defining supply-chain risk. Rare-earth-free routes are pilot-to-early-industrial: Niron FeN (US plant 2027) and the AI-designed Materials Nexus MagNex (2024 lab claim).

### Taxonomy table
| Subcategory | Materials | Components | Key properties | Suppliers/examples | Supply chain | AI/ML |
|---|---|---|---|---|---|---|
| REPM | Sintered NdFeB (NdPr), Dy/Tb via grain-boundary diffusion (GBD) | Frameless torque motors and coreless motors in every joint; rotor assemblies | High (BH)max, coercivity at temperature | JL Mag (GBD over 75% of its NEV magnet shipments; small-batch humanoid rotor assemblies); Zhenghai Magnetic (small-batch humanoid supply, July disclosure; low- or no-heavy-RE magnets); Ningbo Yunsheng (mass supply to a domestic humanoid customer by Q3 2024) ([faxiangongchang](https://faxiangongchang.com/en/reports/china-rare-earth-magnet-2026); [rareearthexchanges](https://rareearthexchanges.com/?p=188660); [moomoo](https://moomoo.com/news/post/46396670/ningbo-yunsheng-600366-sh-for-a-domestic-humanoid-robot-customer)) | China export licences from April 2025, expanded 2025-10-09 | AI magnet discovery (below) |
| RE-free magnets | Iron nitride (FeN), ferrite, MnAl [BG], MagNex (AI-designed) | Lower-spec joints and fans (prospective) | Supply security | Niron Magnetics: Sartell MN plant, 1,500 t/yr, operations 2027; proposed second plant 10,000 t/yr (site selection March 2026); conditional $150M US DoW/OSC loan (2026-08-07) ([Mining.com](https://www.mining.com/niron-breaks-ground-on-rare-earth-free-magnet-manufacturing-plant-in-minnesota/); [Charged EVs](https://chargedevs.com/newswire/niron-magnetics-wins-conditional-150-million-loan-commitment-for-rare-earth-free-magnets/); [pulse.bot](https://www.pulse.bot/real-estate/news/niron-magnetics-begins-site-selection-for-18b-magnetics-plant-b9c91532-c239-46e6-9f6b-f35e73b5572e)) | Lower energy product than NdFeB [BG]; performance claims not independently verified ([geomechanics.io](https://www.geomechanics.io/news/article/niron-magnetics-150m-backing-iron-nitride-plant-economics-for-engineers)) | MagNex |
| Soft magnetics | Electrical steel laminations, SMC [BG] | Stators | Low core loss at high frequency | — | — | (none found) |
| Windings and insulation | Cu (Al alternative) [BG] | Stator windings | Conductivity | WisdomTree: actuators drive magnet and copper demand ([WisdomTree](https://www.wisdomtree.com/ch/en/insights/blog/humanoid-robots-could-drive-new-demand-for-critical-minerals)) | Cu price | — |

### Cited Findings
- **Per-robot magnet content [RPT, second-hand]:**
  - Morgan Stanley: about 1.3 kg NdPr per humanoid across motors and actuators. Its chart of critical-mineral weight per humanoid is dated May 2025 ([WisdomTree](https://www.wisdomtree.com/ch/en/insights/blog/humanoid-robots-could-drive-new-demand-for-critical-minerals); [ValueTheMarkets](https://www.valuethemarkets.com/analysis/are-humanoids-the-next-rare-earth-demand-shock))
  - estimates attributed to the Foundation for American Innovation: 2–4.5 kg NdFeB per robot, containing about 0.57–1.3 kg NdPr and 35–79 g Dy ([Oregon Group](https://theoregongroup.com/latest-news/where-will-the-metals-for-the-robot-revolution-come-from/))
  - one Adamas-linked summary: about 4 kg NdFeB per advanced humanoid
  - **Adamas Intelligence [RPT]:** with 30–40 DoF per professional service humanoid, every 10,000 units consume more than 30 t NdFeB, i.e. 3+ kg per unit, consistent with the above
  - Adamas also projects robotics NdFeB demand growing at about 28% CAGR to 2040, and global NdFeB demand nearly quadrupling, 2024 to 2040, to more than 880,000 t
  - Adamas: 63 million robots would need 1.2 times current annual NdFeB output
  - Sources: [Adamas](https://www.adamasintel.com/humanoid-robots-and-the-future-of-motors-and-ndfeb-markets/); [Oregon Group](https://theoregongroup.com/latest-news/where-will-the-metals-for-the-robot-revolution-come-from/)
- **Lithium [RPT]:** WisdomTree illustrates 2 kg Li per humanoid, so 10M humanoids would need 20,000 t Li — [WisdomTree](https://www.wisdomtree.com/ch/en/insights/blog/humanoid-robots-could-drive-new-demand-for-critical-minerals)
- **Export controls:**
  - April 2025: 7 medium and heavy REEs (incl. Sm, Tb, Dy) placed under licensing, covering Dy-containing NdFeB and SmCo magnets
  - 2025-10-09: MOFCOM expansion adds 5 more REEs, alloys, oxides and technology, plus extraterritorial rules for foreign products with Chinese content
  - Dy/Tb prices inside and outside China have diverged
  - DIGITIMES (2025-04-08): "robotics sector braces for impact"
  - Optimus was reportedly affected by magnet sourcing (secondary)
  - status by November 2026 is unclear: Fastmarkets refers to a "November 2026 deadline" and continued licence approvals
  - Sources: [CSIS](https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions); [China Briefing](https://www.china-briefing.com/news/chinas-rare-earth-export-controls-impacts-on-businesses/); [DIGITIMES](https://www.digitimes.com/news/a20250408PD207.html); [Fastmarkets](https://www.fastmarkets.com/insights/chinas-looming-november-export-controls-test-rare-earth-refining-recycling-ambitions/)
- **JL Mag (2026) [CO/SEC]:**
  - selected as supplier for "a world-renowned technology company's" humanoid motor rotor project (unnamed)
  - capacity target 60,000 t by 2027
  - management says humanoid demand is still "small pilot orders"
  - Sources: [faxiangongchang](https://faxiangongchang.com/en/reports/china-rare-earth-magnet-2026); [JL Mag IR PDF 2026-04](https://irtc.jlmag.com.cn/upload/2026-04/177570783220860200.pdf)
- **AI-discovered magnet [CO, mid-2024]:**
  - Materials Nexus (UK) MagNex: the AI screened more than 100M rare-earth-free compositions for performance, cost, supply security and environment
  - designed, synthesized and tested in about 3 months with the Henry Royce Institute and the University of Sheffield
  - claims about 20% of material cost and about 70% lower material CO2
  - no peer-reviewed magnetic data or commercial availability reported
  - Sources: [Mining.com](https://www.mining.com/ai-helps-quickly-develop-rare-earth-free-permanent-magnet/); [New Atlas](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery); [ScienceAlert](https://www.sciencealert.com/ai-designs-radical-magnet-free-of-rare-earth-metals-in-just-3-months)
- **Korea:**
  - Hyundai Mobis will supply actuators for Atlas mass production (CES 2026), but the CES 2026 Atlas prototype used foreign-made actuators ([Korea JoongAng Daily](https://www.koreajoongangdaily.com/business/actuators-become-new-battleground-in-humanoid-robot-race/12288658); [The Investor](https://m.theinvestor.co.kr/article/10651805))
  - LG Electronics is launching an "Axium" actuator line as a B2B component business ([Korea JoongAng Daily](https://www.koreajoongangdaily.com/business/actuators-become-new-battleground-in-humanoid-robot-race/12288658))
  - LG and KIST formed a humanoid team (2026-05) ([Asiae](https://www.asiae.co.kr/en/article/2026051809402928633))

### Inferences
- With 3–4 kg of NdFeB per humanoid, 1M humanoids per year (the IDTechEx ~2030 scale) would need about 3,000–4,000 t per year of NdFeB. That is small against more than 880 kt of global demand by 2040, so the problem is Dy/Tb access and export licensing rather than total tonnage. This matches the "cost is less of the problem than supply" view in [China Briefing](https://www.china-briefing.com/news/chinas-rare-earth-export-controls-impacts-on-businesses/).
- [BG] Hydraulic actuation (the earlier hydraulic Atlas) used AM titanium/steel manifolds. The commercial field has moved to electric actuation, so hydraulic materials are now niche.

### Gaps
- Magnet grade distribution (N-grade, Dy content per robot) was not found in primary sources.
- No primary data on electrical steel or SMC grades in humanoid frameless motors.
- MnAl status was not researched (budget).

---

## Q3. Transmission and joint materials

### Takeaway
Humanoid rotary joints use strain-wave (harmonic) reducers or planetary/cycloidal gearboxes. Linear joints (Optimus-style) use planetary roller screws (PRS), which are import-dependent in China (about 80%). Japanese incumbents hold the premium reducer market (Nabtesco RV about 53–60% global share; Harmonic Drive Systems the global strain-wave leader), with Leaderdrive about 15% global. The materials science that matters is the fatigue of flexspline steel, the case-hardened and bearing steels for screws and gears, and lubrication. ML here is mostly tribology and lubricant surrogate modelling plus FE-plus-S-N fatigue prediction, still at academic stage.

### Taxonomy table
| Subcategory | Materials | Components | Properties | Suppliers | Supply chain | AI/ML |
|---|---|---|---|---|---|---|
| Strain-wave | Flexspline alloy steel (quenched and tempered) [BG: e.g., 40CrNiMoA in Chinese literature, unverified]; PEEK-CF variants | Wrist, elbow and shoulder joints | Fatigue under asymmetric alternating stress; fine grain | Harmonic Drive Systems (JP); Leaderdrive (CN, about 15% global, 30–40% China) ([Gasgoo](https://autonews.gasgoo.com/articles/news/leaderdrive-plans-hong-kong-ipo-2093357096908443649)) | Leaderdrive Hong Kong IPO plan | FE + S-N fatigue life (nCode) ([Jixie chuandong 2022](https://doaj.org/article/0b39259eca3f4d018806d054cb9b857e)) |
| RV / cycloidal | Bearing and gear steels [BG] | Industrial arm bases and shoulders | Torsional stiffness, shock | Nabtesco 53–60% global, about 60% China; Zhongda Leader, Zhenkang >30% of Chinese-assembled robots (claimed) ([Zane Robotics](https://zanerobotics.substack.com/p/the-technical-gap-in-chinese-robot-reducers); [evsint](https://www.evsint.com/industrial-robot-reducers-harmonic-cycloidal-rv-comparison-2026/)) | China lags in premium RV | — |
| PRS / ball screws | Bearing and high-strength alloy steels (grade not confirmed) | Linear actuators (Optimus: 14 PRS reported; 4 in calves) | Load capacity, thread-grinding precision | GSA (CH), Rollvis, Ewellix (Schaeffler), SKF hold >70%; Chinese entrants from auto and bearings ([holistic.news](https://holistic.news/en/planetary-roller-screws-essential-for-robotics/); [KGG](https://www.kggfa.com/news/the-application-of-planetary-roller-screws-in-humanoid-robots-and-market-development)) | China about 80% import dependence | — |
| Bearings | Bearing steel; hybrid Si3N4 balls | Crossed-roller and output bearings | Si3N4 up to about 40% lighter than steel; brittle under shock | Citizen Fine Devices markets ceramic robot-arm bearings ([ipros](https://pr.mono.ipros.com/en/cfd-citizen/product/detail/2001604608)); Barden hybrid ([Barden](https://www.bardenbearings.co.uk/hybrid-bearings)) | — | — |
| Lubricants | Greases (amide-based etc.) | Reducers, screws | Friction, wear, life | — | — | ML/PINN tribology (below) |
| Tendons | Elastic cables (Optimus hand) | Finger tendons driven from the forearm | Strength, creep | Tesla (Nov 2024) ([Electrek](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/)) | — | — |

### Cited Findings
- **Flexspline fatigue [PEER]:**
  - fatigue fracture of the flexspline is the main harmonic-gear failure mode
  - a 2024 failure analysis (Teshugang) attributed fracture to coarse prior-austenite grain and banding, and recommends cyclic heat treatment or normalizing to refine grain ([DOAJ 2024](https://doaj.org/article/58e93d94db464baca2fb226676ca1987))
  - Harmonic Drive LLC claims no flexspline fatigue failures within published repeated-torque limits [CO] ([Harmonic Drive PDF](https://www.harmonicdrive.net/media/3355/final-vol-1_basics-of-strain-wave-gears_md6698_harmonicdrive_v2.pdf))
- **Optimus PRS count conflict [SEC]:** 14 PRS from GSA (Switzerland) per a 36Kr supply-chain analysis, vs. 4 PRS in the calves — [holistic.news](https://holistic.news/en/planetary-roller-screws-essential-for-robotics/); [Fast Company](https://www.fastcompany.com/91314612)
- **ML in tribology [PEER]:**
  - a stacking-ensemble model predicted friction and wear of amide-based greases and optimized additive ratios: R² 0.9939 (COF) and 0.9535 (wear scar) ([Friction, DOI 10.26599/FRICT.2025.9440982](https://sciopen.com/article/10.26599/FRICT.2025.9440982))
  - an ANN surrogate for TEHL contacts in gears and bearings reached R² above 0.99 ([engrxiv](https://engrxiv.org/preprint/download/5823/9696/8110))
  - a CNN with Grad-CAM was used on tribofilms ([Sci. Rep. 2024](https://doaj.org/article/135e61b66ddc4834be07579483ad9885))
  - PINN friction and wear models exist ([sciforum](https://sciforum.net/paper/37480))
  - a 2026 review covers AI and digital twins in tribology ([tribology.rs](https://tribology.rs/journals/2026/2026-2/6-2096.pdf))
  - no industrial deployment of AI-designed reducer greases was found

### Inferences
- The materials that limit reducers (clean, fine-grained alloy steel with controlled heat treatment) explain why the Chinese harmonic reducer has caught up (Leaderdrive) while RV has lagged. The Zane Robotics analysis frames the gap as process and know-how rather than composition.
- [BG] Plastic (POM/PA) gears appear in low-load hand and finger and in toy-grade robots. UHMWPE (Dyneema) tendons are used in research hands. Neither was verified this session for commercial humanoids.

### Gaps
- Steel grades for flexsplines and PRS (e.g., 40CrNiMo, GCr15/52100) were not confirmed from sources.
- No market-share figure for Harmonic Drive Systems itself.
- Fanuc and Yaskawa materials data were not researched.

---

## Q4. Energy materials

### Takeaway
Humanoid packs cluster around about 2.3 kWh of Li-ion: Figure F.03 is confirmed by the company, and Optimus Gen 2 is a teardown estimate. Structural, cell-to-body integration is the design trend. 2026 brings the first small-batch solid-state packs for humanoids from Chinese makers (XPeng IRON, GAC GoMate, CALB, Farasis sulfide samples). AI for battery materials includes Microsoft–PNNL's 32M-candidate electrolyte screen and the KAIST–POSCO autonomous cathode lab.

### Cited Findings
- **Figure F.03 battery [CO]:**
  - 2.3 kWh, about 5 h runtime at peak performance
  - about 2 kW charging (some outlets)
  - UN38.3 and UL2271 certifications
  - pack built with stamped steel and cast aluminum as structural members (secondary)
  - a third-party page listing 1.2 kWh Li-Po conflicts with this
  - Sources: [Figure](https://figure.ai/news/f-03-battery-development); [eeNews Europe](https://test.eenewseurope.com/en/structural-battery-boost-for-humanoid-robot)
- **Optimus Gen 2 [TD]:** about 2.3 kWh, 52 V pack, attributed to a Morgan Stanley teardown. Tesla has not confirmed it. The 4680-cell link is forum speculation only — [liveinthefuture](https://liveinthefuture.org/stories/optimus-battery-irrelevance-43-robot-model-s-math); [TMC forum](https://teslamotorsclub.com/tmc/threads/tesla-tsla-the-investment-world-the-perpetual-investors-roundtable.139047/post-7987650)
- **Solid-state for robots (2025–2026) [CO/SEC]:**
  - XPeng has begun small-batch SSB production for IRON (chemistry unspecified; supplier a second-tier Chinese maker) ([battery-tech.net](https://battery-tech.net/battery-markets-news/xpeng-solid-state-battery-production/); [Notebookcheck](https://notebookcheck.net/First-solid-state-battery-for-humanoid-robots-goes-to-anthropomorphic-Iron.1440230.0.html))
  - GAC's GoMate uses an all-solid-state battery
  - CALB claims more than 450 Wh/kg and thousands of robot units by Q4 2026
  - Farasis shipped sulfide ASSB samples for humanoids in September 2025
  - CATL's solid-state EV packs are slated for 2030+, with no robot deal found
  - EcoPro (KR) is targeting humanoid battery materials
  - Sources: [Gasgoo](https://autonews.gasgoo.com/articles/icv/will-robots-be-the-first-to-sample-solid-state-batteries-2052295407034589184); [iConnect007](https://iconnect007.com/article/148590/humanoid-robots-near-commercialization-as-solidstate-batteries-advance/148587/ein); [cryptobriefing](https://cryptobriefing.com/ecopro-humanoid-robotics-battery-materials/)
- **TrendForce:** about 74 GWh of robot SSB demand by 2035 — [TrendForce](https://www.trendforce.com/presscenter/news/20260128-12902.html)
- **Microsoft Azure Quantum Elements + PNNL (Jan 2024) [CO]:**
  - about 32M candidates generated, narrowed to about 500k stable, then 800, then 23 after practicality filters (5 already known)
  - N2116 solid electrolyte selected
  - screening took about 80 hours; the process was described as taking "two weeks" vs. years
  - claimed up to about 70% less lithium
  - composition reporting is inconsistent across outlets; not commercial
  - Sources: [Microsoft](https://news.microsoft.com/source/features/sustainability/how-ai-and-hpc-are-speeding-up-scientific-discovery/); [Latitude Media](https://www.latitudemedia.com/news/armed-with-ai-microsoft-found-a-new-battery-material-in-just-two-weeks)
- **KAIST (Prof. Seo Donghwa) + POSCO Holdings autonomous cathode lab (announced 2025-08-03) [CO/press]:**
  - closed-loop AI recommends the next composition and synthesis conditions
  - about 12 times more material data than researcher-led experiments
  - POSCO N.EX.T Hub plans to apply an upgraded version after 2026
  - this is POSCO Holdings, not POSCO Future M
  - Sources: [Asiae](https://www.asiae.co.kr/en/article/2025080309221574066); [EurekAlert](https://www.eurekalert.org/news-releases/1103418); [AlphaGalileo](https://www.alphagalileo.org/en-gb/Item-Display/ItemId/261869)

### Inferences
- At about 2.3 kWh and 5 h runtime, per-robot battery materials are small (for comparison, about 1/30 of an EV). Robots are a low-volume, premium-safety niche, which explains why SSB makers target them first: safety near humans, plus willingness to pay.
- [BG] NMC is typical in high-density humanoid packs; LFP is common in AMRs and industrial mobile robots. Not verified this session.

### Gaps
- Optimus cell format (2170 vs 4680) is unconfirmed.
- Pack thermal materials (aerogel, mica, phase-change) for robots were not researched.

---

## Q5. Electronics, sensing, thermal

### Takeaway
Wide-bandgap GaN is the near-term winner for in-joint motor drivers, because it allows small, heatsink-free inverters in 23–32 mm footprints. SiC fits higher-voltage industrial drives [BG]. Thermal management inside compact joints is a recognised but poorly documented problem.

### Cited Findings
- **EPC GaN boards for humanoid joints [CO]:**
  - EPC91120 (about November 2025): 32 mm diameter, three EPC23102 half-bridges, 7 ARMS without heatsink, 15 ARMS in a motor casing
  - EPC91122 (Feb 2026): 100 V, up to 20 ARMS, 100 kHz PWM default
  - EPC91132 (June 2026): 23 mm, EPC33110 three-phase GaN module
  - EPC91104 for wrist and finger joints (14 Apk / 20 Apk pulsed); EPC9176 for elbow and knee
  - Sources: [Power Electronic Tips](https://www.powerelectronictips.com/three-phase-gan-driver-fits-32-mm-robotic-joints/); [EPC news](https://epc-co.com/epc/about-epc/events-and-news/news/artmid/1627/articleid/3261/epc-accelerates-robotics-innovation-with-integrated-3-phase-bldc-motor-drive-inverter); [EPC article](https://epc-co.com/epc/design-support/technical-publications/articles/artmid/9702/articleid/3314/humanoid-robotics-is-a-power-electronics-problem)
- **Infineon CoolGaN for humanoids [CO]:** a humanoid can have more than 70 joints and up to 600 power switches; GaN lowers inverter losses so heatsinks can shrink — [Mouser/Infineon](https://www.mouser.vn/infineon-gan-based-motor-control-for-humanoid-robots)
- **Thermal [SEC/vendor]:** compact humanoid structures leave little room for traditional cooling, so thin thermal tapes and pads are favoured. PatSnap claims a 3.7 times thermal-resistance improvement for immersion over a liquid jacket (unsourced, marketing) — [ysdiecut](https://www.ysdiecut.com/?p=42243); [PatSnap](https://www.patsnap.com/resources/blog/articles/cut-humanoid-robot-joint-actuator-weight-by-40-50/)
- **Korean view [SEC]:** control of joints and sensors is seen as key to humanoid commercialization — [The Investor](https://m.theinvestor.co.kr/article/10701643)

### Inferences
- 600 switches per robot, if GaN, makes humanoids a meaningful new GaN-on-Si volume market.

### Gaps
- Encoder materials (magnetic vs optical), F/T sensor strain-gauge alloys, LiDAR and camera optics, and EMI shielding were not covered within the tool budget.
- No peer-reviewed data on TIMs for humanoid joints.
- SoC and semiconductor content per robot was not quantified.

---

## Q6. Hands, end-effectors and covering

### Takeaway
Hands are the most materials-intensive subsystem per gram: tendons, soft protective skins over tactile arrays, and high actuator density. Vendors disclose capabilities (DoF, gram-level sensitivity) but almost never the materials.

### Cited Findings
- **Tesla Optimus hand (Nov 2024) [CO via press]:**
  - 22 DoF in the hand plus 3 in the wrist and forearm
  - all actuators moved to the forearm, pulling "strong, elastic cables" as tendons
  - planned tactile integration and forearm weight reduction by end-2024
  - Konstantinos Kovac said the challenge is "balancing the squishiness of the protective layer… without compromising tactile sensing"
  - a 2026 blog claims the Gen 3 hand has 50 actuators (unverified)
  - Sources: [Electrek 2024-11-29](https://electrek.co/2024/11/29/tesla-unveils-upgraded-optimus-robot-hand-but-impressive-demo-is-again-teleoperated/); [The Decoder](https://the-decoder.com/tesla-gives-optimus-robot-a-new-hand-with-improved-grip-and-sensors/); [Basenor](https://www.basenor.com/blogs/news/tesla-optimus-gen-3-hands-22-dof-50-actuators-explained)
- **Figure 03 (Oct 2025) [CO via secondary]:** palm and fingertip tactile sensors detect forces as small as 3 g — [Baltimore Chronicle](https://baltimorechronicle.com/?p=300009); [Notebookcheck](https://www.notebookcheck.net/Figure-03-Humanoid-robot-debuts-with-wireless-charging-and-ultra-sensitive-tactile-palms.1134940.0.html). Soft textile and foam covering materials were not confirmed in search.
- **Sanctuary AI Phoenix (Feb 2025) [CO]:** new tactile sensors integrated (technology from its acquisition of Tangible Research about 2 years earlier), enabling blind picking. Sources conflict on whether this is the 7th or 8th generation — [The Robot Report](https://www.therobotreport.com/sanctuary-ai-integrates-tactile-sensors-into-phoenix-general-purpose-robots/); [Robotics 24/7](https://www.robotics247.com/article/sanctuary-ai-equips-phoenix-humanoids-with-new-touch-sensors)
- **Loomia (textile tactile):** a 131-point tactile sensor for Festo's robotic hand — [Loomia blog](https://www.loomia.com/blog/tactile-sensing-robotic-hand)
- **Research substrates [PEER]:** piezoresistive tactile sensors on fabric and anti-static foam for robot hands — [arXiv 2011.06048](https://arxiv.org/pdf/2011.06048.pdf)
- **Korean press [SEC]:** "from metal to rubber", materials as the humanoid core — [IB토마토](https://ibtomato.com/View.aspx?no=17642&type=1)

### Inferences
- [BG] Fingertip elastomers are usually silicone or TPU, and covers are TPU or textile. Wear-resistant coatings (e.g., PU) apply to grippers. Not verified this session.

### Gaps
- No teardown-level material data for the Optimus, Figure or Sanctuary skins.
- Tendon material (UHMWPE vs steel) for Optimus is not disclosed.

---

## Q7. Other classes (cables, adhesives, coatings) and cross-cutting AI/ML methods

### Takeaway
Material-level AI is real but uneven across classes:
- **Strongest evidence:** discovery screens (MagNex magnets, Microsoft–PNNL electrolytes), autonomous labs (KAIST–POSCO cathodes), and ML alloy design (Mg alloys with reported properties).
- **Process level:** ML for LPBF defect control is established in research.
- **Component level:** generative and topology design is mainly CAD tooling (patents).
- **Least evidence:** ML for composites, lubricants and elastomers in robots, which remains academic.

### Cited Findings
- **ML for LPBF additive manufacturing [PEER]:**
  - Wang et al., Materials Science & Engineering R 167:101112 (2025-09-11), a review of in-situ monitoring plus ML for powder-bed-fusion defects ([preprints.org](https://www.preprints.org/manuscript/202512.0586))
  - an ML framework for in-situ alloyed Ti-45Nb LPBF found porosity governed by hatch spacing and laser power, and unmelted Nb by power and scan speed ([UVic](https://dspace.library.uvic.ca/items/189ed91b-b50f-48cb-9b64-69049f3a03e6))
  - Chen et al. critical review of multisensor and ML in-situ monitoring ([paperswithcode](https://cs.paperswithcode.com/paper/in-situ-process-monitoring-and-adaptive))
- **Generative design [patent]:** level-set topology optimization, lattice+skin, build-material-strength and fatigue-damage-aware generative design patents (assignee not shown in snippet) — [USPTO 12223238](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12223238); [USPTO 11321508](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11321508)
- **Lattice robots [PEER]:** EPFL generalized lattice blending; printed legs carried more than 3 times self-weight and walked at 7.5 mm/s — [PMC12266121](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12266121/)
- **ML Mg alloy design [PEER]:** see Q1 (344 MPa / 21.3%; 395 MPa / 17.9%); a 2020 iterative surrogate-model Mg cast alloy precedent — [Springer MMTA](https://link.springer.com/content/pdf/10.1007/s11661-020-06132-1.pdf)
- **KAIST materials AI [press]:** "AI, the new language of materials science" — [AlphaGalileo](https://www.alphagalileo.org/en-gb/Item-Display/ItemId/264608)

### Inferences
Summary matrix of AI maturity by material class (my synthesis from cited findings):

| Material class | AI application type | Maturity (Nov 2026) | Best example |
|---|---|---|---|
| Magnets | Generative composition screening | Lab-validated, company claim | MagNex (2024) |
| Battery electrolytes and cathodes | HPC+AI screening; autonomous labs | Lab / pilot | MS–PNNL N2116; KAIST–POSCO |
| Light alloys (Mg/Al) | Surrogate and interpretable ML design | Peer-reviewed lab alloys | MZAX2000 |
| AM metals | In-situ monitoring + ML process control | Research to early industrial | Ti-45Nb LPBF |
| Structural links | Generative topology and lattice | Commercial CAD tools | Generative design patents; XPeng IRON lattices (claim) |
| Lubricants and tribology | Ensemble, ANN and PINN surrogates | Academic | Amide grease model |
| Plastics, composites, elastomers, skins | — | No robot-specific evidence found | — |

### Gaps
- Cables and harnesses (flex-life conductors, TPE jackets), structural adhesives and coatings were not researched within budget.
- No public example was found of an OEM (Tesla, Figure, Unitree, Hyundai) stating that it uses ML-designed materials in production.

---

## 접근 상태 로그

All WebSearch queries (about 30) succeeded through the search tool. Every WebFetch failed with `getaddrinfo ENOTFOUND`, which the tool attributes to the host being outside the session's allowed network domains (DNS/proxy refusal), not a paywall or a bot block. The agent proxy status endpoint (`$HTTPS_PROXY/__agentproxy/status`) responded normally. It listed one unrelated recent relay failure, www.kaist.ac.kr:443 tunnel closed (code 1006), which was not from this researcher.

| Host | Tool | Result | What I was trying to get |
|---|---|---|---|
| (search engine via WebSearch) | WebSearch | Success (about 30 queries) | All findings above (snippets and summaries) |
| roboticsresear.ch | WebFetch | Error: DNS ENOTFOUND (not in allowed domains) | IDTechEx-hosted "Emerging materials opportunities in humanoid market" article |
| humanoid.guide | WebFetch | Error: DNS ENOTFOUND (not in allowed domains) | Rare-earth magnets in humanoid joints (kg/robot, Dy/Tb) |
| www.idtechex.com | WebFetch | Error: DNS ENOTFOUND (not in allowed domains) | "Materials for Humanoid Robots 2026–2036" report page (TOC, forecasts) |
| roboticsandautomationnews.com | WebFetch | Error: DNS ENOTFOUND (not in allowed domains) | IDTechEx actuator-materials article (2026-07-30) |
| xenospectrum.com | WebFetch | Error: DNS ENOTFOUND (not in allowed domains) | Humanoid BOM / actuator cost breakdown |
| (localhost proxy) $HTTPS_PROXY/__agentproxy/status | Bash curl | Success | Proxy diagnostics |

Hosts NOT tried directly (only seen as search results): morganstanley.com, goldmansachs.com, figure.ai, adamasintel.com, epc-co.com, csis.org, hankyung.com, asiae.co.kr, 36kr.com, nikkei.com. After 5 consecutive DNS refusals, and following the tool's instruction to stop trying more sites, I made no further fetch attempts. To read the primary reports in full, these hosts would need to be allowed in the session's network settings: idtechex.com, roboticsresear.ch, humanoid.guide, morganstanley.com, goldmansachs.com, adamasintel.com, figure.ai.
