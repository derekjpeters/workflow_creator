import tkinter as tk
from tkinter import filedialog
from graphviz import Digraph

def create_workflow_diagram():
    # Initialize the graph
    workflow = Digraph('workflow', format='png')

    # Add nodes
    workflow.node('A', 'Start')
    workflow.node('B', 'Task 1')
    workflow.node('C', 'Task 2')
    workflow.node('D', 'Task 3')
    workflow.node('E', 'End')

    # Add edges
    workflow.edges(['AB', 'BC', 'CD', 'DE'])

    # Render the graph
    output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if output_file:
        workflow.render(output_file, view=True)
        print(f"Workflow diagram saved as {output_file}")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Workflow Diagram Creator")

    # Create a button to generate the workflow diagram
    create_button = tk.Button(root, text="Create Workflow Diagram", command=create_workflow_diagram)
    create_button.pack(padx=10, pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()