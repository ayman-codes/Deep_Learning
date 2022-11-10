import numpy as np


class Activation:
    def __call__(self, x: np.ndarray, derivative: bool = False) -> np.ndarray:
        if not derivative:
            return self._normal(x)
        else:
            return self._derivate(x)

    @staticmethod
    def _normal(x: np.ndarray):
        raise NotImplementedError

    @staticmethod
    def _derivate(x: np.ndarray):
        raise NotImplementedError


class Tanh(Activation):
    @staticmethod
    def _normal(x: np.ndarray):
        return np.tanh(x)

    @staticmethod
    def _derivate(x: np.ndarray):
        return 1 - np.tanh(x) ** 2


class Sigmoid(Activation):
    @staticmethod
    def _normal(x: np.ndarray):
        return 1/(1+np.exp(-x))

    @staticmethod
    def _derivate(x: np.ndarray):
        return Sigmoid._normal(x) * (1 - Sigmoid._normal(x))

class Leaky_ReLu(Activation):
    @staticmethod
    def _normal(x: np.ndarray):
        return x*0.01 if x < 0 else x

    @staticmethod
    def _derivate(x: np.ndarray):
        return 0.01 if x < 0 else 1

class ReLU(Activation):
    @staticmethod
    def _normal(x: np.ndarray):
        if (x > 0).any():
            return x
        else:
            return 0

    @staticmethod
    def _derivate(x: np.ndarray):
        data = [1 if (value>0).any() else 0 for value in x]
        return np.array(data, dtype=float)



