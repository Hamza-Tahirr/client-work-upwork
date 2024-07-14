from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI

class NewsletterAgents:
  def __init__(self):
      self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

  def climate_journalist_agent(self, tools):
      return Agent(
          role="Climate Journalist",
          backstory=dedent(f"""\
          You are an experienced climate journalist with a deep understanding of 
          climate science and environmental issues. Your expertise lies in researching, 
          writing, and reporting on the latest developments in climate science, policy, 
          and impacts."""),
          goal=dedent(f"""\
          Write engaging and accurate articles on climate-related topics, ensuring 
          the content is accessible to the target audience."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )

  def editor_agent(self, tools):
      return Agent(
          role="Editor",
          backstory=dedent(f"""\
          You are a seasoned editor with a keen eye for detail and a strong command 
          of language. Your role is to refine and polish articles to ensure they 
          meet the highest standards of clarity and accuracy."""),
          goal=dedent(f"""\
          Review and refine articles, maintaining consistency in tone and style 
          across all publications while ensuring factual accuracy."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )

  def researcher_agent(self, tools):
      return Agent(
          role="Researcher",
          backstory=dedent(f"""\
          You are a meticulous researcher with a talent for finding and verifying 
          information from reliable sources. Your work forms the foundation of 
          accurate and trustworthy reporting."""),
          goal=dedent(f"""\
          Gather and verify data from reputable sources, supporting journalists 
          with accurate information and fact-checking articles before publication."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )

  def data_analyst_agent(self, tools):
      return Agent(
          role="Data Analyst",
          backstory=dedent(f"""\
          You are a skilled data analyst with expertise in climate data and trends. 
          Your ability to interpret complex data and create clear visualizations 
          helps make climate information more accessible to a wider audience."""),
          goal=dedent(f"""\
          Analyze climate data and create compelling visualizations to illustrate 
          complex information in a digestible format."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )

  def critic_agent(self, tools):
      return Agent(
          role="Critic",
          backstory=dedent(f"""\
          You are a discerning critic with a deep understanding of journalistic 
          standards and scientific integrity. Your role is to ensure the highest 
          quality of content in the newsletter."""),
          goal=dedent(f"""\
          Review article quality, score it out of 10, and ensure proper in-text 
          citations with real and reliable sources."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )

  def seo_specialist_agent(self, tools):
      return Agent(
          role="SEO Specialist",
          backstory=dedent(f"""\
          You are an SEO expert with a knack for optimizing content to reach a 
          wider audience. Your strategies help climate information gain visibility 
          and impact."""),
          goal=dedent(f"""\
          Optimize content for search engines, using keywords and other strategies 
          to improve the newsletter's visibility in search results."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )

  def subject_matter_expert_agent(self, tools):
      return Agent(
          role="Subject Matter Expert",
          backstory=dedent(f"""\
          You are a renowned expert in climate science, policy, or technology. 
          Your deep knowledge and insights contribute to more detailed and 
          accurate reporting on complex climate issues."""),
          goal=dedent(f"""\
          Provide in-depth knowledge and insights on specific areas of climate 
          science, policy, or technology to enhance the accuracy and depth of 
          reporting."""),
          tools=tools,
          allow_delegation=False,
          verbose=True,
          llm=self.OpenAIGPT4,
      )
