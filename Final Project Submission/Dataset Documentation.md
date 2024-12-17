### Project Dataset Documentation

**1. Dataset Overview**

1. Purpose: To analyze how themes and morals in children’s literature evolve over time.
   
2. Source: Data was collected manually from Project Gutenberg and ICDL.

3. Size: 18 rows and 10 columns.

**2. Data Dictionary**

| Column Name  | Description | Data Type |
| ------------- | ------------- | -------------|
| Book Title  | Title of the book.  | String |
| Author  | Name of the book’s author.  | String |
| Data Published | Year or date when the book was published. "n.d." indicates no specific date.| String |
| Contributed by | Source or institution that contributed the book data.| String |
| Archive | Archive or collection where the book can be found. | String |
| Genre | Genre/category of the book (e.g., Fiction, Humor, Sci-Fi, etc.). | String |
| Historical/Contemporary | Indicates if the book is historical or contemporary. | String |
| Sentiment | Overall sentiment (Positive/Neutral/Negative) derived using TextBlob. | String |
| Polarity | Sentiment polarity score (numerical representation between -1 and +1). | Float |
| Subjectivity | Subjectivity score (0 = objective, 1 = highly opinionated). | Float |

**3. Preprocessing and Cleaning Steps**

1. Dataset Compilation:

Data entries were manually collected using Google Sheets from Project Gutenberg and ICDL.

Key details recorded: Title, Author, Year, Genre, and Archive.

2. Sentiment and Subjectivity Analysis:

Sentiment scores (Polarity and Subjectivity) were calculated using the TextBlob library.

The challenge: Differentiating between narrative tone and dialogue tone.

3. Validation:

Missing values were checked; all fields are complete.

Data types were standardized (e.g., ensuring numerical values for polarity and subjectivity).

**4. Summary of Findings**

Polarity Trends: Polarity peaks in earlier books but stabilizes over time (post-1950).

Subjectivity Trends: Early works are highly subjective; recent works vary.

By Genre:

1. Highest Polarity: Fairy Tale and Christmas Stories.

2. Lowest Polarity: Fantasy Fiction and Classic genres.

3. Highest Subjectivity: Fairy Tale and Christmas Stories.

4. Lowest Subjectivity: Humor and Classic genres.
