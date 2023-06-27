# Mildew detection in cherry leaves
## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
* The dataset contains 4208 images in .jpeg format, taken from the client's crop fields.
* The images  are devided equaly into two categories; healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

The purpose of this project is to save time in this process. The IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* **Hypothesis 1:** It is suspected that cherry leaf with powdery mildew have visual signs that diffirentiate them from healthy cherry leaves.
  * An image avarage and variability study can help to investigate it
    * If this can be confirmed, this would indicate likelyhood of success in addressing hypothesis 2, and motivate the continuation of the project. 
* **Hypothesis 2:** It is suspected that a convolutional neural network (CNN) for image classification, can predict if a cherry leaf is healthy or have powdery mildew.
  * Building, training and testing a CNN using the dataset mentioned above, will help to invastigate it.
    * If this can be confirmed, a dashboard can be deployed and provide end user support in the leaf inspection process.
* **Hypothesis 3:** It is suspected that a softmax activation function can be used to assign a probability to a prediction and that it is represantative of the probability that the prediction is correct. I. e. the lower the probability that the model outputs, the higher the risk is for missclassification.
  * Studying the distribution of predictions in ranges of probability, and distribution of false predictions in ranges of probability, can help investigate it.
    * If this can be confirmed, it might be feasible for the users to "resample" when feeding the model live data, if the assigned probability to a given predication is low.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
### Map the business requirements in a User Story based format to each of the Data Visualization and ML Tasks along with the specific actions required for the enablement of each task.

* **Business Requirement 1**: Data Visualization 
	* We will display an image montage for both healthy leaves and leaves infected with powdery mildew.
	* We will display the "mean" and "standard deviation" images for healthy cherry leaves and cherry leaves that have powdery mildew.
 	* We will display the difference between an average image of healthy cherry leaf and an average uninfected cell.

* **Business Requirement 2**:  Classification
	* We will augment a subset of the dataset provided by the client, to create more data for training a model. 
	* We will build a model using a convolutional neural network (CNN) and train it using the training dataset, to determine if a cherry leaf has powdery mildew or not.
	* We will build the model to output a probability and examine the distribution of assigned probabilities and where false predictions are located in that distirbution, in order to understand its significans.
	* In training the model, we will withold a subset of the provided dataset, in order to evaluate the model, using "unseen" data, in order to ensure we meet the clients request for a minimum of 97% prediction accuracy.
	* We will build a classifier and a dashboard that generate reports based on uploaded data.

## ML Business Case
* We want an ML model to predict if a cherry leaf has powdery mildew or not, based on historical image data. It is a supervised, binary classification model. Though, technicaly it will be approached as a categorical classification model with two classes using a CNN with a softmax activation function in the output layer.
* In order to "expand" the training data, we will use data augmentation techniques to allow the model to train on synthesized data.
* Our ideal outcome is provide the employees working with inspection of cherry trees, with a faster and reliable diagnostic if a given leaf has powdery mildew or not.
* The model success metrics are
	* Accuracy of 97% or above on the test set.
* The model output is a "prediction", indicating if the inputed data (image of a leaf) has powdery mildew or not and the associated probability of having powdery mildew or not. The employees of the client will collect samples as usual and upload the image to the app.
* It will also be considered a success if we can establish an understanding of the probability metric and its significance, as this can guide users to, for example, resample the live data if probability is low for a given sample.
* Heuristics: Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. It leaves room to produce inaccurate diagnostics due to human errors and the solution i hard to scale in order to manage huge crops across the country.
* The data used for training and testing the model was provided by the client and contain 4208 images. For this project it was collected from a [kaggle dataset endpoint](https://www.kaggle.com/codeinstitute/cherry-leaves).


## Dashboard Design (Created using Streamlit)
### Page 1: Project Background
* Info Section: General Page Information
    * Describe the reason for the project and the envisioned benifits from the clients perspective, as well as some heuristics.
* List Section: Business requirements
	* Ordered list with the business requirements that guide the efforts of the project.
	*  1. The client is interested to have a study to visually differentiate between a parasite contained and uninfected cell.
	*  2. The client is interested to tell whether a given cell contains malaria parasite or not.
* Text Section: Project Dataset 
    * Describes the dataset in general terms.
	* Guide the user towards the model specification page where it is examined more thouroughly
	* Guide the user with a link and description about the Kaggle endpoint where it was sourced.
* Info section: More information
	* Guide the user to this readme file on github with a link and a description.

### Page 2: Summary and Results
* Info Section: General Page Information
	* Describe how the business requirements where translated into Hypothesis that could be tested and confirmed/rejected in order for the project to meet the business requirements.
* Text section: Business requirement 1
	* Statement of business requirement 1 
		* Expandable text section (Checkbox) : Hypothesis 1
			* Info section: Hypothesis 1
				* Description of how hypothesis was approached
				* List Conclusions and findings
			* Warning/Error/Success Section indicating and clearly stating if the hypothesis could be confirmed or rejected.
* Text section: Business requirement 2
	* Statement of business requirement 2 
		* Expandable text section (Checkbox) : Hypothesis 2
			* Info section: Hypothesis 2
				* Description of how hypothesis was approached
				* List Conclusions and findings
			* Warning/Error/Success Section indicating and clearly stating if the hypothesis could be confirmed or rejected.
		* Expandable text section (Checkbox) : Hypothesis 3
			* Info section: Hypothesis 3
				* Description of how hypothesis was approached
				* List Conclusions and findings
			* Warning/Error/Success Section indicating and clearly stating if the hypothesis could be confirmed or rejected.

### Page 3: Cherry Leaves Visualization (Meet Business Requirement 1)
* Info section: General Page Description
	* State business requirement 1 as well as hypothesis 1
* Expandable sections (checkbox list)
	* Checkbox 1 - Label Samples
		* Info section: Description of the section
		* RadioButtons ('Healthy', 'Powdery_Mildew')
			* Display 2x6 number of images from selected class in dataset.
	* Checkbox 2 - Average and Variability for each class
		* Info section: Describe the idea behind the conducted image analysis
		* Image montages with variability and Avarage per class
			* Healthy class image mntage
			* Powdery Mildew class image montage
	* Checkbox 3 - Differences Between Label Averages
		* Info Section: Describe the idea behind the conducted image analysis
			* Image montage displaying the avarage images from both classes next to each other, as well as the calculated difference between them 

### Page 4: Mildew Detector
* Info section: General Page Description
	* General decription of page and usage
	* Guide to more information about the model
	* Link to dataset containing cherry leafes for testing
* File uploader widget
	* Option to upload one or more .JPEG images with browse button
* Results Presentation Section
	* Radiobuttons section - ('Table' or 'Images')
		* Caption - Select the format in to show results in
		* RadioOption - Table
			* Show anchhor link to download Table report as CSV
			* Display streamlit table
		* RadioOption - Images
			* For each uploaded file:
				* Show Image
				* Error or Success section indicating "Healthy" or "Infected" and containing:
					* Filename
					* Predicted class
					* Assigned Probability

### Page 5: Machine Learning Details
* Info section: General Page Description
	* Describe the page content and how it relates to hypothesees 2 and 3.
* Expandable sections (checkbox list)
	* Checkbox 1 - Data Preprocessing
		* Info section: Describe data balance and data split ratio
		* Plot data distribution across data subsets
		* Warning section: Comment No call for action
			* Horizontal Section Break
		* Info section: Describe Image size distribution
		* Plot image size distribution for all images
		* Error section: Note: Images where resized for model size management
	* Checkbox 2 - Model Architecture
		* Info section: Description of the model and list image augmentation and regularization techniques applied
		* Text out model.summary()
	* Checkbox 3 - Model Training
		* Info section: Description of the section images
		* Image: Accuracy and validation Accuracy accross epochs in model training
		* Image: Loss and Validation Loss accross epochs in model training
	* Checkbox 4 - Model Evaluation
		* Info section: Description of the section
		* List Loss and Accuracy evaluation on test dataset.
	* Checkbox 5 - Model Output
		* Info section: Description of the section, the purpose of the conducted study and the idea behind it.
		* For training-, validation- and test-data
			* Show "Probability Report" and metrics indicating the probability outputs significance and meaning
			* Show distribution plots of false predictions next to all predictions.
		* Error section: Comment that points to the fact that datapoints are to few for it to be a meaningful study and that hypothesis 3 can not be confirmed or rejected.


## Unfixed Bugs
* Though no bugs were left unfixed during the development and testing process, one feature could be addressed in future iterations of the development cycle.
	* This being that the model is not trained to recognize if it is actually being presented with a cherry leaf. This comes from the fact that the model has only been trained on images of cherry leafes and is only allowed to choose 1 out of two possible outputs.
	* The most obvious implication of this is that even if the model is presented with a selfie of the user, it will return a prediction telling the user that he or she is in fact a cherry leaf with powdery mildew or not.
	* This could perhaps be addressed by introducing a third category to the classification as well as an additional dataset that does not contain images of leaves at all.

## Deployment
### Heroku

* The App live link is: https://jens-brauers-mildew-detector.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button "Open App" on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries

* __Streamlit__ was used to create the dashboard.
* __Pickle__ was used to save and load files, from the Jupyter Notebooks into the dashboard application.
* __Scikit-learn__ was used to create classification reports and confusion matrixes for evaluating the model.
* __Tensorflow__ and __Keras__ was used to build and load the model as well as doing preprocessing like image augmentation and callbacks for early stopping. 
* __Seaborn__ was used to create plots in combination with matplotlib
* __Matplotlib__ was also used to read and load image files into NumPy arrays
* __NumPy__ was used for array manipulation, reshaping, and numerical operations on image data and labels.
* __Pandas__ was used for creating functional dataframes for creating plots as well as reports and tables
* __PIL__ was used for image processing tasks such as resizing, manipulating, and converting image files.
* __base64__ was used to encode data in Base64 format, which is then used to create a download link for a CSV file in the code.
* __os__ as well as __shutil__ was used to manipulate and manage directories for example when spliting datasets and moving data.
* __statistics__ was used to calculate median values and extract insights from probability distributions.
* __random__ was used in some cases for example to shuffle files for randomized selection in sampling etc.
* __sys__ and __io__ was used to capture console outputs and write to files for storing and use in app.
* __zipfile__ was used to extract dataset from kaggle zipfile
* __datetime__ was used to timestamp and name downloadable reports


## Credits 
Thanks to [Sabyasachi Sahoo](https://medium.com/@ssahoo.ai) for explanation on [Deciding optimal kernel size for CNN](https://towardsdatascience.com/deciding-optimal-filter-size-for-cnns-d6f7b56f9363)

Thanks to [Nicolai Nielsen](https://www.youtube.com/@NicolaiAI) for explanation on [Regularization in Neural Networks and Deep Learning with Keras and TensorFlow](https://www.youtube.com/watch?v=aner3u79IGw)

Thanks to [Hugo Larochelle](https://www.youtube.com/@hugolarochelle) for explanation on [Neural networks [7.5] : Deep learning - dropout](https://www.youtube.com/watch?v=UcKPdAM8cnI&t=201s)

Thanks to [Davide Giordano](https://medium.com/@davidegiordano) for [7 tips to choose the best optimizer](https://towardsdatascience.com/7-tips-to-choose-the-best-optimizer-47bb9c1219e)

Thanks to [Code Institute](https://codeinstitute.net/se/) for their amazing program [Diploma in Full Stack
Software Development](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=635849372549&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad=1&gclid=CjwKCAjwkeqkBhAnEiwA5U-uM00n5I1EnBiHAkjq8DQPg5kxyuG5aYfA2b2SnRjNqu9MLuLYEdw4tBoCN9MQAvD_BwE) that is the backbone of this project by providing tutorials, walkthrough projects and educational content covering almost all concepts used in this project.

Thanks to [Code institute on Kaggle](https://www.kaggle.com/codeinstitute) for providing the [dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) for this project.
