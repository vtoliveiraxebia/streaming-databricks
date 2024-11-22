# Moving from batch to streaming ML on databricks

The idea is to create an end-to-end streaming application on databricks using best practices and tools available such as: Spark StructuredStreaming, FeatureStore, Unity Catalog, DABs, MLFlow, etc.
The project will consist then of ingesting streaming data, computing features in near real-time, training model offline, and predicting using model serving / or an API.

Part of the challenges we see in streaming applications are:
 - How to avoid train-serve skew.
 - Feature computation times
 - How to set up infrastructure to prevent failures and how to recover
 - How to ingest streaming data to be resusable across multiple projects

We can initially think of simpler cases and then increase complexity:

## 1. Batch Architecture
	a. Creating a Feature Engineering pipeline from batch data.
	b. Train model using Feature Store
	c. Predict using model serving or a predict pipeline using feature store

This one works well because we are completely avoiding train-serve skew since features are computed from a single, unified feature engineering pipeline.

## 2. Streaming pipelines
    a. Creating a Feature Engineering pipeline from streaming events.
    c. Train model using Feature Store
    d. Predict using model serving or a predict pipeline using feature store.
    5. Set up a online DB for Online data retrieval



This ones adds complexity because we are processing our data in a streaming fashion and we need to set up an online DB (either natively in databricks or a custom one). I would like to understand alternatives in this case if we want to use a different vendor (Redis) for setting up the online database and explore how fast sparkStucturedStreaming and feature / prediction update would be.

## Requirements

We need first to decide on a few topics to start working:

 - A dataset which we can use to simulate streaming events.
   - [Maybe eventsim](https://github.com/Interana/eventsim)
   - Dynamic pricing datasets could be a nice use case as well
 - Infra on databricks with workspace, unity catalog enabled to set up all project's resources
