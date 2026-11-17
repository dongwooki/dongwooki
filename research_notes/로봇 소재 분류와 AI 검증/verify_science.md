# 로봇·소재 AI 핵심 과학 주장 1차 출처 검증 (2026-11-17 기준)

> 범위: 이전 라운드(`로봇 분야 소재공학 AI 도입/self_driving_labs.md`, `challenges_solutions.md`)에서 검색 스니펫으로만 모은 주장을 원문(논문·정정 공고·공식 보도자료)으로 다시 확인했다.
> 표기: **VERIFIED**는 1차 출처 본문이나 공식 초록을 직접 읽은 경우, **PARTIALLY VERIFIED**는 일부만 1차 확인하고 나머지는 2차 출처인 경우, **UNVERIFIED**는 1차 출처에 접근하지 못한 경우다.
> 방법: WebFetch 도구는 이번 세션에서 모든 호스트에 대해 `getaddrinfo ENOTFOUND`를 반환했다(arxiv.org 포함). 그래서 모든 원문은 Bash `curl`로 받아 BeautifulSoup/pdftotext로 추출했다. Cloudflare 차단 출판사(ACS, RSC, APS, Science)는 PMC E-utilities, Europe PMC REST API, NSF PAR, OSTI, Crossref, OpenAlex 메타데이터로 우회했다.

## Q1. A-Lab (Szymanski et al., Nature 2023): 원래 주장, 2026-01-19 Author Correction, Leeman/Schoop/Palgrave PRX Energy 2024 비판

### Takeaway
**VERIFIED.** 원래 논문은 "17일간 58개 표적 중 41개 novel compounds(71%)"를 주장했다. 2026-01-19 Author Correction 이후 Nature 본문은 "57개 표적 중 36개(63%), 4개 inconclusive, 17개 미획득"으로 바뀌었다. 정정 공고 자체의 문장은 "보고된 성공 40건 중 36건에서 올바른 결론"이다. 따라서 이전 노트에서 상충하던 "36/40"과 "36/57"은 **둘 다 맞고**, 가리키는 분모가 다를 뿐이다.
- 40 = 원래 보고된 성공 41건에서 Zn2Cr3FeO8를 뺀 수
- 57 = 표적 58개에서 Zn2Cr3FeO8를 뺀 수

"novel"은 "new to the prediction platform, not necessarily new to science"로 재정의됐고, 논문 제목에서도 "novel materials"가 "inorganic materials"로 바뀌었다.

### Cited Findings
**원래 논문(OSTI 수록 저자 원고, 정정 전 버전)**
- 원래 제목은 "An autonomous laboratory for the accelerated synthesis of **novel** materials"이다(Received 16 May 2023, Accepted 10 Oct 2023). — [OSTI PDF 2281696](https://www.osti.gov/pages/servlets/purl/2281696)
- 원래 초록: "Over 17 days of continuous operation, the A-Lab realized **41 novel compounds from a set of 58 targets**". 본문은 "**71% success rate**", "41 of 58 target materials that span 33 elements and 41 structural prototypes", "35 of the 41 materials … obtained using recipes proposed by ML models trained on … literature", "only 37% of the 355 synthesis recipes tested"라고 썼다. — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/2281696)

**Nature 현행(정정 후) 본문**
- 현행 제목은 "An autonomous laboratory for the accelerated synthesis of **inorganic** materials"이고, 서지는 Nature 624, 86–91(2023)이다. 페이지 상단에 "An Author Correction to this article was published on 19 January 2026"이 표시된다. — [Nature s41586-023-06734-w](https://www.nature.com/articles/s41586-023-06734-w)
- 현행 초록: "Over 17 days of continuous operation, the A-Lab realized **36 compounds from a set of 57 targets** …". "novel"이라는 단어는 빠졌다. — [Nature](https://www.nature.com/articles/s41586-023-06734-w)
- 현행 본문에서 바뀐 수치는 다음과 같다. — [Nature](https://www.nature.com/articles/s41586-023-06734-w)
  - 성공률과 구성: "36 of the 57 target compounds … representing a **63%** success rate", "33 elements and **40** structural prototypes"
  - Fig. 2 범례: "A total of 36 targets were successfully synthesized (blue bars), **four were inconclusive from XRD** (purple bars), and the remaining 17 were not obtained"
  - 레시피: "30 of the 36 materials … obtained using recipes proposed by ML models trained on … literature"
  - Outlook: "the A-Lab performed **353 experiments** and successfully realized 36 of 57"
  - 계산 오류 표적을 제외한 경우: "our total success rate would increase to 70% (38/54 targets)"
- 현행 본문의 novelty 정의: "All target materials considered in this work are **new to the lab**, that is, not present in the training data for the algorithms it uses to propose synthesis recipes". 수동 Rietveld 재분석에 대해서는 "a satisfactory fit … can be obtained only when the target is included in refinement. This does not necessarily imply the target was made with high purity"라고 썼다. — [Nature](https://www.nature.com/articles/s41586-023-06734-w)

**Author Correction 원문** (Nature 650, E1(2026), DOI 10.1038/s41586-025-09992-y, 2026-01-19 게재, 2026-02-05 호) — [Nature s41586-025-09992-y](https://www.nature.com/articles/s41586-025-09992-y)
- 문제 제기: "concerns were raised about the unambiguous identification of the compound structures using diffraction as well as the original claims of material novelty."
- novelty 재정의: "We acknowledge that the original claims of material novelty were subject to misinterpretation—their intention was to indicate that the materials were **new to the prediction platform, not necessarily new to science**."
- 재분석 결과: "we have manually re-analyzed the diffraction patterns and have confirmed that the prediction platform came to the correct conclusion in **36 of its 40 reported successes, with 4 compounds being inconclusive**. This re-analysis was **peer-reviewed post-publication**."
- 제외된 표적: "updated to exclude four target materials whose presence is inconclusive from XRD alone. We have also removed one compound from the discussion (**Zn2Cr3FeO8**) that was mistakenly included in the training data."
- 수정 범위: Fig. 2, SI, Supplementary Data가 수정됐다. 정정 전 원고를 주석으로 표시한 PDF도 함께 제공된다.
- 처리 형태: 철회(retraction)가 아니라 정정(correction)이다(공고 형식으로 확인).
- Crossref도 이 정정이 원 논문(10.1038/s41586-023-06734-w)을 update한다고 기록한다(created 2026-01-19T14:01Z). — [Crossref API](https://api.crossref.org/works?filter=updates:10.1038/s41586-023-06734-w)

**Nature 페이지 독자 댓글(1차 기록이지만 비동료심사)**
- J. Yamaguchi(2023-12-07)는 "36 of these compounds are merely variations in composition of well-established structure types"라고 지적했다. 다른 댓글은 "The nature and magnitude of the errors mean this paper should be retracted"라고 썼다. — [Nature 댓글란](https://www.nature.com/articles/s41586-023-06734-w)

**Leeman, Liu, Stiles, Lee, Bhatt, Schoop, Palgrave, PRX Energy 3, 011002 (2024)** (Perspective, 접수 2024-01-30, 게재 2024-03-07, CC BY 4.0; NSF PAR 사본) — [NSF PAR PDF](https://par.nsf.gov/servlets/purl/10532478)
- 초록: "reported the autonomous discovery of **43 novel materials** … We discuss all 43 synthetic products and point out **four common shortfalls** … These errors unfortunately lead to the conclusion that **no new materials have been discovered** in that work."
- 개선 제안 두 가지: "(i) Automated Rietveld analysis of powder x-ray diffraction data is not yet reliable"와 "(ii) … disorder in materials is often neglected in predictions".
- 무질서 문제: "**two thirds** of the claimed successful materials … are likely to be known compositionally disordered versions of the predicted ordered compounds."
- 숫자 43의 출처: 서론은 "41 new materials out of 58 predicted targets … 71% … Using human intervention, the success rate has been increased to **78%—43** successfully synthesized"라고 쓴다. 43은 원 논문의 "부분 성공 포함" 수치이고, "Below, we discuss the 43 materials (which includes the partial successes)"라고 명시한다. 이전 노트의 "41 vs 43 불일치"는 이렇게 해소된다.
- 핵심 판정: "we believe that at time of publication, **none of the materials produced by A-lab were new**: the large majority were misclassified and a smaller number were correctly identified but already known." 이 중 세 화합물은 GNoME의 ICSD 스냅샷 이후 A-Lab 출판 전 사이에 보고된 것이다.
- 오류 분포(Table I, "36 claimed 'successful' syntheses" 기준):

  | 오류 | 내용 | 해당 수 |
  |---|---|---|
  | Error 1 | very poor and obviously incorrect fits | 18/36 |
  | Error 2 | 보고된 CIF와 다른 CIF를 refinement에 사용(예측 구조를 관측 XRD에 맞춰 변경) | 8/36 |
  | Error 3 | 양이온 질서의 증거가 없고, 알려진 무질서 버전이 존재 | 24/36 |
  | Error 4 | ICSD에 이미 보고된 화합물 | 3/36 |

- 커뮤니티 권고(요지):
  1. 새 물질이라고 주장할 때는 어떤 의미로 새로운지 밝혀야 한다.
  2. 계산 예측에서 조성 무질서를 명시적으로 고려해야 한다.
  3. 적합도 통계만으로 성공을 판정하면 안 된다.
  4. 조성 측정은 구조 측정만큼 중요하다.
  5. "inverse Occam's razor"를 피해야 한다.

**언론 보도(2차, 맥락 확인용)**
- Nature News 기사("Robot chemist sparks row with claim it created new materials")를 확인했다. 2024-01-09 업데이트에서 Palgrave·Schoop 팀이 ChemRxiv에 상세 분석을 올렸다고 밝히고, Leeman et al. ChemRxiv 10.26434/chemrxiv-2024-5p9j4를 인용한다. 본문 대부분은 페이월이다. — [Nature News d41586-023-03956-w](https://www.nature.com/articles/d41586-023-03956-w)
- The Register(2024-01-31)는 "35 of which had been proposed … with the help of GNoMe"라고 썼다. 부제에는 "should be retracted as the main claim of discovery is wrong"이라는 UCL 교수의 말이 있다. — [The Register](https://www.theregister.com/2024/01/31/ai_chemistry_research_disputed/)
- C&EN(2026-01) 기사의 제목은 "'Nature' robot chemist paper corrected, but some questions remain unanswered"이다. 리드는 "claimed that … A-Lab successfully synthesized **43** new materials in 17 days"이다. 리드 이후 본문은 로그인이 필요해 읽지 못했다. — [C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01)

### Inferences
- 이전 노트 판정:
  - "41 of 58 in 17 days": **정확**(원래 주장).
  - "36 of 40": **정확**(정정 공고 문구).
  - "36 of 57": **정확**(정정 후 본문). 이 둘은 서로 모순되지 않는다.
  - "36 inorganic (not novel)": 정정 후 본문 표현과 **대체로 일치**한다.
- 정정 후 A-Lab 논문은 "새 물질 발견"이 아니라 "플랫폼(학습 데이터)에 새로운 표적의 자율 합성" 논문으로 지위가 바뀌었다. 정정은 Leeman et al.의 주된 비판인 무질서 버전 문제(24/36)를 직접 반박하지 않는다. "new to science가 아니다"라고 인정해 쟁점을 우회한 것이다.
- C&EN과 Leeman et al.의 "43"은 원 논문의 부분 성공 포함 수치다. 41과 43을 섞어 쓰면 오해를 부른다. 보고서에는 "41/58(자율 판정), 인간 개입 포함 43"으로 구분해 적는 것이 안전하다.

### Gaps
- C&EN 2026-01 기사 본문의 Palgrave 인용("less interesting but not so flawed")과 Schoop의 반응은 로그인 장벽 때문에 1차 확인하지 못했다(**UNVERIFIED**).
- 정정 첨부 PDF(주석 표시 원고, SI 수정본)는 내려받지 않았다. 제외된 4개 inconclusive 화합물의 이름은 확인하지 못했다.
- Ceder LinkedIn 반론(MnAgO2, Mg3Ni3MnO8 인정)은 이번에 재확인하지 않았다.

## Q2. GNoME (Merchant et al., Nature 2023) 수치와 Cheetham & Seshadri, Chem. Mater. 2024 비판

### Takeaway
**VERIFIED.** GNoME 원문 수치는 다음과 같다.
- MP 대비 안정 구조 2.2 million
- 갱신된 convex hull 위의 신규 381,000개(총 421,000개 안정 결정)
- ICSD 실험 구조와 독립 일치 736개

"380k"는 381,000의 반올림이다. Cheetham & Seshadri가 분석한 Stable Structure DB 항목 수는 384,870이다.

### Cited Findings
**GNoME 원문** — [Nature s41586-023-06735-9](https://www.nature.com/articles/s41586-023-06735-9)
- 초록: "Building on 48,000 stable crystals identified in continuing studies, improved efficiency enables the discovery of **2.2 million structures below the current convex hull** … Of the stable structures, **736** have already been independently experimentally realized."
- 본문: "GNoME models found 2.2 million crystal structures stable with respect to the Materials Project. Of these, **381,000** entries live on the updated convex hull as newly discovered materials." 같은 대목에서 "the updated convex hull consists of 381,000 new entries for a total of **421,000** stable crystals"라고 쓴다.
- 736개의 성격: "Of the experimental structures aggregated in the ICSD, 736 match structures that were independently obtained through GNoME." 즉 GNoME가 이 736개를 직접 합성한 것이 아니다. 독립적으로 보고된 실험 구조와 일치했다는 뜻이다.

**Cheetham & Seshadri, "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery", Chem. Mater. 36, 3490–3495 (2024-04-08), ACS AuthorChoice, PMC11044265** — [PMC E-utilities 전문 XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11044265&rettype=xml); [PMC11044265](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/)
- 초록: "unfortunately finding **scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility** … there is clearly a great need to incorporate domain expertise in materials synthesis and crystallography."
- 방법: "a small, randomized subset of the new materials in both the GNoME Explorer archive and the Stable Structure database". Stable Structure DB는 "Almost 400,000"이고, GNoME Explorer에는 ">2000" 구조가 상세 수록돼 있다.
- 용어 비판: 예측은 "solely of crystalline inorganic compounds"이므로 "material"이라고 부르면 안 된다. 화합물은 "become materials when they demonstrate some utility". 본문 표현은 "cannot yet be regarded as materials."
- 공간군 분석: 384,870개 항목의 공간군 분포가 ICSD와 "strikingly different"하다. ICSD 상위 공간군인 Pnma와 P2₁/c는 각각 약 8%를 차지하지만, Stable Structure DB에서는 Pm이 12.7%, P1이 10.2%로 상위를 차지하고 Pnma는 16위(1.56%)다.
- 방사성 원소: Pm, Ac, Pa 화합물이 "more than 18,000 in all"이다. 이와 별도로 Tc, Np, Pu 화합물이 23,529개 있다.
- 결론: "we have yet to find any strikingly novel compounds in the GNoME and Stable Structure listings, although we anticipate that there must be some among the 384,870 compositions … many of the new compositions are trivial adaptations of known materials". 또 Zr, Hf, Nb처럼 화학적으로 유사한 원소가 서로 다른 자리에 질서 배열돼야 성립하는 예측은 "unlikely"라고 본다.

### Inferences
- 이전 노트의 "2.2M / ~380k / 736"은 정확하다. 다만 "736개 실험 검증"은 "ICSD에 독립 보고된 구조와 일치"라는 뜻으로 표현해야 정확하다.
- 비판의 성격은 A-Lab 비판과 같다. 질서/무질서 처리와 유사 원소 치환이 "novelty"를 부풀린다는 지적이다.

### Gaps
- DeepMind의 공식 반론("We stand by all claims")은 이번에 1차 확인하지 않았다(이전 노트에서는 The Register와 404 Media 인용).

## Q3. MatterGen (Zeni et al., Nature 2025) TaCr2O6 주장과 Juelsholt, Materials Horizons 2026 비판

### Takeaway
**VERIFIED(MatterGen 본문), PARTIALLY VERIFIED(Juelsholt).** Juelsholt는 RSC가 Cloudflare로 막혀 있어 Europe PMC와 Crossref의 공식 초록·서지만 읽었다.

MatterGen 측 주장은 다음과 같다.
- 목표 체적탄성률(bulk modulus) 200 GPa로 생성한 TaCr2O6를 합성했다.
- 측정 추정치는 최대 169 GPa(4회 평균 158±11 GPa)이고, 이것이 "within 20% of our target"이다.
- 저자들도 합성물이 "compositionally disordered version"임을 스스로 밝혔다.

Juelsholt는 이 물질이 1971년 보고된 Ta1/2Cr1/2O2와 동일하며 MatterGen 학습 데이터에 이미 있었다고 주장한다.

### Cited Findings
**MatterGen 원문** — [Nature s41586-025-08628-5](https://www.nature.com/articles/s41586-025-08628-5)
- 초록: "structures produced by MatterGen are **more than twice as likely to be new and stable**, and **more than ten times closer to the local energy minimum** … we synthesize one of the generated structures and measure its property value to be **within 20% of our target**."
- 후보 선별과 합성: 목표값 4개(50, 100, 150, 200 GPa)마다 8,192개 후보를 생성했다. 필터링으로 75개로 줄이고, "expert inspection" 후 4개를 합성했으며 "Synthesis was successful for one of the four candidates".
- 합성물의 정체: "the synthesized material is TaCr2O6, **a compositionally disordered version** of the ordered structure predicted by MatterGen".
- 물성 수치: "generated by targeting a bulk modulus value of **200 GPa**; we predict a value of **222 GPa** using DFT … estimated bulk modulus is **up to 169 GPa** after four measurements (**158 ± 11 GPa**)". 측정은 나노압입으로 Young's modulus를 재고 Poisson ratio 0.30으로 환산했다.
- novelty 판정 기준: "new"는 "an extended version of Alex-MP-ICSD containing 117,652 disordered ICSD structures in addition to the 850,384 ordered structures"에 없다는 뜻이다. 비교에는 "a newly proposed ordered-disordered structure matcher"를 썼다.

**Juelsholt, "Continued challenges in high-throughput materials predictions: MatterGen predicts compounds from the training dataset", Mater. Horiz. 13(11), 5672–5679 (2026, 인쇄판 2026-06), DOI 10.1039/D6MH00268D, PMID 42007796** (저자 소속: Humboldt-Universität zu Berlin, MPI für Kohlenforschung) — [Europe PMC REST 초록](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1039/D6MH00268D&format=json&resultType=core); [Crossref](https://api.crossref.org/works/10.1039/D6MH00268D)
- 초록: "MatterGen was used to predict the novel compound TaCr2O6, which was subsequently synthesised in a disordered form as **Ta1/3Cr2/3O2**. However, detailed crystallographic analysis … reveals that this is not a novel compound but is **identical to the previously reported Ta1/2Cr1/2O2, first described in 1971 and included in MatterGen's training dataset**."
- 함의: "These findings underscore the necessity of rigorous human verification in AI-assisted materials research, limiting their use for rapid and large-scale prediction of new materials."

### Inferences
- 이전 노트의 "1972년 Astrov et al. 보고"는 초록의 "**1971**"과 다르다. 초록 기준 1971로 고쳐야 한다. 1972는 본문 인용 문헌의 출판연도일 가능성이 있으나 본문은 확인하지 못했다.
- MatterGen은 disorder-aware matcher를 도입했는데도 ICSD에 있는 무질서상과 정확히 같은 물질을 "new"로 분류했다. Juelsholt의 핵심 논점은 바로 이 점이다(초록 수준 확인).
- "within 20%"는 측정 최댓값 169 GPa 기준이다. 평균 158 GPa를 쓰면 오차가 약 21%다(계산: (200−158)/200). 이 점은 본문의 "maximum … is our best estimate" 단서와 함께 제시해야 한다.

### Gaps
- Juelsholt 본문(XRD 비교, 인용 문헌)은 RSC Cloudflare 차단으로 읽지 못했다.
- Microsoft의 공식 반론은 찾지 못했다.

## Q4. SDL 가속 메타분석 (arXiv 2508.06642 / Digital Discovery): 중앙값 가속계수 6과 정의

### Takeaway
**VERIFIED.** Adesiji, Wang, Kuo, Brown(Boston Univ.)의 "Benchmarking self-driving labs"(arXiv 2025-08-08, Digital Discovery 5(1), 14–27, 2026)의 결과는 다음과 같다.
- 보고된 AF는 1.3–100 범위이고 **중앙값은 6**이다.
- AF는 차원 수가 늘수록 커진다("blessing of dimensionality").
- EF는 두 자릿수 이상 차이 나지만 차원당 10–20회 실험에서 정점을 찍는다.

### Cited Findings
- 정의(arXiv PDF 2절):
  - **Acceleration factor**: AF(y_AF) = n_ref / n_AL. 같은 성능 y_AF에 도달하는 데 필요한 실험 수의 비다.
  - **Enhancement factor**: EF(n). 같은 실험 수 n 이후 성능 향상을 나타낸다.
  - 기준 전략으로는 주로 random sampling을 쓰고, 이 밖에 LHS, grid, human-directed sampling이 있다.

  — [arXiv 2508.06642 PDF](https://arxiv.org/pdf/2508.06642)
- 표본: "self-driving lab"으로 검색한 **111개 연구** 중 "only 40%"만 직접 벤치마크를 보고했다. 분석 대상은 "**42 unique studies and 63 reported benchmarks**"이고, 데이터는 github.com/kabrownlab/benchmarking에 있다. — [arXiv PDF](https://arxiv.org/pdf/2508.06642)
- 결과: "the reported AF spanned a wide range, from **1.3 to 100** … The **median reported AF was 6**. Interestingly, AF appeared to increase with increasing d". 최저 1.3은 1차원 온도 최적화를 인간 연구자와 비교한 경우이고, 최고는 4차원 금속 박막 다목적 BO 사례다. — [arXiv PDF](https://arxiv.org/pdf/2508.06642)
- 초록: "reported EF values vary by over two orders of magnitude, although they consistently peak at **10-20 experiments per dimension**". 시뮬레이션에서는 "EF depends upon the statistical properties of the parameter space while AF depends on its complexity". — [arXiv abs](https://arxiv.org/abs/2508.06642)
- 저널판 서지: Digital Discovery vol. 5, issue 1, pp. 14–27 (2026), DOI 10.1039/D5DD00337G. — [Crossref](https://api.crossref.org/works/10.1039/D5DD00337G)

### Inferences
- "SDL은 중앙값 약 6배 적은 실험으로 같은 성능에 도달한다"는 표현이 정확하다. 이 6배는 **실험 횟수 기준이며, 주로 random sampling 대비**다. 벽시계 시간 단축이나 인간 전문가 대비 수치로 쓰면 안 된다.
- 이 6은 Clio의 "6-fold vs random"이나 Burger의 "6× more active"와 숫자만 같을 뿐 개념이 다르다. 보고서에서 혼동하지 않도록 해야 한다.

### Gaps
- 저널판에서 수치가 바뀌었는지는 RSC 차단으로 확인하지 못했다. 위 수치는 arXiv v1 기준이다.

## Q5. Volk & Abolhasani(Nat. Commun. 2024) 지표, Tom et al.(Chem. Rev. 2024) 리뷰, 자율성 레벨 프레임워크

### Takeaway
**VERIFIED.**
- Volk & Abolhasani는 SDL 성능 지표 7개를 제시한다. 그중 첫째인 degree of autonomy는 piecewise / semi-closed loop / closed-loop / self-motivated의 4단계다.
- Tom et al.(Chem. Rev. 124(16), 9633–9732, 2024-08-13)은 하드웨어·소프트웨어 자율성 "category"를 조합해 SDL Level을 정의한다. "true Level 5 SDL remains an unattained goal"이다.
- Tobias & Wahab(MITRE, R. Soc. Open Sci. 2025-07-16)는 1차원 Level 1–5 체계와, 하드웨어(L0–3)×소프트웨어(L0–3)를 조합해 overall Level 0–5를 매기는 2차원 체계를 함께 소개한다.

### Cited Findings
**Volk & Abolhasani, "Performance metrics to unleash the power of self-driving labs in chemistry and materials science", Nat. Commun. (2024), DOI 10.1038/s41467-024-45569-5** — [Nature Communications](https://www.nature.com/articles/s41467-024-45569-5)
- 초록: "Metrics such as optimization rate are therefore not necessarily indicative of the capabilities of an SDL across different studies."
- 7개 지표: Degree of autonomy, Operational lifetime, Throughput, Experimental precision, Material usage, Accessible parameter space, Optimization efficiency.
- degree of autonomy의 4단계: "piecewise, semi-closed loop, closed-loop, or self-motivated". piecewise는 "algorithm-guided study"라고도 하며 "complete separation between platform and algorithm"인 상태다. self-motivated는 "the computational system dictates its own objectives"인 상태다.
- operational lifetime의 4구분: demonstrated/theoretical × unassisted/assisted. 본문 예시는 "demonstrated unassisted lifetime is two days, and the demonstrated assisted lifetime is up to one month"이다.
- 실험 정밀도는 "standard deviation of replicates of a single condition"으로 정량화한다.

**Tom et al., "Self-Driving Laboratories for Chemistry and Materials Science", Chem. Rev. 124(16), 9633–9732 (2024)** (PMC11363023) — [PMC E-utilities 전문](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11363023&rettype=xml); [Crossref](https://api.crossref.org/works/10.1021/acs.chemrev.4c00055)
- 범위(초록): 하드웨어, 소프트웨어, 실험실 인프라 통합을 다루고 "comprehensive review of existing real-world examples of SDLs, their different levels of automation, and the challenges and limitations associated with each domain".
- 레벨 정의(Figure 1): "Similar to the hierarchical framework used to define levels of autonomy in self-driving cars". 정의는 아래 표와 같다. 하드웨어 자율성 category 1 이상인데 소프트웨어가 인간 아이디어(category 0)에 머무르면 "automated experiments", 그 반대는 "ML-informed experiments"라고 부른다.

  | Level | 조건(category = 하드웨어/소프트웨어 자율성 등급) |
  |---|---|
  | Level 5 | 소프트웨어와 하드웨어 모두 category 3 |
  | Level 4 | 둘 중 하나가 category 3이거나, 둘 다 category 2 |
  | Level 3 | 한쪽이 category 1 이상이고 다른 쪽이 category 2 이상 |
  | Level 2 | 인간 아이디어(software 0)+자동 워크플로(hardware 2), 수동 실험(hardware 0)+컴퓨터 다회 제안(software 2), 또는 hardware 1+software 1 |

- 현황: "Level 2 and 3 SDLs make up the vast majority of SDL examples to date. For robotically 'simple' tasks, a series of Level 4 SDLs have been demonstrated, however, a true Level 5 SDL remains an unattained goal in the field."

**Tobias & Wahab(MITRE), "Autonomous 'self-driving' laboratories: a review of technology and policy implications", R. Soc. Open Sci. (2025-07-16)** (PMC12368842) — [PMC E-utilities 전문](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12368842&rettype=xml)
- 1차원 Level 1–5 체계: "To date, **Level 4 is the maximal autonomy** reached by SDLs described in the literature. Adam and Eve are two examples." Level 5는 "a full-fledged (artificially) intelligent research scientist … This level of SDL has not yet been realized."
- 2차원 체계(Table 2):

  | 축 | Level 0 | Level 1 | Level 2 | Level 3 |
  |---|---|---|---|---|
  | 하드웨어 | manual | single task | workflow | automated laboratory |
  | 소프트웨어 | human ideation | single cycle | multiple closed-loop cycles | generative(탐색 공간도 컴퓨터가 결정) |

  overall Level은 0–5다. "Level-4 SDLs must be at least Level-2 in both … a Level-5 SDL, which has not yet been demonstrated, must be Level-3 in both dimensions".
- 2차 확인: 서울경제(2025-12, Daum 게재) 기사도 이 MITRE 논문을 "레벨 1부터 레벨 5"로 소개하고, KIST 스마트랩을 레벨 3으로 분류한다. — [Daum/서울경제](https://v.daum.net/v/20251217175541326)

### Inferences
- 이전 노트의 "TRI-linked community survey L0–L5"(Digital Discovery d4dd00059e)는 RSC 차단으로 이번에도 확인하지 못했다. 대신 Tom et al.(Chem. Rev.)과 Tobias & Wahab(RSOS)라는 확인된 두 1차 출처로 대체할 수 있다. 두 출처 모두 "Level 5는 아직 미실현", "대부분은 Level 2–3"이라는 데 합의한다.
- 자율성 레벨은 아직 표준화되지 않았다. 숫자 체계가 문헌마다 다르다(Volk: 4단계 서술형, Tom: Level 2–5, MITRE: 1D Level 1–5와 2D Level 0–5).

### Gaps
- Digital Discovery d4dd00059e(L0–L5 survey)와 "LoLA" 제안은 1차 확인하지 못했다(**UNVERIFIED**).
- Tom et al.의 Figure 1에서 하드웨어·소프트웨어 category 0–3의 정확한 문구는 본문 일부만 확인했다.

## Q6. 대표 SDL 헤드라인 수치 (Liverpool 2020/2024, Clio, Polybot, RoboChem, USTC)

### Takeaway
**대부분 VERIFIED.** Burger 2020(688 experiments/8일/10 variables/6배 활성), Clio(42 experiments/2 work-days/random 대비 6배, 최고 셀 +13%), Polybot(7-D, >4,500 S/cm), USTC(>3M 조성, 550,000 s, 445.1 mV)는 원문 초록이나 본문과 일치한다.

다음 두 수치는 원문으로 확인하지 못했다.
- RoboChem의 "80%"와 "주 10–20 분자": 논문이 아니라 UvA 보도자료의 Noël 인용이다. "80%"는 "무작위 선정 4편 논문 재현" 맥락이다.
- USTC의 "−37 °C"와 Liverpool 2024의 "1.75 m 로봇": 접근 가능한 원문 부분에서 확인하지 못했다.

### Cited Findings
- **Burger et al., "A mobile robotic chemist", Nature 583, 237–241 (published 2020-07-08)**. 초록: "The robot operated autonomously over **eight days**, performing **688 experiments** within a **ten-variable** experimental space, driven by a batched Bayesian search algorithm … identified photocatalyst mixtures that were **six times more active** than the initial formulations … automating the researcher rather than the instruments." **VERIFIED(초록).** — [Nature s41586-020-2442-2](https://www.nature.com/articles/s41586-020-2442-2)
- **Dai et al., "Autonomous mobile robots for exploratory synthetic chemistry", Nature 635, 890–897 (published 2024-11-06)**. **VERIFIED(초록, 정량 헤드라인 없음).** — [Nature s41586-024-08173-7](https://www.nature.com/articles/s41586-024-08173-7)
  - 구성: "Our modular workflow combines mobile robots, an automated synthesis platform, a liquid chromatography–mass spectrometer and a benchtop nuclear magnetic resonance spectrometer … share existing laboratory equipment with human researchers without monopolizing it".
  - 의사결정: "A heuristic decision-maker processes the orthogonal measurement data … automatically checking the reproducibility of any screening hits".
  - 적용 분야: structural diversification, supramolecular host–guest, photochemical synthesis.
  - 하드웨어: 그림 설명에 "KUKA refers to the mobile robots"라고 나온다.
- **Dave et al.(Clio + Dragonfly), Nat. Commun. (published 2022-09-27), DOI 10.1038/s41467-022-32938-1**. **VERIFIED.** — [Nature Communications](https://www.nature.com/articles/s41467-022-32938-1)
  - 초록: "identifies **six fast-charging** non-aqueous electrolyte solutions in **two work-days and forty-two experiments**. This result represents a **six-fold time acceleration compared to a random search** performed by the same automated experiment."
  - 셀 검증: 220 mAh graphite∥NMC532 pouch cell에서 검증했다.
  - 본문: "the best cell with a Clio electrolyte showed a **13% improvement** on this metric compared to the best baseline cell". 이 지표는 4C 충전 후 방전용량이다. 최악 셀끼리 비교하면 5% 개선이다.
- **Wang et al.(Polybot), Nat. Commun. (published 2025-02-17), DOI 10.1038/s41467-024-55655-3**. 초록: "Leveraging importance-guided Bayesian optimization, Polybot efficiently navigates a complex **7-dimensional** processing space … producing transparent conductive thin films with **averaged conductivity exceeding 4500 S/cm**." **VERIFIED(초록).** — [Nature Communications](https://www.nature.com/articles/s41467-024-55655-3)
- **Slattery et al.(RoboChem), "Automated self-optimization, intensification, and scale-up of photocatalysis in flow", Science 383, eadj1817 (2024-01)**. 초록에는 liquid handler, syringe pump, tunable flow photoreactor, IoT 기기, in-line benchtop NMR, closed-loop BO가 나오고, 결과는 "increasing overall reaction yields and improving space-time yields compared with those of previously reported processes"다. **초록 VERIFIED(Europe PMC)**, science.org는 Cloudflare로 차단됐다. — [Europe PMC REST](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1126/science.adj1817&format=json&resultType=core)
  - UvA 보도자료의 Noël 인용: "In a week, we can optimise the synthesis of about **ten to twenty molecules**. This would take a PhD student several months."
  - 같은 보도자료: "used RoboChem to replicate previous research published in **four randomly selected papers** … 'In about **80%** of the cases, the system produced better yields. For the other 20%, the results were similar'".
  - 판정: **보도자료 수준 VERIFIED**. — [UvA HIMS 보도자료](https://hims.uva.nl/content/news/2024/01/autonomous-synthesis-robot-uses-ai-to-speed-up-chemical-discovery.html)
- **USTC robotic AI chemist, Nature Synthesis 3, 319–328 (2024; online 2023-11-13), DOI 10.1038/s44160-023-00424-1**. 초록: "the entire process, including Martian ore pretreatment, catalyst synthesis, characterization, testing and … the search for the optimal catalyst formula, is performed without human intervention … identifies the optimal catalyst formula from **more than three million possible compositions** … operates at a current density of **10 mA cm−2 for over 550,000 s** … overpotential of **445.1 mV**." **VERIFIED(초록).** — [Nature Synthesis](https://www.nature.com/articles/s44160-023-00424-1)
- 서지 보정: USTC 논문은 이전 노트의 "Nature Synthesis, 13 Nov 2023"이 온라인 게재일이다. 권호는 vol. 3(2024), pp. 319–328이다. — [Nature Synthesis](https://www.nature.com/articles/s44160-023-00424-1)

### Inferences
- "RoboChem이 문헌보다 80% 더 좋은 수율"이라는 표현은 부정확하다. 정확히는 "무작위로 고른 문헌 4편의 반응을 재현한 사례 중 약 80%에서 더 높은 수율, 나머지는 비슷함(연구책임자 보도자료 발언)"이다.
- Clio의 "+13%"는 최고 셀끼리 비교한 값이다. 하한(최악 셀끼리)은 +5%이므로 범위로 제시하는 것이 공정하다.

### Gaps
- USTC "−37 °C 안정성"은 CAS 영문 보도자료 URL이 이번에 404를 반환해 확인하지 못했다. 논문 본문은 페이월이다(**UNVERIFIED**).
- Liverpool 2024의 "1.75 m 로봇"은 Nature 공개 부분에서 확인하지 못했다(**UNVERIFIED**, ScienceDaily 2차 출처만 있음).
- USTC JACS 2025 멀티에이전트 버전의 지표는 ACS 차단으로 확인하지 못했다.

## Q7. 한국 SDL: Digital Discovery 2026 리뷰, KIST "24회", KAIST–POSCO "12배", KRICT 대화형 AI, KIMS 합금 자율실험실

### Takeaway
- **Digital Discovery 2026 리뷰**: "Self-driving laboratories in Korea: a new era of autonomous discovery"가 **실재함을 VERIFIED**했다(Crossref, OpenAlex). Digital Discovery 5(5), 1968–1980이고, 저자 21명(SNU 정연성 교수 등, KAIST 서동화, KIST 한상수, KRICT, SAIT 포함)이다. 본문은 RSC Cloudflare와 SNU 리포지토리(JS 필요)에 막혀 읽지 못했다.
- **KRICT**: 대화형 AI는 **동료심사 논문을 확인**했다(JCIM 2026, DOI 10.1021/acs.jcim.6c00976).
- **KIST·KAIST·KIMS**: 동료심사 논문을 찾지 못했다. 언론과 기관 보도자료 수준에서만 확인했다(**PARTIALLY VERIFIED**). 기관 보도자료 원문으로 보면 KAIST "12배"는 실측이 아니라 **"24시간 운용 시" 가정에 따른 추정치**다.

### Cited Findings
- **Digital Discovery 리뷰 서지.** — [Crossref 10.1039/D6DD00024J](https://api.crossref.org/works/10.1039/D6DD00024J); [OpenAlex](https://api.openalex.org/works/doi:10.1039/D6DD00024J)
  - 제목: "Self-driving laboratories in Korea: a new era of autonomous discovery". Digital Discovery vol. 5, issue 5, pp. 1968–1980 (2026). Crossref 등록일은 2026-03-18이다.
  - 초록: "This perspective highlights the current status and future prospects of self-driving laboratories in Korea. It illustrates how AI-robotics integration accelerates material discovery through closed-loop automation and cross-disciplinary collaboration."
  - 접근: OA 상태는 "diamond"이고, 리포지토리 사본은 hdl.handle.net/10371/234679(SNU s-space)다.
  - 저자 소속: 서울대(다수), 홍익대, 삼성종합기술원, KAIST(Dong-Hwa Seo), KIST(Sang Soo Han, KangGeon Kim), KRICT(Su-Hyun Yoo, Jungho Shin), 서울대 Yousung Jung 등.
- **KIST 스마트 연구실 "1만 번 실험을 24번으로"**: 서울경제 서지혜 기자(Daum 게재, 2025-12-17 URL). — [Daum/서울경제](https://v.daum.net/v/20251217175541326)
  - 구축 주체: "한상수 KIST 계산과학연구센터장을 주축으로 한 연구원 4명이 구축한 스마트 연구실".
  - 이전 성과: "지난해 KIST는 … 인간 연구자가 **1만 번** 수행해야 하는 실험을 AI가 **200회** 만에 해결한다고 발표"했다.
  - 최근 성과: "최근에는 촉매 소재를 단 **24번의 실험**만으로 찾아내는 데 성공했다. 최고 성능의 촉매를 도출하는 데 걸린 시간은 **일주일 남짓**". 연구팀은 "특허 출원을 준비"하고 있다.
  - 판정: 기사 본문은 **VERIFIED**. "1만 번 대비 24번"은 헤드라인식 결합이다. 본문은 1만 대 200(작년)과 24회(최근 촉매)를 별개 성과로 서술한다. 동료심사 논문은 찾지 못했다.
- **KAIST–포스코홀딩스 양극재 자율 탐색 실험실**: KAIST 공식 보도자료(등록일 2025-08-05). — [KAIST 뉴스](https://news.kaist.ac.kr/news/html/news/?mode=V&mng_no=49930)
  - 개요: "탐색 기간을 **93%** 단축했다".
  - 12배의 근거: "지능형 실험 자동화 시스템을 **24시간 운용할 경우**, 약 **12배 이상**의 실험 데이터 확보 및 93%의 소재 탐색 시간 단축이 가능하며, 이는 소재 탐색에 필요한 실험 횟수가 **500회라고 가정할 시** … 기존 방식으로는 **84일** … 자동화 시스템은 약 **6일**".
  - 구성: 정량, 혼합, 펠렛화, 소결, 분석 모듈과 중앙 로봇팔이 있고, AI 모델이 XRD를 해석한다. 성공·실패 데이터를 모두 DB에 쌓는다.
  - 판정: 보도자료 원문 **VERIFIED**. 한국경제(2025-08-03) 제목은 "데이터 확보 12배 늘었다"인데, 이는 조건부 추정치를 실적처럼 표현한 것이다. — [한국경제](https://www.hankyung.com/article/2025080386861)
- **KRICT 대화형 AI**: Mottafegh A., Ahn G.-N., "Adaptive human-in-the-loop optimization using language-guided priors for chemical experiments", J. Chem. Inf. Model. (Crossref 출판일 2026-07-13, Europe PMC 2026-08-01), DOI 10.1021/acs.jcim.6c00976. **VERIFIED(공식 초록).** — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1021/acs.jcim.6c00976&format=json&resultType=core); [Crossref 검색](https://api.crossref.org/works?query=human-in-the-loop+optimization+large+language+model+self-driving+laboratory+chemist+knowledge&filter=issn:1549-9596,from-pub-date:2026-01-01&rows=8)
  - 문제의식: "cold start problem".
  - 방법: LLM이 자연어 프롬프트를 "structured prior mean functions and constraints for Bayesian optimization"으로 변환한다. "adaptive weight credibility detection (AWCD)"은 데이터가 전문가 가설과 모순되면 prior를 비활성화한다.
  - 검증: Ugi 다성분 반응(연속)과 P3HT-CNT 복합체(이산) **데이터셋**으로 검증했다. 결과는 "accelerates … relative to unguided Bayesian optimization". 인터페이스 이름은 "Co-Scientist"다.
  - 한계: 물리 SDL 하드웨어로 검증한 것은 아니다. 데이터셋 기반 검증이며, 이는 이전 노트의 "물리 SDL 검증은 예정" 서술과 일치한다.
- **KIMS 오토노머스 랩**: 헤럴드경제 구본혁 기자(Daum 게재, 2025-06-29 URL). — [Daum/헤럴드경제](https://v.daum.net/v/20250629140135289)
  - 장비 흐름: "로봇 팔이 금속 샘플을 집어 들어 … 아크 멜터(Arc Melter)에 올려놓는다 … 튜브 퍼니스(Tube Furnace)에 옮겨 열처리 … X선 회절기(XRD)로 운반해 정밀 분석". 로봇 팔이 자동 인장 시험도 수행한다(사진 설명).
  - 효과: 고온 합금 개발이 "수개월, 길게는 수년" 걸리던 것을 "몇 주 안에" 끝낼 수 있다고 한다. 정량 비교는 없다.
  - 알고리즘: 이호원 재료데이터·분석연구본부장은 "일종의 강화학습 알고리즘처럼 작동한다"고 말했다.
  - 판정: 언론 보도는 **VERIFIED**. 동료심사 논문은 찾지 못했다. 이전 노트의 "Digital Discovery 리뷰가 KIMS 합금 랩을 기술"했다는 서술은 리뷰 본문에 접근하지 못해 여전히 **UNVERIFIED**다.

### Inferences
- 한국 사례 중 동료심사 단계에 도달한 것은 KRICT(JCIM, 데이터셋 기반)와 리뷰 논문(Digital Discovery)뿐이다. KIST "24회", KAIST "12배·93%", KIMS "몇 주"는 모두 기관 발표나 언론 보도다. 보고서에서는 "기관 발표 기준"이라는 단서를 붙이고, KAIST 수치에는 "24시간 가동·500회 가정" 조건을 함께 밝혀야 한다.
- 서울경제 기사는 KIST 스마트랩을 MITRE 체계의 레벨 3(BO·액티브러닝으로 다음 실험을 자율 선택)으로 분류한다. 기자의 분류이며 KIST의 공식 자기평가는 아니다.

### Gaps
- Digital Discovery 한국 리뷰 본문(각 기관별 수치, KIMS 서술 여부)은 확인하지 못했다. pubs.rsc.org는 Cloudflare, s-space.snu.ac.kr은 JS 필요 페이지, hdl.handle.net은 HTTP 500이었다.
- KIST "24회 촉매"와 "200회" 성과의 원 논문이나 보도자료 원문은 찾지 못했다. kist.re.kr 메인은 접근되지만 해당 보도자료는 탐색하지 않았다.
- EurekAlert의 KRICT 영문 보도자료는 AWS WAF challenge(HTTP 202, 빈 본문), Newswise는 Cloudflare 403이었다.

## Q8. LabSafety Bench와 SciHazard 벤치마크 수치

### Takeaway
**VERIFIED.**
- **LabSafety Bench**(arXiv 2410.14182 v4, 2026-02-12): MCQ 765개, 시나리오 404개(개방형 과제 3,128개). 19개 LLM/VLM 중 hazard identification에서 70%를 넘은 모델은 없다. 최종 게재지는 **Nature Machine Intelligence 8, 20–31 (2026)**이다.
- **SciHazard**(arXiv 2607.18665 v2, 2026-10-23; NeurIPS 2026 E&D Track 채택): 2,400개 유해 질문과 600개 과잉안전 질문, 12개 분야. 31개 frontier LLM·deep research agent를 평가했고, deep research agent의 평균 DeHarm-Score가 표준 LLM보다 32.3% 높다.

### Cited Findings
- **LabSafety Bench** (Zhou, Yang, Huang … Chawla, Zhang). — [arXiv 2410.14182](https://arxiv.org/abs/2410.14182)
  - 초록(v4): "evaluates models on hazard identification, risk assessment, and consequence prediction across **765 multiple-choice questions and 404 realistic lab scenarios**, encompassing **3,128 open-ended tasks**. Evaluations on **19** advanced LLMs and VLMs show that **no model evaluated on hazard identification surpasses 70% accuracy**. While proprietary models perform well on structured assessments, they do not show a clear advantage in open-ended reasoning."
  - 버전 이력: v1 2024-10-18, v2 2025-02-26, v3 2025-06-06, v4 2026-02-12.
  - arXiv 메타데이터: comments "Published at Nature Machine Intelligence", journal-ref "Nat Mach Intell 8, 20-31 (2026)".
- **DeepSafe-SciHazard** (Chunxiao Li 외, Shanghai AI Lab 계열 저자 Lei Bai, Jing Shao 포함). — [arXiv 2607.18665](https://arxiv.org/abs/2607.18665)
  - 버전과 채택: v1 2026-07-21, v2 2026-10-23. "Accepted at NeurIPS 2026 Evaluations and Datasets Track".
  - 데이터셋 구성: "**2400 hazardous questions and 600 oversafety questions across 12 disciplines**".
  - 평가 방법: DeHarm-Score는 query hazard severity, refusal behavior, response-level risk(Executability와 Net-new risk)로 분해해 계산한다.
  - 전문가 검증: "improves agreement with expert annotations by 90.17% over the strongest baseline".
  - 핵심 결과: "We benchmark **31** frontier LLMs and deep research agents … deep research agents yield **32.3% higher mean DeHarm-Score** than standard LLMs".

### Inferences
- 이전 노트 판정:
  - "NeurIPS 2025": LabSafety Bench의 최종 게재지가 Nat. Mach. Intell. 2026으로 확인됐으므로 이것을 우선 인용해야 한다. NeurIPS 2025 목록은 이번에 확인하지 않았다.
  - "arXiv v4 reports 520 scenarios": v4 초록은 **404**이므로 오류로 보인다.
  - SciHazard "32.3%": **정확**.
- SciHazard의 "deep research agent"는 웹 검색과 도구를 쓰는 연구 에이전트를 말한다. 물리 실험실을 구동하는 SDL 에이전트가 아니다. SDL 위험의 근거로 쓸 때는 "에이전트화가 위험을 키운다는 간접 증거"로 표현해야 한다.

### Gaps
- 이전 노트의 "16 LLM agents 중 embodied task planning에서 60% 초과 없음"(Lab Manager 2차 출처)은 원 논문을 찾지 않았다(**UNVERIFIED**).
- 재료 SDL 전용 안전 벤치마크는 여전히 확인하지 못했다.

## 접근 상태 로그

이번 세션 도구별 상태(2026-11-17):
- **WebFetch**: 시도한 3개 호스트(pubs.rsc.org, arxiv.org, www.chemistryworld.com) 모두 `getaddrinfo ENOTFOUND`였다. 사용자가 네트워크를 unrestricted로 바꾼 뒤에도 WebFetch는 DNS 단계에서 실패했다. 같은 시각 curl로는 arxiv.org가 200이었으므로, 문제는 네트워크 정책이 아니라 WebFetch 도구 쪽이다.
- **curl**: 에이전트 프록시 경유로 동작했다(프록시 status 정상, recentRelayFailures 없음). 아래 표의 결과는 curl 기준이며, User-Agent는 일반 Chrome UA를 사용했다.

| 호스트 | 결과 | 시도한 자료 |
|---|---|---|
| www.nature.com | **성공 200**(OA 전문, 페이월 논문은 초록만) | A-Lab 원문·정정 공고, GNoME, MatterGen, Volk&Abolhasani, Burger 2020, Dai 2024, Clio, Polybot, USTC, Nature News |
| www.osti.gov | **성공 200**(PDF 10.8MB) | A-Lab 정정 전 저자 원고 |
| par.nsf.gov | **성공 200**(PDF) | Leeman et al. PRX Energy 2024 전문 |
| eutils.ncbi.nlm.nih.gov | **성공 200**(JATS XML 전문) | Cheetham&Seshadri(PMC11044265), Tom et al.(PMC11363023), Tobias&Wahab(PMC12368842) |
| pmc.ncbi.nlm.nih.gov | HTTP 200이지만 **JS bot challenge 페이지**(본문 없음) | A-Lab PMC10700133, PMC11044265 |
| www.ncbi.nlm.nih.gov | 성공 200(PMC 랜딩만 확인) | PMC 접근성 점검 |
| www.ebi.ac.uk (Europe PMC REST API) | **성공 200** | Juelsholt 초록, RoboChem 초록, KRICT JCIM 초록, Korea 리뷰 검색(0건) |
| europepmc.org (웹 UI) | **403 Cloudflare challenge**(cf-mitigated) | 접근성 점검 |
| api.crossref.org | **성공 200** | A-Lab 정정 관계, Juelsholt·Korea 리뷰·Digital Discovery 벤치마크·Chem Rev·Chem Mater 서지, KRICT JCIM DOI 검색 |
| api.openalex.org | 성공 200(단일 works 조회). 검색 쿼리 1건은 응답 형식 오류(필터 문법 문제로 보임) | Korea 리뷰 저자·OA 위치, KRICT 검색 |
| arxiv.org | **성공 200**(abs, PDF) | 2508.06642(SDL 벤치마크), 2410.14182(LabSafety), 2607.18665(SciHazard) |
| www.alphaxiv.org | 성공 200(접근성 점검만, 내용은 arXiv에서 확인) | SciHazard |
| journals.aps.org | **403 Cloudflare challenge** | PRX Energy Leeman et al. |
| pubs.acs.org | **403 Cloudflare challenge** | Cheetham&Seshadri(Chem Mater), Tom et al.(Chem Rev) |
| cen.acs.org | 200이지만 **로그인 장벽**(리드 문단 이후 본문 없음) | C&EN 2026-01 A-Lab 정정 기사 |
| pubs.rsc.org | **403 Cloudflare challenge**(articlehtml, articlelanding, articlepdf 모두) | Korea SDL 리뷰(d6dd00024j), Juelsholt(d6mh00268d) |
| www.science.org | **403 Cloudflare challenge** | RoboChem(Science adj1817) |
| chemrxiv.org | **403 Cloudflare challenge** | Leeman 프리프린트 대체 경로 |
| www.chemistryworld.com | **405 AWS WAF captcha**(x-amzn-waf-action: captcha) | Palgrave/Ceder 인용 기사 |
| www.eurekalert.org | **202 AWS WAF challenge**(본문 0바이트) | KRICT 영문 보도자료 |
| www.newswise.com | **403 Cloudflare challenge** | KRICT 영문 보도자료 |
| www.anl.gov | **403 Cloudflare challenge** | Polybot 보도자료 |
| newscenter.lbl.gov | **403 Cloudflare challenge** | A-Lab 보도자료 |
| discovery.ucl.ac.uk | **403 Cloudflare challenge** | Leeman 그린 OA 사본 |
| livrepository.liverpool.ac.uk | **403 Forbidden**(Apache, UoL Web Server) | Burger 2020 저자 원고 |
| news.liverpool.ac.uk | **302 후 500 오류** | Liverpool 2024 보도자료 |
| english.cas.cn | **404**(URL 변경 또는 삭제) | USTC AI chemist 보도자료(−37 °C 확인용) |
| hims.uva.nl | **성공 200** | RoboChem 보도자료(80%, 주 10–20 분자) |
| www.theregister.com | 성공 200 | A-Lab 논란 보도 |
| experts.umn.edu | 성공 200(접근성 점검만) | A-Lab 정정 기록 |
| www.semanticscholar.org | 성공 200(접근성 점검만) | — |
| v.daum.net | **성공 200** | KIST 스마트랩(서울경제), KIMS 오토노머스 랩(헤럴드경제) |
| www.hankyung.com | 성공 200 | KAIST–POSCO 12배 보도 |
| news.kaist.ac.kr | **성공 200** | KAIST–POSCO 공식 보도자료 |
| www.kaist.ac.kr | **연결 실패: curl (35) Connection reset by peer**(2회 재현) | KAIST 메인·뉴스 |
| www.kist.re.kr | 성공 200(301 리다이렉트 후 200) | 접근성 점검(보도자료 탐색은 안 함) |
| www.krict.re.kr | 성공 200 | 접근성 점검 |
| www.kims.re.kr | 성공 200 | 접근성 점검 |
| hdl.handle.net | **HTTP 500** | Korea 리뷰 SNU 리포지토리 핸들 |
| s-space.snu.ac.kr | HTTP 200이지만 **JavaScript 필수 페이지**(본문 없음). http:// 시도는 DNS 해석 실패(curl 6) | Korea 리뷰 리포지토리 사본 |

요약하면 사용자가 네트워크 설정을 바꾼 뒤에도 남은 차단은 다음 네 유형이다.
- **Cloudflare bot challenge**: ACS(pubs, 단 cen은 로그인 장벽), RSC, APS, Science/AAAS, ChemRxiv, Europe PMC 웹 UI, ANL, LBL, UCL Discovery, Newswise.
- **AWS WAF**: Chemistry World, EurekAlert.
- **JS 필수 페이지**: PMC 기사 페이지, SNU s-space.
- **서버 측 오류·거부**: www.kaist.ac.kr(연결 리셋), Liverpool 리포지토리(403), Liverpool 뉴스(500), hdl.handle.net(500), CAS 영문(404).

Nature, OSTI, NSF PAR, NCBI E-utilities, Europe PMC REST API, Crossref, OpenAlex, arXiv, 한국 언론·기관 사이트는 정상이다.
