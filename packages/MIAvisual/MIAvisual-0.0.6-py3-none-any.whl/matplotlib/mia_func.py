#!/usr/bin/env python
# coding: utf-8

# In[11]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

def plot_roc_curve(test_y, prob,n=2):
    if(n>2):
        fpr = dict()
        tpr = dict()
        thr = dict()
        roc_auc = dict()
        for i in range(n):
            fpr[i], tpr[i], thr[i] = roc_curve(test_y[:,i], prob[:,i])
        plt.figure(figsize=(30, 15))
        a=1
        for idx, i in enumerate(range(n)):     
            plt.subplot(2,2,idx+1)
            plt.plot(fpr[i], tpr[i],color='red', label='ROC ')
            plt.plot([0, 1], [0, 1], color='green', linestyle='--')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Class %0.0f : Roc auc score: %f'%(idx,roc_auc_score(test_y[:,i], prob[:,i])))
            plt.legend()
        plt.show()

    else:
        
        fpr, tpr, thr = roc_curve(test_y, prob)
        plt.plot(fpr, tpr, color='red', label='ROC')
        plt.plot([0, 1], [0, 1], color='green', linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Roc auc score: %f'%(roc_auc_score(test_y, prob)))
        plt.legend()
        plt.show()

#--------------------------------------------------------------
def plot_feature_importance(model, X, y = None,top_n=10):
        ft_importance_values = model.feature_importances_

        # 정렬과 시각화를 쉽게 하기 위해 series 전환
        ft_series = pd.Series(ft_importance_values, index = X.columns)
        ft_top=ft_series.sort_values(ascending=False)[:top_n]
        # 시각화
        plt.figure(figsize=(8,6))
        plt.title('Feature Importance Top 20')
        sns.barplot(x=ft_top, y=ft_top.index)
        plt.show()
#--------------------------------------------------------------      
class SingleLayer:
    
    def __init__(self, learning_rate=0.1, l1=0, l2=0):
        self.w = None
        self.b = None
        self.losses = []
        self.val_losses = []
        self.w_history = []
        self.lr = learning_rate

    def forpass(self, x):
        z = np.sum(x * self.w) + self.b    # 직선 방정식을 계산합니다
        return z

    def backprop(self, x, err):
        w_grad = x * err          # 가중치에 대한 그래디언트를 계산합니다
        b_grad = 1 * err    # 절편에 대한 그래디언트를 계산합니다
        return w_grad, b_grad

    def activation(self, z):
        z = np.clip(z, -100, None) # 안전한 np.exp() 계산을 위해
        a = 1 / (1 + np.exp(-z))  # 시그모이드 계산
        return a
        
    def fit(self, x, y, epochs=100, x_val=None, y_val=None):
        self.w = np.ones(x.shape[1])               # 가중치를 초기화합니다.
        self.b = 0                                 # 절편을 초기화합니다.
        self.w_history.append(self.w.copy())       # 가중치를 기록합니다.
        np.random.seed(42)                         # 랜덤 시드를 지정합니다.
        for i in range(epochs):                    # epochs만큼 반복합니다.
            loss = 0
            # 인덱스를 섞습니다
            indexes = np.random.permutation(np.arange(len(x)))
            for i in indexes:                      # 모든 샘플에 대해 반복합니다
                z = self.forpass(x.iloc[i])             # 정방향 계산
                a = self.activation(z)             # 활성화 함수 적용
                err = -(y.iloc[i] - a)                  # 오차 계산
                w_grad, b_grad = self.backprop(x.iloc[i], err) # 역방향 계산
                # 그래디언트에서 페널티 항의 미분 값을 더합니다
                self.w -= self.lr * w_grad         # 가중치 업데이트
                self.b -= b_grad                   # 절편 업데이트
                # 가중치를 기록합니다.
                self.w_history.append(self.w.copy())
                # 안전한 로그 계산을 위해 클리핑한 후 손실을 누적합니다
                a = np.clip(a, 1e-10, 1-1e-10)
                loss += -(y.iloc[i]*np.log(a)+(1-y.iloc[i])*np.log(1-a))
            # 에포크마다 평균 손실을 저장합니다
            self.losses.append(loss/len(y))
            # 검증 세트에 대한 손실을 계산합니다
            self.update_val_loss(x_val, y_val)
    
    def predict(self, x):
        z = [self.forpass(x_i) for x_i in x]     # 정방향 계산
        return np.array(z) >= 0                   # 스텝 함수 적용
    
    def score(self, x, y):
        return np.mean(self.predict(x) == y)
    
    def reg_loss(self):
        return self.l1 * np.sum(np.abs(self.w)) + self.l2 / 2 * np.sum(self.w**2)
    
    def update_val_loss(self, x_val, y_val):
        if x_val is None:
            return
        val_loss = 0
        for i in range(len(x_val)):
            z = self.forpass(x_val[i])     # 정방향 계산
            a = self.activation(z)         # 활성화 함수 적용
            a = np.clip(a, 1e-10, 1-1e-10)
            val_loss += -(y_val[i]*np.log(a)+(1-y_val[i])*np.log(1-a))
        self.val_losses.append(val_loss/len(y_val) + self.reg_loss())
        
    def update_visual(self):
        weight = []
        cnt = []
        for i, w in enumerate(self.w_history[1:]):
            weight.append(w[w.index[1]])
            cnt.append(i)
        plt.plot(cnt, weight)
        plt.plot(cnt[-1], weight[-1], 'ro')
        plt.xlabel("epoch")
        plt.ylabel(self.w_history[1].index[1])
        plt.show()
#--------------------------------------------------------------------
def plot_layer_history(layer):
    w2=[]
    w3=[]
    for w in layer.w_history:
        w2.append(w[2])
        w3.append(w[3])
    plt.plot(w2, w3)
    plt.plot(w2[-1], w3[-1], 'ro')
    plt.xlabel('w[2]')
    plt.ylabel('w[3]')
    plt.show()
    




