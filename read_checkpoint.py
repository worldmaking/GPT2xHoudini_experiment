import os
from pprint import pprint
import tensorflow as tf 

tf_path = os.path.abspath('models/117M/model.ckpt')
tf_vars = tf.train.list_variables(tf_path)
pprint(tf_vars)