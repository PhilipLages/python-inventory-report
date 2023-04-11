# Inventory Report

This project was developed as a requirement of the Web Development Course at Trybe, in the Computer Science module. It generates a report based on inventory data. The report can be generated in two versions: simple and complete. The project applies Object-Oriented Programming (OOP) concepts, design patterns, and file I/O operations with CSV, JSON, and XML files.

## Installation

1.  Clone the repository to your local machine.

2.  Create a virtual environment for the project using the command:
    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```
 
3.  Install the required dependencies using the command:
    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```
	 
4.  Install the project as a pip package using the command:
    ```bash
    pip install
    ```
6.  Run the project with the command `inventory_report` followed by the required arguments.

## Usage

To generate a report, the project reads inventory data from CSV, JSON, or XML files. The files should be located in the `data` folder. The report can be generated in two versions:

### Simple report

To generate a simple report, run the following command:
```bash
inventory_report <file_path> simples
```

Replace `<file_path>` with the path of the input file.

### Complete report

To generate a complete report, run the following command:
```bash
inventory_report <file_path> completo
```

Replace `<file_path>` with the path of the input file.

Alternatively, you can invoke the command using Python as follows:
```bash
python3 -m inventory_report.main <file_path> <report_type>
```

Replace `<file_path>` with the path of the input file and `<report_type>` with either "simple" or "complete".

## Contributing

If you want to contribute to this project, please follow these steps:

1.  Fork this repository.
2.  Create a new branch with your feature or bug fix.
3.  Commit your changes.
4.  Push your branch to your forked repository.
5.  Create a pull request to the original repository.