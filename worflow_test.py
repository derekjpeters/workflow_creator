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
    workflow.render('workflow_diagram', view=True)

if __name__ == '__main__':
    create_workflow_diagram()