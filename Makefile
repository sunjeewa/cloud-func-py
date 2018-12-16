topic:
	gcloud pubsub topics create jobs

deploy:
	gcloud functions deploy pubsubpy --runtime python37 --trigger-topic jobs 

