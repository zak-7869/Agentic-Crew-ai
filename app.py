import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import BaseTool

# 1. Setup Groq LLM Configuration
# Using Llama 3.3 70B for high-quality reasoning on Groq's LPU
groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.2
)

# 2. Define a Custom Tool
class MyCustomSearchTool(BaseTool):
    name: str = "Internal Database Search"
    description: str = "Search for specific proprietary company data regarding 2026 tech trends."

    def _run(self, query: str) -> str:
        # Here you would add your actual logic (API call, DB query, etc.)
        return f"Found relevant data for '{query}': AI agents are now standard in 85% of enterprises as of April 2026."

custom_tool = MyCustomSearchTool()

# 3. Define Agents
researcher = Agent(
    role='Senior Trend Researcher',
    goal='Uncover the latest advancements in {topic}',
    backstory="""You are a specialist in technical scouting. Your expertise lies in 
    finding deep-source information that others miss.""",
    tools=[custom_tool],
    llm=groq_llm,
    verbose=True
)

summarizer = Agent(
    role='Lead Content Strategist',
    goal='Create a concise executive summary from the research findings',
    backstory="""You excel at distilling complex technical jargon into 
    clear, actionable insights for C-suite executives.""",
    llm=groq_llm,
    verbose=True
)

# 4. Define Tasks
research_task = Task(
    description='Conduct a thorough investigation into {topic} using available tools.',
    expected_output='A detailed report covering 3 major breakthroughs and their impacts.',
    agent=researcher
)

summary_task = Task(
    description='Summarize the research report into a 3-bullet point executive brief.',
    expected_output='A 150-word executive summary in Markdown format.',
    agent=summarizer,
    context=[research_task] # Passes the output of research_task to the summarizer
)

# 5. Form the Crew
tech_crew = Crew(
    agents=[researcher, summarizer],
    tasks=[research_task, summary_task],
    process=Process.sequential # Researcher finishes, then Summarizer starts
)

# 6. Execute
result = tech_crew.kickoff(inputs={'topic': 'trending news today'})
print("\n\n########################")
print("## FINAL SUMMARY OUTPUT ##")
print("########################\n")
print(result)