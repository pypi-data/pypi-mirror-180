import torch
import torch.nn as nn
from pymic.loss.seg.abstract import AbstractSegLoss

class MSELoss(AbstractSegLoss):
    """
    Mean Sequare Loss for segmentation tasks.
    The parameters should be written in the `params` dictionary, and it has the
    following fields:

    :param `loss_softmax`: (bool) Apply softmax to the prediction of network or not. 
    """
    def __init__(self, params = None):
        super(MSELoss, self).__init__(params)
            
    def forward(self, loss_input_dict):
        predict = loss_input_dict['prediction']
        soft_y  = loss_input_dict['ground_truth']
        
        if(isinstance(predict, (list, tuple))):
            predict = predict[0]
        if(self.softmax):
            predict = nn.Softmax(dim = 1)(predict)
        mse  = torch.square(predict - soft_y)
        mse  = torch.mean(mse) 
        return mse 
    
    
class MAELoss(AbstractSegLoss):
    """
    Mean Absolute Loss for segmentation tasks.
    The arguments should be written in the `params` dictionary, and it has the
    following fields:

    :param `loss_softmax`: (bool) Apply softmax to the prediction of network or not. 
    """
    def __init__(self, params = None):
        super(MAELoss, self).__init__(params)
    
    def forward(self, loss_input_dict):
        predict = loss_input_dict['prediction']
        soft_y  = loss_input_dict['ground_truth']
        
        if(isinstance(predict, (list, tuple))):
            predict = predict[0]
        if(self.softmax):
            predict = nn.Softmax(dim = 1)(predict)
        mae = torch.abs(predict - soft_y)
        mae = torch.mean(mae)
        return mae 
