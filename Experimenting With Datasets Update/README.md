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

