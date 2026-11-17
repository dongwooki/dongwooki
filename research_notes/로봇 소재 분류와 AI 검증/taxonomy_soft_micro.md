# Taxonomy of Soft / Bio-inspired / Micro-nano / Medical-Biohybrid Robot Materials and Where AI/ML Is Applied

Notes compiled 2026-11-17. This file extends `research_notes/로봇 분야 소재공학 AI 도입/robot_materials_design.md` (called "prior notes" below). It does not repeat that file's items: Aalto/TUM discrete BO for coiled polymer actuators (62/1,089 samples), the Kent State LCE surrogate, KAIST's AI-formulated DLP elastomer (>6x stretch), GraphMetaMat, DiffuseBot, Northwestern instant evolution, MIT jumping robot, multimodal e-skin at 65%→95%, SHERO, or self-healing skin with transfer learning. The writer should pull those from the prior notes.

**Evidence labels:**
- **[PR]**: peer-reviewed journal or conference paper, seen in this session through search abstracts or snippets.
- **[PRE]**: preprint (arXiv), not peer-reviewed.
- **[PRESS]**: university press release or news coverage.
- **[TK]**: from background knowledge, NOT re-verified in this session. The DOI or URL is given so the writer can check it. Treat it as lower confidence.
- **[INF]**: the note-taker's own judgment, not a sourced fact. All maturity ratings are [INF] unless a source is cited.

**Access caveat:** arxiv.org, www.ncbi.nlm.nih.gov and pubs.rsc.org all failed DNS in this session (see the 접근 상태 로그 at the end). No full text was opened. Every number below comes from search-result abstracts or snippets, or is marked [TK].

---

## Q1. Soft actuator materials (artificial muscles): taxonomy, metrics, maturity and AI/ML use

### Takeaway
The actuator families differ by orders of magnitude in strain, stress, speed and efficiency:
- Dielectric elastomers (DEs) give large, fast strain: VHB above 380% area strain, about 7.2 MPa.
- Twisted and coiled polymer (TCP) fibers give high power: 49% contraction and 5.3 kW/kg.
- Shape memory alloys (SMAs) give high stress at small strain.
- Liquid crystal elastomers (LCEs) and hydrogels are slow but easy to program.

AI/ML use is uneven:
- It is most mature for SMA alloy composition, with NASA ML models predicting transformation temperatures to a mean absolute error (MAE) of 14.8 °C.
- It is also mature for magnetic soft composites (Sitti group, Nature Communications 2025, about 1.5×10⁷ simulation evaluations).
- It is emerging for DEs through self-driving-lab lifetime testing (2026 preprint) and physics-informed hybrid models.
- For hydrogels it is mostly formulation-level Bayesian optimization (BO) and GAN-based composite design.
- For LCEs, I found **no peer-reviewed BO-for-material/fabrication paper**. The only BO-plus-LCE work optimizes light-field gaits of LCE microrobots.

### Cited Findings

**Taxonomy table**

The table summarizes the findings below; the sources are in the bullets. Typical values are indicative and vary with test conditions.

| Category | Subcategory / materials | Mechanism | Typical metrics (source label) | Maturity [INF] | AI/ML used (this session) |
|---|---|---|---|---|---|
| Electroactive, field-driven | Dielectric elastomers: VHB 4910 acrylic, silicones (Elastosil, Sylgard) | Maxwell stress compresses a film between compliant electrodes | VHB area strain >380%, 7.2 MPa [PR snippet]; fast response; high energy density relative to LCE [PR review snippet] | Prototype; some commercial niches | Self-driving-lab lifetime screening (2026 PRE); physics-informed NN + FEM hybrid (<5% error); NN surrogate + GA for electrode patterns |
| Electrohydraulic | HASEL, Peano-HASEL (BOPP/Mylar shell, dielectric liquid) | Electrostatic zipping displaces liquid | Donut HASEL ~50% free strain; planar HASEL 79% strain under a 250 g load [review snippet] | Prototype / early commercial via spinout [INF] | None specific found |
| Thermally driven | SMA (NiTi, NiTiHf), SMP | Martensite↔austenite transformation; glass/melt transition | NiTiHf transformation temperature very composition-sensitive (Ms from 500 to −200 °C as Ni goes 49.8→51.3 at.%) [PR snippet] | NiTi wire commercial; NiTiHf prototype | ML composition→transformation-temperature/hysteresis/strain models (NASA); ML-discovered NiTiHf with Af 403.5 °C |
| Thermally driven | LCE (acrylate/thiol-ene, DLP-printed) | Nematic↔isotropic transition, programmed by director field | ~5.5 kJ/m³ energy density, slow (one review); DLP LCE 63 J/kg and 0.18 MJ/m³ (another) [PR snippets] | Lab / prototype | FEM surrogate inverse design (prior notes); adjoint/gradient optimization (2024); BO only for microrobot gait (2018) |
| Fiber | Twisted and coiled polymer fibers (nylon fishing line, sewing thread), CNT yarns | Thermally driven untwist of coiled fiber | 49% contraction; lifts >100x the load of human muscle of the same length and weight; 5.3 kW/kg; >30% stroke without hysteresis; millions of cycles [PR] | Prototype | Discrete BO (prior notes: strain 1.25 with 62/1,089 samples) |
| Swelling / stimuli-responsive | Hydrogels: PNIPAM (thermo), pH-sensitive, light-responsive; PAAm/alginate double network | Swelling/deswelling, LCST transition | No numbers retrieved this session | Lab | BO of a PAAm/alginate formulation; GAN design of meta-fiber hydrogel composites; SDL tuning of PNIPAM LCST |
| Ionic electroactive | IPMC, ionic EAPs, ionogels | Ion migration causes bending | No numbers retrieved | Lab / niche | None found this session |
| Magnetic soft composites | NdFeB microparticles in silicone (Ecoflex, PDMS) | Programmed magnetization; torque/force in an external field | Not retrieved | Lab / preclinical (medical) | NN + simulation loop co-optimizing magnetization and shape (Nature Communications 2025); GA for MAE unimorphs; inverse model R² 0.949 (prior notes) |
| Fluidic | Pneumatic elastomers (Ecoflex, Dragon Skin, TPU); thin multilayer pneumatic networks | Pressurized chamber expansion | Not retrieved | Commercial (soft grippers) [INF] | Diffusion inverse design of inflatables (prior notes); low-dimensional shape/material/actuation co-design (ETH 2026 PRE) |
| Biodegradable / edible | Gelatin–glycerol biogels | Pneumatic or electrohydraulic | Biogel actuators up to 200 V/µm field; >100,000 cycles; another write-up says >330,000 cycles (attribution unclear) | Lab | FEM model of degradation (R² 0.997); no ML |

**Dielectric elastomers (DE)**
- Acrylic VHB films reach area strain above 380% at a Maxwell stress of 7.2 MPa. DEs are rated "several orders of magnitude" above LCEs in energy density, with fast response, low modulus and low cost [PR review snippets] — [MDPI Polymers 17(6):746, 2025](https://www.mdpi.com/2073-4360/17/6/746); [SmartMat DE materials review, Aug 2023](https://doaj.org/article/e56142484eea4349971ff8501f70a461)
- The original record-strain paper is Pelrine et al., Science 287:836 (2000) [TK] — [doi:10.1126/science.287.5454.836](https://doi.org/10.1126/science.287.5454.836)
- **AI/ML: self-driving lab (SDL).** "A Robotic Testing Platform for Pipelined Discovery of Resilient Soft Actuators" (arXiv 2602.20963, Feb 2026) [PRE, snippet only]:
  - It robotically tests the lifetime of linear DEAs under high electric fields.
  - The samples are Elastosil-based, varying voltage, frequency, electrode material concentration and filler.
  - It claims to be the first SDL for robotic actuator design.
  - Automated fabrication and data-driven optimization are only *planned*.
  - The optimized actuators were built into a quadruped robot.
  - Source: [arXiv html](https://arxiv.org/html/2602.20963). A related NeurIPS 2026 entry frames soft-actuator long-horizon resilience as an AI challenge — [NeurIPS 2026 virtual 167788](https://neurips.cc/virtual/2026/167788)
- **AI/ML: physics-informed hybrid modelling.** Lahariya et al. (arXiv 2202.12977, 2022) pair a neural network that learns DEA material properties with an analytical model of the rest of the task [PRE]:
  - Training data come from FEM.
  - Error versus FEM is under 5%.
  - Used inside model-predictive control (MPC), it converged in fewer iterations than model-free actor-critic, PD and heuristic policies.
  - Source: [arXiv 2202.12977](https://arxiv.org/pdf/2202.12977)
- **AI/ML: PINN.** A physics-informed neural network (PINN) framework for large-deformation electromechanics of inflating DE tubes, aimed at energy harvesting (a DE generator, not an actuator) (Polymers, Aug 2025, doi 10.3390/polym17172329) [PR] — [PMC12431428](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12431428/)
- **AI/ML: NN surrogate + GA.** A neural-network surrogate plus a genetic algorithm (GA) optimized DEA electrode patterns, avoiding repeated FEM runs [PR snippet; paper identity not fully resolved] — [via search result, PMC10924066](https://pmc.ncbi.nlm.nih.gov/articles/PMC10924066)
- An autonomous platform, CORE, drove six DE artificial muscles in the cuttlefish-inspired "Cuttlebot" [PRE listing] — [CatalyzeX, Mihai Duduta](https://www.catalyzex.com/author/Mihai%20Duduta)

**Electrohydraulic (HASEL / Peano-HASEL)**
- A Donut HASEL reaches about 50% strain with no load; a planar HASEL reaches 79% strain under a 250 g (2.452 N) load. Force and strain are noted as the weak points of electrohydraulic actuators [review preprint] — [Tynan et al., Preprints.org 202502.0047](https://www.preprints.org/manuscript/202502.0047)
- Original papers: Acome et al., Science 359:61 (2018); Kellaris et al., Science Robotics 3:eaar3276 (2018). Strain and speed figures were not verified this session [TK] — [doi:10.1126/science.aao6139](https://doi.org/10.1126/science.aao6139); [doi:10.1126/scirobotics.aar3276](https://doi.org/10.1126/scirobotics.aar3276)

**Shape memory alloys (NiTi, NiTiHf) and SMPs**
- **AI/ML: composition models (NASA).** ML models trained on a database of multi-component Ni-Ti alloys predict transformation temperature, hysteresis and transformation strain. The MAEs are 14.8 °C, 7.2 °C and 0.36% respectively, and the models were validated with new experiments [conference abstract/NASA TRS] — [NASA NTRS 20205008258 (SMST 2021)](https://ntrs.nasa.gov/citations/20205008258)
- A NASA presentation notes the limits: some approaches are computationally expensive, still cannot estimate hysteresis or transformation strain accurately, and ignore processing history [NASA presentation] — [NASA NTRS 20220014943 (MS&T22)](https://ntrs.nasa.gov/citations/20220014943)
- **AI/ML: NiTiHf discovery.** ML found the ternary alloy Ni49.7Ti26.6Hf23.7, with an austenite finish temperature of 403.5 °C and "remarkable cyclic stability." Kankanamge et al. trained ML on Ms, thermal hysteresis and work output for balanced high-temperature SMA performance [PR snippets] — [J. Mater. Sci. 2022, s10853-022-07793-6](https://link.springer.com/article/10.1007/s10853-022-07793-6); [Shape Mem. Superelasticity, s40830-022-00405-x](https://link.springer.com/content/pdf/10.1007/s40830-022-00405-x.pdf); [Koç Univ. "SMA design by ML for biomedical and high-temperature applications"](https://research.hub.ku.edu.tr/entities/publication/8d9eedb4-7b56-4452-84a4-6dc1878f457a/full)
- Sensitivity that motivates ML: raising Ni content in NiTiHf from 49.8 to 51.3 at.% lowers Ms from about 500 °C to −200 °C [PR snippet] — [J. Mater. Sci. 2022](https://link.springer.com/article/10.1007/s10853-022-07793-6)
- **AI/ML: SMP lattices.** Inverse ML discovered SMP thin-walled cellular metamaterials with "record high recovery stress" (Int. J. Mech. Sci., 2023). A 2024 study used conditional GANs for SMP plate lattices [PR snippets] — [NSF PAR 10403742](https://par.nsf.gov/servlets/purl/10403742); [NSF PAR 10559158](https://par.nsf.gov/servlets/purl/10559158)
- SMA typical work density (about 10 J/cm³) and strain (about 4–8%): taken from the general review Madden et al., IEEE J. Oceanic Eng. 29 (2004), NOT verified [TK] — [doi:10.1109/JOE.2004.833135](https://doi.org/10.1109/JOE.2004.833135)

**Liquid crystal elastomers (LCE)**
- Two reviews report very different energy densities, from different test conditions: about 5.5 kJ/m³ with "slow actuation" in one, versus 63 J/kg and 0.18 MJ/m³ for a DLP-printed LCE in another [PR snippets] — [MDPI Machines 13(2):101](https://mdpi.com/2075-1702/13/2/101); [Springer Discover s43939-025-00225-7](https://link.springer.com/10.1007/s43939-025-00225-7)
- **AI/ML: Bayesian optimization (BO), the gap from the prior notes.** The only BO + LCE work found is "Gait learning for soft microrobots controlled by light fields" (von Rohr, Trimpe, Marco, Fischer, Palagi; MPI-IS; arXiv 1809.03225, 2018). It uses GP-based BO over periodic structured-light-pattern parameters for photo-responsive LCE microrobots, is data-efficient, and is robust to sample-to-sample variation. This is **control/stimulus optimization, not material optimization** [PRE/conference] — [ar5iv 1809.03225](https://ar5iv.labs.arxiv.org/html/1809.03225)
- **Non-BO optimization of LCEs:** a 2024 study uses a nonlinear LCE model with adjoint sensitivity and gradient optimization of director orientation and shape. A 2023 study used topology optimization to morph thermo-active LCEs into arbitrary target shapes [PR] — [PMC11125878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11125878/); LCE plate theory for metric-constrained actuation [PRE] — [arXiv 2410.00333](https://arxiv.org/pdf/2410.00333)
- Search confirmed that **no paper directly applies BO to LCE actuator material or geometry design** — [search summary; best hits listed above]

**Hydrogels (thermo / pH / light-responsive)**
- **AI/ML: BO of a formulation.** BO tuned a polyacrylamide/alginate double-network hydrogel for flexible electronics (2024). This is formulation, not actuator design [PR] — [PMC11422183](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11422183/)
- **AI/ML: GAN inverse design.** A Beijing University of Technology team used a GAN to design meta-fiber-reinforced hydrogel composites that meet target stress and displacement fields, avoiding topology optimization and trial-and-error [PR] — [PMC11165469](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11165469/)
- **AI/ML: SDL.** A Notre Dame "frugal-twin" low-cost autonomous platform optimized the lower critical solution temperature (LCST) of the thermoresponsive polymer PNIPAM, the basis of thermo-responsive hydrogel actuators [PRE] — [arXiv 2509.05351](https://arxiv.org/html/2509.05351v1)
- Reviews:
  - Hydrogel AI review: property prediction, multi-attribute optimization, high-throughput screening [PR] — [Materials Today Bio, Apr 2024](https://doaj.org/article/7b78e02180704039b697494728fcff2b)
  - AI for hydrogel development short review [PR] — [PMC10670215](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10670215/)
  - "Hydrogel and Machine Learning for Soft Robots' Sensing and Signal Processing" review (J. Bionic Eng., 2022/2023) [PR] — [Phenikaa repository PDF](https://dlib.phenikaa-uni.edu.vn/bitstream/PNK/7971/1/Hydrogel%20and%20Machine%20Learning%20for%20Soft%20Robots%e2%80%99%20Sensing%20and%20Signal%20Processing%20A%20Review-2022.pdf)
- Reference point for fast hydrogel actuation: Yuk et al., "Hydraulic hydrogel actuators and robots optically and sonically camouflaged in water," Nature Communications 8:14230 (2017) [TK] — [doi:10.1038/ncomms14230](https://doi.org/10.1038/ncomms14230)
- POSTECH (Prof. Dong Sung Kim) reported a water-driven hydrogel soft actuator that is "faster and stronger" than conventional ones. No ML was involved and no numbers were retrieved [PRESS via search] — [EurekAlert 1093381](https://www.eurekalert.org/news-releases/1093381)

**Twisted and coiled polymer fibers (TCP) and CNT yarns**
- Haines et al., Science 343:868–872 (2014) [PR]:
  - Coiled nylon or polyethylene fishing-line muscles contract by 49%.
  - They lift loads more than 100x heavier than human muscle of the same length and weight.
  - They produce 5.3 kW/kg of mechanical work.
  - A later Haines/Baughman review reports >30% tensile stroke when heated, no hysteresis, and millions of cycles without significant degradation.
  - Sources: [Soft Robotics Toolkit](https://softroboticstoolkit.com/publications/artificial-muscles-fishing-line-and-sewing-thread); [EMBS Pulse](https://www.embs.org/pulse/?p=365)
- AI/ML: the discrete BO result in the prior notes (strain 1.25 with 62/1,089 samples) is the main ML example. Nothing new was found for CNT yarns.

**Magnetic soft composites (NdFeB/silicone)**
- **AI/ML: data-driven co-design.** Karacakol, Alapan, Demir and Sitti, "Data-driven design of shape-programmable magnetic soft materials," Nature Communications 16:2946 (26 Mar 2025, doi 10.1038/s41467-025-58091-z) [PR]:
  - An optimization loop couples NN prediction with low-cost simulation to co-optimize the magnetization pattern and the 2D shape.
  - The designs fold into complex 2D/3D structures and can maximize rotation or minimize volume.
  - It improved jumping where the intuitive reference design failed to lift off.
  - The released dataset covers 53 learning runs and about 1.5×10⁷ simulation evaluations; the code is on GitHub.
  - This resolves a gap in the prior notes.
  - Sources: [PMC11947188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11947188/); [Nature Index record](https://www.nature.com/nature-index/article/10.1038/s41467-025-58091-z); [Koç Univ. dataset record](https://research.hub.ku.edu.tr/entities/data/4317a948-7e2e-4647-8e5b-da6142c667d2/full)
- **Predecessor (algorithmic, not ML):** MPI-IS (Lum, Sitti et al., 2016) gave a universal programming method that automatically generates magnetization profiles and actuating fields for time-varying shapes. Demos were a jellyfish-like robot, a sperm-like swimmer and an artificial cilium [PRESS] — [Max Planck Society news, Sep 2016](https://www.mpg.de/10754617/shape-programmable-miniscule-robots)
- Key material papers: Kim, Yuk, Zhao et al., Nature 558:274 (2018), printed ferromagnetic domains; Hu, Lum, Sitti et al., Nature 554:81 (2018), multimodal millirobot [TK] — [doi:10.1038/s41586-018-0185-0](https://doi.org/10.1038/s41586-018-0185-0); [doi:10.1038/nature25443](https://doi.org/10.1038/nature25443)

**Pneumatic / fluidic elastomers**
- POSTECH (Keehoon Kim, Wan Kyun Chung, with a Samsung Electronics researcher) built a myosin-inspired paper-thin multilayer 3D pneumatic-network "robot skin actuator" (Nature Communications, 2025). It moves in six directions and is aimed at surgical robots and pipe cleaning. **No ML was involved** [PR + PRESS] — [EurekAlert image 1085163](https://www.eurekalert.org/multimedia/1085163); [Electronics360](https://electronics360.globalspec.com/article/22643/muscle-mimicking-sheet-robot-passes-through-ultra-tight-spaces); [ElectronicsForU](https://www.electronicsforu.com/news/robotic-actuator-developed-using-muscle-protein)
- ETH Zurich (Katzschmann co-author) proposed a low-dimensional design embedding to jointly optimize shape, material distribution and actuation of soft robots (arXiv 2603.06497, Mar 2026) [PRE] — [arXiv 2603.06497](https://arxiv.org/html/2603.06497v1). ETH also has "Learning soft robotic dynamics" (arXiv 2510.27428) [PRE] — [arXiv](https://arxiv.org/html/2510.27428v1)

### Inferences
- [INF] ML in actuator materials splits by data regime:
  - Large legacy alloy databases support supervised composition→property regression (SMA).
  - Cheap simulators support NN-surrogate design loops (magnetic composites, about 10⁷ evaluations; LCE director fields).
  - Expensive experiments support BO or SDLs (TCP fibers, hydrogel formulation, DEA lifetime).
- [INF] LCE BO for chemistry or fabrication (crosslinker ratio, alignment process, print parameters) remains an open niche as of Nov 2026, based on what surfaced in searches.
- [INF] Reliability metrics (cycle life, dielectric breakdown) are becoming ML targets, not only peak strain (DEA SDL 2026; NeurIPS 2026 "resilience optimization").

### Gaps
- No ML studies with numbers were found for IPMC/ionic EAPs, HASEL, or CNT-yarn actuators.
- Full-text numbers could not be retrieved for:
  - the DEA SDL (sample counts, lifetime gains), because arxiv.org was DNS-blocked;
  - the PAAm/alginate BO hydrogel (iterations, properties), because ncbi was DNS-blocked.
- No single peer-reviewed review compares DE, HASEL and LCE on identical metrics (search summary noted this). Typical values above mix sources and conditions.
- HASEL original metrics and SMA work density are [TK] and unverified.

---

## Q2. Soft/stretchable sensing materials (e-skin): taxonomy and ML decoding

### Takeaway
E-skin materials span several transduction families:
- piezoresistive (CNT, graphene, AgNW, EGaIn);
- capacitive;
- piezoelectric (PVDF, BaTiO₃);
- triboelectric;
- ionic (ionogels, hydrogels);
- optical (waveguides);
- magnetic.

ML is now routinely used to decode them:
- Triboelectric grippers classify about 12 objects at 98–99%.
- An EGaIn-silicone glove reaches about 97% gesture accuracy (random forest).
- Tsinghua's 3D-architected e-skin (Science 2024) uses deep learning to infer object modulus and curvature with 240 sensors in a fingertip and about 0.1 mm position resolution.

ML is used far less to *design* the sensing material itself.

### Cited Findings

**Taxonomy table**

| Transduction | Representative materials | ML-decoding example with numbers | Maturity [INF] |
|---|---|---|---|
| Piezoresistive / resistive | EGaIn microchannels in silicone; CNT, graphene, AgNW networks | EGaIn-silicone glove, 6 classifiers: random forest ~97.3%, LDA ~87.4% (Sensors 2021) | Lab to commercial (tactile pads) |
| Capacitive | Elastomer dielectrics with stretchable electrodes; EGaIn capacitive modules | Stretch-sensing glove: 35% better reconstruction than commercial data gloves (NSF PAR) | Commercial (gloves, tactile arrays) |
| Triboelectric | Porous PDMS, fluoropolymers | 98.46% for 12 samples (hybrid tribo-capacitive); 99.2% for 12 grasped objects; SVM 98.1% | Lab / prototype |
| Piezoelectric | PVDF, BaTiO₃ composites | Not retrieved this session | PVDF film commercial |
| Ionic | Ionogels, hydrogels, ionic skins | Hydrogel + ML review (J. Bionic Eng.) | Lab |
| 3D architected / multilayer | Tsinghua 3D e-skin with layer moduli matched to skin | Deep learning infers modulus and curvature; 240 sensors per fingertip; ~0.1 mm resolution | Lab |
| Optical / magnetic | Waveguides, magnetic skins | Not retrieved this session | Lab |

**Supporting findings**
- **Liquid metal (EGaIn) glove.** Shin, Yoon and Yoo, "Hand Gesture Recognition Using EGaIn-Silicone Soft Sensors," Sensors (2021). Random forest reached about 97.3%, LDA about 87.4%, and the other classifiers >90%. The non-linear sensor response hurt the linear model [PR] — [PMC8125695](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8125695/); [UMD DRUM](https://drum.lib.umd.edu/items/8efcf5e4-c061-4006-9a0f-562db0cb91dc/full)
- A stretchable textile glove with an EGaIn-based capacitive module and multi-stage ML (arXiv 2410.02221). Its headline accuracy was not confirmed [PRE] — [deeppaper mirror](https://arxiv.deeppaper.ai/papers/2410.02221v1)
- An interactive stretch-sensing soft glove reported 35% better hand-pose reconstruction than commercial data gloves [PR] — [NSF PAR 10602565](https://par.nsf.gov/biblio/10602565-interactive-hand-pose-estimation-using-stretch-sensing-soft-glove)
- **Triboelectric sensors:**
  - Hybrid triboelectric-capacitive porous-PDMS sensor: deep learning reached 98.46% across 12 samples. The triboelectric unit senses material and texture; the capacitive unit senses hardness (Microsystems & Nanoengineering, Nov 2024) [PR] — [PMC11543809](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11543809/)
  - AI-enhanced triboelectric multimodal robotic-finger sensors: 12 grasped objects at 99.2%, softness at 94.1% (Adv. Funct. Mater., 2024) [PR] — [Bohrium record](https://bohrium.dp.tech/paper/arxiv/38777681)
  - Soft gripper with a 1D-CNN: 98.96% (iScience, Aug 2023) [PR] — [DOAJ](https://doaj.org/article/dff61b11595a44af9e5b88c9e388df3f)
  - Triboelectric soft gripper with an SVM: 98.1% (Nature Communications 2020) [PR] — [RePEc](https://ideas.repec.org/a/nat/natcom/v11y2020i1d10.1038_s41467-020-19059-3.html)
  - Dual-modal flexible e-skin with AlexNet: material 93.49%, hardness 92.22% (RSC 2025) [PR] — [RSC Lab Chip d5lc00020c](https://pubs.rsc.org/en/content/articlepdf/2025/lc/d5lc00020c)
- **Tsinghua (Zhang Yihui).** Liu et al., "A three-dimensionally architected electronic skin mimicking human mechanosensation," Science (2024), doi 10.1126/science.adk5556 [PR + PRESS]:
  - The epidermis, dermis and subcutaneous layers have skin-like moduli.
  - The fingertip patch holds 240 sensors with about 0.1 mm resolution.
  - Deep learning measures object modulus and local principal curvature by touch.
  - Sources: [China Daily, 5 Jun 2024](https://www.chinadaily.com.cn/a/202406/05/WS6660022ea31082fc043cb0b1.html); [TechXplore PDF](https://techxplore.com/news/2024-06-electronic-skin-mimics-human-3d.pdf)
- **UESTC (not Tsinghua).** Nano Research, Nov 2025: an SE-ResNet classified hardness at a reported 100% accuracy [PR snippet] — [EurekAlert 1110905](https://www.eurekalert.org/news-releases/1110905)
- **SNU (Seung Hwan Ko group).** A Nature Materials 2025 multimodal temperature-plus-pressure tactile sensor for robots [PRESS aggregator; not verified]. It may be the same paper as the Nature Materials 2025 e-skin in the prior notes (DOI 10.1038/s41563-025-02373-w, 65%→95% accuracy), but **this link is unconfirmed** — [hyper.ai](https://hyper.ai/de/stories/19de574a138b6c477f7ff1f6e3e11575)
- **SuperTac** (Nature Sensors, Jan 2026), with Tsinghua Shenzhen co-author Ding Wenbo. It is a multi-institution visuotactile sensor; metrics are in the prior notes [PRESS] — [hyper.ai](https://hyper.ai/en/stories/e6741003f026c4ea736b5ad66ca2f95d)

### Inferences
- [INF] The reported 92–100% classification accuracies come from small, closed object sets of about 12 items. They do not show generalization and should not be compared across papers.
- [INF] ML's role in e-skin is mostly *signal decoding*. Examples of *ML-designed sensing materials* (formulation, microstructure) are scarce compared with actuators.

### Gaps
- No ML studies with numbers were retrieved for PVDF/BaTiO₃ piezoelectrics, optical waveguide skins, or magnetic skins.
- No ML-guided synthesis of conductive composites (e.g., CNT or AgNW percolation optimization) was found this session.

---

## Q3. Stretchable conductors and electronics (liquid metal, serpentine metals, PEDOT:PSS, stretchable energy)

### Takeaway
This category was the least covered this session. Liquid-metal (EGaIn) sensors appear mainly as ML-decoded sensor substrates (Q2). No retrieved source applied ML to designing PEDOT:PSS formulations, serpentine-interconnect geometry, or stretchable batteries for robots.

### Cited Findings
- EGaIn-silicone microchannel sensors as an ML-decodable stretchable conductor (Sensors 2021) [PR] — [PMC8125695](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8125695/)
- Polybot autonomous lab work on electrochromic and electrochemical sensing polymers relevant to soft robots (MRS Spring 2024 talk; this is the Argonne Polybot SDL lineage [TK for attribution]) [conference abstract] — [MRS 2024 Spring presentation 4009314](https://mrs.org/meetings-events/presentation/2024_mrs_spring_meeting/2024_mrs_spring_meeting-4009314)
- Background (TK, unverified): Stanford Bao group intrinsically stretchable PEDOT:PSS with ionic additives — Wang et al., Science Advances 3:e1602076 (2017) — [doi:10.1126/sciadv.1602076](https://doi.org/10.1126/sciadv.1602076)
- Battery/GNoME links are in the prior notes (Q2/Q4); not duplicated here.

### Inferences
- [INF] For stretchable conductors, ML is applied downstream (decoding) rather than upstream (material design). This is a clear gap for the report to flag.

### Gaps
- No ML-for-PEDOT:PSS, ML-for-serpentine-interconnect, or ML-for-stretchable-battery robot examples were found.
- No metric table (conductivity vs. strain, cycle life) was retrieved this session. Writers should not invent typical values.

---

## Q4. Functional/smart structural materials: self-healing, variable stiffness, metamaterials, origami/kirigami, 4D printing

### Takeaway
ML is mature here:
- Voxel-level 4D-printing inverse design (ResNet forward model plus gradient descent and evolutionary algorithms; Nature Communications 2024).
- Kirigami inverse design (supervised autoencoder, tandem networks).
- Harvard (Bertoldi) neural-accelerated evolution strategy for nonlinear metamaterial response (Advanced Materials 2022).
- Self-healing polymers via chemistry-informed active learning that co-optimized strength and healing with only 20 experiments (Chem. Sci. 2026).

A Boston University SDL ran more than 25,000 ML-guided experiments on energy-absorbing printed structures. No ML results for variable-stiffness materials (jamming, low-melting-point alloys) were found.

### Cited Findings

**Self-healing polymers**
- **Chemically informed active learning.** Chemical Science 2026 (issue 7), d5sc07752d [PR snippet]:
  - Material: fluorescent self-healing polyurethanes.
  - Method: gradient-boosting regression, then NSGA-III multi-objective optimization to find Pareto-optimal trade-offs between mechanics and healing.
  - Only 20 experimental datasets; average R² > 0.8.
  - Source: [RSC Chem. Sci. d5sc07752d](https://pubs.rsc.org/en/content/articlehtml/2026/sc/d5sc07752d)
- **MD + random forest.** Zhou, Wen and Nie (Macromolecules, 2024) found chain diffusion/interpenetration is the most important factor for self-healing efficiency [PR] — [LAMMPS abstract page](https://www.lammps.org/abstracts/abstract.34877.html); [AMiner](https://aminer.org/pub/65fe7ac113fb2c6cf68a1ea0/microscopic-mechanisms-of-self-healing-in-polymers-revealed-by-molecular-simulations-and)
- **Microcapsule composites.** ANN plus FEM found 10 vol% microcapsules maximize healing efficiency; nanoparticles trade strength for less self-repair (2025) [PR] — [Univ. Isfahan RIS](https://ris.ui.ac.ir/fa/profile/article/Computational-and-experimental-investigation-of-microcapsule-based-self-healing-polymers-Macro-mechanical-finite-element-modeling-and-artificial-neural-network-predictions)
- Early work: "Towards machine learning approaches for predicting the self-healing efficiency of materials" (Comput. Mater. Sci., 2019) [PR] — [OUCI](https://ouci.dntb.gov.ua/works/42zNJww4)
- Robot-level self-healing with ML (SHERO, UNL actuator, transfer-learning skins) is in the prior notes.

**Mechanical metamaterials and kirigami**
- **Harvard (Bertoldi).** Bordiga, Medina, Jafarzadeh, Bösch, Adams, Tournat and Bertoldi, Advanced Materials (2022): a neural-accelerated evolution strategy inverse-designs metamaterials with target nonlinear response [PR + MRSEC highlight] — [Harvard MRSEC highlight 222](https://mrsec.harvard.edu/research/highlight_222.php); [MRSEC.org highlight 1725](https://mrsec.org/highlights/1725-inverse-design-of-mechanical-metamaterials-with-target-nonlinear-response-via-a-neural-accelerated-evolution-strategy)
- **Kirigami (Harvard physics affiliation).** Hanakata, Cubuk, Campbell and Park, Physical Review Research (2020): a supervised autoencoder for inverse kirigami design [PR] — [APS March 2020 abstract](https://archive.aps.org/mar/2020/m34/4)
- **Kirigami (Northwestern).** Alderete, Pathak and Espinosa, npj Computational Materials (2022): clustering, tandem NNs and symbolic regression [PR] — [npj Comput Mater s41524-022-00873-w](https://www.nature.com/articles/s41524-022-00873-w)
- Kirigami-inspired inflatables with programmable shapes (Polimi repository; Bertoldi-group collaboration [TK]) [PR] — [Polimi PDF](https://re.public.polimi.it/bitstream/11311/1156527/1/Kirigami_inspired_inflatables_with_programmable_shapes.pdf)
- **SDL for structures.** A BU self-driving lab ran more than 25,000 ML-guided experiments on additively manufactured structures to find energy-absorbing designs (arXiv 2308.02315) [PRE] — [arXiv 2308.02315](https://pdf.arxiv.org/pdf/2308.02315). Published version: Snapp et al., Nature Communications 2024, reported 75.2% energy-absorbing efficiency [TK, unverified] — [doi:10.1038/s41467-024-48534-4](https://doi.org/10.1038/s41467-024-48534-4)

**4D printing (SMP / active composites)**
- **Voxel inverse design.** Sun et al., "Machine learning-enabled forward prediction and inverse design of 4D-printed active plates," Nature Communications 15:5509 (29 Jun 2024) [PR]:
  - Two-material active/passive voxel encoding.
  - A residual-network forward model.
  - Gradient-descent and evolutionary-algorithm inverse design for target 3D shape change.
  - Sources: [Springer/Nature Comms s41467-024-49775-z](https://link.springer.com/article/10.1038/s41467-024-49775-z); [DOAJ](https://doaj.org/article/f8be89eae64244bb9cd089f4dbc78562)
- **Facial shells.** Bi-material PLA/SMP 4D-printed facial shells: a fully convolutional network for inverse design and forward prediction, with multi-task and transfer learning (Soft Science, Nov 2025) [PR] — [OAE Soft Science ss.2025.81](https://www.oaepublish.com/articles/ss.2025.81)

**Variable stiffness (jamming, LMPA, SMP)**
- No ML-design examples were retrieved this session.

### Inferences
- [INF] Structural/architected materials are where AI inverse design is most established: many forward models (ResNet, GNN, VAE), clear targets (stress–strain curves, shapes) and cheap FEM data.
- [INF] Self-healing ML has moved to small-data active learning (20 experiments) with multi-objective optimization. This suits robot skins, where the strength-versus-healing trade-off is the central constraint.

### Gaps
- No ML for jamming, LMPA or other variable-stiffness materials was found.
- No Bertoldi-specific kirigami-ML paper was found; the search said to check the group's publication list — [Bertoldi Group publications](https://bertoldi.seas.harvard.edu/publications)

---

## Q5. Micro/nano-robot and medical/biohybrid robot materials

### Takeaway
Most ML in micro/medical robots is used for control, not materials:
- Reinforcement learning (RL) for 3D magnetic microrobot positioning (Nature Machine Intelligence 2024).
- BO for light-field gaits of LCE microrobots (2018).

The material/morphology-design exceptions are:
- Sitti's data-driven magnetization + shape design (Nature Communications 2025, Q1).
- AI-designed xenobots: the evolutionary design of 2020; the C-shape that extended kinematic self-replication to about four generations (PNAS 2021).
- ETH's computationally designed muscle-scaffold biohybrid (Nature Communications 2026).

Tokyo's human-muscle biohybrid hand (Science Robotics, Feb 2025) is a non-ML materials milestone: 18 cm, five fingers, fatigue after 10 min. No ML for catalytic micromotor design was found.

### Cited Findings
- **Magnetic microrobots: control.** RL for autonomous 3D positional control of a magnetic microrobot — Abbasi, Choi, Nelson et al., Nature Machine Intelligence (2024) [PR via review] — [MDPI Mathematics 12(14):2180 review](https://mdpi.com/2227-7390/12/14/2180)
- **Design-as-optimization perspective.** Dhatt-Gauthier, Livitz, Wu and Bishop (Columbia), JACS Au (2023): the design-performance relationship is "high-dimensional, nonlinear, stochastic, and unknown," which motivates automated experiments and ML [PR] — [PMC10052236](https://pmc.ncbi.nlm.nih.gov/articles/PMC10052236)
- **Light-driven LCE microrobots.** GP-based BO gait learning (MPI-IS, 2018) [PRE/conf] — [ar5iv 1809.03225](https://ar5iv.labs.arxiv.org/html/1809.03225)
- **Xenobots (biohybrid, AI-designed).** "Kinematic self-replication in reconfigurable organisms," PNAS (2021) [PR + PRESS]:
  - AI simulation found that a C-shape piles loose cells better than the spheroid.
  - It extended replication to about four generations.
  - It was described as the first observation of kinematic self-replication in living organisms.
  - Sources: [Wyss Institute news](https://wyss.harvard.edu/news/team-builds-first-living-robots-that-can-reproduce/embed/); [NPR, 1 Dec 2021](https://www.npr.org/2021/12/01/1060027395/robots-xenobots-living-self-replicating-copy); [Science News](https://sciencenews.org/article/tiny-living-machines-xenobots-replicate-copies-frog-cells). DOI [TK]: [10.1073/pnas.2112672118](https://doi.org/10.1073/pnas.2112672118)
- Biological robots perspective (2022): human cognitive limits narrow the design space, so nonhuman (AI) assistance is needed [PRE] — [arXiv 2207.00880](https://arxiv.org/pdf/2207.00880)
- **ETH Zurich biohybrid** (Balciunaite et al.), Nature Communications 17:10732 (2026; press 1 Nov 2026) [PR + PRESS]:
  - Cultured mouse muscle and a soft scaffold were designed together computationally from scratch.
  - The design calculations favored a two-layer muscle/scaffold stack, modeled in liquid.
  - The robot jumps and walks in liquid.
  - Quote: "we wanted to design the whole thing from scratch on the computer."
  - Sources: [Netzwoche, 1 Nov 2026](https://www.netzwoche.ch/news/2026-11-01/ein-kleiner-sprung-fuer-den-muskel-ein-grosser-schritt-fuer-die-robotik); [Wevolver](https://www.wevolver.com/article/one-small-leap-for-a-muscle-one-giant-step-for-robotics); [Xenospectrum](https://xenospectrum.com/en/biohybrid-muscle-scaffold-robot-design/)
  - Whether the design method is ML or classical optimization was not confirmed.
- **University of Tokyo / Waseda (Shoji Takeuchi).** Ren, Morimoto, Takeuchi et al., "Biohybrid hand actuated by multiple human muscle tissues," Science Robotics (12 Feb 2025) [PR + PRESS]:
  - Bundled thin strands of cultured human muscle in a "sushi-roll" MuMuTA so nutrients reach each strand.
  - The hand is 18 cm long with a 6 cm palm and five independently moving fingers; it makes a scissors gesture and grasps small objects.
  - Earlier devices were limited to single joints and about 1 cm.
  - The hand must be suspended in liquid.
  - Contractile force fatigued after 10 min of electrical stimulation and recovered within 1 h.
  - **No ML in the material design** was reported.
  - Sources: [News-Medical, 14 Feb 2025](https://www.news-medical.net/news/20250214/Biohybrid-hand-with-muscle-tissue-mimics-real-life-movements.aspx); [JST Science Japan, Mar 2025](https://sj.jst.go.jp/news/202503/n0304-01n.html); [New Atlas](https://newatlas.com/robotics/biohybrid-hand-tissue/)
- Original xenobot design paper: Kriegman et al., PNAS 117:1853 (2020) [TK; also in prior notes] — [doi:10.1073/pnas.1910837117](https://doi.org/10.1073/pnas.1910837117)
- Bioinspired and biohybrid soft robots review (BUAA) [PR] — [BUAA portal](https://research.buaa.edu.cn/en/publications/bioinspired-and-biohybrid-soft-robots-principles-and-emerging-tec/)

**Taxonomy table (micro / medical)**

| Subcategory | Materials | Actuation | Example metric | Maturity [INF] | AI/ML |
|---|---|---|---|---|---|
| Magnetic micro/millirobots | NdFeB or ferromagnetic particles in silicone/PDMS; magnetic hydrogels | External magnetic torque/force | Jumping achieved where intuitive design failed (Nature Comms 2025) | Lab / preclinical | NN + simulation co-design; RL control |
| Light-driven microrobots | Photo-responsive LCE | Structured light | Not retrieved | Lab | GP-BO gait learning |
| Biohybrid, cell-based | Frog cells (xenobots); mouse or human skeletal muscle with scaffolds | Cilia; muscle contraction under electrical stimulation | Replication ~4 generations (AI shape); human-muscle hand fatigues after 10 min | Lab | Evolutionary/AI morphology (xenobots); computational co-design (ETH) |
| Catalytic micromotors | Pt/Janus particles, Mg/Zn (TK) | Chemical propulsion | Not retrieved | Lab | None found |
| Biodegradable / biocompatible | PLGA, silk, gelatin | Various | See Q6 | Lab | See Q6 |

### Inferences
- [INF] Biohybrid robotics is moving from hand-designed shapes (Tokyo 2025) to computational co-design of tissue and scaffold (ETH 2026), following xenobots' AI-morphology approach. Living-material variability makes data-efficient methods (BO, active learning) a natural next step, but none was found applied to tissue formulation.

### Gaps
- No ML-designed catalytic micromotors were found (search returned only xenobots).
- No ML studies were found for PLGA, silk or gelatin microrobot formulations, or for biodegradation-rate prediction in medical robots.
- No Max Planck IS 2025–2026 ML-for-microrobot-material work was found beyond the 2025 Nature Communications paper.

---

## Q6. Sustainable/biodegradable soft-robot materials

### Takeaway
Gelatin-glycerol biogels and biodegradable electrohydraulic actuators perform comparably to non-degradable ones. One abstract reports operation up to 200 V/µm and >100,000 cycles; another write-up says >330,000 cycles, and the attribution is unclear. SNU reported a soft robot whose electronics also degrade (Nature Sustainability, Mar 2026). For ML, there is a 2026 Springer review, and FEM modelling of biodegradation agrees with measurement to R² 0.997. A direct ML design of a biodegradable actuator with numbers was not found.

### Cited Findings
- **Gelatin-glycerol pneumatic bending actuator under biodegradation** (Frontiers in Robotics and AI, 2021). Performance falls as degradation progresses; FEM with measured material data agrees at R² up to 0.997 [PR] — [Frontiers 10.3389/frobt.2021.760485](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.760485/full)
- **Cycle counts: conflicting attribution.**
  - The search summary attributes "up to 200 V/µm, comparable to non-degradable counterparts, >100,000 cycles" to a Baumgartner-linked Nature Materials abstract.
  - A press write-up quotes ">330,000 cycles without failure."
  - [INF/TK]: The 330,000-cycle figure most likely belongs to Baumgartner et al., Nature Materials 19:1102 (2020), gelatin biogel pneumatic actuators ([doi:10.1038/s41563-020-0699-3](https://doi.org/10.1038/s41563-020-0699-3)).
  - The 200 V/µm and >100,000-cycle figures most likely belong to Rumley et al., "Biodegradable electrohydraulic actuators for sustainable soft robots," Science Advances (2023), MPI-IS Robotic Materials (Keplinger).
  - The writer must verify which number goes with which paper.
  - Sources: [MPI-IS Robotic Materials, Rumley 2023](https://rm.is.mpg.de/publications/rumley23-scia-biodegradable); [Syfy Wire on the edible biogel](https://www.syfy.com/index%2Ephp/syfy-wire/biodegradable-robot-made-of-food-safe-ingredients); [3D Printing Industry](https://3dprintingindustry.com/?p=203716)
- **SNU (Prof. Kang Seung-kyun).** A soft robot whose electronics also biodegrade, returning "to soil after completing its mission," published online 5 March in Nature Sustainability (2026 per Asiae, 13 Mar 2026) [PRESS] — [Asiae English, Mar 2026](https://view.asiae.co.kr/en/article/2026031309094463564)
- **ML review.** ML for biodegradable soft-robot materials (Discover Materials, 2026) is in the prior notes and not repeated — [Springer s43939-026-01059-7](https://link.springer.com/article/10.1007/s43939-026-01059-7)
- A sustainable robotic materials characterization + FEM-under-biodegradation record [PR] — [DOAJ via UMC](https://busca.umc.cl/Record/oai:doaj.org-article:e6c8427133b84a1ca3f5012c868dedcc/Description?lng=en)

### Inferences
- [INF] Modelling of biodegradable actuators is still physics/FEM-based (R² 0.997). ML-driven formulation of degradation rate versus performance appears to be at the review/proposal stage.

### Gaps
- No quantified ML-designed biodegradable actuator was found. Silk/PLGA soft-robot ML is also absent.

---

## Q7. Cross-cutting: which AI/ML methods map to which material class (with the prior notes' gaps resolved)

### Takeaway
Four status points:
- **BO/active learning** covers TCP fibers, hydrogel formulation, self-healing PU (20 experiments) and LCE microrobot gaits. LCE material BO is still missing.
- **PINNs** exist only for DE generators and DEA hybrid models.
- **Closed-loop SDLs** for robot materials have arrived but are early (DEA lifetime platform 2026, PNIPAM frugal twin 2025, BU 25,000-experiment structures).
- **Institutions** found: SNU (multimodal tactile, biodegradable robot), POSTECH (pneumatic and hydrogel actuators, no ML), ETH (computational biohybrid, learned co-design), Harvard (Bertoldi NN-accelerated evolution strategy, xenobots via Wyss), Tsinghua (3D e-skin with deep learning), Tokyo (biohybrid hand, no ML).

### Cited Findings
**Method ↔ material class map**

All rows are sourced in Q1–Q6.

| AI/ML method | Material classes, with quantified examples |
|---|---|
| Bayesian optimization / active learning | TCP fibers: 62/1,089 samples (prior notes). PAAm/alginate hydrogel (Q1). Self-healing PU: 20 experiments, R² > 0.8, NSGA-III (Q4). LCE microrobot gait via GP-BO (Q1/Q5) |
| Supervised composition→property regression | NiTi/NiTiHf: MAE 14.8 °C, 7.2 °C, 0.36% (Q1). ML-discovered alloy with Af 403.5 °C |
| NN surrogate + evolutionary/gradient inverse design | Magnetic composites: ~1.5×10⁷ simulation evaluations (Q1). 4D-printed voxel plates: ResNet (Q4). Bertoldi metamaterials: NN-accelerated evolution strategy (Q4). DEA electrodes: NN + GA (Q1) |
| Generative models (GAN, autoencoder, diffusion, graph) | Hydrogel composites via GAN (Q1). SMP lattices via cGAN (Q1). Kirigami via supervised autoencoder (Q4). Diffusion and GraphMetaMat in prior notes |
| Physics-informed ML | DEA hybrid NN, <5% error versus FEM (Q1). PINN for DE tubes (Q1) |
| Self-driving labs | DEA lifetime robot platform, 2026 PRE. PNIPAM LCST frugal twin. BU >25,000 experiments. Polybot electronic polymers (Q1/Q3/Q4) |
| RL / differentiable co-design | Magnetic microrobot RL control (Q5). ETH learned shape/material/actuation embedding (Q1). Xenobot AI morphology (Q5) |
| ML signal decoding | EGaIn glove ~97.3% (RF). Triboelectric 98–99%. Tsinghua 3D e-skin (Q2) |

**Institution coverage (gap-filling from the prior notes)**

| Institution | Work found (date) | ML for materials? |
|---|---|---|
| SNU | Ko group multimodal tactile sensor (Nature Materials 2025, aggregator only); Kang group biodegradable soft robot (Nature Sustainability, Mar 2026) | Decoding possibly; material design not shown |
| POSTECH | Myosin-inspired pneumatic skin actuator (Nature Comms 2025); D.S. Kim water-driven hydrogel actuator | No |
| ETH Zurich | Biohybrid muscle-scaffold computational design (Nature Comms 17:10732, 2026); Katzschmann learned co-design embedding (arXiv Mar 2026) | Computational co-design; ML status unclear |
| Harvard (SEAS/Wyss) | Bertoldi NN-accelerated evolution strategy (Adv. Mater. 2022); xenobot replication (Wyss news 2021) | Yes |
| Tsinghua | Zhang Yihui 3D e-skin with deep learning (Science 2024) | Decoding |
| U. Tokyo | Takeuchi biohybrid hand (Sci. Robotics, Feb 2025) | No |
| MPI-IS | Sitti data-driven magnetic soft materials (Nature Comms 2025); LCE microrobot BO (2018); biodegradable HASEL (Rumley 2023) | Yes |

### Inferences
- [INF] The "ML designs the material" claim is strongest where a validated simulator exists (magnetics, 4D printing, metamaterials). It is weakest for chemically complex, slow-to-test systems (LCE chemistry, hydrogels, ionic EAPs, biodegradables), which is where SDLs are now starting.
- [INF] Among East Asian institutions, the published pattern pairs novel materials with ML *decoding or control* rather than ML *materials discovery*. KAIST's AI-formulated elastomer (prior notes) is the main exception.

### Gaps
- No closed-loop SDL was found that both **synthesizes** and tests a robot actuator material end to end. The DEA platform automates testing only; fabrication is planned.
- MIT, CMU and Stanford-Bao ML-for-soft-material items were not searched this session because of the tool budget.

---

## 접근 상태 로그

| Host | Result | What was being retrieved |
|---|---|---|
| Local filesystem (`/root/.claude/skills/.../researcher.md`) | success | Research instructions |
| Local filesystem (`research_notes/로봇 분야 소재공학 AI 도입/robot_materials_design.md`) | success | Prior notes, read to avoid duplication |
| WebSearch tool (search engine backend) | success (21 queries) | All snippets/abstracts cited above |
| arxiv.org | **error: DNS `getaddrinfo ENOTFOUND`** (outside the session's allowed network domains) | Full text of 2602.20963 (DEA self-driving lab): sample counts and lifetime numbers |
| www.ncbi.nlm.nih.gov | **error: DNS `getaddrinfo ENOTFOUND`** (outside the session's allowed network domains) | PMC11422183 full text (BO of PAAm/alginate hydrogel): iterations and property values |
| pubs.rsc.org | **error: DNS `getaddrinfo ENOTFOUND`** (outside the session's allowed network domains) | Chem. Sci. 2026 d5sc07752d full text (self-healing PU active learning): best tensile strength and healing efficiency |

All other hosts in the citations (mdpi.com, nature.com, springer.com, ntrs.nasa.gov, eurekalert.org, mpg.de, wyss.harvard.edu and others) appeared **only as search results and were NOT fetched**. No other fetch was attempted after three DNS failures, per the session's network guidance. To verify the full texts, the user would need to allow arxiv.org, www.ncbi.nlm.nih.gov and pubs.rsc.org in the session's network settings.
