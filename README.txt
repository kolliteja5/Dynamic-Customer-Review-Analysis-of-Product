This project basically demonstrates the Amazon Customer Review Analysis which can be performed dynamically to any product.

Packages required to execute the code (also provided how to install each package in anaconda prompt ):
1) re                            conda install -c conda-forge regex
2) wordcloud              conda install -c conda-forge wordcloud 
3) matplotlib	conda install -c conda-forge matplotlib
4) requests	conda install -c anaconda requests 
5) beautifulsoup4	conda install -c anaconda beautifulsoup4 	
6) nltk		conda install -c anaconda nltk
7) stopwords	https://stackoverflow.com/questions/48385829/how-to-install-stop-words-package-for-anaconda
8) pandas		conda install -c anaconda pandas

Note: make sure that the files are present in a specifc folder and the path while executing is set to that specific folder.

Features:
1) Dynamic code for extracting data from Amazon for any product.
2) There is a parameter file which can be modified with the columns like Name of Product, URL of product customer reviews, class name of that product and number of pages to be extracted.
3) Utilized Vader lexicon parse to generate the polarity of each word through SemanticIntensityAnalyzer.
4) Analysing the reviews using WordCloud.

If you want to find the Analysis of customer reviews of any Product in Amazon, then follow below steps:

1) Open Parameter file, 
	a) change the name of product you want to analyse the customer reviews of
	b) Enter the URL, that means, go to the page where the customer reviews of the specific product is available. an example is shown in the URL_example_page.jpg. Copy the link and paste in URL column of parameter file.
	c) Right click on any of the review and select "View Page Source" and copy first line fo any review and check on "View page source" page with "ctrl+find". the example screenshot is available in "checking_for_class_name.jpg". Now before the found sentence, we observe the "class" name(for my project the class name is "a-size-base").So update the classs name in parameter file in class_name column in line number "3".
	d) it is the user choice to extract the number of pages. The only thing is to provide the range in the "No_Pages_Extract" column: (1,1000)
2) Before executing the code goto:
 Tools>Preferences>Ipython Console>"Graphics">Backend:Inline>change Backend:Automatic>OK

3) Now in code, if you want to view the positive wordcloud you can do it,or you can also view the negative wordcloud or neutral word cloud. its a dynamic definition that has to be changed at the end of code.
4) I have executed the code in Spyder and generated the output for all the 3 views(positive negative and neutral)

