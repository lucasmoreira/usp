#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.sql import SQLContext
# $example on$
from pyspark.ml.classification import LogisticRegression
# $example off$

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: spark <file> <iterations>", file=sys.stderr)
		exit(-1)

	sc = SparkContext(appName="LGSpark")
	sqlContext = SQLContext(sc)

	# $example on$
	# Load training data
	training = sqlContext.read.format("libsvm").load(sys.argv[1])

	# Number of iterations
	iterations = int(sys.argv[2])

	lr = LogisticRegression(maxIter=iterations, regParam=0.3, elasticNetParam=0.8)

	# Fit the model
	lrModel = lr.fit(training)

	# Print the coefficients and intercept for logistic regression
	print("Coefficients: " + str(lrModel.coefficients))
	print("Intercept: " + str(lrModel.intercept))
	# $example off$

	sc.stop()