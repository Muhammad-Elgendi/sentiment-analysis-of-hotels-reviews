# -*- coding: utf-8 -*-
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import csv
import pickle

class SentimentAnalyser:

    def extract_features(self,review):
        word_list = review.split()
        return dict([(word,True) for word in word_list])

    def train(self):
        csv_file = open('hotelsReviews.csv')
        csv_reader = csv.reader(csv_file, delimiter=',')
        goodReviews = []
        neutralReviews = []
        badReviews = []
        for index, row in enumerate(csv_reader):
            if index != 0:
                if row[1] == '1':
                    goodReviews.append(row)
                elif row[1] == '0':
                    neutralReviews.append(row)
                elif row[1] == '-1':
                    badReviews.append(row)
        # separate reviews into positive , neutral and negative features
        features_positive = [(self.extract_features(review[0]), 'Positive')
                         for review in goodReviews]
        features_negative = [(self.extract_features(review[0]), 'Negative')
                         for review in badReviews]
        features_neutral = [(self.extract_features(review[0]), 'Neutral')
                        for review in neutralReviews]
        # Split the dataset into training and testing datasets (80/20)
        threshold_factor = 0.8
        threshold_positive = int(threshold_factor * len(features_positive))
        threshold_negative = int(threshold_factor * len(features_negative))
        threshold_neutral = int(threshold_factor * len(features_neutral))
        # Extract the features
        features_train = features_positive[:threshold_positive] + \
            features_negative[:threshold_negative] + \
            features_neutral[:threshold_neutral]

        # features_test = features_positive[threshold_positive:] + \
        #     features_negative[threshold_negative:] + \
        #     features_neutral[threshold_neutral:]
        # use a Naive Bayes classifier and train it
        classifier = NaiveBayesClassifier.train(features_train)
        # dump classifier into a file
        f = open('classifier.pickle', 'wb')
        pickle.dump(classifier, f)
        f.close()

    def test(self,review):
        f = open('classifier.pickle', 'rb')  
        classifier = pickle.load(f)
        f.close()
        probdist = classifier.prob_classify(self.extract_features(review))
        predected_sentiment = probdist.max()
        probability = round(probdist.prob(predected_sentiment), 2)
        return predected_sentiment, probability