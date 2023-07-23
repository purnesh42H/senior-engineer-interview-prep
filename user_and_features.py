from collections import defaultdict
import unittest

'''
Given a series of users and features, complete the function that returns features for a user id

stream = [["user1": "feature1", "user1": "feature2", "user2": "feature1", "user3": "feature3"]]

get_user_feaatures("user1") => ["feature1", "feature2"]
'''

class UserFeature(object):
    def __init__(self, stream):
        self.stream = stream
        self.user_feature_map = defaultdict(set)

    def get_user_features(self, user_id):
        if not self.user_feature_map:
            self._build_feature_map(self.stream)
        
        if user_id not in self.user_feature_map:
            return []
        
        return list(self.user_feature_map[user_id])

    def _build_feature_map(self, stream):
        for (user, feature) in stream:
            self.user_feature_map[user].add(feature)

class UserFeatureTest(unittest.TestCase):

    def test_get_user_features(self):
        user_feature = UserFeature([["user1", "feature1"], ["user1", "feature2"], ["user2", "feature1"], ["user3", "feature3"]])

        user1_features = user_feature.get_user_features("user1")
        self.assertEqual(2, len(user1_features))
        self.assertTrue("feature1" in user1_features)
        self.assertTrue("feature2" in user1_features)

        user2_features = user_feature.get_user_features("user2")
        self.assertEqual(1, len(user2_features))
        self.assertTrue("feature1" in user2_features)

        user3_features = user_feature.get_user_features("user3")
        self.assertEqual(1, len(user3_features))
        self.assertTrue("feature3" in user3_features)

        user3_features = user_feature.get_user_features("user4")
        self.assertEqual(0, len(user3_features))

if __name__ == "__main__":
    unittest.main()
        