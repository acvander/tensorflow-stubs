import tensorflow as tf

tf.train.import_meta_graph(12345)  # E: incompatible type
tf.train.import_meta_graph([])  # E: incompatible type

tf.train.Saver().restore(tf.Session(), 12345)  # E: incompatible type
