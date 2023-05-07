![Binaryhood](Logo/BinaryhoodLogo.png)

# Flask Chatbot with Langchain and OpenAI GPT

This is a chatbot application built with Flask, Langchain, and OpenAI's GPT 3.5 turbo(ChatGPT) model. The chatbot can access the internet using DuckDuckGo and Wikipedia APIs, and can also run Python programs using Python REPL.

## Features

- Chat with the chatbot using natural language.
- The chatbot will get answers to questions using one or more of the following tools from the Python repl, DuckDuckGo and Wikipedia.
- Run Python programs using Python REPL.
- User-friendly interface.

## Installation

To install and run the application make sure you have Python and git installed on your computer then follow these steps:

1. Clone the repository to your local machine using `git clone https://github.com/Phunbie/Langchain-chat.git` on your terminal.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create an OpenAI API key and add it to your environment variables.
4. Run the application using `python main.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## Usage

To use the chatbot, follow these steps:

1. Type a message to the chatbot in the chat box and hit Enter.
2. Wait for the chatbot to respond.

Example chatbot commands:

- `Hello` - The chatbot will respond with a greeting.
- `What is the capital of France?` - The chatbot will search the internet for the answer.
- `search Who invented the internet?` - The chatbot will search DuckDuckGo for the answer.
- `wiki Who is Elon Musk?` - The chatbot will search Wikipedia for the answer.
- `python print("Hello, world!")` - The chatbot will run the Python program and return the output.

## Demo

[Click here](https://flask-chatbot-langchain.herokuapp.com/) to view a live demo of the application.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
