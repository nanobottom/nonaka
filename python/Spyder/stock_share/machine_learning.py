# -*- coding: utf-8 -*-
import tflearn, datetime
import matplotlib.pyplot as plt
import numpy as np
from stock_share import StockShare
from tensorflow import reset_default_graph
reset_default_graph()

class MachineLearning:
    #datasetはlistにする
    def __init__(self, dataset):
        dataset = np.array(dataset)#listをnumpy.ndarrayに変換する
        self.dataset = dataset.astype("float32")
        #いくつ前のデータまでを学習に用いるか、のフレーム
        #教師信号はstep_in_future日分の株価となる
        self.steps_of_history = 15
        #いくつ先(一日分）のデータを予測するか
        self.steps_in_future = 1
        
        self.train_data_ratio = 0.8
        self.epoch = 50
        
        self.dataset_x = None
        self.dataset_y = None
        self.train_x = None
        self.train_y = None
        self.test_x = None
        self.model = None
        self.train_predict = None
        self.test_predict = None
        
        
    def normalization_zero_one(self, axis = None):
        min = self.dataset.min(axis = axis, keepdims = True)
        max = self.dataset.max(axis = axis, keepdims = True)
        self.dataset = (self.dataset - min) / (max - min)
        
    def create_dataset_x_y(self):
        dataset_x, dataset_y = [], []
        for i in range(0, len(self.dataset) - self.steps_of_history, self.steps_in_future):
            dataset_x.append(self.dataset[i:i + self.steps_of_history])
            dataset_y.append(self.dataset[i + self.steps_of_history])
        
        self.dataset_x = np.reshape(np.array(dataset_x), [-1, self.steps_of_history, 1])
        self.dataset_y = np.reshape(np.array(dataset_y), [-1, 1])
    
    def split_train_test(self):
        pos = round(len(self.dataset_x) * self.train_data_ratio)
        self.train_x, self.train_y = self.dataset_x[:pos], self.dataset_y[:pos]
        self.test_x, test_y        = self.dataset_x[pos:], self.dataset_y[pos:]
        
    def setup(self):
        # Build neural network
        # 入力層
        net = tflearn.input_data(shape=[None, self.steps_of_history, 1])

        # LSTMは時間かかるのでGRU
        # 隠れ層
        net = tflearn.gru(net, n_units=6)
        # dropoutを入れると過学習を防いでくれる
        net = tflearn.dropout(net, 0.9995, name = "dropout_1")

        # 出力層
        net = tflearn.fully_connected(net, 1, activation='linear')

        # 回帰の設定、Adam法で測定
        # 時系列分析での予測精度の指標にmean_squareを使っている
        # mapeが一般的なようだ
        # mean_square : 二乗平均平方根
        net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                loss='mean_square')
        # Define model
        self.model = tflearn.DNN(net, tensorboard_verbose=0)
    
    def setup2(self):
        # 隠れ層のノード数
        nunit = 10
        # dropの比率
        drop_rate = 0.9995
        # 入力層
        net = tflearn.input_data(shape = [None, self.steps_of_history, 1], name = "input_layer")
        # 隠れ層（１層目）
        # 活性化関数にはReLUを用いる
        net = tflearn.lstm(net, n_units = nunit, activation = 'relu', name = "hidden_layer_1"
                           ,return_seq = True, return_state = False)
        # dropoutを入れると過学習を防いでくれる
        net = tflearn.dropout(net, drop_rate, name = "dropout_1")
        # 隠れ層（２層目）
        net = tflearn.lstm(net, n_units = nunit, activation = 'relu', name = "hidden_layer_2"
                           ,return_seq = True, return_state = False)
        net = tflearn.dropout(net, drop_rate, name = "dropout_2")
        # 隠れ層（3層目）
        net = tflearn.lstm(net, n_units = nunit, activation = 'relu', name = "hidden_layer_3"
                           ,return_seq = False, return_state = False)
        net = tflearn.dropout(net, drop_rate, name = "dropout_3")
        # 出力層
        net = tflearn.fully_connected(net, 1, activation = 'linear', name = "output_layer")
        # モデルの作成
        net = tflearn.regression(net, optimizer = "adam", learning_rate = 0.001, loss = "mean_square")
        self.model = tflearn.DNN(net, tensorboard_verbose = 0, tensorboard_dir = "log")
        
        
    def execute_predict(self):
        # Start training (apply gradient descent algorithm)
        self.model.fit(self.train_x, self.train_y, validation_set=0.1, show_metric=False, batch_size=1, n_epoch=self.epoch)

        # predict
        self.train_predict = self.model.predict(self.train_x)
        self.test_predict = self.model.predict(self.test_x)

    def show_result(self):
        """
        # plot train data
        train_predict_plot = np.empty_like(self.dataset)
        train_predict_plot[:, :] = np.nan
        train_predict_plot[self.steps_of_history:len(self.train_predict) + self.steps_of_history, :] = \
                self.train_predict

        # plot test data
        test_predict_plot = np.empty_like(self.dataset)
        test_predict_plot[:, :] = np.nan
        test_predict_plot[len(self.train_predict) + self.steps_of_history:len(self.dataset), :] = \
                self.test_predict
        """

        # plot show res
        plt.figure(figsize=(8, 8))
        plt.title('History={} Future={}'.format(self.steps_of_history, self.steps_in_future))
        plt.plot(self.dataset, label="actual", color="k")
        plt.plot(range(self.steps_of_history, self.steps_of_history + len(self.train_predict)), self.train_predict, label="train", color="r")
        plt.plot(range(self.steps_of_history + len(self.train_predict), self.steps_of_history + len(self.train_predict) + len(self.test_predict)), self.test_predict, label="test", color="b")
        #plt.savefig('result.png')
        plt.show()
        

if __name__ == "__main__":
    
    today = datetime.date.today()
    code = 3849
    # 株価（終値）を取得する 
    stock_share = StockShare(code, end_date = today.strftime("%Y-%m-%d"), term = 300)
    stock_share.get_stock_data()
    ml = MachineLearning(stock_share.ohcl["close"])
    #LSTMは入力値を0~1に正規化しておくと安定した出力が得られる
    ml.normalization_zero_one()
    print(ml.dataset)
    ml.create_dataset_x_y()
    print("dataset_x")
    print(ml.dataset_x)
    print("dataset_y")
    print(ml.dataset_y)
    ml.split_train_test()
    ml.setup2()
    ml.execute_predict()
    ml.show_result()
