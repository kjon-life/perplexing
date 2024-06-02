
## Strategy & Tactics
### Provide sufficient clarity and details
Clear objectives: The more specific and detailed the prompt the more likely a response will be constrained in relevance. 
 
### Eliminate negations  
It seems, like people, LLMs are not great at what *not* to do. 

### Define roles

### Predefine output format
Learn how to ask for something specific that is trivial for an LLM to complete. Example, return the response in a dictionary, list, json, with or without diagrams

### Illustrate  
Incorporate leonardo.ai (or other engines) to generate the visual imagery which supports the response

### Provide your own trusted sources
A reference text, or a functional output example, will significantly improve the quality of response. The general constaints are:
    * Be selective in choosing the documents to attach
    * Be directive: Tell the assistant to use that specific document(s)
    * Be careful: Require the assistant properly cite the specific sections it is reusing or referencing
    * Be comparative: Ask the assistant to generate multiple responses and compare the results for accuracy and relevance

### Calrify vs rewrite?

### RTF
The T is for tasks. Like humans, the more specific and simple the task the more likely the results will be predictable and complete...
#### Add structure first
Break down a task into steps and sequences. **The sequence is important.**

#### Clarify intent

#### Require effective summary
Recursion is your friend, especially for longer inputs. Summary of a summary of summaries, compared to an alternative solution. The general principles:
* Focus on one thing at a time
* Define an order or sequence
* Smaller focused prompts are more cost-effective?

### Few shot prompting
* Do this:
* Example output:
* Followup prompt:

### Establish a baseline
OpenAI describes this as giving the model time to think.
Whether directing the assistant to develop its own solution first, or ...

### Define the external tools
Consider using directives to validate a solution in a specific language or an API

### Testing
1. System directives to compare outputs to factual sources
2. Pre-determined standards esp re factual information
3. Evaluation process for sensitivity

### Priming
* semantic
* repetition
* anti-priming
> “Not the least but the m___.
Not the guest but the ____.
A name for a spirit is a ____.
Cooking food or coffee beans is called a ____.
What you put in a toaster is called ____.”



## TOOLCHAIN  
### Branch Main  
Jupyter Notebooks
* Use personas, delimiters, step-by-step instructions, and other tactics to profoundly influence the quality of assistant output
* Elevate the essential prompt-response workflow to reduce or eliminate hallucinations and inaccuracies

### Branch ZeroToMastery
Python, OpenAI, LangChain, Vector Embeddings, Pinecone.  
* chatbots  
* question answering system  
* summarization tools  

### Branch PellucidController
Python, pplx-api, LangChain, Vector Embeddings, Pinecone.  
[pplx-api](https://blog.perplexity.ai/blog/introducing-pplx-api)  

### Credits  
