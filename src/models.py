from sklearn.linear_model import LinearRegression
class LinearRegressionCustom(LinearRegression):
    def __init__(self):
        super(LinearRegressionCustom(), self).__init__()
    def fit(self):
        return self.fit()