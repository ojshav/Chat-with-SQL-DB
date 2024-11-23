# Chat with SQL DB

This project is a Streamlit application that allows users to interact with a SQL database using natural language queries. It leverages the power of the Langchain library and the Groq API to process and respond to user queries.

## Features

- Connect to either a local SQLite database or a MySQL database.
- Use natural language to query the database.
- Interactive chat interface powered by Streamlit.
- Supports both local and remote database configurations.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Langchain
- SQLAlchemy
- PyMySQL (for MySQL support)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your database:

   - For a local SQLite database, ensure `my_database.db` is in the project directory.
   - For a MySQL database, ensure you have the necessary credentials and access.

## Configuration

- Update the `LOCAL_DB_PATH` and `MYSQL_DB_PATH` in `app.py` with your database paths.
- Enter your Groq API key in the sidebar when running the application.

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run chat_Sql/app.py
   ```

2. Select the database type from the sidebar.
3. Enter the necessary credentials for MySQL if selected.
4. Start chatting with the database using the chat interface.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


![WhatsApp Image 2024-11-23 at 20 01 14_b763080e](https://github.com/user-attachments/assets/b993b5eb-bc77-4c0c-98d3-a23cf8744c88)
