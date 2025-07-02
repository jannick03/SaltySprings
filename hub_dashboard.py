import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
from typing import List
from components import component
from box import box
from machine import machine
from Hub import Hub
from Queue import queue
from product import product
from productionstep import production_step


class HubDashboard:
    def __init__(self, hub: Hub, root=None):
        self.hub = hub
        self.root = root if root else tk.Tk()
        self.root.title(f"Hub {self.hub.id} Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Variables for dynamic updates
        self.update_interval = 1000  # Update every 1 second
        
        self.setup_ui()
        self.start_updates()
    
    def setup_ui(self):
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill='x', padx=10, pady=(10, 0))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text=f"Hub {self.hub.id} Control Dashboard", 
                              font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Create main container with grid layout
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configure grid weights
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_rowconfigure(2, weight=1)
        
        # Create sections
        self.create_machines_section(main_container)
        self.create_products_section(main_container)
        self.create_queue_section(main_container)
        self.create_status_section(main_container)
        
        # Create control buttons
        self.create_control_buttons(main_container)
    
    def create_machines_section(self, parent):
        # Machines Status Section
        machines_frame = tk.LabelFrame(parent, text="Connected Machines", 
                                     font=('Arial', 12, 'bold'), bg='white', relief='raised')
        machines_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 5), pady=(0, 5))
        
        # Create treeview for machines
        columns = ('ID', 'Name', 'Function', 'Status')
        self.machines_tree = ttk.Treeview(machines_frame, columns=columns, show='headings', height=8)
        
        # Define headings
        for col in columns:
            self.machines_tree.heading(col, text=col)
            self.machines_tree.column(col, width=120)
        
        # Add scrollbar
        machines_scrollbar = ttk.Scrollbar(machines_frame, orient='vertical', command=self.machines_tree.yview)
        self.machines_tree.configure(yscrollcommand=machines_scrollbar.set)
        
        self.machines_tree.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        machines_scrollbar.pack(side='right', fill='y', pady=10)
    
    def create_products_section(self, parent):
        # Products in Production Section
        products_frame = tk.LabelFrame(parent, text="Products in Production", 
                                     font=('Arial', 12, 'bold'), bg='white', relief='raised')
        products_frame.grid(row=0, column=1, sticky='nsew', padx=(5, 0), pady=(0, 5))
        
        # Create treeview for products
        columns = ('ID', 'Name', 'Current Step', 'Progress')
        self.products_tree = ttk.Treeview(products_frame, columns=columns, show='headings', height=8)
        
        # Define headings
        for col in columns:
            self.products_tree.heading(col, text=col)
            self.products_tree.column(col, width=120)
        
        # Add scrollbar
        products_scrollbar = ttk.Scrollbar(products_frame, orient='vertical', command=self.products_tree.yview)
        self.products_tree.configure(yscrollcommand=products_scrollbar.set)
        
        self.products_tree.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        products_scrollbar.pack(side='right', fill='y', pady=10)
    
    def create_queue_section(self, parent):
        # Queue Section
        queue_frame = tk.LabelFrame(parent, text="Component Queue", 
                                  font=('Arial', 12, 'bold'), bg='white', relief='raised')
        queue_frame.grid(row=1, column=0, sticky='nsew', padx=(0, 5), pady=5)
        
        # Queue display
        self.queue_text = scrolledtext.ScrolledText(queue_frame, height=10, width=50, 
                                                   font=('Courier', 10), bg='#f8f9fa')
        self.queue_text.pack(fill='both', expand=True, padx=10, pady=10)
    
    def create_status_section(self, parent):
        # Hub Status Section
        status_frame = tk.LabelFrame(parent, text="Hub Status & Metrics", 
                                   font=('Arial', 12, 'bold'), bg='white', relief='raised')
        status_frame.grid(row=1, column=1, sticky='nsew', padx=(5, 0), pady=5)
        
        # Status metrics
        metrics_frame = tk.Frame(status_frame, bg='white')
        metrics_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create status labels
        self.status_labels = {}
        
        # Hub ID
        tk.Label(metrics_frame, text="Hub ID:", font=('Arial', 10, 'bold'), 
                bg='white', anchor='w').grid(row=0, column=0, sticky='w', pady=2)
        self.status_labels['hub_id'] = tk.Label(metrics_frame, text=str(self.hub.id), 
                                               font=('Arial', 10), bg='white', anchor='w')
        self.status_labels['hub_id'].grid(row=0, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Total Machines
        tk.Label(metrics_frame, text="Total Machines:", font=('Arial', 10, 'bold'), 
                bg='white', anchor='w').grid(row=1, column=0, sticky='w', pady=2)
        self.status_labels['total_machines'] = tk.Label(metrics_frame, text="0", 
                                                       font=('Arial', 10), bg='white', anchor='w')
        self.status_labels['total_machines'].grid(row=1, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Active Machines
        tk.Label(metrics_frame, text="Active Machines:", font=('Arial', 10, 'bold'), 
                bg='white', anchor='w').grid(row=2, column=0, sticky='w', pady=2)
        self.status_labels['active_machines'] = tk.Label(metrics_frame, text="0", 
                                                        font=('Arial', 10), bg='white', anchor='w')
        self.status_labels['active_machines'].grid(row=2, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Products in Production
        tk.Label(metrics_frame, text="Products in Production:", font=('Arial', 10, 'bold'), 
                bg='white', anchor='w').grid(row=3, column=0, sticky='w', pady=2)
        self.status_labels['products_count'] = tk.Label(metrics_frame, text="0", 
                                                       font=('Arial', 10), bg='white', anchor='w')
        self.status_labels['products_count'].grid(row=3, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Queue Size
        tk.Label(metrics_frame, text="Queue Size:", font=('Arial', 10, 'bold'), 
                bg='white', anchor='w').grid(row=4, column=0, sticky='w', pady=2)
        self.status_labels['queue_size'] = tk.Label(metrics_frame, text="0", 
                                                   font=('Arial', 10), bg='white', anchor='w')
        self.status_labels['queue_size'].grid(row=4, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Hub Status
        tk.Label(metrics_frame, text="Hub Status:", font=('Arial', 10, 'bold'), 
                bg='white', anchor='w').grid(row=5, column=0, sticky='w', pady=2)
        self.status_labels['hub_status'] = tk.Label(metrics_frame, text="Active", 
                                                   font=('Arial', 10), bg='white', anchor='w', fg='green')
        self.status_labels['hub_status'].grid(row=5, column=1, sticky='w', padx=(10, 0), pady=2)
    
    def create_control_buttons(self, parent):
        # Control Buttons Section
        controls_frame = tk.Frame(parent, bg='#f0f0f0')
        controls_frame.grid(row=2, column=0, columnspan=2, sticky='ew', pady=(10, 0))
        
        # Refresh button
        refresh_btn = tk.Button(controls_frame, text="Refresh Data", command=self.refresh_data,
                               bg='#3498db', fg='white', font=('Arial', 10, 'bold'),
                               relief='raised', borderwidth=2)
        refresh_btn.pack(side='left', padx=(0, 10))
        
        # Start/Stop Production button
        self.production_btn = tk.Button(controls_frame, text="Start Production", 
                                       command=self.toggle_production,
                                       bg='#27ae60', fg='white', font=('Arial', 10, 'bold'),
                                       relief='raised', borderwidth=2)
        self.production_btn.pack(side='left', padx=(0, 10))
        
        # Add Product button
        add_product_btn = tk.Button(controls_frame, text="Add Product to Queue", 
                                   command=self.add_product_dialog,
                                   bg='#f39c12', fg='white', font=('Arial', 10, 'bold'),
                                   relief='raised', borderwidth=2)
        add_product_btn.pack(side='left', padx=(0, 10))
        
        # Export Report button
        export_btn = tk.Button(controls_frame, text="Export Report", 
                              command=self.export_report,
                              bg='#8e44ad', fg='white', font=('Arial', 10, 'bold'),
                              relief='raised', borderwidth=2)
        export_btn.pack(side='left')
    
    def update_dashboard(self):
        """Update all dashboard sections with current data"""
        self.update_machines_display()
        self.update_products_display()
        self.update_queue_display()
        self.update_status_display()
    
    def update_machines_display(self):
        """Update the machines treeview"""
        # Clear existing items
        for item in self.machines_tree.get_children():
            self.machines_tree.delete(item)
        
        # Add current machines
        if hasattr(self.hub, 'machines') and self.hub.machines:
            for machine in self.hub.machines:
                status_color = 'green' if machine.status == 'online' else 'red'
                self.machines_tree.insert('', 'end', values=(
                    machine.mashine_id,
                    machine.name, 
                    machine.funktion, 
                    machine.status
                ), tags=(machine.status,))
            
            # Configure tags for coloring
            self.machines_tree.tag_configure('online', background='#d5f4e6')
            self.machines_tree.tag_configure('offline', background='#f8d7da')
    
    def update_products_display(self):
        """Update the products treeview"""
        # Clear existing items
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)
        
        # Add current products
        if hasattr(self.hub, 'products_in_production') and self.hub.products_in_production:
            for product in self.hub.products_in_production:
                current_step = product.current_step.name if hasattr(product.current_step, 'name') else str(product.current_step)
                progress = f"{product.current_step}/{len(product.production_steps)}" if hasattr(product, 'production_steps') else "N/A"
                
                self.products_tree.insert('', 'end', values=(
                    product.id,
                    product.name,
                    current_step,
                    progress
                ))

    def update_queue_display(self):
        """Update the queue text display"""
        self.queue_text.delete('1.0', tk.END)

        if len(self.hub.queue) == 0:
            print("Hier")
            self.queue_text.insert(tk.END, "❌ No queue data available\n")

        for i, scanned_box in enumerate(self.hub.queue[-10:]):  # last 10 scanned boxes
            print("OK")
            comp_names = ", ".join([comp.name for comp in scanned_box.components])
            self.queue_text.insert(tk.END, f"Box {i + 1}: {comp_names}\n")

    def update_status_display(self):
        """Update the status metrics"""
        # Update Hub ID
        self.status_labels['hub_id'].config(text=str(self.hub.id))
        
        # Update machine counts
        total_machines = len(self.hub.machines) if hasattr(self.hub, 'machines') and self.hub.machines else 0
        active_machines = len([m for m in self.hub.machines if m.status == 'online']) if hasattr(self.hub, 'machines') and self.hub.machines else 0
        
        self.status_labels['total_machines'].config(text=str(total_machines))
        self.status_labels['active_machines'].config(text=str(active_machines))
        
        # Update products count
        products_count = len(self.hub.products_in_production) if hasattr(self.hub, 'products_in_production') and self.hub.products_in_production else 0
        self.status_labels['products_count'].config(text=str(products_count))
        
        # Update queue size
        queue_size = 0
        if hasattr(self.hub, 'queue') and self.hub.queue and hasattr(self.hub.queue, 'boxes'):
            if isinstance(self.hub.queue.boxes, list):
                # Count total components in all boxes
                for box in self.hub.queue.boxes:
                    if hasattr(box, 'components') and box.components:
                        queue_size += len(box.components)
            else:
                # Single box case
                if hasattr(self.hub.queue.boxes, 'components') and self.hub.queue.boxes.components:
                    queue_size = len(self.hub.queue.boxes.components)
        self.status_labels['queue_size'].config(text=str(queue_size))
        
        # Update hub status based on active machines
        if active_machines > 0:
            self.status_labels['hub_status'].config(text="Active", fg='green')
        else:
            self.status_labels['hub_status'].config(text="Idle", fg='orange')
    
    def refresh_data(self):
        """Manually refresh all data"""
        self.update_dashboard()
        print(f"Dashboard refreshed for Hub {self.hub.id}")
    
    def toggle_production(self):
        """Toggle production start/stop"""
        current_text = self.production_btn.cget('text')
        if current_text == "Start Production":
            self.production_btn.config(text="Stop Production", bg='#e74c3c')
            print(f"Production started for Hub {self.hub.id}")
        else:
            self.production_btn.config(text="Start Production", bg='#27ae60')
            print(f"Production stopped for Hub {self.hub.id}")
    
    def add_product_dialog(self):
        """Open dialog to add product to queue"""
        # Simple dialog for demonstration
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Product")
        dialog.geometry("300x200")
        dialog.configure(bg='white')
        
        tk.Label(dialog, text="Add Product to Production Queue", 
                font=('Arial', 12, 'bold'), bg='white').pack(pady=10)
        
        tk.Label(dialog, text="Product Name:", bg='white').pack()
        name_entry = tk.Entry(dialog, width=30)
        name_entry.pack(pady=5)
        
        def add_product():
            name = name_entry.get()
            if name:
                print(f"Product '{name}' would be added to Hub {self.hub.id} queue")
                dialog.destroy()
                self.refresh_data()
        
        tk.Button(dialog, text="Add Product", command=add_product, 
                 bg='#3498db', fg='white').pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy, 
                 bg='#7f8c8d', fg='white').pack()
    
    def export_report(self):
        """Export hub status report"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"hub_{self.hub.id}_report_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Hub {self.hub.id} Status Report\n")
            f.write("=" * 40 + "\n")
            f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("Machines:\n")
            if hasattr(self.hub, 'machines') and self.hub.machines:
                for machine in self.hub.machines:
                    f.write(f"  - {machine.name} (ID: {machine.mashine_id}): {machine.status}\n")
            
            f.write(f"\nProducts in Production: {len(self.hub.products_in_production) if hasattr(self.hub, 'products_in_production') and self.hub.products_in_production else 0}\n")
            
            if hasattr(self.hub, 'products_in_production') and self.hub.products_in_production:
                for product in self.hub.products_in_production:
                    f.write(f"  - {product.name} (ID: {product.id})\n")
        
        print(f"Report exported to {filename}")
    
    def start_updates(self):
        """Start automatic updates"""
        self.update_dashboard()
        self.root.after(self.update_interval, self.start_updates)
    
    def run(self):
        """Start the dashboard"""
        self.root.update()
        self.update_dashboard()


# Function to create dashboard from main.py
def create_hub_dashboard(hub, run_in_thread=False):
    """Create and optionally run hub dashboard"""
    if run_in_thread:
        def run_dashboard():
            dashboard = HubDashboard(hub)
            dashboard.run()
        
        dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
        dashboard_thread.start()
        return dashboard_thread
    else:
        dashboard = HubDashboard(hub)
        return dashboard


if __name__ == "__main__":
    # Example usage - create sample data for testing
    components_list = [
        component(0, "Anker Typ 7"), 
        component(1, "Buerstenhalter"), 
        component(2, "Getriebedeckel Typ 6")
    ]
    
    sample_box = box(components_list)
    sample_machines = [
        machine(0, "Spritzguss Maschine", "Herstellung der Gehäuse", "online"),
        machine(1, "Kupferwickelmaschine", "Wicklung der Kupferdrähte", "offline")
    ]
    
    sample_products = [
        product("Motorgetriebe", 
                [production_step("Spritzguss", "Spritzguss der Teile", sample_machines[0])], 
                components_list)
    ]
    
    sample_hub = Hub(0, sample_machines, [], queue(sample_box), sample_products)
    
    # Create and run dashboard
    dashboard = HubDashboard(sample_hub)
    dashboard.run()
