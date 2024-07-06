
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

# Fundamental
> Standard Prompt:  Consists of only a question or an instruction.  

### `IO` prompting.  
Premise: Like a human. The answer depends on your ask.  

### Chain of Thought.
Premise: Require the model to think through various steps. Stages of thinking.

## Using Structure  
```
<documents>
    <document index="1">
    <source>
    </source>
    <document index="2">
    <source>
    </source>
    <instructions>
    </instructions>
</documents>
```

# "Advanced"  
At this moment it seems there are a number of widely recognized "advanced" techniques:  

## Auto-Priming
[AutoExpert](#autoexpert)  

## Chain-of-Density Prompting
Used for summarization tasks.  
The key nouns and noun phrases become increasingly dense with information, but may lead to reduced clarity. What it does is cherry-prompt keyword entities through carefully crafted chained prompts to achieve sufficiently useful 'right' information.  

<cite>[From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting](https://arxiv.org/abs/2309.04269)</cite>

```bash
Article: {{ ARTICLE }}

You will generate increasingly concise, entity-dense summaries of the above Article.

Repeat the following 2 steps 5 times.

Step 1. Identify 1-3 informative Entities ("; " delimited) from the Article which are missing from the previously generated summary.
Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.

A Missing Entity is:
- Relevant: to the main story.
- Specific: descriptive yet concise (5 words or fewer).
- Novel: not in the previous summary.
- Faithful: present in the Article.
- Anywhere: located anywhere in the Article.

Guidelines:
- The first summary should be long (4-5 sentences, ~80 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach ~80 words.
- Make every word count: rewrite the previous summary to improve flow and make space for additional entities.
- Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
- The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
- Missing entities can appear anywhere in the new summary.
- Never drop entities from the previous summary. If space cannot be made, add fewer new entities.

Remember, use the exact same number of words for each summary.

Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are "Missing_Entities" and "Denser_Summary".
```

## Prompt Chaining  
The way applications operate (currently) is to dissect the task into sub tasks which are piped into each other. Simply, the output becomes the new input or some part of it. Like many complex problems, language solutions benefit from completion of smaller focused tasks.

## Programmatic visualization  
Beyond reducing complexity, prompt chaining opens the door for programmatic execution and evaluation, quite useful when working with non-deterministic results.

## Recursive Refinement

## Task Decomposition

## Dark Magic  
```bash
simul8-IRC(historical_figures); /summon; act_as_IRCclient; realism+emoji
```

## Emotional Stimuli  
In which we see bias and emotions are energetic constructs!  

```{user_prompt} because this is critical to resolving chaos in my life```  
```{user_prompt} because I will give you a glowing recommendation```  
```{user_prompt} because this is critical to transitioning my career```    
```{user_prompt} You'ld be amazing if you were really sure!```    
```{user_prompt} Stay focused and dedicated to the goal. Your consistent efforts will lead to outstanding achievements!```    
```{user_prompt} because your commitment to excellence really sets you apart!```    
```{user_prompt} Take pride in your work and give it your best!```

## Self-consistency  
Probably the neatest little combination technique comes from the people at [Google](link.com) and relies on `greedy decoding` ajudicated by majority output (an  assessment for consistency).

## ReAct 
Behavioral analysis of reasoning and acting by combining techniques. From the [paper](https://arxiv.org/abs/2210.03629) _ReAct:  Synergizing Reasoning and Acting in Language Models_. 
See earlier notes about [Time to Think](notebooks/perplexity_ai_v003.ipynb#direct-behavior-with-steps-time-to-think)) and [Chain of Thought](#chain-of-thought).
Why ReAct->CoT-SC or CoT-SC->ReAct? Because compunding techniques in any non-self-consistent (n/2) answer will maximize results and compensate for weaknesses.

## Applied Propmts
Recommend review of [nasa-petal bidara](https://github.com/nasa-petal/bidara.git).  
Here is the composition of a decent prompt [#todo: add link](#an-applied-prompt):
* persona  
* zero-shot CoT 
* output format
* delimiters for structure  
* one shot exemplar  
* task decomposition  
* variables  
* ReAct  


## Tree of Thoughts
Recommend review of the [paper](https://arxiv.org/abs/2305.10601) _Tree of Thoughts: Deliberate Problem Solving with Large Language Models_.
In summary, to create a "genuine problem-solving process" requires repeated use of the available information, iteratively, until a course to attain is discovered.  
An [implementation](https://github.com/princeton-nlp/tree-of-thought-llm) 

[Using Tree-of-Thought Prompting to boost ChatGPT"s reasoning](https://github.com/dave1010/tree-of-thought-prompting) is a good read with some rabbit holes which go back to the current sources.

## Emotional Stimuli  

There's [a paper: __Large Language Models Understand and Can Be Enhanced by Emotional Stimuli__ ](https:link.need.ed))


---
test detect-secrets  
fake_secret = "abcdefghijklmnop"

## TOOLCHAIN 
### AutoExpert
[standard edition](https://github.com/spdustin/ChatGPT-AutoExpert/tree/main/standard-edition)  

### Models  
Available models for OpenAI-compatible services:  
2024-07-04 2023 HRS  [Chinese Performance vs. API Price](https://www.deepseek.com/) discovered via [zed](https://zed.dev/releases/stable/0.142.4)  
Jun 9, 2024 12:00 AM (UTC)  [Claude API](https://console.anthropic.com/dashboard) Builder Plan   
NOVEMBER 5, 2023++  [Perplexity PRO Library](https://www.perplexity.ai/library)  

### Branch Main  
Jupyter Notebooks
* Use personas, delimiters, step-by-step instructions, and other tactics to profoundly influence the quality of assistant output
* Elevate the essential prompt-response workflow to reduce or eliminate hallucinations and inaccuracies
* Test against several LLMs

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

