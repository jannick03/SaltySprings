#!/usr/bin/env python3
"""
Test script for the Hub Dashboard without camera dependencies
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

def create_test_data():
    """Create sample data for testing the dashboard"""
    
    # Create sample components
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
    
    # Create sample boxes
    test_box = box(components_list[:3])  # First 3 components in the box
    
    # Create sample machines
    test_machines = [
        machine(0, "Spritzguss Maschine", "Herstellung der Gehäuse für das Motorgetriebe", "online"),
        machine(1, "Kupferwickelmaschine", "Wicklung der Kupferdrähte für den Rotor", "offline"),
        machine(2, "Montage Station", "Montage der Komponenten", "online")
    ]
    
    # Create sample production steps
    production_steps = [
        production_step("Spritzguss Getriebegehäuse", "Spritzguss der Getriebegehäuseteile", test_machines[0], components_list[:2]),
        production_step("Rotorwicklung", "Kupferwicklung des Rotors für den Motor", test_machines[1], components_list[2:4])
    ]
    
    # Create sample products
    test_products = [
        product("Motorgetriebe", production_steps, components_list[:3])
    ]
    
    # Create test hub
    test_hub = Hub(0, test_machines, [], queue(test_box), [], test_products)
    
    return test_hub

def main():
    """Main function to run the dashboard test"""
    print("Creating test data for Hub Dashboard...")
    
    # Create test hub with sample data
    test_hub = create_test_data()
    
    print(f"Test Hub created with ID: {test_hub.id}")
    print(f"Machines: {len(test_hub.machines)}")
    print(f"Products in production: {len(test_hub.products_in_production)}")
    
    print("\nLaunching Hub Dashboard...")
    print("The dashboard window should open shortly.")
    print("You can interact with the dashboard to monitor hub status.")
    print("Press Ctrl+C in this terminal to exit when done.")
    
    # Create and run the dashboard
    dashboard = HubDashboard(test_hub)
    dashboard.run()

if __name__ == "__main__":
    main()
