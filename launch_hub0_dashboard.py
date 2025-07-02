#!/usr/bin/env python3
"""
Hub0 Dashboard Launcher - Launches the dashboard for hub0 without camera dependencies
"""

from typing import List
from components import component
from box import box
from machine import machine
from Hub import Hub
from Queue import queue
from product import product
from productionstep import production_step
from hub_dashboard import HubDashboard

def create_hub0_data():
    """Create the same data structure as in main.py for hub0"""
    
    # Create the same components as in main.py
    components_list = [
        component(0, "Anker Typ 7"), 
        component(1, "Buerstenhalter"), 
        component(2, "Getriebedeckel Typ 6"),
        component(3, "Getriebehause typ 10"), 
        component(4, "Getriebehause typ 6"), 
        component(5, "Getriebehause typ 9"),
        component(6, "Magnet Lang"), 
        component(7, "Poltopf-Lang"), 
        component(8, "spange")
    ]
    
    # Create boxes exactly as in main.py
    boxes = [
        box([component(0, "Anker Typ 7"), component(1, "Buerstenhalter"), component(2, "Getriebedeckel Typ 6"),
             component(3, "Getriebehause typ 10"), component(4, "Getriebehause typ 6"), component(5, "Getriebehause typ 9"),
             component(6, "Magnet Lang"), component(7, "Poltopf-Lang"), component(8, "spange")]),
        box([component(6, "Magnet Lang"), component(7, "Poltopf-Lang"), component(8, "spange")])
    ]
    
    # Create machines exactly as in main.py
    machines = [
        machine(0, "Spritzguss Maschine", "Herstellung der Gehäuse für das Motorgetriebe", "offline"), 
        machine(1, "Kupferwickelmaschine", "Wicklung der Kupferdrähte für den Rotor", "offline")
    ]
    
    # Create production steps with needed components
    production_steps = [
        production_step("Spritzguss Getriebegehäuse", "Spritzguss der Getriebegehäuseteile", machines[0], 
                       [component(0, "Anker Typ 7"), component(1, "Buerstenhalter"), component(2, "Getriebedeckel Typ 6")]),
        production_step("Rotorwicklung", "Kupferwicklung des Rotors für den Motor", machines[1],
                       [component(0, "Anker Typ 7"), component(1, "Buerstenhalter"), component(2, "Getriebedeckel Typ 6")])
    ]
    
    # Create products exactly as in main.py
    products_in_production = [
        product("Motorgetriebe", production_steps,
                [component(0, "Anker Typ 7"), component(1, "Buerstenhalter"), component(2, "Getriebedeckel Typ 6")])
    ]
    
    # Create Hub0 exactly as in main.py
    hub0 = Hub(0, machines, [], queue(boxes[0]), [], products_in_production)
    
    return hub0

def main():
    """Main function to launch Hub0 dashboard"""
    print("=" * 60)
    print("       HUB 0 DASHBOARD LAUNCHER")
    print("=" * 60)
    print()
    
    print("Initializing Hub 0 data...")
    hub0 = create_hub0_data()
    
    print(f"✓ Hub 0 initialized successfully")
    print(f"  - Hub ID: {hub0.id}")
    print(f"  - Connected Machines: {len(hub0.machines)}")
    print(f"  - Products in Production: {len(hub0.products_in_production)}")
    print(f"  - Components in Queue: {len(hub0.queue.boxes.components) if hub0.queue.boxes else 0}")
    print()
    
    print("Starting Hub 0 Dashboard...")
    print("Dashboard Features:")
    print("  • Real-time machine status monitoring")
    print("  • Production progress tracking")
    print("  • Component queue management")
    print("  • Hub metrics and statistics")
    print("  • Control buttons for production management")
    print()
    print("The dashboard window will open now.")
    print("You can close this terminal window after the dashboard opens.")
    print()
    
    # Simulate some machine activity for demonstration
    if hub0.machines:
        hub0.machines[0].set_status("online")  # Turn on first machine
        print(f"✓ {hub0.machines[0].name} is now online")
    
    print("\nLaunching dashboard...")
    
    # Create and run the dashboard
    dashboard = HubDashboard(hub0)
    dashboard.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDashboard closed by user.")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please check that all required files are present and properly configured.")
