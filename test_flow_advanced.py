import tkinter as tk
from tkinter import filedialog
from graphviz import Digraph

def create_workflow_diagram(tasks, shape='rect'):
    # Initialize the graph
    workflow = Digraph('workflow', format='png')

    # Add nodes
    for task in tasks:
        workflow.node(task, task, shape=shape)

    # Add edges
    for i in range(len(tasks) - 1):
        workflow.edge(tasks[i], tasks[i + 1])

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
    tasks_entry = tk.Entry(root, width=30)
    tasks_entry.grid(row=0, column=1, padx=10, pady=10)

    tasks = ["Start", "End"]

    # Function to add a task
    def add_task():
        new_task = tasks_entry.get().strip()
        if new_task:
            tasks.insert(-1, new_task)
            tasks_entry.delete(0, tk.END)
            tasks_var.set(', '.join(tasks))

    # Add button to add a new task
    add_button = tk.Button(root, text="+", command=add_task)
    add_button.grid(row=0, column=2, padx=10, pady=10)

    # Display the current list of tasks
    tasks_var = tk.StringVar()
    tasks_var.set(', '.join(tasks))
    tasks_list = tk.Label(root, textvariable=tasks_var)
    tasks_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Function to generate the diagram
    def generate_diagram():
        create_workflow_diagram(tasks)

    # Create a button to generate the workflow diagram
    create_button = tk.Button(root, text="Create Workflow Diagram", command=generate_diagram)
    create_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()