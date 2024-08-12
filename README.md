
## Prerequisites

Before running the project, you need to install the following Python packages:

- `customtkinter` for custom-styled tkinter widgets
- `pyodbc` for connecting to ODBC databases
- `CTkMessagebox` for connecting messageBox

You can install these dependencies using `pip`. Here's how:

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

### Installing the ODBC Driver

If you're using `pyodbc` to connect to SQL Server, you also need to install the ODBC driver. For SQL Server, download and install the [ODBC Driver 17 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server) or the version appropriate for your operating system.

### Running the Project

After installing the prerequisites, you can run the project with:

```sh
python handsOn.py
