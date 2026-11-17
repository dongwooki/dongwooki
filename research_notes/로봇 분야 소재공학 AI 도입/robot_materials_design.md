# AI-Driven Materials Design for Robots (Robotics Hardware Materials Science)

Notes compiled 2026-11-17. Scope: AI/ML used to discover, design and optimize materials for robots (soft actuators, e-skin, self-healing, metamaterials, structural/lightweight materials, magnets, batteries, morphology–material co-design).
Evidence labels used below: **[PR]** = peer-reviewed paper/conference; **[PRESS]** = university/company press release or news coverage; **[MKT]** = market-research/industry claim; **[BLOG]** = blog/secondary, low confidence; **[TK]** = from background knowledge, URL given but NOT re-fetched/verified in this session (report writer should treat as lower confidence or verify).

---

## Q1. Which AI methods are used for robot-materials design?

### Takeaway
The toolkit spans (a) surrogate-model + optimizer loops (NN/ensemble regressors + Bayesian optimization, evolution strategies, genetic algorithms) for actuator/elastomer formulations; (b) generative models (diffusion, graph VAEs, graph-growth generators) for metamaterials and whole robot bodies; (c) differentiable simulation and evolutionary/RL co-design of body + controller; and (d) foundation-scale crystal discovery models (GNoME, MatterGen) that matter mostly indirectly (batteries, magnets). Bayesian optimization applied specifically to LCE actuators appears to be a thin/open area.

### Cited Findings
- **Bayesian optimization (discrete BO / active learning)** for thermally activated coiled polymer actuators: reached an actuation strain of 1.25 after fabricating only 62 of 1,089 possible processing combinations (Materials & Design, 2025) [PR] — [Aalto Research Portal](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat/); [TUM portal](https://portal.fis.tum.de/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat/)
- **Surrogate ML for LCE inverse design** (Kent State group): 1,500 FEM forward simulations used to train a stacked-ensemble regressor (AutoGluon) mapping nematic director fields to heated target shapes; APS March Meeting abstracts 2022/2023, full paper "in preparation" at the time [conference abstract] — [APS MAR 2023 B14.1](https://meetings-archive.aps.org/mar/2023/b14/1); [APS MAR 2022 K21.6](https://meetings-archive.aps.org/mar/2022/k21/6)
- **Neural network + evolution strategies** used for precise inverse design of stress–stretch responses of LCE-based smart mechanical metamaterials (Applied Mathematics and Mechanics, 2025) [PR] — [BUAA research portal](https://research.buaa.edu.cn/zh/publications/inverse-design-of-smart-mechanical-metamaterials-based-on-liquid-/)
- **Genetic algorithms** for design optimization of magneto-active elastomer (MAE) unimorph actuators [PR] — [NSF PAR 10710628](https://par.nsf.gov/biblio/10710628-design-optimization-magneto-active-elastomer-mae-unimorphs-using-genetic-algorithms)
- **ML forward-prediction + inverse design of magnetic soft cantilevers** trained on deformation-simulation data; inverse model R² = 0.9490 (Int. J. Mechanics and Materials in Design, 2025) [PR] — [Springer](https://link.springer.com/article/10.1007/s10999-025-09773-5)
- **Denoising diffusion models** for inverse design of inflatable structures with programmable deformations (arXiv 2508.13097, Aug 2025) [preprint] — [arXiv](https://arxiv.org/pdf/2508.13097)
- **Neural operators** for shape-morphing programming of soft materials on complex geometries (arXiv 2601.11126, Jan 2026) [preprint] — [arXiv](https://arxiv.org/pdf/2601.11126)
- **Generative + uncertainty-informed inverse design (GUIDe)** for on-demand nonlinear functional responses (arXiv 2509.05641, Sep 2025) [preprint] — [arXiv](https://arxiv.org/pdf/2509.05641)
- **Graph-based generative design of metamaterials:** GraphMetaMat (UC Berkeley, Marco Maurizi / Xiaoyu Rayne Zheng; Nature Machine Intelligence cover, July 2025) builds 3D truss metamaterials as graphs from scratch, iteratively adding nodes/edges to hit a target stress–strain curve while accounting for manufacturing/defect constraints [PR + PRESS] — [Berkeley Engineering news, Jul 2025](https://engineering.berkeley.edu/news/2025/07/a-smarter-approach-to-designing-metamaterials/)
- **Graph VAE** latent space for truss lattices covering nonlinear behavior (Nature Communications, 2023) [PR] — [Nature Communications s41467-023-43217-y](https://www.nature.com/articles/s41467-023-43217-y)
- **GNNs** for predicting deformation mechanisms/properties of architected lattices; >90% accuracy on an unseen complex-lattice dataset (arXiv 2202.09427, 2022) [preprint] — [arXiv](https://arxiv.org/pdf/2202.09427)
- **ML of implicit combinatorial rules** in mechanical metamaterials (arXiv 2202.03049) [preprint/PR] — [arXiv](https://arxiv.org/pdf/2202.03049)
- **Diffusion + differentiable-physics co-design of body & controller:** DiffuseBot (MIT CSAIL, Tsun-Hsuan Wang, Chuang Gan, Daniela Rus et al.; NeurIPS 2023 oral) augments diffusion sampling with differentiable soft-body simulation; pipeline = "robotizing" diffusion samples → embedding optimization → "diffusion-as-co-design" guided by task gradients; tested on balancing, landing, crawling, hurdling, gripping, moving objects; physical proof-of-concept built [PR] — [NeurIPS 2023 proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8b1008098947ad59144c18a78337f937-Abstract.html); [arXiv 2311.17053](https://arxiv.org/pdf/2311.17053)
- **Gradient-based "instant evolution":** Northwestern (Sam Kriegman) AI designed a walking soft robot from a shapeless block in ~26 s on a laptop (PNAS, 3 Oct 2023) [PR + PRESS] — [ScienceDaily, Oct 2023](https://sciencedaily.com/releases/2023/10/231003173425.htm); [UVM News](https://www.uvm.edu/news/story/instant-evolution-ai-designs-robots-scratch-seconds-and-they-walk)
- **Topology optimization + learning-based inverse design** identified as a key approach in a 2025 review of soft-robot morphological design (The Innovation Informatics, 2025) [PR] — [The Innovation (PDF)](https://www.the-innovation.org/data/article/informatics/preview/pdf/TII-2025-0022.pdf)
- **ML inverse-design taxonomy:** exploration-based, model-based, and optimization-based inverse design (Computers, Materials & Continua review, Feb 2025) [PR] — [ResearchGate](https://www.researchgate.net/publication/388024287_Machine_Learning-Based_Methods_for_Materials_Inverse_Design_A_Review)
- **Foundation-scale crystal discovery:** GNoME (Google DeepMind, Nature, Nov 2023) found 2.2 million crystal structures, ~381,000 predicted stable; external labs synthesized 736; Berkeley A-Lab (autonomous robotic lab) made 41 GNoME-predicted materials in 17 days [PR + PRESS] — [Nature s41586-023-06735-9](https://www.nature.com/articles/s41586-023-06735-9); [MIT Technology Review, 29 Nov 2023](https://www.technologyreview.com/2023/11/29/1084061/deepmind-ai-tool-for-new-materials-discovery)
- **MatterGen** (Microsoft) is a diffusion-based generative model for inorganic crystals, described as the first instance of generative-AI-enabled discovery of a new material [preprint citing it] — [arXiv 2604.14082](https://arxiv.org/pdf/2604.14082.pdf); original paper (Nature, Jan 2025) [TK] — [Nature s41586-025-08628-5](https://www.nature.com/articles/s41586-025-08628-5)
- **Evolution Gym** (MIT, NeurIPS 2021) is the standard voxel soft-robot benchmark for co-optimizing body + controller via evolution + RL [TK] — [arXiv 2201.09863](https://arxiv.org/abs/2201.09863)

### Inferences
- In robot-materials work, the AI is usually applied at the **structure/formulation/morphology** level (director fields, lattice topology, elastomer recipes, body shape) rather than at the atomic-crystal level; crystal-scale foundation models (GNoME/MatterGen) touch robotics mainly through batteries and magnets.
- The method mix tracks data scarcity: small experimental datasets → BO/active learning; cheap simulators → surrogate NN + evolutionary/gradient search; differentiable simulators → diffusion-guided or gradient co-design.

### Gaps
- No peer-reviewed paper found (in this session) applying Bayesian optimization directly to LCE actuator fabrication with quantified gains; appears to be an open area or simply not surfaced.
- Physics-informed neural networks (PINNs) specifically for robot-material design were not surfaced in searches; no citable example.
- The 2025 Nature Communications paper "Data-driven design of shape-programmable magnetic soft materials" was seen only as a reference-list title; abstract/numbers not retrieved.

---

## Q2. Concrete examples with quantified results (by material class)

### Takeaway
Quantified AI-for-robot-materials results exist mainly in academic prototypes: AI-optimized printable elastomers (>6x stretch, KAIST), 41% higher jumps from diffusion-redesigned linkages (MIT 2025), 26-second evolved walking robots (Northwestern 2023), BO-optimized polymer actuators (62/1,089 experiments), and graph-generative metamaterials (Berkeley 2025). AI-designed rare-earth-free magnets (MagNex) are company claims without independent performance data.

### Cited Findings
**Soft actuators / artificial muscles / elastomers**
- KAIST–KIST–Seoul Tech team used AI to find the optimal formulation of a DLP-3D-printable, rubber-like stretchable material; it printed stably and stretched >6x its original length without tearing; published in Nature Communications; a soft robotic hand made from it gently grips objects from eggs to a 1 kg water bottle (2025) [PR + PRESS] — [AlphaGalileo (KAIST release)](https://www.alphagalileo.org/en-gb/Item-Display/ItemId/277480)
- Coiled thermally activated polymer actuators: BO found actuation strain 1.25 with 62/1,089 samples (2025) [PR] — [Aalto](https://research.aalto.fi/en/publications/data-efficient-optimization-of-thermally-activated-polymer-actuat/)
- Magnetic soft cantilever inverse-design model R² = 0.9490 (2025) [PR] — [Springer](https://link.springer.com/article/10.1007/s10999-025-09773-5)
- KAIST (Hong Chul Moon group) "Ionograsper" ionic soft material that both senses and actuates (Advanced Materials); team said it plans to couple it with AI control for "physical AI" robots (2025) [PR + PRESS; AI coupling is a stated plan, not a result] — [Newswise](https://www.newswise.com/articles/kaist-develops-a-venus-flytrap-inspired-robot-hand-material-that-senses-objects-and-grasps-them-under-light); [Dailian (Korean)](https://www.dailian.co.kr/news/view/1695943)
- KAIST (Jung Kim, Inkyu Park) real-time shape-programmable "robot sheet" (Nature Communications) [PR + PRESS] — [Kukinews (Korean)](https://www.kukinews.com/article/view/kuk202508060169)
- Self-healing artificial muscle: University of Nebraska–Lincoln three-layer actuator (damage-sensing skin, self-healing thermoplastic elastomer middle layer, heat-reprocessed to seal damage); ICRA 2025 Best Paper finalist [PR + PRESS] — [UNL NCMN news](https://ncmn.unl.edu/news/husker-engineers-advance-work-intelligent-self-healing-technology/)

**Whole-body / morphology–material co-design**
- Northwestern "instant evolution" (PNAS, Oct 2023): walking design in ~26 s on a laptop; resulting three-legged body with dorsal fins and internal holes; 3D-printed mold cast in silicone and it walked (actuated pneumatically) [PR + PRESS] — [ScienceDaily](https://sciencedaily.com/releases/2023/10/231003173425.htm); [Euronews, 16 Oct 2023](https://www.euronews.com/2023/10/16/researchers-in-the-us-have-trained-ai-to-design-a-robot-from-scratch); [GovTech](https://www.govtech.com/education/higher-ed/northwestern-universitys-ai-designs-a-new-robot-in-seconds)
- MIT CSAIL diffusion-redesigned jumping robot (ICRA 2025; news June 2025): 500 initial designs, top performers refined over 5 rounds; AI produced curved "drumstick" linkages that store more energy; robot jumps ~2 ft, ~41% higher than the human-designed version; redesigned foot gave an 84% improvement in landing (falling far less) [PR + PRESS] — [MIT Schwarzman College of Computing](https://computing.mit.edu/news/using-generative-ai-to-help-robots-jump-higher-and-land-safely/); [Robotics & Automation News, 16 Jun 2025](https://roboticsandautomationnews.com/2025/06/16/mit-research-using-generative-ai-to-help-robots-jump-higher-and-land-better/92166)
- DiffuseBot (NeurIPS 2023): outperformed comparable approaches across six tasks; physical proof-of-concept [PR] — [arXiv 2311.17053](https://arxiv.org/pdf/2311.17053)
- Xenobots (Kriegman, Blackiston, Levin, Bongard; PNAS 2020): evolutionary algorithm designed reconfigurable organisms from frog cells — the canonical "AI-designed living materials robot" [TK] — [PNAS 10.1073/pnas.1910837117](https://www.pnas.org/doi/10.1073/pnas.1910837117)

**Metamaterials / architected lattices**
- GraphMetaMat (Nature Machine Intelligence, Jul 2025): inverse-designs 3D truss metamaterials to target stress–strain curves with manufacturability constraints [PR + PRESS] — [Berkeley Engineering](https://engineering.berkeley.edu/news/2025/07/a-smarter-approach-to-designing-metamaterials/)
- NSF grant "ACED: Redefining the Design of Mechanical Metamaterials via Generative Models" — project description, not results [grant] — [NSF 2435905 summary](https://api.ai-analytics.org/grant/nsf/2435905.md)
- Growth-inspired graph generation for inverse design of mechanical lattices (2026 listing) [preprint/listing] — [roboticscenter.ai](https://www.roboticscenter.ai/research/papers/growth-inspired-graph-generation-and-inverse-design-of-mechanical-lattices-via-dot-matrice-2609)

**Motor magnets (rare-earth-free)**
- Materials Nexus (UK) AI platform screened >100 million candidate compositions to pick rare-earth-free magnet "MagNex" (with University of Sheffield & Henry Royce Institute), development in ~3 months (claimed ~200x faster); claimed ~20% of rare-earth magnet material cost and ~70% lower material carbon emissions; no published magnetic performance comparison and no robot-motor deployment found (mid-2024) [PRESS, company claims] — [New Atlas](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery/); [Assembly Magazine](https://www.assemblymag.com/articles/98582-ai-helps-company-develop-permanent-magnet-without-rare-earths); [Xataka On](https://www.xatakaon.com/robotics-and-ai/ai-has-designed-a-magnet-without-rare-earth-elements-in-just-three-months-whats-coming-next-is-staggering)
- Niron Magnetics (iron nitride, rare-earth-free) described as >10 years in R&D and "not quite ready" (non-AI route, for context) [PRESS] — [New Atlas](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery/)

**Battery / energy materials**
- GNoME produced 25x more potential solid lithium-ion conductors than previous studies (Nov 2023) [PRESS citing PR] — [VentureBeat](https://venturebeat.com/ai/google-deepminds-materials-ai-has-already-discovered-2-2-million-new-crystals/); [Nature](https://www.nature.com/articles/s41586-023-06735-9)
- "Dual AI" approach for solid-state battery material development (news) [PRESS] — [eeNews Europe](https://www.eenewseurope.com/en/dual-ai-boost-for-solid-state-battery-material-development)

**Biodegradable soft-robot materials**
- Springer review (late Oct/Nov 2026) on ML for biodegradable soft-robot materials covering inverse design, multitask learning, closed-loop optimization [PR] — [Discover Materials s43939-026-01059-7](https://link.springer.com/article/10.1007/s43939-026-01059-7)

### Inferences
- The strongest quantified wins are at the **component/morphology** level (linkage geometry, body shape, elastomer recipe); headline "AI-discovered material" claims (MagNex) remain company-reported and unverified for robotics use.
- Korean groups (KAIST) are visible in AI-assisted formulation and in "physical AI" sensing–actuation materials, but most Korean items found pair novel materials with AI control rather than AI-driven materials discovery.

### Gaps
- No verified data on AI-optimized humanoid hand materials (e.g., Tesla Optimus hand tendons/skins) — not found.
- No 2024–2026 quantified ML-optimized LCE actuator result found; no hydrogel- or SMA/SMP-specific ML design example with numbers retrieved in this session.
- SNU, POSTECH, Tsinghua, Tokyo, ETH, Harvard Wyss AI-materials-for-robots works not surfaced with verifiable details (POSTECH muscle-protein-inspired actuator seen only via a Russian-language aggregator; not verified — [Habr](https://habr.com/ru/articles/934188)).
- MagNex performance (remanence, coercivity, energy product) vs NdFeB not published in sources found.

---

## Q3. How AI helps material-embedded sensing and data interpretation (e-skin, neuromorphic)

### Takeaway
ML is now the default way to decode multimodal and sparse e-skin signals: multimodal (thermal + mechanical) fusion raised object/material classification from ~65% to 95% in a 2025 Nature Materials e-skin; learned models localize touch to ~mm precision and enable self-healing skins to re-calibrate after damage via transfer learning. Neuromorphic/memristive nanowire skins are emerging.

### Cited Findings
- Nature Materials (2025, DOI 10.1038/s41563-025-02373-w): multimodal thermal + mechanical e-skin; ML classification accuracy rose from ~65% (single modality) to 95% (combined); 94.53% with reduced inputs; fingertip version with wireless board identified 20 everyday objects at 83% accuracy; coverage also links the DOI to a memristive nanowire network on a skin replica [PR via news summaries; full text not opened] — [ElectronicsForU](https://www.electronicsforu.com/news/artificial-skin-enables-human-like-robotic-sensing)
- SuperTac biomimetic multimodal tactile sensor (Nature Sensors, Jan 2026): force accuracy 0.06 N, position accuracy 0.4 mm, temperature range 0–90 °C [PR via search summary] — [ElectronicsForU](https://www.electronicsforu.com/?p=194182)
- Science Robotics e-skin (2025) that works as a single unified sensor across its whole surface, interpreted by an ML model trained on test data; robots "feel heat, pain and pressure" (no accuracy figure in coverage) [PR via PRESS] — [HospiMedica](https://mobile.hospimedica.com/critical-care/articles/294805573/highly-sensitive-electronic-skin-allows-robots-to-feel-heat-pain-and-pressure.amp.html)
- Electrical impedance tomography (EIT) finger-shaped soft artificial skin with ML predicting press location and force (IEEE RA-L) [PR] — [UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10207446/1/Electrical_Impedance_Tomography_Based_Finger-Shaped_Soft_Artificial_Skin.pdf)
- ML-based multi-point load sensing for smart skins from sparse strain data (Advanced Materials Technologies, 2025) [PR] — [Stony Brook Research Connect](https://researchconnect.stonybrook.edu/en/publications/machine-learningbased-multi-point-load-sensing-for-smart-skins/)
- DexSkin: high-coverage conformable robotic skin for learning contact-rich manipulation (arXiv) [preprint] — [AITopics](https://aitopics.org/doc/arxivorg:0B3C9830)
- Self-healing sensing skin + learning: five-layer networks after 5,000 probes gave touch localization of 2.3 mm and 95% depth accuracy; transfer learning with one frozen layer re-adapted after damage with <200 probes (Advanced Intelligent Systems, Dec 2022) [PR] — [DOAJ](https://doaj.org/article/155864cd4bf640578c0d35a1cfcecc8d); [Cambridge Engineering](https://www.eng.cam.ac.uk/node/5147)
- Rapidly self-healing e-skin (Science Advances, Feb 2025): ~80% functional recovery within 10 s, used for real-time muscle-strength analysis and AI-based fatigue detection [PR, author claim] — [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:149873d8-5227-4cbb-a6f8-5dc61f397e9d)
- SHERO EU project (Cambridge, Empa, ESPCI; ~€3M): self-healing soft robots using ML for damage detection, localization and controlled healing [PRESS] — [The Robot Report](https://www.therobotreport.com/machine-learning-self-healing-soft-robotics/); [Lab Manager](https://www.labmanager.com/self-healing-robots-that-feel-pain-1264)
- Multilayered e-skin that autonomously heals and realigns (WashU, 2023) [PRESS] — [WashU Engineering](https://engineering.wustl.edu/news/2023/Multilayered-electronic-skin-can-autonomously-heal-and-realign.html)

### Inferences
- Value of ML in e-skin is largely **sensor fusion and decoding of cheap/sparse/continuous sensing layers** (EIT, single-sheet skins), which lowers wiring and material complexity — a materials-design lever as much as a software one.
- Self-healing + ML recalibration is a coherent pairing: healing restores material, learning restores signal mapping.

### Gaps
- Exact Science Robotics 2025 e-skin authors/metrics not retrieved; Nature Materials paper full text not opened (figures from news).
- No concrete neuromorphic-material (memristive skin) performance numbers beyond the mention above.

---

## Q4. Industry relevance: humanoid robot boom and its materials demands; AI-driven materials work tied to it

### Takeaway
Humanoid makers' binding materials constraints in 2025–2026 are NdFeB rare-earth magnets (~3.5–4 kg per humanoid), precision reducers (harmonic/cycloidal/planetary; 24–36 months to add capacity), lightweight structures (PEEK, CF-PEEK, Mg/Al alloys), sensors and batteries. Tesla tied Optimus output to China's magnet export controls in 2025. Direct AI-driven materials programs from humanoid companies were NOT found publicly; the AI-materials link runs through startups (Materials Nexus) and general platforms (GNoME/MatterGen).

### Cited Findings
- Adamas Intelligence calls NdFeB magnets the greatest hurdle for robotics; Elon Musk said on Tesla's Q1 2025 earnings call that Optimus production was limited by China's rare-earth magnet export controls [MKT + company statement] — [Adamas Intelligence](https://www.adamasintel.com/humanoid-robots-and-the-future-of-motors-and-ndfeb-markets/)
- Industry estimates: ~3.5–4 kg rare-earth permanent magnets per humanoid [MKT] — [Meticulous Research](https://www.meticulousresearch.com/meticulous-next/humanoid-robot-components-outlook-2026-2036); [Metalnomist (UBTech), Jun 2026](https://www.metalnomist.com/2026/06/ubtech-humanoid-robot-ubtech-humanoid.html); [Metalnomist (Xiaomi), May 2026](https://www.metalnomist.com/2026/05/xiaomi-humanoid-robots-signal-new-rare.html)
- Precision reducer capacity takes 24–36 months to expand; harmonic, cycloidal, planetary reducers; Chinese localization cited as enabler; Meticulous base case puts inflection ~2031, sensitive to rare-earth policy; notes a rare-earth export-control suspension expiring 10 Nov 2026 (status after that date NOT verified) [MKT] — [Meticulous Research](https://www.meticulousresearch.com/meticulous-next/humanoid-robot-components-outlook-2026-2036)
- Patent analysis: Schaeffler and NTN lead cycloidal-reducer patents [MKT] — [PatSnap / Evidence Engineering, 2026](https://www.patsnap.com/resources/blog/articles/humanoid-robots-in-2026-chips-are-5-of-the-problem/)
- S&P Global (Feb 2026): robot rise could be slowed by metals shortage [MKT] — [S&P Global Market Intelligence](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/2/robot-rise-could-be-slowed-by-metals-shortage-98483872)
- IDTechEx "Materials for Humanoid Robots 2026–2036": analyzes >50 humanoid products/prototypes; 10-year demand forecasts by material (steel, aluminum, magnesium alloys, rare-earth magnets, engineering plastics such as PEEK and PC-ABS); expects 2026–2027 to be key transition years from pilot to production [MKT] — [IDTechEx Humanoid Robots 2026–2036](https://idtechex.com/en/research-report/humanoid-robots/1149); [Industry Europe (IDTechEx actuators article)](https://industryeurope.com/sectors/technology-innovation/trends-and-outlook-for-actuators-the-muscles-behind-humanoid/); [Robotics & Automation News, 30 Jul 2026](https://roboticsandautomationnews.com/2026/07/30/trends-and-outlook-for-actuators-the-muscles-behind-humanoid-motion/103750/)
- PEEK: ~half the density of Al alloy; claims that replacing Al with PEEK cuts skeleton weight ~40%; PEEK ~30x the cost of Mg alloy → tiered use; claim that Optimus Gen2 shed 10 kg (largely PEEK) and walked 30% faster; Mg–Al alloys possibly in Optimus Gen3 — all from blogs, NOT confirmed by Tesla [BLOG] — [PEEK China blog, May 2025](https://peekchina.blogspot.com/2025/05/exploring-lightweight-materials-in.html); [PEEK China blog, Dec 2024](https://peekchina.blogspot.com/2024/12/why-peek-is-key-material-for-teslas.html); [Brewminate](https://brewminate.com/peek-carbon-fiber-composites-are-driving-the-humanoid-robot-lightweighting-wave/)
- Goodfellow overview of advanced materials for humanoids [industry] — [Goodfellow](https://www.goodfellow.com/usa/resources/advanced-materials-for-humanoid-robots/)
- China's Lens Technology expanding humanoid-robot capacity (Argus) [PRESS] — [Argus Media](https://www.argusmedia.com/de/news-and-insights/latest-market-news/2756805-china-s-lens-to-expand-humanoid-robot-capacity)
- AI rare-earth-free magnets (MagNex) positioned for robotics/drones/EVs but no robot-motor adoption found [PRESS] — [New Atlas](https://newatlas.com/materials/ai-rare-earth-free-magnet-discovery/)

### Inferences
- The magnet bottleneck makes AI-accelerated rare-earth-free/reduced-Dy magnet discovery the most commercially direct "AI materials → humanoid" link; GNoME/MatterGen-class tools plus autonomous labs (A-Lab) are the plausible pipeline, but no humanoid OEM has publicly tied itself to one.
- Lightweighting choices (PEEK vs Mg vs Al) are cost-driven trade-offs well suited to multi-objective BO/topology optimization, though no OEM-published AI case was found.

### Gaps
- No public AI-driven materials programs found for Tesla Optimus, Figure, Unitree, Boston Dynamics/Hyundai, Samsung/Rainbow Robotics, UBTech or Xiaomi.
- Goldman Sachs / Morgan Stanley humanoid materials figures not retrieved this session.
- Battery chemistry choices for humanoids (cell format, energy density targets) not retrieved.
- Status of China's rare-earth export-control suspension after 10 Nov 2026 not verified.

---

## Q5. 2024–2026 progress and review papers summarizing the field

### Takeaway
2025 brought several framing reviews ("physical intelligence" in soft robots in Science Robotics; a mechano-intelligence roadmap; morphological design reviews) and a shift from GA/evolution to diffusion/graph generative models and differentiable co-design (DiffuseBot 2023 → MIT jumping robot 2025 → GraphMetaMat 2025 → neural-operator/diffusion preprints 2025–2026). Reviews agree most soft robots still show only "rudimentary" physical intelligence.

### Cited Findings
- Chen et al., "Advancing physical intelligence for autonomous soft robots," Science Robotics (May 2025): most soft robots show rudimentary physical intelligence relying on manipulated external stimuli; proposes "autonomous physical intelligence" (control without artificial modulation of stimulus fields) [PR] — [Yale Faboratory PDF](https://www.eng.yale.edu/faboratory/publications\journal\2025\Chen%20-%202025%20-%20Advancing%20physical%20intelligence%20for%20autonomoussoft%20robots.pdf); [Koç University record](https://research.hub.ku.edu.tr/entities/publication/9911b69f-7545-41d0-ae62-5e27ed640210/full)
- Roadmap on embodying mechano-intelligence in functional materials and structures, Smart Mater. Struct. 34 (2025) 063501 — morphological computation, mechanical neural networks, physical intelligence in small-scale magnetic soft robots [PR] — [NSF PAR](https://par.nsf.gov/servlets/purl/10608528)
- "Physical Intelligence in Small-Scale Robots and Machines" (Advanced Materials review) [PR] — [AMOLF repository](https://ir.amolf.nl/pub/11105/17053acceptedVersion.pdf)
- Metamaterial robotics review: future = convergence of embodied intelligence and reconfigurable matter [PR] — [eScholarship](https://escholarship.org/uc/item/2b28x408)
- "Exploring Embodied Intelligence in Soft Robotics: A Review" (Biomimetics, 2024) [PR] — [PMC11047907](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11047907/)
- Morphological design methodologies of soft robots (The Innovation Informatics, 2025) [PR] — [PDF](https://www.the-innovation.org/data/article/informatics/preview/pdf/TII-2025-0022.pdf)
- ML for biodegradable soft-robot materials (Springer Discover Materials, 2026) [PR] — [Springer](https://link.springer.com/article/10.1007/s43939-026-01059-7)
- ML-based materials inverse design review (CMC, Feb 2025) [PR] — [ResearchGate](https://www.researchgate.net/publication/388024287_Machine_Learning-Based_Methods_for_Materials_Inverse_Design_A_Review)
- Timeline of key generative/co-design milestones: Xenobots PNAS 2020 [TK]; Evolution Gym NeurIPS 2021 [TK]; Northwestern instant evolution PNAS Oct 2023; DiffuseBot NeurIPS 2023; GNoME Nature Nov 2023; MagNex mid-2024 (press); MatterGen Nature Jan 2025 [TK]; MIT diffusion jumping robot ICRA/June 2025; GraphMetaMat NMI Jul 2025; diffusion inflatables (Aug 2025) and neural-operator morphing (Jan 2026) preprints — sources as cited in Q1/Q2 above.

### Inferences
- Trend line: from black-box evolutionary search (2020–2021) → gradient/differentiable and diffusion-guided co-design (2023–2025) → graph-native and operator-learning inverse design of the material architecture itself (2025–2026).
- The field's main bottleneck is the sim-to-real gap for soft/multiphysics materials and sparse experimental data, which pushes adoption of BO/active learning and autonomous labs.

### Gaps
- No single 2024–2026 review dedicated specifically to "AI for robot materials" (spanning actuators, e-skin, magnets, batteries) was found; coverage is fragmented across soft-robotics, metamaterials, and materials-informatics reviews.
- Nature Reviews Materials / Nature Machine Intelligence perspective pieces on this exact intersection not surfaced.

---

## 접근 차단/실패 사이트

- https://roboticsresear.ch/articles/34801/emerging-materials-opportunities-and-trends-in-the-humanoid-market — WebFetch 실패: `getaddrinfo ENOTFOUND roboticsresear.ch` (세션 네트워크 허용 도메인 밖이거나 DNS 해석 불가; 프록시/네트워크 정책에 의한 차단으로 추정). IDTechEx "Emerging Materials Opportunities and Trends in the Humanoid Market" 원문 본문을 확인하지 못함 → 해당 내용은 검색 스니펫과 재게재 기사로만 대체.
- 참고: 위 1건 외에는 WebFetch를 추가로 시도하지 않음(도구 호출 예산 및 차단 안내에 따라). 따라서 Nature Materials e-skin 논문(10.1038/s41563-025-02373-w), Science Robotics e-skin, IDTechEx 보고서 본문(유료), Goldman Sachs/Morgan Stanley 보고서(유료/로그인 필요 가능성) 등은 원문 미확인 상태이며 수치는 검색 요약·언론 보도 기반임.
