## Lucas - Sentiment Analysis and Film Scripts

Define Sentiment Analysis:
Sentiment Analysis is a computational method that assesses the emotional tone or polarity (positive, negative, neutral) in text by analyzing words and phrases. It transforms raw text into sentiment scores—typically as numerical values for positive, negative, or neutral tones—which allow us to quantify emotions expressed in a body of work. This scoring helps reveal emotional and cultural perspectives in narratives, as well as patterns in how themes are emotionally framed. In this study, both the VADER lexicon (for polarity categories like positive, negative, and neutral) and the NRC lexicon (for specific emotions like joy, anger, and fear) were used. Each lexicon scores the text differently, allowing for a nuanced view of how sentiment is expressed in the data.

Why this is valuable for cultural data:
Our project topic is Literature and Texts – specifically Children's Literature. Sentiment Analysis can reveal how characters and themes are portrayed emotionally across narratives, helping to identify cultural trends and shifts in attitudes within children's literature and film.

Scholars:
Frangidis, P., Georgiou, K., Papadopoulos, S. (2020). Sentiment Analysis on Movie Scripts and Reviews. In: Maglogiannis, I., Iliadis, L., Pimenidis, E. (eds) Artificial Intelligence Applications and Innovations. AIAI 2020. IFIP Advances in Information and Communication Technology, vol 583. Springer, Cham. [https://link.springer.com/chapter/10.1007/978-3-030-49161-1_36](https://doi.org/10.1007/978-3-030-49161-1_36)

Review and Summarize Selected Scholarship:

1. Bibliographic Information:
    Authors: Frangidis, P., Georgiou, K., & Papadopoulos, S.
    Title: Sentiment Analysis on Movie Scripts and Reviews: Utilizing Sentiment Scores in Rating Prediction
    Publication Venue: AIAI 2020, IFIP AICT
    Publication Date: 2020

2. Computational Method or Cultural Data Type
    Method: The study applies Sentiment Analysis by combining lexicons (VADER for sentiment scoring and NRC for emotion 
    categorization) to movie scripts and reviews, aiming to predict movie ratings based on emotional alignment between scripts and 
    reviews.
    Transformation: Text data is processed to assign sentiment scores, capturing shifts in emotion throughout the movie scripts and 
    reviews. This transformation allows for the analysis of how emotional tone aligns with audience reception.

3. Summary of Argument and Use of Computational Method:
    Argument: The authors argue that the alignment or divergence between the intended emotional tone of a movie (in the script) and 
    the audience's emotional response (in reviews) can help predict movie ratings.
    Method Application: The study combines sentiment scores from both scripts and reviews to build predictive models. The use of 
    lexicons helps identify emotional trends and rates emotional resonance, which are then evaluated using machine learning 
    algorithms to assess predictive accuracy.

4. Code and Data Availability:
    Data: The dataset includes 747 movie scripts and 78,000 reviews, sourced from the IMSDB and Rotten Tomatoes websites.
    Code: The study used sentiment analysis libraries such as VADER and NRC but does not provide full code

5. Interest, Usefulness, and Disciplinary Approach:
    Interest: The study is compelling in its approach to comparing intended and perceived sentiment, which has applications in media 
    studies and consumer behavior.
    Disciplinary Approach: This study lies within the field of Computational Social Sciences and Digital Humanities, integrating machine 
    learning with cultural and emotional analysis.

6. Potential Use for Group Project:
    This study’s approach could help us analyze themes in children’s literature by looking at emotional patterns. Using both VADER and 
    NRC lexicons, we can track emotions like “trust” or “fear” throughout stories to see if certain themes (like friendship or conflict) 
    show up with specific emotional tones. This could also reveal shifts in cultural attitudes, such as how bravery or kindness are 
    portrayed over time. Plus, by mapping emotions in key story moments, we might get insights into the underlying morals and 
    messages, making sentiment analysis a versatile tool for exploring cultural themes across narratives.

## Gloria - Topic modeling and literary texts
**Define Topic Modeling:**
Topic Modeling is a method that identifies clusters of words in large text collections to reveal hidden themes or topics.

**Why this is valuable for cultural data:**
Our project topic is Literature and Texts – Children's Literature. And this method is commonly used in literary studies to analyze themes, trends, or even authorial influences.

**Scholars:**
Omar, A. (2020). Towards computational models to theme analysis in literature. International Journal of Advanced Computer Science and Applications, 11(9), 93-99–99. https://doi-org.proxy2.library.illinois.edu/10.14569/IJACSA.2020.0110911

**Review & Summarize Selected Scholarship:**

1. Bibliographic Information
Authors: Abdulfattah Omar
Title: Towards Computational Models to Theme Analysis in Literature
Publication Venue: International Journal of Advanced Computer Science and Applications
Publication Date: 2020

2. Computational Method or Cultural Data Type
Method: The study uses **Vector Space Clustering (VSC)**, a lexical clustering approach for thematic classification of literary texts. The data is represented using the **Vector Space Model (VSM)**, where text is processed into clusters based on lexical content.
Transformation: VSM and clustering algorithms _transform the literary text into clusters that group similar themes_, making it possible to objectively categorize and analyze recurring themes.

3. Summary of Argument and Use of Computational Method:
Argument: Omar argues that computational theme analysis offers an objective and replicable approach to categorizing themes in literature, addressing limitations in traditional literary criticism such as subjectivity and limited scalability.
Method Application: By clustering lexical data, the study objectively groups Hardy’s novels and stories according to thematic content. This approach enables a structured thematic analysis of large volumes of text, revealing patterns that may be overlooked through traditional methods.

4. Code and Data Availability:
Data: The study’s dataset consists of Thomas Hardy’s novels and short stories, represented as lexical vectors.
Code: No specific code is provided in the study, but the methods are based on established vector clustering techniques in data science, making it replicable with standard clustering tools.

5. Interest, Usefulness, and Disciplinary Approach:
Interest: The study’s approach to theme analysis is intriguing as it integrates computational and literary methods, addressing both cultural content and computational rigor.
Disciplinary Approach: This study aligns well with Digital Humanities, using data science techniques to advance traditional literary criticism.

6. Potential Use for Group Project:
This study provides a clear framework for using lexical clustering in thematic analysis, which is directly applicable to topic modeling in literary texts. The structured approach to theme identification will be valuable for analyzing recurring themes across a selected corpus in our project.


## Cindy - Social Network Analysis
Hello everyone! Today, I’ll share how Social Network Analysis (SNA) and social media data can help us explore the fantasy genre in children’s literature.

#### Social Network Analysis (SNA)
SNA examines relationships and structures within networks, with social media users as “nodes” and interactions (like likes or shares) as “edges.” For this project, SNA lets us map out social interactions around children’s fantasy literature—showing how fans, authors, and critics connect and engage in discussions.

#### Why SNA is Useful
SNA is helpful because it reveals influential figures, like popular fan pages, and clusters or communities, such as groups of fans who follow a particular series. This allows us to see how certain fantasy books or themes go viral and how different groups engage with children’s fantasy literature.

#### Social Media Data as Cultural Data
Social media data includes user-generated content like posts and comments. Analyzing this data lets us track real-time reactions to children’s fantasy books and spot trends—like popular themes and characters that resonate across regions or demographics.

#### Relevant Scholarship
I found the paper “Community Detection in Social Networks” by Bedi and Sharma helpful. They discuss community detection methods like clustering, which we can apply to identify groups of fans with similar interests in children’s fantasy literature, giving insight into how the genre is received by different audiences.

#### Project Application
Applying SNA and community detection allows us to uncover clusters of fans and trends in children’s fantasy literature, helping us understand the genre’s cultural impact. By using community detection techniques, we can uncover clusters of fans who are passionate about certain aspects of the genre. This could help us understand the cultural impact of specific books and identify trends within fan discussions.

#### Conclusion
In summary, SNA and social media data provide valuable cultural insights into the online discussions around children’s fantasy literature. By studying these interactions, we can get a sense of how readers react to, adapt, and engage with fantasy literature in real-time. This project could offer insights for publishers, educators, and authors who are interested in understanding fan communities in children’s literature.

## Francis - Final decision
We decided to use **Topic Modeling** as our computational method for analyzing children's literature because it allows us to uncover hidden themes, trends, and underlying values embedded within large text collections. This approach is especially valuable for our project on Literature and Texts – Children's Literature, as it provides a structured, objective way to explore cultural messages in stories that are formative for young readers.

This approach not only aligns with Digital Humanities by combining computational and literary studies, but also provides a robust framework for our project’s goal: to explore how children's literature reflects cultural values and influences young readers’ perceptions. Topic Modeling will help us objectively categorize and interpret themes within our chosen corpus, providing insights into both historical and contemporary trends in children's storytelling.
