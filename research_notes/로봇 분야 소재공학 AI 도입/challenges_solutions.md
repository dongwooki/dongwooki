# Open Challenges, Critiques, and Proposed Solutions for AI + Robotics in Materials Science & Engineering (as of Nov 2026)

Scope: self-driving labs (SDLs), AI-driven materials discovery, and AI-designed materials for robots. Research conducted 2026-11-17. Note on method: most full-text fetches were blocked by the session's network policy (see final section), so many findings below come from search-engine extracts of abstracts/primary pages rather than full-text reading. Where a claim comes only from a secondary/aggregator source, it is flagged.

---

## Q1. Data issues (small data, positive-result bias, negative data, metadata/FAIR, sim-to-real, sharing/IP)

### Takeaway
Materials ML is constrained less by algorithms than by data: training sets are small, redundant, biased toward successful/published results, and dominated by 0 K DFT calculations that differ from experiment. The community response is FAIR infrastructure (OPTIMADE, NOMAD/FAIRmat), reporting of failed experiments, and SDLs that generate "complete" datasets including negatives — but federated/IP-preserving sharing remains immature.

### Cited Findings
- **Positive-result / human selection bias (2022):** Strieth-Kalthoff et al. (Angewandte Chemie, 2022) showed reaction-yield ML models struggle partly because failed reactions go unreported; bias traced to experimental error, chemists' planning habits, and reluctance to publish low-yield work. Their tests showed ML models tolerate measurement noise but are *strongly* affected by human selection bias. — [phys.org (Jun 2022)](https://phys.org/news/2022-06-clearer-negative-experimental-results-reaction.amp); [EurekAlert](https://www.eurekalert.org/news-releases/955739); [Chemistry World](https://www.chemistryworld.com/news/yield-predicting-ai-needs-chemists-to-stop-ignoring-failed-experiments/4015662.article)
- Chemistry World commentary argues publishing negative results is "more important than ever" for training ML in chemistry. — [Chemistry World](https://chemistryworld.com/4017017.article) (date not verified; fetch blocked)
- Analogous evidence from biomedicine (preprint, peer review unverified): NegBioDB reports that using "control" (assumed) negatives instead of confirmed negatives inflates model performance, and some models fall below random on cold-entity splits. — [NegBioDB abstract (Hugging Face)](https://huggingface.co/datasets/jang1563/NegBioDB/blob/main/paper/sections/abstract.tex)
- **Data redundancy inflates reported accuracy:** Random train/test splitting "frequently results in artificially high performance assessments due to the inherent redundancy of typical material datasets" (Omee et al., arXiv 2401.08032, 2024). — [arXiv 2401.08032](https://arxiv.org/pdf/2401.08032.pdf); [NSF PAR record](https://par.nsf.gov/biblio/10520915)
- MatFold (RSC Digital Discovery, 2025): for superconducting Tc models, leave-one-cluster-out CV showed generalizability and expected accuracy are "drastically overestimated due to data leakage in random train/test splits." — [Digital Discovery d4dd00250d](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)
- Li et al. (arXiv 2210.13597): models trained on Materials Project data show "unexpectedly acute performance degradation" on newer database entries — an excellent benchmark score may not imply generalization. — [arXiv 2210.13597](https://www.arxiv.org/pdf/2210.13597)
- **Multi-fidelity / sim-to-real data gap:** A 2026 perspective on generative design of inorganic materials states foundation models "must be trained to learn across data modalities and fidelities," and that combining low-fidelity approximations with high-fidelity calculations and experiments "requires … new approaches to uncertainty quantification and transfer learning"; also notes representing symmetry, disorder and defects remains hard. — [arXiv 2604.14082 (Apr 2026)](https://arxiv.org/pdf/2604.14082)
- Zero-temperature DFT stability hulls neglect finite-temperature effects; text-mined synthesis-recipe models generalize poorly and overestimate synthesis likelihood (from a 2026 arXiv synthesizability study, extract only). — [arXiv 2602.04075](https://arxiv.org/pdf/2602.04075)
- **FAIR infrastructure – OPTIMADE:** common API for querying materials databases; as of March 2026, 20 database providers expose OPTIMADE-compliant APIs indexing >25 million materials; the optimade-maker tool (arXiv, Mar 2026) auto-generates OPTIMADE APIs from raw simulation outputs, applied automatically on upload in the Materials Cloud Archive. — [arXiv 2603.23536 (Mar 2026)](https://arxiv.org/html/2603.23536v1); earlier OPTIMADE paper: [Cambridge TCM PDF (2024)](https://www.tcm.phy.cam.ac.uk/~gjc29/papers/OPTIMADE24.pdf)
- **FAIR infrastructure – NOMAD/FAIRmat:** NOMAD is a free public research-data-management platform that institutions can also self-host; connected installations form a federated infrastructure. NOMAD Oasis (local install) lets labs "manage their lab and share selectively" — a partial answer to IP concerns. NOMAD metainfo can be extended with OPTIMADE and other vocabularies. — [FAIRmat presentation (28 Nov 2024)](https://indico.desy.de/event/45458/contributions/178565/attachments/94106/127917/20241128_PUNCH_FAIRmat_SB.pdf); [CoRDI paper "FAIR Research Data With NOMAD"](https://doi.org/10.52825/cordi.v1i.376)
- **Standardization still a recognized gap in SDLs:** a Sept 2025 review (preprint, not peer-reviewed) lists "data standardization issues, limited data availability in unexplored chemical domains, model interpretability needs" as persistent challenges. — [Preprints.org 202509.1369](https://www.preprints.org/manuscript/202509.1369/v1)
- The 2023 community perspective "What is missing in autonomous discovery" (Digital Discovery, 2023) flags data management, storage, analysis and interpretation of data as crucial hurdles alongside hardware/software, ethics, education and community building. — [Digital Discovery d3dd00143a](https://pubs.rsc.org/en/content/articlelanding/2023/dd/d3dd00143a); [arXiv 2304.11120](https://pdf.arxiv.org/pdf/2304.11120)
- **Korea's data response (Apr 30, 2026):** MSIT's "AI소재 R&D 플랫폼 구축 전략(2026~2030)(안)" (8th Science & Technology Ministers' Meeting) expands the existing materials research data platform into a "국가소재연구데이터통합플랫폼 (provisional)" and targets "AI-Ready" datasets of 10 million records within 5 years and 50 million within 10 years. — [Daum/news (30 Apr 2026)](https://v.daum.net/v/20260430155346042); [Daum/news (30 Apr 2026)](https://v.daum.net/v/20260430101533808)

### Inferences
- The same "redundancy + leakage" problem that inflates property-prediction accuracy (MatFold, Omee et al.) also underlies novelty failures in generative/discovery claims (Q2): models are rewarded for re-finding training-set neighbors.
- SDLs are the most-cited structural fix for negative-data scarcity because a closed loop records all attempts, not just successes — but this only helps if SDL outputs are published in FAIR formats (OPTIMADE/NOMAD), which remains a coordination problem.

### Gaps
- No primary source found on federated learning applied to materials data or on concrete IP-sharing agreements (e.g., industrial consortia data trusts); searched but results only addressed NOMAD Oasis selective sharing.
- Could not verify a widely circulated "~60% of failed experiments missing from public record" figure (secondary blog only) — excluded.

---

## Q2. Critiques and controversies (A-Lab, GNoME, MatterGen, reproducibility, benchmark leakage)

### Takeaway
All three flagship 2023–2025 AI-materials results (A-Lab, GNoME, MatterGen) faced published solid-state-chemistry critiques arguing their "novel" materials were known compounds, often disordered phases misrepresented as new ordered structures. The A-Lab critique led to a Nature Author Correction (Jan 2026) that narrowed (not retracted) the novelty claims. A common methodological lesson: automated novelty checks and automated PXRD phase identification are unreliable without expert crystallographic review and disorder-aware matching.

### Cited Findings
**A-Lab (Szymanski et al., Nature, Nov 2023; Ceder group, LBNL/UC Berkeley)**
- Original paper: "An autonomous laboratory for the accelerated synthesis of novel materials." — [OSTI copy](https://www.osti.gov/pages/servlets/purl/2281696)
- Leeman, Liu, Stiles, Lee, Bhatt, Schoop & Palgrave, "Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis," *PRX Energy* 3, 011002 (2024): argue the central claim that many previously unknown materials were synthesized does not hold — "we believe that at time of publication, none of the materials were new." Issues: (1) automated PXRD phase identification seriously flawed in several cases; (2) novelty checking against ICSD unreliable; (3) many ordered DFT targets had previously been made as disordered structures. — [NSF PAR full text](https://par.nsf.gov/servlets/purl/10532478); [Princeton record](https://collaborate.princeton.edu/en/publications/challenges-in-high-throughput-inorganic-materials-prediction-and-/)
- Press coverage (Jan 2024): of the 35 supposedly novel materials analyzed, most resembled mixes of known compounds and three were not new at all; Ceder stated "The work of Dr Palgrave is not peer reviewed and we believe it has multiple errors in it." — [The Register (31 Jan 2024)](https://www.theregister.com/2024/01/31/ai_chemistry_research_disputed/)
- Nature News: many ordered DFT structures A-Lab was told to make had in fact been made before as disordered structures, per Palgrave. — [Nature News d41586-023-03956-w](https://www.nature.com/articles/d41586-023-03956-w)
- Chemistry World: critics said many PXRD patterns of different A-Lab products were identical; Ceder responded that the goal was to show what an autonomous lab can achieve, "not … what the best (or average) human can do." — [Chemistry World](https://chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article) (fetch blocked; via search extract)
- **Nature Author Correction published online 19 January 2026 (Nature vol. 650):** updated Supplementary Information and Data following concerns about diffraction-based structure identification; thanked correspondents who raised issues and reviewers who re-analyzed PXRD data. — [UMN experts record of Author Correction](https://experts.umn.edu/en/publications/author-correction-an-autonomous-laboratory-for-the-accelerated-sy/)
- Secondary (unverified against Nature text): a tracker reports the correction reframes results as 36 of 57 targets synthesized, "new to the lab rather than necessarily new to science"; status corrected, not retracted. — [kingy.ai Breakthrough Tracker](https://kingy.ai/mathematics-science-breakthrough-tracker/records/science-correction-2026-a-lab-autonomous-materials/)

**GNoME (Merchant et al., Nature, Nov 2023; Google DeepMind; claimed 2.2M new crystals, ~380k stable)**
- Cheetham & Seshadri, "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery," *Chem. Mater.* 36, 3490–3495 (2024): propose that useful predictions need **credibility, novelty, and utility**; found "scant evidence for compounds that fulfill the trifecta"; a large fraction of the 384,870 compositions adopt structures already in ICSD; many entries are trivial variants; many rely on ordering of metal ions unlikely to be ordered in reality; no functionality demonstrated so they "cannot yet be regarded as materials"; scope excluded polymers, glasses, MOFs, heterostructures, composites. — [PMC11044265](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265); [eScholarship PDF](https://escholarship.org/content/qt9qx9t3kz/qt9qx9t3kz.pdf?t=sd23fh)
- Seshadri: "We don't think that there's a problem with AI fundamentally … We think it's a problem of how you use it." DeepMind: "We stand by all claims made in Google DeepMind's GNoME paper." — [The Register (11 Apr 2024)](https://www.theregister.com/2024/04/11/google_deepmind_material_study/); [404 Media](https://www.404media.co/google-says-it-discovered-millions-of-new-materials-with-ai-human-researchers/)

**MatterGen (Zeni et al., Nature, Jan 2025; Microsoft Research)**
- M. Juelsholt, "Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset," *Materials Horizons* 13, 5672–5679 (2026), DOI 10.1039/D6MH00268D: the experimentally validated "new" TaCr2O6 is isostructural with/identical to known Ta1/2Cr1/2O2 (TaCrO4-type; reported 1972 by Astrov et al.) and was in MatterGen's training data; the synthesized sample was disordered; generative tools misclassify known disordered phases as new ordered compounds; "human inspection of each predicted compound is needed to ensure novelty." A ChemRxiv preprint version appeared in 2025. — [Materials Horizons D6MH00268D](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d6mh00268d); [ChemRxiv/Cambridge Engage](https://www.cambridge.org/engage/coe/article-details/694d24f36e8e74030e9067de)
- Microsoft's mitigation: a disorder-aware structure-matching algorithm assessing whether two structures are ordered approximations of the same disordered structure (Jan 2025 blog). No direct Microsoft rebuttal to Juelsholt found. — [Microsoft Research blog](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai)

**Benchmarks and reproducibility**
- Matbench Discovery (Riebesell et al., *Nature Machine Intelligence*, 2025): universal interatomic potentials top the leaderboard with F1 0.57–0.82 for stability pre-screening, but authors themselves report misalignment between regression metrics and task-relevant classification metrics — accurate regressors can yield high false-positive rates near 0 eV/atom above hull; they favor prospective test data over retrospective splits. — [LBL record](https://eta-publications.lbl.gov/bibcite/reference/36666); [arXiv 2308.14920](https://pdf.arxiv.org/pdf/2308.14920)
- MLIP Arena (NeurIPS 2025 Datasets & Benchmarks): existing MLIP benchmarks "suffer from data leakage, limited transferability, and an over-reliance on error-based metrics"; top-ranked Matbench Discovery models perform worse on physics-based tests (broken crystal symmetry, rough PES derivatives). — [NeurIPS 2025 paper PDF](https://papers.neurips.cc/paper_files/paper/2025/file/bfa45223cc236855dbaa5c468c809896-Paper-Datasets_and_Benchmarks_Track.pdf)
- Omee et al. benchmark: SOTA GNNs significantly underperform on OOD property prediction vs. their MatBench results; MatBench leaders (coGN, coNGN) less robust OOD than CGCNN/ALIGNN/DeeperGATGNN. — [arXiv 2401.08032](https://arxiv.org/pdf/2401.08032.pdf)

### Inferences
- Pattern across A-Lab, GNoME and MatterGen: (i) DFT/generative pipelines output ordered cells for what are, experimentally, site-disordered solid solutions; (ii) automated novelty checks (ICSD lookup, StructureMatcher) miss these; (iii) automated PXRD refinement can "confirm" targets erroneously. Proposed fixes from the critics: disorder-aware matching, expert crystallographer review, and the credibility–novelty–utility criteria.
- The A-Lab correction (Jan 2026) is the first formal journal correction in this controversy series, establishing a precedent that novelty claims in AI-materials papers will be scrutinized post-publication.

### Gaps
- Could not access the full text of the Nature Author Correction (nature.com fetch not attempted after multiple DNS blocks); the "36 of 57" figure is secondary.
- No systematic reproducibility audit of materials-ML papers (code/data availability rates) found in this session.

---

## Q3. Robotics/hardware challenges (solids/powders, generalist manipulation, cost, modularity/standards, maintenance, error recovery, safety, characterization, synthesizability)

### Takeaway
SDL hardware remains narrow, expensive and bespoke; solid/powder handling and characterization (e.g., PXRD sample prep) are the key bottlenecks specific to materials science, and instrument vendors rarely design for robotic integration. Proposed solutions: standard communication protocols (SiLA 2, ROS), universal sample holders, mobile robots linking existing instruments, low-cost "frugal twins," and "SDL 2.0" flexible, networked platforms. Synthesizability prediction is a parallel bottleneck: thermodynamic stability is necessary but not sufficient.

### Cited Findings
- NIST: "a particular challenge in automated systems for materials science is the need to move around solid samples" (thin films, bulk, powders each need different handling), compared with chemistry/biopharma AE platforms; NIST proposes universal sample holders. — [NIST](https://www.nist.gov/node/1874991)
- End-to-end automation of powder XRD is hard because it involves solid powder handling and sample processing. — [arXiv 2501.06847 (Jan 2025)](https://arxiv.org/html/2501.06847v1)
- Toronto group (Acceleration Consortium) Account (2022): SDL challenges split into "cognition and motor function"; "few instrument manufacturers design their products with self-driving laboratories in mind," making software control/integration the practical near-term problem. — [Chemspeed news summary](https://www.chemspeed.com/news/autonomous-chemical-experiments-challenges-and-perspectives-on-establishing-a-self-driving-lab)
- Tom et al., "Self-Driving Laboratories for Chemistry and Materials Science," *Chemical Reviews* (Nov 2024; Aspuru-Guzik senior author; Acceleration Consortium): reviews hardware, software, integration, real-world examples, levels of automation and domain-specific limitations. — [Chemspeed summary](https://www.chemspeed.com/news/self-driving-laboratories-for-chemistry-and-materials-science)
- Qiu et al., *Chem. Commun.* (2025): "only a limited number of SDLs have been successfully constructed and applied," mainly due to interdisciplinary collaboration and system-integration difficulties. — [Chem. Commun. 2025, issue 55](https://pubs.rsc.org/he/content/articlehtml/2025/cc/d5cc01959a)
- Lee, Yoo, Han et al., "Toward self-driving laboratory 2.0 for chemistry and materials discovery," *Materials Horizons* (2026): first-generation SDLs "remain limited in scope … within narrow experimental domains"; SDL 2.0 roadmap = flexible platforms, AI-driven decision making, distributed networks of labs. — [Materials Horizons d5mh01984b](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d5mh01984b); [UNIST repository PDF](https://scholarworks.unist.ac.kr/bitstream/201301/91305/2/d5mh01984b.pdf)
- Pickles et al., *Matter* (2026), community discussion on harmonizing and accelerating SDLs: obstacles include proprietary software, institutional silos, lack of standards adoption; calls for stronger standards for interoperability, safety, reproducibility. — [Strathprints PDF](https://strathprints.strath.ac.uk/95936/7/Pickles-etal-Matter-2026-community-discussion-on-harmonizing-and-accelerating-self-driving-laboratories.pdf) (via search extract; full text blocked)
- Standards in use: SiLA (device communication protocol) with ROS (robotics middleware), e.g., SLAS Technology 2024 paper and a mobile-robot labware-transfer pilot; lack of interoperability protocols such as SiLA cited as an adoption barrier. — [SLAS Technology 2024 (MTAK repository)](https://real.mtak.hu/206359/1/02_1-s2.0-S2472630324000505-main.pdf); [Óbuda Univ. thesis](https://lib.uni-obuda.hu/sites/lib.uni-obuda.hu/files/Wolf_Adam_ertekezes.pdf); [CHIMIA 2025](https://www.chimia.ch/chimia/article/download/2025_600/2025_600/28621)
- **Cost / accessibility:** "frugal twin" concept — e.g., a color-mixing SDL as a low-cost stand-in for an expensive multi-step chemical-discovery SDL; SDL-Demo proposals argue for cheaper, simpler SDLs retaining core principles. — [Digital Discovery d4dd00059e (2024)](https://pubs.rsc.org/en/content/articlehtml/2024/dd/d4dd00059e); [NSF PAR](https://par.nsf.gov/servlets/purl/10500964)
- **Characterization bottleneck (policy):** DOE's Jan 2025 RFI on autonomous experimentation platforms (MGI implementation) lists automated in-line and in situ sensing for closed-loop experimentation as a technical priority. — [Federal Register 90(11), 17 Jan 2025](https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01161.htm)
- **Synthesizability:** thermodynamic stability is a useful preliminary filter but leaves gaps (Schlesinger & Bartel, *Materials Horizons*, 2026); synthesizability cannot be predicted from thermodynamic or kinetic constraints alone (npj Comput. Mater. 2023); kinetics and precursor availability matter (arXiv 1806.05772). ML approaches: SynthNN (classification on synthesized compositions), SynCoTrain (semi-supervised co-training of SchNet + ALIGNN). — [Bartel group PDF (Aug 2026)](https://bartel.cems.umn.edu/sites/bartel.cems.umn.edu/files/2026-08/schlesinger.bartel_2026-materhoriz.pdf); [npj Comput. Mater. s41524-023-01114-4](https://www.nature.com/articles/s41524-023-01114-4.pdf); [arXiv 1806.05772](https://arxiv.org/abs/1806.05772v3)

### Inferences
- Materials SDLs face a harder hardware problem than liquid-handling chemistry/biology SDLs because powders and solids (weighing, grinding, pelletizing, furnace loading, XRD sample prep) lack mature commercial automation and standard containers; the A-Lab PXRD-identification failure (Q2) shows characterization automation is also an *accuracy* bottleneck, not just a throughput one.
- The convergence of SiLA/ROS, mobile robots, and "distributed SDL networks" suggests the field is moving from monolithic bespoke rigs to modular, networked infrastructure.

### Gaps
- No quantitative cost figures for SDL builds or powder-handling robots found (IFP report likely contains some, but fetch was blocked).
- No sources found specifically on SDL maintenance burden, mean-time-between-failure, or automated error recovery metrics.
- Generalist robot manipulation (foundation-model robots) for lab work: not covered by sources obtained in this session.

---

## Q4. AI model challenges (UQ, interpretability, OOD generalization, LLM hallucination/safety, dual-use, agent benchmarks)

### Takeaway
OOD generalization is the core technical weakness (benchmarks overestimate real-world accuracy); UQ for foundation-model interatomic potentials is an active fix (ensembles, readout ensembling, quantile regression). LLM agents controlling labs raise hallucination and dual-use risks: no model surpassed 70% on lab hazard identification (LabSafety Bench), and research agents produced more harmful content than plain LLMs (SciHazard, 2026).

### Cited Findings
- OOD: see Q1/Q2 (Omee et al.; MatFold; Li et al.) — benchmark scores do not imply generalization. — [arXiv 2401.08032](https://arxiv.org/pdf/2401.08032.pdf); [Digital Discovery d4dd00250d](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)
- **UQ for foundation models:** Bilbrey et al., *npj Comput. Mater.* (Apr 2025, PNNL) — readout ensembling (fine-tune readout layers of an ensemble for model uncertainty) and quantile regression (data uncertainty), demonstrated on MACE-MP-0. — [PNNL (30 Apr 2025)](https://www.pnnl.gov/publications/uncertainty-quantification-neural-network-potential-foundation-models)
- Liu et al. (*npj Comput. Mater.*, 2025/26): heterogeneous ensemble of existing pretrained universal potentials gives a universal uncertainty metric U that "strongly tracks true prediction errors"; used for distillation, matched full DFT-trained performance for tungsten with ~4% of DFT data. — [arXiv 2507.21297](https://arxiv.org/html/2507.21297v1); [TU Delft repository](https://repository.tudelft.nl/record/uuid:e713a9c2-7520-4e23-8db0-aabb028f911c)
- Foundation models must include stability, synthesizability and domain-relevance constraints, not just property prediction (2026 perspective). — [arXiv 2604.14082](https://arxiv.org/pdf/2604.14082)
- **LabSafety Bench (Zhou et al., arXiv 2410.14182; NeurIPS 2025):** 765 multiple-choice questions + 404 lab scenarios (3,128 open-ended tasks; arXiv v4 reports 520 scenarios), aligned with OSHA; across 19 LLMs/VLMs, no model exceeded 70% on hazard identification; weakest in chemistry scenarios; hallucination measured via distractors. — [arXiv 2410.14182](https://arxiv.org/pdf/2410.14182); [NeurIPS 2025 listing](https://neurips.cc/virtual/2025/133184); [Lab Manager](https://www.labmanager.com/new-ai-safety-benchmarking-reveals-major-risks-in-experimental-decision-making-34825)
- A separate study: none of 16 LLM agents achieved a safety score above 60% on embodied task planning (reported alongside LabSafety coverage; secondary). — [Lab Manager](https://www.labmanager.com/new-ai-safety-benchmarking-reveals-major-risks-in-experimental-decision-making-34825)
- ChemSafetyBench (arXiv 2411.16736, Nov 2024): chemistry-specific misuse benchmark (chemical properties, legality assessment, synthesis). — [ChemSafetyBench](https://arxiv.deeppaper.ai/papers/2411.16736v1)
- **Dual-use:** Coscientist (Boiko et al., 2023, GPT-4-driven) showed semi-autonomous chemical experimental design/execution, "revealing its potential for the synthesis of hazardous chemicals" (LLM safety survey). — [arXiv 2412.17686](https://arxiv.org/pdf/2412.17686)
- Scientific-agent risk taxonomy (Tang et al., arXiv 2402.04247, 2024) lists chemical weapons and explosive materials among domain risks; distinguishes malicious use vs. unintended consequences of legitimate tasks. — [arXiv 2402.04247](https://arxiv.org/pdf/2402.04247v4)
- 2026 review of molecular LLM agents: jailbreaks can compel agents to propose routes to hazardous compounds; direct physical manipulation requires strict risk controls and human oversight; cites Coscientist's "bounded laboratory interfaces" as a mitigation. — [arXiv 2608.23104](https://arxiv.org/pdf/2608.23104)
- SciHazard benchmark (2026): deep-research agents scored 32.3% higher mean harm score (DEHARM-SCORE) than standard LLMs. — [alphaXiv 2607.18665](https://www.alphaxiv.org/abs/2607.18665)
- Berkeley CLTC RFI response (Dec 2024) on safety considerations for chemical/biological AI models. — [CLTC PDF](https://cltc.berkeley.edu/wp-content/uploads/2024/12/Safety-Considerations-for-Chemical-andor-Biological-AI-Models_RFI-Response-.pdf)

### Inferences
- Agentic wrappers (tool use + lab actuation) appear to *increase* risk relative to chat LLMs (SciHazard), implying safety must be engineered at the hardware/API layer (bounded interfaces, reagent whitelists, human approval gates) rather than relying on model alignment alone.
- Disorder handling (Q2) is effectively an OOD/representation failure; UQ methods that flag low-confidence regions could also serve as novelty sanity-checks.

### Gaps
- Interpretability-specific materials sources (e.g., symbolic regression, SHAP for materials) not retrieved in this session.
- No dedicated benchmark for LLM agents operating *materials* SDLs found (LabSafety/ChemSafety are general/chemistry).

---

## Q5. Materials-for-robots challenges (soft-material durability/fatigue, manufacturability, multi-physics simulation, co-design)

### Takeaway
Soft actuators/skins degrade far faster than rigid actuators (fatigue, delamination, wear, punctures), durability testing is non-standardized, and hyperelastic/viscoelastic simulation is too inaccurate and slow for reliable AI-driven co-design. Proposed fixes: standardized durability benchmarks, self-healing/damage-resistant materials, residual (learned-correction) sim-to-real, and prototyping-in-the-loop co-design.

### Cited Findings
- Durability review + benchmarking protocol (HKUST soft robotics lab, *Advanced Robotics Research*, Apr 2026): soft pneumatic actuators (SPAs) degrade faster than conventional actuators mainly via fatigue, delamination, wear; conventional actuators tolerate 5–10 years continuous operation with minimal maintenance; lifetime research is "limited and fragmented"; many studies don't assess durability; proposes standardized durability test protocol. — [HKUST Soft Robotics Lab (23 Apr 2026)](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)
- Tan et al., *Chem. Soc. Rev.* (2024): durable soft tactile actuators — failures from overloading, punctures, tears, cuts; moisture, dust, temperature effects; material strategies include self-healing, damage resistance, self-cleaning, temperature stability; "the pursuit of durability may compromise their soft features." — [Chem. Soc. Rev. d3cs01017a](https://pubs.rsc.org/en/content/articlehtml/2024/cs/d3cs01017a)
- Simulation accuracy: accurate soft-material modeling requires hyperelastic, plastic, anisotropic constitutive laws beyond linear elasticity (SORS simulator, arXiv 2512.15994, Dec 2025). — [arXiv 2512.15994](https://arxiv.org/html/2512.15994v1)
- Sim-to-real gap sources: coarse geometry/material models, manufacturing defects, viscoelasticity/plasticity, hysteresis; system identification fails when discrepancies come from unmodeled behaviors (RAFL, arXiv 2603.22039, Mar 2026) — proposed fix: residual acceleration-field learning. — [arXiv 2603.22039](https://arxiv.org/pdf/2603.22039)
- Co-design perspective (arXiv 2505.03761, 2025): current methods emphasize computation "without ensuring feasible realization," risking sim-to-real gaps; high-fidelity FEA can be hundreds of times slower than real time; proposes real-world prototyping in the loop and surrogate metrics. — [arXiv 2505.03761](https://arxiv.org/abs/2505.03761)
- Kriegman et al., "Scalable sim-to-real transfer of soft robot designs" (2019/2020): modular silicone kit to measure the gap across many designs. — [arXiv 1911.10290](https://arxiv.org/pdf/1911.10290)
- Schaff et al. (TTIC, 2023): zero-shot sim-to-real of co-optimized soft crawlers, though simulator reliability across the reality gap remains uncertain. — [TTIC PDF](https://ttic.edu/ripl/assets/publications/schaff23.pdf)

### Inferences
- For AI-designed robot materials, the lack of standardized fatigue/durability data means ML models cannot be trained to predict lifetime; a standardized protocol (HKUST 2026) is a prerequisite for "durability-aware" materials discovery.
- Manufacturing variability (defects) is itself a sim-to-real error source, linking manufacturability and simulation accuracy.

### Gaps
- No in-depth source found covering scale-up/manufacturability of AI-designed robot materials (e.g., liquid crystal elastomers, e-skins) in industry settings.
- No quantitative fatigue-life benchmarks (cycles-to-failure distributions) retrieved.

---

## Q6. Human/organizational issues (workforce, cost, access inequality, energy/compute, regulation)

### Takeaway
Interdisciplinary skill gaps and system integration are cited as the main reasons few SDLs exist; access is uneven due to capital cost, with "frugal twins" and cloud labs proposed as democratizers (cloud labs also raise concern). Governments (US MGI, Korea MSIT) are now funding workforce and infrastructure explicitly. Energy/compute footprint and regulation are under-documented.

### Cited Findings
- Interdisciplinary collaboration and integration difficulties are the main reasons few SDLs exist (Chem. Commun. 2025). — [Chem. Commun.](https://pubs.rsc.org/he/content/articlehtml/2025/cc/d5cc01959a)
- 2023 community perspective lists education and community building alongside ethics as crucial considerations. — [Digital Discovery d3dd00143a](https://pubs.rsc.org/en/content/articlelanding/2023/dd/d3dd00143a)
- Cloud labs offer subscription-based remote access; AI-directed experiments in cloud labs "preview a democratization of science that intrigues but inspires concern." — [NSF PAR 10500964](https://par.nsf.gov/servlets/purl/10500964)
- SDL Futures Workshop Report (NC State, Jun 2025) on democratizing SDLs (frugal/low-cost hybrids). — [NCSU PDF](https://research.ncsu.edu/futurelabsworkshop/files/2025/06/SDL-Futures-Workshop-Report.pdf)
- **Korea (Apr 30, 2026):** MSIT strategy targets ≥300 master's and ≥75 PhD "AI소재 융합인재," converting experiment-centric researchers into AI/data-driven researchers; builds strategic-field "AI 소재 전용 자율실험센터" for 24-hour automated synthesis-to-prototype; develops single- and multi-property AI models for 6 key properties. MSIT also announced a first national SDL industry–academia–research consortium (80+ institutions) launch scheduled for 11 Aug 2026 (announcement; actual launch not verified). — [Daum/news](https://v.daum.net/v/20260430155346042); [Daum/news](https://v.daum.net/v/20260430101533808)
- Korea "K-문샷" strategy for AI-era S&T competitiveness (Mar 2026 agenda document). — [K-문샷 추진전략(안) PDF](https://smartcity.go.kr/wp-content/uploads/2026/03/안건4AI시대과학기술경쟁력대도약을위한K-문샷추진전략안.pdf)
- **US:** MGI 2021 Strategic Plan (Nov 2021) uses "challenges" to unify adoption of Materials Innovation Infrastructure; 2024 challenges include a semiconductor materials challenge linked to CHIPS for America funding up to $100M. June 2024 NSF workshop by MGI's Autonomous Materials Innovation Infrastructure (AMII) IWG produced gap inventories; DOE Jan 2025 RFI on autonomous experimentation platforms. — [mgi.gov](https://mgi.gov/); [MGI AMII workshop report](https://mgi.gov/media/261); [Federal Register 17 Jan 2025](https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01161.htm)
- Institute for Progress (advocacy, not official) recommends DOE Office of Science increase national-lab funding for autonomous experimentation infrastructure. — [IFP PDF](https://ifp.org/wp-content/uploads/Scaling-Materials-Discovery-with-Self-Driving-Labs-Yang-1.pdf)

### Inferences
- Cost and integration expertise concentrate SDL capability in well-funded institutions/countries; national programs (US AMII, Korea's autonomous experiment centers) are effectively shared-facility models to counter this.

### Gaps
- No reliable source found quantifying energy/compute footprint of materials foundation models or SDLs.
- No source found on specific regulation of autonomous labs (beyond general chem/bio AI safety RFIs); EU-specific roadmaps (e.g., EU Materials 2030 / Advanced Materials initiative) not retrieved.

---

## Q7. Proposed solutions and roadmaps (consolidated)

### Takeaway
The expert consensus solution set is: (1) FAIR, standardized, negative-inclusive data (OPTIMADE, NOMAD, SDL-generated data); (2) modular, interoperable, networked SDL hardware (SiLA/ROS, SDL 2.0, frugal twins, cloud labs); (3) UQ-driven active learning and multi-fidelity foundation models with synthesizability constraints; (4) human-in-the-loop expert validation of novelty and characterization; (5) graded levels-of-autonomy frameworks; (6) bounded interfaces and safety benchmarks for LLM agents; (7) government programs for shared infrastructure and workforce.

### Cited Findings
- **Levels of autonomy:** TRI-linked community survey proposes six levels L0 (non-automated) to L5 (fully autonomous); frameworks adapted from SAE vehicle autonomy levels; a separate "Levels of Laboratory Autonomy (LoLA)" proposal exists — levels are not yet standardized. — [Digital Discovery d4dd00059e](https://pubs.rsc.org/en/content/articlehtml/2024/dd/d4dd00059e); [PMC12368842](https://pmc.ncbi.nlm.nih.gov/articles/PMC12368842)
- **SDL 2.0 roadmap (Materials Horizons, 2026):** flexible platforms, AI decision-making, distributed lab networks. — [Materials Horizons d5mh01984b](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d5mh01984b)
- **Community harmonization (Matter, 2026):** stronger standards for interoperability, safety, reproducibility; overcome proprietary software and silos. — [Strathprints PDF](https://strathprints.strath.ac.uk/95936/7/Pickles-etal-Matter-2026-community-discussion-on-harmonizing-and-accelerating-self-driving-laboratories.pdf)
- **Novelty/credibility criteria:** credibility, novelty, utility (Cheetham & Seshadri 2024); human crystallographic inspection and disorder-aware matching (Juelsholt 2026; Microsoft 2025). — [PMC11044265](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265); [Materials Horizons D6MH00268D](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d6mh00268d); [Microsoft blog](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai)
- **Evaluation reform:** task-based, prospective benchmarks (Matbench Discovery); physics-based tests beyond error metrics (MLIP Arena); OOD splits (MatFold LOCO-CV). — [LBL](https://eta-publications.lbl.gov/bibcite/reference/36666); [NeurIPS 2025 MLIP Arena](https://papers.neurips.cc/paper_files/paper/2025/file/bfa45223cc236855dbaa5c468c809896-Paper-Datasets_and_Benchmarks_Track.pdf); [Digital Discovery d4dd00250d](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d4dd00250d)
- **UQ + active learning / data efficiency:** heterogeneous-ensemble UQ enabled distillation with ~4% of DFT data (tungsten). — [arXiv 2507.21297](https://arxiv.org/html/2507.21297v1)
- **Sim-to-real for robot materials:** residual learning over simulators (RAFL 2026), prototyping-in-the-loop co-design (2025), standardized durability protocols (2026). — [arXiv 2603.22039](https://arxiv.org/pdf/2603.22039); [arXiv 2505.03761](https://arxiv.org/abs/2505.03761); [HKUST](https://softrobotics.hkust.edu.hk/2026/04/23/durability-of-soft-pneumatic-actuators-a-review-and-benchmarking-protocol/)
- **National programs:** US MGI/AMII (2021 plan, 2024 workshop, 2025 DOE RFI); Korea MSIT AI-materials platform strategy 2026–2030 (Apr 2026). — [mgi.gov](https://mgi.gov/); [Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01161.htm); [Daum/news](https://v.daum.net/v/20260430155346042)

### Inferences
- The critiques in Q2 have shifted the roadmap emphasis from "throughput" toward "verification" — expert-in-the-loop validation and better automated characterization are increasingly framed as part of the solution rather than a step back from autonomy.

### Gaps
- Acceleration Consortium's own published roadmap/white paper details, EU (e.g., Battery 2030+ / BIG-MAP, Advanced Materials 2030) and China/Japan national SDL roadmaps were not retrieved in this session.
- Physics-informed ML and federated learning in materials: no specific primary sources retrieved.

---

## 접근 차단/실패 사이트

All fetch failures below returned `getaddrinfo ENOTFOUND` — the host is outside this cloud session's allowed network domains (blocked by network policy), not a paywall. Content for these sources was taken only from search-engine extracts.

| URL attempted | Result / reason |
|---|---|
| https://strathprints.strath.ac.uk/95936/7/Pickles-etal-Matter-2026-community-discussion-on-harmonizing-and-accelerating-self-driving-laboratories.pdf | Blocked by network policy (DNS ENOTFOUND; host not in allowed domains) |
| https://pubs.rsc.org/en/content/articlehtml/2026/mh/d5mh01984b (SDL 2.0, Materials Horizons) | Blocked by network policy (DNS ENOTFOUND) — all pubs.rsc.org content (Digital Discovery, Materials Horizons, Chem. Commun., Chem. Soc. Rev.) therefore unread in full |
| https://ifp.org/scaling-materials-discovery-with-self-driving-labs/ | Blocked by network policy (DNS ENOTFOUND) |
| https://www.chemistryworld.com/news/new-analysis-raises-doubts-over-autonomous-labs-materials-discoveries/4018791.article | Blocked by network policy (DNS ENOTFOUND) |
| https://arxiv.org/abs/2304.11120 | Blocked by network policy (DNS ENOTFOUND) — all arxiv.org full texts therefore unread |
| (not attempted after repeated blocks) nature.com, pmc.ncbi.nlm.nih.gov, pubs.acs.org, mgi.gov full texts | Not fetched; per session guidance, stopped attempting additional hosts after multiple DNS blocks. Findings rely on search extracts |
| https://biomed.reviewer.ly/... (appeared in search results) | Requires login (not attempted) |
