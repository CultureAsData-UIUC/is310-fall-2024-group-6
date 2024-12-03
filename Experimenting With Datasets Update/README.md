### 1. Purpose of Experimentation
   
*Exploring Data Utility:* 

The purpose is to evaluate how well the dataset captures key aspects of the fantasy genre in children’s literature and its effectiveness in answering the research question. Experimentation helps identify recurring themes like magic, mythical creatures, or heroic quests, as well as trends such as changes in language, diversity, or storytelling styles. It also highlights gaps, such as missing demographic data on authors or underrepresented cultural elements, ensuring the dataset is robust and relevant for future research.

*Informing Future Use:* 

The experimentation phase also helps you think about how others might use your dataset. By documenting the outcomes of your experiments, you can provide future users with insights into the dataset’s strengths, limitations, and potential applications.

### 2. Method Selection and Application

*Choosing Computational Methods:* 

The computational methods that we plan on using are Sentiment Analysis along with mapping it out with a visualization techinique. When lookoing at fantasy stories, especially children's literature, we can see that they invoke strong emotions. With the vary genres of heroism, conflict, wonder, or loss we can use sentiment analysis that can give us patterns or tones that align with our genres. These patterns can also show trends which we can align with time and see how different decades or time periods have different moods with their stories. In order to apply such things to our dataset we would have to first clean our data. Punctuation, grammar, or even unessecary words are things we can remove using python by importing the raw txt file of our data into a code we can generate. Another idea could be to use an html web scraper if applicable. After doing this we would have to choose a sentiment analysis tool. Something like the library TextBlob can help us give a sentiment polarity where -1 to +1 negative to positive can give us a numeric value for whether something is positive or not.

When visualizing this, a simple Matplotlib and Seaborn code can run this. By generating word clouds or even plotting these scores on a bar chart can help us further expand our exploratory data analysis on our topic.

*Applying the Methods:* 

Once you’ve chosen your methods, you will attempt to apply them to your dataset. You are again encouraged to consult the Instructor for assistance with applying these methods, as well as using AI chatbots. You will be primarily assessed on your efforts to apply the method, not on the success of your result. This process allows you to test the data’s validity and robustness. You may find that certain aspects of the data need revision, such as missing variables, inconsistent formatting, or incomplete entries. The results of these experiments will guide your next steps in refining the dataset.

### 3. Documentation and Reflection
*Documentation of Experimentation Process:*

a. Methods Used:

Data Exploration: 
Cindy completed the "Exploring Data Utility" section, focusing on analyzing the dataset's relevance and its potential for cultural analysis within the context of children's literature.

Data Cleaning and Analysis Program: 
Francis developed a Python program that processes .txt files of children's books, cleaning the text and providing two key rankings:

1). Sentiment Analysis: 
Scores stories on a scale from -1 to +1, where negative numbers indicate negative emotions, 0 indicates neutrality, and positive numbers suggest positive emotions.

2). Fact vs. Opinion Scale: 
Scores stories from 0 (entirely factual) to 1 (opinion-based content).
The program outputs these rankings for further analysis and visualization.

Data Collection: 
Francis retrieved additional .txt files from Project Gutenberg to supplement the existing dataset, ensuring diversity and richness in the analysis.
Data Consolidation: Lucas created a new .csv file that integrates the cleaned .txt files with updated titles and metadata to reflect the expanded dataset.

b. Issues Encountered:

Data Consistency: Ensuring that the titles and metadata of the new .txt files matched the existing dataset required careful cross-referencing and manual adjustments.

File Integration: Transitioning from .txt files to a structured .csv format involved additional steps, such as copying and pasting data into Excel and verifying correctness.

Visualization Challenges: 
While our group has discussed the possibility of creating bar charts using matplotlib, the integration of visualizations has not yet been finalized.

c. Results Obtained:

Successfully processed and cleaned the new .txt files, generating rankings for sentiment and fact/opinion balance.
Updated dataset now stored in a .csv file with consistent formatting and metadata, ready for visualization and further analysis.

*Individual Contributions:*

Cindy: Led the initial exploration of data utility, providing a foundational understanding of the dataset's relevance and scope for cultural analysis.

Francis: Developed the Python program for text analysis, ensuring automated sentiment and fact/opinion scoring. Also contributed by collecting additional .txt files from Project Gutenberg.

Gloria: Authored the documentation and reflection, ensuring that the entire process was transparently recorded and ready for replication.

Lucas: Consolidated the dataset into a new .csv file, ensuring that updated titles and metadata were accurately reflected, and prepared the data for visualization.

Collaboration Reflection: Our group worked effectively by dividing responsibilities based on individual strengths, allowing for efficient progress. Francis’s Python expertise streamlined text analysis, while Lucas’s focus on data consolidation ensured a seamless transition to a structured format. Cindy’s exploration provided a clear context for the project, and Gloria’s documentation unified the work into a coherent report. Communication was essential in resolving issues such as metadata consistency and visualization planning. 
