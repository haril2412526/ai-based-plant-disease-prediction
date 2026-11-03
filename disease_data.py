"""
PlantCare AI - Comprehensive Plant Disease Knowledge Base
Contains rich metadata, symptoms, causes, conventional treatments,
organic options, and prevention guidelines for common crop diseases.
"""

DISEASE_DATABASE = {
    "Tomato___Early_blight": {
        "id": "Tomato___Early_blight",
        "crop": "Tomato",
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "severity": "Moderate to High",
        "severity_color": "warning",
        "overview": "Early blight is a very common fungal disease affecting tomatoes and potatoes. It can cause leaf spot, fruit rot, and stem cankers, significantly reducing fruit yield and plant vigor.",
        "symptoms": [
            "Concentric ring 'bullseye' target patterns on older lower leaves first.",
            "Yellow halo surrounding brown necrotic spots.",
            "Premature defoliation starting from the ground up, exposing fruit to sunscald.",
            "Dark, sunken, leathery lesions near the stem end of tomato fruits."
        ],
        "causes": [
            "Warm temperatures (24°C–29°C / 75°F–85°F) with high humidity or frequent rain.",
            "Forespores overwintering on infected crop debris in the soil.",
            "Water splash spreading fungal spores from soil onto lower foliage."
        ],
        "treatment_chemical": [
            "Apply protective fungicides containing Chlorothalonil or Mancozeb at first sign of infection.",
            "Rotate with azoxystrobin or copper-based fungicides to prevent fungal resistance.",
            "Spray in early morning on clear days every 7-14 days as weather conditions dictate."
        ],
        "treatment_organic": [
            "Apply cold-pressed pure Neem Oil (0.5% - 1% dilution) with mild emulsifier every 7 days.",
            "Use bio-fungicides formulated with Bacillus subtilis or Bacillus amyloliquefaciens (e.g., Serenade).",
            "Spray Copper Octanoate (copper soap) which is OMRI-listed for organic farming.",
            "Aerate with diluted compost tea containing beneficial antagonistic microbes."
        ],
        "prevention": [
            "Practice strict 3-year crop rotation (avoid planting solanaceous crops in the same bed).",
            "Mulch heavily around the base with clean straw or plastic mulch to stop soil splashing.",
            "Prune bottom 12 inches of foliage once plant is established to maximize airflow.",
            "Water at the base with drip irrigation or soaker hoses; avoid overhead watering."
        ]
    },

    "Tomato___Late_blight": {
        "id": "Tomato___Late_blight",
        "crop": "Tomato",
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Severe / Critical",
        "severity_color": "danger",
        "overview": "Late blight is a devastating water-mold disease famous for causing the Irish Potato Famine. It can destroy entire fields within a few days under cool, wet conditions.",
        "symptoms": [
            "Irregular, water-soaked dark green to black-brown lesions on leaves and stems.",
            "Delicate white fuzzy fungal growth appearing on leaf undersides in high humidity.",
            "Rapid browning, shriveling, and death of entire foliage branches.",
            "Greasy, dark brown, firm rot developing rapidly across green or ripe tomatoes."
        ],
        "causes": [
            "Cool, damp, fog-laden weather (15°C–20°C / 60°F–70°F) with relative humidity >90%.",
            "Windborne sporangia travelling miles from infected potato cull piles or neighboring fields.",
            "Extended leaf wetness lasting 8 or more hours."
        ],
        "treatment_chemical": [
            "Immediately apply systemic fungicides containing Cyazofamid, Mandipropamid, or Dimethomorph.",
            "Tank-mix with a multi-site protectant like Chlorothalonil or Mancozeb.",
            "Severely blighted plants must be pulled up, bagged, and incinerated immediately to protect neighboring crops."
        ],
        "treatment_organic": [
            "Apply Fixed Copper hydroxide or Copper sulfate preventative sprays before disease establishes.",
            "Apply Potassium Bicarbonate sprays combined with bio-fungicide (Bacillus subtilis).",
            "Note: Once late blight enters vascular tissue, organic treatments are largely suppressive; prompt removal of infected plants is safest."
        ],
        "prevention": [
            "Select resistant cultivars (e.g., Mountain Magic, Defiant, Iron Lady, Plum Regal).",
            "Destroy all volunteer tomato and potato plants in spring.",
            "Space plants widely (at least 24-36 inches) to promote rapid sun drying of foliage.",
            "Monitor regional late blight forecasting networks (e.g., USAblight alerts)."
        ]
    },

    "Tomato___Leaf_Mold": {
        "id": "Tomato___Leaf_Mold",
        "crop": "Tomato",
        "disease_name": "Leaf Mold",
        "pathogen": "Passalora fulva (syn. Cladosporium fulvum)",
        "severity": "Moderate",
        "severity_color": "warning",
        "overview": "Leaf mold primarily attacks greenhouse and high-tunnel tomatoes where humidity remains continuously elevated, though it can occur in humid outdoor gardens.",
        "symptoms": [
            "Pale green to yellow chlorotic spots with indefinite margins on upper leaf surfaces.",
            "Olive green to velvety brown fungal sporulation on corresponding leaf undersides.",
            "Lower leaves curl, wither, and drop prematurely.",
            "Fruit symptoms are rare, but blossoms may abort under heavy infection."
        ],
        "causes": [
            "Very high relative humidity (above 85%) and moderate temperatures (20°C–24°C).",
            "Poor greenhouse air circulation and dense canopy crowding."
        ],
        "treatment_chemical": [
            "Fungicides with Chlorothalonil, Difenoconazole, or Cyprodinil provide effective control.",
            "Thorough coverage on the undersides of leaves is critical."
        ],
        "treatment_organic": [
            "Copper soap (copper octanoate) sprays applied thoroughly to leaf undersides.",
            "Sulfur-based fungicides (avoid when temperatures exceed 30°C / 86°F).",
            "Biological agents such as Trichoderma harzianum leaf sprays."
        ],
        "prevention": [
            "Ventilate greenhouses with exhaust fans and horizontal airflow fans to keep humidity <85%.",
            "Heat and ventilate greenhouse air at sunset to prevent evening dew condensation.",
            "Prune suckers and lower senescent leaves to open the plant canopy."
        ]
    },

    "Tomato___Bacterial_spot": {
        "id": "Tomato___Bacterial_spot",
        "crop": "Tomato",
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas vesicatoria / perforans",
        "severity": "High",
        "severity_color": "danger",
        "overview": "A damaging bacterial disease that causes unsightly lesions on leaves, stems, and fruits, rendering tomatoes unmarketable and weakening plant canopy.",
        "symptoms": [
            "Small (less than 3mm), water-soaked angular dark brown spots on foliage.",
            "Spots may coalesce, giving leaves a blighted, ragged, or shot-hole appearance.",
            "Leaves turn yellow and drop prematurely.",
            "Scabby, elevated black spots on green fruit, often surrounded by a white halo."
        ],
        "causes": [
            "Warm temperatures (24°C–30°C) with persistent rains, wind-driven storms, or overhead sprinkler irrigation.",
            "Bacterial contamination of seed or infected transplant plugs.",
            "Bacterial entry through natural stomata or wound openings."
        ],
        "treatment_chemical": [
            "Apply Copper bactericides mixed with Mancozeb (this combination breaks copper resistance).",
            "Apply Actigard (acibenzolar-S-methyl) to induce systemic acquired resistance in commercial crops."
        ],
        "treatment_organic": [
            "Apply OMRI-listed Copper fungicides/bactericides early in morning.",
            "Treat plants with bacteriophage sprays specific to Xanthomonas species (e.g., AgriPhage).",
            "Hydrogen dioxide / peroxyacetic acid spray sanitizers for surface disinfection."
        ],
        "prevention": [
            "Use certified pathogen-free, hot-water-treated tomato seed.",
            "Never work among wet tomato plants (pruning, tying, or harvesting).",
            "Sanitize trellising stakes, pruning shears, and greenhouse benches with 10% bleach or sanitizing solution.",
            "Implement a minimum 2-year non-solanaceous crop rotation."
        ]
    },

    "Tomato___healthy": {
        "id": "Tomato___healthy",
        "crop": "Tomato",
        "disease_name": "Healthy Plant (No Disease Detected)",
        "pathogen": "None - Plant is in optimal health",
        "severity": "Optimal / Healthy",
        "severity_color": "success",
        "overview": "Your tomato foliage displays vigorous, uniform green color, firm vascular tissue, and no signs of fungal, bacterial, or viral pathogens.",
        "symptoms": [
            "Vibrant, even deep green coloration without chlorosis.",
            "Absence of necrotic spotting, wilting, or mildew growth.",
            "Firm, supple stems with healthy trichomes (leaf hairs).",
            "Uniform leaf expansion and normal blossom development."
        ],
        "causes": [
            "Excellent cultural practices, well-balanced nutrition, and optimal environmental conditions."
        ],
        "treatment_chemical": [
            "No chemical fungicides or bactericides required. Do not apply unnecessary chemicals."
        ],
        "treatment_organic": [
            "Maintain soil biology with organic compost, worm castings, or seaweed foliar tonic.",
            "Apply beneficial mycorrhizal fungi to root zone to enhance nutrient uptake."
        ],
        "prevention": [
            "Continue regular inspection schedule (twice weekly).",
            "Maintain consistent soil moisture to prevent blossom end rot and fruit splitting.",
            "Ensure balanced fertilization (avoid excess nitrogen which promotes dense, humid foliage)."
        ]
    },

    "Potato___Early_blight": {
        "id": "Potato___Early_blight",
        "crop": "Potato",
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "severity": "Moderate",
        "severity_color": "warning",
        "overview": "Early blight is a recurring fungal disease in potatoes, attacking maturing foliage and causing dark corky tuber rot during post-harvest storage.",
        "symptoms": [
            "Target-like dark brown circular to angular spots with concentric ridges.",
            "Chlorotic yellowing around leaf lesions leading to premature leaf drop.",
            "Sunken, irregular, leathery dark brown spots on tuber skin with dry rot underneath."
        ],
        "causes": [
            "High humidity, alternating dry and wet periods, warm temperatures (24°C–29°C).",
            "Stressed plants lacking nitrogen, phosphorus, or moisture are more susceptible."
        ],
        "treatment_chemical": [
            "Spray Chlorothalonil, Mancozeb, or Pyraclostrobin at tuber initiation.",
            "Alternate fungicide modes of action according to FRAC guidelines."
        ],
        "treatment_organic": [
            "Spray copper-based organic formulations (Copper Hydroxide or Octanoate).",
            "Apply bio-fungicides containing Bacillus amyloliquefaciens or Trichoderma.",
            "Foliar silica sprays to strengthen plant cell walls."
        ],
        "prevention": [
            "Maintain optimal crop fertility and irrigation throughout tuber bulking.",
            "Use certified disease-free seed tubers.",
            "Wait 2-3 weeks after vine desiccation before harvesting tubers so skins can cure."
        ]
    },

    "Potato___Late_blight": {
        "id": "Potato___Late_blight",
        "crop": "Potato",
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Severe / Critical",
        "severity_color": "danger",
        "overview": "Late blight is the most notorious disease of potatoes worldwide. Capable of decimating an entire potato canopy within a week and turning stored tubers into mushy rot.",
        "symptoms": [
            "Large, dark, water-soaked lesions that turn necrotic and blackish brown.",
            "Fuzzy white mildew on the underside of leaves during wet morning hours.",
            "Rapid stem collapse and foul decaying odor in the canopy.",
            "Coppery reddish-brown dry granular rot extending into the tuber flesh."
        ],
        "causes": [
            "Prolonged wetness (dew or rain) and cool to moderate temperatures (12°C–22°C).",
            "Infected seed tubers or volunteer plants serving as initial inoculum sources."
        ],
        "treatment_chemical": [
            "Apply systemic oomycide fungicides like Mefenoxam, Fluopicolide, or Cyazofamid immediately.",
            "Destroy badly blighted vine patches to prevent spore migration into tubers."
        ],
        "treatment_organic": [
            "Preventive fixed copper sprays before rainfall events.",
            "Bio-rational potassium silicate and biological antagonists.",
            "Rapidly kill and bury severely affected vines before tubers are infected."
        ],
        "prevention": [
            "Plant only certified disease-free seed potatoes.",
            "Hill soil deeply around potatoes (at least 4-6 inches) to prevent spores washing into tubers.",
            "Eliminate cull potato piles and volunteer potatoes."
        ]
    },

    "Potato___healthy": {
        "id": "Potato___healthy",
        "crop": "Potato",
        "disease_name": "Healthy Plant (No Disease Detected)",
        "pathogen": "None - Plant is in optimal health",
        "severity": "Optimal / Healthy",
        "severity_color": "success",
        "overview": "Your potato foliage shows robust green health, excellent vegetative vigor, and complete absence of pathogenic blights.",
        "symptoms": [
            "Lush emerald foliage with crisp edges.",
            "No necrotic spots, target rings, or mildew.",
            "Uniform stem growth and vigorous flower/tuber formation."
        ],
        "causes": [
            "Healthy seed stock, well-drained acidic soil (pH 5.8-6.5), and optimal weather."
        ],
        "treatment_chemical": [
            "No chemical intervention needed."
        ],
        "treatment_organic": [
            "Apply balanced compost tea and kelp meal to support tuber sizing."
        ],
        "prevention": [
            "Ensure steady irrigation (1 to 2 inches per week) to prevent knobby tubers.",
            "Maintain adequate hilling to protect developing tubers from sunlight."
        ]
    },

    "Apple___Apple_scab": {
        "id": "Apple___Apple_scab",
        "crop": "Apple",
        "disease_name": "Apple Scab",
        "pathogen": "Venturia inaequalis (Fungus)",
        "severity": "Moderate to High",
        "severity_color": "warning",
        "overview": "Apple scab is the most economically significant apple disease in humid apple-growing regions, causing leaf defoliation and corky blemished fruits.",
        "symptoms": [
            "Velvety olive-green to dark brown circular spots on leaves.",
            "Leaves turn twisted, yellow, and drop prematurely in midsummer.",
            "Rough, scabby, corky brown lesions on fruit surface with cracks allowing secondary rot."
        ],
        "causes": [
            "Ascospores released from fallen overwintered leaves during spring rains.",
            "Leaf wetness periods of 6 to 9 hours at temperatures between 15°C and 24°C."
        ],
        "treatment_chemical": [
            "Fungicide sprays starting at green tip stage: Captan, Myclobutanil, or Mancozeb.",
            "Follow Mill's scab infection period model to time applications effectively."
        ],
        "treatment_organic": [
            "Lime-sulfur or wettable sulfur applied preventatively during early green tip and pink bud stages.",
            "Liquid copper spray applied at silver tip to 1/4-inch green.",
            "Bacillus subtilis foliar applications."
        ],
        "prevention": [
            "Shred fallen autumn leaves with a flail mower or spray 5% urea solution to accelerate decomposition.",
            "Prune tree canopy annually into open-center or central-leader shape to maximize airflow and sun penetration.",
            "Plant scab-resistant apple cultivars (e.g., Liberty, Prima, Enterprise, GoldRush)."
        ]
    },

    "Apple___Black_rot": {
        "id": "Apple___Black_rot",
        "crop": "Apple",
        "disease_name": "Black Rot (Frogeye Leaf Spot)",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "severity": "High",
        "severity_color": "danger",
        "overview": "A fungal disease causing frogeye leaf spots, trunk cankers, and a firm, mummified black fruit rot on apples.",
        "symptoms": [
            "Small purple specks on leaves expanding into circular spots with tan centers and purple margins ('frogeye').",
            "Sunken, reddish-brown bark cankers on limbs that girdle twigs.",
            "Rotting apples developing concentric dark rings and turning completely black, shriveled 'mummies'."
        ],
        "causes": [
            "Inoculum residing in dead wood, fire blight cankers, and mummified apples hanging in trees.",
            "Warm (26°C–28°C), wet weather during petal fall."
        ],
        "treatment_chemical": [
            "Fungicides containing Captan, Thiophanate-methyl, or Pristine (pyraclostrobin + boscalid)."
        ],
        "treatment_organic": [
            "Thorough copper spray applications at delayed dormant stage.",
            "Sulfur sprays applied from tight cluster through bloom."
        ],
        "prevention": [
            "Prune out dead wood, cankered limbs, and mummified fruit during dormant winter pruning.",
            "Sterilize pruning tools with 70% isopropyl alcohol between cuts.",
            "Control codling moth and plum curculio, as insect wounds allow fungal entry into fruit."
        ]
    },

    "Apple___healthy": {
        "id": "Apple___healthy",
        "crop": "Apple",
        "disease_name": "Healthy Plant (No Disease Detected)",
        "pathogen": "None - Plant is in optimal health",
        "severity": "Optimal / Healthy",
        "severity_color": "success",
        "overview": "Apple leaves show clean, smooth, glossy surfaces with healthy venation and no evidence of fungal scab, rust, or canker.",
        "symptoms": [
            "Glossy dark green leaves without chlorosis or necrotic margins.",
            "Healthy terminal shoot growth without mildew coating.",
            "Smooth bark and clean fruit set."
        ],
        "causes": [
            "Optimal orchard sanitation, balanced soil nutrients, and proper dormant care."
        ],
        "treatment_chemical": [
            "No chemical application required."
        ],
        "treatment_organic": [
            "Spray bio-stimulants such as cold-water kelp extract to strengthen leaf cuticle."
        ],
        "prevention": [
            "Maintain annual winter pruning for air circulation and light interception.",
            "Apply dormant horticultural oil in late winter to suppress overwintering insect eggs."
        ]
    },

    "Corn___Common_rust": {
        "id": "Corn___Common_rust",
        "crop": "Corn (Maize)",
        "disease_name": "Common Rust",
        "pathogen": "Puccinia sorghi (Fungus)",
        "severity": "Moderate",
        "severity_color": "warning",
        "overview": "Common rust occurs wherever maize is grown. It creates powdery cinnamon-brown pustules that rupture leaf epidermis, diminishing photosynthetic area.",
        "symptoms": [
            "Small, oval to elongated cinnamon-brown pustules on both upper and lower leaf surfaces.",
            "Pustules rupture the epidermis and release dusty reddish-brown urediniospores when touched.",
            "Severe infections cause leaves to yellow, dry out, and senesce prematurely."
        ],
        "causes": [
            "Cool to moderate temperatures (16°C–25°C) and high relative humidity (near 100%).",
            "Spores blown northward from southern subtropical regions on storm systems."
        ],
        "treatment_chemical": [
            "Foliar fungicides with Strobilurins (Azoxystrobin) or Triazoles (Propiconazole) applied if rust appears before tasseling."
        ],
        "treatment_organic": [
            "Liquid copper fungicides or wettable sulfur applied as protectants early in the season.",
            "Bio-fungicides based on Bacillus pumilus or Bacillus subtilis."
        ],
        "prevention": [
            "Plant resistant corn hybrids with Rp gene resistance.",
            "Plant early in the season to minimize exposure to peak spore migration periods.",
            "Ensure balanced fertilization (avoid excessive nitrogen and insufficient potassium)."
        ]
    },

    "Corn___Northern_Leaf_Blight": {
        "id": "Corn___Northern_Leaf_Blight",
        "crop": "Corn (Maize)",
        "disease_name": "Northern Corn Leaf Blight (NCLB)",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "severity": "High",
        "severity_color": "danger",
        "overview": "Northern Corn Leaf Blight is a destructive foliar disease causing large cigar-shaped lesions, leading to significant grain fill loss if it strikes during silking.",
        "symptoms": [
            "Characteristic long, elliptical, grayish-green to tan 'cigar-shaped' lesions (2.5 to 15 cm long).",
            "Lesions start on lower leaves and progress rapidly up the canopy.",
            "Under humid conditions, lesions produce dark olive-colored fungal spores in the center."
        ],
        "causes": [
            "Moderate temperatures (18°C–27°C) with heavy dews and frequent rainfall.",
            "Fungus overwinters in corn residue from the previous season."
        ],
        "treatment_chemical": [
            "Fungicides with Pyraclostrobin, Trifloxystrobin, or Difenoconazole applied from V6 to tasseling.",
            "Economics usually justify treatment if lesions appear on the third leaf below ear leaf or higher before silking."
        ],
        "treatment_organic": [
            "Bio-fungicide sprays containing Bacillus or Trichoderma formulations.",
            "Sulfur and copper protectants applied early in vegetative growth."
        ],
        "prevention": [
            "Select hybrids possessing specific (Ht) or high multi-genic resistance.",
            "Rotate crops for at least 1-2 years with non-host crops like soybeans, wheat, or alfalfa.",
            "Perform conservation tillage to incorporate crop residue into the soil."
        ]
    },

    "Corn___healthy": {
        "id": "Corn___healthy",
        "crop": "Corn (Maize)",
        "disease_name": "Healthy Plant (No Disease Detected)",
        "pathogen": "None - Plant is in optimal health",
        "severity": "Optimal / Healthy",
        "severity_color": "success",
        "overview": "Your maize leaves show vibrant green parallel venation, crisp upright blades, and zero symptoms of rust pustules or blight lesions.",
        "symptoms": [
            "Uniform dark green foliage.",
            "Strong stalk architecture and clean leaf collars.",
            "Normal silk and tassel development without fungal distortion."
        ],
        "causes": [
            "Adequate nitrogen, phosphorus, potassium, balanced soil moisture, and good weed suppression."
        ],
        "treatment_chemical": [
            "No chemical intervention needed."
        ],
        "treatment_organic": [
            "Ensure regular soil aeration and side-dress with organic nitrogen during V6 stage."
        ],
        "prevention": [
            "Maintain soil drainage to avoid waterlogged root conditions.",
            "Regular scout monitoring for early signs of fall armyworm or corn borers."
        ]
    },

    "Grape___Black_rot": {
        "id": "Grape___Black_rot",
        "crop": "Grape",
        "disease_name": "Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "severity": "Severe / High",
        "severity_color": "danger",
        "overview": "Black rot is one of the most destructive grape diseases in warm, humid regions. It can devastate up to 80-100% of the grape cluster crop if left uncontrolled.",
        "symptoms": [
            "Small reddish-brown circular spots on leaves with tiny black specks (pycnidia) arranged in a ring.",
            "Infected grape berries turn soft and brown, rapidly shriveling into hard, wrinkled black 'mummies'.",
            "Black elliptical cankers on shoots and tendrils."
        ],
        "causes": [
            "Warm (21°C–32°C) and humid weather with extended rainfall periods during bloom.",
            "Overwintering mummified berries left on the vine or on the vineyard floor."
        ],
        "treatment_chemical": [
            "Apply Myclobutanil, Tebuconazole, Mancozeb, or Kresoxim-methyl.",
            "Critical spray window is from early bloom through 4 to 6 weeks post-bloom."
        ],
        "treatment_organic": [
            "Copper hydroxide or copper octanoate applied protectively before rain events.",
            "Sulfur sprays (effective early in season, note temperature sensitivity).",
            "Bacillus subtilis biological fungicides."
        ],
        "prevention": [
            "Sanitation: Hand-prune and burn or deeply bury all mummified grape clusters during winter.",
            "Train vines on high trellis systems to improve sun exposure and airflow through the fruit zone.",
            "Keep grass and weeds mowed short under the vine rows to reduce vineyard humidity."
        ]
    },

    "Pepper_bell___Bacterial_spot": {
        "id": "Pepper_bell___Bacterial_spot",
        "crop": "Pepper (Bell)",
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas campestris pv. vesicatoria",
        "severity": "High",
        "severity_color": "danger",
        "overview": "A serious seedborne bacterial disease affecting bell peppers, causing widespread defoliation, sunburned fruit, and wart-like scabs on peppers.",
        "symptoms": [
            "Small, yellow-green spots on leaves that turn brown with water-soaked borders.",
            "Spots usually appear slightly raised on lower leaf surfaces.",
            "Severe defoliation exposing bell peppers to sunscald.",
            "Small raised circular blisters or scabby warts on the fruit surface."
        ],
        "causes": [
            "Warm temperatures (24°C–30°C) combined with high rainfall or sprinkler irrigation.",
            "Contaminated seed or infected seedlings."
        ],
        "treatment_chemical": [
            "Fixed copper sprays tank-mixed with Mancozeb to enhance copper efficacy.",
            "Foliar applications of acibenzolar-S-methyl (Actigard) for plant defense priming."
        ],
        "treatment_organic": [
            "OMRI-listed copper sulfate or copper soap spray.",
            "Bio-pesticide sprays using beneficial antagonistic bacteria (Bacillus subtilis).",
            "Neem-based emulsified botanicals for mild antibacterial suppression."
        ],
        "prevention": [
            "Use certified disease-free, tested pepper seeds.",
            "Avoid overhead irrigation; use drip tape beneath plastic mulch.",
            "Do not enter fields or handle plants when foliage is wet.",
            "Practice 2 to 3-year crop rotation away from solanaceous plants."
        ]
    },

    "Pepper_bell___healthy": {
        "id": "Pepper_bell___healthy",
        "crop": "Pepper (Bell)",
        "disease_name": "Healthy Plant (No Disease Detected)",
        "pathogen": "None - Plant is in optimal health",
        "severity": "Optimal / Healthy",
        "severity_color": "success",
        "overview": "Your bell pepper plant exhibits clean, glossy foliage, thick dark green leaves, sturdy branching, and zero bacterial or fungal spots.",
        "symptoms": [
            "Smooth, crisp, dark green leaf surfaces.",
            "No necrotic lesions, wilting, or yellowing.",
            "Strong crown flowering and robust bell fruit set."
        ],
        "causes": [
            "Warm sunny weather, well-draining loamy soil with steady calcium and magnesium levels."
        ],
        "treatment_chemical": [
            "No chemical treatments needed."
        ],
        "treatment_organic": [
            "Apply foliar Epsom salt (magnesium sulfate) or calcium spray to support thick cell walls."
        ],
        "prevention": [
            "Ensure consistent watering to avoid blossom end rot on bell peppers.",
            "Provide light shade netting if summer temperatures consistently exceed 35°C (95°F)."
        ]
    }
}

# Generic fallback profile for any unexpected class
DEFAULT_DISEASE_INFO = {
    "id": "Unknown___Disease",
    "crop": "Plant",
    "disease_name": "Foliar Plant Anomaly",
    "pathogen": "Suspected Plant Pathogen or Nutrient Deficiency",
    "severity": "Moderate",
    "severity_color": "warning",
    "overview": "An abnormal pattern or discoloration was detected on the plant leaf that warrants closer examination.",
    "symptoms": [
        "Unusual pigmentation, spotting, or leaf edge discoloration.",
        "Localized tissue chlorosis or drying."
    ],
    "causes": [
        "Environmental stress, fungal or bacterial infection, or micro-nutrient imbalance."
    ],
    "treatment_chemical": [
        "Apply a broad-spectrum copper or multi-site protective fungicide if fungal symptoms advance.",
        "Consult your local agricultural extension service for lab soil testing."
    ],
    "treatment_organic": [
        "Apply cold-pressed neem oil (1 tablespoon per gallon water + mild soap).",
        "Prune and discard damaged leaves to reduce pathogen pressure."
    ],
    "prevention": [
        "Improve air circulation and avoid wetting leaves during watering.",
        "Ensure proper soil drainage and balanced N-P-K fertilization."
    ]
}

def get_disease_info(class_name: str) -> dict:
    """Retrieve detailed disease information by class key or return safe fallback."""
    if class_name in DISEASE_DATABASE:
        return DISEASE_DATABASE[class_name]
    
    # Try fuzzy matching
    for key in DISEASE_DATABASE:
        if class_name.lower() in key.lower() or key.lower() in class_name.lower():
            return DISEASE_DATABASE[key]
            
    return DEFAULT_DISEASE_INFO
