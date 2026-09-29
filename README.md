# Climate Newsletter Crew

A command-line app built with CrewAI where a team of seven agents researches a climate topic and turns it into a newsletter. The agents run as a sequential pipeline and every step's output is saved to the `logs/` folder.

## Features

- Asks for a climate topic on the command line. You can include a word count in the prompt; otherwise the newsletter aims for about 400 words.
- **Researcher** searches the web (Serper) for around five recent, relevant articles and lists each with a title, short summary and URL.
- **Climate journalist** writes a newsletter from the research: welcome message, table of contents, 5-6 sections and references.
- **Data analyst** can use a custom chart tool (pandas + seaborn) that saves a line chart to `charts.pdf`.
- **Editor** polishes the draft: rewrites titles, reorders the content and drops off-topic items.
- **Subject matter expert** reviews the technical accuracy and suggests additions.
- **Critic** scores each article out of 10 and checks the citations and sources.
- **SEO specialist** produces a search-optimised final version of the newsletter.

All agents are set up with GPT-4 (`ChatOpenAI` from `langchain-openai`, temperature 0.7).

## Pipeline

Tasks run in this order: research, writing, data analysis, editing, expert review, critique, SEO. Writing and data analysis both work from the research report, editing works from the journalist's draft, and the expert review, critique and SEO steps each build on the step before.

## Tech stack

- Python
- CrewAI and crewai-tools (`SerperDevTool`, `FileReadTool`)
- LangChain / langchain-openai (GPT-4)
- pandas, matplotlib, seaborn
- python-decouple for loading API keys from `.env`

## Project structure

```
.
├── main.py                 # entry point: asks for a topic and runs the crew
├── agents.py               # agent roles, goals and backstories
├── tasks.py                # task instructions, expected output and log file for each step
├── tools/
│   ├── file_write.py       # write-file tool
│   ├── directory_write.py  # create-directory tool
│   └── data_viz.py         # chart tool that saves charts.pdf
├── logs/                   # output of each task
├── requirements.txt
└── .env.example
```

## Setup

You need Python 3.10 or 3.11, an OpenAI API key and a [Serper](https://serper.dev) API key.

```bash
python -m venv venv
venv\Scripts\activate         # Windows
# source venv/bin/activate    # macOS / Linux

pip install -r requirements.txt
```

Copy `.env.example` to `.env` in the project root and add your keys:

```
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key
```

`requirements.txt` pins CrewAI 0.76 and crewai-tools 0.13 because the code uses the older tool style (`crewai_tools.tool`, LangChain tools and a LangChain chat model), which later releases changed. A few of their dependencies are pinned too so pip resolves quickly, and setuptools stays below 81 because this CrewAI release still imports `pkg_resources`.

## Usage

```bash
python main.py
```

Type a topic when asked, for example `Carbon removal technologies, around 400 words`. The crew prints its progress and the final result to the terminal and saves each step to `logs/`:

| File | Step |
| --- | --- |
| `logs/research_agent.txt` | research report |
| `logs/writing_agent.txt` | first newsletter draft |
| `logs/data_agent.txt` | data analysis |
| `logs/editor_agent.txt` | edited newsletter |
| `logs/review_agent.txt` | subject matter expert review |
| `logs/critique_agent.txt` | scores and feedback |
| `logs/seo_agent.txt` | SEO-optimised newsletter |

The files currently in `logs/` are from earlier test runs on carbon removal and carbon credit topics. A new run overwrites them.

## License

MIT. See [LICENSE](LICENSE).
