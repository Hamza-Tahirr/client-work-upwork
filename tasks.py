from crewai import Task
from textwrap import dedent

class NewsletterTasks:
  def __tip_section(self):
      return "Produce the highest quality work to ensure our newsletter is informative, engaging, and impactful!"

  def research_task(self, agent, tools, user_input):
      return Task(
          description=dedent(f"""
              You are a world-class climate journalist, researcher, and tech expert. 
              Your task is to gather the most interesting, relevant, and useful articles on: {user_input}.
              Focus on recent developments and ensure all sources are reliable and reputable.
              Include around 5 articles.
              {self.__tip_section()}
          """),
          expected_output="""
          A comprehensive research report with verified data and sources. 
          Name of the file: ResearchReport.txt
          Each news story should contain the following:
          - Title of the news
          - Summary of the news (Around 50 words)
          - URL of the article where the news was found

          Here is an example of the format of a news article that you could include in the document:
          
          <EXAMPLE>
            Story 1:
            - Title: **Daily briefing: AI now beats humans at basic reading and maths**
            - **Summary:** AI systems can now nearly match and sometimes exceed human performance in basic tasks. The report discusses the need for new benchmarks to assess AI capabilities and highlights the ethical considerations for AI models.
            - **URL:** [Nature Article](https://www.nature.com/articles/d41586-024-01125-1)
          </EXAMPLE>
          """,
          agent=agent,
          tools=tools,
          output_file="logs/research_agent.txt"
      )
  def writing_task(self, agent, tools, context, user_input):
      return Task(
          description=dedent(f"""
              As a world-class climate journalist, researcher, and newsletter writer, 
              your task is to write engaging and informative newsletters based on the research report provided.
              Ensure the content is accurate, clear, and accessible to our target audience.
              Include relevant in-text citations for all factual claims.

              Take a look at the word count and actual input given by the user: {user_input}.
              If the word count is not given, make sure it is around 400 words.
              {self.__tip_section()}
          """),
          expected_output="""
          Well-written newsletter with proper citations and engaging content. 
          Name of the file: Newsletter.txt
          This should be the format of the final newsletter:
          - Welcome Message and a description explaining the about the newsletter service.
          - Table of Contents. Table of content should be consisting of the 5-6 sections present in the body.
          - The body should be divided into 5-6 sections. All the content from the research report must be summarized and shown. (Very Important)
          Remember, The body should not contain summary of each article, but should be a generalized summary of all the articles. 
          - References and Citations.            
          """,
          agent=agent,
          tools=tools,
          context=context,
          output_file="logs/writing_agent.txt"
      )  
  def editing_task(self, agent, tools, context, user_input):
      return Task(
          description=dedent(f"""
              As a world-class climate journalist and editor, 
              your task is to review and refine the articles written by the journalists.
              Ensure clarity, accuracy, and consistency in tone and style across all pieces.
              Check for and correct any grammatical or factual errors.

              Keep in mind the following:
              - Rewrite the title of each news article to make it more engaging and interesting for the newsletter readers.
              - Add a paragraph to each news article explaining its importance and potential impact on the readers.
              - Reorder the bullet points to prioritize the most relevant and important news and topics at the top.
              - Verify that each news article is directly related to {user_input} and remove any off-topic articles.
              - Ensure that the URLs are correct and lead directly to the specific news article, not to a list of articles or the front page of a website. If a URL is incorrect, request the correct URL from the researcher.
              - Do not search for additional news articles or alter the content of the existing news articles. Only edit the provided articles.

              Take a look at the word count and actual input given by the user: {user_input}.
              If the word count is not given, make sure it is around 400 words.
              {self.__tip_section()}
          """),
          expected_output="""
          Polished newsletter ready for final review. 
          Name of the file: Editor.txt 

          This should be the format of the final newsletter:
          - Welcome Message and a description explaining the about the newsletter service.
          - Table of Contents.
          - The body should be divided into 6 sections. All the content from the research report must be summarized and shown. (Very Important)
          - References and Citations.           
          """,
          agent=agent,
          tools=tools,
          context=context,
          output_file="logs/editor_agent.txt"
      )

  def data_analysis_task(self, agent, tools, context):
      return Task(
          description=dedent(f"""
              Analyze climate data and trends relevant to the articles.
              Create clear and informative visualizations (graphs, charts) to illustrate key points.
              Ensure all data representations are accurate and easy to understand.
              {self.__tip_section()}
          """),
            expected_output='Data visualizations and analysis to complement the articles. Name of the file: DataAnalysis.txt and save the charts as well as pdf',
          agent=agent,
          tools=tools,
          context=context,
          output_file="logs/data_agent.txt"

      )

  def critique_task(self, agent, tools, context, user_input):
      return Task(
          description=dedent(f"""
              Review the quality of each article and score it out of 10.
              Ensure all articles have proper in-text citations and verify the reliability of sources.
              Provide constructive feedback for improvements if necessary.

              Take a look at the word count and actual input given by the user: {user_input}
              {self.__tip_section()}
          """),
          expected_output='Quality scores and detailed feedback for each article.',
          agent=agent,
          tools=tools,
          context=context,
          output_file="logs/critque_agent.txt"
      )

  def seo_optimization_task(self, agent, tools, context, user_input):
      return Task(
          description=dedent(f"""
              Optimize the content for search engines to improve visibility.
              Implement relevant keywords and SEO strategies without compromising readability.
              Ensure all meta descriptions and titles are optimized for search.
              {self.__tip_section()}

              Take a look at the word count and actual input given by the user: {user_input}.
              If the word count is not given, make sure it is around 400 words.
          """),
          expected_output="""
              SEO-optimized versions of the EditorReport and metadata. 
              Name of the file: SEO_OptimizedNewsletter.txt
              This should be the format of the final newsletter
              - Welcome Message and a description explaining the about the newsletter service.
              - Table of Contents.
              - The body should be divided into 6 sections. All the content from the research report must be summarized and shown. (Very Important)
              - References and Citations.     

          """,
          agent=agent,
          tools=tools,
          context=context,
          output_file="logs/seo_agent.txt"

      )

  def expert_review_task(self, agent, tools, context):
      return Task(
          description=dedent(f"""
              Review the articles from the perspective of a subject matter expert in climate science.
              Provide in-depth insights and ensure all technical information is accurate and up-to-date.
              Suggest any additional points or clarifications that would enhance the articles.
              {self.__tip_section()}
          """),
          expected_output='Expert feedback and additional insights for each article.',
          agent=agent,
          tools=tools,
          context=context,
          output_file="logs/review_agent.txt"

      )
