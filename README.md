# Mildew detection in cherry leaves
## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
* The dataset contains 4208 images in .jpeg format, taken from the client's crop fields.
* The images  are devided equaly into two categories; healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

The purpose of this project is to save time in this process. The IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


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
	* We will display the "mean" and "standard deviation" images for healthy cherry leaves and cherry leaves that have powdery mildew.
 	* We will display the difference between an average image of healthy cherry leaf and an average uninfected cell.
	* We will display an image montage for both healthy leaves and leaves infected with powdery mildew.

* **Business Requirement 2**:  Classification
	* We will augment a subset of the dataset provided by the client, to create more data for training a model. 
	* We will build a model using a convolutional neural network (CNN) and train it using the training dataset, to determine if a cherry leaf has powdery mildew or not.
	* We will build the model to output a probability and examine the distribution of assigned probabilities and where false predictions are located in that distirbution, in order to understand its significans.
	* In training the model, we will withold a subset of the provided dataset, in order to evaluate the model, using "unseen" data, in order to ensure we meet the clients request for a minimum of 97% prediction accuracy.
	* We will build a classifier and a dashboard that generate reports based on uploaded data.

## ML Business Case
### Articulate a Business Case for each Machine Learning task which must include the aim behind the predictive analytics task, the learning method, the ideal outcome for the process, success/failure metrics, model output and its relevance for the user, and any heuristics and training data used.

* We want an ML model to predict if a cherry leaf has powdery mildew or not, based on historical image data. It is a supervised, binary classification model. Though, approached as a categorical problem with two classes. 
* Our ideal outcome is provide the employees working with inspection of cherry trees, with a faster and reliable diagnostic if a given leaf has powdery mildew or not.
* The model success metrics are
	* Accuracy of 97% or above on the test set.
* The model output is defined as a flag, indicating if the leaf has powdery mildew or not and the associated probability of having powdery mildew or not. The employees of the client will collect samples as usual and upload the picture to the app.
* Heuristics: Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. It leaves room to produce inaccurate diagnostics due to human errors and the solution i hard to scale in order to manage huge crops across the country.
* The training data to fit the model was provided by the client under an NDA (Non-Disclosure Agreement) and contain 4208 images. For this project it was collected from a [kaggle dataset endpoint](https://www.kaggle.com/codeinstitute/cherry-leaves).


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

### Page 3: Cells Visualizer (Meet Business Requirement 1)
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
* Business requirement 2 information - "The client is interested to tell whether a given cell contains malaria parasite or not."
* Link to download a set of parasite contained and uninfected cell images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple malaria cell image. It will display the image and a prediction statement, indicating if the cell is infected or not with malaria and the probability associated with this statement. 
* Table with image name and prediction results.
* Download button to download table.

### Page 5: ML Performance Metrics
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
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button "Open App" on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.

describe the content (such as text, plot, widgets etc)
when applicable, indicate the business requirement that a given page is answering.
