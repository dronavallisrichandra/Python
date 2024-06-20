## ATSIRE ( Advanced Tracking System with Intelligent Resume Embeddings )

#### Overview: 

- During economic downturns, businesses face significant challenges in maintaining their operations and remaining profitable. In such times, it becomes even more crucial to hire highly qualified candidates who can help improve the company's operations and ensure its success. However, identifying the most suitable candidates is not always easy, and traditional recruitment methods may not be sufficient to evaluate a candidate's qualifications accurately. To address this issue, a recent study has proposed a unique method that uses embeddings to assess a candidate's qualifications. Embeddings are a type of deep-learning technique that can create comprehensive and multidimensional representations of data, such as resumes and job descriptions. 

- Currently, our data is limited and manageable using Google Colab. However, as the data becomes larger and more complex, we can utilize TACC systems for better handling and processing of the data. TACC systems are designed to handle large amounts of data and complex computations, making them an ideal choice for data analysis tasks that require significant computing resources. By leveraging TACC systems, we can ensure that our data analysis is efficient and effective and can accommodate future growth in our data needs.

#### Tools requirement:
1. Google Collab
2. python 3
3. Libraries: pandas, string, spacy, transformers, deep learning algorithms like Bert-base-nli-mean-tokens, Roberta-base-nli-mean-tokens, distill Bert-base-nli-mean-tokens, gpt2, t5.

#### Implementation:

1. Importing the required files: Initially we will be importing the Resume dataset that we collected from the Kaggle and Linkedin Job descriptions using the web scrapping.
2. Preprocessing the text : A text_preprocess function is created to remove the special characters and additional hyper links from the resume ad job description dataset
3. Installing the Sentence Transformer: After pre-processing the data, we will then install the sentence transformers. Which are pretrained to convert the sentences into embeddings.
4. Models used for creating the Embeddings Bert , DistillBert , Roberta, GPT2 and T5
5. Defining Sentence Embeddings, In order to iterate through each model. A sentence embedding function is created to get the sentence embeddings from a different models.
6. Then call Sentence Embedding Function to get the embeddings out of the resume and job description.
7. Calculating the  Cosine Similarity and creating a data frame for cosine similarity for different models is used to evaluate the best model out of it.
8. Evaluating the results of cosine similarities
10. Visualizing the embeddings by applying the PCA and plotting using the scatter plot, to identify the clusters between each Resume and Job description.

#### Future work:

- Working in collaboration with recruting companies to get the updated resume and validating their Job requirements and improving the models to further finetune based on the skills required for the job description vs skills extracted from the resume.



