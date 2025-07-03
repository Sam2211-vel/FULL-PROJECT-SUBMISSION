def estimate_cost(label):
    cost_map = {
        "Battery": 50,
        "Keyboard": 200,
        "Microwave": 2200,
        "Mobile Phone": 1000,
        "Mouse": 150,
        "PCB": 500,
        "Player": 600,
        "Printer": 800,
        "Television": 2500,
        "Washing Machine": 3500,
    }
    return cost_map.get(label, 100)
