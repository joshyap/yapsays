# Python tweet bot with tweepy and AWS Lambda 

You can view this project in action by checking out the [@yapsays](https://twitter.com/yapsays) bot on twitter.

This bot runs off of an AWS Lambda function that runs on a timer. The timer is really just an AWS CloudWatch trigger that runs every 4 hours. This was all set up using AWS free tier account constraints and was a fun little developer project. 

You can read more about the experience and project on my corresponding [blog post](https://joshyap.dev/blog/serverless-python-twitter-bot).