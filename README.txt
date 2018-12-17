Search Data Exercises
--------------------

The attached file ("search_data.csv") contains simulated search data from a fictional application. In this application, users search for medications by entering text strings. Each keystroke triggers a call to a search service, which returns a response with a variable number of results.

The dataset contains a view of this process from the server side. Included are six fields:

1. requestDate - the datetime that the request is received by the server
2. requestSize - the size of the request received by the server
3. request - the actual search string received by the server
4. responseDate - the datetime that the server responded to the request
5. responseSize - the size of the response sent by the server
6. totalResults - the number of results that were returned by the server

Using this dataset, please complete the following three exercises:

1. Perform an exploratory analysis of the data. Describe and summarize the data.

2. You may have noticed that one notable thing that is missing from the dataset is a "user ID" that can uniquely identify the user that submitted a given search request. As a result, it is difficult to link searches over time that are made by the same user.

  - Choose and implement a method for linking search requests "over time by user"
  - Using the chosen method, explore/describe/summarize the data from the perspective of "the user"

3. Imagine that you have been asked to design and implement an algorithm or model for improving the performance of the search function. Outline the approach that you would take. Your answer should include:

  - What have other people/organizations done to solve similar problems
  - How you will setup the data (e.g., what is your X and what is your Y?)
  - How you will setup the problem
  - Other data that you may need or desire
  - Algorithm/model to be used
  - Evaluation metrics for chosen algorithm/model
  - Implementation concerns (e.g., how will your algorithm/model work in a production-level environment?)
  - How you will monitor and improve the performance of your algorithm/model over time, once it is deployed and in use
