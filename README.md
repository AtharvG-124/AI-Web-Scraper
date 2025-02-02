# AI-Web-Scraper

to run the project: streamlit run main.py

Files:
parse.py: file is used to parse the data frin web page that the user inputs. It takes the dom content and organizes it using the Ollama LLM.
scrape.py: file is used to actually go through the inputed web page and scrape the data on the page. It gets the bare html from the page.
main.py: uses the functionality provided in parse.py and scrape.py to organize the data that has been scrpaed and provides the ui from streamlit library.

