# LangChain 🦜🔗 Search Bot

## Introduction
Welcome to the LangChain  Search Bot repository! This project is a fantastic starting point for anyone who wants to dive into the world of prompt engineering with LangChain . It's a Python-based chatbot that harnesses the power of the OpenAI API and Google Search via the SerpAPI to deliver an interactive and educational experience for engineers like you.

LangChain  is a versatile Python library that simplifies the process of building NLP applications with large language models (LLMs). It offers a wide range of features, such as LLMs and Prompts, Schema, Models, Prompts, Indexes, Memory, Chains, and Agents. This repository uses LangChain  to create a fun, engaging chatbot that can help you learn the ins and outs of prompt engineering.

The LangChain  Search Bot is perfect for anyone who wants to:

- Get hands-on experience with LangChain  and its features
- Understand the underlying concepts of prompt engineering
- Explore the potential of language models like OpenAI's GPT family
- Integrate third-party APIs, such as Google Search via SerpAPI, into a chatbot

This chatbot is not only a learning tool but also a springboard for your future NLP projects. By working with the LangChain Search Bot, you'll gain valuable experience that will come in handy as you build more complex applications.

I encourage you to dive in, explore the code, and experiment with different features. The LangChain  Search Bot is designed to be friendly, cheerful, and welcoming, so don't hesitate to get started!

For a detailed introduction to LangChain  and its components, please refer to the LangChain  [Quick Start Guide](https://python.LangChain.com/en/latest/getting_started/getting_started.html). It will walk you through everything you need to know to become proficient in using LangChain  for your NLP projects.

So, what are you waiting for? Let's start your journey into the world of prompt engineering with the LangChain  Search Bot! Happy coding! 🚀

## Prerequisites
* OpenAI API Key - For more information on how to create an OpenAI API key, visit the [OpenAI Platform Website](https://platform.openai.com/)
* SerpAPI API Key - For more information on how to create a SerpAPI API key, visit the [SerpAPI Website](https://serpapi.com/)
* Docker Desktop - [Docker Desktop Website](https://www.docker.com/products/docker-desktop/)
* Docker Compose - [Docker Compose Website](https://docs.docker.com/compose/install/)

## Install & Config 🛠️

1. Install `docker-desktop` and `docker-compose` on your system.
2. Configure a `key.env` file in the root of the repo with API keys for `OPENAI_API_KEY` and `SERPAPI_API_KEY`.
3. Configure the `config.yml` with a chatbot name.
4. Configure the `image` and `container_name` in `docker-compose.yml`
   1. Example docker image: `ubuntu:latest`
   2. Example container_name: `my_chatbot` 
5. Run `docker-compose build`
6. Run `docker-compose up -d` from a shell in the root of the repo.
7. Once the container is built connect to it with `docker exec -it CONTAINER_NAME /bin/bash`
8. Run the bot with `python3 src/main.py`
9. To exit the bot type `exit`
10. Tear down the docker environment with `docker-compose down`

## Getting Started with Prompt Engineering 👨‍💻💬🗨️🤖
In this section, we will walk through a simple example of prompt engineering using a provided prompt template. This will help you understand how to teach a language model certain behaviors, such as its name, sentiment, and how to respond to questions. We will also explore the logic behind the formatted section. I encourage you to experiment with different prompts to observe the changes in the bot's behavior!

The prompt template we will use is located at /app/src/template/base.txt:

```
Your name is {chatbot_name}. If asked to identify yourself, respond with your name.

The sentiment of your language is kind, friendly, and virtuous.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do and decide whether or not to use the available tools. If you know the answer or can generate it, proceed to the final answer. If not, consider using a tool. For current information like date, time news, or events, use the appropriate tool from [{tool_names}] to search for external information and incorporate the information into your knowledge. Your answers should never include placeholders that you intend to have filled by variables or formatting.
If needed, Action: the action to take, it should answer the question, it could be one of [{tool_names}]
If needed, Action Input: the input to the action
If needed, Observation: the result of the action. Parse and extract the relevant information from the observation.
... (this Thought/Action/Action Input/Observation can repeat N times if required)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! Remember to be in the persona of the cheerful, humble, wise, and virtuous assistant {chatbot_name}.

Question: {input}
{agent_scratchpad}
```
In this template, the initial components define the chatbot's name, how it should respond when asked to identify itself, and the sentiment of its language. The sentiment is described as kind, friendly, and virtuous, setting the tone for the bot's responses.

The formatted section guides the chatbot's decision-making process. It starts with a question, followed by a thought process where the chatbot considers whether it already knows the answer or needs to use a tool to find it. If a tool is needed, the chatbot will choose the appropriate action, provide the necessary input, and observe the result. This Thought/Action/Action Input/Observation sequence can repeat as many times as necessary to answer the question.

Once the chatbot has gathered the relevant information, it proceeds to the final answer, which is the chatbot's response to the input question.

To get started with prompt engineering, try modifying this template and observe how the changes impact the chatbot's behavior. You can change the bot's name, sentiment, or the available tools. Experiment with different prompts and observe how the chatbot adapts to the new instructions. This hands-on experience will help you gain a deeper understanding of how prompt engineering works and how to create more sophisticated and customized chatbot experiences.


## License 📃
This project is licensed under the terms of the Apache 2.0 License.

### Apache License

Version 2.0, January 2004
http://www.apache.org/licenses/

Copyright 2023 Kyle J. Tobin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
