
## Strategy & Tactics  
When will AI "take your job"? Probably never. But that person who is AI-augmented is going to make you look like you are standing still. These notebooks are progress into the articulations which will let AI augment your reality. 

### Provide sufficient clarity and details
Clear objectives: The more specific and detailed the prompt the more likely a response will be constrained in relevance. This is known as __context__.
 
### Eliminate negations  
It seems, like people, LLMs are not great at what *not* to do. 



### Illustrate  
Incorporate leonardo.ai (or other engines) to generate the visual imagery which supports the response

### Provide your own trusted sources
A reference text, or a functional output example, will significantly improve the quality of response. The general constaints are:
    * Be selective in choosing the documents to attach
    * Be directive: Tell the assistant to use that specific document(s)
    * Be careful: Require the assistant properly cite the specific sections it is reusing or referencing
    * Be comparative: Ask the assistant to generate multiple responses and compare the results for accuracy and relevance

### Clarify vs rewrite?  
Keep in mind that, in general, your current prompt and prior prompts will be resubmitted, contributing to your token use. 

### Token Limits
Token use adds up. It's important to know the token limit we work within, for impact upon coherance. See also, `lost in the middle`. 


### RTF
#### Define roles
An LLM needs help. Be clear about its role so it can focus on being helpful for you. The role should be as simple as it needs to be relevant the desired focus and complexity of the desired output
#### Add tasks first
The T is for tasks. Like humans, the more specific and simple the task the more likely the results will be predictable and complete...
Break down a task into steps and sequences. **The sequence is important.**  
#### Ask for the format  
Learn how to ask for something specific that is trivial for an LLM to complete. Example, return the response in a dictionary, list, json, with or without diagrams

#### Clarify intent

### Require effective summary
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

### Lost in the Middle
*  Too much context, esp in the middle can be detrimental to accuracy
* the most important data should be at the beginning or the end of the prompt
* focus on how much context is strictly necessary  

### In six months
* None of this may be relevant in six months

### Pipes  
Control the boundary message:
#### Length is fuzzy  
"Write a 100 token or 100 word output" will not be reliable  
There are ways to create the outline, then create more complex outputs sequentially.
Ask for the max tokens if it's not obviously specified  
#### Formats are effortless
A consistent efficiency can be found by getting the models to produce the reliable output in a specific format suited to your needs.
- Why create an Excel file if the model is efficent in doing it?
- Why restructure for semantic HTML if a model is far faster than a human?
- Have the model create diagrams in Mermaid?
#### Jailbreaking  
[Do Anything Now](chat.imsys.org) and Pliny the Prompter  
![](images/2024-06-20-22-17-18.png)  
#### Prompt injection  
- Add some prompt in an image; See what (doesn't) happen...  



## Fundamentals & Setup
### Delimiters provide structure  
```
===
'''
###
***
<data> </data>
```  
Structured data provide patterns, especially for larger or more complex prompts; It reduces the surface of possibilities with punctuation
### It seems a solution
Is the solution pre-supposed in the prompt? That's always counter-productive.

### Zero-Shot
Simple task, no training nor exemplars
### Two-Shot
Provide an example (shot)
### Few-Shot  
Provide a few examples
```
<examples>
Something specific that might serve as an example

Something else specific that might serve as an example

</example>

```
> but do accurate shots (demos) really matter? probably not (source)  

## Chain-of-Thought
If provided superior chain of thought, model output improves. If required to print out a chain-of-thought, model output actually improves. Seems relatively complex, but perhaps, like many things in nature, the core algorythm is quite simple?

### Zero-shot-CoT
Basically, add "Let's proceed step-by-step"

### Top P
Diversity via nucleus sampling; Or when top p is lowered we reduce the scope of  tokens (only consider some percentage of most likely tokens)

### Frequency and Presence penalties  
Simply reduces likelhood of repetions; Really, the model could spool into repetitions if variability is not enforced

### Stop Sequences  
A rather cludgy attempt to get the model to just stop generating tokens; I wonder how it could be used

# Fundamentals
> Standard Prompt:  Consists of only a question or an instruction. Premise: Like a human. The answer depends on your ask. If

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

### Papers  
[Language Models are Few-Shot Learners](source.not.found)  
[Rethinking the Role of Demonstration](source.not.found)