## TITLE: TANZANIA WATER WELL PUMP STATUS PREDICTION
### OVERVIEW
In Tanzania, the history of water supply has been a dynamic interplay of geographical, social, and economic factors. Initially blessed with abundant water resources, the country encountered challenges in distributing water efficiently. To address this, a proactive initiative has emerged. By analyzing historical data on pump functionality, geography, maintenance, and local demographics, this project aims to predict potential pump issues. Its goal is to create a scalable predictive tool aiding decision-makers. This tool not only optimizes resource allocation and maintenance but also engages communities. Through partnerships and qualitative data integration, it seeks to blend data-driven insights with community perspectives. Ultimately, this holistic approach aims to improve water infrastructure management sustainably while fostering community empowerment in Tanzania.

In Tanzania, water supply history intertwines geography, society, and economics. Despite abundant resources, efficient distribution posed challenges. Addressing this, a project analyzes pump data to predict issues, aiding decision-makers in resource allocation and maintenance. Beyond predictive analytics, it prioritizes community engagement, integrating qualitative data for a holistic, participatory approach to sustainable water infrastructure management.
## Challenges
In a developing country like Tanzania, ensuring clean and accessible piped water faces numerous challenges. Some of these challenges include:
1.`Infrastructure Deficiency`: Many areas lack the necessary infrastructure for piped water systems. Remote or rural areas might not have pipelines or water treatment facilities, making it difficult to distribute clean water to these regions.


2.`Limited Access to Technology`: Developing countries may face limitations in accessing advanced technology for water treatment and distribution.


3.`Financial Constraints`: Funding constraints often limit the government's ability to invest in water infrastructure and maintenance.


4.`Population Growth`: Rapid population growth strains existing water resources and infrastructure. As urbanization increases, the demand for water rises, putting pressure on already limited water sources and distribution systems.


5 `Poor Maintenance`: Existing water infrastructure might suffer from poor maintenance due to a lack of resources or skilled personnel.
## Proposed solutions
1.Build a predictive machine learning model that predicts whether a pump is functional , not functional or functioning but needs repair in orde to reduce water shortage due to failure of pumps


2.Identify features or properties that lead to these water related problems and adress them


3.Identify regions that suffer most from these challenges so we can have a map or ways on how to improve their status.


4.Investigate whether the infrastructure available is enough to meet the people's need 
### PROBLEM STATEMENT
The provision of clean and sustainable water access remains a critical challenge in Tanzania, with a vast network of water pumps serving communities across the country. However, the operational status of these pumps fluctuates, leading to intermittent water supply and hindering communities' access to safe drinking water. This project addresses the pressing need to develop a robust machine learning classification model capable of accurately predicting the operational status of water pumps in Tanzania.

The project scope focuses on harnessing historical data encompassing pump functionality, geographical features, maintenance records, and regional demographics to train and validate a predictive model. The objective is to accurately classify water pumps into different status categories, including 'functional,' 'functional needs repair,' and 'non-functional.' A successful model will enable stakeholders and decision-makers to anticipate potential pump failures or maintenance requirements proactively, thus optimizing resource allocation, reducing downtime, and ensuring sustained water access for Tanzanian communities.
# GOALS AND OBJECTIVE
General objective;
The main objective is to build and train a machine learning model to help us predict if water pumps installed in water points are functioning, not functional or working but needs repair.
Specific objectives

Use exploratory analysis to visually understand and understand what the data is communicating and also try to understand relationship between our data columns
# DATA UNDERSTANDING AND ANALYSIS
Data understanding involves comprehending the dataset's structure, contents, and potential insights, examining features and their relationships to extract valuable information for analysis or modeling purposes.

-`Source` - The dataset originates from Taarifa, a platform collecting reports on infrastructure and services, particularly focused on water points. This data was compiled by GeoData company limited.

-`Components`- This dataset consists of 59400 rows and 41 columns of data.
# DATA PREPARATION
There we many columns that had similar data or almost related data so I studied them one by one and dropped those seemd irrelevant or duplicates to other columns

I also deal with missing values where i used an imputer to fill the values. Since it was categorical I imputed with the most frequent one(mode)

There were a few outliers and I was able to sort that using the interquartile range clipping.The plot below shows behavior after clipping(left plot) and before clipping(right_plot)
![Alt text](image.png)
### Our status_group(Target class)
Our target group has three classes and below is their distribution
![Alt text](image-1.png)
### Univariate exploratory analysis
#### Region
The following are the regions under study or from where our problem data was collected
![Alt text](image-2.png)
#### Water basins in Tanzania
The water basins geographically located in Tanzania are nine in total. Lake Victoria is the largest in terms of body mass and Lake Rukwa holds the last position
![Alt text](image-3.png)
#### Management groups
The management columns tells us about the people incharge of running the water wells located in Tanzania. Most water wells in Tanzania are managed by the Village Water Community(VWC). This makes a lot of sense sinse Tanzania is a communist country. School and trust hold the least share for the water well management.
The abbreviations of the values are explained here;
  1. VWC - Village Water Community 
  2. WUG - Water User Group
  3. WUA - Water User Association
Both WUG and WUA are mainly involved in activities such as irrigation, maintaining water infrastructure, resolving issues related to water usage among other things
![Alt text](image-4.png)
#### Payment methods
The means of payment for water in Tanzania has seven unique modes of payment. Most of the water wells are free and no charges are needed to access water. This is what the plot says as we can see most common mode of payment is "never pay". Our other plots on management concur with this as we can see most water wells are managed by the village community
![Alt text](image-5.png)
#### Water quality
In terms of water quality, Tanzania is blessed with soft water. Soft water generally contains low concentrations of minerals like calcium and magnesium, leading to fewer issues related to limescale buildup in pipes and appliances. In Tanzania, having soft water can contribute to reduced instances of scale accumulation in plumbing systems and appliances, potentially minimizing maintenance and extending the lifespan of water-related infrastructure. 
### Multi-variate analysis
#### Distribution of pumps in Tanzania
 From the scatter plot we can say that the pumps status across the region is almost even. The functional class is the highest followed by the non functional class and the ones that function but need repair are significantly low. The white spaces can be accounted as large water bodies such as lakes within the region
 ![Alt text](image-6.png)
 #### Relationship betweeen Status group and region
 Iringa region is the region with the most functioning pumps. Mbeya and Shinyanga regions are leading in pumps that are not functioning.
Kigoma, Shinyanga and Kigoma also have highest number of pumps that need repair.
![Alt text](image-7.png)
#### Relationship betweeen Status group and management
Village Water Community managed wells have the highest number of functioning, non function and functioning but needs repair. This can indicate that some communities are best at managing their well's infrastructure and some of them don't know how to manage their water well
![Alt text](image-8.png)
#### Relationship betweeen Status group and waterquality
Soft water is the most used water in Tanzania as we can see it has the highest count of all three classes of the status group
![Alt text](image-9.png)
#### Relationship betweeen Status group and payment_type
The neverpay water wells have the highest number of non functional pumps which can indicate lack of funds to repair the broken pumps in the region.
![Alt text](image-10.png)

## MODELLING
The purpose of this notebook is to create various models and try and determine which one works best for the project task. As well as trying various models, I will also experiment with different features and perform feature engineering to try and get the best predictors. As I go through this process I will try and explore the data further and continue with EDA while in the process since it is an iterative process
In this chapter I am going to build machine learning models to help us classify whether pumps in Tanzania are function, not function or functioning and needs repair. This is a ternary problem meaning we have three target classes
### TRANSFORMING DATA SETS AND SCALING
I transfromed categorical values into numerical values using the onehotencode technique so our models could train on it. Since classifiers only works with O'sand 1's I scaled the numeric columns so they could fall within the same scale(0, 1)
### Selecting a model
There are several algorithms for classification problems but these are the ones I used in my model;
1. LogisticRegression

2. LogisticRegressionCV-cross validate

3. DecisionTreeClassifieer

4.RandomForestClassifier

5. GradientBoosting

6 XGBoost classifier
### Model Evaluation and selection
For the models build, I used the followwing metrics to evaluate to determine which one was working or performing well without underfitting or overfitting; accuracy score, precision, and recall. The best performing model was 
### Limitations
There were a few challenges between the process and are as follows'
1. Low computational power to build the models and this affected testing and evaluating process as the process of building took so long

2. A lot of dirty work to clean in the dataset. The dataset had outliers, missing values and outliers and this consumed almost all of my time on analysis.

3. There was an issue with class imbalance in the target group and had to employ techniques like weights and synthetic to curb the problem
### Conclusion
### Recommendations
### Next step
1. Deploy our model into use to see how it will perform in the business world.

2. Improve on computational power in order to analyze data with ease


