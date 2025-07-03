def get_recommendation(label):
    recommendations = {
        "Battery": "Do not throw in regular trash. Tape terminals.",
        "Keyboard": "Clean before disposal. Remove batteries if any.",
        "Microwave": "Do not open casing. Can contain capacitors with charge.",
        "Mobile Phone": "Wipe all personal data. Remove SIM and SD cards.",
        "Mouse": "Remove batteries. Clean and test for reuse before disposal.",
        "PCB": "Wear gloves. Do not burn or crush PCBs.",
        "Player": "Remove batteries. Test for reuse before discarding.",
        "Printer": "Remove ink cartridges before recycling.",
        "Television": "Do not try to open or fix cathode-ray TVs. Risk of electric shock.",
        "Washing Machine": "Remove all clothing and clean before pickup. Avoid dismantling.",
    }
    return recommendations.get(label, "Remove SIM and SD cards")
