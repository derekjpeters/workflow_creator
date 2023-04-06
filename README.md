# Workflow Diagram Creator

This Python script allows you to create a simple workflow diagram using `tkinter` and `graphviz` libraries. The user can enter tasks in the application window, and the script will generate a directed graph displaying the workflow.

## Dependencies

- Python 3
- tkinter - Is installed
- graphviz

To install the `graphviz` & library, run the following command:

## Install
- pip3 install graphviz

Note: If you are using a Windows system and the `pip3` command is not recognized, try using `pip` instead:

The application window will open. Enter the task names in the "Tasks:" input field and press the "+" button or the "Enter" key to add them to the workflow.

Click the "Create Workflow Diagram" button to generate the workflow diagram.

A file dialog will open, asking you to specify a location and a file name to save the diagram as a PNG image. Choose the desired location and

## Running the Application
To run the Workflow Diagram Creator, follow these steps:

Windows
- Open File Explorer and navigate to the dist directory containing the workflowcreator executable.
- Double-click the workflowcreator.exe file to launch the application.
macOS and Linux
- Open a terminal window.
- Change to the dist directory containing the workflowcreator executable using the cd command. For example:
bash
- Copy code
- cd /path/to/dist/directory
- Make sure to replace /path/to/dist/directory with the actual path to your dist directory.

Give the workflowcreator file execute permissions (if not already executable):
bash
Copy code
`chmod +x workflowcreator`
Run the workflowcreator executable:
bash
Copy code
`./workflowcreator`
This will launch the application.

### Using the Workflow Diagram Creator
- Enter a task name in the "Tasks" input box.
- Press Enter or click the "+" button to add the task to the list.
- Repeat steps 1-2 to add more tasks as needed.
- Click the "Create Workflow Diagram" button to generate a workflow diagram with the listed tasks.
- Choose a location to save the generated diagram as a PNG file.
- To clear the tasks list, click the "Clear Tasks" button.