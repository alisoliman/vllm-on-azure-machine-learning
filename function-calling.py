from openai import OpenAI
import json

# Set up API client with the vLLM server settings
openai_api_key = <your-deployment-key>
openai_api_base = "https://vllm-hf.eastus2.inference.ml.azure.com/v1/"
client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)

def query_historical_event(date):
    fictional_historical_events = {
        "1805-03-21": "On March 21, 1805, the Treaty of Varis signed by several European powers established the first coordinated effort to protect migratory bird species.",
        "1898-07-10": "On July 10, 1898, the Great Illumination Act was passed in London, mandating the installation of electric streetlights across all major cities in the United Kingdom.",
        "1923-09-05": "On September 5, 1923, the International Academy of Innovation was founded in Zurich, Switzerland, promoting global collaboration in scientific research.",
        "1940-02-14": "On February 14, 1940, the first underwater train tunnel connecting two countries was completed between France and the United Kingdom.",
        "1954-11-08": "On November 8, 1954, the Global Weather Watch Program was launched, pioneering the use of satellites for monitoring Earth's climate systems.",
        "1977-06-30": "On June 30, 1977, the first fully solar-powered town, Solaria, was inaugurated in Arizona, setting a benchmark for renewable energy communities.",
        "1983-12-12": "On December 12, 1983, the Universal Language Project introduced a simplified global auxiliary language intended to foster cross-cultural communication.",
        "1994-04-23": "On April 23, 1994, the Oceanic Research Pact was signed, marking a commitment by 40 nations to share oceanographic research and preserve marine ecosystems.",
        "2009-08-15": "On August 15, 2009, the first international digital art exhibition was hosted simultaneously in Tokyo, Berlin, and New York, linked by live virtual tours.",
        "2020-01-10": "On January 10, 2020, the World Clean Air Initiative achieved its milestone goal of reducing urban air pollution levels in 50 major cities globally."
    }
    return fictional_historical_events.get(date, f"No historical event information available for {date}.")

tools = [
    {
        "function": {
            "name": "query_historical_event",
            "description": "Provides information about a historical event that occurred on a specified date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date of the event in YYYY-MM-DD format."
                    },
                },
                "required": ["date"]
            }
        }
    }
]

messages = [
    {"role": "system", "content": "You are a knowledgeable assistant that can retrieve information about historical events."},
    {"role": "user", "content": "Can you tell me what happened on August 15, 2009?"},
]

chat_response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=messages,
    temperature=0.7,
    max_tokens=1024,
    top_p=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.6,
    tools=tools,
    tool_choice='auto'
)

if chat_response.choices[0].message.tool_calls:
    date_argument = json.loads(chat_response.choices[0].message.tool_calls[0].function.arguments)
    date = date_argument.get("date", None)

    response = query_historical_event(date)
    print("Assistant response:", response)
else:
    print("Assistant response:", chat_response.choices[0].message.content)