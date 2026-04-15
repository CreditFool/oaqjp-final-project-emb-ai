from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_input_iAmGladThisHappened_expect_joy(self):
        actual = emotion_detector("I am glad this happened")
        self.assertEqual(actual["dominant_emotion"], "joy")

    def test_input_iAmReallyMadAboutThis_expect_anger(self):
        actual = emotion_detector("I am really mad about this")
        self.assertEqual(actual["dominant_emotion"], "anger")

    def test_input_iFeelDisgustedJustHearingAboutThis_expect_disgust(self):
        actual = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(actual["dominant_emotion"], "disgust")
    
    def test_input_iAmSoSadAboutThis_expect_sadness(self):
        actual = emotion_detector("I am so sad about this")
        self.assertEqual(actual["dominant_emotion"], "sadness")

    def test_input_IAmReallyAfraidThatThisWillHappen_expect_sadness(self):
        actual = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(actual["dominant_emotion"], "fear")

unittest.main()