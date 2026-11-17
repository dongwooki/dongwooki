# Primary-Source Verification and Gap-Filling: Soft, Micro, Bio-hybrid and Medical Robot Materials (and AI/ML Use)

Notes compiled 2026-11-17. This file checks the key numbers in two earlier files against primary sources, then fills the gaps those files listed:
- `research_notes/로봇 소재 분류와 AI 검증/taxonomy_soft_micro.md`, called **"taxonomy notes"** below.
- `research_notes/로봇 분야 소재공학 AI 도입/robot_materials_design.md`, called **"prior notes"** below.

Both earlier files were built from search snippets only.

**Verification labels**
- **VERIFIED**: the exact number or claim was read in the primary source: the paper's abstract or full text, the publisher's article page, or the institution's own record.
- **PARTIALLY VERIFIED**: the paper exists and the main claim matches, but the specific number was read only in press coverage or a secondary review, or the primary source gives a slightly different number. The difference is stated.
- **UNVERIFIED**: the number could not be found in any primary text that was reachable.

**Evidence-type labels:** [PR] peer-reviewed; [PRE] preprint; [CONF] conference abstract or talk; [PRESS] press release or news; [SNIP] search-engine summary only, not opened. Dates are online publication dates unless stated otherwise.

**Method:** pages were fetched with `curl` through the session proxy. WebFetch was not used: it was reported broken and was not attempted. Primary text came from:
- NCBI E-utilities (PMC full-text XML);
- Europe PMC REST;
- the OpenAlex and Crossref APIs;
- nature.com article pages;
- the arXiv export API;
- NASA NTRS;
- the Aalto research portal;
- the MIT News and Tsinghua news sites.

Every host attempt is in the log at the end.

---

## Q1. Are the actuator metric anchors correct? (DE, TCP, HASEL, LCE, biogels, BO actuator, SMA ML)

### Takeaway
Results for the actuator anchors:
- **Fully verified:** the coiled-nylon numbers (49%, >100x, 5.3 kW/kg); the BO polymer-actuator result (62 of 1,089 combinations, strain 1.25); the Rumley 2023 biogel actuator numbers (200 V/µm, >100,000 cycles).
- **VHB ">380% area strain / 7.2 MPa":** partially verified. Pelrine's 2000 Science *abstract* gives 117% (silicone) and 215% (acrylic). The 380%, 7.2 MPa and 3.4 MJ/m³ figures come from a later review by co-author Qibing Pei, which credits them to Pelrine 2000.
- **Biogel cycle counts:** the ">330,000 cycles" figure belongs to Baumgartner 2020 (Nature Materials) and ">100,000 cycles" to Rumley 2023 (Science Advances). The taxonomy notes' guess was right, but the 330,000 figure is confirmed only by press coverage and summaries, not by the abstract.
- **HASEL:** the primary Peano-HASEL numbers are 10% contraction, 900%/s, 50 Hz and >200x own weight. The "Donut 50% / planar 79%" figures in the taxonomy notes remain unverified secondary numbers.
- **NASA NiTi MAE values (14.8 °C, 7.2 °C, 0.36%):** UNVERIFIED. No reachable NASA document states them; the NASA abstracts say only "extremely low" or "low" MAE.
- **LCE energy density:** the verified primary range spans about **63 J/kg** (DLP-printed LCE) to **650 J/kg** (graphene-LCE fibre).

### Cited Findings

**Verification table (actuators)**

| Claim in earlier notes | Status | What the primary source says (exact) | Source |
|---|---|---|---|
| VHB DE >380% area strain, 7.2 MPa (Pelrine 2000) | **PARTIALLY VERIFIED** | Abstract (Science 287:836, 4 Feb 2000): "Actuated strains up to 117% were demonstrated with silicone elastomers, and up to 215% with acrylic elastomers using biaxially and uniaxially prestrained films." A review by co-author Q. Pei: "VHB acrylic elastomers from 3M exhibit exceptionally large area strain, exceeding 380%, and a high Maxwell stress of 7.2 MPa… VHB's 3.4 MJ/m³ theoretical energy density far exceeds the 0.07 MJ/m³ of human skeletal muscle." It cites Pelrine et al., Science 2000 as ref. 6. | [OpenAlex record, Pelrine 2000](https://api.openalex.org/works/doi:10.1126/science.287.5454.836) [PR]; [Qiu, Zhang, Plamthottam & Pei, "Dielectric elastomer artificial muscle: materials innovations and device explorations" (NSF PAR PDF)](https://par.nsf.gov/servlets/purl/10128818) [PR review] |
| Coiled nylon 49% contraction, 5.3 kW/kg (Haines 2014) | **VERIFIED** | Abstract (Science, 20 Feb 2014): coiled muscles "can contract by 49%, lift loads over 100 times heavier than can human muscle of the same length and weight, and generate 5.3 kilowatts of mechanical work per kilogram of muscle weight." The abstract also calls them "nonhysteretic, long-life". The ">30% stroke, millions of cycles" figures from a later review were not re-checked. | [doi:10.1126/science.1246906 via OpenAlex](https://api.openalex.org/works/doi:10.1126/science.1246906) [PR] |
| HASEL strains (Donut ~50%; planar 79% under 250 g) | **UNVERIFIED** (secondary only); primary Peano-HASEL numbers added | Kellaris et al., Science Robotics (5 Jan 2018): "controllable linear contraction up to 10%, a strain rate of 900% per second, actuation at 50 hertz, and the ability to lift more than 200 times their weight." Acome et al., Science (5 Jan 2018) abstract gives no numbers: "muscle-like performance" and repeated self-healing after dielectric breakdown. | [Kellaris 2018](https://api.openalex.org/works/doi:10.1126/scirobotics.aar3276) [PR]; [Acome 2018](https://api.openalex.org/works/doi:10.1126/science.aao6139) [PR] |
| LCE energy density (5.5 kJ/m³ vs 63 J/kg / 0.18 MJ/m³) | **63 J/kg and 0.18 MJ/m³ VERIFIED**; 5.5 kJ/m³ UNVERIFIED | A DLP-printed LCE (Science Advances 2021, abg3677) reports "high specific work capacity (63 J kg⁻¹) and energy density (0.18 MJ m⁻³)", "the highest specific work capacity yet reported for 3D printed LCE soft actuators." A graphene-filled LCE single-fibre actuator (Nature Nanotechnology 2022) "attains work capacity and power density of 650 J kg⁻¹ and 293 W kg⁻¹," about 17x and 6x human muscle. | [PMC8302124](https://pmc.ncbi.nlm.nih.gov/articles/PMC8302124/) [PR]; [PMC9646516](https://pmc.ncbi.nlm.nih.gov/articles/PMC9646516/) [PR] |
| Biodegradable HASEL: 200 V/µm, >100,000 cycles | **VERIFIED, attributed to Rumley et al. 2023** | Science Advances (22 Mar 2023; JKU Linz, MPI-IS, CU Boulder): actuators built from biodegradable polymer films, ester-based liquid dielectric and NaCl-infused gelatin hydrogel "reliably operate up to high electric fields of 200 V/μm, show performance comparable to nonbiodegradable counterparts, and survive more than 100,000 actuation cycles." | [doi:10.1126/sciadv.adf5551 via OpenAlex](https://api.openalex.org/works/doi:10.1126/sciadv.adf5551) [PR] |
| Gelatin biogel >330,000 cycles | **PARTIALLY VERIFIED, attributed to Baumgartner et al. 2020** | Nature Materials 19:1102–1109 (15 Jun 2020; JKU Linz, Kaltenbrunner group). The abstract (Europe PMC) gives no cycle count. ">330,000 cycles without failure" appears in press and summary coverage of this paper, for an elephant-trunk pneumatic actuator. The full text was paywalled. | [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41563-020-0699-3%22&format=json); [SYFY Wire coverage](https://www.syfy.com/index%2Ephp/syfy-wire/biodegradable-robot-made-of-food-safe-ingredients) [PRESS] |
| BO coiled polymer actuator: strain 1.25, 62 of 1,089 (Materials & Design 2025) | **VERIFIED** | Abstract: "a discrete Bayesian optimization workflow was developed. An actuation strain of 1.25 was achieved by optimizing the processing conditions, which required the fabrication of only 62 sample combinations out of 1089 possible ones." There were three processing variables: ply number, twisting stress and coiling stress. Published in Materials & Design, May 2025, article 113908, doi 10.1016/j.matdes.2025.113908 (Zhang, Vaara, Alesafar, Nguyen, Silva, Koskelo, Ristolainen, Stosiek …; Aalto). An SSRN preprint appeared in 2024. | [Aalto Research Portal](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat) [PR]; [Crossref metadata](https://api.crossref.org/works/10.1016/j.matdes.2025.113908) |
| NASA NiTi ML MAEs: 14.8 °C, 7.2 °C, 0.36% | **UNVERIFIED** | The SMST 2021 abstract (Honrao, Benafan, Lawson) says only that the models "are capable of accurately predicting the transition temperature, hysteresis, and transformation strain." The MS&T22 abstract and slides give the dataset: "over 8,000 multi-component Ni-Ti alloys containing 37 different alloying elements," with "52 composition, thermo-mechanical processing, and test parameter related inputs," "extremely low mean absolute errors," and "ML predictions are validated through new experiments." No MAE values appear in the extractable text; they may be in slide figures or in the journal paper. Journal paper: Honrao, Benafan & Lawson, *Shape Memory and Superelasticity*, 8 Dec 2022, doi 10.1007/s40830-022-00405-x (Springer returned a bot challenge). | [NTRS 20205008258](https://ntrs.nasa.gov/citations/20205008258) [CONF]; [NTRS 20220005395](https://ntrs.nasa.gov/citations/20220005395) [CONF]; [NTRS 20220014943 slides](https://ntrs.nasa.gov/citations/20220014943) [CONF] |

**DEA self-driving lab (preprint, abstract now read)**
- "A Robotic Testing Platform for Pipelined Discovery of Resilient Soft Actuators" (arXiv 2602.20963, 24 Feb 2026) [PRE]. The abstract says:
  - It scanned the lifetime of Elastosil-based linear DEAs across input voltage, frequency, electrode material concentration and electrical-connection filler.
  - "The optimal parameter combinations improved operational lifetime under boundary operating conditions by up to 100%."
  - A quadruped built with the optimized actuators carried a payload of ">100% of its untethered body weight, and >700% of combined actuator weight."
  - It claims to be "the first to introduce a self-driving lab approach into robotic actuator design."
  - Source: [arXiv API record](https://export.arxiv.org/api/query?id_list=2602.20963)
- A search summary says fabrication is still manual and automated fabrication is planned [SNIP]; that point was not seen in the abstract. — [arXiv html](https://arxiv.org/html/2602.20963)

### Inferences
- The table value "VHB >380%" is safe as an **area** strain. Pelrine's abstract headline of 215% (acrylic) is a different strain measure (a search summary calls it linear [SNIP]). The report should not mix the two.
- LCE "energy density" figures differ by orders of magnitude because units differ (J/kg vs kJ/m³ vs MJ/m³) and so do test modes (photothermal fibre vs printed film). Quote with units and source.
- The NASA MAE numbers should not appear in the report as verified figures. Use the verifiable dataset descriptors instead (>8,000 alloys, 37 elements, 52 inputs, experimental validation).

### Gaps
- The Pelrine 2000 full text (Table 1) and the Baumgartner 2020 full text were not readable (Science and Nature Materials paywalls), so 380%, 7.2 MPa and 330,000 cycles remain second-hand.
- The source of the NASA MAEs (14.8 °C / 7.2 °C / 0.36%) is unknown. It probably comes from the 2022 Shape Memory and Superelasticity paper, which was blocked.

---

## Q2. Are the sensing / e-skin anchors correct? (Nature Materials 2025 SNU e-skin, Tsinghua 3DAE-Skin, SuperTac)

### Takeaway
Results for the sensing anchors:
- **Nature Materials paper:** DOI 10.1038/s41563-025-02373-w **is** the Seung Hwan Ko (SNU) paper. Its title is "Unisensory processing of interleaving memristive nanowires enabling multimodal sensing at human-scale resolution." It went online 24 Oct 2025, in the March 2026 issue. The abstract verifies "20 household objects with 83% accuracy." The **65%→95%** and **94.53%** figures are in press coverage only.
- **Tsinghua 3DAE-Skin (Science, 30 May 2024):** the abstract is verified. The **240 sensors** and **~0.1 mm** figures come from China Daily's quotes of Zhang Yihui, not the abstract.
- **SuperTac (Nature Sensors, 15 Jan 2026):** fully verified from the publisher abstract. There is a parameter-count conflict for its DOVE language model: the paper says 8.5B, Tsinghua's Chinese release says 8.5亿 (850M).

### Cited Findings

| Claim | Status | Primary-source detail | Source |
|---|---|---|---|
| Nature Materials 2025 multimodal e-skin; 65%→95%; is it Seung Hwan Ko (SNU)? | **Identity VERIFIED; 83% VERIFIED; 65%→95% PARTIALLY VERIFIED (press only)** | Authors: Kyun Kyu Kim, Junhyuk Bang, Munju Kim, Juho Jeong, Inho Ha … Seung Hwan Ko (SNU; Stanford co-affiliation). Online 2025-10-24; issue date 2026-03. The abstract describes a single memristive nanowire network that "switches between thermal and mechanical sensing at 16 Hz." Response times are "submicrosecond (mechanical) and millisecond (thermal)." With an ML model it identified "20 household objects with 83% accuracy using a single fingertip-mounted sensor." Press: accuracy "improved from approximately 65% when the model was trained with thermal or mechanical data separately to 95% after the integration of both" modes; 94.53% with reduced input. | [nature.com article page](https://www.nature.com/articles/s41563-025-02373-w) [PR]; [OpenAlex](https://api.openalex.org/works/doi:10.1038/s41563-025-02373-w); [ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing) [PRESS] |
| Tsinghua (Zhang Yihui) Science 2024 e-skin, 240 sensors, 0.1 mm | **Paper VERIFIED; 240 / 0.1 mm PARTIALLY VERIFIED (press quotes)** | Liu Z., Hu X., Bo R., … (Tsinghua; NUS), Science, online 30 May 2024. The abstract describes the 3DAE-Skin: force and strain sensors in a 3D layout mimicking Merkel cells and Ruffini endings. It decouples normal force, shear force and strain, and enables "simultaneous modulus/curvature measurements of an object through touch" (fruit, bread, cake). The abstract does not mention deep learning. China Daily quotes Zhang: fingertip-sized, 240 sensors each about 200–300 µm, about 0.1 mm position resolution, deep-learning processing. | [OpenAlex abstract](https://api.openalex.org/works/doi:10.1126/science.adk5556) [PR]; [China Daily, 5 Jun 2024](https://govt.chinadaily.com.cn/s/202406/05/WS6673996e498ed2d7b7eb0c2c/chinese-scientists-design-bio-inspired-3d-e-skin.html) [PRESS] |
| SuperTac (Nature Sensors 2026) | **VERIFIED** (parameter-count conflict noted) | Nature Sensors, online 2026-01-15, title "Biomimetic multimodal tactile sensing enables human-like robotic perception." Inspired by pigeon multispectral vision. A "single 1-mm-thick light-field-modulated skin" combines multispectral imaging (MIR to UV), triboelectric and inertial sensing. Reported: resolution 0.00545 mm² px⁻¹; force accuracy 0.06 N; position accuracy 0.4 mm; temperature 0–90 °C; proximity <15 cm; vibration 0–60 Hz; ">94% accuracy" for texture, material, sliding, collision and colour; "DOVE, an 8.5B-parameter tactile language model." Tsinghua's release (20 Jan 2026) names Associate Prof. Ding Wenbo (Tsinghua SIGS) and gives DOVE as "8.5亿参数" (850 million). | [nature.com s44460-025-00006-y](https://www.nature.com/articles/s44460-025-00006-y) [PR]; [Tsinghua News (zh)](https://www.tsinghua.edu.cn/info/1175/123978.htm) [PRESS] |

### Inferences
- The prior notes described the Nature Materials paper as an "e-skin" with "memristive nanowire network" coverage. It is in fact **one** paper: a single-layer Ag/Cu₂O memristive nanowire receptor [SNIP for the core–shell composition]. The ML role is object classification (decoding), not material design.
- For SuperTac, cite "8.5B (paper) vs 850M (Tsinghua release)" as unresolved, or use the publisher's figure.

### Gaps
- The full texts for SNU 65%→95% and Tsinghua 240 sensors / 0.1 mm were not reachable. EurekAlert returned HTTP 403, and the Science and Nature Materials papers are paywalled.

---

## Q3. Are the design / structural / co-design anchors correct? (KAIST elastomer, Karacakol & Sitti, Sun 2024, Chem. Sci. self-healing PU, Northwestern PNAS 2023, MIT jumping robot)

### Takeaway
All six anchors exist, but three need corrections:
- **KAIST/KIST elastomer:** published **4 Jun 2026**, not 2025. The paper reports **elongation at break >600%**, which is consistent with the press figure of ">6x stretch". It used **36 formulations** for the surrogate model.
- **Northwestern PNAS:** the paper says "**less than 30 s** on a laptop… only 10 design attempts." The "26 s" figure comes from press.
- **Karacakol & Sitti:** the paper describes a "**5 million designs**" open database. The "53 runs / 1.5×10⁷ evaluations" figures could not be confirmed.

The Chem. Sci. self-healing PU paper (20 experiments, R² > 0.8, NSGA-III) and Sun et al. 2024 (ResNet + gradient descent / evolutionary algorithm) are verified. So are the MIT jumping-robot figures of +41% and +84% (MIT News).

### Cited Findings

| Claim | Status | Primary-source detail | Source |
|---|---|---|---|
| KAIST/KIST AI-optimized DLP elastomer, >6x stretch (Nature Communications) | **VERIFIED with corrections** | Song Y., Park B., Jeon S., Kweon H., Lee S., Na J., "Machine learning guided formulation design of digital light processing printable elastomers beyond viscosity stretchability tradeoff," Nature Communications, online **2026-06-04**, doi 10.1038/s41467-026-73735-4. Affiliations: KAIST Mechanical Eng.; KIST Extreme Materials Research Center; SeoulTech; KRICT; Konkuk Univ.; Univ. of Queensland (AIBN). Method: small-volume mold curing decouples characterization from printability; regression models were trained on viscosity, curing time, elongation at break and tensile modulus. Five-fold CV used "the 36 formulations used for surrogate-model development (33-point training set + three anchor formulations)." The ML-recommended resin (50:30:16:4 wt%) has viscosity "approximately 2500 mPa·s and elongation at break exceeding 600%." Printed pneumatic grippers held a glass bottle, an egg, an egg carton and a mouse, at >200 kPa. GP/BO is named as **future** work, so the method itself is not BO. The press claim of a 1 kg water bottle was not found in the text checked. | [nature.com article](https://www.nature.com/articles/s41467-026-73735-4) [PR]; [Crossref](https://api.crossref.org/works/10.1038/s41467-026-73735-4) |
| Karacakol, Alapan, Demir & Sitti, Nat. Commun. 2025; 53 runs; ~1.5×10⁷ evaluations | **Paper VERIFIED; 53 runs / 1.5×10⁷ UNVERIFIED** | Online 26 Mar 2025, doi 10.1038/s41467-025-58091-z (MPI-IS; Koç Univ.; others). Abstract: "stochastic design alterations guided by a predictive neural network, combined with cost-efficient simulations," to co-optimize magnetization profile and morphology. It reports "enhanced jumping performance over an intuitive reference design." Full text: design spaces "~1.2e752 and ~1.8e53" for sheet and beam robots; a MAP-Elites-based algorithm; "The 5 million designs generated in this work, made available through an open-access database." Dataset: Zenodo 10.5281/zenodo.14827843 (HTTP 403 when fetched). | [PMC11947188 full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11947188/) [PR] |
| Sun et al., Nat. Commun. 2024, 4D-printed active plates | **VERIFIED** | Sun X., Yue L., Yu L., Forte C.T., Armstrong C.D., Zhou K., Demoly F., **Ruike Renee Zhao** (Stanford corresponding group; also Georgia Tech, NTU, UTBM/CNRS). Online 29 Jun 2024. "A residual network ML model is developed for the forward shape prediction. A global-subdomain design strategy with ML-GD and ML-EA is then used for the inverse material-distribution design." | [OpenAlex abstract](https://api.openalex.org/works/doi:10.1038/s41467-024-49775-z) [PR] |
| Chem. Sci. 2026 self-healing PU, 20 experiments | **VERIFIED** (date nuance) | Liang K., Qi X., Xiao X., Wang L., Zhang J., "Chemically-informed active learning enables data-efficient multi-objective optimization of self-healing polyurethanes," Chem. Sci., **first published 2025-12-23** (2026 volume; correction 2026-01-22). Abstract: "optimize fluorescent self-healing PU with merely 20 experimental datasets… gradient boosting regression with multi-objective optimization… relative error of the comprehensive performance index below 12%… optimal results with only 15 samples when discrete performance data are available." Full text: "average prediction accuracy R² > 0.8," Pareto front via NSGA-III. Earlier baseline models over-fit, with test R² as low as 0.10–0.40. | [PMC12758484 full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758484/) [PR] |
| Northwestern 2023 PNAS "instant evolution", 26 s | **PARTIALLY VERIFIED** (paper says <30 s) | Matthews D., Spielberg A., **Rus D.**, Kriegman S., Bongard J., "Efficient automatic design of robots," PNAS, 3 Oct 2023. Full text: "a custom robot was efficiently and automatically generated in less than 30 s on a laptop computer (Fig. 1), requiring only 10 design attempts." The abstract says "within seconds on a single consumer-grade computer," starting from "a randomly-generated apodous body plan," and "consistently discovers legged locomotion." The 26 s figure is from press. | [PMC10576117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10576117/) [PR]; [ScienceDaily](https://sciencedaily.com/releases/2023/10/231003173425.htm) [PRESS] |
| MIT CSAIL diffusion jumping robot +41% | **VERIFIED** (press + conference metadata) | Kim B., Wang T.-H., Rus D., "Generative-AI-Driven Jumping Robot Design Using Diffusion Models," ICRA 2025 (19 May 2025). MIT News: the robot "leaps up an average of roughly 2 feet, or 41 percent higher than a similar machine they created on their own"; the AI-designed foot meant it "fell far less often than its baseline, to the tune of an 84 percent improvement." | [Crossref ICRA record](https://doi.org/10.1109/icra55743.2025.11128113) [PR]; [MIT News](https://news.mit.edu/2025/using-generative-ai-help-robots-jump-higher-land-safely-0627) [PRESS] |
| Xenobot replication "~4 generations" (PNAS 2021) | **VERIFIED** | Kriegman, Blackiston, Levin & Bongard, PNAS, 29 Nov 2021. "The maximum of two rounds of self-replication achieved by the spheroids … was extended by the semitoroids to a maximum of four rounds." The significance statement says "artificial intelligence can design clusters that replicate better." | [PMC8670470](https://pmc.ncbi.nlm.nih.gov/articles/PMC8670470/) [PR]; [Crossref](https://doi.org/10.1073/pnas.2112672118) |

### Inferences
- The KAIST paper is ML-guided formulation (regression surrogates on 36 formulations), **not** a closed loop or BO. The earlier "AI found the optimal formulation" wording is acceptable, but "2025" must become "June 2026".
- MIT's Daniela Rus is a co-author on both the Northwestern PNAS 2023 paper and the ICRA 2025 jumping robot. MIT's role in morphology–material co-design is therefore larger than the earlier notes implied.

### Gaps
- The 1 kg water-bottle demo for the KAIST material and the "500 designs / 5 rounds" detail for MIT were not re-checked in primary text.
- The 53 runs / 1.5×10⁷ evaluations figures for Karacakol rest only on a Koç University dataset record seen in the earlier session. The paper itself says 5 million designs.

---

## Q4. Gap-fill: ML/AI for IPMC/ionic actuators, HASEL design and CNT-yarn actuators

### Takeaway
- **IPMC:** has **ML for control and behaviour prediction**: BO-based learning control of 3D-printed IPMCs (Scientific Reports 2019) and NN prediction of Cu-IPMC output. It has no ML-driven material design.
- **HASEL:** no ML *design* paper was found. The ML work is data-driven modelling and control: a spectral-submanifold model from Jan 2026 (preprint) and an RNN/MLP predictive controller (2022).
- **CNT-yarn muscles:** no ML study was found. Optimization there is physics- and simulation-based.

### Cited Findings
- **IPMC + BO control (VERIFIED abstract).** Carrico, Hermans, Kim & Leang, "3D-Printing and Machine Learning Control of Soft Ionic Polymer-Metal Composite Actuators," Scientific Reports, 25 Nov 2019 [PR]:
  - Fused-filament 3D printing of ionomeric precursor produces custom-shaped monolithic IPMCs.
  - "Bayesian optimization is used as a learning-based control approach to help mitigate complex time-varying dynamic effects."
  - A modular IPMC soft crawling robot was demonstrated.
  - "Results show enhancement of actuator performance through machine learning."
  - Source: [PMC6877587](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6877587/)
- **IPMC NN prediction [SNIP].** Yang et al., ACS Omega (2020): a Levenberg–Marquardt back-propagation network maps dimension ratio and voltage to displacement and blocking force for Cu/Nafion IPMC — [Bohrium record](https://bohrium.dp.tech/paper/arxiv/812676022817259521)
- **IPMC hybrid model [PRE, SNIP].** Annabestani et al. (2022) pair an analytical model with a deep NN for a non-autoregressive IPMC model, average NMSE 9.58×10⁻⁴ — [arXiv 2203.01616](https://arxiv.org/abs/2203.01616v1)
- **Actuator selection by ML [PRE, SNIP].** An SVM trained on a literature-derived artificial-muscle dataset, including IPMCs, to pick actuators for given constraints — [arXiv 2104.07168](https://arxiv.org/pdf/2104.07168.pdf)
- **KAIST "Ionograsper" (prior notes).** An ionic sense-and-actuate material; coupling with AI is a stated plan, not a result.
- **HASEL data-driven model and control (VERIFIED abstract).** "Nonlinear Spectral Modeling and Control of Soft-Robotic Muscles from Data" (arXiv 2601.03247, 6 Jan 2026) [PRE]:
  - It learns an input-to-output map on a spectral submanifold from forced-response trajectories, "avoiding decay experiments that can trigger hysteresis."
  - It was deployed for real-time control of an antagonistic HASEL-clutch joint, with "a substantial reduction in tracking error compared to feedback-only and feedforward" baselines.
  - Source: [arXiv API record](https://export.arxiv.org/api/query?id_list=2601.03247)
- **HASEL other work [SNIP].**
  - An RNN/MLP pattern-matching predictive controller for HASEL (2022 conference) — [Bohrium record](https://bohrium.dp.tech/paper/arxiv/864971402757800208)
  - A non-ML geometric dimensioning of antagonistic HASELs using grid search and CMOPSO (UCLouvain master's thesis) — [UCLouvain DIAL](https://thesis.dial.uclouvain.be/entities/masterthesis/8714307b-2a4c-4ff0-a8ad-82b31e6e2861)
- **CNT yarn [SNIP].** No ML work found. Reported numbers:
  - Baughman-group coiled CNT yarn with "contractile work capacity of 3.78 kJ/kg" — [UT Dallas repository](https://utd-ir.tdl.org/items/ebf1c023-506f-44a6-bc37-e1b2e066ac13)
  - A non-ML "tension optimization process" for record-efficiency coiled CNT muscles (J. Power Sources 2025) — [Illinois Experts](https://experts.illinois.edu/en/publications/improving-energy-conversion-efficiency-of-ion-driven-artificial-m/)

### Inferences
- For ionic and electrohydraulic actuators as of Nov 2026, ML sits at the **control and modelling layer**. The hysteresis and memory effects of IPMC and HASEL make data-driven models attractive, but no study optimizes the material (ionomer, dielectric liquid, shell film) with ML. This open niche parallels the LCE gap in the taxonomy notes.

### Gaps
- The ACS Omega IPMC paper and the HASEL RNN paper were not opened.
- No CNT-yarn BO or surrogate study was found in one targeted search.

---

## Q5. Gap-fill: ML for piezoelectric / triboelectric / magnetic skins, PEDOT:PSS and liquid-metal conductors, stretchable batteries

### Takeaway
- **Magnetic skins:** deep learning is applied, for example **60-fold super-resolution** in a 0.5 mm magnetized-film skin (Science Robotics 2021).
- **Stretchable conductors:** the strongest new item is a **University of Maryland (Po-Yen Chen) Nature Communications Jan 2026** paper. It combines robot-automated experimentation, an active-learning ANN ensemble and FE simulation to design strain-insensitive stretchable electrodes. Its caption reports metal-like conductivity at >1000% elongation. The paper also builds a **stretchable Zn‖MnO₂ battery**. This is the only ML-linked stretchable-battery result found.
- **Piezoelectric skins:** ML appears mainly as small-data inverse design of artificial-skin microstructure (2023 preprint, at least four orders of magnitude more efficient).
- **PEDOT:PSS and liquid metal:** no ML-for-formulation paper was found. Majidi's CMU group contributes an ML-for-soft-sensing **review** (2020).

### Cited Findings
- **Magnetic skin (VERIFIED abstract).** Yan, Hu, Yang, Yuan, Song, Pan & Shen, "Soft magnetic skin for super-resolution tactile sensing with force self-decoupling," Science Robotics, 1 Feb 2021 (CityU/HKUST/CMU affiliations per records) [PR]:
  - A "sinusoidally magnetized flexible film (with the thickness ~0.5 millimeters)" is read by a Hall sensor.
  - It measures normal and shear force with a single unit.
  - It achieves "a 60-fold super-resolved accuracy enhanced by deep learning."
  - Demos: grasping fragile objects and threading a needle by teleoperation.
  - Source: [Europe PMC record doi 10.1126/scirobotics.abc8801](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Soft%20magnetic%20skin%20for%20super-resolution%20tactile%20sensing%22&format=json)
- **Stretchable electrodes via robotics + ML (VERIFIED abstract/full text).** Yang H., Chen Q., … Li T., Chen P.-Y., "Predictive design of stretchable electrodes with strain-insensitive performance via robotics- and machine learning-integrated workflow," Nature Communications, 19 Jan 2026, doi 10.1038/s41467-026-68484-3 [PR]:
  - The workflow merges "robot-automated experimentation, machine learning predictions, and finite element simulations."
  - An ANN ensemble was built in two stages: feasible parameter-space definition, then active-learning loops.
  - It discovered a microtextured nanocomposite; a thin gold layer gives "metal-like conductivity" (a figure caption says "at over 1000% elongation").
  - "Electrodeposition of Zn and MnO₂ on gold conductors enables a stretchable Zn‖MnO₂ battery … strain-insensitive electrochemical performance."
  - Source: [PMC12916966](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916966/)
- **Earlier conference abstract, likely the same lineage [CONF, SNIP].** "Automatic Stretchable Conductor Design and Fabrication Via Machine Learning" (AIChE 2022): an SVM classifier on 286 compositions, then active learning and data augmentation to more than 10,000 virtual and real points — [AIChE 697f](https://www.aiche.org/academy/conferences/aiche-annual-meeting/2022/proceeding/paper/697f-automatic-stretchable-conductor-design-and-fabrication-machine-learning)
- **PEDOT:PSS.** No peer-reviewed ML formulation-optimization paper was found. Non-ML formulation results [SNIP]:
  - PEDOT:PSS blended with PR-PEGMA improves stretchability, conductivity and photopatternability together — [USPTO doc](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12662593)
  - 5 wt% ethylene glycol gives about 58 Ω/sq in inkjet-printed PEDOT:PSS — [bib-bvb record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_2520855381)
  - Background (still [TK]): Bao group, Wang et al., Science Advances 3:e1602076 (2017) — [doi](https://doi.org/10.1126/sciadv.1602076)
- **Liquid metal / CMU Majidi.**
  - Chin, Hellebrekers & Majidi, "Machine Learning for Soft Robotic Sensing and Control," Advanced Intelligent Systems, 3 Mar 2020, doi 10.1002/aisy.201900171 [PR review; title/venue verified via Crossref] — [Crossref](https://doi.org/10.1002/aisy.201900171)
  - Majidi-group LM papers found: EGaIn-wetted microelectronics skin (IROS 2018); SMA actuator with an embedded LM curvature sensor (Frontiers 2021). These use closed-loop control, not ML material design [SNIP] — [CMU RI](https://www.ri.cmu.edu/publications/liquid-metal-microelectronics-integration-for-a-sensorized-soft-robot-skin); [Frontiers frobt.2021.599650](https://www.frontiersin.org/articles/10.3389/frobt.2021.599650/pdf)
- **Piezoelectric / artificial-skin inverse design (VERIFIED abstract).** "Inverse design of artificial skins" (arXiv 2304.04609, 10 Apr 2023) [PRE]:
  - "Property-to-structure inverse design of artificial skins based on small dataset machine learning."
  - "Comprehensive efficiency at least four orders of magnitude higher than the conventional routine."
  - Source: [arXiv API record](https://export.arxiv.org/api/query?id_list=2304.04609)
- **Related piezoelectric work [SNIP]:**
  - Multi-objective BO choosing stacking sequences for P(VDF-TrFE) yarns (Advanced Science 2024).
  - Phase-field + ML prediction of the piezoelectric coefficient of polymer/oxide nanocomposites (Advanced Science 2022).
  - Source: [search hit list incl. PMC10456750](https://pmc.ncbi.nlm.nih.gov/articles/PMC10456750)
- **Triboelectric.** Covered in the taxonomy notes Q2 (98–99% on about 12-object sets); nothing new.

### Inferences
- The UMD paper is the clearest 2026 example of ML *designing* a soft-robot conductor rather than decoding its signals. It partly overturns the taxonomy notes' inference that "ML is downstream only" for stretchable conductors.
- Magnetic and piezo skins show the same pattern as other e-skins: ML is used for decoding (super-resolution), with only early material/microstructure inverse design.

### Gaps
- No ML for intrinsically stretchable battery chemistries (electrolytes, binders) beyond the UMD electrode-plus-battery demo.
- No ML formulation study for PEDOT:PSS or EGaIn composites.
- The piezo inverse-design preprint's materials system was not checked in full text.

---

## Q6. Gap-fill: jamming / variable stiffness, catalytic micromotors, PLGA/silk biodegradable robots

### Takeaway
- **Variable stiffness:** ML now exists for jamming. A J. Bionic Eng. 2024 paper uses a grey-box NN with the virtual-work principle for particle-jamming modules. There are also an MRS 2024 ML-optimized 3D-printed jamming structure and ML+FEA surrogates for layer jamming.
- **Catalytic micromotors:** one verified ML-design paper exists (ACS AMI 2019). ML predicted speed and water-cleaning efficiency from 13 features, and the Pt nanomotor designed from it matched predictions within 15%.
- **PLGA/silk microrobots:** no ML-designed robot was found. ML-based PLGA degradation prediction (2026) exists as an enabling piece.

### Cited Findings
- **Particle-jamming module.** "Intelligent Optimization of Particle-Jamming-Based Variable Stiffness Module Design Using a Grey-box Model Based on Virtual Work Principle," Journal of Bionic Engineering, 24 Jun 2024, doi 10.1007/s42235-024-00563-x (title, venue and date verified via Crossref; method from snippet) [PR] — [Crossref](https://doi.org/10.1007/s42235-024-00563-x); [UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10195378)
- **3D-printed jamming structure.** Yoo, Jin & Gu (UC Berkeley), MRS Spring 2024: designs optimized with ML models trained on FE stiffness, then fabricated and tested in a pneumatic gripper [CONF, SNIP] — [MRS 2024](https://mrs.org/meetings-events/presentation/2024_mrs_spring_meeting/2024_mrs_spring_meeting-4010001)
- **Layer jamming.** Zeng & Su: an ML surrogate replaces FE simulations that take "tens of hours" [SNIP] — [NSF PAR 10557920](https://par.nsf.gov/servlets/purl/10557920)
- **Grain dataset.** A dataset paper on grain choice for granular grippers notes that ML has been used to create bespoke grains [PRE, SNIP] — [arXiv 2212.06511](https://arxiv.org/pdf/2212.06511)
- **Catalytic micromotors (VERIFIED abstract).** Zeng, Yuan, Huang & Cheng, "Accelerated Design of Catalytic Water-Cleaning Nanomotors via Machine Learning," ACS Applied Materials & Interfaces, 18 Oct 2019, doi 10.1021/acsami.9b14792 [PR]:
  - "Average absolute error of predicted velocity and predicted efficiency … 0.10 and 0.12."
  - 13 features and four algorithms; key features were particle size, catalyst type and aspect ratio.
  - A Pt-coated nanomotor designed from the models gave "less than 15% of prediction error."
  - Gradient boosting performed best.
  - Source: [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Accelerated%20Design%20of%20Catalytic%20Water-Cleaning%20Nanomotors%20via%20Machine%20Learning%22&format=json)
- **ML tracking of micromotors [PRESS, SNIP].** ICIQ / Univ. Gothenburg (Nanoscale, Nov 2023): ML tracks laccase-coated Si/MnO₂ tubular micromotors, converting urea to ammonia, under bubble occlusion. Here ML is used for characterization, not design — [ScienceDaily, 14 Nov 2023](https://www.sciencedaily.com/releases/2023/11/231114143902.htm)
- **PLGA [SNIP].** "Machine Learning Assisted Prediction of Degradation Behavior of Poly(Lactic-Co-Glycolic Acid)" (Materials Genome Engineering Advances, 2026) — [journal.hep.com.cn](https://journal.hep.com.cn/mgea/EN/10.1002/mgea.70062). A biodegradable-microrobot review notes PLGA is the only degradable polymer the FDA has approved for drug delivery, and that its acidic hydrolysis products are a concern [SNIP] — [Biomimetic Intelligence & Robotics PDF](https://journal.hep.com.cn/bir/EN/PDF/10.1016/j.birob.2025.100263)
- **Silk.** Only non-ML reviews were found: programmable biodegradability, with earlier silk devices mostly passive layers [SNIP] — [Frontiers in Chemistry 2022](https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2022.881028/epub)

### Inferences
- The micro/medical robot gap has narrowed but not closed:
  - catalytic motors have one 2019 supervised-ML design paper;
  - jamming has ML surrogates since 2024;
  - biodegradable polymers have degradation-prediction ML (2026) but no robot-level ML design.
- Linking degradation-rate ML to actuator performance, which ties to the Rumley and Baumgartner biogels, is the open next step.

### Gaps
- The full texts of the jamming and PLGA-ML papers were not opened; no quantified gains were retrieved.
- No ML study for Mg/Zn degradable micromotors or for silk microrobots was found.

---

## Q7. Institutions (MIT, CMU, Stanford-Bao) and closed-loop self-driving labs that synthesize AND test soft-robot materials

### Takeaway
- **MIT (Rus / Matusik):** a consistent co-design lineage: ChainQueen differentiable simulation co-optimizing material properties and geometry, DiffuseBot (2023), the PNAS 2023 co-authorship, and the ICRA 2025 jumping robot.
- **CMU (Majidi):** an ML-for-soft-sensing review (2020) and liquid-metal sensor hardware, but no ML-designed liquid-metal material.
- **Stanford (Bao):** neuromorphic e-skin (Science 2023), which is **not** ML-based. Bao's group also appears as a co-affiliation on the SNU Nature Materials paper.
- **Closed-loop SDLs:** none was found that **autonomously synthesizes/fabricates and tests a soft-robot actuator material end to end**. The closest are:
  - the 2026 DEA robotic *testing* platform (preprint; fabrication manual per a search summary);
  - the UMD 2026 robot-automated stretchable-electrode workflow (Nature Communications);
  - polymer-film SDLs such as PANDA (Materials Horizons 2024).

### Cited Findings
- **MIT ChainQueen [PR, SNIP].** Spielberg, Du, Hu, Rus & Matusik, "Advanced soft robot modeling in ChainQueen," Robotica (2021): the differentiable MPM simulator was extended to co-optimize material properties and geometric parameters — [MIT CDFG PDF](https://cdfg.csail.mit.edu/assets/files/robotica.pdf)
- **MIT, other verified items.**
  - Rus is a co-author of the PNAS 2023 Northwestern/UVM paper — [PMC10576117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10576117/)
  - The ICRA 2025 jumping robot is by Kim, Wang and Rus — [Crossref](https://doi.org/10.1109/icra55743.2025.11128113)
  - DiffuseBot (NeurIPS 2023) is in the prior notes.
- **CMU (Majidi).** Advanced Intelligent Systems review (2020) — [Crossref](https://doi.org/10.1002/aisy.201900171). Sitti also lists a CMU affiliation on the Karacakol 2025 Nature Communications paper per OpenAlex — [OpenAlex](https://api.openalex.org/works/doi:10.1038/s41467-025-58091-z)
- **Stanford (Bao).** Wang, Zhao, Bao et al., Science (2023): a monolithic soft prosthetic e-skin with multimodal perception, "neuromorphic pulse-train signal generation, and closed-loop actuation." No ML was reported in the coverage found [PRESS, SNIP] — [Stanford Engineering news](https://engineering.stanford.edu/news/soft-e-skin-generates-nerve-impulses-talk-brain). Stanford co-affiliation on the SNU Nature Materials paper is per OpenAlex — [OpenAlex](https://api.openalex.org/works/doi:10.1038/s41563-025-02373-w)
- **SDL status for soft-robot materials:**
  - **DEA testing robot** (arXiv 2602.20963): lifetime improved by up to 100%; claims the "first … self-driving lab approach" in actuator design [PRE] — [arXiv](https://export.arxiv.org/api/query?id_list=2602.20963). A NeurIPS 2026 entry frames long-horizon soft-actuator resilience as an AI challenge — [NeurIPS 2026 virtual 167788](https://neurips.cc/virtual/2026/167788)
  - **UMD stretchable-electrode workflow:** robot-automated experimentation, active-learning ANN and FE; the closest to synthesize-plus-test with ML for a soft-robot-relevant material [PR] — [PMC12916966](https://pmc.ncbi.nlm.nih.gov/articles/PMC12916966/)
  - **PANDA** (Materials Horizons 2024): a low-cost SDL doing polymer-film electrodeposition plus optical characterization in closed loop. It is not an actuator system [SNIP] — [RSC d4mh00797b](https://pubs.rsc.org/en/content/articlepdf/2024/mh/d4mh00797b)
  - **Earlier-session items:** a PNIPAM LCST "frugal twin" (arXiv 2509.05351) and the BU >25,000-experiment structures SDL (taxonomy notes).
  - **KAIST 2026 elastomer:** ML-guided, but uses manual small-volume mold curing (not autonomous) — [nature.com](https://www.nature.com/articles/s41467-026-73735-4)

### Inferences
- As of Nov 2026, the field has (a) autonomous *testing* of actuators, (b) robot-automated synthesis-plus-test for *conductors*, and (c) BO or active learning with manual synthesis for actuators (Aalto TCP 62/1,089, Chem. Sci. PU, 20 samples). Joining (a) and (b) into a fully autonomous actuator SDL is the visible next milestone.
- Updated institution map:
  - MIT: co-design / morphology.
  - CMU: sensing ML review plus liquid-metal hardware; Sitti co-affiliation.
  - Stanford: Bao neuromorphic hardware without ML; Zhao 4D-printing ML (Sun et al. 2024).
  - UMD: ML stretchable conductors.
  - KAIST/KIST: ML resin formulation.
  - SNU: memristive multimodal sensor with ML decoding.

### Gaps
- No 2024–2026 Matusik-group soft-material ML paper was located.
- No Bao-group ML-for-material paper was located.
- The fabrication-automation status of the DEA platform rests on a search summary, not on full text.

---

## 접근 상태 로그

All attempts in this session, via `curl -sSL -m 30 -A "Mozilla/5.0"` unless noted.

| Host | Result | Purpose |
|---|---|---|
| (WebFetch tool) | not attempted (reported broken in this session) | — |
| WebSearch tool (search backend) | success (17 queries) | Discovery of gap-fill papers and press figures; results marked [SNIP] |
| api.openalex.org | success, HTTP 200 ×10; then **HTTP 429** ×2 (daily free budget exhausted, "Rate limit exceeded") | Abstracts and metadata for Pelrine 2000, Haines 2014, Acome 2018, Kellaris 2018, Rumley 2023, Baumgartner 2020, Ko 2025, Liu 2024, Karacakol 2025, Sun 2024; title searches failed |
| www.ebi.ac.uk (Europe PMC REST) | success, HTTP 200 ×12 | Abstracts: Baumgartner, Chem. Sci. PU, PNAS 2023, IPMC, magnetic skin, nanomotor ML, UMD electrode; full-text phrase searches (no hits for "330,000"/"380%") |
| eutils.ncbi.nlm.nih.gov (NCBI efetch, PMC XML) | success, HTTP 200 ×7 | Full text of PMC11947188, PMC12758484, PMC10576117, PMC8302124, PMC9646516, PMC12916966, PMC8670470 |
| api.crossref.org | success, HTTP 200 ×8; **HTTP 500** ×1 (query exception); **HTTP 429** ×2 (rate limit; succeeded on retry) | Metadata: KAIST Nat. Commun. 2026, Materials & Design 2025, NiTi SMS 2022, ICRA 2025, Majidi review, jamming J. Bionic Eng., xenobot PNAS |
| www.nature.com | success, HTTP 200 ×4 (no Cloudflare) | KAIST s41467-026-73735-4 full page; Ko s41563-025-02373-w abstract (paywalled body); SuperTac s44460-025-00006-y abstract; Baumgartner s41563-020-0699-3 (paywalled, no cycle count visible) |
| export.arxiv.org (arXiv API) | **DNS failure** ×2 ("Could not resolve host", first http:// attempts), then success, HTTP 200 ×3 over https | Abstracts of 2602.20963, 2601.03247, 2304.04609 (one title search returned zero entries) |
| ntrs.nasa.gov (API + PDFs) | success, HTTP 200 ×8 | NiTi ML abstracts (20205008258, 20220005395) and slides (20220014943); no MAE values in text |
| link.springer.com | HTTP 200 but **bot "Client Challenge" page** ×2 (HTML and PDF URL) | NiTi ML paper 10.1007/s40830-022-00405-x |
| www.sciencedirect.com | **HTTP 403, Cloudflare** challenge | Materials & Design BO paper (guessed PII) |
| research.aalto.fi | success, HTTP 200 | Materials & Design 2025 BO abstract (62/1,089) |
| zenodo.org (API) | **HTTP 403** | Karacakol dataset record 10.5281/zenodo.14827843 |
| par.nsf.gov | success, HTTP 200 (PDF) | Pei-group DE review (380% / 7.2 MPa / 3.4 MJ/m³ attribution) |
| is.mpg.de | success, HTTP 200 (no cycle count on page) | Baumgartner biogels20 record |
| www.electronicsforu.com | success, HTTP 200 | Press figures 65%→95% for the SNU e-skin |
| www.eurekalert.org | **HTTP 403** | SNU press release 1133642 |
| www.tsinghua.edu.cn | success, HTTP 200 | SuperTac Chinese release (date, Ding Wenbo, DOVE 8.5亿) |
| computing.mit.edu | **HTTP 403, Cloudflare** | MIT jumping-robot news |
| news.mit.edu | success, HTTP 200 | MIT jumping-robot news (41%, 84%) |

Hosts cited above but **not fetched** (search results only): mdpi.com, syfy.com, govt.chinadaily.com.cn, sciencedaily.com, bohrium.dp.tech, aiche.org, mrs.org, discovery.ucl.ac.uk, journal.hep.com.cn, frontiersin.org, pubs.rsc.org, cdfg.csail.mit.edu, engineering.stanford.edu, utd-ir.tdl.org, experts.illinois.edu, thesis.dial.uclouvain.be, ri.cmu.edu, neurips.cc.
