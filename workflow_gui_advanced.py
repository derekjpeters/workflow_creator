import tkinter as tk
from tkinter import filedialog
from graphviz import Digraph

def create_workflow_diagram(tasks, edges):
    # Initialize the graph
    workflow = Digraph('workflow', format='png')

    # Add nodes
    for task in tasks:
        workflow.node(task, task)

    # Add edges
    for edge in edges:
        workflow.edge(edge[0], edge[1])

    # Render the graph
    output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if output_file:
        workflow.render(output_file, view=True)
        print(f"Workflow diagram saved as {output_file}")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Workflow Diagram Creator")

    # Create the tasks list
    tasks_label = tk.Label(root, text="Tasks:")
    tasks_label.grid(row=0, column=0, padx=10, pady=10)
    tasks_entry = tk.Entry(root, width=40)
    tasks_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create the edges list
    edges_label = tk.Label(root, text="Edges:")
    edges_label.grid(row=1, column=0, padx=10, pady=10)
    edges_entry = tk.Entry(root, width=40)
    edges_entry.grid(row=1, column=1, padx=10, pady=10)

    # Function to generate the diagram
    def generate_diagram():
        tasks = tasks_entry.get().split(',')
        edges = [edge.strip().split('-') for edge in edges_entry.get().split(',')]
        create_workflow_diagram(tasks, edges)

    # Create a button to generate the workflow diagram
    create_button = tk.Button(root, text="Create Workflow Diagram", command=generate_diagram)
    create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()