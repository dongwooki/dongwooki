# Why AI Was Introduced into Materials Science & Engineering (MSE) — Drivers, Robotics Angle, Timeline, and Global Policy/Funding (as of Nov 2026)

> Method note (2026-11-17): All WebFetch attempts in this session failed (host not resolvable / outside session network allowlist — see final section). Findings below therefore come from search-engine result summaries/snippets of the cited pages, not full-text reads. Figures marked "conflict" or "unverified" should be checked against the primary source before final publication.

## Q1. What fundamental problems motivated AI in MSE?

### Takeaway
AI was brought into MSE to break the slow, costly, trial-and-error (Edisonian) paradigm: materials historically took ~10–20 years and up to ~$100M to go from lab to market, the compositional/chemical search space is astronomically large (≥10^60 small organic molecules alone, larger for inorganic materials), and high-throughput DFT databases (AFLOW, Materials Project, OQMD) created a data supply that ML could exploit. Governments framed the goal as "twice as fast at a fraction of the cost" (US, 2011) or "halve cycle time and cost" (China, 2016).

### Cited Findings
- **Timeline/cost problem.** US Materials Genome Initiative (MGI) white paper (June 2011) set the goal to "discover, develop, manufacture, and deploy advanced materials at least twice as fast as possible today, at a fraction of the cost." — [MGI white paper, OSTP/NSTC June 2011](https://mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf); repeated in the [2014 MGI Strategic Plan](https://www.nist.gov/document/mgi-strategicplan-2014pdf)
- Traditional materials discovery approaches "typically have long timeframes (up to 20 years on average)" (JACS perspective). — [JACS perspective, iris.polito.it copy](https://iris.polito.it/bitstream/11583/2981642/1/jacs.2c06833.pdf)
- University of Toronto's Acceleration Consortium (2023) frames the problem as reducing development from roughly **20 years and $100 million to as little as 1 year and $1 million** per material. — [U of T News / Faculty of Engineering, Apr 2023](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/)
- A 2025 review of autonomous materials synthesis labs: "traditional materials development pipelines typically require 10–20 years," and SDLs/Materials Acceleration Platforms "aim to reduce this to 1–2 years" (aspirational, abstract-level claim). — [ICML 2025 listing](https://icml.cc/virtual/2025/50694)
- Korea's MSIT (과기정통부) 2026 strategy explicitly cites that conventional materials research, relying on "researcher experience and repeated experiments," takes **10–20+ years from new material development to commercialization** (기존 소재 연구는 연구자의 경험과 반복 실험에 의존…10~20년 이상). — [다음/뉴스 보도 2026-04-30](https://v.daum.net/v/20260430155346042); [헤럴드경제 2026-04-29](https://www.heraldk.com/article/2026042918221956653)
- **Search-space problem.** Estimates of stable small organic molecules exceed **10^60** (Bohacek et al., 1996, ≤30 heavy atoms); more conservative estimates give ~10^33 drug-like molecules; a JACS perspective gives a range of 10^23–10^60 hypothetical molecules; adding inorganic elements expands the space further. — [arXiv review "ML, QM and chemical compound space"](https://arxiv.org/pdf/1510.07512); [JACS perspective](https://iris.polito.it/bitstream/11583/2981642/1/jacs.2c06833.pdf)
- Example of scale handled by AI+robot: USTC's robotic AI chemist searched **>3.7 million candidate formulae** for an oxygen-evolution catalyst from Martian-meteorite elements and produced a catalyst in **six weeks** (Nature Synthesis, Nov 2023). — [CAS English news, 2023-11-15](https://english.cas.cn/newsroom/cas_media/202311/t20231115_643207.shtml); [SCMP](https://www.scmp.com/news/china/science/article/3195880/chinese-made-robot-pushing-boundaries-chemical-and-clean-energy)
- **Data supply from high-throughput computation.** The AFLOWLIB paper (received Nov 2011) described an alloy thermodynamics compilation of **>150,000 entries**; the AFLOW repository later grew to **>1.7 million entries** (AFLOW Fleet paper, 2017). — [AFLOWLIB paper (BYU)](https://bsg.byu.edu/docs/papers/aflowlib.pdf); [AFLOW Fleet, arXiv 1712.00422](https://ar5iv.labs.arxiv.org/html/1712.00422)
- MRS Bulletin (2018) groups Materials Project, AFLOW and OQMD as the major DFT databases enabling "data-intensive scientific discovery." — [MRS Bulletin 2018](https://link.springer.com/article/10.1557/mrs.2018.205)
- Data-quality caveat: Hegde et al. (2020/2023) found that differences between any two HT-DFT databases are often comparable to the DFT–experiment gap — a motivation for experimental (robotic) data generation. — [arXiv 2007.01988](https://arxiv.org/abs/2007.01988v2); [Phys. Rev. Materials 7, 053805](https://link.aps.org/accepted/10.1103/PhysRevMaterials.7.053805)
- **Scale of AI-generated candidates (2023).** Google DeepMind's GNoME produced **2.2 million** predicted crystal structures, **~380,000** predicted stable and added to Materials Project (Nature, 2023-11-29); only **736** had been independently synthesized at the time. — [Berkeley Lab News, 2023-11-29](https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/)
- **China's framing.** MOST's 2016 National Key R&D Program special project "Materials Genome Engineering key technologies and support platforms" aimed to integrate high-throughput computation, high-throughput experiments and databases so new materials are developed via theory-led prediction instead of trial-and-error, targeting to **halve R&D cycle time and cost**. — [Engineering (CAE journal)](https://www.engineering.org.cn/en/article/28200/detail); [CAST journal 科技导报](https://castjournals.cast.org.cn/joweb/kjdb/CN/PDF/1242134819853906283)

### Inferences
- The consistent quantitative framing across US (2011), China (2016), Canada (2023) and Korea (2026) is "10–20 years → 2x faster / halve / 1–2 years," i.e., the timeline problem is the canonical policy justification.
- Computational databases created a "prediction surplus" (millions of candidates; GNoME 2.2M vs 736 synthesized) — a gap that is the direct rationale for robotic/autonomous experimentation.

### Gaps
- No primary-source quantification found for high-dimensional process–structure–property (PSP) complexity or for labor/reproducibility costs in MSE specifically (e.g., % irreproducible experiments).
- Original Materials Project (2011) and OQMD (2013) launch-year compound counts not retrieved.
- A widely quoted "10x faster discovery" target from a government agency was not located in this session; the BIG-MAP "≥5x discovery rate" (Q4) and SDL median acceleration factor ~6 (Q2) are the closest quantified claims.

## Q2. Why combine AI with robotics in materials research? Why did materials for robots need AI-driven design?

### Takeaway
Robotics closes the loop: ML proposes, robots synthesize/characterize, results update the model — enabling 24/7 operation, reproducible standardized data, safe handling of hazardous chemicals, and sample-efficient exploration. Benchmarks show a median ~6x acceleration over reference strategies. For robot materials (soft actuators, sensors, LCEs), nonlinearity, hysteresis and large design spaces make physics-only design hard, motivating data-driven/ML design — though end-to-end SDL discovery of soft-robot materials remains thinly documented.

### Cited Findings
- **Closed-loop definition.** Abolhasani & Kumacheva (Nature Synthesis, 2023) define self-driving labs (SDLs) as systems combining machine learning, lab automation and robotics. — [NSF PAR copy](https://par.nsf.gov/servlets/purl/10421607); [NCSU news](https://cbe.ncsu.edu/?p=24420)
- **Quantified acceleration.** "Benchmarking Self-Driving Labs" (Adesiji, Wang, Kuo, Brown; Boston Univ.; arXiv Aug 2025 → Digital Discovery 2026) surveys the literature: reported **acceleration factors (AF) have a median of 6**, rising with dimensionality of the parameter space; enhancement factors vary by >2 orders of magnitude, peaking at 10–20 experiments per dimension. — [arXiv 2508.06642](https://arxiv.org/pdf/2508.06642); [Digital Discovery 2026](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00337g)
- **24/7 throughput.** Liverpool's mobile robotic chemist (Burger et al., Nature, July 2020) ran **688 experiments over 8 days** autonomously, working continuously. Follow-up (Nature, 2024): two mobile robots + AI performed exploratory synthesis, making decisions comparable to humans "in seconds" versus hours. — [Univ. of Liverpool news](https://news.liverpool.ac.uk/?p=123346); [Electronic Specifier](https://electronicspecifier.com/industries/robotics/ai-robots-carry-out-chemical-synthesis-research)
- Berkeley Lab's A-Lab (Nature, 2023-11-29) synthesized **41 of 58** targeted novel inorganic compounds (71%) in **17 days** of autonomous operation (>2 new materials/day). Caveat: some scientists called for retraction, arguing phase identification was unreliable. — [Berkeley Lab News](https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/); [Freethink](https://www.freethink.com/robots-ai/google-ai-discovers-2-2-million-new-materials)
- **Safety.** Abolhasani-group account: SDLs increase safety by handling hazardous materials with minimal human exposure; photochemistry SDL chapter: automation enhances reproducibility and safety and systems can operate continuously. A chemRxiv preprint (not peer reviewed) warns safety must be brought "to the forefront" of SDL research. — [NCSU](https://cbe.ncsu.edu/?p=24420); [UvA chapter](https://pure.uva.nl/ws/files/225440366/Chapter_1.pdf); [chemRxiv "Steering towards safe SDLs"](https://chemrxiv.org/engage/chemrxiv/article-details/6764449b6dde43c908a1d8c6)
- **Reproducibility/data quality.** A review argues standardization of process specification and execution is crucial for interoperability and reproducibility as experiments become automated; Volk & Abolhasani (Nature Communications, 2024) proposed a definition and **seven performance metrics** for SDLs. — [NSF PAR](https://par.nsf.gov/servlets/purl/10562425); [Lab Manager](https://www.labmanager.com/do-ai-driven-chemistry-labs-actually-work-new-metrics-promise-answers-31810)
- US MGI 2021 and 2024 documents call for autonomous systems generating "high-quality, reproducible data in a scalable and shareable format." — [IFP "Scaling Materials Discovery with SDLs"](https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf) (snippet only; fetch blocked)
- **LLM agents (2023→).** Coscientist (Boiko, MacKnight, Kline, Gomes; Nature 624, 2023-12-20), GPT-4-driven, autonomously planned syntheses, read hardware docs, controlled liquid handlers and optimized Suzuki/Sonogashira couplings; it was developed in parallel with ChemCrow. — [PMC10733136](https://pmc.ncbi.nlm.nih.gov/articles/PMC10733136); [EurekAlert](https://www.eurekalert.org/news-releases/1011392)
- **Toward "SDL 2.0."** A Materials Horizons 2026 review argues first-generation SDLs ("SDL 1.0") remain limited in scope and calls for flexible, interoperable platforms. — [Materials Horizons 2026 (UNIST repository)](https://scholarworks.unist.ac.kr/bitstream/201301/91305/2/d5mh01984b.pdf)
- **Materials for robots — why ML.** PLoS ONE review (2021) organizes ML in soft robotics around soft sensors and soft actuators; soft-body **nonlinearity and hysteresis** make modeling/control hard, motivating ML. — [PMC7891779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7891779/)
- Frontiers in Electronic Materials mini-review (Nov 2022): ML for strain-sensor-integrated soft robots covers **sensor materials optimization**, signal analysis, in-sensor computing. — [Frontiers](https://frontiersin.org/journals/electronic-materials/articles/10.3389/femat.2022.1000781/full)
- Smart Materials & Structures review (2025): FEA + ML + digital twins for data-driven design, shape exploration, 4D-printed soft robots and metamaterials. — [NTU repository](https://irep.ntu.ac.uk/id/eprint/53045/1/2367043_Bodaghi.pdf)
- Example inverse design: FEM simulations generated training data for ML that maps task requirements back to soft-actuator designs. — [UGA OpenScholar](https://openscholar.uga.edu/record/3095)
- Experimental optimization of liquid-crystal-elastomer (LCE) robots: Bayesian optimization of light fields for LCE microrobot gaits (arXiv 2018); evolutionary algorithms identified fastest LCE swimmers among **345,600** parameter combinations (arXiv 2025). — [arXiv 1809.03225](https://arxiv.org/pdf/1809.03225); [arXiv 2503.00204](https://arxiv.org/pdf/2503.00204v3)
- Soft-matter SDL example: Notre Dame SDL using robotic fluid handling, online sensors and BO to hit target LCST of thermoresponsive polymers (arXiv Sept 2025); 2026 preprint reviews BO/active learning/RL for self-driving soft-matter labs. — [arXiv 2509.05351](https://arxiv.org/html/2509.05351v1); [arXiv 2601.17920](https://arxiv.org/pdf/2601.17920)
- Japan's Moonshot Goal 3 (Cabinet Office) explicitly targets, by 2050, "AI robots that autonomously think and act in natural science to discover impactful scientific principles and solutions"; U. Tokyo project (PM Kanako Harada) 2030 milestone: AI-robots autonomously perform experiments that human scientists alone could not. — [Cabinet Office Moonshot Goal 3](https://www8.cao.go.jp/cstp/english/moonshot/sub3_en.html); [JST Harada project](https://www.jst.go.jp/moonshot/en/program/goal3/33_harada.html)

### Inferences
- The robotics rationale is two-directional: (1) robots as *tools* for materials discovery (SDLs) and (2) robots as *consumers* of new materials (soft actuators, sensors), where the design space is too nonlinear for intuition. Policy attention (Genesis Mission, Korea 자율실험실, Canada AC) is overwhelmingly on (1); (2) is mostly academic.
- The A-Lab dispute and SDL safety preprints indicate that "autonomy" claims carry characterization/safety risks — relevant counterpoint for a balanced report.

### Gaps
- No source found documenting a full closed-loop SDL that synthesizes *new* soft-robot materials (e.g., new LCE chemistries) end-to-end; only parameter-optimization studies.
- No quantitative data found on labor cost savings of SDLs.
- ChemCrow details and materials-specific LLM agents (e.g., 2024–2026 agentic systems) not retrieved in this session.

## Q3. Timeline of key milestones

### Takeaway
The progression runs: high-throughput DFT databases (c. 2011) → US MGI (June 2011) → national copycats (Japan MI2I 2015, China MGE 2016, UK Royce 2015) → ML + first robotic chemists (2020) → EU MAPs (BIG-MAP 2020) → MGI Strategic Plan 2021 → Canada AC $200M (2023) → GNoME/A-Lab/Coscientist (late 2023) → policy wave of AI-for-science + autonomous labs (EU 2024, China AI+ 2025, US Genesis Mission Nov 2025, Korea K-Moonshot & AI 소재 strategy 2026).

### Cited Findings
- **2011-06-24** — President Obama announces Materials Genome Initiative ("twice as fast, fraction of the cost"). — [Obama White House archive](https://obamawhitehouse.archives.gov/node/164866); [MGI white paper](https://mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf)
- **2011 (Nov)** — AFLOWLIB paper (>150,000 entries). — [AFLOWLIB](https://bsg.byu.edu/docs/papers/aflowlib.pdf)
- **2012** — NSF DMREF first competition: just over **$12M**, 22 grants, 14 projects. — [Nanowerk, 2012-10-12](https://nanowerk.com/news2/newsid=26961.php)
- **2014** — MGI Strategic Plan (Dec 2014); CAS & CAE submit "Strategic Consultation Report on Materials Genome" to China's State Council. — [NIST](https://www.nist.gov/document/mgi-strategicplan-2014pdf); [Engineering](https://www.engineering.org.cn/en/article/28200/detail)
- **2015** — UK Henry Royce Institute formed with **£235M** government investment via EPSRC. — [UKRI](https://www.ukri.org/who-we-are/epsrc/centres-and-institutes/henry-royce-institute/)
- **2015-07-01** — Japan MI2I (Materials research by Information Integration Initiative) begins at NIMS under JST "Support program for starting up innovation hub"; ended **March 2020**, forming the materials informatics community. — [NIMS press 2015-09](https://archive.nims.go.jp/eng/news/press/2015/09/201509020.html); [NIMS MI2I](https://www.nims.go.jp/MII-I/en/index.html)
- **2016** — China MOST National Key R&D Program "Materials Genome Engineering" special project (e.g., grant 2016YFB0700503). — [Engineering](https://www.engineering.org.cn/en/article/28200/detail); [Chin. Phys. B](https://cpb.iphy.ac.cn/article/2018/1962\\cpb_27_11_118101.html)
- **2016 (Aug)** — MGI five-year accomplishments report; >$250M federal investment since 2011 (per White House). — [NIST MGI at 5 years](https://www.nist.gov/system/files/documents/2018/06/26/mgi-accomplishments-at-5-years-august-2016.pdf)
- **2019 (Aug)** — Korea's post-Japan-export-control 소재·부품·장비 R&D strategy: **≥5조 원** (2020–2022) for core items, diagnosis of ~100 items. — [뉴시스 2019-08-27](https://www.newsis.com/view/NISX20190827_0000752621)
- **2020 (Jul)** — Liverpool mobile robotic chemist (688 experiments/8 days, Nature). — [Liverpool](https://news.liverpool.ac.uk/?p=123346)
- **2020-09-01** — EU BIG-MAP starts (Horizon 2020 GA 957189; to 2024-02-29). — [Fraunhofer ISC](https://isc.fraunhofer.de/en/press-and-media/press-releases/EU-project-BIG-MAP-development-of-the-next-generation-of-super-batteries.html)
- **2021** — USTC first robotic chemist "Xiao Lai"; **MGI 2021 Strategic Plan** (3 goals: unify the Materials Innovation Infrastructure; harness the power of materials data; educate/train/connect the workforce); NSF **$65.3M** for 37 DMREF awards at MGI's 10th anniversary. — [USTC](https://en.ustc.edu.cn/info/1007/4956.htm); [ACerS](https://ceramics.org/ceramic-tech-today/materials-genome-initiative-updates-strategic-plan/); [NSF](https://www.nsf.gov/news/nsf-invests-designing-materials-future)
- **2023 (Apr)** — Canada CFREF **C$200M** to U of T Acceleration Consortium. **2023** — NSF **$72.5M** for 37 DMREF projects (161 researchers, 61 universities). — [U of T](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/); [NSF](https://www.nsf.gov/news/nsf-invests-72m-design-revolutionary-materials)
- **2023-11-29** — GNoME (2.2M structures) and A-Lab (41/58 in 17 days) in Nature. **2023-12-20** — Coscientist in Nature. **Nov 2023** — USTC robotic AI chemist Mars catalyst (Nature Synthesis). — [LBNL](https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10733136); [CAS](https://english.cas.cn/newsroom/cas_media/202311/t20231115_643207.shtml)
- **2024-02-27** — EU Communication COM(2024)98 "Advanced Materials for Industrial Leadership" (Materials Commons; AI-supported). — [EC R&I](https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/key-enabling-technologies/chemicals-and-advanced-materials/advanced-materials-industrial-leadership_en)
- **2024** — MGI Challenges; DOE RFI on Autonomous Experimentation platforms. — [ACerS/MGI coverage](https://ceramics.org/ceramic-tech-today/materials-genome-initiative-updates-strategic-plan/); [mgi.gov](https://mgi.gov/)
- **2024-07-22** — Korea MOTIE "AI 자율제조 얼라이언스" launched (153 firms/institutions, 12 sectors). **2024-10** — MOTIE "AI+R&DI 추진전략." — [뉴시스](https://www.newsis.com/view/NISX20240722_0002819949); [뉴데일리](https://biz.newdaily.co.kr/site/data/html/2024/10/17/2024101700207.html)
- **2025-08** — China State Council "AI+" Opinions (Guofa [2025] No.11): AI-driven research paradigms, scientific large models. — [Geopolitechs](https://www.geopolitechs.org/p/china-releases-ai-plus-policy-a-brief)
- **2025-11-24** — US EO 14363 "Launching the Genesis Mission" (FR 2025-11-28). — [Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21665.htm); [MoFo](https://www.mofo.com/resources/insights/251211-executive-order-establishes-genesis-mission)
- **2026-02-25** — Korea K-문샷 추진전략. **2026-04-30** — MSIT "AI 소재 R&D 플랫폼 구축 전략(2026~2030)". **2026-07-22** — Genesis Mission >$5B commitments. **2026-08** — Korea national autonomous lab consortium. **2026-09-30** — K-문샷 roadmap approved. — see Q4 sources.

### Inferences
- The dominant pattern is US-led agenda setting followed within 1–5 years by national equivalents; the 2025–2026 wave (Genesis Mission → K-Moonshot explicitly framed as a response) repeats the 2011 MGI → copycat pattern, now centered on autonomous labs rather than databases.

### Gaps
- Materials Project and OQMD founding dates/sizes, and DARPA materials-AI programs (e.g., Accelerated Molecular Discovery) were not retrieved.

## Q4. Government programs and funding by region

### Takeaway
Funding has shifted from data/computation infrastructure (MGI, MI2I, MGE) to autonomous-lab + AI-model infrastructure. Headline numbers: US Genesis Mission (EO Nov 2025; ~$293M DOE FOA Mar 2026; >$5B commitments Jul 2026), Canada C$200M CFREF (2023, largest ever to a Canadian university), UK £235M Royce + up to £137M AI for Science Strategy, EU BIG-MAP €16M (≥5x discovery rate goal) and a €500M advanced-materials partnership (2025–27), China MGE (halve cycle/cost) + AI+ (2025) + Beijing autonomous-lab plan (2026–28), Japan MI2I/Moonshot Goal 3, Korea AI 소재 전략 (10M→50M datasets, 24h 자율실험센터).

### Cited Findings
**United States**
- MGI 2011; >$250M federal R&D/infrastructure investment since 2011 (as of 2016). — [NIST MGI at 5](https://www.nist.gov/system/files/documents/2018/06/26/mgi-accomplishments-at-5-years-august-2016.pdf); [Obama WH archive](https://obamawhitehouse.archives.gov/node/164866)
- NSF DMREF: $12M (2012), $65.3M/37 awards (2021), $72.5M/37 projects (2023). Cumulative total not found. — [Nanowerk](https://nanowerk.com/news2/newsid=26961.php); [NSF 2021](https://www.nsf.gov/news/nsf-invests-designing-materials-future); [NSF 2023](https://www.nsf.gov/news/nsf-invests-72m-design-revolutionary-materials)
- MGI 2021 Strategic Plan three goals (infrastructure, data, workforce); autonomous experimentation sits under the infrastructure goal. — [ACerS](https://ceramics.org/ceramic-tech-today/materials-genome-initiative-updates-strategic-plan/); [NCCR MARVEL](https://nccr-marvel.ch/news/communication/MGI-US-strategy)
- **Genesis Mission (EO 14363, signed 2025-11-24)**: DOE leads; builds an integrated AI platform ("American Science and Security Platform"); priority domains include **critical materials**, advanced manufacturing, biotech, fission/fusion, QIS, semiconductors; within **240 days** DOE must review national-lab capabilities for **robotic laboratories and AI-directed experimentation**; 90-day computing inventory; 120-day initial data corpus. One analysis: EO redirects existing investments rather than net-new money. — [MoFo, 2025-12-11](https://www.mofo.com/resources/insights/251211-executive-order-establishes-genesis-mission); [FedScoop](https://fedscoop.com/trump-ai-executive-order-genesis-mission-platform/); [Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21665.htm)
- Mar 2026: DOE funding opportunity **~$293M** (autonomous labs one challenge area; Phase I due 2026-04-28) — **conflict**: another analysis cites $320M. — [HPCwire 2026-03-18](https://www.hpcwire.com/2026/03/18/doe-announces-293m-funding-opportunity-as-genesis-mission-moves-toward-operational-phase/); [MeriTalk](https://meritalk.com/articles/doe-announces-293m-in-ai-research-funding-under-genesis-mission/); [GrantedAI ($320M)](https://grantedai.com/blog/doe-genesis-mission-293-million-ai-scientific-discovery-funding-strategy-2026)
- 2026-07-22: White House announced **>$5B** federal commitments; an autonomous-labs track where DOE, HHS, NSF, NIST build autonomous labs leveraging robotics, edge AI, real-time analysis; reported **278 projects**, 16 DOE/NNSA labs, 142 universities, 157 companies, 13 nonprofits (secondary sources). Berkeley Lab to lead 13 projects; CMU 3 projects incl. linking autonomous labs at Argonne & LLNL (2026-08-03). — [AI Weekly](https://aiweekly.co/alerts/trump-unveils-5b-genesis-mission-doe-picks-278-ai-projects); [CMU RI](https://www.ri.cmu.edu/connecting-autonomous-laboratories-to-speed-scientific-advancement/); [MIT Climate](https://climate.mit.edu/posts/mit-projects-selected-funding-under-us-department-energys-genesis-mission)

**Canada**
- Acceleration Consortium (U of T): **C$200M CFREF** (Apr 2023), largest federal research grant to a Canadian university; U of T adds **C$130M** for facilities; six SDLs; goal 20 yrs/$100M → 1 yr/$1M. — [U of T Engineering News](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/); [U of T CS](https://web.cs.toronto.edu/news-events/news/u-of-t-receives-200-million-grant-to-support-acceleration-consortiums-self-driving-labs-research)

**European Union**
- BIG-MAP (Battery Interface Genome – Materials Acceleration Platform), Horizon 2020 GA 957189, 2020-09-01 to 2024-02-29, largest of seven BATTERY 2030+ projects, 34 partners/15 countries, ambition to **increase discovery rate ≥5x**. Budget **€16M** (EurekAlert, Fraunhofer) — **conflict**: CIDETEC lists €20M. — [Fraunhofer ISC](https://isc.fraunhofer.de/en/press-and-media/press-releases/EU-project-BIG-MAP-development-of-the-next-generation-of-super-batteries.html); [EurekAlert](https://www.eurekalert.org/news-releases/478904); [CIDETEC](https://energystorage.cidetec.es/proyectos/big-map); [Battery 2030+](https://battery2030.eu/news/activities/big-map-the-battery-interface-genome-‐-materials-acceleration-platform-is-the-largest-of-the-seven-battery-2030-projects/)
- COM(2024)98 (2024-02-27): "Materials Commons" FAIR digital infrastructure (to be developed by mid-2025) with AI tools for design/testing; new Horizon Europe partnership targeting **€500M (2025–2027), ≥€250M private**; Advanced Materials Academy with EIT; Technology Council C(2024)4749. — [EC R&I](https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/key-enabling-technologies/chemicals-and-advanced-materials/advanced-materials-industrial-leadership_en); [EU Monitor](https://eumonitor.eu/9353000/1/j4nvirkkkr58fyw_j9vvik7m1c3gyxp/vmb4htis8sxx)

**United Kingdom**
- Henry Royce Institute: **£235M** via EPSRC (2015); Phase II EPSRC funding confirmed (amount not found); Digital Materials Foundry (May 2025); UK **AI for Science Strategy** directs **up to £137M**, names Royce for materials-data curation for AI; £50M National Materials Innovation Programme; Royce CEO (Aug 2026) argues for a federated **UK National Autonomous Laboratory**. UK also launched early market engagement for autonomous-lab projects. — [UKRI](https://www.ukri.org/who-we-are/epsrc/centres-and-institutes/henry-royce-institute/); [GOV.UK AI for Science Strategy](https://www.gov.uk/government/publications/ai-for-science-strategy/ai-for-science-strategy); [Royce](https://www.royce.ac.uk/?p=18280); [Sheffield](https://sheffield.ac.uk/royce-institute/news/ai-science-strategy); [Scientific Computing World](https://www.scientific-computing.com/article/uk-launches-early-market-engagement-ambitious-autonomous-lab-projects)
- Liverpool Materials Innovation Factory: mobile robotic chemist (2020), multi-robot synthesis (2024), spin-out Gearu (2020). MIF capital cost (often quoted £68M) **unverified** in this session. — [Liverpool](https://news.liverpool.ac.uk/?p=123346); [Liverpool spin-outs](https://liverpool.ac.uk/collaborate/enterprise/spin-out-companies/gearu)

**China**
- MGE National Key R&D special project (2016): four technical areas (high-throughput computation; high-throughput preparation & characterization; in-service evaluation; materials big data) + demos in energy, biomedical, rare-earth functional, catalytic, special-alloy materials; goal to halve R&D cycle and cost. — [Engineering](https://www.engineering.org.cn/en/article/28200/detail)
- USTC robotic AI chemists: "Xiao Lai" (2021), "Xiao Lin" (2nd gen), "Luke" (2024); Mars-catalyst study (Nature Synthesis, Nov 2023). — [CAS 2025-11](https://english.cas.cn/newsroom/mutimedia_news/202511/t20251128_1134257.shtml); [CAS 2023-11](https://english.cas.cn/newsroom/cas_media/202311/t20231115_643207.shtml)
- State Council "AI+" Opinions (Guofa [2025] No.11, Aug 2025): explore AI-driven research paradigms for "0 to 1" discoveries; scientific large models; intelligent upgrading of research platforms; shared scientific datasets. — [Geopolitechs](https://www.geopolitechs.org/p/china-releases-ai-plus-policy-a-brief); [SESEC](https://sesec.eu/?p=683)
- Beijing Implementation Plan for AI-Empowered Scientific Research (2026–2028; interpreted Jul 2026): five dimensions led by **autonomous laboratory systems**; "dry-lab and wet-lab loop." — [Beijing gov](https://english.beijing.gov.cn/investinginbeijing/InvestmentSpecial/DigitalEconomy/PolicesAndInterpretations/202607/t20260715_4763931.html)

**Japan**
- MI2I at NIMS (JST, 2015-07 to 2020-03), explicitly inspired by US MGI. — [NIMS](https://archive.nims.go.jp/eng/news/press/2015/09/201509020.html)
- Moonshot Goal 3: by 2050 AI robots that autonomously discover scientific principles; U. Tokyo AI-robot scientist project (2030 milestone); new Goal 3 PD Kuniyoshi Yasuo from 2025-12-01. — [Cabinet Office](https://www8.cao.go.jp/cstp/english/moonshot/sub3_en.html); [JST Goal 3](https://www.jst.go.jp/moonshot/en/program/goal3/)

**South Korea (대한민국)**
- 2019-08: 소재·부품·장비 R&D 투자전략 및 혁신대책 — ≥5조 원 (2020–2022), ~100 items diagnosed, triggered by Japan's export controls. — [뉴시스](https://www.newsis.com/view/NISX20190827_0000752621)
- MOTIE 소재 AI 선도사업: 4 materials sectors (화학·금속·세라믹·섬유), **12 AI flagship projects**, **397만 건** standardized data via 소재데이터 생성전용시설(MDF); **8 industrial-materials AI models** released (2022-06). — [smartcity.go.kr 재게시 산업부 보도](https://smartcity.go.kr/2022/06/28/산업부-산업소재-디지털화를-통한-제조분야-인공지/)
- 2024-07-22 MOTIE AI 자율제조 얼라이언스 (153 firms/institutions, 12 sectors, ~2.5조 원 민·관 투자 기대); 2024-10 MOTIE "AI+R&DI 추진전략" (AI+R&D 트랙 신설, 2032년까지 신규예산 100% 적용, 산업데이터 플랫폼); a MOTIE document cites a plan to phase in **500 AI 자율실험실 by 2030**. — [뉴시스](https://www.newsis.com/view/NISX20240722_0002819949); [뉴데일리](https://biz.newdaily.co.kr/site/data/html/2024/10/17/2024101700207.html)
- 2025-04: MOTIE·MSIT open ~**300만 건** materials public data via 데이터안심구역; 소재 거점(HUB) 전문가 기술교류회 (2025-04-10). — [서울시립대 연구처 공지 재게시](https://research.uos.ac.kr/node/8668)
- 2026-02-25: **K-문샷 추진전략** ("AI시대 과학기술 경쟁력 대도약") approved by 국가AI전략위원회; 8 fields/12 national missions incl. **소재, 피지컬 AI, AI 과학자**; framed in media as a counter to the US Genesis Mission ("美 제니시스 미션 맞선 K-문샷"); roadmap approved at 제13회 과학기술관계장관회의 2026-09-30 (1st target period to 2029, 2035 goals). — [K-문샷 안건 PDF](https://smartcity.go.kr/wp-content/uploads/2026/03/안건4AI시대과학기술경쟁력대도약을위한K-문샷추진전략안.pdf); [뉴시스 2026-02-25](https://www.newsis.com/view/NISX20260225_0003525436); [머니투데이 2026-09-30](https://www.mt.co.kr/tech/2026/09/30/2026093015522912240)
- 2026-04-30: MSIT **"AI 소재 R&D 플랫폼 구축 전략(2026∼2030)(안)"** at 제8회 과학기술관계장관회의 — 물성/소재 AI 특화모델 (supply-chain advanced materials, national strategic technologies: 반도체·이차전지·우주항공); 기존 '소재연구데이터생태계플랫폼' → '국가소재연구데이터통합플랫폼(가칭)'; AI-ready datasets **1,000만 건 in 5 yrs, 5,000만 건 in 10 yrs**; 통합센터 지정 2026 H2; field-specific **'AI소재 전용 자율실험센터'** running synthesis→prototype **24h automated**; "AI소재 연구동료" linking data/model/lab; talent goal **석사 300명·박사 75명+**. — [다음 2026-04-30 (a)](https://v.daum.net/v/20260430101533808); [다음 2026-04-30 (b)](https://v.daum.net/v/20260430155346042); [헤럴드경제](https://www.heraldk.com/article/2026042918221956653)
- 2026-08: Korea's first national **자율실험실 산·학·연 협의체** launched; chair 정유성 (서울대), co-secretariat KBSI & 국가과학AI연구센터; positioned as core base for K-문샷. — [아시아경제 2026-08-11](https://view.asiae.co.kr/article/2026081109490769317)
- MOTIE (산업통상부) "첨단소재 특화형 AX플랫폼" 사업 (2026–2028): government R&D ≤ **145.5억 원**. — [motir.go.kr 공고 첨부](https://www.motir.go.kr/attach/down/aa4abe331409819421ff269b271f06a6/2d0da881271c3984f723ad8ceb5ba24c/debc2e19d8870bf491bf5e73464259e8)

### Inferences
- Korea's trajectory: supply-chain shock (2019 소부장) → materials data (MDF, 397만 건, 소재연구데이터플랫폼) → AI models → autonomous labs (2026), mirroring the global database→ML→SDL sequence but compressed into ~7 years and explicitly benchmarked against the US Genesis Mission.
- Across all regions, robotics/autonomous labs moved from academic demonstrations (2020–2023) to named line items in national strategies (2025–2026).

### Gaps
- Total budget for K-문샷 and for the MSIT AI 소재 strategy not found; KIST/KRICT-specific AI materials program budgets not found.
- Japan post-MI2I programs (NIMS DICE, ARIM data platform, 2021+) not retrieved.
- DARPA and DOE pre-Genesis autonomous-lab funding not retrieved; official energy.gov Genesis figures not directly verified.
- Chinese MOST AI-for-Science materials-specific budget figures not found.

## Q5. Expert/agency statements about expected acceleration

### Takeaway
Stated targets range from 2x (US MGI 2011) and 2x/halving (China MGE 2016), to ≥5x discovery rate (EU BIG-MAP 2020), to 10–20x+ ("20 years/$100M → 1 year/$1M", Acceleration Consortium 2023; "10–20 yrs → 1–2 yrs", MAP literature). Measured evidence: median SDL acceleration factor ~6x versus baseline optimizers.

### Cited Findings
- MGI: "at least twice as fast… at a fraction of the cost" (2011). — [MGI white paper](https://mgi.gov/sites/mgi/files/materials_genome_initiative-final.pdf)
- China MGE: halve R&D cycle and cost (2016). — [Engineering](https://www.engineering.org.cn/en/article/28200/detail)
- BIG-MAP: increase battery-materials discovery rate "by at least a factor 5" (2020). — [Fraunhofer ISC](https://isc.fraunhofer.de/en/press-and-media/press-releases/EU-project-BIG-MAP-development-of-the-next-generation-of-super-batteries.html)
- Acceleration Consortium: 20 yrs/$100M → 1 yr/$1M (2023). — [U of T](https://news.engineering.utoronto.ca/self-driving-labs-200-million-federal-grant-powers-ai-driven-materials-discovery-for-clean-energy-advanced-manufacturing-and-more/)
- SDL/MAP literature: 10–20 yrs → 1–2 yrs (aspirational). — [ICML 2025](https://icml.cc/virtual/2025/50694)
- Measured: median AF = 6 across SDL literature. — [arXiv 2508.06642](https://arxiv.org/pdf/2508.06642)
- Genesis Mission marketing frames a goal to "double" the productivity/impact of American science (secondary). — [GrantedAI](https://grantedai.com/blog/doe-genesis-mission-double-science-ai)
- Korea MSIT 2026: goal of shortening development time and cost (개발 기간·비용 단축); no numeric target found. — [다음](https://v.daum.net/v/20260430155346042)

### Inferences
- Policy targets are 2–20x; empirical benchmarks (~6x, per optimization campaign) support the lower-to-middle of that range and say nothing yet about full lab-to-market timelines.

### Gaps
- No primary-source agency statement of a literal "10x faster discovery" was found; Genesis Mission "double" claim only via secondary source.
- Consulting/think-tank quantifications (McKinsey, BCG, OECD, CSET) not retrieved within the tool budget.

## 접근 차단/실패 사이트

All failures below occurred on 2026-11-17 via WebFetch. Every fetch attempted returned `getaddrinfo ENOTFOUND` — i.e., the host was outside this cloud session's allowed network domains (blocked by session network policy / proxy allowlist), not a paywall or 404. Content from these URLs in the notes above comes only from search-engine snippets.

| # | URL attempted | Result / reason |
|---|---|---|
| 1 | https://v.daum.net/v/20260430101533808 (MSIT AI 소재 전략 기사) | ENOTFOUND — v.daum.net not in session network allowlist |
| 2 | https://www.govinfo.gov/content/pkg/FR-2025-11-28/html/2025-21665.htm (Genesis Mission EO text) | ENOTFOUND — www.govinfo.gov not in allowlist |
| 3 | https://newsseoul.co.kr/news/view/1065583210368100 (과기정통부 자율실험실 기사) | ENOTFOUND — newsseoul.co.kr not in allowlist |
| 4 | https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf (IFP SDL policy report) | ENOTFOUND — ifp.org not in allowlist |
| 5 | https://www.nature.com/articles/s41578-022-00466-5 (Nature Reviews Materials 2022 review) | ENOTFOUND — www.nature.com not in allowlist (would also likely be paywalled) |

Notes:
- After 5 consecutive host-resolution failures, further fetches were not attempted (per tool guidance), so primary documents (mgi.gov, energy.gov, nsf.gov, msit.go.kr, motir.go.kr, korea.kr, cordis.europa.eu, jst.go.jp, utoronto.ca) were **not directly opened**; only search summaries were used. To verify, the user would need to allow these hosts in the session network settings.
- Search-level unverifiable/conflicting items: Liverpool MIF "£68M" (not found); BIG-MAP budget €16M vs €20M; Genesis FOA $293M vs $320M; U of T coverage ambiguity on "$200M per year" vs $200M total (majority: $200M total).
