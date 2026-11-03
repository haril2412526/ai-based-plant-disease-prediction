"""
PlantCare AI - AI Farming Assistant
Comprehensive agricultural advisory engine providing expert guidance on
crop diseases, organic solutions, soil nutrition, pest management, and farming best practices.
"""

import re
from disease_data import DISEASE_DATABASE, get_disease_info

class FarmingAssistant:
    def __init__(self):
        self.common_topics = {
            "neem_oil": {
                "keywords": ["neem", "neem oil", "organic spray", "botanical spray"],
                "title": "How to Prepare and Apply Neem Oil Spray",
                "response": (
                    "**Neem Oil Preparation Guide:**\n\n"
                    "1. **Concentration:** Mix **2 tablespoons (30 ml) of cold-pressed pure neem oil** per gallon (3.8 liters) of lukewarm water.\n"
                    "2. **Emulsifier:** Add **1 teaspoon of mild liquid castile soap** or dish detergent. The soap breaks surface tension so the oil mixes with water.\n"
                    "3. **Application:** Shake vigorously and spray thoroughly, coating both the **tops and undersides of leaves**.\n"
                    "4. **Timing:** Spray during early morning or dusk. **Never apply under harsh midday sunlight** (temperatures > 30°C / 85°F), as oil can scorch leaves.\n"
                    "5. **Frequency:** Apply every **7–10 days** as a preventative, or every **5 days** during an active pest or mild fungal outbreak."
                )
            },
            "blossom_end_rot": {
                "keywords": ["blossom end rot", "black bottom", "bottom rot", "calcium deficiency"],
                "title": "Managing Blossom End Rot in Tomatoes & Peppers",
                "response": (
                    "**Blossom End Rot Diagnosis & Solution:**\n\n"
                    "Blossom end rot appears as a dark, sunken, leathery patch on the blossom end of developing fruit. It is caused by **localized calcium deficiency in fruit tissue**, almost always triggered by **erratic soil moisture**.\n\n"
                    "**Immediate Actions:**\n"
                    "- **Consistent Watering:** Water deeply and regularly (aim for 1 to 1.5 inches of water per week). Never allow soil to alternate between bone-dry and waterlogged.\n"
                    "- **Mulch Soil:** Apply a 2–3 inch layer of straw, woodchips, or dried grass clippings to stabilize soil moisture.\n"
                    "- **Foliar Calcium Spray:** Spray with calcium chloride or liquid chelated calcium directly on leaves and young fruit for immediate absorption.\n"
                    "- **Avoid Excess Nitrogen:** High ammonium nitrogen promotes rapid foliage growth that steals calcium away from developing fruit."
                )
            },
            "yellow_leaves": {
                "keywords": ["yellow leaf", "yellow leaves", "chlorosis", "leaves turning yellow", "yellowing"],
                "title": "Causes and Solutions for Yellowing Plant Leaves (Chlorosis)",
                "response": (
                    "**Identifying Causes of Yellow Leaves:**\n\n"
                    "1. **Lower Older Leaves Yellowing Uniformly:** Usually **Nitrogen Deficiency** or natural leaf shedding. Feed with a nitrogen-rich organic fertilizer (fish emulsion, blood meal, or compost tea).\n"
                    "2. **Yellow Leaves with Green Veins (Interveinal Chlorosis):** Typically **Iron or Magnesium Deficiency**. If on young leaves, it's iron (often due to high soil pH > 7.0). If on older leaves, it's magnesium—dissolve 1 tablespoon of Epsom salt in 1 gallon of water and spray foliage.\n"
                    "3. **Yellowing Accompanied by Wilting:** **Overwatering or Root Rot**. Ensure drainage holes are clear; allow top 2 inches of soil to dry before watering again.\n"
                    "4. **Yellow Leaves with Dark Spots / Halos:** **Fungal or Bacterial Blight** (such as Septoria or Early Blight). Remove infected foliage immediately and apply copper or neem fungicide."
                )
            },
            "aphids_pests": {
                "keywords": ["aphid", "aphids", "whitefly", "spider mite", "mites", "insects", "bugs", "pest"],
                "title": "Organic Pest Control for Common Garden Insects",
                "response": (
                    "**Eco-Friendly Pest Management:**\n\n"
                    "- **Water Jet Blast:** For aphids and spider mites, knock them off leaf undersides with a strong jet of water from your hose.\n"
                    "- **Insecticidal Soap Spray:** Mix 2 tablespoons of mild soap in 1 quart of warm water. Spray directly onto insects to dissolve their protective waxy cuticle.\n"
                    "- **Beneficial Predators:** Introduce or encourage ladybugs, lacewings, and predatory mites in your garden.\n"
                    "- **Yellow Sticky Traps:** Hang sticky traps near crop height to capture adult whiteflies and thrips.\n"
                    "- **Companion Planting:** Plant marigolds, basil, and sweet alyssum nearby to repel pests and attract pollinating hoverflies."
                )
            },
            "watering_drip": {
                "keywords": ["watering", "how often to water", "irrigation", "drip irrigation", "water schedule"],
                "title": "Best Watering Practices to Prevent Fungal Diseases",
                "response": (
                    "**Smart Irrigation Rules for Disease Prevention:**\n\n"
                    "1. **Water the Roots, Not the Leaves:** 80% of fungal pathogens (blights, powdery mildew, rusts) require wet foliage to germinate. Use **drip irrigation or soaker hoses**.\n"
                    "2. **Water in Early Morning (5 AM - 9 AM):** Morning watering ensures any accidental splash onto leaves dries quickly under early sun rays.\n"
                    "3. **Deep, Infrequent Watering:** Water deeply (so moisture reaches 6–8 inches deep) 2–3 times a week rather than light daily sprinkling. This encourages deep, drought-resilient root systems.\n"
                    "4. **Mulching:** Always keep soil mulched to prevent fungal spores from splashing up onto lower foliage during rain."
                )
            },
            "fertilizer_npk": {
                "keywords": ["fertilizer", "npk", "nitrogen", "phosphorus", "potassium", "feeding", "compost"],
                "title": "NPK Fertilizer Ratios & Crop Feeding Stages",
                "response": (
                    "**Crop Nutrition & N-P-K Guide:**\n\n"
                    "- **Vegetative Growth Stage (Leaves & Stems):** Needs higher **Nitrogen (N)**. Ideal NPK: `3-1-2` or `10-5-5`. Organic sources: Alfalfa meal, fish hydrolysate, composted manure.\n"
                    "- **Flowering & Fruit Setting Stage:** Needs higher **Phosphorus (P) and Potassium (K)**. Ideal NPK: `5-10-10` or `4-18-38`. Organic sources: Bone meal, rock phosphate, kelp meal, wood ash.\n"
                    "- **Signs of Over-Fertilization:** Dark green curled leaf tips (nitrogen burn), salt crust on soil surface, rapid soft vegetative growth that attracts aphids."
                )
            },
            "powdery_mildew": {
                "keywords": ["powdery mildew", "white powder", "white spots on leaves", "mildew"],
                "title": "Controlling Powdery Mildew Organically",
                "response": (
                    "**Powdery Mildew Treatment:**\n\n"
                    "Powdery mildew appears as white, flour-like dusting on leaves and flourishes in warm, dry weather with high relative humidity.\n\n"
                    "**Proven Organic Solutions:**\n"
                    "1. **Potassium Bicarbonate / Baking Soda Spray:** Mix 1 tablespoon baking soda + 1/2 teaspoon vegetable oil + 1/2 teaspoon dish soap in 1 gallon water. The alkaline pH arrests fungal growth.\n"
                    "2. **Milk Spray (Highly Effective):** Mix **40% whole milk with 60% water**. The whey proteins produce natural antiseptics when exposed to sunlight. Spray every 7 days.\n"
                    "3. **Sulfur Dust or Spray:** Wettable sulfur is the agricultural gold standard for organic powdery mildew suppression (do not apply if temperature > 32°C / 90°F)."
                )
            }
        }

    def respond(self, query: str, context_scan: dict = None) -> dict:
        """
        Produce context-rich, actionable farming advisory response.
        """
        clean_q = query.strip()
        lower_q = clean_q.lower()

        # Check if user query refers to a specific disease in our database
        for d_id, d_data in DISEASE_DATABASE.items():
            disease_name_lower = d_data["disease_name"].lower()
            crop_name_lower = d_data["crop"].lower()

            if (disease_name_lower in lower_q) or (crop_name_lower in lower_q and ("blight" in lower_q or "rot" in lower_q or "spot" in lower_q or "rust" in lower_q or "disease" in lower_q or "treatment" in lower_q)):
                return {
                    "reply": (
                        f"### Diagnostic Guide: **{d_data['crop']} - {d_data['disease_name']}**\n\n"
                        f"**Pathogen:** {d_data['pathogen']} *(Severity: {d_data['severity']})*\n\n"
                        f"**Key Symptoms:**\n" + "\n".join([f"- {s}" for s in d_data['symptoms']]) + "\n\n"
                        f"**Recommended Conventional Treatment:**\n" + "\n".join([f"- {t}" for t in d_data['treatment_chemical']]) + "\n\n"
                        f"**Organic Treatment Options:**\n" + "\n".join([f"- {o}" for o in d_data['treatment_organic']]) + "\n\n"
                        f"**Preventative Practices:**\n" + "\n".join([f"- {p}" for p in d_data['prevention']])
                    ),
                    "suggested_questions": [
                        f"What organic spray works best for {d_data['crop']}?",
                        "How to make homemade neem oil spray?",
                        "How can I prevent fungal diseases using irrigation?"
                    ]
                }

        # Check if query matches common farming problem topics
        for topic_key, topic in self.common_topics.items():
            for kw in topic["keywords"]:
                if kw in lower_q:
                    return {
                        "reply": f"### {topic['title']}\n\n{topic['response']}",
                        "suggested_questions": [
                            "What is the best NPK fertilizer for fruiting?",
                            "How do I prevent blossom end rot?",
                            "How often should I water my crops?"
                        ]
                    }

        # Check if user asks about their recent scan result
        if context_scan and ("scan" in lower_q or "my leaf" in lower_q or "result" in lower_q or "this plant" in lower_q or "it" in lower_q):
            c_name = context_scan.get("disease_name", "Detected Condition")
            c_crop = context_scan.get("crop", "Plant")
            c_conf = context_scan.get("confidence_percentage", 90.0)
            c_id = context_scan.get("class_id", "")
            d_info = get_disease_info(c_id)

            return {
                "reply": (
                    f"### Context for Your Recent Scan: **{c_crop} ({c_name})**\n\n"
                    f"The analysis showed **{c_name}** with **{c_conf}% diagnostic confidence**.\n\n"
                    f"**Recommended immediate step:**\n"
                    f"- {d_info['treatment_organic'][0] if d_info.get('treatment_organic') else 'Isolate infected foliage.'}\n"
                    f"- {d_info['treatment_chemical'][0] if d_info.get('treatment_chemical') else 'Consult local agricultural extension.'}\n\n"
                    f"Would you like detailed preparation instructions for organic treatments or prevention strategies for next season?"
                ),
                "suggested_questions": [
                    f"Show full treatment plan for {c_name}",
                    "Is this disease contagious to other plants?",
                    "How to sanitize tools after pruning diseased plants?"
                ]
            }

        # General friendly agricultural response with helpful tips
        return {
            "reply": (
                "### PlantCare AI Farming Advisory\n\n"
                f"Hello! I am your **AI Farming Assistant**. I can help you diagnose crop conditions, suggest safe chemical and organic remedies, optimize irrigation, and improve soil fertility.\n\n"
                "**Here are popular topics I can assist with:**\n"
                "- **Disease Control:** Tomato Early/Late Blight, Apple Scab, Corn Rust, Powdery Mildew, Bacterial Spots.\n"
                "- **Organic Treatments:** Cold-pressed Neem oil, Bacillus subtilis, baking soda formulas, copper soaps.\n"
                "- **Plant Nutrition:** NPK fertilizer schedules, magnesium/calcium deficiencies, blossom end rot.\n"
                "- **Pest Protection:** Aphids, spider mites, thrips, whiteflies, and companion planting.\n\n"
                "*Tip: You can also upload a leaf photo in the **Detect Disease** tab, and ask me specific questions about the diagnosis!*"
            ),
            "suggested_questions": [
                "How to treat Tomato Late Blight organically?",
                "What causes yellow leaves on tomato plants?",
                "How to make an effective neem oil spray?",
                "What is the best watering schedule to avoid blight?"
            ]
        }

# Global singleton assistant
assistant_engine = FarmingAssistant()
