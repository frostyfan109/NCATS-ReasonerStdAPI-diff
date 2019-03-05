x= { # this edge was extracted to make diff results interesting.
        "relation": "RO:0002200",
        "target_id": "MONDO:0018874",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:16039247",
          "PMID:6591864",
          "PMID:7049597",
          "PMID:8241983",
          "PMID:8404130"
        ],
        "id": "1820642",
        "predicate_id": "RO:0002200",
        "source_database": "BioLink", #diff "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3735547,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      }#,


answer = {
  "question_graph": {
    "edges": [
      {
        "id": "e0",
        "source_id": "n1",
        "target_id": "n2"
      },
      {
        "id": "e1",
        "source_id": "n2",
        "target_id": "n3"
      }
    ],
    "nodes": [
      {
        "id": "n1",
        "type": "phenotypic_feature",
        "curie": "HP:0002105"
      },
      {
        "id": "n2",
        "type": "disease"
      },
      {
        "id": "n3",
        "type": "gene"
      }
    ]
  },
  "knowledge_graph": {
    "nodes": [

      {
        "equivalent_identifiers": [
          "MEDDRA:10005806",
          "MEDDRA:10011234",
          "HP:0002105",
          "MEDDRA:10019523",
          "MEDDRA:10018964",
          "UMLS:C0019079",
          "MEDDRA:10041804"
        ],
        "name": "Hemoptysis",
        "id": "HP:0002105",
        "type": "phenotypic_feature",
        "omnicorp_article_count": 10902
      },

      {
        "name": "acute myeloid leukemia",
        "id": "MONDO:0018874",
        "equivalent_identifiers": [
          "MEDDRA:10000884",
          "MEDDRA:10024291",
          "MEDDRA:10000886",
          "MEDDRA:10051003",
          "MEDDRA:10054296",
          "MEDDRA:10028552",
          "DOID:9119",
          "MEDDRA:10024346",
          "MESH:D015470",
          "UMLS:C0023467",
          "MEDDRA:10029551",
          "MEDDRA:10060394",
          "MEDDRA:10000878",
          "MEDDRA:10060354",
          "ORPHANET:519",
          "MEDDRA:10060557",
          "MONDO:0018874",
          "MEDDRA:10029549",
          "MEDDRA:10060553",
          "MEDDRA:10028557",
          "OMIM:601626",
          "UMLS:C1879321",
          "MEDDRA:10000801",
          "MEDDRA:10000880",
          "MEDDRA:10001941"
        ],
        "type": "disease",
        "rare disease": True,
        "syndromic disease": True,
        "omnicorp_article_count": 40008
      },
      {
        "name": "tuberculosis",
        "id": "MONDO:0018076",
        "equivalent_identifiers": [
          "MEDDRA:10044755",
          "MEDDRA:10071157",
          "MONDO:0018076",
          "MEDDRA:10044766",
          "DOID:399",
          "MEDDRA:10021868",
          "MEDDRA:10021870",
          "MEDDRA:10044756",
          "UMLS:C0151332",
          "UMLS:C0041296",
          "ORPHANET:3389",
          "MEDDRA:10043148",
          "MESH:D014376"
        ],
        "transmissible disease": True,
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 210883
      },
      {
        "equivalent_identifiers": [
          "MESH:D002289",
          "UMLS:C0007131",
          "MEDDRA:10061873",
          "MONDO:0005233",
          "DOID:3908",
          "MEDDRA:10029514"
        ],
        "name": "non-small cell lung carcinoma (disease)",
        "id": "MONDO:0005233",
        "type": "disease",
        "omnicorp_article_count": 44014
      },
      {
        "name": "hepatocellular carcinoma",
        "id": "MONDO:0007256",
        "equivalent_identifiers": [
          "MEDDRA:10073071",
          "DOID:686",
          "MEDDRA:10007416",
          "OMIM:114550",
          "UMLS:C2239176",
          "ORPHANET:88673",
          "MEDDRA:10019838",
          "DOID:684",
          "MEDDRA:10049010",
          "MEDDRA:10048491",
          "MONDO:0007256",
          "UMLS:C1867955",
          "UMLS:C1862761",
          "MEDDRA:10024658",
          "MESH:D006528"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 105682
      },
      {
        "name": "cystic fibrosis",
        "monogenic disease": True,
        "autosomal genetic disease": True,
        "id": "MONDO:0009061",
        "equivalent_identifiers": [
          "UMLS:C0010674",
          "MEDDRA:10011762",
          "MEDDRA:10011764",
          "DOID:1485",
          "OMIM:219700",
          "MEDDRA:10028141",
          "MESH:D003550",
          "ORPHANET:586",
          "MONDO:0009061"
        ],
        "type": "disease",
        "rare disease": True,
        "autosomal recessive disease": True,
        "omnicorp_article_count": 50748
      },
      {
        "name": "pulmonary hypertension",
        "id": "MONDO:0005149",
        "equivalent_identifiers": [
          "UMLS:C3203102",
          "MEDDRA:10036727",
          "UMLS:C2973725",
          "UMLS:C0152171",
          "MONDO:0005149",
          "MEDDRA:10020787",
          "MONDO:0015924",
          "MESH:D006976",
          "ORPHANET:182090",
          "MEDDRA:10037403",
          "ORPHANET:275766",
          "MEDDRA:10065151",
          "MEDDRA:10037401",
          "MESH:D065627",
          "MESH:C536282",
          "UMLS:C0020542",
          "MONDO:0017147",
          "DOID:6432",
          "MEDDRA:10064911",
          "UMLS:CN202574",
          "UMLS:CN200519",
          "MEDDRA:10037400",
          "MEDDRA:10037405"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 26734
      },
      {
        "name": "amyloidosis (disease)",
        "systemic or rheumatic disease": True,
        "nutritional or metabolic disease": True,
        "id": "MONDO:0019065",
        "equivalent_identifiers": [
          "MEDDRA:10002023",
          "UMLS:C0002726",
          "MEDDRA:10002024",
          "MEDDRA:10002021",
          "MESH:D000686",
          "DOID:9120",
          "ORPHANET:69",
          "MONDO:0019065",
          "MEDDRA:10002022"
        ],
        "type": "disease",
        "omnicorp_article_count": 77839
      },
      {
        "name": "influenza",
        "id": "MONDO:0005812",
        "equivalent_identifiers": [
          "MESH:D007251",
          "DOID:8469",
          "MONDO:0005812"
        ],
        "transmissible disease": True,
        "type": "disease",
        "omnicorp_article_count": 78620
      },
      {
        "id": "MONDO:0005279",
        "equivalent_identifiers": [
          "DOID:9477",
          "MEDDRA:10014521",
          "MEDDRA:10037380",
          "MEDDRA:10050071",
          "MEDDRA:10034191",
          "MONDO:0005279",
          "MEDDRA:10014537",
          "MESH:D011655",
          "MEDDRA:10037377",
          "UMLS:C0034065"
        ],
        "name": "pulmonary embolism (disease)",
        "type": "disease",
        "omnicorp_article_count": 48125
      },
      {
        "equivalent_identifiers": [
          "OMIM:608437",
          "OMIM:613145",
          "OMIM:609903",
          "OMIM:612253",
          "UMLS:C1835309",
          "UMLS:C1835308",
          "OMIM:610927",
          "OMIM:605480",
          "OMIM:612254",
          "OMIM:601744",
          "OMIM:152700",
          "OMIM:605218",
          "UMLS:C0242380",
          "OMIM:609939",
          "MeSH:D008180",
          "Orphanet:536",
          "UMLS:C0024141",
          "OMIM:610065",
          "OMIM:612378",
          "OMIM:610066",
          "OMIM:300809",
          "MONDO:0007915",
          "EFO:0002690",
          "OMIM:614420",
          "UMLS:C2895176",
          "Orphanet:93552",
          "DOID:9074",
          "OMIM:612251"
        ],
        "name": "systemic lupus erythematosus (disease)",
        "id": "MONDO:0007915",
        "type": "disease",
        "omnicorp_article_count": 62089
      },
      {
        "id": "MONDO:0002076",
        "name": "pneumothorax (disease)",
        "equivalent_identifiers": [
          "MEDDRA:10035759",
          "DOID:1673",
          "MESH:D011030",
          "MONDO:0002076",
          "MEDDRA:10035763",
          "MEDDRA:10035762",
          "UMLS:C0149781",
          "UMLS:C0032326"
        ],
        "type": "disease",
        "omnicorp_article_count": 23805
      },
      {
        "id": "MONDO:0004492",
        "name": "mediastinitis",
        "equivalent_identifiers": [
          "UMLS:C0025064",
          "MEDDRA:10027082",
          "DOID:819",
          "MESH:D008480",
          "MONDO:0004492"
        ],
        "type": "disease",
        "omnicorp_article_count": 4403
      },
      {
        "id": "MONDO:0004670",
        "name": "lupus erythematosus",
        "equivalent_identifiers": [
          "MEDDRA:10025134",
          "UMLS:C0409974",
          "DOID:8857",
          "MEDDRA:10025131",
          "MONDO:0004670"
        ],
        "type": "disease",
        "omnicorp_article_count": 29831
      },
      {
        "name": "sarcoidosis",
        "systemic or rheumatic disease": True,
        "nutritional or metabolic disease": True,
        "id": "MONDO:0019338",
        "equivalent_identifiers": [
          "DOID:13402",
          "MONDO:0005764",
          "MONDO:0006804",
          "UMLS:C0036202",
          "DOID:626",
          "MedDRA:10039486",
          "OMIM:612387",
          "MONDO:0003832",
          "MONDO:0006611",
          "UMLS:C0036204",
          "UMLS:C0036203",
          "UMLS:C0036205",
          "MONDO:0001708",
          "Orphanet:797",
          "DOID:11335",
          "DOID:13406",
          "UMLS:C0477322",
          "OMIM:181000",
          "OMIM:612388",
          "MONDO:0019338",
          "UMLS:C0348826",
          "MeSH:D012507"
        ],
        "type": "disease",
        "rare disease": True,
        "syndromic disease": True,
        "omnicorp_article_count": 28946
      },
      {
        "id": "MONDO:0005275",
        "name": "lung disease",
        "equivalent_identifiers": [
          "MEDDRA:10013259",
          "MONDO:0005275",
          "MESH:D008171",
          "MEDDRA:10025083",
          "MEDDRA:10051054",
          "UMLS:C0024115",
          "MEDDRA:10037373",
          "MEDDRA:10013235",
          "MEDDRA:10048522",
          "MEDDRA:10049490",
          "MEDDRA:10025082",
          "DOID:850",
          "UMLS:C4021760"
        ],
        "type": "disease",
        "omnicorp_article_count": 115966
      },
      {
        "congenital abnormality": True,
        "name": "patent ductus arteriosus",
        "id": "MONDO:0011827",
        "equivalent_identifiers": [
          "DOID:13832",
          "UMLS:C0013274",
          "MONDO:0011827",
          "MESH:D004374"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 6974
      },
      {
        "name": "lung lymphangioleiomyomatosis",
        "id": "MONDO:0006277",
        "equivalent_identifiers": [
          "OMIM:606690",
          "DOID:3319",
          "ORPHANET:538",
          "MESH:D018192",
          "UMLS:C0751674",
          "UMLS:C0238399",
          "MEDDRA:10049462",
          "MEDDRA:10049459",
          "MONDO:0006277"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 327
      },
      {
        "name": "glomerulonephritis (disease)",
        "id": "MONDO:0002462",
        "equivalent_identifiers": [
          "MONDO:0002462",
          "MEDDRA:10029143",
          "MEDDRA:10018375",
          "UMLS:C0017658",
          "MEDDRA:10018364",
          "DOID:2921",
          "MESH:D005921"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 40524
      },
      {
        "congenital abnormality": True,
        "name": "hereditary hemorrhagic telangiectasia",
        "monogenic disease": True,
        "autosomal genetic disease": True,
        "autosomal dominant disease": True,
        "systemic or rheumatic disease": True,
        "id": "MONDO:0019180",
        "equivalent_identifiers": [
          "MEDDRA:10019883",
          "MEDDRA:10019887",
          "MONDO:0019180",
          "UMLS:C0039445",
          "MEDDRA:10031132",
          "MESH:D013683",
          "MEDDRA:10020023",
          "ORPHANET:774",
          "DOID:1270",
          "MEDDRA:10038554"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 2660
      },
      {
        "id": "MONDO:0002363",
        "name": "papilloma",
        "equivalent_identifiers": [
          "MEDDRA:10033715",
          "MONDO:0002363",
          "MEDDRA:10033713",
          "MESH:D010212",
          "UMLS:C0030354",
          "MEDDRA:10033725",
          "DOID:2615"
        ],
        "type": "disease",
        "omnicorp_article_count": 19600
      },
      {
        "id": "MONDO:0003781",
        "name": "bronchitis",
        "equivalent_identifiers": [
          "UMLS:C0006277",
          "MEDDRA:10006462",
          "MEDDRA:10066672",
          "MEDDRA:10006451",
          "MONDO:0003781",
          "MEDDRA:10006461",
          "MESH:D001991",
          "MEDDRA:10006452",
          "UMLS:C0149514",
          "MEDDRA:10000687",
          "MEDDRA:10006453",
          "DOID:6132"
        ],
        "type": "disease",
        "omnicorp_article_count": 30298
      },
      {
        "name": "antiphospholipid syndrome",
        "id": "MONDO:0007140",
        "equivalent_identifiers": [
          "MONDO:0007140",
          "MEDDRA:10002817",
          "DOID:2988",
          "UMLS:C0085278",
          "OMIM:107320",
          "MESH:D016736"
        ],
        "type": "disease",
        "syndromic disease": True,
        "omnicorp_article_count": 9233
      },
      {
        "id": "MONDO:0001243",
        "equivalent_identifiers": [
          "MEDDRA:10013441",
          "MESH:D004211",
          "UMLS:C0012739",
          "MONDO:0001243",
          "MEDDRA:10012126",
          "DOID:11247",
          "MEDDRA:10010785",
          "MEDDRA:10012769",
          "UMLS:C4321305",
          "MEDDRA:10013442",
          "MEDDRA:10010786",
          "MEDDRA:10013429"
        ],
        "name": "disseminated intravascular coagulation",
        "type": "disease",
        "omnicorp_article_count": 17611
      },
      {
        "name": "pneumocystosis",
        "id": "MONDO:0019121",
        "equivalent_identifiers": [
          "MONDO:0019121",
          "MEDDRA:10073755",
          "DOID:11339",
          "UMLS:C1535939",
          "ORPHANET:723",
          "MEDDRA:10051460",
          "MEDDRA:10064108",
          "MESH:D011020",
          "MEDDRA:10035659",
          "MEDDRA:10035661",
          "MEDDRA:10035662",
          "MEDDRA:10034184"
        ],
        "transmissible disease": True,
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 20325
      },
      {
        "name": "Takayasu arteritis",
        "systemic or rheumatic disease": True,
        "id": "MONDO:0017991",
        "equivalent_identifiers": [
          "MESH:D013625",
          "OMIM:207600",
          "ORPHANET:3287",
          "MEDDRA:10043098",
          "MEDDRA:10043097",
          "MEDDRA:10037496",
          "MONDO:0017991",
          "DOID:2508",
          "UMLS:C0039263"
        ],
        "type": "disease",
        "rare disease": True,
        "syndromic disease": True,
        "omnicorp_article_count": 5847
      },
      {
        "id": "MONDO:0005160",
        "name": "aortic aneurysm (disease)",
        "equivalent_identifiers": [
          "DOID:3627",
          "MEDDRA:10043481",
          "UMLS:C1305122",
          "MONDO:0005160",
          "MEDDRA:10002339",
          "UMLS:C0741160",
          "MEDDRA:10002330",
          "MEDDRA:10002886",
          "UMLS:C0003486",
          "MEDDRA:10043464",
          "UMLS:C0265010",
          "MEDDRA:10002884",
          "MEDDRA:10000053",
          "MESH:D001014",
          "MEDDRA:10002882",
          "UMLS:C0265012"
        ],
        "type": "disease",
        "omnicorp_article_count": 47506
      },
      {
        "id": "MONDO:0004822",
        "name": "bronchiectasis",
        "equivalent_identifiers": [
          "MONDO:0004822",
          "MEDDRA:10006446",
          "UMLS:C0006267",
          "MEDDRA:10006445",
          "MESH:D001987",
          "DOID:9563"
        ],
        "type": "disease",
        "omnicorp_article_count": 11028
      },
      {
        "id": "MONDO:0006932",
        "name": "pulmonary edema",
        "equivalent_identifiers": [
          "UMLS:C0034063",
          "MEDDRA:10037424",
          "MEDDRA:10055929",
          "MEDDRA:10037375",
          "MEDDRA:10025084",
          "MESH:D011654",
          "DOID:11396",
          "MEDDRA:10030126",
          "MEDDRA:10037423",
          "MEDDRA:10037426",
          "MONDO:0006932",
          "MEDDRA:10025112",
          "MEDDRA:10014233",
          "MEDDRA:10014253"
        ],
        "type": "disease",
        "omnicorp_article_count": 22442
      },
      {
        "name": "aspergillosis",
        "id": "MONDO:0005657",
        "equivalent_identifiers": [
          "MONDO:0005657",
          "MEDDRA:10003488",
          "MEDDRA:10051356",
          "MEDDRA:10051619",
          "ORPHANET:1163",
          "MESH:D001228",
          "MEDDRA:10074171",
          "DOID:13564",
          "UMLS:C0004030",
          "MEDDRA:10003486"
        ],
        "transmissible disease": True,
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 16908
      },
      {
        "id": "MONDO:0004849",
        "name": "pulmonary emphysema",
        "equivalent_identifiers": [
          "DOID:9675",
          "MESH:D011656",
          "MEDDRA:10014563",
          "MEDDRA:10014561",
          "UMLS:C0034067",
          "MONDO:0004849",
          "MESH:D004646"
        ],
        "type": "disease",
        "omnicorp_article_count": 16078
      },
      {
        "name": "leiomyosarcoma",
        "id": "MONDO:0005058",
        "equivalent_identifiers": [
          "MEDDRA:10024189",
          "ORPHANET:64720",
          "UMLS:C0023269",
          "MONDO:0005058",
          "MEDDRA:10024190",
          "MESH:D007890",
          "MEDDRA:10024193",
          "DOID:1967"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 10800
      },
      {
        "id": "MONDO:0005396",
        "name": "thoracic aortic aneurysm",
        "equivalent_identifiers": [
          "MESH:D017545",
          "UMLS:C0162872",
          "DOID:14004",
          "MONDO:0005396",
          "MEDDRA:10043465"
        ],
        "type": "disease",
        "omnicorp_article_count": 2475
      },
      {
        "name": "pleural empyema (disease)",
        "id": "MONDO:0018667",
        "equivalent_identifiers": [
          "MONDO:0018667",
          "MESH:D016724",
          "MEDDRA:10037658",
          "ORPHANET:449266",
          "UMLS:C0014013",
          "MEDDRA:10037381",
          "DOID:3798"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 11544
      },
      {
        "name": "Behcet disease",
        "systemic or rheumatic disease": True,
        "id": "MONDO:0007191",
        "equivalent_identifiers": [
          "MEDDRA:10004213",
          "MEDDRA:10004211",
          "UMLS:C0004943",
          "MESH:D001528",
          "MONDO:0007191",
          "OMIM:109650",
          "DOID:13241",
          "ORPHANET:117",
          "MEDDRA:10004212",
          "MEDDRA:10004215"
        ],
        "type": "disease",
        "rare disease": True,
        "syndromic disease": True,
        "omnicorp_article_count": 8852
      },
      {
        "name": "leptospirosis",
        "id": "MONDO:0005825",
        "equivalent_identifiers": [
          "MEDDRA:10024234",
          "MEDDRA:10024238",
          "DOID:2297",
          "MEDDRA:10024241",
          "ORPHANET:509",
          "UMLS:C0023364",
          "MONDO:0005825",
          "MESH:D007922"
        ],
        "transmissible disease": True,
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 8791
      },
      {
        "name": "granulomatosis with polyangiitis",
        "systemic or rheumatic disease": True,
        "id": "MONDO:0012105",
        "equivalent_identifiers": [
          "MEDDRA:10047888",
          "DOID:12132",
          "UMLS:C3495801",
          "ORPHANET:900",
          "OMIM:608710",
          "MEDDRA:10072579",
          "UMLS:C4050407",
          "MONDO:0012105",
          "UMLS:C0043092",
          "MEDDRA:10072580",
          "MESH:D014890",
          "MEDDRA:10047889"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 13257
      },
      {
        "id": "MONDO:0002568",
        "name": "tracheal stenosis",
        "equivalent_identifiers": [
          "MEDDRA:10050816",
          "UMLS:C0040583",
          "DOID:3227",
          "MESH:D014135",
          "MONDO:0002568"
        ],
        "type": "disease",
        "omnicorp_article_count": 6111
      },
      {
        "name": "strongyloidiasis",
        "id": "MONDO:0005974",
        "equivalent_identifiers": [
          "UMLS:C0038463",
          "MESH:D013322",
          "MEDDRA:10042252",
          "ORPHANET:76",
          "MONDO:0005974",
          "DOID:10955",
          "UMLS:C0348996",
          "MEDDRA:10042254",
          "UMLS:C0085810"
        ],
        "transmissible disease": True,
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 3783
      },
      {
        "name": "aortitis",
        "systemic or rheumatic disease": True,
        "id": "MONDO:0006656",
        "equivalent_identifiers": [
          "MESH:D001025",
          "MEDDRA:10002921",
          "UMLS:C0003509",
          "MONDO:0006656",
          "DOID:519",
          "MEDDRA:10002922"
        ],
        "type": "disease",
        "rare disease": True,
        "omnicorp_article_count": 2411
      },
      {
        "name": "MET",
        "location": "7q31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Receptor tyrosine kinases",
          "Deafness associated genes",
          "IPT domain containing"
        ],
        "chromosome": "7",
        "id": "HGNC:7029",
        "equivalent_identifiers": [
          "UniProtKB:P08581",
          "ENSEMBL:ENSG00000105976",
          "NCBIGene:4233",
          "HGNC:7029",
          "HGNC.SYMBOL:MET"
        ],
        "taxon": "9606",
        "gene_family_id": [
          321,
          1152,
          1752
        ],
        "type": "gene",
        "omnicorp_article_count": 303503
      },
      {
        "name": "EGFR",
        "location": "7p11.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Erb-b2 receptor tyrosine kinases"
        ],
        "chromosome": "7",
        "id": "HGNC:3236",
        "equivalent_identifiers": [
          "HGNC:3236",
          "NCBIGENE:1956",
          "ENSEMBL:ENSG00000146648",
          "HGNC.SYMBOL:EGFR",
          "UniProtKB:P00533",
          "NCBIGene:1956"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1096
        ],
        "type": "gene",
        "omnicorp_article_count": 42417
      },
      {
        "name": "F2",
        "location": "11p11.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands",
          "Gla domain containing",
          "Complement system regulators and receptors"
        ],
        "chromosome": "11",
        "id": "HGNC:3535",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000180210",
          "UniProtKB:E9PIT3",
          "NCBIGENE:2147",
          "UniProtKB:C9JV37",
          "HGNC:3535",
          "UniProtKB:P00734"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542,
          1250,
          1639
        ],
        "type": "gene",
        "omnicorp_article_count": 2459
      },
      {
        "name": "APP",
        "location": "21q21.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands"
        ],
        "chromosome": "21",
        "id": "HGNC:620",
        "equivalent_identifiers": [
          "UniProtKB:P05067",
          "HGNC:620",
          "NCBIGENE:351",
          "HGNC.SYMBOL:APP",
          "ENSEMBL:ENSG00000142192",
          "NCBIGene:351"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542
        ],
        "type": "gene",
        "omnicorp_article_count": 15614
      },
      {
        "name": "JUN",
        "location": "1p32.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Basic leucine zipper proteins",
          "Jun transcription factor family"
        ],
        "chromosome": "1",
        "id": "HGNC:6204",
        "equivalent_identifiers": [
          "UniProtKB:P05412",
          "HGNC.SYMBOL:JUN",
          "ENSEMBL:ENSG00000177606",
          "HGNC:6204",
          "NCBIGene:3725"
        ],
        "taxon": "9606",
        "gene_family_id": [
          506,
          1257
        ],
        "type": "gene",
        "omnicorp_article_count": 6848
      },
      {
        "name": "AR",
        "location": "Xq12",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Nuclear hormone receptors"
        ],
        "chromosome": "Xq",
        "id": "HGNC:644",
        "equivalent_identifiers": [
          "NCBIGene:367",
          "NCBIGENE:367",
          "ENSEMBL:ENSG00000169083",
          "UniProtKB:P10275",
          "HGNC:644",
          "HGNC.SYMBOL:AR"
        ],
        "taxon": "9606",
        "gene_family_id": [
          71
        ],
        "type": "gene",
        "omnicorp_article_count": 25867
      },
      {
        "name": "TNF",
        "location": "6p21.33",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Tumor necrosis factor superfamily"
        ],
        "chromosome": "6",
        "id": "HGNC:11892",
        "equivalent_identifiers": [
          "NCBIGene:7124",
          "HGNC.SYMBOL:TNF",
          "ENSEMBL:ENSG00000232810",
          "HGNC:11892",
          "UniProtKB:P01375"
        ],
        "taxon": "9606",
        "gene_family_id": [
          781
        ],
        "type": "gene",
        "omnicorp_article_count": 37726
      },
      {
        "name": "TP53",
        "location": "17p13.1",
        "locus_group": "protein-coding gene",
        "chromosome": "17",
        "id": "HGNC:11998",
        "equivalent_identifiers": [
          "UniProtKB:P04637",
          "NCBIGene:7157",
          "HGNC:11998",
          "HGNC.SYMBOL:TP53",
          "NCBIGENE:7157",
          "ENSEMBL:ENSG00000141510"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 13943
      },
      {
        "name": "FES",
        "location": "15q26.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "SH2 domain containing",
          "F-BAR domain containing ",
          "Fes family tyrosine kinases"
        ],
        "chromosome": "15",
        "id": "HGNC:3657",
        "equivalent_identifiers": [
          "NCBIGene:2242",
          "HGNC.SYMBOL:FES",
          "HGNC:3657",
          "UniProtKB:P07332",
          "UniProtKB:P07332",
          "ENSEMBL:ENSG00000182511"
        ],
        "taxon": "9606",
        "gene_family_id": [
          741,
          1288,
          1461
        ],
        "type": "gene",
        "omnicorp_article_count": 3518
      },
      {
        "name": "RARA",
        "location": "17q21.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Nuclear hormone receptors"
        ],
        "chromosome": "17",
        "id": "HGNC:9864",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:RARA",
          "NCBIGENE:5914",
          "UniProtKB:P10276",
          "HGNC:9864",
          "ENSEMBL:ENSG00000131759",
          "NCBIGene:5914"
        ],
        "taxon": "9606",
        "gene_family_id": [
          71
        ],
        "type": "gene",
        "omnicorp_article_count": 1998
      },
      {
        "name": "VDR",
        "location": "12q13.11",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Nuclear hormone receptors",
          "Protein phosphatase 1 regulatory subunits"
        ],
        "chromosome": "12",
        "id": "HGNC:12679",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:VDR",
          "NCBIGene:7421",
          "UniProtKB:P11473",
          "ENSEMBL:ENSG00000111424",
          "UniProtKB:P11473",
          "HGNC:12679"
        ],
        "taxon": "9606",
        "gene_family_id": [
          71,
          694
        ],
        "type": "gene",
        "omnicorp_article_count": 5751
      },
      {
        "name": "VEGFA",
        "location": "6p21.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "VEGF family"
        ],
        "chromosome": "6",
        "id": "HGNC:12680",
        "equivalent_identifiers": [
          "NCBIGene:7422",
          "HGNC.SYMBOL:VEGFA",
          "HGNC:12680",
          "UniProtKB:P15692",
          "ENSEMBL:ENSG00000112715",
          "NCBIGENE:7422"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1267
        ],
        "type": "gene",
        "omnicorp_article_count": 11259
      },
      {
        "name": "SMAD4",
        "location": "18q21.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "SMAD family"
        ],
        "chromosome": "18",
        "id": "HGNC:6770",
        "equivalent_identifiers": [
          "UniProtKB:Q13485",
          "HGNC.SYMBOL:SMAD4",
          "HGNC:6770",
          "ENSEMBL:ENSG00000141646",
          "NCBIGene:4089"
        ],
        "taxon": "9606",
        "gene_family_id": [
          750
        ],
        "type": "gene",
        "omnicorp_article_count": 3461
      },
      {
        "name": "SMAD3",
        "location": "15q22.33",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "SMAD family"
        ],
        "chromosome": "15",
        "id": "HGNC:6769",
        "equivalent_identifiers": [
          "NCBIGENE:4088",
          "UniProtKB:H0YMY0",
          "UniProtKB:H0YKE2",
          "UniProtKB:H3BQ00",
          "UniProtKB:A0A024R5Z3",
          "UniProtKB:P84022",
          "UniProtKB:H0YL71",
          "HGNC:6769",
          "ENSEMBL:ENSG00000166949",
          "UniProtKB:H0YNV1",
          "UniProtKB:Q9P0T0",
          "UniProtKB:H0YMP2",
          "UniProtKB:H3BVD1",
          "UniProtKB:H3BP09"
        ],
        "taxon": "9606",
        "gene_family_id": [
          750
        ],
        "type": "gene",
        "omnicorp_article_count": 4818
      },
      {
        "name": "TGFBR2",
        "location": "3p24.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Type 2 receptor serine/threonine kinases"
        ],
        "chromosome": "3",
        "id": "HGNC:11773",
        "equivalent_identifiers": [
          "HGNC:11773",
          "UniProtKB:P37173",
          "ENSEMBL:ENSG00000163513",
          "UniProtKB:P37173",
          "HGNC.SYMBOL:TGFBR2",
          "NCBIGene:7048"
        ],
        "taxon": "9606",
        "gene_family_id": [
          346
        ],
        "type": "gene",
        "omnicorp_article_count": 648
      },
      {
        "name": "NODAL",
        "location": "10q22.1",
        "locus_group": "protein-coding gene",
        "chromosome": "10",
        "id": "HGNC:7865",
        "equivalent_identifiers": [
          "HGNC:7865",
          "HGNC.SYMBOL:NODAL",
          "ENSEMBL:ENSG00000156574",
          "NCBIGene:4838",
          "UniProtKB:Q96S42"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 38334
      },
      {
        "name": "PDGFRA",
        "location": "4q12",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Receptor tyrosine kinases",
          "CD molecules",
          "I-set domain containing"
        ],
        "chromosome": "4",
        "id": "HGNC:8803",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:PDGFRA",
          "NCBIGene:5156",
          "UniProtKB:P16234",
          "ENSEMBL:ENSG00000134853",
          "HGNC:8803"
        ],
        "taxon": "9606",
        "gene_family_id": [
          321,
          471,
          593
        ],
        "type": "gene",
        "omnicorp_article_count": 1447
      },
      {
        "name": "TGFB2",
        "location": "1q41",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands",
          "Transforming growth factor beta family"
        ],
        "chromosome": "1",
        "id": "HGNC:11768",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:TGFB2",
          "NCBIGene:7042",
          "UniProtKB:P61812",
          "NCBIGENE:7042",
          "ENSEMBL:ENSG00000092969",
          "HGNC:11768"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542,
          1664
        ],
        "type": "gene",
        "omnicorp_article_count": 614
      },
      {
        "name": "NKX2-1",
        "location": "14q13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "NKL subclass homeoboxes and pseudogenes"
        ],
        "chromosome": "14",
        "id": "HGNC:11825",
        "equivalent_identifiers": [
          "UniProtKB:P43699",
          "HGNC.SYMBOL:NKX2-1",
          "NCBIGene:7080",
          "HGNC:11825",
          "ENSEMBL:ENSG00000136352"
        ],
        "taxon": "9606",
        "gene_family_id": [
          519
        ],
        "type": "gene",
        "omnicorp_article_count": 1007
      },
      {
        "name": "CDK4",
        "location": "12q14.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Cyclin dependent kinases",
          "MicroRNA protein coding host genes"
        ],
        "chromosome": "12",
        "id": "HGNC:1773",
        "equivalent_identifiers": [
          "HGNC:1773",
          "ENSEMBL:ENSG00000135446",
          "NCBIGene:1019",
          "UniProtKB:P11802",
          "HGNC.SYMBOL:CDK4",
          "NCBIGENE:1019"
        ],
        "taxon": "9606",
        "gene_family_id": [
          496,
          1691
        ],
        "type": "gene",
        "omnicorp_article_count": 5083
      },
      {
        "name": "WT1",
        "location": "11p13",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Zinc fingers C2H2-type"
        ],
        "chromosome": "11",
        "id": "HGNC:12796",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:WT1",
          "HGNC:12796",
          "NCBIGENE:7490",
          "UniProtKB:P19544",
          "NCBIGene:7490",
          "ENSEMBL:ENSG00000184937"
        ],
        "taxon": "9606",
        "gene_family_id": [
          28
        ],
        "type": "gene",
        "omnicorp_article_count": 3823
      },
      {
        "name": "CFTR",
        "location": "7q31.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Chloride channels, ATP-gated CFTR",
          "ATP binding cassette subfamily C"
        ],
        "chromosome": "7",
        "id": "HGNC:1884",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000001626",
          "NCBIGene:1080",
          "NCBIGENE:1080",
          "HGNC.SYMBOL:CFTR",
          "HGNC:1884",
          "UniProtKB:P13569"
        ],
        "taxon": "9606",
        "gene_family_id": [
          309,
          807
        ],
        "type": "gene",
        "omnicorp_article_count": 9263
      },
      {
        "name": "ACHE",
        "location": "7q22.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Blood group antigens"
        ],
        "chromosome": "7",
        "id": "HGNC:108",
        "equivalent_identifiers": [
          "UniProtKB:P22303",
          "HGNC.SYMBOL:ACHE",
          "NCBIGene:43",
          "ENSEMBL:ENSG00000087085",
          "HGNC:108"
        ],
        "taxon": "9606",
        "gene_family_id": [
          454
        ],
        "type": "gene",
        "omnicorp_article_count": 15083
      },
      {
        "name": "CD14",
        "location": "5q31.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Scavenger receptors"
        ],
        "chromosome": "5",
        "id": "HGNC:1628",
        "equivalent_identifiers": [
          "HGNC:1628",
          "UniProtKB:P08571",
          "ENSEMBL:ENSG00000170458",
          "NCBIGene:929",
          "NCBIGENE:929",
          "HGNC.SYMBOL:CD14"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          1253
        ],
        "type": "gene",
        "omnicorp_article_count": 7673
      },
      {
        "name": "SKI",
        "location": "1p36.33-p36.32",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "SKI transcriptional corepressors"
        ],
        "chromosome": "1",
        "id": "HGNC:10896",
        "equivalent_identifiers": [
          "UniProtKB:P12755",
          "HGNC:10896",
          "ENSEMBL:ENSG00000157933",
          "HGNC.SYMBOL:SKI",
          "NCBIGene:6497"
        ],
        "taxon": "9606",
        "gene_family_id": [
          748
        ],
        "type": "gene",
        "omnicorp_article_count": 4801
      },
      {
        "name": "CD34",
        "location": "1q32.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules"
        ],
        "chromosome": "1",
        "id": "HGNC:1662",
        "equivalent_identifiers": [
          "HGNC:1662",
          "ENSEMBL:ENSG00000174059",
          "NCBIGene:947",
          "UniProtKB:P28906",
          "HGNC.SYMBOL:CD34"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471
        ],
        "type": "gene",
        "omnicorp_article_count": 23324
      },
      {
        "name": "TGFBR1",
        "location": "9q22.33",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Type 1 receptor serine/threonine kinases"
        ],
        "chromosome": "9",
        "id": "HGNC:11772",
        "equivalent_identifiers": [
          "UniProtKB:P36897",
          "ENSEMBL:ENSG00000106799",
          "HGNC.SYMBOL:TGFBR1",
          "HGNC:11772",
          "NCBIGene:7046"
        ],
        "taxon": "9606",
        "gene_family_id": [
          345
        ],
        "type": "gene",
        "omnicorp_article_count": 405
      },
      {
        "name": "HRAS",
        "location": "11p15.5",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "RAS type GTPase family"
        ],
        "chromosome": "11",
        "id": "HGNC:5173",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000174775",
          "NCBIGene:3265",
          "UniProtKB:P01112",
          "NCBIGENE:3265",
          "HGNC.SYMBOL:HRAS",
          "HGNC:5173"
        ],
        "taxon": "9606",
        "gene_family_id": [
          389
        ],
        "type": "gene",
        "omnicorp_article_count": 2917
      },
      {
        "name": "TSC2",
        "location": "16p13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Protein phosphatase 1 regulatory subunits",
          "Armadillo-like helical domain containing",
          "TSC complex"
        ],
        "chromosome": "16",
        "id": "HGNC:12363",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000103197",
          "HGNC.SYMBOL:TSC2",
          "UniProtKB:P49815",
          "HGNC:12363",
          "NCBIGene:7249"
        ],
        "taxon": "9606",
        "gene_family_id": [
          694,
          1492,
          1497
        ],
        "type": "gene",
        "omnicorp_article_count": 1721
      },
      {
        "name": "ARC",
        "location": "8q24.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Gag like LTR retrotransposon derived genes"
        ],
        "chromosome": "8",
        "id": "HGNC:648",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:ARC",
          "HGNC:648",
          "UniProtKB:Q7LC44",
          "ENSEMBL:ENSG00000198576",
          "NCBIGene:23237"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1411
        ],
        "type": "gene",
        "omnicorp_article_count": 19158
      },
      {
        "name": "AVP",
        "location": "20p13",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands"
        ],
        "chromosome": "20",
        "id": "HGNC:894",
        "equivalent_identifiers": [
          "HGNC:894",
          "HGNC.SYMBOL:AVP",
          "NCBIGene:551",
          "NCBIGENE:551",
          "ENSEMBL:ENSG00000101200",
          "UniProtKB:P01185"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542
        ],
        "type": "gene",
        "omnicorp_article_count": 8710
      },
      {
        "name": "CD33",
        "location": "19q13.41",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "V-set domain containing",
          "Sialic acid binding Ig like lectins"
        ],
        "chromosome": "19",
        "id": "HGNC:1659",
        "equivalent_identifiers": [
          "NCBIGene:945",
          "UniProtKB:P20138",
          "HGNC:1659",
          "ENSEMBL:ENSG00000105383",
          "HGNC.SYMBOL:CD33"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          590,
          745
        ],
        "type": "gene",
        "omnicorp_article_count": 2124
      },
      {
        "name": "FLT3",
        "location": "13q12.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Receptor tyrosine kinases",
          "CD molecules",
          "Immunoglobulin like domain containing"
        ],
        "chromosome": "13",
        "id": "HGNC:3765",
        "equivalent_identifiers": [
          "UniProtKB:P36888",
          "HGNC:3765",
          "ENSEMBL:ENSG00000122025",
          "NCBIGene:2322",
          "HGNC.SYMBOL:FLT3"
        ],
        "taxon": "9606",
        "gene_family_id": [
          321,
          471,
          594
        ],
        "type": "gene",
        "omnicorp_article_count": 4169
      },
      {
        "name": "ADM",
        "location": "11p15.4",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands"
        ],
        "chromosome": "11",
        "id": "HGNC:259",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:ADM",
          "NCBIGENE:133",
          "NCBIGene:133",
          "UniProtKB:P35318",
          "HGNC:259",
          "ENSEMBL:ENSG00000148926"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542
        ],
        "type": "gene",
        "omnicorp_article_count": 3897
      },
      {
        "name": "TNFSF10",
        "location": "3q26",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Tumor necrosis factor superfamily"
        ],
        "chromosome": "3",
        "id": "HGNC:11925",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:TNFSF10",
          "ENSEMBL:ENSG00000121858",
          "UniProtKB:P50591",
          "NCBIGene:8743",
          "HGNC:11925"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          781
        ],
        "type": "gene",
        "omnicorp_article_count": 3150
      },
      {
        "name": "BST2",
        "location": "19p13.11",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules"
        ],
        "chromosome": "19",
        "id": "HGNC:1119",
        "equivalent_identifiers": [
          "UniProtKB:Q10589",
          "HGNC:1119",
          "NCBIGENE:684",
          "UniProtKB:A0A024R7H5",
          "ENSEMBL:ENSG00000130303"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471
        ],
        "type": "gene",
        "omnicorp_article_count": 443
      },
      {
        "name": "ROS1",
        "location": "6q22.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Receptor tyrosine kinases",
          "Fibronectin type III domain containing"
        ],
        "chromosome": "6",
        "id": "HGNC:10261",
        "equivalent_identifiers": [
          "NCBIGene:6098",
          "ENSEMBL:ENSG00000047936",
          "HGNC:10261",
          "HGNC.SYMBOL:ROS1",
          "UniProtKB:P08922"
        ],
        "taxon": "9606",
        "gene_family_id": [
          321,
          555
        ],
        "type": "gene",
        "omnicorp_article_count": 740
      },
      {
        "name": "KIT",
        "location": "4q12",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Receptor tyrosine kinases",
          "CD molecules",
          "Immunoglobulin like domain containing"
        ],
        "chromosome": "4",
        "id": "HGNC:6342",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:KIT",
          "NCBIGene:3815",
          "ENSEMBL:ENSG00000157404",
          "HGNC:6342",
          "UniProtKB:P10721"
        ],
        "taxon": "9606",
        "gene_family_id": [
          321,
          471,
          594
        ],
        "type": "gene",
        "omnicorp_article_count": 34091
      },
      {
        "name": "BRAF",
        "location": "7q34",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Mitogen-activated protein kinase kinase kinases",
          "RAF family"
        ],
        "chromosome": "7",
        "id": "HGNC:1097",
        "equivalent_identifiers": [
          "UniProtKB:P15056",
          "ENSEMBL:ENSG00000157764",
          "NCBIGene:673",
          "UniProtKB:P15056",
          "HGNC.SYMBOL:BRAF",
          "HGNC:1097"
        ],
        "taxon": "9606",
        "gene_family_id": [
          654,
          1157
        ],
        "type": "gene",
        "omnicorp_article_count": 9853
      },
      {
        "name": "BCL2",
        "location": "18q21.33",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Protein phosphatase 1 regulatory subunits",
          "BCL2 family"
        ],
        "chromosome": "18",
        "id": "HGNC:990",
        "equivalent_identifiers": [
          "HGNC:990",
          "ENSEMBL:ENSG00000171791",
          "NCBIGene:596",
          "NCBIGENE:596",
          "UniProtKB:P10415",
          "HGNC.SYMBOL:BCL2"
        ],
        "taxon": "9606",
        "gene_family_id": [
          694,
          1057
        ],
        "type": "gene",
        "omnicorp_article_count": 6387
      },
      {
        "name": "APC",
        "location": "5q22.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Armadillo repeat containing",
          "Protein phosphatase 1 regulatory subunits"
        ],
        "chromosome": "5",
        "id": "HGNC:583",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000134982",
          "NCBIGENE:324",
          "HGNC.SYMBOL:APC",
          "HGNC:583",
          "NCBIGene:324",
          "UniProtKB:P25054"
        ],
        "taxon": "9606",
        "gene_family_id": [
          409,
          694
        ],
        "type": "gene",
        "omnicorp_article_count": 17981
      },
      {
        "name": "MTOR",
        "location": "1p36.22",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "MTOR complex 1",
          "MTOR complex 2",
          "Armadillo-like helical domain containing"
        ],
        "chromosome": "1",
        "id": "HGNC:3942",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:MTOR",
          "ENSEMBL:ENSG00000198793",
          "NCBIGENE:2475",
          "HGNC:3942",
          "NCBIGene:2475",
          "UniProtKB:P42345"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1332,
          1333,
          1492
        ],
        "type": "gene",
        "omnicorp_article_count": 18168
      },
      {
        "name": "PC",
        "location": "11q13.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "MicroRNA protein coding host genes"
        ],
        "chromosome": "11",
        "id": "HGNC:8636",
        "equivalent_identifiers": [
          "UniProtKB:P11498",
          "HGNC.SYMBOL:PC",
          "UniProtKB:P11498",
          "NCBIGene:5091",
          "HGNC:8636",
          "ENSEMBL:ENSG00000173599"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1691
        ],
        "type": "gene",
        "omnicorp_article_count": 26322
      },
      {
        "name": "MTHFR",
        "location": "1p36.22",
        "locus_group": "protein-coding gene",
        "chromosome": "1",
        "id": "HGNC:7436",
        "equivalent_identifiers": [
          "UniProtKB:P42898",
          "HGNC.SYMBOL:MTHFR",
          "ENSEMBL:ENSG00000177000",
          "NCBIGene:4524",
          "HGNC:7436"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 5666
      },
      {
        "name": "TAT",
        "location": "16q22.2",
        "locus_group": "protein-coding gene",
        "chromosome": "16",
        "id": "HGNC:11573",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:TAT",
          "UniProtKB:P17735",
          "ENSEMBL:ENSG00000198650",
          "NCBIGene:6898",
          "HGNC:11573"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 11629
      },
      {
        "name": "TLR2",
        "location": "4q31.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Toll like receptors"
        ],
        "chromosome": "4",
        "id": "HGNC:11848",
        "equivalent_identifiers": [
          "HGNC:11848",
          "HGNC.SYMBOL:TLR2",
          "NCBIGene:7097",
          "UniProtKB:O60603",
          "ENSEMBL:ENSG00000137462"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          948
        ],
        "type": "gene",
        "omnicorp_article_count": 8263
      },
      {
        "name": "CYP3A4",
        "location": "7q22.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Cytochrome P450 family 3"
        ],
        "chromosome": "7",
        "id": "HGNC:2637",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:CYP3A4",
          "UniProtKB:P08684",
          "NCBIGene:1576",
          "UniProtKB:P08684",
          "HGNC:2637",
          "ENSEMBL:ENSG00000160868"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1002
        ],
        "type": "gene",
        "omnicorp_article_count": 8155
      },
      {
        "name": "ENG",
        "location": "9q34.11",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules"
        ],
        "chromosome": "9",
        "id": "HGNC:3349",
        "equivalent_identifiers": [
          "UniProtKB:Q5T9B9",
          "NCBIGENE:2022",
          "HGNC:3349",
          "UniProtKB:F5GX88",
          "UniProtKB:A0A024R878",
          "UniProtKB:P17813",
          "UniProtKB:B7Z6Y5",
          "UniProtKB:Q96CG0",
          "ENSEMBL:ENSG00000106991"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471
        ],
        "type": "gene",
        "omnicorp_article_count": 6157
      },
      {
        "name": "COL3A1",
        "location": "2q32.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Collagens",
          "MicroRNA protein coding host genes"
        ],
        "chromosome": "2",
        "id": "HGNC:2201",
        "equivalent_identifiers": [
          "HGNC:2201",
          "NCBIGene:1281",
          "UniProtKB:P02461",
          "ENSEMBL:ENSG00000168542",
          "HGNC.SYMBOL:COL3A1"
        ],
        "taxon": "9606",
        "gene_family_id": [
          490,
          1691
        ],
        "type": "gene",
        "omnicorp_article_count": 751
      },
      {
        "name": "TTR",
        "location": "18q12.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Gla domain containing"
        ],
        "chromosome": "18",
        "id": "HGNC:12405",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:TTR",
          "NCBIGene:7276",
          "UniProtKB:P02766",
          "HGNC:12405",
          "ENSEMBL:ENSG00000118271"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1250
        ],
        "type": "gene",
        "omnicorp_article_count": 2965
      },
      {
        "name": "VWF",
        "location": "12p13.31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands"
        ],
        "chromosome": "12",
        "id": "HGNC:12726",
        "equivalent_identifiers": [
          "NCBIGene:7450",
          "ENSEMBL:ENSG00000110799",
          "NCBIGENE:7450",
          "HGNC.SYMBOL:VWF",
          "HGNC:12726",
          "UniProtKB:P04275"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542
        ],
        "type": "gene",
        "omnicorp_article_count": 8456
      },
      {
        "name": "MMP9",
        "location": "20q13.12",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "M10 matrix metallopeptidases"
        ],
        "chromosome": "20",
        "id": "HGNC:7176",
        "equivalent_identifiers": [
          "NCBIGENE:4318",
          "HGNC.SYMBOL:MMP9",
          "HGNC:7176",
          "UniProtKB:P14780",
          "ENSEMBL:ENSG00000100985",
          "NCBIGene:4318"
        ],
        "taxon": "9606",
        "gene_family_id": [
          891
        ],
        "type": "gene",
        "omnicorp_article_count": 5831
      },
      {
        "name": "HLA-DQA1",
        "location": "6p21.32",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Histocompatibility complex",
          "C1-set domain containing"
        ],
        "chromosome": "6",
        "id": "HGNC:4942",
        "equivalent_identifiers": [
          "UniProtKB:A0A0G2JKJ3",
          "UniProtKB:A0A182DWH0",
          "UniProtKB:P01909",
          "UniProtKB:A0A182DWF8",
          "UniProtKB:Q5Y7H0",
          "UniProtKB:A0A1W2PP70",
          "UniProtKB:A0A173ADG5",
          "UniProtKB:A0A182DWH1",
          "UniProtKB:Q08AS3",
          "UniProtKB:A0A140TA20",
          "UniProtKB:Q8MH44",
          "UniProtKB:E9PI37",
          "UniProtKB:F6UB03",
          "UniProtKB:E9PMV2",
          "HGNC:4942",
          "NCBIGENE:3117",
          "ENSEMBL:ENSG00000196735"
        ],
        "taxon": "9606",
        "gene_family_id": [
          588,
          591
        ],
        "type": "gene",
        "omnicorp_article_count": 1407
      },
      {
        "name": "KRAS",
        "location": "12p12.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "RAS type GTPase family"
        ],
        "chromosome": "12",
        "id": "HGNC:6407",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:KRAS",
          "NCBIGENE:3845",
          "HGNC:6407",
          "NCBIGene:3845",
          "UniProtKB:P01116",
          "ENSEMBL:ENSG00000133703"
        ],
        "taxon": "9606",
        "gene_family_id": [
          389
        ],
        "type": "gene",
        "omnicorp_article_count": 9010
      },
      {
        "name": "MDM2",
        "location": "12q15",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Ring finger proteins",
          "Zinc fingers RANBP2-type "
        ],
        "chromosome": "12",
        "id": "HGNC:6973",
        "equivalent_identifiers": [
          "HGNC:6973",
          "HGNC.SYMBOL:MDM2",
          "UniProtKB:Q00987",
          "ENSEMBL:ENSG00000135679",
          "NCBIGene:4193"
        ],
        "taxon": "9606",
        "gene_family_id": [
          58,
          89
        ],
        "type": "gene",
        "omnicorp_article_count": 7162
      },
      {
        "name": "CAT",
        "location": "11p13",
        "locus_group": "protein-coding gene",
        "chromosome": "11",
        "id": "HGNC:1516",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000121691",
          "UniProtKB:A0A3B3ITJ0",
          "NCBIGENE:847",
          "HGNC:1516",
          "UniProtKB:A0A384P5Q0",
          "UniProtKB:P04040"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 169299
      },
      {
        "name": "POR",
        "location": "7q11.23",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "MicroRNA protein coding host genes"
        ],
        "chromosome": "7",
        "id": "HGNC:9208",
        "equivalent_identifiers": [
          "UniProtKB:P16435",
          "NCBIGene:5447",
          "ENSEMBL:ENSG00000127948",
          "HGNC.SYMBOL:POR",
          "HGNC:9208",
          "UniProtKB:P16435"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1691
        ],
        "type": "gene",
        "omnicorp_article_count": 7819
      },
      {
        "name": "ACVRL1",
        "location": "12q13.13",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Type 1 receptor serine/threonine kinases"
        ],
        "chromosome": "12",
        "id": "HGNC:175",
        "equivalent_identifiers": [
          "HGNC:175",
          "UniProtKB:P37023",
          "NCBIGene:94",
          "HGNC.SYMBOL:ACVRL1",
          "ENSEMBL:ENSG00000139567"
        ],
        "taxon": "9606",
        "gene_family_id": [
          345
        ],
        "type": "gene",
        "omnicorp_article_count": 528
      },
      {
        "name": "CAMP",
        "location": "3p21.31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands"
        ],
        "chromosome": "3",
        "id": "HGNC:1472",
        "equivalent_identifiers": [
          "UniProtKB:P49913",
          "NCBIGENE:820",
          "ENSEMBL:ENSG00000164047",
          "HGNC.SYMBOL:CAMP",
          "HGNC:1472",
          "NCBIGene:820"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542
        ],
        "type": "gene",
        "omnicorp_article_count": 63877
      },
      {
        "name": "C3",
        "location": "19p13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands",
          "C3 and PZP like, alpha-2-macroglobulin domain containing",
          "Complement system activation components"
        ],
        "chromosome": "19",
        "id": "HGNC:1318",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000125730",
          "UniProtKB:P01024",
          "HGNC.SYMBOL:C3",
          "NCBIGene:718",
          "HGNC:1318"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542,
          1234,
          1638
        ],
        "type": "gene",
        "omnicorp_article_count": 4383
      },
      {
        "name": "C5",
        "location": "9q33.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands",
          "C3 and PZP like, alpha-2-macroglobulin domain containing",
          "Complement system activation components"
        ],
        "chromosome": "9",
        "id": "HGNC:1331",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:C5",
          "HGNC:1331",
          "NCBIGene:727",
          "ENSEMBL:ENSG00000106804",
          "UniProtKB:P01031"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542,
          1234,
          1638
        ],
        "type": "gene",
        "omnicorp_article_count": 1240
      },
      {
        "name": "NOS3",
        "location": "7q36.1",
        "locus_group": "protein-coding gene",
        "chromosome": "7",
        "id": "HGNC:7876",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:NOS3",
          "ENSEMBL:ENSG00000164867",
          "UniProtKB:P29474",
          "HGNC:7876",
          "UniProtKB:P29474",
          "NCBIGene:4846"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 7530
      },
      {
        "name": "IL6",
        "location": "7p15.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Interferons",
          "Interleukins",
          "Interleukin 6 type cytokine family"
        ],
        "chromosome": "7",
        "id": "HGNC:6018",
        "equivalent_identifiers": [
          "UniProtKB:B5MC21",
          "UniProtKB:B4DNQ5",
          "HGNC:6018",
          "UniProtKB:B5MC14",
          "UniProtKB:C9J5B0",
          "UniProtKB:B5MCZ3",
          "ENSEMBL:ENSG00000136244",
          "UniProtKB:B4DNV3",
          "UniProtKB:B4DVM1",
          "NCBIGENE:3569",
          "UniProtKB:Q75MH2",
          "UniProtKB:P05231"
        ],
        "taxon": "9606",
        "gene_family_id": [
          598,
          601,
          1264
        ],
        "type": "gene",
        "omnicorp_article_count": 9357
      },
      {
        "name": "EGF",
        "location": "4q25",
        "locus_group": "protein-coding gene",
        "chromosome": "4",
        "id": "HGNC:3229",
        "equivalent_identifiers": [
          "NCBIGene:1950",
          "HGNC.SYMBOL:EGF",
          "ENSEMBL:ENSG00000138798",
          "UniProtKB:P01133",
          "HGNC:3229"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 25677
      },
      {
        "name": "MCC",
        "location": "5q22.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "EF-hand domain containing"
        ],
        "chromosome": "5",
        "id": "HGNC:6935",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:MCC",
          "NCBIGene:4163",
          "ENSEMBL:ENSG00000171444",
          "HGNC:6935",
          "NCBIGENE:4163",
          "UniProtKB:P23508"
        ],
        "taxon": "9606",
        "gene_family_id": [
          863
        ],
        "type": "gene",
        "omnicorp_article_count": 4067
      },
      {
        "name": "TREX1",
        "location": "3p21.31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Exonucleases",
          "SET complex"
        ],
        "chromosome": "3",
        "id": "HGNC:12269",
        "equivalent_identifiers": [
          "UniProtKB:C9J052",
          "NCBIGENE:11277",
          "HGNC:12269",
          "UniProtKB:Q9NSU2",
          "ENSEMBL:ENSG00000213689",
          "UniProtKB:Q5TZT0"
        ],
        "taxon": "9606",
        "gene_family_id": [
          544,
          1659
        ],
        "type": "gene",
        "omnicorp_article_count": 179
      },
      {
        "name": "PALM",
        "location": "19p13.3",
        "locus_group": "protein-coding gene",
        "chromosome": "19",
        "id": "HGNC:8594",
        "equivalent_identifiers": [
          "NCBIGene:5064",
          "HGNC:8594",
          "UniProtKB:O75781",
          "HGNC.SYMBOL:PALM",
          "ENSEMBL:ENSG00000099864"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 12324
      },
      {
        "name": "TLR4",
        "location": "9q33.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Toll like receptors"
        ],
        "chromosome": "9",
        "id": "HGNC:11850",
        "equivalent_identifiers": [
          "NCBIGENE:7099",
          "ENSEMBL:ENSG00000136869",
          "UniProtKB:O00206",
          "HGNC:11850",
          "NCBIGene:7099",
          "HGNC.SYMBOL:TLR4"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          948
        ],
        "type": "gene",
        "omnicorp_article_count": 15009
      },
      {
        "name": "TSC1",
        "location": "9q34",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Armadillo-like helical domain containing",
          "TSC complex"
        ],
        "chromosome": "9",
        "id": "HGNC:12362",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:TSC1",
          "HGNC:12362",
          "UniProtKB:Q92574",
          "ENSEMBL:ENSG00000165699",
          "NCBIGene:7248"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1492,
          1497
        ],
        "type": "gene",
        "omnicorp_article_count": 1273
      },
      {
        "name": "PPL",
        "location": "16p13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Plakins"
        ],
        "chromosome": "16",
        "id": "HGNC:9273",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000118898",
          "HGNC:9273",
          "UniProtKB:O60437",
          "HGNC.SYMBOL:PPL",
          "NCBIGene:5493"
        ],
        "taxon": "9606",
        "gene_family_id": [
          939
        ],
        "type": "gene",
        "omnicorp_article_count": 1084
      },
      {
        "name": "MPO",
        "location": "17q22",
        "locus_group": "protein-coding gene",
        "chromosome": "17",
        "id": "HGNC:7218",
        "equivalent_identifiers": [
          "NCBIGENE:4353",
          "UniProtKB:P05164",
          "HGNC:7218",
          "UniProtKB:J3QSF7",
          "ENSEMBL:ENSG00000005381"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 9524
      },
      {
        "name": "CD163",
        "location": "12p13.31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Scavenger receptors",
          "Scavenger receptor cysteine rich domain containing"
        ],
        "chromosome": "12",
        "id": "HGNC:1631",
        "equivalent_identifiers": [
          "NCBIGene:9332",
          "HGNC:1631",
          "UniProtKB:Q86VB7",
          "HGNC.SYMBOL:CD163",
          "ENSEMBL:ENSG00000177575",
          "UniProtKB:Q86VB7"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          1253,
          1404
        ],
        "type": "gene",
        "omnicorp_article_count": 1967
      },
      {
        "name": "ALB",
        "location": "4q13.3",
        "locus_group": "protein-coding gene",
        "chromosome": "4",
        "id": "HGNC:399",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000163631",
          "UniProtKB:P02768",
          "HGNC.SYMBOL:ALB",
          "HGNC:399",
          "NCBIGene:213"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 2826
      },
      {
        "name": "ALK",
        "location": "2p23.2-p23.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Receptor tyrosine kinases",
          "CD molecules"
        ],
        "chromosome": "2",
        "id": "HGNC:427",
        "equivalent_identifiers": [
          "HGNC:427",
          "HGNC.SYMBOL:ALK",
          "NCBIGene:238",
          "ENSEMBL:ENSG00000171094",
          "UniProtKB:Q9UM73",
          "NCBIGENE:238"
        ],
        "taxon": "9606",
        "gene_family_id": [
          321,
          471
        ],
        "type": "gene",
        "omnicorp_article_count": 4109
      },
      {
        "name": "NTM",
        "location": "11q25",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "I-set domain containing",
          "IgLON cell adhesion molecules"
        ],
        "chromosome": "11",
        "id": "HGNC:17941",
        "equivalent_identifiers": [
          "NCBIGENE:50863",
          "UniProtKB:H7BZ62",
          "UniProtKB:Q9P121",
          "UniProtKB:B7Z1I4",
          "UniProtKB:C9J0V2",
          "UniProtKB:F6WFR7",
          "UniProtKB:F8W8Y1",
          "UniProtKB:F8VTR5",
          "HGNC:17941",
          "ENSEMBL:ENSG00000182667",
          "UniProtKB:C9JK95"
        ],
        "taxon": "9606",
        "gene_family_id": [
          593,
          1052
        ],
        "type": "gene",
        "omnicorp_article_count": 1902
      },
      {
        "name": "BID",
        "location": "22q11.21",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Endogenous ligands",
          "BCL2 homology region 3 (BH3) only",
          "MicroRNA protein coding host genes"
        ],
        "chromosome": "22",
        "id": "HGNC:1050",
        "equivalent_identifiers": [
          "UniProtKB:P55957",
          "HGNC:1050",
          "HGNC.SYMBOL:BID",
          "NCBIGene:637",
          "ENSEMBL:ENSG00000015475"
        ],
        "taxon": "9606",
        "gene_family_id": [
          542,
          1277,
          1691
        ],
        "type": "gene",
        "omnicorp_article_count": 11509
      },
      {
        "name": "MSC",
        "location": "8q13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Basic helix-loop-helix proteins"
        ],
        "chromosome": "8",
        "id": "HGNC:7321",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:MSC",
          "HGNC:7321",
          "ENSEMBL:ENSG00000178860",
          "NCBIGene:9242",
          "UniProtKB:O60682"
        ],
        "taxon": "9606",
        "gene_family_id": [
          420
        ],
        "type": "gene",
        "omnicorp_article_count": 11151
      },
      {
        "name": "CXCL2",
        "location": "4q13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Chemokine ligands",
          "Endogenous ligands"
        ],
        "chromosome": "4",
        "id": "HGNC:4603",
        "equivalent_identifiers": [
          "HGNC:4603",
          "HGNC.SYMBOL:CXCL2",
          "NCBIGene:2920",
          "UniProtKB:P19875",
          "ENSEMBL:ENSG00000081041"
        ],
        "taxon": "9606",
        "gene_family_id": [
          483,
          542
        ],
        "type": "gene",
        "omnicorp_article_count": 2373
      },
      {
        "name": "CRP",
        "location": "1q23.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Short pentraxins"
        ],
        "chromosome": "1",
        "id": "HGNC:2367",
        "equivalent_identifiers": [
          "UniProtKB:C9JRE9",
          "ENSEMBL:ENSG00000132693",
          "HGNC:2367",
          "UniProtKB:P02741",
          "UniProtKB:Q5VVP7",
          "NCBIGENE:1401"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1143
        ],
        "type": "gene",
        "omnicorp_article_count": 33000
      },
      {
        "name": "CD4",
        "location": "12p13.31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "V-set domain containing",
          "C2-set domain containing"
        ],
        "chromosome": "12",
        "id": "HGNC:1678",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000010610",
          "NCBIGene:920",
          "HGNC.SYMBOL:CD4",
          "NCBIGENE:920",
          "HGNC:1678",
          "UniProtKB:P01730"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          590,
          592
        ],
        "type": "gene",
        "omnicorp_article_count": 67595
      },
      {
        "name": "CD7",
        "location": "17q25.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "V-set domain containing"
        ],
        "chromosome": "17",
        "id": "HGNC:1695",
        "equivalent_identifiers": [
          "NCBIGene:924",
          "ENSEMBL:ENSG00000173762",
          "UniProtKB:P09564",
          "HGNC:1695",
          "HGNC.SYMBOL:CD7"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          590
        ],
        "type": "gene",
        "omnicorp_article_count": 1654
      },
      {
        "name": "IFNG",
        "location": "12q15",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Interferons"
        ],
        "chromosome": "12",
        "id": "HGNC:5438",
        "equivalent_identifiers": [
          "NCBIGENE:3458",
          "HGNC:5438",
          "UniProtKB:P01579",
          "NCBIGene:3458",
          "HGNC.SYMBOL:IFNG",
          "ENSEMBL:ENSG00000111537"
        ],
        "taxon": "9606",
        "gene_family_id": [
          598
        ],
        "type": "gene",
        "omnicorp_article_count": 1473
      },
      {
        "name": "CD1A",
        "location": "1q23.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "C1-set domain containing"
        ],
        "chromosome": "1",
        "id": "HGNC:1634",
        "equivalent_identifiers": [
          "UniProtKB:P06126",
          "HGNC:1634",
          "UniProtKB:P06126",
          "HGNC.SYMBOL:CD1A",
          "NCBIGene:909",
          "ENSEMBL:ENSG00000158477"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          591
        ],
        "type": "gene",
        "omnicorp_article_count": 2422
      },
      {
        "name": "CD79A",
        "location": "19q13.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "V-set domain containing"
        ],
        "chromosome": "19",
        "id": "HGNC:1698",
        "equivalent_identifiers": [
          "UniProtKB:M0QX61",
          "NCBIGENE:973",
          "ENSEMBL:ENSG00000105369",
          "HGNC:1698",
          "UniProtKB:P11912"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          590
        ],
        "type": "gene",
        "omnicorp_article_count": 1054
      },
      {
        "name": "FAS",
        "location": "10q23.31",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Tumor necrosis factor receptor superfamily",
          "Death inducing signaling complex "
        ],
        "chromosome": "10",
        "id": "HGNC:11920",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000026103",
          "UniProtKB:P25445",
          "NCBIGene:355",
          "HGNC:11920",
          "HGNC.SYMBOL:FAS"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          782,
          1342
        ],
        "type": "gene",
        "omnicorp_article_count": 45179
      },
      {
        "name": "SPN",
        "location": "16p11.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules"
        ],
        "chromosome": "16",
        "id": "HGNC:11249",
        "equivalent_identifiers": [
          "NCBIGENE:6693",
          "NCBIGene:6693",
          "HGNC:11249",
          "HGNC.SYMBOL:SPN",
          "ENSEMBL:ENSG00000197471",
          "UniProtKB:P16150"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471
        ],
        "type": "gene",
        "omnicorp_article_count": 1467
      },
      {
        "name": "BMPR2",
        "location": "2q33.1-q33.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Type 2 receptor serine/threonine kinases"
        ],
        "chromosome": "2",
        "id": "HGNC:1078",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000204217",
          "UniProtKB:Q13873",
          "HGNC.SYMBOL:BMPR2",
          "HGNC:1078",
          "NCBIGENE:659",
          "NCBIGene:659"
        ],
        "taxon": "9606",
        "gene_family_id": [
          346
        ],
        "type": "gene",
        "omnicorp_article_count": 800
      },
      {
        "name": "ATM",
        "location": "11q22.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Armadillo-like helical domain containing"
        ],
        "chromosome": "11",
        "id": "HGNC:795",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000149311",
          "HGNC.SYMBOL:ATM",
          "UniProtKB:Q13315",
          "HGNC:795",
          "NCBIGene:472"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1492
        ],
        "type": "gene",
        "omnicorp_article_count": 11653
      },
      {
        "name": "TEF",
        "location": "22q13.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "PAR bZIP family"
        ],
        "chromosome": "22",
        "id": "HGNC:11722",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:TEF",
          "UniProtKB:Q10587",
          "ENSEMBL:ENSG00000167074",
          "HGNC:11722",
          "NCBIGene:7008",
          "NCBIGENE:7008"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1248
        ],
        "type": "gene",
        "omnicorp_article_count": 1808
      },
      {
        "name": "HCCS",
        "location": "Xp22.2",
        "locus_group": "protein-coding gene",
        "chromosome": "Xp",
        "id": "HGNC:4837",
        "equivalent_identifiers": [
          "HGNC:4837",
          "NCBIGene:3052",
          "ENSEMBL:ENSG00000004961",
          "HGNC.SYMBOL:HCCS",
          "UniProtKB:P53701",
          "UniProtKB:P53701"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 4781
      },
      {
        "name": "AES",
        "location": "19p13.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "TLE family"
        ],
        "chromosome": "19",
        "id": "HGNC:307",
        "equivalent_identifiers": [
          "NCBIGENE:166",
          "ENSEMBL:ENSG00000104964",
          "HGNC:307",
          "NCBIGene:166",
          "HGNC.SYMBOL:AES",
          "UniProtKB:Q08117"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1680
        ],
        "type": "gene",
        "omnicorp_article_count": 9466
      },
      {
        "name": "G6PD",
        "location": "Xq28",
        "locus_group": "protein-coding gene",
        "chromosome": "Xq",
        "id": "HGNC:4057",
        "equivalent_identifiers": [
          "NCBIGENE:2539",
          "ENSEMBL:ENSG00000160211",
          "NCBIGene:2539",
          "UniProtKB:P11413",
          "HGNC:4057",
          "HGNC.SYMBOL:G6PD"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 3174
      },
      {
        "name": "ADAMTS13",
        "location": "9q34.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "ADAM metallopeptidases with thrombospondin type 1 motif"
        ],
        "chromosome": "9",
        "id": "HGNC:1366",
        "equivalent_identifiers": [
          "HGNC:1366",
          "NCBIGENE:11093",
          "NCBIGene:11093",
          "HGNC.SYMBOL:ADAMTS13",
          "ENSEMBL:ENSG00000160323",
          "UniProtKB:Q76LX8"
        ],
        "taxon": "9606",
        "gene_family_id": [
          50
        ],
        "type": "gene",
        "omnicorp_article_count": 1903
      },
      {
        "name": "ACE",
        "location": "17q23.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules"
        ],
        "chromosome": "17",
        "id": "HGNC:2707",
        "equivalent_identifiers": [
          "NCBIGene:1636",
          "HGNC:2707",
          "NCBIGENE:1636",
          "ENSEMBL:ENSG00000159640",
          "HGNC.SYMBOL:ACE",
          "UniProtKB:P12821"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471
        ],
        "type": "gene",
        "omnicorp_article_count": 17616
      },
      {
        "name": "TLR9",
        "location": "3p21.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Toll like receptors",
          "My-T-BRC complex"
        ],
        "chromosome": "3",
        "id": "HGNC:15633",
        "equivalent_identifiers": [
          "NCBIGene:54106",
          "UniProtKB:Q9NR96",
          "HGNC.SYMBOL:TLR9",
          "HGNC:15633",
          "UniProtKB:Q9NR96",
          "ENSEMBL:ENSG00000239732"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          948,
          1632
        ],
        "type": "gene",
        "omnicorp_article_count": 4112
      },
      {
        "name": "PCNA",
        "location": "20p12.3",
        "locus_group": "protein-coding gene",
        "chromosome": "20",
        "id": "HGNC:8729",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000132646",
          "HGNC.SYMBOL:PCNA",
          "HGNC:8729",
          "UniProtKB:P12004",
          "NCBIGene:5111"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 12573
      },
      {
        "name": "TST",
        "location": "22q12.3",
        "locus_group": "protein-coding gene",
        "chromosome": "22",
        "id": "HGNC:12388",
        "equivalent_identifiers": [
          "UniProtKB:Q16762",
          "UniProtKB:Q16762",
          "NCBIGene:7263",
          "HGNC:12388",
          "ENSEMBL:ENSG00000128311",
          "HGNC.SYMBOL:TST"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 4166
      },
      {
        "name": "NRAS",
        "location": "1p13.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "RAS type GTPase family"
        ],
        "chromosome": "1",
        "id": "HGNC:7989",
        "equivalent_identifiers": [
          "NCBIGene:4893",
          "HGNC:7989",
          "ENSEMBL:ENSG00000213281",
          "NCBIGENE:4893",
          "UniProtKB:P01111",
          "HGNC.SYMBOL:NRAS"
        ],
        "taxon": "9606",
        "gene_family_id": [
          389
        ],
        "type": "gene",
        "omnicorp_article_count": 2276
      },
      {
        "name": "GCA",
        "location": "2q24.2",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "EF-hand domain containing"
        ],
        "chromosome": "2",
        "id": "HGNC:15990",
        "equivalent_identifiers": [
          "UniProtKB:P28676",
          "NCBIGene:25801",
          "ENSEMBL:ENSG00000115271",
          "HGNC.SYMBOL:GCA",
          "HGNC:15990"
        ],
        "taxon": "9606",
        "gene_family_id": [
          863
        ],
        "type": "gene",
        "omnicorp_article_count": 2417
      },
      {
        "name": "CD68",
        "location": "17p13.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "CD molecules",
          "Scavenger receptors"
        ],
        "chromosome": "17",
        "id": "HGNC:1693",
        "equivalent_identifiers": [
          "NCBIGene:968",
          "ENSEMBL:ENSG00000129226",
          "HGNC:1693",
          "HGNC.SYMBOL:CD68",
          "UniProtKB:P34810"
        ],
        "taxon": "9606",
        "gene_family_id": [
          471,
          1253
        ],
        "type": "gene",
        "omnicorp_article_count": 7587
      },
      {
        "name": "MVP",
        "location": "16p11.2",
        "locus_group": "protein-coding gene",
        "chromosome": "16",
        "id": "HGNC:7531",
        "equivalent_identifiers": [
          "UniProtKB:Q14764",
          "HGNC.SYMBOL:MVP",
          "NCBIGene:9961",
          "ENSEMBL:ENSG00000013364",
          "NCBIGENE:9961",
          "HGNC:7531"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 1586
      },
      {
        "name": "DNASE1",
        "location": "16p13.3",
        "locus_group": "protein-coding gene",
        "chromosome": "16",
        "id": "HGNC:2956",
        "equivalent_identifiers": [
          "UniProtKB:P24855",
          "ENSEMBL:ENSG00000213918",
          "UniProtKB:I3L0Z9",
          "UniProtKB:I3L4U3",
          "UniProtKB:I3L298",
          "UniProtKB:I3L4C7",
          "UniProtKB:I3L530",
          "NCBIGENE:1773",
          "UniProtKB:I3L4B8",
          "HGNC:2956",
          "UniProtKB:I3L1N2"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 388
      },
      {
        "name": "GEM",
        "location": "8q22.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "RGK type GTPase family"
        ],
        "chromosome": "8",
        "id": "HGNC:4234",
        "equivalent_identifiers": [
          "ENSEMBL:ENSG00000164949",
          "UniProtKB:P55040",
          "HGNC.SYMBOL:GEM",
          "NCBIGene:2669",
          "HGNC:4234",
          "NCBIGENE:2669"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1260
        ],
        "type": "gene",
        "omnicorp_article_count": 3017
      },
      {
        "name": "CP",
        "location": "3q24-q25.1",
        "locus_group": "protein-coding gene",
        "chromosome": "3",
        "id": "HGNC:2295",
        "equivalent_identifiers": [
          "UniProtKB:P00450",
          "NCBIGene:1356",
          "HGNC:2295",
          "HGNC.SYMBOL:CP",
          "UniProtKB:P00450",
          "ENSEMBL:ENSG00000047457"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 25525
      },
      {
        "name": "AFP",
        "location": "4q13.3",
        "locus_group": "protein-coding gene",
        "chromosome": "4",
        "id": "HGNC:317",
        "equivalent_identifiers": [
          "UniProtKB:P02771",
          "HGNC:317",
          "HGNC.SYMBOL:AFP",
          "ENSEMBL:ENSG00000081051",
          "NCBIGene:174"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 11609
      },
      {
        "name": "NPL",
        "location": "1q25.3",
        "locus_group": "protein-coding gene",
        "chromosome": "1",
        "id": "HGNC:16781",
        "equivalent_identifiers": [
          "NCBIGENE:80896",
          "UniProtKB:Q9BXD5",
          "ENSEMBL:ENSG00000135838",
          "HGNC.SYMBOL:NPL",
          "HGNC:16781",
          "NCBIGene:80896"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 768
      },
      {
        "name": "MLANA",
        "location": "9p24.1",
        "locus_group": "protein-coding gene",
        "chromosome": "9",
        "id": "HGNC:7124",
        "equivalent_identifiers": [
          "UniProtKB:Q16655",
          "HGNC.SYMBOL:MLANA",
          "ENSEMBL:ENSG00000120215",
          "HGNC:7124",
          "NCBIGene:2315"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 888
      },
      {
        "name": "PTS",
        "location": "11q22.3",
        "locus_group": "protein-coding gene",
        "chromosome": "11",
        "id": "HGNC:9689",
        "equivalent_identifiers": [
          "UniProtKB:Q03393",
          "HGNC:9689",
          "NCBIGene:5805",
          "HGNC.SYMBOL:PTS",
          "ENSEMBL:ENSG00000150787"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 23874
      },
      {
        "name": "SON",
        "location": "21q22.11",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "G-patch domain containing",
          "Minor histocompatibility antigens",
          "MicroRNA protein coding host genes"
        ],
        "chromosome": "21",
        "id": "HGNC:11183",
        "equivalent_identifiers": [
          "HGNC:11183",
          "NCBIGENE:6651",
          "ENSEMBL:ENSG00000159140",
          "UniProtKB:P18583",
          "HGNC.SYMBOL:SON",
          "NCBIGene:6651"
        ],
        "taxon": "9606",
        "gene_family_id": [
          579,
          870,
          1691
        ],
        "type": "gene",
        "omnicorp_article_count": 24562
      },
      {
        "name": "MUC5AC",
        "location": "11p15.5",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Mucins"
        ],
        "chromosome": "11",
        "id": "HGNC:7515",
        "equivalent_identifiers": [
          "NCBIGene:4586",
          "UniProtKB:P98088",
          "HGNC.SYMBOL:MUC5AC",
          "HGNC:7515",
          "ENSEMBL:ENSG00000215182"
        ],
        "taxon": "9606",
        "gene_family_id": [
          648
        ],
        "type": "gene",
        "omnicorp_article_count": 2246
      },
      {
        "name": "SHE",
        "location": "1q21.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "SH2 domain containing"
        ],
        "chromosome": "1",
        "id": "HGNC:27004",
        "equivalent_identifiers": [
          "HGNC:27004",
          "UniProtKB:Q5VZ18",
          "NCBIGENE:126669",
          "UniProtKB:H0YJR4",
          "ENSEMBL:ENSG00000169291",
          "UniProtKB:H0YJQ6"
        ],
        "taxon": "9606",
        "gene_family_id": [
          741
        ],
        "type": "gene",
        "omnicorp_article_count": 100291
      },
      {
        "name": "IMPACT",
        "location": "18q11.2",
        "locus_group": "protein-coding gene",
        "chromosome": "18",
        "id": "HGNC:20387",
        "equivalent_identifiers": [
          "UniProtKB:Q9P2X3",
          "NCBIGene:55364",
          "ENSEMBL:ENSG00000154059",
          "HGNC.SYMBOL:IMPACT",
          "HGNC:20387"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 809794
      },
      {
        "name": "STAT4",
        "location": "2q32.2-q32.3",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "SH2 domain containing"
        ],
        "chromosome": "2",
        "id": "HGNC:11365",
        "equivalent_identifiers": [
          "HGNC:11365",
          "ENSEMBL:ENSG00000138378",
          "UniProtKB:E9PG69",
          "UniProtKB:A0A2R8Y693",
          "UniProtKB:C9JFG0",
          "UniProtKB:E9PBE2",
          "NCBIGENE:6775",
          "UniProtKB:C9JM11",
          "UniProtKB:Q14765"
        ],
        "taxon": "9606",
        "gene_family_id": [
          741
        ],
        "type": "gene",
        "omnicorp_article_count": 1311
      },
      {
        "name": "ADO",
        "location": "10q21.3",
        "locus_group": "protein-coding gene",
        "chromosome": "10",
        "id": "HGNC:23506",
        "equivalent_identifiers": [
          "HGNC:23506",
          "UniProtKB:Q96SZ5",
          "ENSEMBL:ENSG00000181915",
          "UniProtKB:Q96SZ5",
          "HGNC.SYMBOL:ADO",
          "NCBIGene:84890"
        ],
        "taxon": "9606",
        "type": "gene",
        "omnicorp_article_count": 2093
      },
      {
        "name": "VARS",
        "location": "6p21.33",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "Aminoacyl tRNA synthetases, Class I"
        ],
        "chromosome": "6",
        "id": "HGNC:12651",
        "equivalent_identifiers": [
          "HGNC.SYMBOL:VARS",
          "UniProtKB:P26640",
          "HGNC:12651",
          "ENSEMBL:ENSG00000204394",
          "NCBIGene:7407",
          "UniProtKB:P26640"
        ],
        "taxon": "9606",
        "gene_family_id": [
          131
        ],
        "type": "gene",
        "omnicorp_article_count": 17011
      },
      {
        "name": "GOPC",
        "location": "6q22.1",
        "locus_group": "protein-coding gene",
        "gene_family": [
          "PDZ domain containing"
        ],
        "chromosome": "6",
        "id": "HGNC:17643",
        "equivalent_identifiers": [
          "NCBIGENE:57120",
          "ENSEMBL:ENSG00000047932",
          "UniProtKB:F5H1Y4",
          "UniProtKB:Q9HD26",
          "HGNC:17643"
        ],
        "taxon": "9606",
        "gene_family_id": [
          1220
        ],
        "type": "gene",
        "omnicorp_article_count": 111
      }
    ],
    "edges": [
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:16039247",
          "PMID:6591864",
          "PMID:7049597",
          "PMID:8241983",
          "PMID:8404130"
        ],
        "id": "3452626",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0018874-x", #diff "MONDO:0018874",
        "type": "has_phenotype",
        "ctime": 1543623215.0472252,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0018076",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:4053715",
          "PMID:10671331",
          "PMID:22333506",
          "PMID:20033836",
          "PMID:19681705"
        ],
        "id": "1820676",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype_x", #diff "has_phenotype",
        "ctime": 1543707244.375745,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:21684172",
          "PMID:21665082",
          "PMID:11113673",
          "PMID:20517728",
          "PMID:12030044"
        ],
        "id": "3306367",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0018076",
        "type": "has_phenotype",
        "ctime": 1543620733.2432625,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005233",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:17167137",
          "PMID:12499415",
          "PMID:22778577",
          "PMID:19373944",
          "PMID:17033613"
        ],
        "id": "1820678",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.377082,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:9324672",
          "PMID:7552426",
          "PMID:11776767",
          "PMID:16332433",
          "PMID:11381509"
        ],
        "id": "3893921",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005233",
        "type": "has_phenotype",
        "ctime": 1543615184.2194393,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0007256",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1328737",
          "PMID:11462940",
          "PMID:19465842",
          "PMID:2472436",
          "PMID:17496446"
        ],
        "id": "1820643",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3736265,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:1328737",
          "PMID:11462940",
          "PMID:19465842",
          "PMID:2472436",
          "PMID:17496446"
        ],
        "id": "2042288",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0007256",
        "type": "has_phenotype",
        "ctime": 1543616168.3488474,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0009061",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1913738",
          "PMID:19584209",
          "PMID:15078765",
          "PMID:6663409",
          "PMID:11115445"
        ],
        "id": "1820740",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3810499,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:1913738",
          "PMID:19584209",
          "PMID:15078765",
          "PMID:6663409",
          "PMID:11115445"
        ],
        "id": "3059422",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0009061",
        "type": "has_phenotype",
        "ctime": 1543617658.2017093,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005149",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:17651639",
          "PMID:15259821",
          "PMID:22090231",
          "PMID:7474302",
          "PMID:18478262"
        ],
        "id": "1820671",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3754163,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:9556469",
          "PMID:2309547",
          "PMID:11456142",
          "PMID:10498138",
          "PMID:22360787"
        ],
        "id": "3717678",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005149",
        "type": "has_phenotype",
        "ctime": 1543625735.2813478,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0019065",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1767091",
          "PMID:20219273",
          "PMID:8753122",
          "PMID:23857203",
          "PMID:15111203"
        ],
        "id": "1820665",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.37504,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:1767091",
          "PMID:20219273",
          "PMID:8753122",
          "PMID:23857203",
          "PMID:15111203"
        ],
        "id": "3815301",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0019065",
        "type": "has_phenotype",
        "ctime": 1543627419.1909685,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005812",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:21503407",
          "PMID:22407041",
          "PMID:23071646",
          "PMID:22043762",
          "PMID:23128913"
        ],
        "id": "1820737",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3808625,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:21503407",
          "PMID:22407041",
          "PMID:23071646",
          "PMID:22043762",
          "PMID:23128913"
        ],
        "id": "3203776",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005812",
        "type": "has_phenotype",
        "ctime": 1543613029.8987536,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005279",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:7739177",
          "PMID:12134443",
          "PMID:23465996",
          "PMID:11799511",
          "PMID:3717106"
        ],
        "id": "1820660",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3747487,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:7739177",
          "PMID:12134443",
          "PMID:23465996",
          "PMID:11799511",
          "PMID:3717106"
        ],
        "id": "3966551",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005279",
        "type": "has_phenotype",
        "ctime": 1543616511.3809505,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0007915",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:6893127",
          "PMID:4045853",
          "PMID:362123",
          "PMID:9292793",
          "PMID:577388"
        ],
        "id": "1820716",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3795679,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:6893127",
          "PMID:4045853",
          "PMID:362123",
          "PMID:9292793",
          "PMID:577388"
        ],
        "id": "2984965",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0007915",
        "type": "has_phenotype",
        "ctime": 1543616294.853112,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "hetio:PRESENTS_DpS",
        "target_id": "HP:0002105",
        "edge_source": "hetio.disease_to_phenotype",
        "publications": [],
        "id": "2984206",
        "predicate_id": "RO:0002200",
        "source_database": "hetio",
        "source_id": "MONDO:0007915",
        "type": "has_phenotype",
        "ctime": 1543616298.206763,
        "relation_label": "PRESENTS_DpS",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0002076",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:8723510",
          "PMID:22273501",
          "PMID:20675678",
          "PMID:8292398",
          "PMID:17594887"
        ],
        "id": "1820669",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.375298,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:8723510",
          "PMID:22273501",
          "PMID:20675678",
          "PMID:8292398",
          "PMID:17594887"
        ],
        "id": "3076044",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0002076",
        "type": "has_phenotype",
        "ctime": 1543617282.1946514,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0004492",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1402100",
          "PMID:16520136",
          "PMID:875431",
          "PMID:2225451",
          "PMID:22516383"
        ],
        "id": "1820727",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3802774,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:1402100",
          "PMID:16520136",
          "PMID:875431",
          "PMID:2225451",
          "PMID:22516383"
        ],
        "id": "2831780",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0004492",
        "type": "has_phenotype",
        "ctime": 1543614693.8146496,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:6893127",
          "PMID:4045853",
          "PMID:362123",
          "PMID:9292793",
          "PMID:577388"
        ],
        "id": "2867546",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "has_phenotype",
        "ctime": 1543613309.9855397,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0019338",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:11240427",
          "PMID:6478899",
          "PMID:20831365",
          "PMID:12462021",
          "PMID:23037473"
        ],
        "id": "1820699",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3784437,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:11240427",
          "PMID:6478899",
          "PMID:20831365",
          "PMID:12462021",
          "PMID:23037473"
        ],
        "id": "4051191",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0019338",
        "type": "has_phenotype",
        "ctime": 1543623875.9949005,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005275",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:16039247",
          "PMID:7088745",
          "PMID:2653801",
          "PMID:529307",
          "PMID:17212899"
        ],
        "id": "1820697",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3783126,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:2736976",
          "PMID:8457080",
          "PMID:19764496",
          "PMID:15510826",
          "PMID:22704276"
        ],
        "id": "3959644",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005275",
        "type": "has_phenotype",
        "ctime": 1543616440.221302,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0011827",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:9071838",
          "PMID:8469838",
          "PMID:2681912",
          "PMID:19131134",
          "PMID:2326460"
        ],
        "id": "1820745",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3813756,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:9071838",
          "PMID:8469838",
          "PMID:2681912",
          "PMID:19131134",
          "PMID:2326460"
        ],
        "id": "3098975",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0011827",
        "type": "has_phenotype",
        "ctime": 1543618542.922527,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0006277",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:23114958",
          "PMID:19361321",
          "PMID:19921132",
          "PMID:11778518",
          "PMID:17718126"
        ],
        "id": "1820735",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3807225,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:23114958",
          "PMID:19361321",
          "PMID:19921132",
          "PMID:11778518",
          "PMID:17718126"
        ],
        "id": "2941808",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0006277",
        "type": "has_phenotype",
        "ctime": 1543614883.7951524,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0002462",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:699399",
          "PMID:2256583",
          "PMID:17695814",
          "PMID:1479723",
          "PMID:8248108"
        ],
        "id": "1820715",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.379495,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:18282444",
          "PMID:16432770",
          "PMID:2323259",
          "PMID:19787477",
          "PMID:17149061"
        ],
        "id": "3676714",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0002462",
        "type": "has_phenotype",
        "ctime": 1543619591.2585833,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0019180",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1780531",
          "PMID:313737",
          "PMID:17641482",
          "PMID:10453873",
          "PMID:18792970"
        ],
        "id": "1820757",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3823547,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:1780531",
          "PMID:313737",
          "PMID:17641482",
          "PMID:10453873",
          "PMID:18792970"
        ],
        "id": "3942179",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0019180",
        "type": "has_phenotype",
        "ctime": 1543630156.1926455,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0002363",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1205998",
          "PMID:7301318",
          "PMID:16801040",
          "PMID:18487874",
          "PMID:18708941"
        ],
        "id": "1820640",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3734362,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:1205998",
          "PMID:7301318",
          "PMID:16801040",
          "PMID:18487874",
          "PMID:18708941"
        ],
        "id": "3665783",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0002363",
        "type": "has_phenotype",
        "ctime": 1543618901.9798858,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0003781",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:15208530",
          "PMID:16446530",
          "PMID:12134443",
          "PMID:17001541",
          "PMID:3792090"
        ],
        "id": "1820630",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.372679,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:15208530",
          "PMID:16446530",
          "PMID:12134443",
          "PMID:17001541",
          "PMID:3792090"
        ],
        "id": "2801990",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0003781",
        "type": "has_phenotype",
        "ctime": 1543614654.7465687,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0007140",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:15456604",
          "PMID:16607057",
          "PMID:8371225",
          "PMID:9292793",
          "PMID:14635591"
        ],
        "id": "1820734",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3806524,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:15456604",
          "PMID:16607057",
          "PMID:8371225",
          "PMID:9292793",
          "PMID:14635591"
        ],
        "id": "2914921",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0007140",
        "type": "has_phenotype",
        "ctime": 1543615629.951873,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0001243",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:7867481",
          "PMID:10923965",
          "PMID:7687947",
          "PMID:11760657",
          "PMID:1761901"
        ],
        "id": "1820638",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3733165,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:7867481",
          "PMID:10923965",
          "PMID:7687947",
          "PMID:11760657",
          "PMID:1761901"
        ],
        "id": "2923197",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0001243",
        "type": "has_phenotype",
        "ctime": 1543614617.5264509,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0019121",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:3872089",
          "PMID:2068304",
          "PMID:1080700",
          "PMID:9118696",
          "PMID:15336585"
        ],
        "id": "1820739",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3809803,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:3872089",
          "PMID:2068304",
          "PMID:1080700",
          "PMID:9118696",
          "PMID:15336585"
        ],
        "id": "3928858",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0019121",
        "type": "has_phenotype",
        "ctime": 1543629923.4225829,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0017991",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:21674131",
          "PMID:16607057",
          "PMID:16859597",
          "PMID:21803399",
          "PMID:24003540"
        ],
        "id": "1820691",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3779433,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:21674131",
          "PMID:16607057",
          "PMID:16859597",
          "PMID:21803399",
          "PMID:24003540"
        ],
        "id": "3284226",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0017991",
        "type": "has_phenotype",
        "ctime": 1543622255.2870386,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005160",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:19329505",
          "PMID:2687763",
          "PMID:2396239",
          "PMID:7929546",
          "PMID:1788690"
        ],
        "id": "1820700",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3785126,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:9288506",
          "PMID:16773489",
          "PMID:17154705",
          "PMID:11193440",
          "PMID:12822650"
        ],
        "id": "3776653",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005160",
        "type": "has_phenotype",
        "ctime": 1543613202.145675,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0004822",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:2736976",
          "PMID:8457080",
          "PMID:19764496",
          "PMID:15510826",
          "PMID:22704276"
        ],
        "id": "1820728",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3803613,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:2736976",
          "PMID:8457080",
          "PMID:19764496",
          "PMID:15510826",
          "PMID:22704276"
        ],
        "id": "2899034",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0004822",
        "type": "has_phenotype",
        "ctime": 1543613866.5960224,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0006932",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:6591864",
          "PMID:15790053",
          "PMID:16520136",
          "PMID:9861587",
          "PMID:8775933"
        ],
        "id": "1820666",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3751109,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:6591864",
          "PMID:15790053",
          "PMID:16520136",
          "PMID:9861587",
          "PMID:8775933"
        ],
        "id": "2980256",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0006932",
        "type": "has_phenotype",
        "ctime": 1543617020.9475396,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005657",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:1554270",
          "PMID:11753460",
          "PMID:10819373",
          "PMID:9229298",
          "PMID:8089940"
        ],
        "id": "1820724",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3800788,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:17319045",
          "PMID:3595464",
          "PMID:9580089",
          "PMID:8980793",
          "PMID:6690237"
        ],
        "id": "3177611",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005657",
        "type": "has_phenotype",
        "ctime": 1543623444.0090919,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0004849",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:9588587",
          "PMID:8292398",
          "PMID:20860505",
          "PMID:15993574",
          "PMID:9229298"
        ],
        "id": "1820688",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3777413,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:9588587",
          "PMID:8292398",
          "PMID:20860505",
          "PMID:15993574",
          "PMID:9229298"
        ],
        "id": "2769040",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0004849",
        "type": "has_phenotype",
        "ctime": 1543613944.3280752,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005058",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:6344822",
          "PMID:8184399",
          "PMID:1431408",
          "PMID:8057542",
          "PMID:931184"
        ],
        "id": "1820654",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3743567,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:6344822",
          "PMID:8184399",
          "PMID:1431408",
          "PMID:8057542",
          "PMID:931184"
        ],
        "id": "3321142",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005058",
        "type": "has_phenotype",
        "ctime": 1543618852.0691922,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005396",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:9288506",
          "PMID:16773489",
          "PMID:17154705",
          "PMID:11193440",
          "PMID:12822650"
        ],
        "id": "1820633",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3729544,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:9288506",
          "PMID:16773489",
          "PMID:17154705",
          "PMID:11193440",
          "PMID:12822650"
        ],
        "id": "4090114",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005396",
        "type": "has_phenotype",
        "ctime": 1543619730.833026,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "hetio:PRESENTS_DpS",
        "target_id": "HP:0002105",
        "edge_source": "hetio.disease_to_phenotype",
        "publications": [],
        "id": "4090108",
        "predicate_id": "RO:0002200",
        "source_database": "hetio",
        "source_id": "MONDO:0005396",
        "type": "has_phenotype",
        "ctime": 1543619732.4037771,
        "relation_label": "PRESENTS_DpS",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0018667",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:7365817",
          "PMID:2276771",
          "PMID:9234640",
          "PMID:7065764",
          "PMID:12062287"
        ],
        "id": "1820761",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3826163,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:7365817",
          "PMID:2276771",
          "PMID:9234640",
          "PMID:7065764",
          "PMID:12062287"
        ],
        "id": "3366092",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0018667",
        "type": "has_phenotype",
        "ctime": 1543622439.4068303,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0007191",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:17446699",
          "PMID:1877340",
          "PMID:9510565",
          "PMID:17047893",
          "PMID:15343111"
        ],
        "id": "1820684",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3774738,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:17446699",
          "PMID:1877340",
          "PMID:9510565",
          "PMID:17047893",
          "PMID:15343111"
        ],
        "id": "2939362",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0007191",
        "type": "has_phenotype",
        "ctime": 1543615954.6274416,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "hetio:PRESENTS_DpS",
        "target_id": "HP:0002105",
        "edge_source": "hetio.disease_to_phenotype",
        "publications": [],
        "id": "2938947",
        "predicate_id": "RO:0002200",
        "source_database": "hetio",
        "source_id": "MONDO:0007191",
        "type": "has_phenotype",
        "ctime": 1543615956.8892539,
        "relation_label": "PRESENTS_DpS",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005825",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:14650704",
          "PMID:11131876",
          "PMID:15684465",
          "PMID:21152929",
          "PMID:1308063"
        ],
        "id": "1820696",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3782418,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:14650704",
          "PMID:11131876",
          "PMID:15684465",
          "PMID:21152929",
          "PMID:1308063"
        ],
        "id": "3209598",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005825",
        "type": "has_phenotype",
        "ctime": 1543613080.683818,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0012105",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:18282444",
          "PMID:16432770",
          "PMID:2323259",
          "PMID:19787477",
          "PMID:17149061"
        ],
        "id": "1820746",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3814456,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:18282444",
          "PMID:16432770",
          "PMID:2323259",
          "PMID:19787477",
          "PMID:17149061"
        ],
        "id": "3123106",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0012105",
        "type": "has_phenotype",
        "ctime": 1543618633.274625,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0002568",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:22137422",
          "PMID:11692592",
          "PMID:20094734",
          "PMID:2462371",
          "PMID:15254614"
        ],
        "id": "1820705",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3788419,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:22137422",
          "PMID:11692592",
          "PMID:20094734",
          "PMID:2462371",
          "PMID:15254614"
        ],
        "id": "2794766",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0002568",
        "type": "has_phenotype",
        "ctime": 1543620649.0196688,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0005974",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:14588206",
          "PMID:2343206",
          "PMID:8545686",
          "PMID:7325594",
          "PMID:21964988"
        ],
        "id": "1820749",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.3818233,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:14588206",
          "PMID:2343206",
          "PMID:8545686",
          "PMID:7325594",
          "PMID:21964988"
        ],
        "id": "2865645",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0005974",
        "type": "has_phenotype",
        "ctime": 1543613579.6185522,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "MONDO:0006656",
        "edge_source": "biolink.phenotype_get_disease",
        "publications": [
          "PMID:10398742",
          "PMID:17154705",
          "PMID:18430650",
          "PMID:19492894",
          "PMID:12822650"
        ],
        "id": "1820644",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "HP:0002105",
        "type": "has_phenotype",
        "ctime": 1543707244.373697,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "RO:0002200",
        "target_id": "HP:0002105",
        "edge_source": "biolink.disease_get_phenotype",
        "publications": [
          "PMID:10398742",
          "PMID:17154705",
          "PMID:18430650",
          "PMID:19492894",
          "PMID:12822650"
        ],
        "id": "2921981",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0006656",
        "type": "has_phenotype",
        "ctime": 1543615982.0699837,
        "relation_label": "has phenotype",
        "weight": 0.8093606487732907
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7029",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221380",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.268787,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7029",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183318",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1622598,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7029",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679307",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.725187,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3236",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186980",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7110498,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3236",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4182474",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.133451,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3236",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678939",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7215288,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3236",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2643829",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002363",
        "type": "disease_to_gene_association",
        "ctime": 1543724721.8795905,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3535",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187085",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7176187,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:620",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4217625",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019065",
        "type": "disease_to_gene_association",
        "ctime": 1543740400.9698584,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6204",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221169",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2620065,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6204",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187015",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7136471,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6204",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183062",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.153115,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6204",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2676198",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.7278428,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:644",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678625",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.717773,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256642",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.789838,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4253212",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019338",
        "type": "disease_to_gene_association",
        "ctime": 1543738365.0301268,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222556",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3017824,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4217711",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019065",
        "type": "disease_to_gene_association",
        "ctime": 1543740400.9718316,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187087",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7176836,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2691482",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002462",
        "type": "disease_to_gene_association",
        "ctime": 1543725398.5531836,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2687749",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004822",
        "type": "disease_to_gene_association",
        "ctime": 1543724537.7998154,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679798",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7279172,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2671506",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0006932",
        "type": "disease_to_gene_association",
        "ctime": 1543729723.7535045,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11892",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2621751",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0001243",
        "type": "disease_to_gene_association",
        "ctime": 1543725113.0328221,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11998",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187051",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7164364,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11998",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183709",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.177737,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11998",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2761884",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005058",
        "type": "disease_to_gene_association",
        "ctime": 1543727668.3451118,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11998",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679456",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7259543,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11998",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2643885",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002363",
        "type": "disease_to_gene_association",
        "ctime": 1543724721.8800948,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3657",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220874",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2520466,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:9864",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221966",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2864068,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12679",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222793",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3084328,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12680",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222772",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3077335,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12680",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187098",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7180436,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12680",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4184723",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.2125678,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12680",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678135",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.7366133,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6770",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4224308",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019180",
        "type": "disease_to_gene_association",
        "ctime": 1543741001.31125,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6769",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222386",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.297149,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6769",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4194846",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005396",
        "type": "disease_to_gene_association",
        "ctime": 1543725429.3889956,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6769",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175637",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3062015,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11773",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4194851",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005396",
        "type": "disease_to_gene_association",
        "ctime": 1543725429.389221,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11773",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175641",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3064356,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7865",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2687733",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004822",
        "type": "disease_to_gene_association",
        "ctime": 1543724537.7996266,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:8803",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187057",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7167099,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11768",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4194848",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005396",
        "type": "disease_to_gene_association",
        "ctime": 1543725429.3890707,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11768",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175638",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3062341,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11825",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183562",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.172615,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11825",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187044",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7158978,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1773",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4255896",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.6442986,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1773",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4182162",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1222403,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1773",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678843",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.720466,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12796",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256729",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.792038,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12796",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222803",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.308762,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12796",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2691502",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002462",
        "type": "disease_to_gene_association",
        "ctime": 1543725398.5533922,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1884",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186964",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7098699,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1884",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2748009",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3250082,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1884",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2687686",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004822",
        "type": "disease_to_gene_association",
        "ctime": 1543724537.7989857,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1884",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2640275",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005657",
        "type": "disease_to_gene_association",
        "ctime": 1543727464.6207411,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1884",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2582031",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0003781",
        "type": "disease_to_gene_association",
        "ctime": 1543725183.3542922,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:108",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4217640",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019065",
        "type": "disease_to_gene_association",
        "ctime": 1543740400.9699883,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1628",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220393",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2378888,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:10896",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222272",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.29377,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1662",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4182156",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1220458,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11772",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4194849",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005396",
        "type": "disease_to_gene_association",
        "ctime": 1543725429.389146,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11772",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175639",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3062675,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:5173",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679579",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.726727,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:5173",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2643897",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002363",
        "type": "disease_to_gene_association",
        "ctime": 1543724721.8802278,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12363",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256661",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.7904623,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12363",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2651610",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0006277",
        "type": "disease_to_gene_association",
        "ctime": 1543725529.9518056,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12363",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2596297",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002076",
        "type": "disease_to_gene_association",
        "ctime": 1543726665.263569,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:648",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4181725",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1073425,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:894",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187046",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7160466,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1659",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4255834",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.6431975,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1659",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220299",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2358203,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3765",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256063",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.6649995,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3765",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220881",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2522802,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:259",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2674411",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.7182899,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11925",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256641",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.7898054,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11925",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222554",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3017166,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11925",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2677846",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.7353446,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1119",
        "edge_source": "pharos.gene_get_disease",
        "publications": [],
        "id": "6912140",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543589961.8514094,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1119",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2747335",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.320586,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:10261",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4184100",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1913247,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6342",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256775",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738951.1293159,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6342",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221295",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2659323,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6342",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187029",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7146745,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6342",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183202",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.158322,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6342",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2751291",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3464265,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1097",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220149",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2323346,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1097",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678737",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7190661,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:990",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4255784",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.641573,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:990",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220097",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2305706,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:583",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4181797",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1097398,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:583",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678638",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7179208,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3942",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679411",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7257245,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:8636",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183908",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1843786,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7436",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187291",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005279",
        "type": "disease_to_gene_association",
        "ctime": 1543724332.8985991,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7436",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183550",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1722095,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7436",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2635845",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007140",
        "type": "disease_to_gene_association",
        "ctime": 1543727479.0524125,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11573",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2674578",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.71904,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11848",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222546",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3014545,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11848",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2753890",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3729649,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11848",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2656447",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005825",
        "type": "disease_to_gene_association",
        "ctime": 1543723180.1909523,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11848",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2654663",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005812",
        "type": "disease_to_gene_association",
        "ctime": 1543723090.8927863,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11848",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2640318",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005657",
        "type": "disease_to_gene_association",
        "ctime": 1543727464.62193,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2637",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220499",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2408435,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3349",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220758",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.248328,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3349",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4224304",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019180",
        "type": "disease_to_gene_association",
        "ctime": 1543741001.311087,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2201",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175610",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3052585,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2201",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2596205",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002076",
        "type": "disease_to_gene_association",
        "ctime": 1543726665.263061,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12405",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4217717",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019065",
        "type": "disease_to_gene_association",
        "ctime": 1543740400.9720266,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12726",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187311",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005279",
        "type": "disease_to_gene_association",
        "ctime": 1543724332.899353,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12726",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2621762",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0001243",
        "type": "disease_to_gene_association",
        "ctime": 1543725113.0329688,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7176",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221495",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2725165,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7176",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4194840",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005396",
        "type": "disease_to_gene_association",
        "ctime": 1543725429.3887732,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7176",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183448",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1676812,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7176",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175628",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3059046,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7176",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679373",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7255268,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7176",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2579885",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004849",
        "type": "disease_to_gene_association",
        "ctime": 1543724715.2101946,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002326",
        "target_id": "HGNC:4942",
        "edge_source": "biolink.disease_get_gene",
        "publications": [
          "PMID:25827949"
        ],
        "id": "7928757",
        "predicate_id": "RO:0002326",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "contributes_to",
        "ctime": 1549664779.2590451,
        "relation_label": "contributes to",
        "weight": 0.4071474314830641
      },
      {
        "relation": "RO:0002607",
        "target_id": "HGNC:4942",
        "edge_source": "biolink.disease_get_gene",
        "publications": [
          "PMID:26316170",
          "PMID:18204098",
          "PMID:26502338",
          "PMID:11436868",
          "PMID:21408207"
        ],
        "id": "7928980",
        "predicate_id": "RO:0002607",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "biomarker_for",
        "ctime": 1549664779.2599387,
        "relation_label": "is marker for",
        "weight": 0.8093606487732907
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6407",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256426",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.7679248,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6407",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183981",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1868176,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6407",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679590",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7267601,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6973",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183469",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1684148,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6973",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2676692",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.729959,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1516",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220277",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2350855,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1516",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2671406",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0006932",
        "type": "disease_to_gene_association",
        "ctime": 1543729723.752671,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1516",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2667232",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007915",
        "type": "disease_to_gene_association",
        "ctime": 1543730018.3244066,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1516",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2640976",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007191",
        "type": "disease_to_gene_association",
        "ctime": 1543728053.7335646,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:9208",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221551",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2743974,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:175",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4224300",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019180",
        "type": "disease_to_gene_association",
        "ctime": 1543741001.3108857,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:175",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186923",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7060347,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:175",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175020",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005149",
        "type": "disease_to_gene_association",
        "ctime": 1543729335.342004,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1472",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2747055",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.31924,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1472",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186936",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.707046,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1472",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220161",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2327316,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1318",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220555",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2417696,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1318",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2667369",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007915",
        "type": "disease_to_gene_association",
        "ctime": 1543730018.325456,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1331",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220516",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.241141,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7876",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187048",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7161953,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7876",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175070",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005149",
        "type": "disease_to_gene_association",
        "ctime": 1543729335.3460014,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7876",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2671453",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0006932",
        "type": "disease_to_gene_association",
        "ctime": 1543729723.7530568,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6018",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221138",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.260982,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6018",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183031",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1520543,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6018",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2750766",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3418036,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6018",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2679202",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7246192,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6018",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2667768",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007915",
        "type": "disease_to_gene_association",
        "ctime": 1543730018.3366594,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:3229",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2675343",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.7235074,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:6935",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2748586",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.328021,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002200",
        "target_id": "HGNC:12269",
        "edge_source": "biolink.disease_get_gene",
        "publications": [],
        "id": "7927304",
        "predicate_id": "RO:0002200",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "has_phenotype",
        "ctime": 1549664779.2511995,
        "relation_label": "has phenotype",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12269",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2662659",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004670",
        "type": "disease_to_gene_association",
        "ctime": 1543723570.44426,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002607",
        "target_id": "HGNC:12269",
        "edge_source": "biolink.disease_get_gene",
        "publications": [
          "PMID:17660818"
        ],
        "id": "7927194",
        "predicate_id": "RO:0002607",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "biomarker_for",
        "ctime": 1549664779.2505257,
        "relation_label": "is marker for",
        "weight": 0.4071474314830641
      },
      {
        "relation": "GENO:0000840",
        "target_id": "HGNC:12269",
        "edge_source": "biolink.disease_get_gene",
        "publications": [
          "PMID:17357087",
          "PMID:27566796"
        ],
        "id": "7927307",
        "predicate_id": "BIOLINK:0000001",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "gene_associated_with_condition",
        "ctime": 1549664779.2512407,
        "relation_label": "pathogenic_for_condition",
        "weight": 0.5391111411287752
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:8594",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2752446",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3575137,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11850",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222503",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2999904,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11850",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2753777",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3719347,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11850",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2677772",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728995.735017,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11850",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2654646",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005812",
        "type": "disease_to_gene_association",
        "ctime": 1543723090.892639,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11850",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2641075",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007191",
        "type": "disease_to_gene_association",
        "ctime": 1543728059.8822534,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11850",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2640317",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005657",
        "type": "disease_to_gene_association",
        "ctime": 1543727464.6218557,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12362",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2651604",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0006277",
        "type": "disease_to_gene_association",
        "ctime": 1543725529.9517303,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:9273",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187056",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.716677,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7218",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4200726",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0012105",
        "type": "disease_to_gene_association",
        "ctime": 1543731954.3660653,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7218",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187053",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7165787,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7218",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2752427",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.357315,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7218",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2582131",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0003781",
        "type": "disease_to_gene_association",
        "ctime": 1543725183.3548954,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1631",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220154",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2325,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:399",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4219976",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2270732,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:399",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2691241",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002462",
        "type": "disease_to_gene_association",
        "ctime": 1543725398.5500543,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:427",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4181676",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.105691,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:17941",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2752298",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3559446,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1050",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220100",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2306693,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1050",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678712",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7187672,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7321",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221517",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2732384,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:4603",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220601",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2432973,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:4603",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186974",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.710606,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:4603",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2748524",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3276272,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4224250",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018667",
        "type": "disease_to_gene_association",
        "ctime": 1543737650.9009643,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220622",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2439845,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4217677",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019065",
        "type": "disease_to_gene_association",
        "ctime": 1543740400.970618,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4216339",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0017991",
        "type": "disease_to_gene_association",
        "ctime": 1543739512.2153351,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187277",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005279",
        "type": "disease_to_gene_association",
        "ctime": 1543724332.8981397,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175612",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3053246,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2748607",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3281963,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2687690",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004822",
        "type": "disease_to_gene_association",
        "ctime": 1543724537.7990503,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678916",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.721212,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2667402",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007915",
        "type": "disease_to_gene_association",
        "ctime": 1543730018.3256962,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2653990",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005812",
        "type": "disease_to_gene_association",
        "ctime": 1543723090.8856473,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2641868",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004492",
        "type": "disease_to_gene_association",
        "ctime": 1543726030.1895304,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2640490",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0006656",
        "type": "disease_to_gene_association",
        "ctime": 1543727645.473065,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2367",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2582040",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0003781",
        "type": "disease_to_gene_association",
        "ctime": 1543725183.354326,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1678",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186955",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7084825,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1678",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222647",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019121",
        "type": "disease_to_gene_association",
        "ctime": 1543740706.5705867,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1678",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4252662",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019338",
        "type": "disease_to_gene_association",
        "ctime": 1543738365.0209336,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1695",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220438",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.239312,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:5438",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221134",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2608492,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:5438",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4187003",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.712761,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:5438",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2640296",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005657",
        "type": "disease_to_gene_association",
        "ctime": 1543727464.6213357,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1634",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186954",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7084067,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1698",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220414",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2385242,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1698",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2687682",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004822",
        "type": "disease_to_gene_association",
        "ctime": 1543724537.798922,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11920",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256643",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.7898707,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11920",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4184556",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.206663,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11920",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2641077",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007191",
        "type": "disease_to_gene_association",
        "ctime": 1543728059.8823273,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11249",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183289",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.161279,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1078",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175032",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005149",
        "type": "disease_to_gene_association",
        "ctime": 1543729335.3429255,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1078",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4224302",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019180",
        "type": "disease_to_gene_association",
        "ctime": 1543741001.3110006,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:795",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678685",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7185445,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11722",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2580242",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002568",
        "type": "disease_to_gene_association",
        "ctime": 1543726097.4861386,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11722",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2596271",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002076",
        "type": "disease_to_gene_association",
        "ctime": 1543726665.2634695,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11722",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2687744",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0004822",
        "type": "disease_to_gene_association",
        "ctime": 1543724537.799753,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:4837",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220294",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.235656,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:307",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2746251",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3150241,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:4057",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220903",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2530596,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1366",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2621562",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0001243",
        "type": "disease_to_gene_association",
        "ctime": 1543725113.0307145,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2707",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4252547",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019338",
        "type": "disease_to_gene_association",
        "ctime": 1543738365.017276,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2707",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4219962",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2266023,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2707",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186928",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7064357,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2707",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175604",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.3050423,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2707",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175021",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005149",
        "type": "disease_to_gene_association",
        "ctime": 1543729335.342085,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:15633",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222708",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3055866,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:15633",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2654807",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005812",
        "type": "disease_to_gene_association",
        "ctime": 1543723090.8934052,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:15633",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2668558",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007915",
        "type": "disease_to_gene_association",
        "ctime": 1543730018.3401027,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:15633",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2691494",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0002462",
        "type": "disease_to_gene_association",
        "ctime": 1543725398.5533233,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:8729",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183760",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1794457,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12388",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222701",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.3054554,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7989",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4256440",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018874",
        "type": "disease_to_gene_association",
        "ctime": 1543738949.7844925,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:15990",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221005",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.256961,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1693",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4175609",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005160",
        "type": "disease_to_gene_association",
        "ctime": 1543722878.305225,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1693",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186956",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7085571,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:1693",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4252664",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0019338",
        "type": "disease_to_gene_association",
        "ctime": 1543738365.0209668,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7531",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221518",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2732708,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2956",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4186979",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005275",
        "type": "disease_to_gene_association",
        "ctime": 1543724283.7109752,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2956",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2748882",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3298047,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2956",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2667472",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007915",
        "type": "disease_to_gene_association",
        "ctime": 1543730018.3263,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:4234",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4220961",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2554908,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:2295",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678794",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.7199087,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:317",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2678987",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0007256",
        "type": "disease_to_gene_association",
        "ctime": 1543728999.722288,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:16781",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221676",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2773085,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7124",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2654432",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005812",
        "type": "disease_to_gene_association",
        "ctime": 1543723090.8901634,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:9689",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183911",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.184477,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:11183",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222362",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2963605,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7515",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2582109",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0003781",
        "type": "disease_to_gene_association",
        "ctime": 1543725183.3547604,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:7515",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2751884",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3514574,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:27004",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4184208",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1949022,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:27004",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2753212",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3657181,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:27004",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2624085",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005974",
        "type": "disease_to_gene_association",
        "ctime": 1543724148.7046342,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:20387",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4183052",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0005233",
        "type": "disease_to_gene_association",
        "ctime": 1543723811.1527913,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:20387",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4221163",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2618077,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "RO:0002326",
        "target_id": "HGNC:11365",
        "edge_source": "biolink.disease_get_gene",
        "publications": [
          "PMID:26316170",
          "PMID:18204098",
          "PMID:24871463",
          "PMID:23273568",
          "PMID:23740937",
          "PMID:26606652",
          "PMID:19838195",
          "PMID:26502338",
          "PMID:23053960",
          "PMID:19838193",
          "PMID:26663301",
          "PMID:27399966",
          "PMID:19165918",
          "PMID:21408207"
        ],
        "id": "7927309",
        "predicate_id": "RO:0002326",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "contributes_to",
        "ctime": 1549664779.251603,
        "relation_label": "contributes to",
        "weight": 0.991348765537732
      },
      {
        "relation": "RO:0002607",
        "target_id": "HGNC:11365",
        "edge_source": "biolink.disease_get_gene",
        "publications": [
          "PMID:17804842",
          "PMID:19838195",
          "PMID:19838193",
          "PMID:18204446",
          "PMID:19109131"
        ],
        "id": "7927871",
        "predicate_id": "RO:0002607",
        "source_database": "biolink",
        "source_id": "MONDO:0004670",
        "type": "biomarker_for",
        "ctime": 1549664779.2543535,
        "relation_label": "is marker for",
        "weight": 0.8093606487732907
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:23506",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2748824",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0011827",
        "type": "disease_to_gene_association",
        "ctime": 1543734278.4806762,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:23506",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2746157",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3145287,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:12651",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "4222431",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0018076",
        "type": "disease_to_gene_association",
        "ctime": 1543737147.2986758,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "relation": "PHAROS:gene_involved",
        "target_id": "HGNC:17643",
        "edge_source": "pharos.disease_get_gene",
        "publications": [],
        "id": "2750050",
        "predicate_id": "NCIT:R176",
        "source_database": "pharos",
        "source_id": "MONDO:0009061",
        "type": "disease_to_gene_association",
        "ctime": 1543731394.3374348,
        "relation_label": "gene_involved",
        "weight": 0.25832639515782074
      },
      {
        "type": "literature_co-occurrence",
        "id": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "num_publications": 1274,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0018076",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1476095070785095
      },
      {
        "type": "literature_co-occurrence",
        "id": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "num_publications": 192,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005233",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10699002530169066
      },
      {
        "type": "literature_co-occurrence",
        "id": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "num_publications": 25,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0007256",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "num_publications": 259,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0009061",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10956417557819753
      },
      {
        "type": "literature_co-occurrence",
        "id": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "num_publications": 29,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0018874",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10053329177959736
      },
      {
        "type": "literature_co-occurrence",
        "id": "25824f35-1ee1-494d-bd75-0b61c167fb52",
        "num_publications": 114,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0019338",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10410632769888484
      },
      {
        "type": "literature_co-occurrence",
        "id": "1be65edb-c074-41d5-90a6-73e6454b33ec",
        "num_publications": 44,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0004670",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10129265705809365
      },
      {
        "type": "literature_co-occurrence",
        "id": "32376d24-7763-42e2-91b7-4141b85013d1",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11772",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10003365419968091
      },
      {
        "type": "literature_co-occurrence",
        "id": "4d114400-db1b-4b00-9d51-b33cce932faf",
        "num_publications": 25,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1678",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b63e4788-a139-4886-bfcc-5cbc9bbc347c",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11925",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "e805f860-28b7-4f5b-826a-166202064858",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:4603",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10004282731948311
      },
      {
        "type": "literature_co-occurrence",
        "id": "c2db85d2-4c2a-4c8e-9788-e8e65e657060",
        "num_publications": 152,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0006932",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10572806151049985
      },
      {
        "type": "literature_co-occurrence",
        "id": "965adb3b-749e-4b1e-b8d6-371bd2e62361",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7876",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "0f9c87f9-709d-4c9b-9063-88ee41059a5a",
        "num_publications": 27,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0006932",
        "target_id": "HGNC:7876",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10083715167730678
      },
      {
        "type": "literature_co-occurrence",
        "id": "003463ba-08ff-4701-a318-41c042b128f8",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "fcf9e79a-e20b-4a04-952c-66626af73791",
        "num_publications": 79,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0006932",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10194343687408802
      },
      {
        "type": "literature_co-occurrence",
        "id": "9c93a4b8-4884-41ef-8463-3d977325aef8",
        "num_publications": 82,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7029",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9ebc49cf-3a40-43d8-8ad8-98764d927578",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6769",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "d7d9bb39-7ad7-4e46-afeb-f907b34c11a2",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1631",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1000091887826976
      },
      {
        "type": "literature_co-occurrence",
        "id": "fe06ce36-5fce-4e25-81fc-fc456a50f807",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:317",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001815796614044
      },
      {
        "type": "literature_co-occurrence",
        "id": "8d9fe083-0320-4a38-983e-2eaa1df3ba3d",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1318",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9873d8a9-a400-4a74-b25f-9afaf699254f",
        "num_publications": 166,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005149",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10622078202787044
      },
      {
        "type": "literature_co-occurrence",
        "id": "1d468ded-ca12-49f1-b7b5-a8eff9acae3f",
        "num_publications": 6,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:108",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000374279018731
      },
      {
        "type": "literature_co-occurrence",
        "id": "04a65677-6c89-4927-983e-14843f0e0527",
        "num_publications": 91,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0007915",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10266728727451369
      },
      {
        "type": "literature_co-occurrence",
        "id": "dda1ef5a-7786-4be5-bba5-a77634ef19a6",
        "num_publications": 29,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0001243",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10088409305861179
      },
      {
        "type": "literature_co-occurrence",
        "id": "3553716c-487d-4609-9a6c-2802ab88ef22",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1366",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10005018887259376
      },
      {
        "type": "literature_co-occurrence",
        "id": "9350b4b2-542e-455f-953c-2271a1d83eea",
        "num_publications": 52,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0001243",
        "target_id": "HGNC:1366",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1020317260594148
      },
      {
        "type": "literature_co-occurrence",
        "id": "39790313-d958-40f8-8314-3966274b2777",
        "num_publications": 51,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005812",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10080846518580766
      },
      {
        "type": "literature_co-occurrence",
        "id": "a7d23f2a-de44-40e7-abac-2b9f93627714",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6973",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b38e7a56-a562-4282-9cd3-38a1d9e5adec",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12363",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10005303951656241
      },
      {
        "type": "literature_co-occurrence",
        "id": "1d897c9b-0d8c-40d5-827e-66df33cedc31",
        "num_publications": 18,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1662",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10035463697429126
      },
      {
        "type": "literature_co-occurrence",
        "id": "a7f079d4-f475-4954-b656-92c8c2bcd1c0",
        "num_publications": 218,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0002462",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1080845511506332
      },
      {
        "type": "literature_co-occurrence",
        "id": "35075ee5-4215-43cb-922c-409ed452d486",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:399",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9d714683-5b7f-4878-a8f7-7cbb2f1c8587",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11722",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001167918045839
      },
      {
        "type": "literature_co-occurrence",
        "id": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "num_publications": 1951,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005275",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1760373902391008
      },
      {
        "type": "literature_co-occurrence",
        "id": "9ea2cbf1-63a4-49f7-9172-de14b016e5aa",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11848",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "09cd9f4c-016c-49be-9063-e910cfc6f035",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3535",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10004148031189208
      },
      {
        "type": "literature_co-occurrence",
        "id": "cdb535f8-867b-48d5-bb8d-949b21fc4247",
        "num_publications": 15,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0006277",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10059484313732658
      },
      {
        "type": "literature_co-occurrence",
        "id": "c3e21e5d-20e3-43a4-ba67-51df39a2072f",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12405",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b43d0e58-7c89-477f-91fd-3bcdf5cd4589",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6018",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "6b9d3347-f486-4e4a-a603-56eaa4b4e710",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:259",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "d4ae3940-5df2-48ff-bce6-92bc59787c01",
        "num_publications": 126,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0012105",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1048320166615545
      },
      {
        "type": "literature_co-occurrence",
        "id": "e8074d52-9b40-404f-a038-67e504171729",
        "num_publications": 19,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3236",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10009558330922341
      },
      {
        "type": "literature_co-occurrence",
        "id": "5c8e3c6d-2830-4f56-aeef-2df2e44bf3b3",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12726",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "08ad4229-205a-4f6f-9e15-4b7b07c55d53",
        "num_publications": 38,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0001243",
        "target_id": "HGNC:12726",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10130595933736464
      },
      {
        "type": "literature_co-occurrence",
        "id": "9356e5cd-14f2-4cff-8f2c-be5801d075a2",
        "num_publications": 59,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0019065",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10114067882652111
      },
      {
        "type": "literature_co-occurrence",
        "id": "eaaa2aa5-41a7-4229-b893-e87f62086030",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1698",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002348899121993
      },
      {
        "type": "literature_co-occurrence",
        "id": "10e1043c-53f0-4541-a2e0-5bd6722db771",
        "num_publications": 34,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0017991",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10126833894035048
      },
      {
        "type": "literature_co-occurrence",
        "id": "56e355ce-1622-45e0-8deb-f8ce0d4cf17c",
        "num_publications": 32,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0007140",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10113530933813086
      },
      {
        "type": "literature_co-occurrence",
        "id": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "num_publications": 639,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0004822",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1253790479627669
      },
      {
        "type": "literature_co-occurrence",
        "id": "0689bf34-29ae-4ab5-b6ee-c8e0419c0c33",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1331",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002057569572764
      },
      {
        "type": "literature_co-occurrence",
        "id": "3d0a5950-d98c-43c2-88b8-cd770c874eab",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1628",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a5fec654-ade3-40b3-810f-859adce4db14",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:644",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b8032ded-cd9d-496e-baf1-dab21b8dd15c",
        "num_publications": 42,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005396",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10164113451455103
      },
      {
        "type": "literature_co-occurrence",
        "id": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "num_publications": 20,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1002830782974865
      },
      {
        "type": "literature_co-occurrence",
        "id": "7a40a3ac-cae3-4943-b9da-e8fe6e354ab8",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6342",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "6fbde79f-d983-4d62-b16a-97f23517bf98",
        "num_publications": 18,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0002363",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10041296552506096
      },
      {
        "type": "literature_co-occurrence",
        "id": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "num_publications": 244,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005160",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10901504817350771
      },
      {
        "type": "literature_co-occurrence",
        "id": "d1981f79-da4d-4852-885d-5a4e3b9491b4",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:5438",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001692624492209
      },
      {
        "type": "literature_co-occurrence",
        "id": "fbe16108-7e95-48f7-b0ad-6cd0622d35ea",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:9273",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10010301443578895
      },
      {
        "type": "literature_co-occurrence",
        "id": "d0c70c79-d4ea-4bcc-8e8f-a8608f34048e",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11920",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "11f5bc12-4ca0-41fd-8542-0676c5acdb39",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:2707",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "da5bce9a-85af-4442-869e-cb20669c00b8",
        "num_publications": 96,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005149",
        "target_id": "HGNC:2707",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10316315561091371
      },
      {
        "type": "literature_co-occurrence",
        "id": "89084498-ab21-459a-acb4-fa60f065d7fc",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:427",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10013562955761934
      },
      {
        "type": "literature_co-occurrence",
        "id": "b8371b6c-d7a8-440c-a40f-9096bab5a5f1",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:8803",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001733347977604
      },
      {
        "type": "literature_co-occurrence",
        "id": "9d75beb6-f2d8-4c2d-8af2-7346df36d0ff",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002984812008853
      },
      {
        "type": "literature_co-occurrence",
        "id": "adca4ca6-33b5-4ca2-836f-e70407bc62a4",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11998",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "71340ade-a0cf-4b2d-b4d5-c47e7052104f",
        "num_publications": 20,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0011827",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10069072026007353
      },
      {
        "type": "literature_co-occurrence",
        "id": "808635f5-7cbb-4d68-b4a6-88b5b069eb7d",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12388",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10013473677353635
      },
      {
        "type": "literature_co-occurrence",
        "id": "a60558b0-f6c8-42a1-9ddc-2bea0a1980b5",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:2201",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1001882255035852
      },
      {
        "type": "literature_co-occurrence",
        "id": "32e568d6-fba8-4233-bde3-9b8e4a762911",
        "num_publications": 52,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0019180",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10203821187330953
      },
      {
        "type": "literature_co-occurrence",
        "id": "cb2599a2-1d54-48fc-b37f-481e50d4f91c",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:2956",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10007391813416522
      },
      {
        "type": "literature_co-occurrence",
        "id": "85d3afca-dc0f-447c-9965-b6a3ca1d55cb",
        "num_publications": 35,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:2956",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10133527337953341
      },
      {
        "type": "literature_co-occurrence",
        "id": "307a3370-b219-4a6b-89a9-d80ceb9c6c30",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1695",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001409126382399
      },
      {
        "type": "literature_co-occurrence",
        "id": "d8924caf-d2b0-4839-b1b6-62bc33edfa5e",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6407",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001886812297056
      },
      {
        "type": "literature_co-occurrence",
        "id": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "e240213a-915c-4eee-9e05-0e1d45dbfd55",
        "num_publications": 10,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1884",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1002548914019219
      },
      {
        "type": "literature_co-occurrence",
        "id": "fd7ff6fe-9164-44be-9257-17786e848143",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:2295",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "259b01be-50d1-432f-a3dd-03cf59ae9ed2",
        "num_publications": 68,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0004849",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10246800731211325
      },
      {
        "type": "literature_co-occurrence",
        "id": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "2a322cc4-81a9-4d48-980a-a655c1375d25",
        "num_publications": 31,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004849",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1011052354904507
      },
      {
        "type": "literature_co-occurrence",
        "id": "46c297af-8f47-4d1d-9f86-06e60a2a2f72",
        "num_publications": 7,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7218",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10013081039932126
      },
      {
        "type": "literature_co-occurrence",
        "id": "3c25f748-71f9-482f-b50e-b01f76b928fe",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1097",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "4dfaee62-09f8-4af5-bc6d-10db49ac5921",
        "num_publications": 219,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:2956",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10873092598124079
      },
      {
        "type": "literature_co-occurrence",
        "id": "044de512-efa6-4249-b6d3-5d569fea9574",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7436",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a075d96a-b573-4ed5-8d06-e37c7ae073dc",
        "num_publications": 21,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1516",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "655edf81-d3e2-41f8-b3f1-0fd92ff49367",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1634",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10004205983841385
      },
      {
        "type": "literature_co-occurrence",
        "id": "07e8031f-da3f-4085-a05b-a7923d34ad30",
        "num_publications": 460,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005279",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11764288967400571
      },
      {
        "type": "literature_co-occurrence",
        "id": "6e29de85-dea0-49b5-917e-9c4177033f28",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1695",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9a0a1531-405b-4c5b-be3e-0a06aa40f8fd",
        "num_publications": 164,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0007191",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10642086042871002
      },
      {
        "type": "literature_co-occurrence",
        "id": "d1987fd3-c29f-4a52-afce-abdf2d164952",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:5173",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "72f4972a-f115-4c0f-8239-ebe1d75b959a",
        "num_publications": 63,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005279",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10023819729987538
      },
      {
        "type": "literature_co-occurrence",
        "id": "73126933-ec74-4a10-adbc-07a344d2b5cd",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12680",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "42710e03-1759-49e4-87d9-dde68c8aab08",
        "num_publications": 310,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10240109124160168
      },
      {
        "type": "literature_co-occurrence",
        "id": "a3888560-692c-4833-8a88-125e0d36be4d",
        "num_publications": 567,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005657",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.12240921577719743
      },
      {
        "type": "literature_co-occurrence",
        "id": "78e8cd5f-8491-4677-bf3d-d9f98c695e86",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005657",
        "target_id": "HGNC:5438",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10004421367822569
      },
      {
        "type": "literature_co-occurrence",
        "id": "edc74501-6cdc-499a-875a-21bdccb43f4b",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:990",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "cd8dd063-0ec7-4c9e-8fc2-32a6d37f66f4",
        "num_publications": 8,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:583",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10003834709820436
      },
      {
        "type": "literature_co-occurrence",
        "id": "d188e62c-e201-4b32-b3e4-43fc77b49915",
        "num_publications": 56,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:5173",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10179696975891728
      },
      {
        "type": "literature_co-occurrence",
        "id": "6fe33571-68cb-41c7-af1c-77d8e329ac98",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12796",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "6a662190-a7f1-4a93-9a80-e3e9fcfe6573",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12679",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "4738946c-9430-48f3-82e9-772619087210",
        "num_publications": 74,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005825",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1028221256422468
      },
      {
        "type": "literature_co-occurrence",
        "id": "4e813b42-dc60-40c5-be59-1526f44dcecb",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1078",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10014746035824718
      },
      {
        "type": "literature_co-occurrence",
        "id": "29a68ee9-d8db-47a1-b6bc-1759867e471f",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12362",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10006005648632688
      },
      {
        "type": "literature_co-occurrence",
        "id": "f9d6e263-c4c2-4f08-83ef-d8d7508efee2",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11768",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10003038065797387
      },
      {
        "type": "literature_co-occurrence",
        "id": "41779006-bae4-4bcf-941e-610e2a8baf91",
        "num_publications": 130,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:2295",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10132415588883936
      },
      {
        "type": "literature_co-occurrence",
        "id": "68c8602b-a12b-446e-83a1-2e80866aee97",
        "num_publications": 661,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0002076",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.12605831682242852
      },
      {
        "type": "literature_co-occurrence",
        "id": "1f1eec31-ca08-47ea-ae00-8f58e1d44e67",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6770",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10006578377273767
      },
      {
        "type": "literature_co-occurrence",
        "id": "09bdf6cb-27a8-4f7d-a046-ec7f9821515a",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:894",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "98bf3607-9d01-439e-b8b6-334b0c6cd3f1",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:12651",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b6d040c9-7aeb-40d1-bd7e-8bd521274dea",
        "num_publications": 132,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005149",
        "target_id": "HGNC:7876",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1049904233799559
      },
      {
        "type": "literature_co-occurrence",
        "id": "fcab9d15-4847-4425-b8ec-745a2dd02b59",
        "num_publications": 60,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0002568",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10230413905383795
      },
      {
        "type": "literature_co-occurrence",
        "id": "653a41a0-1421-474d-aee6-9610fe0d9d9d",
        "num_publications": 23,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002568",
        "target_id": "HGNC:11722",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10090407238149757
      },
      {
        "type": "literature_co-occurrence",
        "id": "357f945d-bb26-4d9a-ac49-05e3c02d8812",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:9208",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10003752261184107
      },
      {
        "type": "literature_co-occurrence",
        "id": "b8741672-8ce3-4de1-a457-0a38eedb6f06",
        "num_publications": 236,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:9208",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10707034107376845
      },
      {
        "type": "literature_co-occurrence",
        "id": "bc79686a-b5ae-441b-a145-f6f7f935725f",
        "num_publications": 37,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0019121",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10116156496996354
      },
      {
        "type": "literature_co-occurrence",
        "id": "b7d8e996-6f84-4564-99cb-b50ca822ef6e",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7515",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000481883945667
      },
      {
        "type": "literature_co-occurrence",
        "id": "7e8fb0e1-9a86-4d16-9b83-0c3753c5b895",
        "num_publications": 40,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005657",
        "target_id": "HGNC:11848",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10139918330100317
      },
      {
        "type": "literature_co-occurrence",
        "id": "b68de93e-7cab-4450-8065-c37d18b08d11",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3942",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "d759e27a-9059-4338-b558-63822b7b8034",
        "num_publications": 340,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:6342",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11163902705713336
      },
      {
        "type": "literature_co-occurrence",
        "id": "695daf3a-5059-48be-9d57-5950f1ace359",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6204",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "af5beb5c-96a1-4444-8c0e-88bf41d8d027",
        "num_publications": 16,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:6204",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "ccdc03ab-5e45-4fa6-bc18-2903d4410a29",
        "num_publications": 8,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1693",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1002011470592088
      },
      {
        "type": "literature_co-occurrence",
        "id": "3e663fd5-c703-455f-9b00-95431f7204fd",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11825",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002422514653253
      },
      {
        "type": "literature_co-occurrence",
        "id": "36ce6c55-c075-426e-9348-5d2ef326c938",
        "num_publications": 30,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005058",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10103077042685615
      },
      {
        "type": "literature_co-occurrence",
        "id": "ad7c10fc-0b80-4861-803e-b7f46799845d",
        "num_publications": 11,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007191",
        "target_id": "HGNC:1516",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9bc5f308-bece-44e7-b366-128a3a0c199b",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7531",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001515633959568
      },
      {
        "type": "literature_co-occurrence",
        "id": "6553dde3-90e6-442a-9249-99a5e6f0f933",
        "num_publications": 198,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0018667",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10773853481487128
      },
      {
        "type": "literature_co-occurrence",
        "id": "cfcd27f5-6364-4809-8190-bc3cf60f700e",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:15633",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "e3d91d36-dc47-44c0-97bf-94fdd14e5cb4",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:8729",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "28d37fbf-2bfe-4c58-9499-ee8ded0728e4",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:10896",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "24171e4f-6ff7-45cd-80a8-cb51fbe99830",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:2637",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "e6026ec6-200c-4314-9311-6223b47be88c",
        "num_publications": 157,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007915",
        "target_id": "HGNC:1318",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10588857217637426
      },
      {
        "type": "literature_co-occurrence",
        "id": "e8dbd5c1-ae32-4771-9ab5-a1f119674473",
        "num_publications": 18,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:17941",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10069016705130562
      },
      {
        "type": "literature_co-occurrence",
        "id": "89d37a96-83f1-4b99-826d-4a49543eefad",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1331",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "0ec14d0b-aaa0-4d4f-842c-8ca710a6a79f",
        "num_publications": 236,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0003781",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10896459870387265
      },
      {
        "type": "literature_co-occurrence",
        "id": "90b76a43-05da-4d2f-8c35-0d44215a3a1f",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7989",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000434895308685
      },
      {
        "type": "literature_co-occurrence",
        "id": "ac079803-90d8-412b-a8ba-60954973bfc5",
        "num_publications": 36,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0004492",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10137095124828721
      },
      {
        "type": "literature_co-occurrence",
        "id": "246cf859-1443-4825-9e3f-c42cda25577e",
        "num_publications": 12,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0005974",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10042071928639673
      },
      {
        "type": "literature_co-occurrence",
        "id": "6666e7cd-cfd2-47f1-acff-e3afa674a04f",
        "num_publications": 480,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:27004",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11762577981313149
      },
      {
        "type": "literature_co-occurrence",
        "id": "c19179ec-922c-4a6c-80b2-00cef30fa5d2",
        "num_publications": 46,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005974",
        "target_id": "HGNC:27004",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10129480737212093
      },
      {
        "type": "literature_co-occurrence",
        "id": "e9bad44b-25d2-4da8-b558-a710a4fe89aa",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b027e13e-3f39-470b-bf15-62206de64a9d",
        "num_publications": 41,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:1773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10134773547511655
      },
      {
        "type": "literature_co-occurrence",
        "id": "0dd171a3-04de-43db-a4be-ebf09a63c7b8",
        "num_publications": 31,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:11825",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10107215277995507
      },
      {
        "type": "literature_co-occurrence",
        "id": "45afbd5c-b2fe-4fe2-8655-c982bdb8c6a9",
        "num_publications": 35,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007140",
        "target_id": "HGNC:7436",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10132475768000104
      },
      {
        "type": "literature_co-occurrence",
        "id": "2660e5b9-ab35-4a40-b260-78fa5aadde56",
        "num_publications": 181,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:1773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10646769853777271
      },
      {
        "type": "literature_co-occurrence",
        "id": "efb36668-168b-423f-adbf-4e1cf3e3fe71",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:4057",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b23530e0-3e0a-47d2-a1a6-1dbf5f5bfe8f",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:4057",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b6c5b7e7-6c1a-4b84-9424-f12ed831022a",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:9864",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000870323344868
      },
      {
        "type": "literature_co-occurrence",
        "id": "3fcc313c-1771-4e98-8a2b-282b23f3f086",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:9864",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a82af5d4-ea60-4097-9e4d-c62e1ef72a66",
        "num_publications": 14,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:4603",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "ca6f9d74-aacf-423b-9d52-52eda69ad327",
        "num_publications": 110,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:6204",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10335997459599844
      },
      {
        "type": "literature_co-occurrence",
        "id": "1a67f7c6-c9ca-4387-a754-c08e8ae7acbd",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:6935",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b72bbe3a-7c9a-4d81-a0ac-c48951ca1fc6",
        "num_publications": 17,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:12680",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "beff4fc7-93ee-4423-a766-bc3c53ec935a",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:795",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "7ee09dc5-e449-4836-baae-10eed1240ae7",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:16781",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002796857461038
      },
      {
        "type": "literature_co-occurrence",
        "id": "29c299f0-fe55-4984-adb4-fc3d6f446342",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:16781",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "dc3b26b4-c084-4993-b206-e2a5152fe227",
        "num_publications": 6,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11183",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a03c35db-4b8c-4d1d-a67b-419afc4ff85c",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:4234",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "8fdc8ea6-302b-4694-816c-d1169710a5b7",
        "num_publications": 221,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:12680",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10712984616582355
      },
      {
        "type": "literature_co-occurrence",
        "id": "2edb34f2-fe85-44df-af03-46d0ea23f5c7",
        "num_publications": 10,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:307",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10025171183773662
      },
      {
        "type": "literature_co-occurrence",
        "id": "40ff5b74-db6c-4676-be56-3d9efc6c73a3",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:307",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10026978228160788
      },
      {
        "type": "literature_co-occurrence",
        "id": "9b140846-32e1-4574-b655-796b7ac54f75",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:4837",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "2d8449e5-8a74-41d8-b8b8-702e71b8077b",
        "num_publications": 79,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007915",
        "target_id": "HGNC:6018",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10232513675414967
      },
      {
        "type": "literature_co-occurrence",
        "id": "fda92bc4-df81-4618-8681-e96d6b552764",
        "num_publications": 17,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "ac32a369-076c-4c14-820f-7cac67b92cc4",
        "num_publications": 32,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:11925",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1010988646333083
      },
      {
        "type": "literature_co-occurrence",
        "id": "65d91f85-dada-41ee-bb40-1a377d862245",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7124",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002608902913201
      },
      {
        "type": "literature_co-occurrence",
        "id": "caab29af-1337-495f-b191-91137344b224",
        "num_publications": 13,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:6204",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "ecbe7598-34ba-491c-b589-d66b6a900de2",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1472",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "00ac3850-75da-4437-b89d-0a105d3ef93d",
        "num_publications": 121,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:1472",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "ee03eab1-2eff-4753-a185-48b9956bae29",
        "num_publications": 16,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:9689",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10026602707006449
      },
      {
        "type": "literature_co-occurrence",
        "id": "fbe70775-422a-47af-8b34-a65f8f386c74",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3349",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002355665106433
      },
      {
        "type": "literature_co-occurrence",
        "id": "7f3e75ba-2cb4-41e6-af99-499e99de2fb9",
        "num_publications": 6428,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:1884",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.3497087675243802
      },
      {
        "type": "literature_co-occurrence",
        "id": "91c29a06-7bbd-4d6f-b9c1-66091857dd85",
        "num_publications": 169,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005149",
        "target_id": "HGNC:1078",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10672875318420372
      },
      {
        "type": "literature_co-occurrence",
        "id": "06138187-242b-4e0b-8290-a0c4a3126d77",
        "num_publications": 51,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:6018",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a502287b-7a86-4d3d-a0c0-907ea8f587c5",
        "num_publications": 1206,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:7029",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10215538151678993
      },
      {
        "type": "literature_co-occurrence",
        "id": "a3820c04-2130-4bf3-870b-e7c9bcd14d4c",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3657",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10002489332305364
      },
      {
        "type": "literature_co-occurrence",
        "id": "64b32f6f-5a0a-4d72-a07b-9d2012800d13",
        "num_publications": 93,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:6973",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1032668808140178
      },
      {
        "type": "literature_co-occurrence",
        "id": "61ccb8c7-112d-4137-b3e1-c5c52fee3f28",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1097",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "96a0dfb4-a315-411b-8b59-0ce7b9347b81",
        "num_publications": 37,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002462",
        "target_id": "HGNC:15633",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10124050916170091
      },
      {
        "type": "literature_co-occurrence",
        "id": "a379968c-b3a1-48a9-8923-69ba8c3e16c9",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:4837",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "8edb6baf-97bf-4ffa-ad69-8abe5c7aa5ed",
        "num_publications": 145,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:259",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10520790983337536
      },
      {
        "type": "literature_co-occurrence",
        "id": "5ec3bca7-d2d7-4e83-bc74-e705c9a0b824",
        "num_publications": 142,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0012105",
        "target_id": "HGNC:7218",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10549820314426639
      },
      {
        "type": "literature_co-occurrence",
        "id": "7ca38e7e-4a3c-42d3-98f1-b38803054eb0",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:10261",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10006840480079149
      },
      {
        "type": "literature_co-occurrence",
        "id": "636f790a-dae4-4f8e-836e-16fc7cd708b7",
        "num_publications": 234,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10307398491455033
      },
      {
        "type": "literature_co-occurrence",
        "id": "e6d2f528-f8e9-4893-8939-697cdcd63ace",
        "num_publications": 34,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007191",
        "target_id": "HGNC:11920",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10078534978860565
      },
      {
        "type": "literature_co-occurrence",
        "id": "6a428009-bf33-47c3-8a00-2a9584073f2c",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1050",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10001972425403993
      },
      {
        "type": "literature_co-occurrence",
        "id": "00245fe3-b418-4e40-bf01-5e45b735f557",
        "num_publications": 169,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:1050",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10501210662014981
      },
      {
        "type": "literature_co-occurrence",
        "id": "ec4983f9-5460-4463-b5f1-5aee5fba320b",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11249",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10009701555320594
      },
      {
        "type": "literature_co-occurrence",
        "id": "1178bf6a-2eec-4f48-8960-2216288d7351",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:11249",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10086717823420643
      },
      {
        "type": "literature_co-occurrence",
        "id": "f442c0de-3752-4c85-8e16-2044b2e5c292",
        "num_publications": 59,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:11825",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10229617983470574
      },
      {
        "type": "literature_co-occurrence",
        "id": "0d910f59-7b57-4631-bc38-dc6af7d48ce8",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3229",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "1e08325e-1eee-4a81-af33-6508637c0a5f",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:3349",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "4da67aa5-6ab9-48f8-a7aa-0c78cbdd808d",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:3765",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "024d40f3-5c3d-49dd-a74e-47c9dd3ca3c5",
        "num_publications": 6,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:8636",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "64a48dbe-c7cb-4461-9939-fccfed2a470c",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:17643",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10003825908609965
      },
      {
        "type": "literature_co-occurrence",
        "id": "d8f0f46e-45d6-4d96-8036-02fa1c2ba9c8",
        "num_publications": 21,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:17643",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10083185778391945
      },
      {
        "type": "literature_co-occurrence",
        "id": "4f9c539c-46c6-403b-b74a-89eef6b41dc5",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7321",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "c16f2fb3-e28d-4d4c-ab66-bb99b8e76b26",
        "num_publications": 33,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:6018",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.100637708313835
      },
      {
        "type": "literature_co-occurrence",
        "id": "6eb7ac4f-9c71-44cc-9e8f-8f1275933688",
        "num_publications": 9,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:5438",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10011456527012108
      },
      {
        "type": "literature_co-occurrence",
        "id": "4000cdaa-c19e-42ba-89fa-2d9da7750386",
        "num_publications": 18,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:7865",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1001195371781467
      },
      {
        "type": "literature_co-occurrence",
        "id": "26068437-c5d8-4f2e-b504-18c1eac8f3b5",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:23506",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000721525994372
      },
      {
        "type": "literature_co-occurrence",
        "id": "8763d51e-cb5f-40ac-9be5-4002e683008f",
        "num_publications": 37,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:23506",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10132731300520681
      },
      {
        "type": "literature_co-occurrence",
        "id": "3146238d-dc22-4316-9e8d-91e9545392a4",
        "num_publications": 90,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:6407",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10308188843555921
      },
      {
        "type": "literature_co-occurrence",
        "id": "46185e64-99d1-405b-a5ce-4f0f6500f4f7",
        "num_publications": 17,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004670",
        "target_id": "HGNC:11365",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10062377320722415
      },
      {
        "type": "literature_co-occurrence",
        "id": "c156621d-c2be-4850-9de3-9a038f3a88cc",
        "num_publications": 28,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:1634",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10071640968763673
      },
      {
        "type": "literature_co-occurrence",
        "id": "30e54399-ddbd-4660-878d-1b2b8664c479",
        "num_publications": 32,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0003781",
        "target_id": "HGNC:7218",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10086535418430409
      },
      {
        "type": "literature_co-occurrence",
        "id": "def1d058-498a-44a5-b636-5f74264fbc0a",
        "num_publications": 35,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005396",
        "target_id": "HGNC:6769",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1013827852368403
      },
      {
        "type": "literature_co-occurrence",
        "id": "bcd1cbd7-da62-4015-ae8a-2915d4987991",
        "num_publications": 135,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005812",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10167222806866805
      },
      {
        "type": "literature_co-occurrence",
        "id": "4547b505-3a9c-40de-9198-5cf293650f2f",
        "num_publications": 1951,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:3765",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.17760263224066597
      },
      {
        "type": "literature_co-occurrence",
        "id": "777fc308-370d-432e-bbe9-e647f7bba182",
        "num_publications": 17,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005396",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10065922617185619
      },
      {
        "type": "literature_co-occurrence",
        "id": "5eea36f8-be38-4582-96a3-dd3eb0a97ad1",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:1659",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000672971069469
      },
      {
        "type": "literature_co-occurrence",
        "id": "7aee237f-5d23-49ad-9f5d-d6733574ff03",
        "num_publications": 38,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:2637",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "e6ef7a6b-a309-41e7-bba1-38b366e73961",
        "num_publications": 50,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:6935",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10170335815963294
      },
      {
        "type": "literature_co-occurrence",
        "id": "ff0919de-468c-4e8e-9d7c-3289bcb986d7",
        "num_publications": 184,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:9689",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10584982012498934
      },
      {
        "type": "literature_co-occurrence",
        "id": "9d99e913-aeed-4c87-b76c-2342b197684f",
        "num_publications": 330,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1516",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "dc8b39a3-0510-43a4-98a6-adb7ade127e8",
        "num_publications": 105,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:11183",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "3ab300a9-48da-40b2-9989-0a15e7389507",
        "num_publications": 83,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:7515",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10315603849331001
      },
      {
        "type": "literature_co-occurrence",
        "id": "f1626e97-3586-4535-9eea-381afb9f34b3",
        "num_publications": 1282,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:427",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1509626016440061
      },
      {
        "type": "literature_co-occurrence",
        "id": "231143ed-3952-4cb4-a8b1-5247e0f54776",
        "num_publications": 13,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "MONDO:0006656",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10048220640658123
      },
      {
        "type": "literature_co-occurrence",
        "id": "3f160b3b-ca7a-4400-9ab5-7df5122af84b",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0006656",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10084563574371708
      },
      {
        "type": "literature_co-occurrence",
        "id": "4850066a-5417-40b7-9bd2-573cf5c14f2b",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:7531",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "5431b21d-fa5e-459d-9d3a-3a6e64375807",
        "num_publications": 185,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:6973",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10631203604785677
      },
      {
        "type": "literature_co-occurrence",
        "id": "3e5ccb53-09e0-4c2d-a5c6-da81a576106d",
        "num_publications": 194,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:2707",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10482453277062842
      },
      {
        "type": "literature_co-occurrence",
        "id": "eeab134e-8992-4db2-b9d7-d172f7a5ac8c",
        "num_publications": 25,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004670",
        "target_id": "HGNC:12269",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10099226963480357
      },
      {
        "type": "literature_co-occurrence",
        "id": "b6167a85-cc76-45a0-9317-21f54d69aada",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:175",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10015172066121758
      },
      {
        "type": "literature_co-occurrence",
        "id": "699df82b-7de8-4579-9aa5-e67bef82ce5f",
        "num_publications": 22,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:7876",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "95a4a14d-804b-4781-acf3-9ec3c9dc51e4",
        "num_publications": 1284,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:7029",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.13215135909218823
      },
      {
        "type": "literature_co-occurrence",
        "id": "aa96dace-92ac-4dd9-8e8e-a30475cda44f",
        "num_publications": 135,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:20387",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "4bf86012-8190-4e95-8a56-75f90a64a254",
        "num_publications": 4546,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:20387",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "0fb7650b-b4ba-415b-936c-8cab9f45cbef",
        "num_publications": 45,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:1693",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1012820679563734
      },
      {
        "type": "literature_co-occurrence",
        "id": "1932a066-d3de-43a5-ab80-a9f10a173c3e",
        "num_publications": 48,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005396",
        "target_id": "HGNC:11773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10191758087561054
      },
      {
        "type": "literature_co-occurrence",
        "id": "a193ff5e-5bd5-4178-87d3-01336434cfa5",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:11573",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "6bcd63b2-8895-4eca-bb2f-b2c4cb821d89",
        "num_publications": 160,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:11573",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10463391852440207
      },
      {
        "type": "literature_co-occurrence",
        "id": "f6e2e12c-ea68-41d7-b081-4d64e7b6a60b",
        "num_publications": 11,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002076",
        "target_id": "HGNC:12363",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10038111508405612
      },
      {
        "type": "literature_co-occurrence",
        "id": "1bb6a333-dc12-4ebd-aa49-375ab8d97484",
        "num_publications": 144,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002462",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10356320960092902
      },
      {
        "type": "literature_co-occurrence",
        "id": "88e3c734-8b9b-469e-86d6-8a63a59926cb",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:648",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "c29174d4-6925-4e3a-91cc-8b1d767d5804",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:10896",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "14c1e53c-ff44-49d1-8f90-1a400167e573",
        "num_publications": 108,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:5438",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10387344160608392
      },
      {
        "type": "literature_co-occurrence",
        "id": "cf7279cd-37df-42ac-84d2-13ba7e2423c0",
        "num_publications": 41,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0006277",
        "target_id": "HGNC:12363",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10163909395507253
      },
      {
        "type": "literature_co-occurrence",
        "id": "81e63527-e413-41a8-aa2e-27889deeca35",
        "num_publications": 74,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:795",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1011905155355356
      },
      {
        "type": "literature_co-occurrence",
        "id": "99d6270a-9796-4855-b3d1-7c8aa06942d2",
        "num_publications": 61,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:7218",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10174546497867087
      },
      {
        "type": "literature_co-occurrence",
        "id": "456e452f-a810-4d5f-9d6b-6f9eadcec7fd",
        "num_publications": 342,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:11998",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11279665618300072
      },
      {
        "type": "literature_co-occurrence",
        "id": "6548a938-10b8-4199-ac43-2144d468b993",
        "num_publications": 30,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004822",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10067708104670814
      },
      {
        "type": "literature_co-occurrence",
        "id": "ab6a5a5c-c120-4153-8ed6-823cdd6eb25b",
        "num_publications": 583,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019065",
        "target_id": "HGNC:108",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.12162772572561209
      },
      {
        "type": "literature_co-occurrence",
        "id": "67240bb3-d838-4f72-8739-13e167a46b8b",
        "num_publications": 5969,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:3236",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.33079522589239074
      },
      {
        "type": "literature_co-occurrence",
        "id": "8a0e0908-37c1-4d18-ae7e-3007c37dbb15",
        "num_publications": 163,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019338",
        "target_id": "HGNC:1678",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10370854868018509
      },
      {
        "type": "literature_co-occurrence",
        "id": "f1186809-1d21-457e-9c62-c64b78b0ce85",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004822",
        "target_id": "HGNC:1698",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1000232981920105
      },
      {
        "type": "literature_co-occurrence",
        "id": "5cde924e-e871-4ad1-8a47-9cb59b6e1907",
        "num_publications": 356,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:1678",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10297728410232998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a94f7cf1-a880-44a0-a8db-cd2a9994c3a5",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:8594",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "5c800fcc-a4b7-4db7-8d22-ad57878df856",
        "num_publications": 1,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "HP:0002105",
        "target_id": "HGNC:15990",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10000214048714773
      },
      {
        "type": "literature_co-occurrence",
        "id": "10125de2-f8e5-4991-9c8a-0e50eb97aecd",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:15990",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b095dfb4-2e5d-4d39-a228-182a77d7bc51",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005279",
        "target_id": "HGNC:12726",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10037528698412779
      },
      {
        "type": "literature_co-occurrence",
        "id": "1cf325ff-ff6e-4150-87b9-7ebb4c80e8c0",
        "num_publications": 14,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:7321",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "6dea9a51-e684-4e73-acdd-a14a419d7cd1",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1050",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "215bcbf1-42c7-427a-b544-8fa9b4e3daad",
        "num_publications": 2948,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:20387",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.16658406397877845
      },
      {
        "type": "literature_co-occurrence",
        "id": "847b4dbc-b416-4a4c-9f6e-eaa0625bc13f",
        "num_publications": 115,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:1662",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10312483016594065
      },
      {
        "type": "literature_co-occurrence",
        "id": "f594a22f-1d77-4a3d-9d04-43fe1dd4578b",
        "num_publications": 71,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005279",
        "target_id": "HGNC:7436",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10244807486833674
      },
      {
        "type": "literature_co-occurrence",
        "id": "c3ea54b6-ec4c-4e9e-ac39-6b1f99f2bfb3",
        "num_publications": 45,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:8594",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1009013575081894
      },
      {
        "type": "literature_co-occurrence",
        "id": "98b72ee8-9daa-460b-bd54-7ead9a5f974d",
        "num_publications": 63,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:15633",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10127401833606964
      },
      {
        "type": "literature_co-occurrence",
        "id": "051059d7-911a-4480-bcdf-28d6bc43fee3",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:12796",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a96964d0-e071-4e76-9428-e34da2031cfd",
        "num_publications": 161,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:7218",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10485280167146616
      },
      {
        "type": "literature_co-occurrence",
        "id": "52e2545a-e864-4e4d-83b4-f7f8273ae11a",
        "num_publications": 4559,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:317",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.2782015859368945
      },
      {
        "type": "literature_co-occurrence",
        "id": "a2aa7bb2-ff09-41b6-b8d4-293ac9712d7c",
        "num_publications": 162,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10146912847230449
      },
      {
        "type": "literature_co-occurrence",
        "id": "ab69f6c4-ea20-494c-9195-e2ada5957fc3",
        "num_publications": 568,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019338",
        "target_id": "HGNC:2707",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.12198171108729916
      },
      {
        "type": "literature_co-occurrence",
        "id": "533a819b-cbec-4e22-bc13-50724660c9ee",
        "num_publications": 1079,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019121",
        "target_id": "HGNC:1678",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.14115492633124094
      },
      {
        "type": "literature_co-occurrence",
        "id": "f8bf2d98-924c-4cb0-8a3e-110316269243",
        "num_publications": 71,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007915",
        "target_id": "HGNC:1516",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "a543b153-56ef-4061-8e58-df45aa8332bf",
        "num_publications": 108,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:17941",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10418104387507587
      },
      {
        "type": "literature_co-occurrence",
        "id": "123555ce-21d1-4673-a774-ffbf3673604b",
        "num_publications": 81,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:583",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10210278188095945
      },
      {
        "type": "literature_co-occurrence",
        "id": "22ecb0af-90d1-4c5a-90b6-ffb6ad015265",
        "num_publications": 39,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0003781",
        "target_id": "HGNC:7515",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10146214138711485
      },
      {
        "type": "literature_co-occurrence",
        "id": "ef87d609-7495-4c76-861e-fc18cbd1f73c",
        "num_publications": 192,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:27004",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10036738131467349
      },
      {
        "type": "literature_co-occurrence",
        "id": "1cf4d951-b27d-494f-a7ff-3512eb34f91e",
        "num_publications": 85,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:8636",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10173533262514001
      },
      {
        "type": "literature_co-occurrence",
        "id": "b21c1a07-5458-4e6c-b7ea-c04e7ab07f6f",
        "num_publications": 74,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005812",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10126451217988286
      },
      {
        "type": "literature_co-occurrence",
        "id": "e8aee3d6-ebc7-4c7b-b378-350f24f0113a",
        "num_publications": 48,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0003781",
        "target_id": "HGNC:1884",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10151667675326492
      },
      {
        "type": "literature_co-occurrence",
        "id": "3813ed7e-82fb-42bc-9d97-03012aa8cdd4",
        "num_publications": 77,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0011827",
        "target_id": "HGNC:23506",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1030588376037248
      },
      {
        "type": "literature_co-occurrence",
        "id": "b0c8ca5f-fc49-42e4-9f57-4798ec0d55d1",
        "num_publications": 134,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:11920",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1025027950309112
      },
      {
        "type": "literature_co-occurrence",
        "id": "6fb30f27-f398-4ed6-90d1-225dd6dfb642",
        "num_publications": 99,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:6342",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "f305827b-326a-4d0b-98bd-a704b27d341a",
        "num_publications": 51,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0001243",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10108534908279809
      },
      {
        "type": "literature_co-occurrence",
        "id": "d56e7cdf-4a5a-4ef5-b85f-e17cdb2a8980",
        "num_publications": 187,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0006932",
        "target_id": "HGNC:1516",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10202095889037188
      },
      {
        "type": "literature_co-occurrence",
        "id": "9ac01071-2fc4-4638-a7eb-483a8794ed1c",
        "num_publications": 1722,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:12388",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.16748686880649344
      },
      {
        "type": "literature_co-occurrence",
        "id": "a9c329d3-567f-420e-bb37-3c2660242c72",
        "num_publications": 57,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:1693",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10101581091407774
      },
      {
        "type": "literature_co-occurrence",
        "id": "35fe2ba4-1319-4cbd-9d18-4897b923fcfc",
        "num_publications": 51,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:6769",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10171104189044922
      },
      {
        "type": "literature_co-occurrence",
        "id": "42cd0d6a-053e-4433-a73c-8d7819c449b9",
        "num_publications": 365,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:3229",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11070002547246183
      },
      {
        "type": "literature_co-occurrence",
        "id": "6f784abd-54c9-4b5e-a1e0-0f3c388ef06e",
        "num_publications": 14,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:990",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "7908c7f5-ff27-4457-a017-3be747b8b371",
        "num_publications": 84,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:6342",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10087424458243355
      },
      {
        "type": "literature_co-occurrence",
        "id": "9a1c57b9-556e-4571-8950-277d7badc03d",
        "num_publications": 80,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:1097",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10170379975584176
      },
      {
        "type": "literature_co-occurrence",
        "id": "32c6ebe4-96f2-4b5d-8099-58b0e244b01a",
        "num_publications": 265,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:10261",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11055210408902971
      },
      {
        "type": "literature_co-occurrence",
        "id": "dd66d7f2-d9f8-415d-a3b4-6180990dec5d",
        "num_publications": 9,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004822",
        "target_id": "HGNC:7865",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9f1f3436-6cb3-482f-84ea-cd7672bb05de",
        "num_publications": 68,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0003781",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10128338112706758
      },
      {
        "type": "literature_co-occurrence",
        "id": "dd56164a-4d26-494a-8fdc-c0f164f0f694",
        "num_publications": 32,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:2201",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10122866746416048
      },
      {
        "type": "literature_co-occurrence",
        "id": "78e4e770-2712-4f0d-adbe-3264e70f0280",
        "num_publications": 110,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10212087640921597
      },
      {
        "type": "literature_co-occurrence",
        "id": "058e91c1-8c81-4cb4-902c-c4768ab5b216",
        "num_publications": 107,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:3236",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "c42229b8-520c-4d2d-ab17-c744941cee94",
        "num_publications": 193,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:583",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1049893875211051
      },
      {
        "type": "literature_co-occurrence",
        "id": "ad41a7cf-286b-4be4-ae26-3e80ac64a95b",
        "num_publications": 8,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:11998",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "7bda85d5-3f03-404c-81c9-b9a7b6ff8e64",
        "num_publications": 42,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:6204",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10124686914619563
      },
      {
        "type": "literature_co-occurrence",
        "id": "4da159d0-307e-4ae0-b0ae-df6dd6d04802",
        "num_publications": 308,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10659110793391224
      },
      {
        "type": "literature_co-occurrence",
        "id": "b2497bd7-1be0-4d98-9c52-78f34bc43d6c",
        "num_publications": 234,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019180",
        "target_id": "HGNC:175",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10935709879122812
      },
      {
        "type": "literature_co-occurrence",
        "id": "f13f202c-3f29-4d5a-8f95-51fc07a28a27",
        "num_publications": 667,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11524694423513637
      },
      {
        "type": "literature_co-occurrence",
        "id": "7dc1e0a5-dc33-40e9-a1ee-efc7c5a2e4ba",
        "num_publications": 35,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005812",
        "target_id": "HGNC:15633",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10093545449423347
      },
      {
        "type": "literature_co-occurrence",
        "id": "a7f8902c-d26d-4125-97af-7667a827674c",
        "num_publications": 25,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:12363",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1009010192868881
      },
      {
        "type": "literature_co-occurrence",
        "id": "ba756d7c-9dbb-43aa-97a5-6954d346ba7b",
        "num_publications": 13,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005396",
        "target_id": "HGNC:11768",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10051778631911146
      },
      {
        "type": "literature_co-occurrence",
        "id": "0045a810-b19a-45a9-aeef-cf5f34f7e304",
        "num_publications": 62,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:2707",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "eb4c94a5-6803-4a21-ba51-aeaae5c11757",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:3535",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "34d15b30-b0b6-49c9-903a-e59f8bfe624f",
        "num_publications": 67,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:4603",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10228447769114579
      },
      {
        "type": "literature_co-occurrence",
        "id": "8c335ffb-0ac7-4449-92b2-ccc11a94d37f",
        "num_publications": 142,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004822",
        "target_id": "HGNC:1884",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10553283675319036
      },
      {
        "type": "literature_co-occurrence",
        "id": "a3939df2-009d-4b46-a210-91048d58cfeb",
        "num_publications": 30,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:4603",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10102691519137308
      },
      {
        "type": "literature_co-occurrence",
        "id": "ba61fe3b-3092-455b-8a0a-a24710e992e3",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:6769",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "23ad785a-853b-49ce-9539-917e945778ee",
        "num_publications": 136,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:6018",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10401895357011215
      },
      {
        "type": "literature_co-occurrence",
        "id": "4cb983e4-1598-4cc7-8f96-0fec5e1985ef",
        "num_publications": 259,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:11920",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10776234093569359
      },
      {
        "type": "literature_co-occurrence",
        "id": "cfdd064e-19de-4d15-9167-1fd2af435fdd",
        "num_publications": 38,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005657",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10115531675014156
      },
      {
        "type": "literature_co-occurrence",
        "id": "10f8ff3b-44ce-4956-bdab-8c1c9e2cc5c6",
        "num_publications": 38,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:11848",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10091745946581254
      },
      {
        "type": "literature_co-occurrence",
        "id": "91093666-c719-4f63-b01f-88493c217c8e",
        "num_publications": 469,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:3942",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11599871606754564
      },
      {
        "type": "literature_co-occurrence",
        "id": "59b75b54-fbef-45a9-be68-e3b742a4765c",
        "num_publications": 134,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019338",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10379076669880216
      },
      {
        "type": "literature_co-occurrence",
        "id": "fb9b8bd5-feae-49b3-b25a-9de63d92afd5",
        "num_publications": 86,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:12651",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "b0cdfdbd-425a-4da2-8201-5e74a6eaecf5",
        "num_publications": 25,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005812",
        "target_id": "HGNC:7124",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10089963892055342
      },
      {
        "type": "literature_co-occurrence",
        "id": "95f0d351-c24d-4d28-89a2-be52b5166742",
        "num_publications": 80,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002363",
        "target_id": "HGNC:11998",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1028071793647447
      },
      {
        "type": "literature_co-occurrence",
        "id": "0827515b-423a-4bc5-b6b9-9ae6e84a8d1b",
        "num_publications": 8,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:894",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "d84f5de2-d7de-4445-a5f2-f084c4a15fd1",
        "num_publications": 147,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:27004",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "4a0c9d21-e16d-4f07-b9dd-ea09963b35dd",
        "num_publications": 139,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10516164290253449
      },
      {
        "type": "literature_co-occurrence",
        "id": "5fdb0a52-6c1c-4de5-a141-c30c33988025",
        "num_publications": 27,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:7436",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10072164835556985
      },
      {
        "type": "literature_co-occurrence",
        "id": "4160dcd6-b360-460a-9b7b-b8b774a0545f",
        "num_publications": 441,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007915",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11469396155815437
      },
      {
        "type": "literature_co-occurrence",
        "id": "ffd25be4-d433-4d48-93dc-e22e167c60f2",
        "num_publications": 162,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:7989",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10634869341081643
      },
      {
        "type": "literature_co-occurrence",
        "id": "90a6ba3d-9e8a-4a2c-afaa-b445d105204d",
        "num_publications": 47,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:9273",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10169928509580539
      },
      {
        "type": "literature_co-occurrence",
        "id": "8c4d68d7-aa7d-45ce-94bb-a9b388bdf62c",
        "num_publications": 33,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005149",
        "target_id": "HGNC:175",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10129964228249111
      },
      {
        "type": "literature_co-occurrence",
        "id": "d88676fb-2ea5-4d64-bcd6-8ae40f8966e9",
        "num_publications": 1137,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019065",
        "target_id": "HGNC:12405",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.14510793910360054
      },
      {
        "type": "literature_co-occurrence",
        "id": "8f29925a-21a2-4387-ace3-143657fd2c74",
        "num_publications": 119,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:8729",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10396464523910409
      },
      {
        "type": "literature_co-occurrence",
        "id": "f5812967-7bec-4a10-a089-995988872fb5",
        "num_publications": 8424,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019065",
        "target_id": "HGNC:620",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.42051013112569735
      },
      {
        "type": "literature_co-occurrence",
        "id": "d853a01a-6b31-4776-adcd-36085960a189",
        "num_publications": 9,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002076",
        "target_id": "HGNC:2201",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.100334294332595
      },
      {
        "type": "literature_co-occurrence",
        "id": "566660aa-6e93-4a48-9973-efe0179484e2",
        "num_publications": 243,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007915",
        "target_id": "HGNC:15633",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10935229285538317
      },
      {
        "type": "literature_co-occurrence",
        "id": "40aa1e35-c5f3-4b25-a8dc-be18e973a496",
        "num_publications": 51,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005812",
        "target_id": "HGNC:11848",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10110654828254206
      },
      {
        "type": "literature_co-occurrence",
        "id": "ceac4a36-ca9f-4828-aaf1-b8c5723989b0",
        "num_publications": 13,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004822",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "6b8f8b25-45f3-4401-a243-0285f8509b69",
        "num_publications": 207,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019065",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10458905016300912
      },
      {
        "type": "literature_co-occurrence",
        "id": "4570615e-da8e-456c-a0d6-3b4811077dfc",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004492",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10075119305405245
      },
      {
        "type": "literature_co-occurrence",
        "id": "ae32f692-47f9-49ab-af60-7ef06c7ca776",
        "num_publications": 77,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:648",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10186836498289753
      },
      {
        "type": "literature_co-occurrence",
        "id": "f43f7ee8-d9a6-4f26-908d-fc9b79e1e0fd",
        "num_publications": 12,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:4234",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "586e3522-6308-4ac3-95f6-6b314d87ca4c",
        "num_publications": 1581,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:7029",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9757ddcc-dc18-42fe-8a25-475ff40e62a7",
        "num_publications": 45,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005058",
        "target_id": "HGNC:11998",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10158354905153011
      },
      {
        "type": "literature_co-occurrence",
        "id": "0cde5943-6c9d-4840-bf9b-9a7ed4866db0",
        "num_publications": 45,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:2707",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10059757179584705
      },
      {
        "type": "literature_co-occurrence",
        "id": "b80be848-f2de-4f6a-899d-1cc760625ad5",
        "num_publications": 156,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:12680",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10552760555774732
      },
      {
        "type": "literature_co-occurrence",
        "id": "5f7ea310-295b-4cd1-a0ae-8ecfaa5dae9e",
        "num_publications": 9,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004822",
        "target_id": "HGNC:11722",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10033133319978049
      },
      {
        "type": "literature_co-occurrence",
        "id": "8cdaec86-1fee-4aa2-b314-4cb8a90b889c",
        "num_publications": 42,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019338",
        "target_id": "HGNC:1693",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10136438297437411
      },
      {
        "type": "literature_co-occurrence",
        "id": "f4a406a4-074f-45bd-a0e9-2c2ad4fd3554",
        "num_publications": 308,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:11848",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10981540832038472
      },
      {
        "type": "literature_co-occurrence",
        "id": "2c31905b-d8ef-4a1e-99c3-ed6a63d46c8f",
        "num_publications": 107,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1628",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10195501894984771
      },
      {
        "type": "literature_co-occurrence",
        "id": "9cfe97f6-3083-4c8a-8f84-2ff1e7a00ea6",
        "num_publications": 13,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1318",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "c9467ff3-42be-4ff0-afa0-5fd8033b89ad",
        "num_publications": 3,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:8803",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "3cc10b3f-d93d-4f04-9dfa-2ea641fcdb20",
        "num_publications": 23,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:11768",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10087803944931839
      },
      {
        "type": "literature_co-occurrence",
        "id": "16eebf17-8ad7-4e26-9e68-4ab0743c3cbf",
        "num_publications": 27,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002363",
        "target_id": "HGNC:5173",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10099779595638791
      },
      {
        "type": "literature_co-occurrence",
        "id": "972b4b0f-233e-4e79-96ed-b17ae9cc821d",
        "num_publications": 5,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:3765",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "7a5e5f21-acce-4eab-b478-71b530e89e90",
        "num_publications": 104,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10175374025754436
      },
      {
        "type": "literature_co-occurrence",
        "id": "753057aa-c7da-469f-a651-60b8c311239f",
        "num_publications": 7,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002076",
        "target_id": "HGNC:11722",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10021814898844783
      },
      {
        "type": "literature_co-occurrence",
        "id": "3834ceab-f340-4595-b693-414ca3b954cd",
        "num_publications": 114,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:990",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1041925826071024
      },
      {
        "type": "literature_co-occurrence",
        "id": "5b245966-a28b-4377-98d7-4531335aa201",
        "num_publications": 30,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005657",
        "target_id": "HGNC:1884",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10097491570424688
      },
      {
        "type": "literature_co-occurrence",
        "id": "e55cca82-bd37-4d6b-b69d-3f79db41b633",
        "num_publications": 154,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.101612285003704
      },
      {
        "type": "literature_co-occurrence",
        "id": "b76f8fab-dea9-4505-bf1f-68b007f52b4a",
        "num_publications": 157,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019065",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10206068918919675
      },
      {
        "type": "literature_co-occurrence",
        "id": "d1ba65fd-38e5-4d01-a66a-94814e4612f0",
        "num_publications": 77,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0017991",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10280259892942956
      },
      {
        "type": "literature_co-occurrence",
        "id": "09e8567b-7417-4604-9b94-436aedfeb1ba",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0004670",
        "target_id": "HGNC:4942",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10009968927213275
      },
      {
        "type": "literature_co-occurrence",
        "id": "ac3c92b4-8686-4493-bd04-425253d1a665",
        "num_publications": 85,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:6407",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1020317819653499
      },
      {
        "type": "literature_co-occurrence",
        "id": "3fad7f1e-e606-41c4-9be7-3db80f1b696b",
        "num_publications": 183,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10643412444066869
      },
      {
        "type": "literature_co-occurrence",
        "id": "4e18e231-ed54-4076-81ce-dc2d4d58f843",
        "num_publications": 29,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007915",
        "target_id": "HGNC:2956",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10112532090521353
      },
      {
        "type": "literature_co-occurrence",
        "id": "cec2d31d-abba-49a9-a00d-ca633907555e",
        "num_publications": 19,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1631",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10016400355750166
      },
      {
        "type": "literature_co-occurrence",
        "id": "96dee345-0b9b-4e28-b7ed-1a0afd7b80a9",
        "num_publications": 117,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:12679",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10293730646053667
      },
      {
        "type": "literature_co-occurrence",
        "id": "0573b3cc-c0a8-4040-8480-724b92b3a3a4",
        "num_publications": 140,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:11892",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10343118857548805
      },
      {
        "type": "literature_co-occurrence",
        "id": "73f9b121-3e7d-4d6f-9f8b-051da7e2d6bc",
        "num_publications": 18,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007191",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10052907873383965
      },
      {
        "type": "literature_co-occurrence",
        "id": "4af5995a-8115-4a18-9f6f-6ada9e11bfd9",
        "num_publications": 760,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:1659",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.13026472407309342
      },
      {
        "type": "literature_co-occurrence",
        "id": "bc78a8d5-f4c3-4bfb-8e43-fe9c7f2ba548",
        "num_publications": 1102,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:6407",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.14347382199748526
      },
      {
        "type": "literature_co-occurrence",
        "id": "2144aa9f-3e85-44b6-b5d6-ff6984c83b8e",
        "num_publications": 58,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:11850",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1012255645964183
      },
      {
        "type": "literature_co-occurrence",
        "id": "be055a40-abb0-4299-b845-41945f3e208a",
        "num_publications": 496,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0009061",
        "target_id": "HGNC:1472",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11518015984036412
      },
      {
        "type": "literature_co-occurrence",
        "id": "e65f77dd-e7ba-465c-b18f-673a86fde017",
        "num_publications": 41,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:6018",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10104821565270072
      },
      {
        "type": "literature_co-occurrence",
        "id": "cb2f567a-23c0-4871-a385-735fb7266dff",
        "num_publications": 79,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:1773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10283838361308184
      },
      {
        "type": "literature_co-occurrence",
        "id": "ac015958-b423-4c27-a96e-82f336af37fe",
        "num_publications": 31,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005396",
        "target_id": "HGNC:11772",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10123848674477454
      },
      {
        "type": "literature_co-occurrence",
        "id": "075909c0-78a3-4ea8-ac7b-5b785521010c",
        "num_publications": 290,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019180",
        "target_id": "HGNC:3349",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11157515507171867
      },
      {
        "type": "literature_co-occurrence",
        "id": "dc461c01-9177-422b-8b7c-9a40eb638936",
        "num_publications": 27,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:12680",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "cc3c836c-bbf7-4026-9845-5d9bda57bb44",
        "num_publications": 93,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002363",
        "target_id": "HGNC:3236",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1025253442659565
      },
      {
        "type": "literature_co-occurrence",
        "id": "c6cd093a-fe4a-493d-a047-6e9ed725a0e3",
        "num_publications": 101,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:7176",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10367102166777842
      },
      {
        "type": "literature_co-occurrence",
        "id": "3f34ee0f-452b-4c04-b83c-dd6fdf34973b",
        "num_publications": 349,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:6342",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10363044033755753
      },
      {
        "type": "literature_co-occurrence",
        "id": "d11c752b-0b43-41a2-879d-27e4636826f5",
        "num_publications": 67,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019180",
        "target_id": "HGNC:6770",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10266660918498505
      },
      {
        "type": "literature_co-occurrence",
        "id": "7191e9b8-356e-4b70-963d-ccf274f83efc",
        "num_publications": 161,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:644",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10251215103869249
      },
      {
        "type": "literature_co-occurrence",
        "id": "98eb7b9a-238f-4d50-a8d4-e7a2f9576bec",
        "num_publications": 479,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018874",
        "target_id": "HGNC:12796",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11893634300406264
      },
      {
        "type": "literature_co-occurrence",
        "id": "886d9ab3-431b-4b00-a312-7c4f46bfc59b",
        "num_publications": 47,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018667",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10133257642791293
      },
      {
        "type": "literature_co-occurrence",
        "id": "08e051f8-ad8c-46bb-b739-3c5f7df5b5de",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:175",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10007202158968964
      },
      {
        "type": "literature_co-occurrence",
        "id": "c7ca2c62-aff6-426d-83ab-46ef3fb1481b",
        "num_publications": 456,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:11998",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11612020253681732
      },
      {
        "type": "literature_co-occurrence",
        "id": "cd1faca0-1553-4217-96bd-87bf6f7d1105",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:11925",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "f8268d97-3624-4c9d-93d7-f311d16fc9b4",
        "num_publications": 4,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1659",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9328c5bf-9e3d-4fd7-97ae-5af57016b290",
        "num_publications": 219,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005233",
        "target_id": "HGNC:6342",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10660363218796332
      },
      {
        "type": "literature_co-occurrence",
        "id": "df4456ba-3911-46d2-bd4b-01971e806944",
        "num_publications": 143,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:11925",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.1052413326959909
      },
      {
        "type": "literature_co-occurrence",
        "id": "326d6798-6d22-42e5-84d6-57c09fa89fe1",
        "num_publications": 192,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1472",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "9bb4e880-984e-4396-ad31-3afb5f976392",
        "num_publications": 6,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:1698",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "4716c24a-6178-4eb9-a434-0e43da156703",
        "num_publications": 78,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:11773",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10307557880867091
      },
      {
        "type": "literature_co-occurrence",
        "id": "23d3d210-5444-4f2f-8f5b-52692643bb6f",
        "num_publications": 550,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005275",
        "target_id": "HGNC:1884",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.12045190385316784
      },
      {
        "type": "literature_co-occurrence",
        "id": "3eb898ca-cf12-4a74-9991-0252c9307fbd",
        "num_publications": 596,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0007256",
        "target_id": "HGNC:3236",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.11739613749831879
      },
      {
        "type": "literature_co-occurrence",
        "id": "07b31d5b-91b0-438b-a1ee-c29dc0d70c6e",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0019180",
        "target_id": "HGNC:1078",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10095688632320676
      },
      {
        "type": "literature_co-occurrence",
        "id": "863f1854-f622-4af0-95fd-788944c74c5e",
        "num_publications": 22,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002462",
        "target_id": "HGNC:12796",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10065737063889857
      },
      {
        "type": "literature_co-occurrence",
        "id": "feb06eb5-4633-4e26-86fa-c1db4bfb7de9",
        "num_publications": 130,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:2367",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10294737779528351
      },
      {
        "type": "literature_co-occurrence",
        "id": "292929d4-d75e-4e8d-9516-d5b73215bfde",
        "num_publications": 24,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005825",
        "target_id": "HGNC:11848",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10085558194602728
      },
      {
        "type": "literature_co-occurrence",
        "id": "bcb4fb0f-9c1c-4842-a70f-108dbe7b09c6",
        "num_publications": 31,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0006277",
        "target_id": "HGNC:12362",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10123932879748399
      },
      {
        "type": "literature_co-occurrence",
        "id": "b91a35db-8671-48f8-970a-8037a1c9184a",
        "num_publications": 2,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:3657",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      },
      {
        "type": "literature_co-occurrence",
        "id": "074ab227-dc19-4347-9114-988a9bac4664",
        "num_publications": 21,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0002462",
        "target_id": "HGNC:399",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10067541904119481
      },
      {
        "type": "literature_co-occurrence",
        "id": "249a7005-ca27-49e1-b1bd-0ec45c072e4a",
        "num_publications": 59,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0005160",
        "target_id": "HGNC:11772",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.10233221509107315
      },
      {
        "type": "literature_co-occurrence",
        "id": "8e7449b4-ae11-4a2c-85eb-dc8dc0dd1e00",
        "num_publications": 9,
        "publications": [],
        "source_database": "omnicorp",
        "source_id": "MONDO:0018076",
        "target_id": "HGNC:399",
        "edge_source": "omnicorp.term_to_term",
        "weight": 0.09999999999999998
      }
    ]
  },
  "answers": [
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004670",
        "n3": "HGNC:11365"
      },
      "edge_bindings": {
        "e0": [
          "2867546"
        ],
        "e1": [
          "7927309",
          "7927871"
        ],
        "s105": "1be65edb-c074-41d5-90a6-73e6454b33ec",
        "s26262": "46185e64-99d1-405b-a5ce-4f0f6500f4f7"
      },
      "score": 0.617303007598795
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004670",
        "n3": "HGNC:12269"
      },
      "edge_bindings": {
        "e0": [
          "2867546"
        ],
        "e1": [
          "7927304",
          "2662659",
          "7927194",
          "7927307"
        ],
        "s105": "1be65edb-c074-41d5-90a6-73e6454b33ec",
        "s29779": "eeab134e-8992-4db2-b9d7-d172f7a5ac8c"
      },
      "score": 0.5770616878278981
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:1884"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2748009"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s4247": "e240213a-915c-4eee-9e05-0e1d45dbfd55",
        "s19547": "7f3e75ba-2cb4-41e6-af99-499e99de2fb9"
      },
      "score": 0.5516617531987208
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:3236"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4182474"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s1546": "e8074d52-9b40-404f-a038-67e504171729",
        "s37185": "67240bb3-d838-4f72-8739-13e167a46b8b"
      },
      "score": 0.5409070455937589
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004670",
        "n3": "HGNC:4942"
      },
      "edge_bindings": {
        "e0": [
          "2867546"
        ],
        "e1": [
          "7928757",
          "7928980"
        ],
        "s105": "1be65edb-c074-41d5-90a6-73e6454b33ec",
        "s70135": "09e8567b-7417-4604-9b94-436aedfeb1ba"
      },
      "score": 0.5398339177302737
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:317"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678987"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s619": "fe06ce36-5fce-4e25-81fc-fc456a50f807",
        "s43908": "52e2545a-e864-4e4d-83b4-f7f8273ae11a"
      },
      "score": 0.5105424076193379
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019065",
        "n3": "HGNC:620"
      },
      "edge_bindings": {
        "e0": [
          "1820665",
          "3815301"
        ],
        "e1": [
          "4217625"
        ],
        "s1604": "9356e5cd-14f2-4cff-8f2c-be5801d075a2",
        "s62926": "f5812967-7bec-4a10-a089-995988872fb5"
      },
      "score": 0.48831851456409836
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:3765"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256063"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s23228": "4da67aa5-6ab9-48f8-a7aa-0c78cbdd808d",
        "s27378": "4547b505-3a9c-40de-9198-5cf293650f2f"
      },
      "score": 0.4494307774102687
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:12388"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222701"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s3450": "808635f5-7cbb-4d68-b4a6-88b5b069eb7d",
        "s48530": "9ac01071-2fc4-4638-a7eb-483a8794ed1c"
      },
      "score": 0.44492265846258877
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:20387"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183052"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s30506": "aa96dace-92ac-4dd9-8e8e-a30475cda44f",
        "s40838": "215bcbf1-42c7-427a-b544-8fa9b4e3daad"
      },
      "score": 0.4426412574031274
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:427"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4181676"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s2960": "89084498-ab21-459a-acb4-fa60f065d7fc",
        "s29032": "f1626e97-3586-4535-9eea-381afb9f34b3"
      },
      "score": 0.43265203126492985
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019065",
        "n3": "HGNC:12405"
      },
      "edge_bindings": {
        "e0": [
          "1820665",
          "3815301"
        ],
        "e1": [
          "4217717"
        ],
        "s1443": "c3e21e5d-20e3-43a4-ba67-51df39a2072f",
        "s1604": "9356e5cd-14f2-4cff-8f2c-be5801d075a2",
        "s62196": "d88676fb-2ea5-4d64-bcd6-8ae40f8966e9"
      },
      "score": 0.42847229846856544
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:6407"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183981"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s4138": "d8924caf-d2b0-4839-b1b6-62bc33edfa5e",
        "s72456": "bc78a8d5-f4c3-4bfb-8e43-fe9c7f2ba548"
      },
      "score": 0.4276288360626799
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019121",
        "n3": "HGNC:1678"
      },
      "edge_bindings": {
        "e0": [
          "1820739",
          "3928858"
        ],
        "e1": [
          "4222647"
        ],
        "s293": "4d114400-db1b-4b00-9d51-b33cce932faf",
        "s8753": "bc79686a-b5ae-441b-a145-f6f7f935725f",
        "s44478": "533a819b-cbec-4e22-bc13-50724660c9ee"
      },
      "score": 0.4258765337440446
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:7029"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183318"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s549": "9c93a4b8-4884-41ef-8463-3d977325aef8",
        "s30313": "95a4a14d-804b-4781-acf3-9ec3c9dc51e4"
      },
      "score": 0.42012593555279654
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:1659"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4255834"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s27810": "5eea36f8-be38-4582-96a3-dd3eb0a97ad1",
        "s72412": "4af5995a-8115-4a18-9f6f-6ada9e11bfd9"
      },
      "score": 0.41865835139067237
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005974",
        "n3": "HGNC:27004"
      },
      "edge_bindings": {
        "e0": [
          "1820749",
          "2865645"
        ],
        "e1": [
          "2624085"
        ],
        "s13716": "246cf859-1443-4825-9e3f-c42cda25577e",
        "s13717": "6666e7cd-cfd2-47f1-acff-e3afa674a04f",
        "s13718": "c19179ec-922c-4a6c-80b2-00cef30fa5d2"
      },
      "score": 0.41674700613051857
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:27004"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2753212"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s13717": "6666e7cd-cfd2-47f1-acff-e3afa674a04f",
        "s46066": "ef87d609-7495-4c76-861e-fc18cbd1f73c"
      },
      "score": 0.4163851867326553
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:27004"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4184208"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s13717": "6666e7cd-cfd2-47f1-acff-e3afa674a04f",
        "s59463": "d84f5de2-d7de-4445-a5f2-f084c4a15fd1"
      },
      "score": 0.41605710129005663
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007915",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820716",
          "2984965",
          "2984206"
        ],
        "e1": [
          "2667402"
        ],
        "s707": "04a65677-6c89-4927-983e-14843f0e0527",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s60148": "4160dcd6-b360-460a-9b7b-b8b774a0545f"
      },
      "score": 0.4158949634719011
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:1884"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186964"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s4247": "e240213a-915c-4eee-9e05-0e1d45dbfd55",
        "s78014": "23d3d210-5444-4f2f-8f5b-52692643bb6f"
      },
      "score": 0.4147361992447435
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019338",
        "n3": "HGNC:2707"
      },
      "edge_bindings": {
        "e0": [
          "1820699",
          "4051191"
        ],
        "e1": [
          "4252547"
        ],
        "s98": "25824f35-1ee1-494d-bd75-0b61c167fb52",
        "s2553": "11f5bc12-4ca0-41fd-8542-0676c5acdb39",
        "s44264": "ab69f6c4-ea20-494c-9195-e2ada5957fc3"
      },
      "score": 0.4132408866291719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019065",
        "n3": "HGNC:108"
      },
      "edge_bindings": {
        "e0": [
          "1820665",
          "3815301"
        ],
        "e1": [
          "4217640"
        ],
        "s684": "1d468ded-ca12-49f1-b7b5-a8eff9acae3f",
        "s1604": "9356e5cd-14f2-4cff-8f2c-be5801d075a2",
        "s36718": "ab6a5a5c-c120-4153-8ed6-823cdd6eb25b"
      },
      "score": 0.41290993773590356
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007915",
        "n3": "HGNC:15633"
      },
      "edge_bindings": {
        "e0": [
          "1820716",
          "2984965",
          "2984206"
        ],
        "e1": [
          "2668558"
        ],
        "s707": "04a65677-6c89-4927-983e-14843f0e0527",
        "s10956": "cfcd27f5-6364-4809-8190-bc3cf60f700e",
        "s63183": "566660aa-6e93-4a48-9973-efe0179484e2"
      },
      "score": 0.41182377129705255
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:12796"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256729"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s6156": "6fe33571-68cb-41c7-af1c-77d8e329ac98",
        "s76306": "98eb7b9a-238f-4d50-a8d4-e7a2f9576bec"
      },
      "score": 0.41107998017007985
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:3236"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678939"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s1546": "e8074d52-9b40-404f-a038-67e504171729",
        "s78583": "3eb898ca-cf12-4a74-9991-0252c9307fbd"
      },
      "score": 0.4101225905397508
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222556"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s53013": "f13f202c-3f29-4d5a-8f95-51fc07a28a27"
      },
      "score": 0.4100684534829885
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007915",
        "n3": "HGNC:1318"
      },
      "edge_bindings": {
        "e0": [
          "1820716",
          "2984965",
          "2984206"
        ],
        "e1": [
          "2667369"
        ],
        "s637": "8d9fe083-0320-4a38-983e-2eaa1df3ba3d",
        "s707": "04a65677-6c89-4927-983e-14843f0e0527",
        "s11635": "e6026ec6-200c-4314-9311-6223b47be88c"
      },
      "score": 0.4093582088799686
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:11998"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679456"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s3238": "adca4ca6-33b5-4ca2-836f-e70407bc62a4",
        "s76572": "c7ca2c62-aff6-426d-83ab-46ef3fb1481b"
      },
      "score": 0.409167909413549
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:3942"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679411"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s9001": "b68de93e-7cab-4450-8065-c37d18b08d11",
        "s57816": "91093666-c719-4f63-b01f-88493c217c8e"
      },
      "score": 0.4090860569846031
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:1472"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2747055"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s18764": "ecbe7598-34ba-491c-b589-d66b6a900de2",
        "s72750": "be055a40-abb0-4299-b845-41945f3e208a"
      },
      "score": 0.4088387675640126
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:11998"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183709"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s3238": "adca4ca6-33b5-4ca2-836f-e70407bc62a4",
        "s35952": "456e452f-a810-4d5f-9d6b-6f9eadcec7fd"
      },
      "score": 0.4071456845499305
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007915",
        "n3": "HGNC:6018"
      },
      "edge_bindings": {
        "e0": [
          "1820716",
          "2984965",
          "2984206"
        ],
        "e1": [
          "2667768"
        ],
        "s707": "04a65677-6c89-4927-983e-14843f0e0527",
        "s1474": "b43d0e58-7c89-477f-91fd-3bcdf5cd4589",
        "s17575": "2d8449e5-8a74-41d8-b8b8-702e71b8077b"
      },
      "score": 0.4068140573449812
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005396",
        "n3": "HGNC:11773"
      },
      "edge_bindings": {
        "e0": [
          "1820633",
          "4090114",
          "4090108"
        ],
        "e1": [
          "4194851"
        ],
        "s1998": "b8032ded-cd9d-496e-baf1-dab21b8dd15c",
        "s3105": "9d75beb6-f2d8-4c2d-8af2-7346df36d0ff",
        "s31156": "1932a066-d3de-43a5-ab80-a9f10a173c3e"
      },
      "score": 0.406528007768216
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:11848"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222546"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s1253": "9ea2cbf1-63a4-49f7-9172-de14b016e5aa",
        "s66200": "f4a406a4-074f-45bd-a0e9-2c2ad4fd3554"
      },
      "score": 0.40636112566454746
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019180",
        "n3": "HGNC:3349"
      },
      "edge_bindings": {
        "e0": [
          "1820757",
          "3942179"
        ],
        "e1": [
          "4224304"
        ],
        "s3500": "32e568d6-fba8-4233-bde3-9b8e4a762911",
        "s18935": "fbe70775-422a-47af-8b34-a65f8f386c74",
        "s74366": "075909c0-78a3-4ea8-ac7b-5b785521010c"
      },
      "score": 0.4061868167125238
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:6342"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256775"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s2062": "7a40a3ac-cae3-4943-b9da-e8fe6e354ab8",
        "s9654": "d759e27a-9059-4338-b558-63822b7b8034"
      },
      "score": 0.40615917336517227
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005396",
        "n3": "HGNC:6769"
      },
      "edge_bindings": {
        "e0": [
          "1820633",
          "4090114",
          "4090108"
        ],
        "e1": [
          "4194846"
        ],
        "s575": "9ebc49cf-3a40-43d8-8ad8-98764d927578",
        "s1998": "b8032ded-cd9d-496e-baf1-dab21b8dd15c",
        "s26857": "def1d058-498a-44a5-b636-5f74264fbc0a"
      },
      "score": 0.4061155965692945
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005396",
        "n3": "HGNC:11772"
      },
      "edge_bindings": {
        "e0": [
          "1820633",
          "4090114",
          "4090108"
        ],
        "e1": [
          "4194849"
        ],
        "s177": "32376d24-7763-42e2-91b7-4141b85013d1",
        "s1998": "b8032ded-cd9d-496e-baf1-dab21b8dd15c",
        "s73803": "ac015958-b423-4c27-a96e-82f336af37fe"
      },
      "score": 0.40604599769385186
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007915",
        "n3": "HGNC:2956"
      },
      "edge_bindings": {
        "e0": [
          "1820716",
          "2984965",
          "2984206"
        ],
        "e1": [
          "2667472"
        ],
        "s707": "04a65677-6c89-4927-983e-14843f0e0527",
        "s3920": "cb2599a2-1d54-48fc-b37f-481e50d4f91c",
        "s70718": "4e18e231-ed54-4076-81ce-dc2d4d58f843"
      },
      "score": 0.4060296117087357
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007191",
        "n3": "HGNC:11920"
      },
      "edge_bindings": {
        "e0": [
          "1820684",
          "2939362",
          "2938947"
        ],
        "e1": [
          "2641077"
        ],
        "s2548": "d0c70c79-d4ea-4bcc-8e8f-a8608f34048e",
        "s5173": "9a0a1531-405b-4c5b-be3e-0a06aa40f8fd",
        "s22063": "e6d2f528-f8e9-4893-8939-697cdcd63ace"
      },
      "score": 0.40580100598193763
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:10261"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4184100"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s22004": "7ca38e7e-4a3c-42d3-98f1-b38803054eb0",
        "s50318": "32c6ebe4-96f2-4b5d-8099-58b0e244b01a"
      },
      "score": 0.40569327037866404
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007191",
        "n3": "HGNC:11850"
      },
      "edge_bindings": {
        "e0": [
          "1820684",
          "2939362",
          "2938947"
        ],
        "e1": [
          "2641075"
        ],
        "s4159": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "s5173": "9a0a1531-405b-4c5b-be3e-0a06aa40f8fd",
        "s71940": "73f9b121-3e7d-4d6f-9f8b-051da7e2d6bc"
      },
      "score": 0.40561739221139975
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005396",
        "n3": "HGNC:7176"
      },
      "edge_bindings": {
        "e0": [
          "1820633",
          "4090114",
          "4090108"
        ],
        "e1": [
          "4194840"
        ],
        "s1998": "b8032ded-cd9d-496e-baf1-dab21b8dd15c",
        "s4686": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "s27789": "777fc308-370d-432e-bbe9-e647f7bba182"
      },
      "score": 0.40559772424660107
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005396",
        "n3": "HGNC:11768"
      },
      "edge_bindings": {
        "e0": [
          "1820633",
          "4090114",
          "4090108"
        ],
        "e1": [
          "4194848"
        ],
        "s1998": "b8032ded-cd9d-496e-baf1-dab21b8dd15c",
        "s7029": "f9d6e263-c4c2-4f08-83ef-d8d7508efee2",
        "s53660": "ba756d7c-9dbb-43aa-97a5-6954d346ba7b"
      },
      "score": 0.40552683484851776
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:3229"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2675343"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s22918": "0d910f59-7b57-4631-bc38-dc6af7d48ce8",
        "s49690": "42cd0d6a-053e-4433-a73c-8d7819c449b9"
      },
      "score": 0.4055067644662789
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007191",
        "n3": "HGNC:1516"
      },
      "edge_bindings": {
        "e0": [
          "1820684",
          "2939362",
          "2938947"
        ],
        "e1": [
          "2640976"
        ],
        "s4908": "a075d96a-b573-4ed5-8d06-e37c7ae073dc",
        "s5173": "9a0a1531-405b-4c5b-be3e-0a06aa40f8fd",
        "s10536": "ad7c10fc-0b80-4861-803e-b7f46799845d"
      },
      "score": 0.4052381894462826
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007915",
        "n3": "HGNC:1516"
      },
      "edge_bindings": {
        "e0": [
          "1820716",
          "2984965",
          "2984206"
        ],
        "e1": [
          "2667232"
        ],
        "s707": "04a65677-6c89-4927-983e-14843f0e0527",
        "s4908": "a075d96a-b573-4ed5-8d06-e37c7ae073dc",
        "s44805": "f8bf2d98-924c-4cb0-8a3e-110316269243"
      },
      "score": 0.4051498245086929
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019180",
        "n3": "HGNC:175"
      },
      "edge_bindings": {
        "e0": [
          "1820757",
          "3942179"
        ],
        "e1": [
          "4224300"
        ],
        "s3500": "32e568d6-fba8-4233-bde3-9b8e4a762911",
        "s29906": "b6167a85-cc76-45a0-9317-21f54d69aada",
        "s52964": "b2497bd7-1be0-4d98-9c52-78f34bc43d6c"
      },
      "score": 0.4048119068752943
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:2956"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2748882"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s3920": "cb2599a2-1d54-48fc-b37f-481e50d4f91c",
        "s4772": "4dfaee62-09f8-4af5-bc6d-10db49ac5921"
      },
      "score": 0.40454180162166237
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:9208"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221551"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s8724": "357f945d-bb26-4d9a-ac49-05e3c02d8812",
        "s8725": "b8741672-8ce3-4de1-a457-0a38eedb6f06"
      },
      "score": 0.40451780594557735
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:7218"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187053"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s4707": "46c297af-8f47-4d1d-9f86-06e60a2a2f72",
        "s42899": "a96964d0-e071-4e76-9428-e34da2031cfd"
      },
      "score": 0.40390708988181295
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:2707"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186928"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s2553": "11f5bc12-4ca0-41fd-8542-0676c5acdb39",
        "s29701": "3e5ccb53-09e0-4c2d-a5c6-da81a576106d"
      },
      "score": 0.40375673932611417
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:11920"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256643"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s2548": "d0c70c79-d4ea-4bcc-8e8f-a8608f34048e",
        "s57407": "4cb983e4-1598-4cc7-8f96-0fec5e1985ef"
      },
      "score": 0.40353100928082536
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005149",
        "n3": "HGNC:1078"
      },
      "edge_bindings": {
        "e0": [
          "1820671",
          "3717678"
        ],
        "e1": [
          "4175032"
        ],
        "s662": "9873d8a9-a400-4a74-b25f-9afaf699254f",
        "s6772": "4e813b42-dc60-40c5-be59-1526f44dcecb",
        "s19884": "91c29a06-7bbd-4d6f-b9c1-66091857dd85"
      },
      "score": 0.4031507209445911
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:12680"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678135"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s5414": "73126933-ec74-4a10-adbc-07a344d2b5cd",
        "s17275": "8fdc8ea6-302b-4694-816c-d1169710a5b7"
      },
      "score": 0.4030848374987433
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004822",
        "n3": "HGNC:1884"
      },
      "edge_bindings": {
        "e0": [
          "1820728",
          "2899034"
        ],
        "e1": [
          "2687686"
        ],
        "s1765": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "s4247": "e240213a-915c-4eee-9e05-0e1d45dbfd55",
        "s55601": "8c335ffb-0ac7-4449-92b2-ccc11a94d37f"
      },
      "score": 0.4030217965521293
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:6342"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183202"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s2062": "7a40a3ac-cae3-4943-b9da-e8fe6e354ab8",
        "s77220": "9328c5bf-9e3d-4fd7-97ae-5af57016b290"
      },
      "score": 0.4029416210663856
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679798"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s52489": "4da159d0-307e-4ae0-b0ae-df6dd6d04802"
      },
      "score": 0.4027186499499956
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:9689"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183911"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s18805": "ee03eab1-2eff-4753-a185-48b9956bae29",
        "s28548": "ff0919de-468c-4e8e-9d7c-3289bcb986d7"
      },
      "score": 0.4026942321097344
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:1773"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678843"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s14007": "e9bad44b-25d2-4da8-b558-a710a4fe89aa",
        "s14416": "2660e5b9-ab35-4a40-b260-78fa5aadde56"
      },
      "score": 0.40263474030770774
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:7176"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679373"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s4686": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "s70220": "3fad7f1e-e606-41c4-9be7-3db80f1b696b"
      },
      "score": 0.4026119105829973
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:7989"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256440"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s12973": "90b76a43-05da-4d2f-8c35-0d44215a3a1f",
        "s61207": "ffd25be4-d433-4d48-93dc-e22e167c60f2"
      },
      "score": 0.4025745581402516
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187087"
        ],
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s22056": "636f790a-dae4-4f8e-836e-16fc7cd708b7"
      },
      "score": 0.4025457204540946
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:6973"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2676692"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s936": "a7d23f2a-de44-40e7-abac-2b9f93627714",
        "s29691": "5431b21d-fa5e-459d-9d3a-3a6e64375807"
      },
      "score": 0.40252888668381165
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:1678"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186955"
        ],
        "s293": "4d114400-db1b-4b00-9d51-b33cce932faf",
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s38194": "5cde924e-e871-4ad1-8a47-9cb59b6e1907"
      },
      "score": 0.4024787661297998
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:5438"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221134"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s2252": "d1981f79-da4d-4852-885d-5a4e3b9491b4",
        "s34038": "14c1e53c-ff44-49d1-8f90-1a400167e573"
      },
      "score": 0.4023006755972297
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0012105",
        "n3": "HGNC:7218"
      },
      "edge_bindings": {
        "e0": [
          "1820746",
          "3123106"
        ],
        "e1": [
          "4200726"
        ],
        "s1527": "d4ae3940-5df2-48ff-bce6-92bc59787c01",
        "s4707": "46c297af-8f47-4d1d-9f86-06e60a2a2f72",
        "s22003": "5ec3bca7-d2d7-4e83-bc74-e705c9a0b824"
      },
      "score": 0.4022536787609528
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:12680"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4184723"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s5414": "73126933-ec74-4a10-adbc-07a344d2b5cd",
        "s65352": "b80be848-f2de-4f6a-899d-1cc760625ad5"
      },
      "score": 0.4022086340906645
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:6342"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221295"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s2062": "7a40a3ac-cae3-4943-b9da-e8fe6e354ab8",
        "s75838": "3f34ee0f-452b-4c04-b83c-dd6fdf34973b"
      },
      "score": 0.40211651780693275
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:17941"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2752298"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s11923": "e8dbd5c1-ae32-4771-9ab5-a1f119674473",
        "s45067": "a543b153-56ef-4061-8e58-df45aa8332bf"
      },
      "score": 0.40205822068938996
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:4603"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186974"
        ],
        "s452": "e805f860-28b7-4f5b-826a-166202064858",
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s55080": "34d15b30-b0b6-49c9-903a-e59f8bfe624f"
      },
      "score": 0.4020417281871057
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:7176"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175628"
        ],
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s4686": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "s59527": "4a0c9d21-e16d-4f07-b9dd-ea09963b35dd"
      },
      "score": 0.4020206282028645
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005149",
        "n3": "HGNC:7876"
      },
      "edge_bindings": {
        "e0": [
          "1820671",
          "3717678"
        ],
        "e1": [
          "4175070"
        ],
        "s481": "965adb3b-749e-4b1e-b8d6-371bd2e62361",
        "s662": "9873d8a9-a400-4a74-b25f-9afaf699254f",
        "s8257": "b6d040c9-7aeb-40d1-bd7e-8bd521274dea"
      },
      "score": 0.401819065034918
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:11925"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2677846"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s345": "b63e4788-a139-4886-bfcc-5cbc9bbc347c",
        "s77235": "df4456ba-3911-46d2-bd4b-01971e806944"
      },
      "score": 0.40180035846656503
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:259"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2674411"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s1508": "6b9d3347-f486-4e4a-a603-56eaa4b4e710",
        "s21843": "8edb6baf-97bf-4ffa-ad69-8abe5c7aa5ed"
      },
      "score": 0.40177760482754293
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:9273"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187056"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s2289": "fbe16108-7e95-48f7-b0ad-6cd0622d35ea",
        "s61311": "90a6ba3d-9e8a-4a2c-afaa-b445d105204d"
      },
      "score": 0.40169634747193095
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019065",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820665",
          "3815301"
        ],
        "e1": [
          "4217677"
        ],
        "s1604": "9356e5cd-14f2-4cff-8f2c-be5801d075a2",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s63770": "6b8f8b25-45f3-4401-a243-0285f8509b69"
      },
      "score": 0.40167401977202477
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:583"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678638"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s5947": "cd8dd063-0ec7-4c9e-8fc2-32a6d37f66f4",
        "s52180": "c42229b8-520c-4d2d-ab17-c744941cee94"
      },
      "score": 0.4016671681734545
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:1050"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678712"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s22239": "6a428009-bf33-47c3-8a00-2a9584073f2c",
        "s22240": "00245fe3-b418-4e40-bf01-5e45b735f557"
      },
      "score": 0.40166401537604063
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:12679"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222793"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s6489": "6a662190-a7f1-4a93-9a80-e3e9fcfe6573",
        "s71113": "96dee345-0b9b-4e28-b7ed-1a0afd7b80a9"
      },
      "score": 0.4016392988855903
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220622"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s5576": "42710e03-1759-49e4-87d9-dde68c8aab08"
      },
      "score": 0.40155298273757234
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:2956"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186979"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s3920": "cb2599a2-1d54-48fc-b37f-481e50d4f91c",
        "s3921": "85d3afca-dc0f-447c-9965-b6a3ca1d55cb"
      },
      "score": 0.4014148617392316
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:11573"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2674578"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s31541": "a193ff5e-5bd5-4178-87d3-01336434cfa5",
        "s31542": "6bcd63b2-8895-4eca-bb2f-b2c4cb821d89"
      },
      "score": 0.40138672872480574
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:1693"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186956"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s10201": "ccdc03ab-5e45-4fa6-bc18-2903d4410a29",
        "s48608": "a9c329d3-567f-420e-bb37-3c2660242c72"
      },
      "score": 0.4013205194749104
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:11825"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187044"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s10406": "3e663fd5-c703-455f-9b00-95431f7204fd",
        "s14026": "0dd171a3-04de-43db-a4be-ebf09a63c7b8"
      },
      "score": 0.4011826796422934
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:8729"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183760"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s11501": "e3d91d36-dc47-44c0-97bf-94fdd14e5cb4",
        "s62289": "8f29925a-21a2-4387-ace3-143657fd2c74"
      },
      "score": 0.40114260460867485
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:990"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4255784"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s5839": "edc74501-6cdc-499a-875a-21bdccb43f4b",
        "s69341": "3834ceab-f340-4595-b693-414ca3b954cd"
      },
      "score": 0.4011022758342389
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:6018"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679202"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s1474": "b43d0e58-7c89-477f-91fd-3bcdf5cd4589",
        "s56936": "23ad785a-853b-49ce-9539-917e945778ee"
      },
      "score": 0.4009677113977324
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1628"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220393"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s1856": "3d0a5950-d98c-43c2-88b8-cd770c874eab",
        "s66587": "2c31905b-d8ef-4a1e-99c3-ed6a63d46c8f"
      },
      "score": 0.40096246694060644
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:1634"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186954"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s4971": "655edf81-d3e2-41f8-b3f1-0fd92ff49367",
        "s26411": "c156621d-c2be-4850-9de3-9a038f3a88cc"
      },
      "score": 0.4009537154272802
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:7176"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183448"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s4686": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "s75521": "c6cd093a-fe4a-493d-a047-6e9ed725a0e3"
      },
      "score": 0.4009421583963208
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019338",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820699",
          "4051191"
        ],
        "e1": [
          "4253212"
        ],
        "s98": "25824f35-1ee1-494d-bd75-0b61c167fb52",
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s58529": "59b75b54-fbef-45a9-be68-e3b742a4765c"
      },
      "score": 0.4009367298443799
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:1662"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4182156"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s993": "1d897c9b-0d8c-40d5-827e-66df33cedc31",
        "s41155": "847b4dbc-b416-4a4c-9f6e-eaa0625bc13f"
      },
      "score": 0.40092378026300823
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002462",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820715",
          "3676714"
        ],
        "e1": [
          "2691482"
        ],
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s999": "a7f079d4-f475-4954-b656-92c8c2bcd1c0",
        "s31795": "1bb6a333-dc12-4ebd-aa49-375ab8d97484"
      },
      "score": 0.400901537785974
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019338",
        "n3": "HGNC:1678"
      },
      "edge_bindings": {
        "e0": [
          "1820699",
          "4051191"
        ],
        "e1": [
          "4252662"
        ],
        "s98": "25824f35-1ee1-494d-bd75-0b61c167fb52",
        "s293": "4d114400-db1b-4b00-9d51-b33cce932faf",
        "s37236": "8a0e0908-37c1-4d18-ae7e-3007c37dbb15"
      },
      "score": 0.40088063152248676
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175612"
        ],
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s79487": "feb06eb5-4633-4e26-86fa-c1db4bfb7de9"
      },
      "score": 0.4007918338087079
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:11850"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222503"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s4159": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "s69393": "e55cca82-bd37-4d6b-b69d-3f79db41b633"
      },
      "score": 0.40072616371659464
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:7515"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2751884"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s8841": "b7d8e996-6f84-4564-99cb-b50ca822ef6e",
        "s28972": "3ab300a9-48da-40b2-9989-0a15e7389507"
      },
      "score": 0.4006726762271211
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:6973"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183469"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s936": "a7d23f2a-de44-40e7-abac-2b9f93627714",
        "s21046": "64b32f6f-5a0a-4d72-a07b-9d2012800d13"
      },
      "score": 0.40066617388522235
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:11773"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175641"
        ],
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s3105": "9d75beb6-f2d8-4c2d-8af2-7346df36d0ff",
        "s77559": "4716c24a-6178-4eb9-a434-0e43da156703"
      },
      "score": 0.4006262250113498
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:175"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186923"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s29906": "b6167a85-cc76-45a0-9317-21f54d69aada",
        "s76536": "08e051f8-ad8c-46bb-b739-3c5f7df5b5de"
      },
      "score": 0.40061612067791746
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256642"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s71842": "0573b3cc-c0a8-4040-8480-724b92b3a3a4"
      },
      "score": 0.4005831739732605
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005149",
        "n3": "HGNC:2707"
      },
      "edge_bindings": {
        "e0": [
          "1820671",
          "3717678"
        ],
        "e1": [
          "4175021"
        ],
        "s662": "9873d8a9-a400-4a74-b25f-9afaf699254f",
        "s2553": "11f5bc12-4ca0-41fd-8542-0676c5acdb39",
        "s2554": "da5bce9a-85af-4442-869e-cb20669c00b8"
      },
      "score": 0.4005721573968833
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:6204"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2676198"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s9914": "695daf3a-5059-48be-9d57-5950f1ace359",
        "s15668": "ca6f9d74-aacf-423b-9d52-52eda69ad327"
      },
      "score": 0.4005184296473886
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:5438"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187003"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s2252": "d1981f79-da4d-4852-885d-5a4e3b9491b4",
        "s24537": "6eb7ac4f-9c71-44cc-9e8f-8f1275933688"
      },
      "score": 0.40051086313820006
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:3236"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186980"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s1546": "e8074d52-9b40-404f-a038-67e504171729",
        "s52009": "058e91c1-8c81-4cb4-902c-c4768ab5b216"
      },
      "score": 0.40050997811076916
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:15633"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222708"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s10956": "cfcd27f5-6364-4809-8190-bc3cf60f700e",
        "s42253": "98b72ee8-9daa-460b-bd54-7ead9a5f974d"
      },
      "score": 0.40049286588861144
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0017991",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820691",
          "3284226"
        ],
        "e1": [
          "4216339"
        ],
        "s1630": "10e1043c-53f0-4541-a2e0-5bd6722db771",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s69928": "d1ba65fd-38e5-4d01-a66a-94814e4612f0"
      },
      "score": 0.40045962866217355
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:3535"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187085"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s1295": "09cd9f4c-016c-49be-9063-e910cfc6f035",
        "s54185": "eb4c94a5-6803-4a21-ba51-aeaae5c11757"
      },
      "score": 0.40045587511343794
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:8803"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187057"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s3011": "b8371b6c-d7a8-440c-a40f-9096bab5a5f1",
        "s66990": "c9467ff3-42be-4ff0-afa0-5fd8033b89ad"
      },
      "score": 0.40043172828132156
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005279",
        "n3": "HGNC:7436"
      },
      "edge_bindings": {
        "e0": [
          "1820660",
          "3966551"
        ],
        "e1": [
          "4187291"
        ],
        "s4849": "044de512-efa6-4249-b6d3-5d569fea9574",
        "s5037": "07e8031f-da3f-4085-a05b-a7923d34ad30",
        "s41406": "f594a22f-1d77-4a3d-9d04-43fe1dd4578b"
      },
      "score": 0.40042472161345755
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:6204"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187015"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s9914": "695daf3a-5059-48be-9d57-5950f1ace359",
        "s18483": "caab29af-1337-495f-b191-91137344b224"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:1472"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4186936"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s18764": "ecbe7598-34ba-491c-b589-d66b6a900de2",
        "s18765": "00ac3850-75da-4437-b89d-0a105d3ef93d"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:6342"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187029"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s2062": "7a40a3ac-cae3-4943-b9da-e8fe6e354ab8",
        "s47523": "6fb30f27-f398-4ed6-90d1-225dd6dfb642"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:11998"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187051"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s3238": "adca4ca6-33b5-4ca2-836f-e70407bc62a4",
        "s52231": "ad41a7cf-286b-4be4-ae26-3e80ac64a95b"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:894"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187046"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s7875": "09bdf6cb-27a8-4f7d-a046-ec7f9821515a",
        "s59286": "0827515b-423a-4bc5-b6b9-9ae6e84a8d1b"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:12680"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187098"
        ],
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s5414": "73126933-ec74-4a10-adbc-07a344d2b5cd",
        "s74521": "dc461c01-9177-422b-8b7c-9a40eb638936"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005275",
        "n3": "HGNC:7876"
      },
      "edge_bindings": {
        "e0": [
          "1820697",
          "3959644"
        ],
        "e1": [
          "4187048"
        ],
        "s481": "965adb3b-749e-4b1e-b8d6-371bd2e62361",
        "s1216": "f4b4f7c0-911c-4519-9656-d042e7d0cddb",
        "s29962": "699df82b-7de8-4579-9aa5-e67bef82ce5f"
      },
      "score": 0.4004143948015457
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:1773"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4182162"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s14007": "e9bad44b-25d2-4da8-b558-a710a4fe89aa",
        "s73396": "cb2f567a-23c0-4871-a385-735fb7266dff"
      },
      "score": 0.4003734399832612
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:6407"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256426"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s4138": "d8924caf-d2b0-4839-b1b6-62bc33edfa5e",
        "s26059": "3146238d-dc22-4316-9e8d-91e9545392a4"
      },
      "score": 0.4003637698676202
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0011827",
        "n3": "HGNC:23506"
      },
      "edge_bindings": {
        "e0": [
          "1820745",
          "3098975"
        ],
        "e1": [
          "2748824"
        ],
        "s3332": "71340ade-a0cf-4b2d-b4d5-c47e7052104f",
        "s25152": "26068437-c5d8-4f2e-b504-18c1eac8f3b5",
        "s47259": "3813ed7e-82fb-42bc-9d97-03012aa8cdd4"
      },
      "score": 0.4003411563569673
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019180",
        "n3": "HGNC:6770"
      },
      "edge_bindings": {
        "e0": [
          "1820757",
          "3942179"
        ],
        "e1": [
          "4224308"
        ],
        "s3500": "32e568d6-fba8-4233-bde3-9b8e4a762911",
        "s7861": "1f1eec31-ca08-47ea-ae00-8f58e1d44e67",
        "s75996": "d11c752b-0b43-41a2-879d-27e4636826f5"
      },
      "score": 0.40017275230867616
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002363",
        "n3": "HGNC:11998"
      },
      "edge_bindings": {
        "e0": [
          "1820640",
          "3665783"
        ],
        "e1": [
          "2643885"
        ],
        "s2091": "6fbde79f-d983-4d62-b16a-97f23517bf98",
        "s3238": "adca4ca6-33b5-4ca2-836f-e70407bc62a4",
        "s59162": "95f0d351-c24d-4d28-89a2-be52b5166742"
      },
      "score": 0.40015381590130844
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:11920"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4184556"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s2548": "d0c70c79-d4ea-4bcc-8e8f-a8608f34048e",
        "s47284": "b0c8ca5f-fc49-42e4-9f57-4798ec0d55d1"
      },
      "score": 0.40014409403885726
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:11772"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175639"
        ],
        "s177": "32376d24-7763-42e2-91b7-4141b85013d1",
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s81015": "249a7005-ca27-49e1-b1bd-0ec45c072e4a"
      },
      "score": 0.40012181574285094
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002363",
        "n3": "HGNC:3236"
      },
      "edge_bindings": {
        "e0": [
          "1820640",
          "3665783"
        ],
        "e1": [
          "2643829"
        ],
        "s1546": "e8074d52-9b40-404f-a038-67e504171729",
        "s2091": "6fbde79f-d983-4d62-b16a-97f23517bf98",
        "s75137": "cc3c836c-bbf7-4026-9845-5d9bda57bb44"
      },
      "score": 0.4000570433713358
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:11825"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183562"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s10406": "3e663fd5-c703-455f-9b00-95431f7204fd",
        "s22822": "f442c0de-3752-4c85-8e16-2044b2e5c292"
      },
      "score": 0.400027078800707
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2748607"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s67802": "7a5e5f21-acce-4eab-b478-71b530e89e90"
      },
      "score": 0.39999189280184994
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:644"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678625"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s1950": "a5fec654-ade3-40b3-810f-859adce4db14",
        "s76223": "7191e9b8-356e-4b70-963d-ccf274f83efc"
      },
      "score": 0.39993997813124393
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:583"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4181797"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s5947": "cd8dd063-0ec7-4c9e-8fc2-32a6d37f66f4",
        "s45607": "123555ce-21d1-4673-a774-ffbf3673604b"
      },
      "score": 0.39990897023603994
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005657",
        "n3": "HGNC:11848"
      },
      "edge_bindings": {
        "e0": [
          "1820724",
          "3177611"
        ],
        "e1": [
          "2640318"
        ],
        "s1253": "9ea2cbf1-63a4-49f7-9172-de14b016e5aa",
        "s5600": "a3888560-692c-4833-8a88-125e0d36be4d",
        "s8845": "7e8fb0e1-9a86-4d16-9b83-0c3753c5b895"
      },
      "score": 0.39984643063556663
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:7218"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2752427"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s4707": "46c297af-8f47-4d1d-9f86-06e60a2a2f72",
        "s35447": "99d6270a-9796-4855-b3d1-7c8aa06942d2"
      },
      "score": 0.39983396155579115
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005657",
        "n3": "HGNC:1884"
      },
      "edge_bindings": {
        "e0": [
          "1820724",
          "3177611"
        ],
        "e1": [
          "2640275"
        ],
        "s4247": "e240213a-915c-4eee-9e05-0e1d45dbfd55",
        "s5600": "a3888560-692c-4833-8a88-125e0d36be4d",
        "s69345": "5b245966-a28b-4377-98d7-4531335aa201"
      },
      "score": 0.3998100694688417
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0003781",
        "n3": "HGNC:1884"
      },
      "edge_bindings": {
        "e0": [
          "1820630",
          "2801990"
        ],
        "e1": [
          "2582031"
        ],
        "s4247": "e240213a-915c-4eee-9e05-0e1d45dbfd55",
        "s12865": "0ec14d0b-aaa0-4d4f-842c-8ca710a6a79f",
        "s46912": "e8aee3d6-ebc7-4c7b-b378-350f24f0113a"
      },
      "score": 0.399783573548509
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0006932",
        "n3": "HGNC:1516"
      },
      "edge_bindings": {
        "e0": [
          "1820666",
          "2980256"
        ],
        "e1": [
          "2671406"
        ],
        "s480": "c2db85d2-4c2a-4c8e-9788-e8e65e657060",
        "s4908": "a075d96a-b573-4ed5-8d06-e37c7ae073dc",
        "s47786": "d56e7cdf-4a5a-4ef5-b85f-e17cdb2a8980"
      },
      "score": 0.3997768557061035
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1631"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220154"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s612": "d7d9bb39-7ad7-4e46-afeb-f907b34c11a2",
        "s71110": "cec2d31d-abba-49a9-a00d-ca633907555e"
      },
      "score": 0.3997359715600533
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0006932",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820666",
          "2980256"
        ],
        "e1": [
          "2671506"
        ],
        "s480": "c2db85d2-4c2a-4c8e-9788-e8e65e657060",
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s525": "fcf9e79a-e20b-4a04-952c-66626af73791"
      },
      "score": 0.399723854550266
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004822",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820728",
          "2899034"
        ],
        "e1": [
          "2687690"
        ],
        "s1765": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s36441": "6548a938-10b8-4199-ac43-2144d468b993"
      },
      "score": 0.3997207060424234
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:648"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4181725"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s32012": "88e3c734-8b9b-469e-86d6-8a63a59926cb",
        "s63862": "ae32f692-47f9-49ab-af60-7ef06c7ca776"
      },
      "score": 0.39971031420896197
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:7029"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679307"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s549": "9c93a4b8-4884-41ef-8463-3d977325aef8",
        "s20772": "a502287b-7a86-4d3d-a0c0-907ea8f587c5"
      },
      "score": 0.3996964211817399
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0001243",
        "n3": "HGNC:1366"
      },
      "edge_bindings": {
        "e0": [
          "1820638",
          "2923197"
        ],
        "e1": [
          "2621562"
        ],
        "s792": "dda1ef5a-7786-4be5-bba5-a77634ef19a6",
        "s793": "3553716c-487d-4609-9a6c-2802ab88ef22",
        "s794": "9350b4b2-542e-455f-953c-2271a1d83eea"
      },
      "score": 0.3996888190765844
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005657",
        "n3": "HGNC:11850"
      },
      "edge_bindings": {
        "e0": [
          "1820724",
          "3177611"
        ],
        "e1": [
          "2640317"
        ],
        "s4159": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "s5600": "a3888560-692c-4833-8a88-125e0d36be4d",
        "s57441": "cfdd064e-19de-4d15-9167-1fd2af435fdd"
      },
      "score": 0.3996790347139908
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:6935"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2748586"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s15717": "1a67f7c6-c9ca-4387-a754-c08e8ae7acbd",
        "s28453": "e6ef7a6b-a309-41e7-bba1-38b366e73961"
      },
      "score": 0.39967433384213036
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005812",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820737",
          "3203776"
        ],
        "e1": [
          "2653990"
        ],
        "s854": "39790313-d958-40f8-8314-3966274b2777",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s27255": "bcd1cbd7-da62-4015-ae8a-2915d4987991"
      },
      "score": 0.3996738568025174
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:11850"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2677772"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s4159": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "s51808": "78e4e770-2712-4f0d-adbe-3264e70f0280"
      },
      "score": 0.39967286104492455
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019065",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820665",
          "3815301"
        ],
        "e1": [
          "4217711"
        ],
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s1604": "9356e5cd-14f2-4cff-8f2c-be5801d075a2",
        "s69909": "b76f8fab-dea9-4505-bf1f-68b007f52b4a"
      },
      "score": 0.39966614130686456
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:6769"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175637"
        ],
        "s575": "9ebc49cf-3a40-43d8-8ad8-98764d927578",
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s48622": "35fe2ba4-1319-4cbd-9d18-4897b923fcfc"
      },
      "score": 0.39966320686833684
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:4603"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220601"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s452": "e805f860-28b7-4f5b-826a-166202064858",
        "s14705": "a82af5d4-ea60-4097-9e4d-c62e1ef72a66"
      },
      "score": 0.399656354286655
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0003781",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820630",
          "2801990"
        ],
        "e1": [
          "2582040"
        ],
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s12865": "0ec14d0b-aaa0-4d4f-842c-8ca710a6a79f",
        "s51455": "9f1f3436-6cb3-482f-84ea-cd7672bb05de"
      },
      "score": 0.3996520657549922
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018667",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820761",
          "3366092"
        ],
        "e1": [
          "4224250"
        ],
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s10947": "6553dde3-90e6-442a-9249-99a5e6f0f933",
        "s76314": "886d9ab3-431b-4b00-a312-7c4f46bfc59b"
      },
      "score": 0.39964918918037245
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:16781"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221676"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s16278": "7ee09dc5-e449-4836-baae-10eed1240ae7",
        "s16279": "29c299f0-fe55-4984-adb4-fc3d6f446342"
      },
      "score": 0.3996414955417823
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:3657"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220874"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s21034": "a3820c04-2130-4bf3-870b-e7c9bcd14d4c",
        "s80481": "b91a35db-8671-48f8-970a-8037a1c9184a"
      },
      "score": 0.39963842029022545
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:3349"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220758"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s18935": "fbe70775-422a-47af-8b34-a65f8f386c74",
        "s23173": "1e08325e-1eee-4a81-af33-6508637c0a5f"
      },
      "score": 0.3996370836182359
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1698"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220414"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s1605": "eaaa2aa5-41a7-4229-b893-e87f62086030",
        "s77318": "9bb4e880-984e-4396-ad31-3afb5f976392"
      },
      "score": 0.3996370159583918
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1331"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220516"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s1793": "0689bf34-29ae-4ab5-b6ee-c8e0419c0c33",
        "s12369": "89d37a96-83f1-4b99-826d-4a49543eefad"
      },
      "score": 0.39963410266289967
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1050"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220100"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s22239": "6a428009-bf33-47c3-8a00-2a9584073f2c",
        "s40829": "6dea9a51-e684-4e73-acdd-a14a419d7cd1"
      },
      "score": 0.39963325122121185
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:6407"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679590"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s4138": "d8924caf-d2b0-4839-b1b6-62bc33edfa5e",
        "s70216": "ac3c92b4-8686-4493-bd04-425253d1a665"
      },
      "score": 0.3996308917411182
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:7531"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221518"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s10892": "9bc5f308-bece-44e7-b366-128a3a0c199b",
        "s29352": "4850066a-5417-40b7-9bd2-573cf5c14f2b"
      },
      "score": 0.39962868330676765
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1695"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220438"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s4111": "307a3370-b219-4a6b-89a9-d80ceb9c6c30",
        "s5091": "6e29de85-dea0-49b5-917e-9c4177033f28"
      },
      "score": 0.3996276182309957
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:9864"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221966"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s14625": "b6c5b7e7-6c1a-4b84-9424-f12ed831022a",
        "s14626": "3fcc313c-1771-4e98-8a2b-282b23f3f086"
      },
      "score": 0.3996222302006206
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1659"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220299"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s27810": "5eea36f8-be38-4582-96a3-dd3eb0a97ad1",
        "s77049": "f8268d97-3624-4c9d-93d7-f311d16fc9b4"
      },
      "score": 0.3996202566778664
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:8636"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183908"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s23714": "024d40f3-5c3d-49dd-a74e-47c9dd3ca3c5",
        "s46112": "1cf4d951-b27d-494f-a7ff-3512eb34f91e"
      },
      "score": 0.3996193223547458
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:15990"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221005"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s38391": "5c800fcc-a4b7-4db7-8d22-ad57878df856",
        "s38398": "10125de2-f8e5-4991-9c8a-0e50eb97aecd"
      },
      "score": 0.39961566745431965
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:6204"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221169"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s9914": "695daf3a-5059-48be-9d57-5950f1ace359",
        "s9915": "af5beb5c-96a1-4444-8c0e-88bf41d8d027"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:4057"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220903"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s14572": "efb36668-168b-423f-adbf-4e1cf3e3fe71",
        "s14573": "b23530e0-3e0a-47d2-a1a6-1dbf5f5bfe8f"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:12680"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222772"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s5414": "73126933-ec74-4a10-adbc-07a344d2b5cd",
        "s15753": "b72bbe3a-7c9a-4d81-a0ac-c48951ca1fc6"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:7176"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221495"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s4686": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "s17704": "fda92bc4-df81-4618-8681-e96d6b552764"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:6018"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221138"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s1474": "b43d0e58-7c89-477f-91fd-3bcdf5cd4589",
        "s20505": "06138187-242b-4e0b-8290-a0c4a3126d77"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1097"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220149"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s4742": "3c25f748-71f9-482f-b50e-b01f76b928fe",
        "s21057": "61ccb8c7-112d-4137-b3e1-c5c52fee3f28"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:4837"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220294"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s17480": "9b140846-32e1-4574-b655-796b7ac54f75",
        "s21711": "a379968c-b3a1-48a9-8923-69ba8c3e16c9"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:2637"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220499"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s11619": "24171e4f-6ff7-45cd-80a8-cb51fbe99830",
        "s28063": "7aee237f-5d23-49ad-9f5d-d6733574ff03"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1516"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220277"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s4908": "a075d96a-b573-4ed5-8d06-e37c7ae073dc",
        "s28629": "9d99e913-aeed-4c87-b76c-2342b197684f"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:11183"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222362"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s17071": "dc3b26b4-c084-4993-b206-e2a5152fe227",
        "s28636": "dc8b39a3-0510-43a4-98a6-adb7ade127e8"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:20387"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221163"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s30506": "aa96dace-92ac-4dd9-8e8e-a30475cda44f",
        "s30507": "4bf86012-8190-4e95-8a56-75f90a64a254"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:10896"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222272"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s11514": "28d37fbf-2bfe-4c58-9499-ee8ded0728e4",
        "s33175": "c29174d4-6925-4e3a-91cc-8b1d767d5804"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:7321"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221517"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s24139": "4f9c539c-46c6-403b-b74a-89eef6b41dc5",
        "s38656": "1cf325ff-ff6e-4150-87b9-7ebb4c80e8c0"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:12796"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222803"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s6156": "6fe33571-68cb-41c7-af1c-77d8e329ac98",
        "s42261": "051059d7-911a-4480-bcdf-28d6bc43fee3"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:990"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220097"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s5839": "edc74501-6cdc-499a-875a-21bdccb43f4b",
        "s49788": "6f784abd-54c9-4b5e-a1e0-0f3c388ef06e"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:2707"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4219962"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s2553": "11f5bc12-4ca0-41fd-8542-0676c5acdb39",
        "s53818": "0045a810-b19a-45a9-aeef-cf5f34f7e304"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:6769"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222386"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s575": "9ebc49cf-3a40-43d8-8ad8-98764d927578",
        "s56811": "ba61fe3b-3092-455b-8a0a-a24710e992e3"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:12651"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222431"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s7945": "98bf3607-9d01-439e-b8b6-334b0c6cd3f1",
        "s58821": "fb9b8bd5-feae-49b3-b25a-9de63d92afd5"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:4234"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220961"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s17163": "a03c35db-4b8c-4d1d-a67b-419afc4ff85c",
        "s63898": "f43f7ee8-d9a6-4f26-908d-fc9b79e1e0fd"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:7029"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4221380"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s549": "9c93a4b8-4884-41ef-8463-3d977325aef8",
        "s64965": "586e3522-6308-4ac3-95f6-6b314d87ca4c"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1318"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220555"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s637": "8d9fe083-0320-4a38-983e-2eaa1df3ba3d",
        "s66751": "9cfe97f6-3083-4c8a-8f84-2ff1e7a00ea6"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:3765"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220881"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s23228": "4da67aa5-6ab9-48f8-a7aa-0c78cbdd808d",
        "s67784": "972b4b0f-233e-4e79-96ed-b17ae9cc821d"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:11925"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4222554"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s345": "b63e4788-a139-4886-bfcc-5cbc9bbc347c",
        "s76913": "cd1faca0-1553-4217-96bd-87bf6f7d1105"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:1472"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4220161"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s18764": "ecbe7598-34ba-491c-b589-d66b6a900de2",
        "s77244": "326d6798-6d22-42e5-84d6-57c09fa89fe1"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018076",
        "n3": "HGNC:399"
      },
      "edge_bindings": {
        "e0": [
          "1820676",
          "3306367"
        ],
        "e1": [
          "4219976"
        ],
        "s12": "7f1088be-34c6-43af-a4d1-414b550ebb87",
        "s1015": "35075ee5-4215-43cb-922c-409ed452d486",
        "s81271": "8e7449b4-ae11-4a2c-85eb-dc8dc0dd1e00"
      },
      "score": 0.3996135269671719
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:1693"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175609"
        ],
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s10201": "ccdc03ab-5e45-4fa6-bc18-2903d4410a29",
        "s31135": "0fb7650b-b4ba-415b-936c-8cab9f45cbef"
      },
      "score": 0.3995707383894134
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:2201"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175610"
        ],
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s3472": "a60558b0-f6c8-42a1-9ddc-2bea0a1980b5",
        "s51728": "dd56164a-4d26-494a-8fdc-c0f164f0f694"
      },
      "score": 0.3995212578892479
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678916"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s44028": "a2aa7bb2-ff09-41b6-b8d4-293ac9712d7c"
      },
      "score": 0.39951077813183367
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0003781",
        "n3": "HGNC:7515"
      },
      "edge_bindings": {
        "e0": [
          "1820630",
          "2801990"
        ],
        "e1": [
          "2582109"
        ],
        "s8841": "b7d8e996-6f84-4564-99cb-b50ca822ef6e",
        "s12865": "0ec14d0b-aaa0-4d4f-842c-8ca710a6a79f",
        "s45653": "22ecb0af-90d1-4c5a-90b6-ffb6ad015265"
      },
      "score": 0.3994961738256346
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019338",
        "n3": "HGNC:1693"
      },
      "edge_bindings": {
        "e0": [
          "1820699",
          "4051191"
        ],
        "e1": [
          "4252664"
        ],
        "s98": "25824f35-1ee1-494d-bd75-0b61c167fb52",
        "s10201": "ccdc03ab-5e45-4fa6-bc18-2903d4410a29",
        "s65774": "8cdaec86-1fee-4aa2-b314-4cb8a90b889c"
      },
      "score": 0.3994804649621231
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:5173"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2679579"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s5212": "d1987fd3-c29f-4a52-afce-abdf2d164952",
        "s6052": "d188e62c-e201-4b32-b3e4-43fc77b49915"
      },
      "score": 0.39945165902668506
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005149",
        "n3": "HGNC:175"
      },
      "edge_bindings": {
        "e0": [
          "1820671",
          "3717678"
        ],
        "e1": [
          "4175020"
        ],
        "s662": "9873d8a9-a400-4a74-b25f-9afaf699254f",
        "s29906": "b6167a85-cc76-45a0-9317-21f54d69aada",
        "s62144": "8c4d68d7-aa7d-45ce-94bb-a9b388bdf62c"
      },
      "score": 0.399449987529647
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:23506"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2746157"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s25152": "26068437-c5d8-4f2e-b504-18c1eac8f3b5",
        "s25153": "8763d51e-cb5f-40ac-9be5-4002e683008f"
      },
      "score": 0.3994241375986137
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0006277",
        "n3": "HGNC:12363"
      },
      "edge_bindings": {
        "e0": [
          "1820735",
          "2941808"
        ],
        "e1": [
          "2651610"
        ],
        "s944": "b38e7a56-a562-4282-9cd3-38a1d9e5adec",
        "s1307": "cdb535f8-867b-48d5-bb8d-949b21fc4247",
        "s34220": "cf7279cd-37df-42ac-84d2-13ba7e2423c0"
      },
      "score": 0.39941475484645705
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002076",
        "n3": "HGNC:2201"
      },
      "edge_bindings": {
        "e0": [
          "1820669",
          "3076044"
        ],
        "e1": [
          "2596205"
        ],
        "s3472": "a60558b0-f6c8-42a1-9ddc-2bea0a1980b5",
        "s7606": "68c8602b-a12b-446e-83a1-2e80866aee97",
        "s63040": "d853a01a-6b31-4776-adcd-36085960a189"
      },
      "score": 0.39941007423104874
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:1119"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "6912140",
          "2747335"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c"
      },
      "score": 0.39939521404771444
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:1097"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678737"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s4742": "3c25f748-71f9-482f-b50e-b01f76b928fe",
        "s50094": "9a1c57b9-556e-4571-8950-277d7badc03d"
      },
      "score": 0.3993880187039112
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:11850"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2753777"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s4159": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "s72605": "2144aa9f-3e85-44b6-b5d6-ff6984c83b8e"
      },
      "score": 0.3993472573035158
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005058",
        "n3": "HGNC:11998"
      },
      "edge_bindings": {
        "e0": [
          "1820654",
          "3321142"
        ],
        "e1": [
          "2761884"
        ],
        "s3238": "adca4ca6-33b5-4ca2-836f-e70407bc62a4",
        "s10408": "36ce6c55-c075-426e-9348-5d2ef326c938",
        "s65034": "9757ddcc-dc18-42fe-8a25-475ff40e62a7"
      },
      "score": 0.39933687179563404
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002462",
        "n3": "HGNC:15633"
      },
      "edge_bindings": {
        "e0": [
          "1820715",
          "3676714"
        ],
        "e1": [
          "2691494"
        ],
        "s999": "a7f079d4-f475-4954-b656-92c8c2bcd1c0",
        "s10956": "cfcd27f5-6364-4809-8190-bc3cf60f700e",
        "s21298": "96a0dfb4-a315-411b-8b59-0ce7b9347b81"
      },
      "score": 0.39931341422645233
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002076",
        "n3": "HGNC:12363"
      },
      "edge_bindings": {
        "e0": [
          "1820669",
          "3076044"
        ],
        "e1": [
          "2596297"
        ],
        "s944": "b38e7a56-a562-4282-9cd3-38a1d9e5adec",
        "s7606": "68c8602b-a12b-446e-83a1-2e80866aee97",
        "s31743": "f6e2e12c-ea68-41d7-b081-4d64e7b6a60b"
      },
      "score": 0.3993070782971392
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:6204"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183062"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s9914": "695daf3a-5059-48be-9d57-5950f1ace359",
        "s52392": "7bda85d5-3f03-404c-81c9-b9a7b6ff8e64"
      },
      "score": 0.3992851222216603
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:4603"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2748524"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s452": "e805f860-28b7-4f5b-826a-166202064858",
        "s56781": "a3939df2-009d-4b46-a210-91048d58cfeb"
      },
      "score": 0.3992540539235893
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0003781",
        "n3": "HGNC:7218"
      },
      "edge_bindings": {
        "e0": [
          "1820630",
          "2801990"
        ],
        "e1": [
          "2582131"
        ],
        "s4707": "46c297af-8f47-4d1d-9f86-06e60a2a2f72",
        "s12865": "0ec14d0b-aaa0-4d4f-842c-8ca710a6a79f",
        "s26826": "30e54399-ddbd-4660-878d-1b2b8664c479"
      },
      "score": 0.3992135623246368
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004822",
        "n3": "HGNC:11722"
      },
      "edge_bindings": {
        "e0": [
          "1820728",
          "2899034"
        ],
        "e1": [
          "2687744"
        ],
        "s1193": "9d714683-5b7f-4878-a8f7-7cbb2f1c8587",
        "s1765": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "s65511": "5f7ea310-295b-4cd1-a0ae-8ecfaa5dae9e"
      },
      "score": 0.3992116641644016
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005279",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820660",
          "3966551"
        ],
        "e1": [
          "4187277"
        ],
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s5037": "07e8031f-da3f-4085-a05b-a7923d34ad30",
        "s5315": "72f4972a-f115-4c0f-8239-ebe1d75b959a"
      },
      "score": 0.39919240739945483
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007140",
        "n3": "HGNC:7436"
      },
      "edge_bindings": {
        "e0": [
          "1820734",
          "2914921"
        ],
        "e1": [
          "2635845"
        ],
        "s1718": "56e355ce-1622-45e0-8deb-f8ce0d4cf17c",
        "s4849": "044de512-efa6-4249-b6d3-5d569fea9574",
        "s14168": "45afbd5c-b2fe-4fe2-8655-c982bdb8c6a9"
      },
      "score": 0.39916315420524007
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:1773"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4255896"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s14007": "e9bad44b-25d2-4da8-b558-a710a4fe89aa",
        "s14008": "b027e13e-3f39-470b-bf15-62206de64a9d"
      },
      "score": 0.39916077913746606
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002076",
        "n3": "HGNC:11722"
      },
      "edge_bindings": {
        "e0": [
          "1820669",
          "3076044"
        ],
        "e1": [
          "2596271"
        ],
        "s1193": "9d714683-5b7f-4878-a8f7-7cbb2f1c8587",
        "s7606": "68c8602b-a12b-446e-83a1-2e80866aee97",
        "s69271": "753057aa-c7da-469f-a651-60b8c311239f"
      },
      "score": 0.39915366985177253
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:6018"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183031"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s1474": "b43d0e58-7c89-477f-91fd-3bcdf5cd4589",
        "s73152": "e65f77dd-e7ba-465c-b18f-673a86fde017"
      },
      "score": 0.3991491614304069
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0006277",
        "n3": "HGNC:12362"
      },
      "edge_bindings": {
        "e0": [
          "1820735",
          "2941808"
        ],
        "e1": [
          "2651604"
        ],
        "s1307": "cdb535f8-867b-48d5-bb8d-949b21fc4247",
        "s6968": "29a68ee9-d8db-47a1-b6bc-1759867e471f",
        "s79917": "bcb4fb0f-9c1c-4842-a70f-108dbe7b09c6"
      },
      "score": 0.3991485954074135
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0001243",
        "n3": "HGNC:12726"
      },
      "edge_bindings": {
        "e0": [
          "1820638",
          "2923197"
        ],
        "e1": [
          "2621762"
        ],
        "s792": "dda1ef5a-7786-4be5-bba5-a77634ef19a6",
        "s1548": "5c8e3c6d-2830-4f56-aeef-2df2e44bf3b3",
        "s1549": "08ad4229-205a-4f6f-9e15-4b7b07c55d53"
      },
      "score": 0.39914276366640233
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:11848"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2753890"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s1253": "9ea2cbf1-63a4-49f7-9172-de14b016e5aa",
        "s57646": "10f8ff3b-44ce-4956-bdab-8c1c9e2cc5c6"
      },
      "score": 0.3991362627029521
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:2295"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678794"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s4467": "fd7ff6fe-9164-44be-9257-17786e848143",
        "s7054": "41779006-bae4-4bcf-941e-610e2a8baf91"
      },
      "score": 0.39912864177442453
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:8594"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2752446"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s38279": "a94f7cf1-a880-44a0-a8db-cd2a9994c3a5",
        "s41809": "c3ea54b6-ec4c-4e9e-ac39-6b1f99f2bfb3"
      },
      "score": 0.399125234151587
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:11768"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175638"
        ],
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s7029": "f9d6e263-c4c2-4f08-83ef-d8d7508efee2",
        "s67057": "3cc10b3f-d93d-4f04-9dfa-2ea641fcdb20"
      },
      "score": 0.399123320323488
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:11249"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183289"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s22748": "ec4983f9-5460-4463-b5f1-5aee5fba320b",
        "s22749": "1178bf6a-2eec-4f48-8960-2216288d7351"
      },
      "score": 0.39912225029853565
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:17643"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2750050"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s23952": "64a48dbe-c7cb-4461-9939-fccfed2a470c",
        "s23953": "d8f0f46e-45d6-4d96-8036-02fa1c2ba9c8"
      },
      "score": 0.39911588954262006
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005812",
        "n3": "HGNC:11850"
      },
      "edge_bindings": {
        "e0": [
          "1820737",
          "3203776"
        ],
        "e1": [
          "2654646"
        ],
        "s854": "39790313-d958-40f8-8314-3966274b2777",
        "s4159": "f03c7ae2-ab85-4f42-ae54-4e9e6896371c",
        "s46221": "b21c1a07-5458-4e6c-b7ea-c04e7ab07f6f"
      },
      "score": 0.39911216483871675
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:6342"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2751291"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s2062": "7a40a3ac-cae3-4943-b9da-e8fe6e354ab8",
        "s50003": "7908c7f5-ff27-4457-a017-3be747b8b371"
      },
      "score": 0.3991066635848506
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0006656",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820644",
          "2921981"
        ],
        "e1": [
          "2640490"
        ],
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s29104": "231143ed-3952-4cb4-a8b1-5247e0f54776",
        "s29105": "3f160b3b-ca7a-4400-9ab5-7df5122af84b"
      },
      "score": 0.399099111606119
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004822",
        "n3": "HGNC:7865"
      },
      "edge_bindings": {
        "e0": [
          "1820728",
          "2899034"
        ],
        "e1": [
          "2687733"
        ],
        "s1765": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "s24875": "4000cdaa-c19e-42ba-89fa-2d9da7750386",
        "s50467": "dd66d7f2-d9f8-415d-a3b4-6180990dec5d"
      },
      "score": 0.3990917137442664
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0019180",
        "n3": "HGNC:1078"
      },
      "edge_bindings": {
        "e0": [
          "1820757",
          "3942179"
        ],
        "e1": [
          "4224302"
        ],
        "s3500": "32e568d6-fba8-4233-bde3-9b8e4a762911",
        "s6772": "4e813b42-dc60-40c5-be59-1526f44dcecb",
        "s78666": "07b31d5b-91b0-438b-a1ee-c29dc0d70c6e"
      },
      "score": 0.39908618125578643
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004492",
        "n3": "HGNC:2367"
      },
      "edge_bindings": {
        "e0": [
          "1820727",
          "2831780"
        ],
        "e1": [
          "2641868"
        ],
        "s2026": "97f7a0aa-9408-4b6a-96b0-635667a0074d",
        "s13290": "ac079803-90d8-412b-a8ba-60954973bfc5",
        "s63847": "4570615e-da8e-456c-a0d6-3b4811077dfc"
      },
      "score": 0.399061152444252
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004849",
        "n3": "HGNC:7176"
      },
      "edge_bindings": {
        "e0": [
          "1820688",
          "2769040"
        ],
        "e1": [
          "2579885"
        ],
        "s4685": "259b01be-50d1-432f-a3dd-03cf59ae9ed2",
        "s4686": "7ee3be0c-bcab-4aa4-aa8b-2869e14a8b2d",
        "s4687": "2a322cc4-81a9-4d48-980a-a655c1375d25"
      },
      "score": 0.399053039250818
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0007256",
        "n3": "HGNC:795"
      },
      "edge_bindings": {
        "e0": [
          "1820643",
          "2042288"
        ],
        "e1": [
          "2678685"
        ],
        "s35": "1511cbd5-3572-4128-8f76-b29c06f9fe48",
        "s16275": "beff4fc7-93ee-4423-a766-bc3c53ec935a",
        "s35432": "81e63527-e413-41a8-aa2e-27889deeca35"
      },
      "score": 0.3990373146638951
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004822",
        "n3": "HGNC:1698"
      },
      "edge_bindings": {
        "e0": [
          "1820728",
          "2899034"
        ],
        "e1": [
          "2687682"
        ],
        "s1605": "eaaa2aa5-41a7-4229-b893-e87f62086030",
        "s1765": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "s37672": "f1186809-1d21-457e-9c62-c64b78b0ce85"
      },
      "score": 0.3990116865933924
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005812",
        "n3": "HGNC:11848"
      },
      "edge_bindings": {
        "e0": [
          "1820737",
          "3203776"
        ],
        "e1": [
          "2654663"
        ],
        "s854": "39790313-d958-40f8-8314-3966274b2777",
        "s1253": "9ea2cbf1-63a4-49f7-9172-de14b016e5aa",
        "s63286": "40aa1e35-c5f3-4b25-a8dc-be18e973a496"
      },
      "score": 0.39900419047341795
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005279",
        "n3": "HGNC:12726"
      },
      "edge_bindings": {
        "e0": [
          "1820660",
          "3966551"
        ],
        "e1": [
          "4187311"
        ],
        "s1548": "5c8e3c6d-2830-4f56-aeef-2df2e44bf3b3",
        "s5037": "07e8031f-da3f-4085-a05b-a7923d34ad30",
        "s38515": "b095dfb4-2e5d-4d39-a228-182a77d7bc51"
      },
      "score": 0.3990034293469241
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0001243",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820638",
          "2923197"
        ],
        "e1": [
          "2621751"
        ],
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s792": "dda1ef5a-7786-4be5-bba5-a77634ef19a6",
        "s47536": "f305827b-326a-4d0b-98bd-a704b27d341a"
      },
      "score": 0.39899196729044495
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:11925"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256641"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s345": "b63e4788-a139-4886-bfcc-5cbc9bbc347c",
        "s17791": "ac32a369-076c-4c14-820f-7cac67b92cc4"
      },
      "score": 0.39899068200127175
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0004822",
        "n3": "HGNC:11892"
      },
      "edge_bindings": {
        "e0": [
          "1820728",
          "2899034"
        ],
        "e1": [
          "2687749"
        ],
        "s524": "003463ba-08ff-4701-a318-41c042b128f8",
        "s1765": "66d6b011-c1ab-437c-bed8-5ad3668694e6",
        "s63765": "ceac4a36-ca9f-4828-aaf1-b8c5723989b0"
      },
      "score": 0.39897217656611983
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0006932",
        "n3": "HGNC:7876"
      },
      "edge_bindings": {
        "e0": [
          "1820666",
          "2980256"
        ],
        "e1": [
          "2671453"
        ],
        "s480": "c2db85d2-4c2a-4c8e-9788-e8e65e657060",
        "s481": "965adb3b-749e-4b1e-b8d6-371bd2e62361",
        "s482": "0f9c87f9-709d-4c9b-9063-88ee41059a5a"
      },
      "score": 0.3989670672763445
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:6018"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2750766"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s1474": "b43d0e58-7c89-477f-91fd-3bcdf5cd4589",
        "s24201": "c16f2fb3-e28d-4d4c-ab66-bb99b8e76b26"
      },
      "score": 0.3989446313896078
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0009061",
        "n3": "HGNC:307"
      },
      "edge_bindings": {
        "e0": [
          "1820740",
          "3059422"
        ],
        "e1": [
          "2746251"
        ],
        "s48": "04f8d674-e21c-4f0d-b3af-da0596ce688c",
        "s17414": "2edb34f2-fe85-44df-af03-46d0ea23f5c7",
        "s17415": "40ff5b74-db6c-4676-be56-3d9efc6c73a3"
      },
      "score": 0.39894423341704394
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005657",
        "n3": "HGNC:5438"
      },
      "edge_bindings": {
        "e0": [
          "1820724",
          "3177611"
        ],
        "e1": [
          "2640296"
        ],
        "s2252": "d1981f79-da4d-4852-885d-5a4e3b9491b4",
        "s5600": "a3888560-692c-4833-8a88-125e0d36be4d",
        "s5601": "78e8cd5f-8491-4677-bf3d-d9f98c695e86"
      },
      "score": 0.3989327810799526
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002462",
        "n3": "HGNC:399"
      },
      "edge_bindings": {
        "e0": [
          "1820715",
          "3676714"
        ],
        "e1": [
          "2691241"
        ],
        "s999": "a7f079d4-f475-4954-b656-92c8c2bcd1c0",
        "s1015": "35075ee5-4215-43cb-922c-409ed452d486",
        "s80753": "074ab227-dc19-4347-9114-988a9bac4664"
      },
      "score": 0.3989265049979765
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005233",
        "n3": "HGNC:7436"
      },
      "edge_bindings": {
        "e0": [
          "1820678",
          "3893921"
        ],
        "e1": [
          "4183550"
        ],
        "s32": "7968ccec-4091-4626-be63-8e4e671dfefe",
        "s4849": "044de512-efa6-4249-b6d3-5d569fea9574",
        "s59888": "5fdb0a52-6c1c-4de5-a141-c30c33988025"
      },
      "score": 0.39892559867019656
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002568",
        "n3": "HGNC:11722"
      },
      "edge_bindings": {
        "e0": [
          "1820705",
          "2794766"
        ],
        "e1": [
          "2580242"
        ],
        "s1193": "9d714683-5b7f-4878-a8f7-7cbb2f1c8587",
        "s8297": "fcab9d15-4847-4425-b8ec-745a2dd02b59",
        "s8559": "653a41a0-1421-474d-aee6-9610fe0d9d9d"
      },
      "score": 0.39892224190615216
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002363",
        "n3": "HGNC:5173"
      },
      "edge_bindings": {
        "e0": [
          "1820640",
          "3665783"
        ],
        "e1": [
          "2643897"
        ],
        "s2091": "6fbde79f-d983-4d62-b16a-97f23517bf98",
        "s5212": "d1987fd3-c29f-4a52-afce-abdf2d164952",
        "s67396": "16eebf17-8ad7-4e26-9e68-4ab0743c3cbf"
      },
      "score": 0.39891798327050687
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0002462",
        "n3": "HGNC:12796"
      },
      "edge_bindings": {
        "e0": [
          "1820715",
          "3676714"
        ],
        "e1": [
          "2691502"
        ],
        "s999": "a7f079d4-f475-4954-b656-92c8c2bcd1c0",
        "s6156": "6fe33571-68cb-41c7-af1c-77d8e329ac98",
        "s78950": "863f1854-f622-4af0-95fd-788944c74c5e"
      },
      "score": 0.39891414406014475
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0018874",
        "n3": "HGNC:12363"
      },
      "edge_bindings": {
        "e0": [
          "1820642",
          "3452626"
        ],
        "e1": [
          "4256661"
        ],
        "s60": "8695605d-b919-45b2-afc6-5beb63c152b4",
        "s944": "b38e7a56-a562-4282-9cd3-38a1d9e5adec",
        "s53538": "a7f8902c-d26d-4125-97af-7667a827674c"
      },
      "score": 0.3989084700256629
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005160",
        "n3": "HGNC:2707"
      },
      "edge_bindings": {
        "e0": [
          "1820700",
          "3776653"
        ],
        "e1": [
          "4175604"
        ],
        "s2223": "f86e339a-8b21-4c0a-aa3c-fd5447600560",
        "s2553": "11f5bc12-4ca0-41fd-8542-0676c5acdb39",
        "s65085": "0cde5943-6c9d-4840-bf9b-9a7ed4866db0"
      },
      "score": 0.3989008312615699
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005825",
        "n3": "HGNC:11848"
      },
      "edge_bindings": {
        "e0": [
          "1820696",
          "3209598"
        ],
        "e1": [
          "2656447"
        ],
        "s1253": "9ea2cbf1-63a4-49f7-9172-de14b016e5aa",
        "s6503": "4738946c-9430-48f3-82e9-772619087210",
        "s79646": "292929d4-d75e-4e8d-9516-d5b73215bfde"
      },
      "score": 0.39889289347707424
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005812",
        "n3": "HGNC:7124"
      },
      "edge_bindings": {
        "e0": [
          "1820737",
          "3203776"
        ],
        "e1": [
          "2654432"
        ],
        "s854": "39790313-d958-40f8-8314-3966274b2777",
        "s18261": "65d91f85-dada-41ee-bb40-1a377d862245",
        "s59050": "b0cdfdbd-425a-4da2-8201-5e74a6eaecf5"
      },
      "score": 0.39888882423950556
    },
    {
      "node_bindings": {
        "n1": "HP:0002105",
        "n2": "MONDO:0005812",
        "n3": "HGNC:15633"
      },
      "edge_bindings": {
        "e0": [
          "1820737",
          "3203776"
        ],
        "e1": [
          "2654807"
        ],
        "s854": "39790313-d958-40f8-8314-3966274b2777",
        "s10956": "cfcd27f5-6364-4809-8190-bc3cf60f700e",
        "s53133": "7dc1e0a5-dc33-40e9-a1ee-efc7c5a2e4ba"
      },
      "score": 0.3988872228310673
    }
  ]
}

